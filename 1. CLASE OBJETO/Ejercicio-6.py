#Defino la clase
class Moto:
    #Método constructor
    def __init__(self, marca, modelo, año, cilindrada, color):
        #Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.cilindrada = cilindrada
        self.color = color 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion de la Moto")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año: " + self.año)
        print("Cilindrada: " + self.cilindrada)
        print("Color: " + self.color)
        print("--------------------------")
        
     #Método para saber la velocidad de la Moto y cuando frenar
    def velocidades (self):
        #Defino el atributo privado velocidad solo para el metodo velocidades
        self.velocidad  = int(input("Digite en cuanto tiene su velocidad: "))
        #Evaluamos si la moto tiene mucha velocidad o esta normal
        if self.velocidad > 80:
            print("La moto "+self.marca+" tiene mucha velocidad")
            print(f"||||||||||| usted debe frenar y bajar su velocidad")
            print("-----------------------------------")
        else:
            print("La moto "+self.marca+" tiene una velocidad normal")
            print("-----------------------------------")
        

        
#Creamos los objetos a partir de instanciar la clase Moto     
objeto1 = Moto("Yamaha", "YZF-R6", "2020", "600 cc", "Azul")
objeto2 = Moto("Ducati", "Panigale V4", "2021", "1103 cc", "Rojo")
objeto3 = Moto("Kawasaki", "Ninja H2", "2021", "998 cc", "Verde")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.velocidades() #Método que evaluar el encendido de la Moto
objeto2.mostrar_detalles()
objeto2.velocidades()
objeto3.mostrar_detalles()
objeto3.velocidades()