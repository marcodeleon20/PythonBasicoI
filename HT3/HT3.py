print("EJERCICIO 1:")
print("Escribir un programa que almacene una cadena de caracteres de  contraseña en una variable, ingresada por el usuario, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.")
print("")

contra = "curso"
password = input("Ingrese la contraseña: ")
if contra == password.lower():
    print("La contaseña es correcta.")
else:
    print("La contraseña no es correcta")


print("")
print("EJERCICIO TERMINADO")


print("")
print("EJERCICIO 2:")
print("Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.")
print("")

nombre = input("¿Cuál es su nombre? ")
genero = input("¿Cuál es su sexo (INGRESE LA LETRA F o M? ")
if (genero == "M" and nombre.lower() < 'm') or (genero == "H" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Usted pertenece al grupo " + grupo)

print("")
print("Se ingresaron correctamente a los alumnos por grupos. " )
print("EJERCICIO TERMINADO")
