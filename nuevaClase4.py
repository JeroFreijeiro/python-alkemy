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
# 1. ATRIBUTOS/PROPIEDADES - que tiene determinadas características
# 2. MÉTODOS - puede realizar acciones, tiene 'x' comportamiento
# 3. ESTADOS - puede tener un estado


# CLASES

# Un OBJETO es una INSTANCIA de una CLASE
# ejemplo en clase: "los objetos que hoy vamos a estar creando van a tener una estructura (una especie
# de molde), que es la CLASE, una vez que determinemos que es lo que va a componer esa CLASE AUTO,
# vamos a crear 1, 2, 10 autos, y cada uno de esos autos que creemos es una INSTANCIA DE ESA CLASE.
# O sea, cada auto que creemos es un OBJETO, y cada objeto que creemos es una INSTANCIA DE ESA CLASE (AUTO)"


class Auto: # El nombre de la clase (la 1ra letra) va siempre en mayúscula
    #constructor - acá definimos los ATRIBUTOS
    def __init__(
                self,
                marca, 
                modelo, 
                color, 
                estadoMotor, #¿cuantos estados tiene un motor?: dos, prendido, apagado. Boolean True/False
                estadoCambios, 
                velocidades
            ): #los últimos tres son ESTADOS (estadoMotor, estadoCambios, velocidades)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.estadoMotor = estadoMotor
        self.estadoCambios = estadoCambios
        self.velocidades = velocidades
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
    def cambiarEstadoMotor(self):
        if(self.estadoMotor): # acá el == True es redundante, ya está explicitado
            print("Motor del " + self.getModelo() + " prendido, lo voy a apagar")
            self.estadoMotor = False
            print("Motor apagado")
        else:
            print("Motor del " + self.getModelo() + " apagado, lo voy a encender")
            self.estadoMotor = True
            print("Motor encendido")
    def subirVelocidad(self):
        # creamos la condición IF para que no se exceda en sumar cambios al vehículo
        if(self.estadoCambios < self.velocidades):
            self.estadoCambios += 1 
            print(f'el {self.getModelo()} estaba en {self.estadoCambios - 1 } ahora esta en {self.estadoCambios}')
        else:
            print("No podes subir mas")
    def bajarVelocidad(self):
        if(self.estadoCambios > -1): # aca es -1 porque es lo máximo que se puede bajar - la reversa -
            self.estadoCambios -= 1 
            print(f'el {self.getModelo()} estaba en {self.estadoCambios + 1 } ahora esta en {self.estadoCambios}')
        else:
            print("No podes bajar más")

auto1 = Auto("Toyota", "Prius", "Blanco",True, 1, 6)
auto2 = Auto("Fiat", "Cronos", "Rojo", False, 0, 5)
auto3 = Auto("Peugeot", "208", "Gris", False, -1, 5)

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

auto1.cambiarEstadoMotor()
""" Marca: Peugeot
Modelo: 208
Color: Gris
Motor prendido, lo voy a apagar
Motor apagado """

auto2.cambiarEstadoMotor()
auto3.cambiarEstadoMotor()
""" Motor del Prius prendido, lo voy a apagar
Motor apagado
Motor del Cronos apagado, lo voy a encender
Motor encendido
Motor del 208 apagado, lo voy a encender
Motor encendido """

# testeando el estado subirVelocidad
auto1.subirVelocidad()  # el Prius estaba en 1 ahora esta en 2
# testeando el estado bajarVelocidad
auto1.bajarVelocidad()  # el Prius estaba en 4 ahora esta en 3 <-(este resultado me arrojo antes de cambiar el signo de + a -, ojo porque el código puede funcionar pero está mal)
# el Prius estaba en 2 ahora esta en 1 <-(resultado con el signo correcto)

#los vehículos tienen determinadas cantidad de cambios para realiza, ¿que pasa si se excede?
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
auto1.subirVelocidad()
""" el Prius estaba en 1 ahora esta en 2
el Prius estaba en 2 ahora esta en 3
el Prius estaba en 3 ahora esta en 4
el Prius estaba en 4 ahora esta en 5
el Prius estaba en 5 ahora esta en 6
el Prius estaba en 6 ahora esta en 7            # inconsistente o erróneo, se crea una CONDICIÓN IF
el Prius estaba en 7 ahora esta en 8
el Prius estaba en 8 ahora esta en 9
el Prius estaba en 9 ahora esta en 10
el Prius estaba en 10 ahora esta en 11 """

""" el Prius estaba en 1 ahora esta en 2
el Prius estaba en 2 ahora esta en 3
el Prius estaba en 3 ahora esta en 4
el Prius estaba en 4 ahora esta en 5
el Prius estaba en 5 ahora esta en 6            # condicion ya creada
No podes subir mas
No podes subir mas
No podes subir mas
No podes subir mas
No podes subir mas """


auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()
auto1.bajarVelocidad()

""" el Prius estaba en 6 ahora esta en 5
el Prius estaba en 5 ahora esta en 4
el Prius estaba en 4 ahora esta en 3
el Prius estaba en 3 ahora esta en 2
el Prius estaba en 2 ahora esta en 1
el Prius estaba en 1 ahora esta en 0
el Prius estaba en 0 ahora esta en -1
No podes bajar m�s
No podes bajar m�s
No podes bajar m�s """
