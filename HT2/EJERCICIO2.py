print("EJERCICIO 2:")
print("Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.")
print("")
x = int(input("Ingrese un número entero positivo (debe ingresar un número que sea mayor a 1): "))
for j in range(1, x):
    if x % j == 0:
        break
if (j + 1)  == x:
    print(str(x) + " es un número primo.")
else: 
    print(str(x) + " no es un número primo.")

print("")
print("Se ingreso correctamente el número. " )
print("EJERCICIO TERMINADO")