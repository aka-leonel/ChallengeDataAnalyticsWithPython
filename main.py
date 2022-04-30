import ObtenerCSV as OCSV

#aqui introducimos el link a las tres fuentes de informacion
#que son archivos CSV
urlMuseos = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
urlCines = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv'
urlBibliotecas = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'


# Organizar los archivos en rutas siguiendo la siguiente estructura:
# “categoría\año-mes\categoria-dia-mes-año.csv”
# ○ Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
# ○ Si el archivo existe debe reemplazarse. La fecha de la nomenclatura
# es la fecha de descarga.


OCSV.obtenerCSV(urlMuseos, "museos")
OCSV.obtenerCSV(urlCines, "cines")
OCSV.obtenerCSV(urlBibliotecas, "bibliotecas")
