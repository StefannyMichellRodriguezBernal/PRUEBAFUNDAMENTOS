voltaje1 = float(input("ingrese el voltaje: "))
voltaje2 = float(input("ingrese el voltaje: "))
voltaje3 = float(input("ingrese el voltaje: "))
voltaje4 = float(input("ingrese el voltaje: "))
voltaje5 = float(input("ingrese el voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3 + voltaje4 + voltaje5)
print ("promedio: ", promedio)

if promedio > 220:
    print("ALTO VOLTAJE")
else: 
    print("VOLTAJE CORRECTO")
    