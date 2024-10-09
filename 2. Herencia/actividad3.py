class Instrumento:
    # Método constructor
    def __init__(self, instrumento, marca, material):
        # Defino los atributos de instancia de la clase
        self.instrumento = instrumento
        self.marca = marca
        self.material = material  
        
        self.precio = int(input("Ingrese el precio del instrumento: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Instrumentos registrados")
        print("---------------------------->")
        print(f"Instrumento: {self.instrumento}")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio instrumento: {self.precio} pesos")

        
class Guitarra(Instrumento):
    def __init__(self, instrumento, marca, material):
        super().__init__(instrumento, marca, material)
        
        # Definir el sistema operativo y conectividad
        self.numero_cuerdas = input("Ingrese el numero de cuerdas: ")
        self.acordes_basicos = input("Digite cuales son los acordes básicos que conoce: ")
        
    def tocar_guitarra(self):
        self.tocar = input("Desea tocar el instrumento (si/no): ")
        
        if self.tocar.lower() == "si":
            print(f"||||||||||")
            print(f"Que buena opción, adelante. ")
            print("------------------------->")
        else:
            print("Hasta la proxima.")
            

            
# Crear el objeto de la clase Instrumento
objeto_musica = Guitarra("guitarra", "Ibanez", "Madera")
objeto_musica.registro()
objeto_musica.tocar_guitarra()
