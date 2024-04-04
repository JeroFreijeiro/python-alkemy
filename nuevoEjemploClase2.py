print("Soy el nuevo archivo Python")

# En Python si quiero crear una CONSTANTES debe inicializarse con mayúscula
# Las VARIABLES no se inician con mayúscula
# Python SI es case sensitive

nombre = "Juan"
apellido = "Perez"
edad = 21

nombre_entero = nombre + " " + apellido

saludo = f'Hola! Mi nombre es {nombre_entero} y tengo {edad} anios.'

print(saludo)

# ESTRUCTURAS DE CONTROL
# Con estructuras de control creamos reglas y escenarios para tomar decisiones en el orden del flujo y en base a los resultados que aparecen

# ESTRUCTURAS DE CONTROL Nº 1  - CONDICIONALES IF / ELIF / ELSE

# Boliche 18 o más años
# Matinee entre 13 y 17

edad = 10
esSuCumpleanios = True

if (edad >= 18):
    print(f'Tenes {edad} anios, podes entrar al boliche.')
    if(esSuCumpleanios):
        print(f'Feliz cumple, te ganaste un trago')
elif((edad >=13) and (edad <=17)):
    print(f'Tenes {edad} anios, podes entrar a la matinee.')
    if(esSuCumpleanios):
        print(f'Feliz cumple, te ganaste una gaseosa')
else:
    print(f'Tenes {edad} anios, no podes entrar.')