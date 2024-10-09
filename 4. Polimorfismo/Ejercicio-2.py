''' Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion()
    que describa el tipo de vehículo y una función para mostrar el polimorfismo mostrar_descripcion() '''

# Clase Aprendiz
class Carro:
    def __init__(self, marca, modelo, año, color, motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        print(f"---------------------------------")

    def descripcion(self):
        print("Soy un carro")
        print(f"Mi marca es {self.marca} con modelo {self.modelo}")
        print(f"Soy del año: {self.año}")
        print(f"Mi color es: {self.color}")
        print(f"Y tengo un motor de {self.motor}")
        print(f"---------------------------------")

# Clase Instructor
class Moto:
    def __init__(self, marca, modelo, año, cilindrada, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.cilindrada = cilindrada
        self.color = color

    def descripcion(self):
        print("Soy una moto")
        print(f"Mi marca es {self.marca} con modelo {self.modelo}")
        print(f"Soy del año: {self.año}")
        print(f"Tengo una cilindrada: {self.cilindrada}")
        print(f"Mi color es {self.color}")
        print(f"---------------------------------")


# Clase Coordinador
class Bicicleta:
    def __init__(self, color, tamaño, tipo_frenos, tipo_llantas, peso):
        self.color = color
        self.tamaño = tamaño
        self.tipo_frenos = tipo_frenos
        self.tipo_llantas = tipo_llantas
        self.peso = peso

    def descripcion(self):
        print("Soy una Bicicleta")
        print(f"Mi color es {self.color} tengo un tamaño {self.tamaño}")
        print(f"Mi tipo de frenos es: {self.tipo_frenos}")
        print(f"Mi tipo de llantas es: {self.tipo_llantas}")
        print(f"Y peso: {self.peso}")
        print(f"---------------------------------")

# Función que muestra la información de cualquier tipo de objeto
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()


# Instancias de cada clase
objeto_carro = Carro("Toyota", "Camry", "2021", "Gris", "2.5L")
objeto_moto = Moto("Ducati", "Panigale V4", "2021", "1103 cc", "Rojo")
objeto_bicicleta = Bicicleta("Rojo", "Mediano (17 pulgadas)", "Disco", "Montaña", "12 kg")

# Llamado al método mostrar_info para cada objeto
mostrar_descripcion(objeto_carro)
mostrar_descripcion(objeto_moto)
mostrar_descripcion(objeto_bicicleta)