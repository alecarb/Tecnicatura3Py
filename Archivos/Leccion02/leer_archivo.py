# Las letras son r read, a append, w write, x si no existe el archivo manda una excepcion

archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())
# print(archivo.read(16))
# print(archivo.read(5))
# print(archivo.read(10)) # Continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

# No se especifica la ruta de acceso si el archivo esta en la misma ubicacion. Pero sino si.
# queda asi:
# archivo = open("c:\\usuario\\ale\prueba.txt", 'r', encoding='utf8') #las \\ se interpreta como una sola. Es un caracter de escape. Ver bien eso!!

# Anexamos informacion, copiamos a otro. OJO porque cada vez que se ejecute, se agrega el contenido. Es un append por cada ejecucion.
# Se soluciona cambiando la a por la w que solo escribe. Y listo! nada duplicado. Por lo menos es este ejemplo.
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # carramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')