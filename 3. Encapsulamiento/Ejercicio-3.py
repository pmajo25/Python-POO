#Clase Libro con atributos encapsulados o privados
class Libro:
    #Metodo constructor
    def __init__(self,titulo,autor,isbn,editorial):
        self.__titulo = titulo #privado
        self.__autor = autor #privado
        self.__isbn = isbn #privado
        self.editorial = editorial #publico
        
        
    #Metodo getter
    def obtener_titulo(self):
        return self.__titulo
    
    #Metodo getter
    def obtener_autor(self):
        return self.__autor
    
    #Metodo getter
    def obtener_isbn(self):
        return self.__isbn
    
    #Metodo setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo=nuevo_titulo
        
    #Metodo setter
    def establecer_autor(self, nuevo_autor):
        self.__autor=nuevo_autor  
        
    #Metodo setter
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn=nuevo_isbn  
        
        
    #Metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nTitulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")
#objeto
libro = Libro("Cien años de soledad","Gabriel Garcia Márquez",978555555,"Editorial Sudamericana")
    
    
#Imprimir atributos publicos y privados
libro.mostrar_detalles()
    
print("-------------------------")
    
#Imprimir el atributo encapsulado modificado su acceso con getter y setter
libro.establecer_titulo("El tunel") #setter
print(f"Titulo: { libro.obtener_titulo() }") #getter
libro.establecer_autor("Ernesto Sabato") #setter
print(f"Autor: { libro.obtener_autor() }") #getter
libro.establecer_isbn("9781154222") #setter
print(f"ISBN: { libro.obtener_isbn() }") #getter
print(f"Editorial: { libro.editorial }") #publico