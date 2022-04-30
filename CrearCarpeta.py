import os
import datetime
now= datetime.datetime.now()
#print(f'{now.day}/{now.month}/{now.year}')
# def CrearCarpeta(nombreCarpeta):
#     parent_dir = os.getcwd()
#     path = os.path.join(parent_dir, nombreCarpeta)
#     os.mkdir(path)
#     print(f"Creada la carpeta {nombreCarpeta}")
#     print("Dir: %s" %path)
def CrearCarpeta(categoria):
    path = os.getcwd()
    path = os.path.join(path, categoria)
    os.mkdir(path)
    path = os.path.join(path, f"{now.year}-{now.month}")
    os.mkdir(path)
    path = os.path.join(path, f"{categoria}-{now.day}-{now.month}-{now.year}")
    os.mkdir(path)    
    print("Creado Dir: %s" %path)
    return path
    
# Organizar los archivos en rutas siguiendo la siguiente estructura:
# “categoría\año-mes\categoria-dia-mes-año.csv”
# ○ Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
# ○ Si el archivo existe debe reemplazarse. La fecha de la nomenclatura
# es la fecha de descarga.

    