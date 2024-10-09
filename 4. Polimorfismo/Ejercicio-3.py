''' Crea tres clases: Perro, Gato y Pajaro, cada una con un método sonido())
    que describa el tipo de Animal y una función para mostrar el polimorfismo sonido_animal() '''
# Clase Perro
class Perro:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        

    def sonido(self):
        print(f"---------------------------------")
        print("¡Guau, guau!")
        print(f"Mi nombre es {self.nombre} soy de especie {self.especie}")
        print(f"tengo: {self.edad} años")
        print(f"Peso: {self.peso}")
        print(f"---------------------------------")

# Clase Gato
class Gato:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        

    def sonido(self):
        print("¡Miau, miau!")
        print(f"Mi nombre es {self.nombre} soy de especie {self.especie}")
        print(f"tengo: {self.edad} años")
        print(f"Peso: {self.peso}")
        print(f"---------------------------------")

# Clase Pájaro
class Pajaro:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        
    def sonido(self):
        print("¡Pío, pío!")
        print(f"Mi nombre es {self.nombre} soy de especie {self.especie}")
        print(f"tengo: {self.edad} años")
        print(f"Peso: {self.peso}")
        print(f"---------------------------------")
        
# Función que utiliza polimorfismo para tocar cualquier instrumento
def sonido_animal(animal):
    animal.sonido()

# Instancias de cada clase
objeto_perro = Perro("Simba", "Canis familiaris", "7 años", "20 kg")
objeto_gato = Gato("Pardo", "Felis catus", "3 años", "4 kg")
objeto_pajaro = Pajaro("Ruby", "Serinus canaria", "2 años", "0.03 kg")

# Llamado al método sonido para cada objeto
sonido_animal(objeto_perro)
sonido_animal(objeto_gato)
sonido_animal(objeto_pajaro)