# Calculadora de áreas
# Autor: Carlos Daniel Morales Aguilar 
# Grupo: 6010

# Mostrar menú de figuras
print("\nElige la operación que deseas saber el área")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Circulo")
print("4. Triángulo")
print("5. Romboide")
print("6. Rombo")

opción = input("Ingresa el número de la opción")

# Evaluar la opción seleccionada
if opción == "1":
    ladoc = float(input("Ingresa un valor para el lado"))
    resultado = ladoc * ladoc 
    print("El resultado del área del cuadrado es:", resultado)
elif opción == "2":
    baser = float(input("Ingresa un valor para la base"))
    alturar = float(input("Ingresa un valor para la altura"))
    resultado = baser * alturar 
    print(" El resultado del área del rectángulo es:", resultado)
elif opción == "3": 
    radioc = float(input("Ingresa un valor para el radio"))
    resultado = radioc * radioc * 3.1416
    print(" El resultado del área del circulo es:", resultado)
elif opción == "4": 
    baset = float(input("Ingresa un valor para la base-t"))
    alturat = float(input("Ingresa un valor para el lado"))
    resultado = baset * alturat / 2
    print(" El resultado del área del triángulo es:", resultado)
elif opción == "5":
    basero = float(input("Ingresa un valor para la base-ro"))
    alturaro = float(input("Ingresa un valor para la altura-ro"))
    resultado = basero * alturaro
    print(" El resultado del área de un romboide es:", resultado)
elif opción == "6":
    diametrom = float(input("Ingresa un valor para el diametro mayor"))
    diametromn = float(input("Ingresa un valor para el diametro menor"))
    resultado = diametrom * diametromn / 2
    print(" El resultado del área del rombo es:", resultado)
    