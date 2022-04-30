import requests
import CrearCarpeta as CC


def obtenerCSV(url, categoria):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        path = CC.CrearCarpeta(categoria)
        contenido = respuesta.content
        file = open(f"{path}\\reporte_{categoria}.csv", "wb")
        file.write(contenido)
        file.close()
        print(f"la informacion de {categoria} se obtuvo")
    else:
        file = open(f"error_{categoria}", "wb")
        file.write(f"Hubo un error al consultar la url: {url}")
        file.close()
        print(f"No se obtuvo la informacion de {categoria}")