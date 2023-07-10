import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

#Creamos un cursor. Un cursor es un objeto que permite ejecutar sentencias SQL
cursor= conexion.cursor()
sentecia= 'SELECT * FROM persona'
cursor.execute(sentecia) #De esta manera ejecutamos la sentencia
registros= cursor.fetchall()# Recupera todos los registros que seran una lista
print(registros)

cursor.close()
conexion.close()
