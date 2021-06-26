#*****Examen, Ejercicio 2 - Menu*****#

def menu():
    print("********************************")
    print("*             MENU             *")
    print("* 1. Area de Triangulo         *")
    print("* 2. Area de Cuadrado          *")
    print("* 3. Area de Circulo           *")
    print("* 4. Salir                     *")
    print("********************************")
    opcion = int(input("Elija Opcion: "))
    return opcion

opcion = menu()
while opcion !=4:
    if opcion == 1:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
            calculo = (valor1 * valor2)/2
            print("\nEl area del triangulo es " + str(calculo) + "\n")

    elif opcion == 2:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
            calculo = valor1 * valor2
            print("\nEl area del cuadrado es " + str(calculo) + "\n")
        
    elif opcion == 3:
            valor1 = int(input("Ingrese el primer valor: "))
            valor2 = int(input("Ingrese el segundo valor: "))
            calculo = (3.1416) * (valor1 * valor2)
            print("\nEl radio del circulo es " + str(calculo) + "\n")
    
    else:
        print("\nOpcion no valido\n")

    opcion = menu()