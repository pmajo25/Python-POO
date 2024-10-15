"""
Crea una clase abstracta Empleado con un método abstracto calcular_salario(). 
Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.
"""

from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta EmpleadoTiempoCompleto
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta EmpleadoPorHoras
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

# Uso de las clases
empleado_tiempo_completo = EmpleadoTiempoCompleto("Andres", 1000000)
print(f"Salario de {empleado_tiempo_completo.nombre} es de: {empleado_tiempo_completo.calcular_salario()}")

empleado_por_horas = EmpleadoPorHoras("Pablo", 24, 10000)
print(f"Salario de {empleado_por_horas.nombre} es de: {empleado_por_horas.calcular_salario()}")

