import psycopg2
from psycopg2 import Error

#la primer parte es igual que en conexionBBDD.py
myusr = "postgres"
mypsw = "23"
mydb = "culturaBBDD"
# Connect to an existing database
connection = psycopg2.connect(user=myusr, password=mypsw, host="127.0.0.1", port="5432", database=mydb)
try:

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # SQL crear nueva tabla
    create_table_query =  '''CREATE TABLE tablaPrimera
            (ID SERIAL PRIMARY KEY,         
	COD_LOCALIDAD INT NOT NULL,
ID_PROVINCIA INT NOT NULL,
ID_DEPARTAMENTO INT NOT NULL,
CATEGORIA VARCHAR[30],
PROVINCIA VARCHAR[50],
LOCALIDAD VARCHAR[50],
NOMBRE VARCHAR[50],
DOMICILIO VARCHAR[100],
CODIGO_POSTAL VARCHAR[14],
NUMERO_DE_TELEFONO VARCHAR[30],
MAIL VARCHAR[100],
WEB VARCHAR[100]
); '''    
    #ejecutar comando
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabla creada exitosamente en PostgreSQL")
    
except(Exception, Error) as error:
    print("Error al conectarse", error)

finally:
    if connection: cursor.close()
    connection.close()
    print("Conexion cerrada con PostgreSQL")