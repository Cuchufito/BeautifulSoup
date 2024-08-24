url = "https://www.worldometers.info/world-population/population-by-country/"

# Realizar la solicitud HTTP y obtener el contenido de la página
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, features="html.parser")















#Crea la ruta completa del archivo Excel combinando el directorio y el nombre del archivo y guarda el DataFrame df_poblacion como un archivo Excel en la ubicación especificada
#y guarda el DataFrame df_poblacion como un archivo Excel en la ubicación especificada
archivo_salida = os.path.join(directorio, "datos.xlsx")
df_poblacion.to_excel(archivo_salida, index=None, header=True)


#Imprime un mensaje en la consola que indica la ubicación donde se guardaron los datos
print(f"Datos guardados en {archivo_salida}")