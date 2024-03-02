# Matinee entre 13 y 17 años
# 1. Edad tiene que ser mayor o igual a 13
# 2. Edad tiene que ser menor o igual a 17 

edad = 21

print((edad >= 13) and (edad <= 17))

# AND - CONJUNCIÓN
# V + V = V
# V + F = F
# F + V = F
# F + F = F

# OR - DISYUNCIÓN
# V + V = V
# V + F = V
# F + V = V
# F + F = F




# Tipos de datos

# Numérico - int (número entero, sin comas)
NumEntero = 25

# Numérico - float (número con comas, con decimales)
numFloat = 29.4

# Boolean (verdadero/falso, 1 y 0)
esCliente = True #True y False en boolean empiezan con mayús

# Texto - string (cadena de caracteres)
saludo = "Hola mundo!"
#         ----------- 11 caracteres (espacios en blanco y caracteres especiales tmb cuentan)


# OPERADORES

# Aritméticos

num1 = 10
num2 = 5

suma = num1 + num2
print(suma)

resta = num1 - num2
print(resta)

mult = num1 * num2
print(mult)

div = num1 / num2 # División entera utiliza doble barra // y en lugar de un resultado con decimal devuelve un entero
print(div)

raizCuadrada = num1 ** num2
print(raizCuadrada)


# ASIGNACIÓN = ESTA VARIABLE ES (ESTE) DATO
variable = "Hola" # Esta variabe es el string "Hola"

print(variable)

# COMPARACIÓN = ESTA VARIABLE (ES IGUAL A) ESTA OTRA VARIABLE - devuelve un boolean
print(variable == "Hola") #true
print(variable == "hola") #false

# DISTINTO QUE (ES LO OPUESTO A "IGUAL QUE")

print(variable != "hola") #true


edad = 18

print(edad == 18) # igual que (18)  
print(edad != 18) # distinto que (18)
print(edad > 18) # mayor que (19, 20, 21, ...)  
print(edad >= 18) # mayor o igual que (18, 19, 20, 21, ...)    
print(edad < 18) # menor que (16, 17, 18, ...)  
print(edad <= 18) # menor o igual que (16, 17, 18, ...)


edad = 14
print(edad)
edad = edad + 1 #Puede simplificarse en el ejemplo de abajo (+=)
print(edad)
edad += 1
print(edad)
edad -= 1
print(edad)