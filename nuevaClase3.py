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