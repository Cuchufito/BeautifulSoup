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
