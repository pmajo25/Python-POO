# Defino la clase
class Figuras:
    # Método constructor
    def init(self, nombre, lados,color, area, perimetro):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.lados = lados
        self.color = color 
        self.area = area
        self.perimetro = perimetro
        
    # Métodos para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de las figuras")
        print("Nombre: " + self.nombre)
        print("Número de lados: " + str(self.lados))
        print("Color de la figura:" +str(self.color))
        print("Área: " + str(self.area))
        print("Perímetro: " + str(self.perimetro))
        print("--------------------------------")
        
    # Método para calcular el perímetro de un triangulo
    def calcular_perimetro(self): 
        if self.nombre.lower() == "triangulo":
            lado = float(input("Digite la longitud de un lado del triangulo: "))
            if lado > 0:
                self.perimetro = 4 * lado
                print(f"El perímetro del {self.nombre} es {self.perimetro} unidades.")
                print("----------------------------------------------")
            else:
                print("El valor ingresado no es válido.")
        else:
            print(f"El cálculo del perímetro no está implementado para {self.nombre}.")
    
# Creamos los objetos a partir de instanciar la clase Figuras        
figura1 = Figuras("triangulo", 3, "azul", 10)
figura2 = Figuras("triángulo", 3, "18.8 unidades", 18)
figura3 = Figuras("círculo", 0, "78.5 unidades", 31.4)

# Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura1.calcular_perimetro()  # Solo calcula el perímetro del cuadrado
figura2.mostrar_detalles()
figura3.mostrar_detalles()