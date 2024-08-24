url = "https://www.worldometers.info/world-population/population-by-country/"

# Realizar la solicitud HTTP y obtener el contenido de la página
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, features="html.parser")