print("Índice de masa corporal (IMC)")
peso = input("Ingresar peso en kilogramos:  ")
estatura = input("Ingresar estatura en metros:  ")
imc = round(float(peso)/float(estatura)**2,2)
print("Su imc es: " + str(imc))