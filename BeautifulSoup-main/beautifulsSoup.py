import csv
#para manejar archivos Csv aunque en este caso no se utiliza#
import requests
#para realizar solicitudes HTTP, que es cómo se obtiene el contenido de una página web#
from bs4 import BeautifulSoup
#Para analizar el HTML de la página y extraer información específica#
import pandas as pd
#Para manipular datos tabulares de manera eficiente, como DataFrames#
from io import StringIO
#Para tratar cadenas de texto como si fueran archivos, útil para manipular datos en memoria#
import os
#Para interactuar con el sistema de archivos, como crear directorios o manejar rutas de archivos#


url = "https://www.worldometers.info/world-population/population-by-country/"

# Realizar la solicitud HTTP y obtener el contenido de la página
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, features="html.parser")




directorio = r"C:\\Users\\nahue\\Desktop\\Trabajo_Practico"
#Define la ruta donde se guardará el archivo Excel. La r antes de la cadena indica una "cadena cruda" donde las barras invertidas no se escapan#
if not os.path.exists(directorio):
# Verifica si el directorio ya existe#
    os.makedirs(directorio)
#Si el directorio no existe, lo crea#

#Crea la ruta completa del archivo Excel combinando el directorio y el nombre del archivo y guarda el DataFrame df_poblacion como un archivo Excel en la ubicación especificada
#y guarda el DataFrame df_poblacion como un archivo Excel en la ubicación especificada
archivo_salida = os.path.join(directorio, "datos.xlsx")
df_poblacion.to_excel(archivo_salida, index=None, header=True)


#Imprime un mensaje en la consola que indica la ubicación donde se guardaron los datos
print(f"Datos guardados en {archivo_salida}")
tabla_html = soup.find_all("table")[0]

Explicación:
soup.find_all("table"): Busca todas las etiquetas <table> en el documento HTML y las devuelve como una lista.
[0]: Selecciona la primera tabla en esa lista. Este código asume que la primera tabla es la que contiene la información de población que se necesita.

datos_html = StringIO(str(tabla_html))

Explicación:
str(tabla_html): Convierte la tabla HTML seleccionada en una cadena de texto.
StringIO(str(tabla_html)): Convierte esa cadena en un objeto StringIO, que permite tratar la cadena como si fuera un archivo, útil para leerlo directamente con pandas.

df_poblacion = pd.read_html(datos_html)[0]

Explicación:
pd.read_html(datos_html): pandas lee el "archivo" en memoria (el objeto StringIO) como una tabla (o DataFrame). read_html devuelve una lista de DataFrames porque podría haber más de una tabla en el HTML.
[0]: Selecciona el primer (y en este caso, único) DataFrame de la lista.
