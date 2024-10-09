#Defino la clase
class Celular:
    #Método constructor
    def __init__(self,nombre, marca, IMEI, bateria, camara):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.IMEI = IMEI
        self.bateria = bateria
        self.camara = camara 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Celular")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("IMEI: " + self.IMEI)
        print("Bateria: " + self.bateria)
        print("Camara: " + self.camara)
        print("--------------------------")
        
    #Método para Encender el Celular
    def encender (self):
        #Defino el atributo privado energia solo para el metodo encender
        self.energia  = int(input("Digite el valor de la carga: "))
        #Evaluamos si tiene carga el celular
        if self.energia >0:
            print("El celular "+self.nombre+" se puede encender")
            print(f"||||||||||| {self.energia} % de carga")
            print("-----------------------------------")
        else:
            print("El celular "+self.nombre+" no se puede encender")
            print("-----------------------------------")
        

        
#Creamos los objetos a partir de instanciar la clase Celular     
objeto1 = Celular("Redmi Note 8", "Xiaomi", "123456789111", "4000 MAH", "48PX")
objeto2 = Celular("Samsung Galaxy S21", "Samsung", "2867861", "5000 MAH", "64PX")
objeto3 = Celular("¡phone 13", "Apple", "356789123999", "3240 MAH", "12PX")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.encender() #Método que evaluar el encendido del celular
objeto2.mostrar_detalles()
objeto2.encender()
objeto3.mostrar_detalles()
objeto3.encender()