#Defino la clase
class Animal:
    #Método constructor
    def __init__(self,nombre, especie, edad, peso, habitad):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.habitad = habitad 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Animal")
        print("Nombre: " + self.nombre)
        print("especie: " + self.especie)
        print("edad: " + self.edad)
        print("peso: " + self.peso)
        print("habitad: " + self.habitad)
        print("--------------------------")
        
    #Método para saber si el Animal ya descanso o no lo suficiente
    def animales (self):
        #Defino el atributo privado dormir solo para el metodo animales
        self.dormir  = int(input("Digite cuanto tiempo lleva su mascota durmiendo: "))
        #Evaluamos si el animal ya descanso o no lo suficiente
        if self.dormir > 10:
            print(" "+self.nombre+" ya debe despertar.")
            print(f"||||||||||| Ya descanso lo suficiente")
            print("-----------------------------------")
        else:
            print(" "+self.nombre+" debe seguir descansando.")
            print(f"|||||||||||  Aun no ha descansado lo suficiente ")
            print("-----------------------------------")
        

        
#Creamos los objetos a partir de instanciar la clase Animal     
objeto1 = Animal("Simba", "León", "7 años", "190 kg", "Sabana")
objeto2 = Animal("Pardo", "Oso", "10 años", "600 kg", "Bosques")
objeto3 = Animal("Ruby", "Gacela", "4 años", "50 kg", "Sabana")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.animales() #Método que evalua si ya comio elAnimal
objeto2.mostrar_detalles()
objeto2.animales()
objeto3.mostrar_detalles()
objeto3.animales()