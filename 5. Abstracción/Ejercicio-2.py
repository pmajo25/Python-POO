"""
Crea una clase abstracta Empleado con un método abstracto calcular_salario(). 
Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.
"""

from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
        

    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, pago_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
       
    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

# Uso de las clases
empleado1 = EmpleadoTiempoCompleto(3000)
print(f"El salario del empleado a tiempo completo es de: {empleado1.calcular_salario()}")

empleado2 = EmpleadoPorHoras(120, 15)
print(f"El salario del empleado por horas es de: {empleado2.calcular_salario()}")
