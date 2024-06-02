# importamos las librerías Python que utilizaremos:
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re
#Indicamos la ruta de la web que deseamos acceder:
# indicar la ruta
url_page = 'https://es.rollingstone.com/100-canciones-que-marcaron-el-2023/'
#hacer el request a esa ruta y procesamos el HTML mediante un objeto de tipo BeautifulSoap:
# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, features="html.parser")
#pensar la estrategia para acceder al valor
# Obtenemos la tabla por un ID específico
tabla = soup.findAll('strong')

#crear el archivo para guardar los datos
with open('datos.csv', 'w')as archivo:
    for fila in tabla:
        listaResultado = re.split("<strong>+",str(fila))
        listaResultado = re.split("</strong>", listaResultado[1])
        listaResultado = re.split("\xa0", listaResultado[0])
        listaResultado[0] = listaResultado[0].replace("&amp;", "&")
        linea = "{0},{1}"
        linea = linea.format(listaResultado[0],"\n")
        print(linea)
        archivo.write(linea)