# Colección de Datos (LISTAS / TUPLAS / DICCIONARIOS)

# LISTA - Array / ArrayList

# Las listas son : Ordenadas / Dinámicas / Mutable

nombre1 = "Juan"
nombre2 = "Pepe"
nombre3 = "Luis"
nombres = ["Juan", "Pepe", "Luis"] # En un solo espacio de memoria pude almacenar 3 nombres
# Posiciones  0       1        2
# Elementos   1       2        3
names = ["John", "Mary", "Louis"]

print(nombres) # ['Juan', 'Pepe', 'Luis']
print(nombres[2]) # Luis

nombres = ["Juan", "Pepe", "Martin", "Luis"] 
print(nombres) # ['Juan', 'Pepe', 'Martin', 'Luis']
print(nombres[2]) # Martin

nombres = [1, 2, 3, 4, 5] # La info anterior se borro y se sobreescribió
print(nombres)

# O un dato primitivo
nombres = False
print(nombres)

# MÉTODOS = Acciones específicas para trabajar con listas

# append - agrega un elemento al final de la lista
nombres = ["Juan", "Pepe", "Martin", "Luis"] 

nuevoDato = "Lucia"
nombres.append(nuevoDato) # ['Juan', 'Pepe', 'Martin', 'Luis', 'Lucia']

print(nombres)

# insert - agrega un elemento en el índice indicado
nombres.insert(2, "Carla") # ['Juan', 'Pepe', 'Carla', 'Martin', 'Luis', 'Lucia']

print(nombres)

# pop - elimina un elemento al final de la lista o en el índice indicado
# pop() -> al final de la lista
# pop(1) -> elimina elem en la posición 1
nombres.pop() # ['Juan', 'Pepe', 'Carla', 'Martin', 'Luis']
print(nombres) 

nombres.pop(2) # ['Juan', 'Pepe', 'Martin', 'Luis']
print(nombres)

# remove - elimina el elemento si lo consigue específicamente
nombres.remove("Juan") # ['Pepe', 'Martin', 'Luis']
print(nombres)

# extend - añadir una lista a otra lista preexistente
nombres.extend(names) # ['Pepe', 'Martin', 'Luis', 'John', 'Mary', 'Louis']
print(nombres)


numeros = [16, 43, 25, 76, 44, 87, 555, 897, 4325, 23, 4, 2, 7, 6]

print (numeros)

# sort - ordena la lista de menor a mayor
""" numeros.sort() # [2, 4, 6, 7, 16, 23, 25, 43, 44, 76, 87, 555, 897, 4325]
print (numeros) """

# reverse - invertir el orden de la lista
numeros.reverse() # [6, 7, 2, 4, 23, 4325, 897, 555, 87, 44, 76, 25, 43, 16]
print(numeros)




# Colección de Datos (LISTAS / TUPLAS / DICCIONARIOS)

# TUPLA - tuple()

# son inmutables, los valores que almacenan NO pueden ser modificados

diasSemana = (
    "Lunes", 
    "Martes", 
    "Miercoles", 
    "Jueves", 
    "Viernes", 
    "Sabado", 
    "Domingo"
) # 7 elementos, 6 posiciones (las posiciones se inician en el índice 0)

# Las tuplas al ser inmutables tienen solamente dos métodos para poder trabajar: Count e Index

# count - devuelve la cantidad de veces que un elemento aparece en la tupla
print(diasSemana.count("Lunes")) # 1

# index - devuelve el índice (la posición) del elemento en cuestión
print(diasSemana.index("Miercoles")) # 2




# Colección de Datos (LISTAS / TUPLAS / DICCIONARIOS)

# Diccionarios - dict()

# Los datos se almacenan en par (key/value - clave/valor)

# Se arman con {}, son dinámicos (se pueden modificar)

# POO - un objeto es una manera en la que podemos representar una entidad del mundo real, abstraída en informática

#   key   :   value
persona1 = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 30,
    "altura" : 1.75
}

print(persona1) # {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 30, 'altura': 1.75}
print(persona1.keys()) # dict_keys(['nombre', 'apellido', 'edad', 'altura']) se crea una lista
print(persona1.values()) # dict_values(['Juan', 'Perez', 30, 1.75]) se crea una lista
print(persona1.items()) # dict_items([('nombre', 'Juan'), ('apellido', 'Perez'), ('edad', 30), ('altura', 1.75)]) se crea una lista donde cada elemento es una tupla


# get - devuelve un elemento con su key, si no lo encuentra devuelve -> default
resultado = persona1.get("apellido") # Perez
print(resultado)

# Eliminar elementos del diccionario    ( POP - CLEAR )

# pop - elimina elemento a través de su key
persona1.pop("apellido") # {'nombre': 'Juan', 'edad': 30, 'altura': 1.75}
print(persona1)

# clear - elimina todos los elementos
persona1.clear() # {}
print(persona1)