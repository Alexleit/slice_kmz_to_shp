# -*- coding: utf-8 -*-
# Geógrafo Alexandre Leite de Araújo | Geophocus Consultoria
# Extração e exportação de todas as camadas de um KMZ/KML e salva cada uma como shapefile reprojetado


import os, zipfile # as bibliotecas padrão, não necessitará instalar nenhum módulo
from qgis.core import (
    QgsVectorLayer,
    QgsProviderRegistry,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsProject,
    QgsVectorFileWriter
)

#CONFIGURE O CAMINHO DO SEU ARQUIVO KMZ E UMA PASTA CHAMADA 'EXPORTADOS' SERÁ CRIADA ONDE OS SHAPES IRÃO SER SALVOS
kmz_path = r"seucaminho deve estar entre estas aspas\seu_arquivo.kmz"
export_folder = os.path.join(os.path.dirname(kmz_path), "EXPORTADOS")

if not os.path.exists(export_folder):
    os.makedirs(export_folder)

target_crs = QgsCoordinateReferenceSystem("EPSG:31984")  # AQUI VOCÊ ALTERA SEUC CÓDIGO EPSG - este é para SIRGAS200/24S
project = QgsProject.instance()

# AQUI O KMZ É DESCOMPACTADO
if kmz_path.lower().endswith(".kmz"):
    with zipfile.ZipFile(kmz_path, "r") as z:
        for f in z.namelist():
            if f.lower().endswith(".kml"):
                kml_path = os.path.join(export_folder, os.path.basename(f))
                z.extract(f, export_folder)
                os.rename(os.path.join(export_folder, f), kml_path)
                print(f" Extraído: {kml_path}")
                break
else:
    kml_path = kmz_path

#AS CAMADAS SERÃO LISTADAS E AVISADAS SOBRE ALGUM POSSÍVEL ERRO DE EXTRAÇÃO
provider = QgsProviderRegistry.instance()
sublayers = provider.querySublayers(kml_path)  # sem segundo argumento

if not sublayers:
    raise Exception("Nenhuma subcamada encontrada dentro do KML/KMZ.")

print(f"🔹 {len(sublayers)} camadas encontradas dentro do arquivo.")

# A EXPORTAÇÃO
for sub in sublayers:
    name = sub.name()
    uri = f"{kml_path}|layername={name}"
    layer = QgsVectorLayer(uri, name, "ogr")

    if not layer.isValid():
        print(f" Falha ao carregar camada: {name}")
        continue

    print(f" Exportando: {name}")

    source_crs = layer.crs()
    transform = QgsCoordinateTransform(source_crs, target_crs, project)

    shp_name = f"{name.replace(' ', '_')}_SIRGAS2000_UTM24S.shp" #NOTE QUE JÁ SAEM RENOMEADAS,SE NÃO FOR NECESSÁRIO APAGUE O QUE VEM DEPOIS DO ULTIMO COLCHETE
    shp_path = os.path.join(export_folder, shp_name)

    writer = QgsVectorFileWriter(
        shp_path,
        "UTF-8",
        layer.fields(),
        layer.wkbType(),
        target_crs,
        "ESRI Shapefile"
    )

    for feat in layer.getFeatures():
        geom = feat.geometry()
        geom.transform(transform)
        new_feat = feat
        new_feat.setGeometry(geom)
        writer.addFeature(new_feat)
    del writer

    QgsProject.instance().addMapLayer(QgsVectorLayer(shp_path, shp_name, "ogr"))
    print(f"   ✔ Salvo: {shp_name}")

print("\n VOILÀ! Exportação concluída!")
print(f" Pasta de saída: {export_folder}")
print(" Sistema: SIRGAS 2000 / UTM 24S (EPSG: 31984)")
