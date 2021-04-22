print("EJERCICIO 1:")
print("Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.")
print("")
x = int(input("Ingresar altura del triangulo: "))


for i in range(x):
    for j in range(i+1):
        print("*", end="")
    print("")

print("")
print("Se ingreso correctamente el trinagulo. " )
print("EJERCICIO TERMINADO")
