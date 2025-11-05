# 🗺️ slice_kmz_to_shp

**Conversor automático de arquivos KMZ/KML em shapefiles reprojetados**  
Desenvolvido por **Geógrafo Alexandre Leite de Araújo | Geophocus Consultoria e Serviços**
+55 85 99135-5489

![Badge QGIS](https://img.shields.io/badge/QGIS-3.40_LTR-green?style=flat-square)
![Badge Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Badge License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

---

## 📘 Sobre o projeto

**slice_kmz_to_shp** é um script desenvolvido em **PyQGIS (Python para QGIS)** que converte arquivos **KMZ ou KML** em **shapefiles separados**, mantendo cada camada ("folder" ou "placemark") em um arquivo `.shp` independente.

Durante o processo, todas as geometrias são automaticamente **reprojetadas para SIRGAS 2000 / UTM Zona 24S (EPSG: 31984)**, atendendo aos padrões geodésicos e cartográficos brasileiros.

Ideal para **projetos topográficos, ambientais e de mineração**, nos quais há necessidade de compatibilidade entre dados do Google Earth e SIG profissionais.

---

## ⚙️ Funcionalidades

✅ Extrai e converte automaticamente todos os layers internos de um `.kmz`  
✅ Cria shapefiles independentes para cada camada/folder  
✅ Reprojeta automaticamente para **SIRGAS 2000 / UTM 24S (EPSG:31984)**  
✅ Compatível com **QGIS 3.40 LTR**  
✅ Nenhuma dependência externa (usa apenas módulos nativos `os` e `zipfile`)  
✅ Adiciona automaticamente os shapefiles exportados ao projeto QGIS  

---

## 🚀 Como usar

1. Abra o **QGIS 3.40 LTR**  
2. Vá em **Processamento → Caixa de Ferramentas → Scripts → Novo Script**  
3. Cole o conteúdo do arquivo `slice_kmz_to_shp.py`  
4. Ajuste o caminho do arquivo `.kmz` e execute o script  

🗂️ Os shapefiles resultantes serão salvos automaticamente em uma pasta chamada **`EXPORTADOS`** no mesmo diretório do arquivo original.

---

## 📂 Estrutura típica de saída

