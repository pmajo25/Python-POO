#Clase Producto con atributos encapsulados o privados
class Producto:
    #Metodo constructor
    def __init__(self,nombres,precio,cantidad,categoria):
        self.__nombres = nombres #privado
        self.__precio = precio #privado
        self.cantidad = cantidad #publico
        self.categoria = categoria #publico
        
    #Metodo getter
    def obtener_nombres(self):
        return self.__nombres
    
    #Metodo getter
    def obtener_precio(self):
        return self.__precio
    
    #Metodo setter
    def establecer_nombres(self, nuevo_nombres):
        self.__nombres=nuevo_nombres
        
    #Metodo setter
    def establecer_precios(self, nuevo_precios):
        self.__precio=nuevo_precios  
        
        
    #Metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombres: {self.__nombres}")
        print(f"Precio: {self.__precio} pesos")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoria: {self.categoria}")
        
#objeto
producto = Producto("iphone 14",1300000,"3","Smartphone")
    
    
#Imprimir atributos publicos y privados
producto.mostrar_detalles()
    
print("-------------------------")
    
#Imprimir el atributo encapsulado modificado su acceso con getter y setter
producto.establecer_nombres("iphone 15") #setter
print(f"Nombres: { producto.obtener_nombres() }") #getter
producto.establecer_precios("5199000") #setter
print(f"Precio: { producto.obtener_precio() }") #getter
print(f"Cantidad: { producto.cantidad }") #getter
print(f"Categoria: { producto.categoria }") #publico
