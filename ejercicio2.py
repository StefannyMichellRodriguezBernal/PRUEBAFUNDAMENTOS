BASE = float(input("ingrese el lado del triangulo: "))
AlTURA = float(input("ingresa el lado del triangulo: "))

AREA = (BASE * AlTURA) / 2
print("el area del triangulo es: ", AREA)

if AREA > 1000: 
        print("datos no validos")