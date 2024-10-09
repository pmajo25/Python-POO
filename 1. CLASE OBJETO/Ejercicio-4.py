#Defino la clase
class Empleados:
    #Método constructor
    def __init__(self,nombre, cargo, salario, edad, departamento):
        #Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad
        self.salario = salario
        self.departamento = departamento 
        
    #Metodo para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Informacion del Empleado")
        print("Nombre: " + self.nombre)
        print("Cargo: " + self.cargo)
        print("Edad: " + self.edad)
        print("Salario: " + self.salario)
        print("Departamento: " + self.departamento)
        print("--------------------------")
        
    #Método para saber si el empleado ya tomo notas
    def notas (self):
        #Defino el atributo privado nota solo para el metodo notas 
        self.nota  = int(input("Digite cuantas horas llevas sin tomar notas: "))
        #Evaluamos si el empleado ya debe tomar o no las notas
        if self.nota > 2:
            print(" "+self.nombre+" ya se han cumplido las horas.")
            print(f"||||||||||| Debes tomar nota y actualizar datos ")
            print("-----------------------------------")
        else:
            print(" "+self.nombre+" aun falta para tomar nueva nota.")
            print(f"|||||||||||  recueda que debes tomar nota cada 2 hora ")
            print("-----------------------------------")
        

        
#Creamos los objetos a partir de instanciar la clase Empleado     
objeto1 = Empleados("Carlos", "Fabrica", "4000 USD", "30 años", "Fabricación")
objeto2 = Empleados("Adriana", "Jefe de cocina", "5000 USD", "25 años", "Cocina")
objeto3 = Empleados("Lucia", "Jefe de enfermeria", "3500 USD", "29 años", "Enfermeria")

#Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.notas() #Método que evalua si ya tomo notas el empleado
objeto2.mostrar_detalles()
objeto2.notas()
objeto3.mostrar_detalles()
objeto3.notas()