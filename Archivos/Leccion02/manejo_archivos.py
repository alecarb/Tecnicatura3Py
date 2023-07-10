# Declaramos una variable que siempre va a estar dentro de un try.
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # La w es de write que significa escribir. Por default el
    # método open crea y guarda el archivo dentro de la misma carpeta de trabajo.
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt. \n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción.\n')
    archivo.write('Las letras son:\nr read, \na append anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt esta es para texto o text,\nb archivo binario\nw+ para escribir y para leer,\nr+ para leer y para escribir\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:
    archivo.close()  # Con esto se debe cerrar el archivo. Es necesario
# archivo.write('Todo quedó perfecto') : este es un error. No se puede trabajar después que se ejecuto el close
