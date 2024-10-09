#Defino la clase
class Carro:
    #Método constructor
    def __init__(self, marca, modelo, año, color, motor):
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Carro")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año: " + self.año)
        print("Color: " + self.color)
        print("Motor: " + self.motor)
        print("--------------------------")
        
     #Método para saber la velocidad del carro y cuando frenar
    def velocidad (self):
        #Defino el atributo privado frenar solo para el metodo velocidad
        self.frenar  = int(input("Digite en cuanto tiene su velocidad: "))
        #Evaluamos si el carro tiene mucha velocidad o esta normal
        if self.frenar > 80:
            print("El carro "+self.marca+" tiene mucha velocidad")
            print(f"||||||||||| usted debe frenar y bajar su velocidad")
            print("-----------------------------------")
        else:
            print("El carro "+self.marca+" tiene una velocidad normal")
            print("-----------------------------------")
        
#Creamos los objetos a partir de instanciar la clase Carro     
objeto1 = Carro("Toyota", "Camry", "2021", "Gris", "2.5L")
objeto2 = Carro("Ford", "Ranger", "2019", "Blanco", "3.2L")
objeto3 = Carro("Tesla", "Model S", "2022", "Rojo", "Electrico")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.velocidad() #Método que evaluar velocidad del carro 
objeto2.mostrar_detalles()
objeto2.velocidad()
objeto3.mostrar_detalles()
objeto3.velocidad()