# FUNCIONES

# Nativas y definidas por el usuario

# En casi cualquier lenguaje de programación, las funciones constan de bloques de código, que se encierran bajo un nombre
#y esa función cumple una tarea específica (no es gral), de esa manera es más fácil reutilizarla

# 2 razones: optimizar código / ordenar el código (es más organizado)

# Pueden (o no) retornar algo
# Pueden (o no) recibir argumentos
# Son reutilizables

# FUNCIONES NATIVAS DE PYTHON : https://docs.python.org/es/3.9/library/functions.html

# ----------------------------

# FUNCIONES DEFINIDAS POR EL USUARIO

# Tienen 3 pasos : declaración / definición / invocación-ejecución

# Se inician con def nombre_funcion():

precio = 2500

def sumar_iva(): # Función declarada
    print(precio * 1.21) # Definir la función

sumar_iva() # 3025.0 invoco / llamo la función

# Para trabajar funciones se necesitan crear PARÁMETROS
# ¿Que son los parámetros? Son una especie de variable dentro de la función, y se definen en el llamado dentro de la función

def sumar_iva(precio): # precio es el parámetro
    print(precio * 1.21)

sumar_iva(2500)         # acá se está definiendo dentro cuando es llamada
sumar_iva(2960)
sumar_iva(1650)
sumar_iva(850)
sumar_iva(496)

""" 3025.0
    3581.6
    1996.5
    1028.5
    600.16 """   


# ALGORITMOS
# 1. ENTRADA DE DATOS - en la función serían los parámetros
# 2. PROCESAMIENTO DE DATOS
# 3. RETORNO DE DATOS

def sumar_iva(precio): # Declaramos la función - 1. ENTRADA DE DATOS
    return precio * 1.21 # Definir la función - 2. PROCESAMIENTO DE DATOS

print(sumar_iva(100)) # invocar / llamar - 3. RETORNO DE DATOS
print(sumar_iva(2960))
print(sumar_iva(1650))
print(sumar_iva(850))
print(sumar_iva(496))

""" 121.0
    3581.6
    1996.5
    1028.5
    600.16 """

def sumar_iva(precio, porcIva): 
    resultado = precio * porcIva
    return resultado 

print(sumar_iva(100, 1.10)) 
print(sumar_iva(2960, 1.18))
print(sumar_iva(1650, 1.21))
print(sumar_iva(850, 1.25))
print(sumar_iva(496, 1.20))

""" 10.00000000000001
    3492.7999999999997
    1996.5
    1062.5
    595.1999999999999 """

def sumar_iva(nombre,precio, porcIva): 
    resultado = precio * porcIva
    saludo = f'Hola {nombre} precio total {resultado}'
    return saludo 

print(sumar_iva("Juan",100, 1.10)) 
print(sumar_iva("Pedro",2960, 1.18))
print(sumar_iva("Mario",1650, 1.21))
print(sumar_iva("Jose",850, 1.25))
print(sumar_iva("Hernan",496, 1.20))

""" Hola Juan precio total 110.00000000000001
    Hola Pedro precio total 3492.7999999999997
    Hola Mario precio total 1996.5
    Hola Jose precio total 1062.5
    Hola Hernan precio total 595.1999999999999 """