""" CONSIGNA
Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos
por la terminal acorde a distintas opciones. Para ello debemos definir una función que reciba
parámetros:

- Combinar funciones nativas y funciones definidas, condicionales y bucles.
- Si el usuario ingresa el nro 1, realiza la acción A.
- Si el usuario ingresa el nro 2, realiza la acción B.
"""

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def operacion_aritmetica():
    while True:
        print("\nOpciones:")
        print("1. Sumar dos números.")
        print("2. Multiplicar dos números.")
        print("3. Salir.")
        
        opcion = input("Ingrese el número de la acción que desea realizar: ")
        
        if opcion == '1' or opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == '2':
                resultado = multiplicar(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    operacion_aritmetica()


""" ejercicio de compañero """

def sumar(nro1, nro2):
    print(nro1+nro2)

def restar(nro1, nro2):
    print(nro1-nro2)

numero1 = int(input('Ingrese un número entero: '))
numero2 = int(input('Ingrese otro número entero: '))

salir = False

while not salir:
    print('A) Sumarlos')
    print('B) Restarlos')
    print('X) Salir')
    opcion = input('Ingrese opcion A o B').upper()

    match opcion:
        case 'A':
            sumar(numero1,numero2)
        case 'B':
            restar(numero1,numero2)
        case 'X':
            salir = True
        case _:
            print('Opcion no valida, reintente')