voltaje1 = float(input("ingresa el voltaje: "))
voltaje2 = float(input("ingresa el voltaje: "))
voltaje3 = float(input("ingresa el voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3) /3
print("el primedio es de: ", promedio)

if promedio < 115:
    print("voltaje correcto")

if (promedio > 115) and (promedio < 220):
    print("alto voltaje")

if (promedio > 220):
    print("peligro")

