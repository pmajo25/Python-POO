class Electrodomestico:
    #metodo constructor
    def __init__(self,marca,color,capacidad):
        #defino los atributos de instancia de la clase
        self.marca = marca 
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Ingrese el consumo eléctrico en kWh: "))
        
    #metodo para registrar la inf. del electrodoméstico
    def registro(self):
        print("---------------------------->")
        print("Electrodomésticos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Consumo eléctrico: {self.consumo_electrico} kWh")
        print(f"Tipo del refrigerador: {self.tipo}")
        
    #Subclase Refrigerados que hereda de electrodoméstico
class Refrigerador(Electrodomestico):
    def __init__(self,marca,color,capacidad,tipo):
      #Heredamos los atributos de Electrodoméstico
        super().__init__(marca,color,capacidad)
        self.tipo = tipo
        self.temperatura = int(input("Ingrese la temperatura inicial del refrigerador en grados °C: "))
        #Metodo para ajustar la temperatura
        
    def ajustar_temperatura(self):
        print("---------------------------->")
        if self.temperatura >= 3 and self.temperatura <= 5:
            print(f"El refrigerador {self.marca} tiene una temperatura normal")
        else:
            print(f"El refrigerador {self.marca} tiene una temperatura fuera del rango recomendado. Por favor revise su refrigerador.")
            
            
nevera=Refrigerador("LG","Acero inoxidable","410 L","No Frost")
nevera.registro()
nevera.ajustar_temperatura()