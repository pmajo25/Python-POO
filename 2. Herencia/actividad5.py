class Reloj:
    # Método constructor
    def __init__(self, marca, tipo, material):
        # Defino los atributos de instancia de la clase
        self.marca = marca 
        self.tipo = tipo
        self.material = material  
        self.precio = int(input("Ingrese el precio del reloj: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Dispositivos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Material: {self.material}")
        print(f"Precio del reloj: {self.precio} pesos")

        
class Relojinteligente(Reloj):
    def __init__(self, marca, tipo, material):
        super().__init__(marca, tipo, material)
        
        self.tipopantalla = input("Ingrese el tipo de pantalla (Ej: Amoled): ")
        self.sistemaoperativo = input("Ingrese el sistema operativo (Ej: Wear OS): ")
        
    def encender(self):
        self.tocar = input("Desea encender su reloj (si/no): ")
        
        if self.tocar.lower() == "si":
            print(f"||||||||||")
            print(f"Su reloj {self.marca} ha encendido exitosamente")
            print("------------------------->")
        else:
            print("Perfecto, cuando desees puedes encenderlo")

            
# Crear el objeto de la clase Smartphone
objeto_reloj = Relojinteligente("Samsung", "SmartWatch", "Acero inoxidable")
objeto_reloj.registro()
objeto_reloj.encender()
