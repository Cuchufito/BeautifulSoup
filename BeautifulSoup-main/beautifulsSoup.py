import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import os
# URL de la página web que contiene la tabla de población
url =
"https://www.worldometers.info/world-population/population-by-country/"
# Realizar la solicitud HTTP y obtener el contenido de la página
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, features="html.parser")
# Extraer la primera tabla encontrada en la página
tabla_html = soup.find_all("table")[0]
# Convertir la tabla HTML a un objeto StringIO
datos_html = StringIO(str(tabla_html))
# Leer la tabla desde el objeto StringIO como un DataFrame de pandas
df_poblacion = pd.read_html(datos_html)[0]
# Verificar si el directorio existe, si no, crearlo
directorio = r"C:\\Users\\nahue\\Desktop\\Trabajo_Practico"
if not os.path.exists(directorio):
    os.makedirs(directorio)
# Guardar el DataFrame como un archivo Excel en el directorio
especificado
archivo_salida = os.path.join(directorio, "datos.xlsx")
df_poblacion.to_excel(archivo_salida, index=None, header=True)
print(f"Datos guardados en {archivo_salida}")
