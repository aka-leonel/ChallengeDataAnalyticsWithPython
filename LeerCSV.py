import copy
import os
import datetime
#este now traera problemas ya que no debe redefinerse las fechas a la hora de ejecutar
#hay que cambiarlo
now= datetime.datetime.now()
#para trabajar con esto primero hay que ejecutar main.py
#y se crearan las carpetas museos, cines y bibliotecas

def ObtenerPath(categoria):
    #obtener directorio actual
    path = os.getcwd()
    #componer el path -ej categoria:museos- /thisFolder/museos/
    path = os.path.join(path, categoria)
    #componer /thisFolder/museos/2022-4/
    path = os.path.join(path, f"{now.year}-{now.month}")
    #componer /thisFolder/museos/2022-4/museos-30-4-2022
    path = os.path.join(path, f"{categoria}-{now.day}-{now.month}-{now.year}")
    return path

def LeerCSV(categoria):
    path = ObtenerPath(categoria)
    file = open(f'{path}\\reporte_{categoria}.csv')
    file.close()    

LeerCSV('museos')

    
    
    