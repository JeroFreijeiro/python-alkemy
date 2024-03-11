# REPASO
# - Funciones nativas de Python
# - Funciones personalizadas
# - Funciones parametrizadas y su ejecución

# POO es un paradigma más, de entre varios

# OTROS TIPOS DE PARADIGMAS
""" 
    1- Paradigma imperativo
    2- Paradigma funcional
    3- Paradigma declarativo
    4- Paradigma reactivo
"""

# POO permite manipular los objetos, de acuerdo a 3 propiedades:
# 1- las propiedades
# 2- el comportamiento
# 3- el estado

# POO - Un objeto es una 'entidad' 
# ATRIBUTOS/PROPIEDADES - que tiene determinadas características
# MÉTODOS - puede realizar acciones, tiene 'x' comportamiento
# ESTADOS - puede tener un estado


# CLASES

# Un OBJETO es una INSTANCIA de una CLASE
# ejemplo en clase: "los objetos que hoy vamos a estar creando van a tener una estructura (una especie
# de molde), que es la CLASE, una vez que determinemos que es lo que va a componer esa CLASE AUTO,
# vamos a crear 1, 2, 10 autos, y cada uno de esos autos que creemos es una INSTANCIA DE ESA CLASE.
# O sea, cada auto que creemos es un OBJETO, y cada objeto que creemos es una INSTANCIA DE ESA CLASE (AUTO)"


class Auto: # El nombre de la clase (la 1ra letra) va siempre en mayúscula
    #constructor - acá definimos los ATRIBUTOS
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    #métodos - permiten funcionalidades
    #getters - muestran los atributos fuera del contexto de la clase
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getAuto(self):
        print("Marca: " + self.getMarca())
        print("Modelo: " + self.getModelo())
        print("Color: " + self.getColor())


auto1 = Auto("Toyota", "Prius", "Blanco")
auto2 = Auto("Fiat", "Cronos", "Rojo")
auto3 = Auto("Peugeot", "208", "Gris")

auto1.getAuto() # getAuto es el getter que se creó en la CLASE AUTO, trajo marca modelo y color
print("----------")
auto2.getAuto()
print("----------")
auto3.getAuto()

""" Marca: Toyota
Modelo: Prius
Color: Blanco
----------
Marca: Fiat
Modelo: Cronos
Color: Rojo
----------
Marca: Peugeot
Modelo: 208
Color: Gris """