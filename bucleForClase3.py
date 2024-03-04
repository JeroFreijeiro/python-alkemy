# bucle for...in con LISTAS

nombres = ["Juan", "Pepe", "Martin", "Luis", "Ricardo"]

for nombre in nombres:
    print(nombre) # por cada elemento NOMBRE en la lista "nombres" hacer un print

""" Juan
    Pepe
    Martin
    Luis
    Ricardo """ # el print se ejecutó 5 veces, 1 print por cada elemento

for e in nombres:
    print(e)   


# bucle for...in con TUPLAS
diasSemana = (
    "Lunes", 
    "Martes", 
    "Miercoles", 
    "Jueves", 
    "Viernes", 
    "Sabado", 
    "Domingo"
)

for e in diasSemana:
    print(e) 

""" Lunes
    Martes
    Miercoles
    Jueves
    Viernes
    Sabado
    Domingo """


# bucle for...in con DICCIONARIOS
persona1 = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 30,
    "altura" : 1.75
}

for e in persona1:
    print(e)

""" nombre
    apellido
    edad
    altura """

print("------------")

for e in persona1.values(): # Acá regresa solo los values
    print(e)

""" Juan
    Perez
    30
    1.75 """

print("------------")

for e in persona1.keys(): # Acá regresa solo los keys
    print(e)

""" nombre
    apellido
    edad
    altura """

print("------------")

for e in persona1.items(): # Acá regresa las tuplas
    print(e)

""" ('nombre', 'Juan')
    ('apellido', 'Perez')
    ('edad', 30)
    ('altura', 1.75) """

print("------------")

for dato in persona1.items(): # son dos for anidados
    for e in dato :
        print(e)

""" nombre
    Juan
    apellido
    Perez
    edad
    30
    altura
    1.75 """