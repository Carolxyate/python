a = input("Ingrese los minutos de la llamada: ")
b = float(a)
c = (b * 50) + 200
if b <= 3:
    print("Su llamada cuesta 200 pesos.")
elif b > 4:
    print("Su llamada cuesta: ", c)
    
