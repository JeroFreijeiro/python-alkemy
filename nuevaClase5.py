# POLIMORFISMO

# En informática se conoce a POLIMORFISMO a la cualidad que tienen los objetos de tomar diferentes formas

# ejercicio propuesto en clase

class Auto:
    def acelera(self):
        print("Me transporto en 4 ruedas")

class Moto:
    def acelera(self):
        print("Me transporto en 2 ruedas")

class Camion:
    def acelera(self):
        print("Me transporto en 18 ruedas") 

# aca dependiendo del vehiculo que se trabaje será ese.
miVehiculo = Auto() # Me transporto en 4 ruedas
miVehiculo = Camion() 
miVehiculo = Moto() #Me transporto en 2 ruedas





def vehiculoAcelera(vehiculo): # esta es una funcion global (chequear la sangria), una vez definida la funcion le ponemos el atributo vehiculo
    vehiculo.acelera()

vehiculoAcelera(miVehiculo)

""" auto = Auto() # se crean las INSTANCIAS
auto.acelera()  # aunque los 3 tengan el mismo método, se van a ejecutar uno de cada porque se está
                # trabajando dentro de clases
moto = Moto() 
moto.acelera()

camion = Camion() 
camion.acelera() 


Me transporto en 4 ruedas
Me transporto en 2 ruedas
Me transporto en 18 ruedas"""


# ------------ ABSTRACCIÓN ------------

# consiste de un proceso lógico en interpretar la info exterior, y saber diferenciar entre lo que 
# necesitamos (representar informaticamente de alguna manera) y cuales no, o trasladar lo mas
# fielmente posible las cualidades del objeto que necesitamos manipular en nuestro codigo

# proceso que debemos darnos cuenta que atributos sirven y que no para poder trabajar en POO

# ej: si trabajo en programa para seguros de autos datos importantes son Nº de chasis, pero no sera
# tan importante como suena la bocina.

# datos innecesarios es perdida de tiempo o de recursos informaticos



# ------------ ENCAPSULAMIENTO ------------

# python y java existen atributos PUBLICOS Y PRIVADOS
# en java (lenguaje estricto) siempre que se empieza una variable nueva se pone private o public
# despues se pone tipo de dato, dsps se pone nombre de la variable, y por ultimo el valor que tiene.

class Algo:
    def __init__(self, _nombre, apellido): #el guion bajo delante de nombre lo hace PRIVADO
        self._nombre = _nombre #atributo privado
        self.apellido = apellido #atributo publico
#ATRIBUTO PUBLICO: no hace falta usar setters y getters para verlo en consola o trabajarlo fuera de la clase
        
# en python atributos publi y private funcionan mas para organizacion y buenas practicas para programadores

algo = Algo("juan","perez")

print(algo._nombre)
print(algo.apellido)

""" juan
perez """  #¿no eran necesarios setters y getters? Explicacion a continuacion:

class Algo:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre # ACA SE AGREGO DOBLE GUION BAJO, AHI SE HIZO PRIVADO
        self.apellido = apellido

algo = Algo("juan","perez")

print(algo.__nombre)
print(algo.apellido)

""" Traceback (most recent call last):
  File "c:\Users\Jeronimo\OneDrive\Escritorio\Tests Alkemy\tempCodeRunnerFile.py", line 8, in <module>
    print(algo.__nombre)
          ^^^^^^^^^^^^^
AttributeError: 'Algo' object has no attribute '__nombre' """



# ------------ HERENCIA ------------

# 
