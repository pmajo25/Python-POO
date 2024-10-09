''' Crea tres clases: Guitarra, Piano y Trompeta, cada una con un método tocar()
    que describa el tipo de InstumentoMusicales y una función para mostrar el polimorfismo tocar_instrumento() '''
# Clase Guitarra
class Guitarra:
    def __init__(self, cuerdas, tipo, marca):
        self.cuerdas = cuerdas
        self.tipo = tipo
        self.marca = marca

    def tocar(self):
        print(f"---------------------------------")
        print(f"Soy una guitarra de {self.cuerdas} cuerdas")
        print(f"Tipo {self.tipo}")
        print(f"De la marca {self.marca}")
        print(f"---------------------------------")
        

# Clase Piano
class Piano:
    def __init__(self, teclas, tipo, marca):
        self.teclas = teclas
        self.tipo = tipo
        self.marca = marca

    def tocar(self):
        print(f"Soy un piano con {self.teclas} teclas")
        print(f"Tipo {self.tipo}")
        print(f"De la marca {self.marca}")
        print(f"---------------------------------")
# Clase Trompeta
class Trompeta:
    def __init__(self, material, afinacion, marca):
        self.material = material
        self.afinacion = afinacion
        self.marca = marca

    def tocar(self):
        print(f"Soy una trompeta de {self.material}")
        print(f"Afinación en {self.afinacion}")
        print(f"De la marca {self.marca}")
        print(f"---------------------------------")

# Función que utiliza polimorfismo para tocar cualquier instrumento
def tocar_instrumento(instrumento):
    instrumento.tocar()

# Instancias de cada clase
guitarra = Guitarra(6, "Acústica", "Yamaha")
piano = Piano(88, "De cola", "Steinway")
trompeta = Trompeta("Latón", "Si bemol", "Bach")

# Llamado al método tocar para cada objeto usando polimorfismo
tocar_instrumento(guitarra)
tocar_instrumento(piano)
tocar_instrumento(trompeta)