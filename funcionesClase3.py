# FUNCIONES

# Nativas y definidas por el usuario

# En casi cualquier lenguaje de programación, las funciones constan de bloques de código, que se encierran bajo un nombre
#y esa función cumple una tare específica (no es gral), de esa manera es más fácil reutilizarla

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