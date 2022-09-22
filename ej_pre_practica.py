#Se desea crear un programa que simule el funcionamiento basico de un vehiculo

"""-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int )
,color(Str),enMarcha(Booleano, por defecto False)<br />
    -Crear su constructor<br />
    -Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo<br />
    -crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 
ruedas y "Motocicleta" si posee 2 ruedas.<br />
    -Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.<br /><br />
"""
import string

class Vehiculo:
    def __init__(self, marca: str, ruedas: int, color: str, enMarcha: bool) -> None:
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = False

    def arracar(self) -> None:
        self.enMarcha = True

    def tipoVehiculo(self) -> string:
        tipo_vehiculo = " "
        
        if self.ruedas == 4:
            tipo_vehiculo =  "Automovil"
        elif self.ruedas == 2:
            tipo_vehiculo = "Motocicleta"
        
        return tipo_vehiculo

    def mostrar(self) -> None:
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.enMarcha)


v11 = Vehiculo("Nissan", 4, "Gris", True)
v11.arracar()
v11.mostrar()
print(v11.tipoVehiculo())

"""lucho = Vehiculo("Luchito", 2, "Negro", False)
lucho.arracar()
lucho.mostrar()
print(lucho.tipoVehiculo())
"""