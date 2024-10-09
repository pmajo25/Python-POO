"""
Ejercicio 3: Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea(). 
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el método realizar_tarea() de manera específica según su especialidad.
"""

from abc import ABC, abstractmethod

# Definir la clase abstracta con un método abstracto
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase Ingeniero que hereda de TareaEmpleado
class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelido = apellido

    def realizar_tarea(self):
        return f"{self.nombre} {self.apelido} está realizando su nuevo proyecto en python."

# Clase Doctor que hereda de TareaEmpleado
class Doctor(TareaEmpleado):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelido = apellido

    def realizar_tarea(self):
        return f"{self.nombre} {self.apelido} está evaluando el estado de salud de su paciente."

# Uso de las clases
ingeniero = Ingeniero("María", "Paternina")
print(f"La ingeniera: {ingeniero.realizar_tarea()}")

doctor = Doctor("Juan", "Vargas")
print(f"El doctor: {doctor.realizar_tarea()}")