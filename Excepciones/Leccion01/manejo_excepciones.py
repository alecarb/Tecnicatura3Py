from NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input("Digite un nro: "))
    b = int(input("Digite otro nro: "))
    if a == b:
        raise NumerosIgualesException("Son numeros iguales") # raise permite arrojar una excepcion
    resultado = a / b
except TypeError as e:
    print(f'TypeError - Ocurrio un error : {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')
else:
    print("No se arrojo ninguna excepcion")
finally:  # Sempre se va a ejecutar
    print("Ejercucion de este bloque finally")

print(f'El resultado es: {resultado}')
print("seguimos...")
