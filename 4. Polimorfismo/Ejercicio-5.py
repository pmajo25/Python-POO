''' Crea tres clases: Medico, Ingeniero y Docente, cada una con un método trabajar()
    que describa el tipo de Profesion y una función para mostrar el polimorfismo describir_profesion() '''
# Clase Médico
class Medico:
    def __init__(self, especialidad, hospital, años_experiencia):
        self.especialidad = especialidad
        self.hospital = hospital
        self.años_experiencia = años_experiencia

    def trabajar(self):
        print(f"---------------------------------")
        print(f"Soy un médico especializado en {self.especialidad}")
        print(f"trabajo en el hospital {self.hospital}")
        print(f"y tengo {self.años_experiencia} años de experiencia.")
        print(f"---------------------------------")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, rama, empresa, proyectos_realizados):
        self.rama = rama
        self.empresa = empresa
        self.proyectos_realizados = proyectos_realizados

    def trabajar(self):
        print(f"Soy un ingeniero de {self.rama}")
        print(f"trabajo en la empresa {self.empresa}")
        print(f"y he realizado {self.proyectos_realizados} proyectos exitosos.")
        print(f"---------------------------------")

# Clase Docente
class Docente:
    def __init__(self, materia, nivel_educativo, años_enseñanza):
        self.materia = materia
        self.nivel_educativo = nivel_educativo
        self.años_enseñanza = años_enseñanza

    def trabajar(self):
        print(f"Soy un docente de {self.materia}")
        print(f"enseño en el nivel {self.nivel_educativo}")
        print(f"y tengo {self.años_enseñanza} años de experiencia en la enseñanza.")
        print(f"---------------------------------")

# Función que utiliza polimorfismo para describir el trabajo de cada profesional
def describir_profesion(profesional):
    profesional.trabajar()

# Instancias de cada clase
medico = Medico("Cardiología", "Hospital Central", 15)
ingeniero = Ingeniero("Sistemas", "Tech Solutions", 10)
docente = Docente("Matemáticas", "Secundaria", 8)

# Llamado al método trabajar para cada objeto usando polimorfismo
describir_profesion(medico)
describir_profesion(ingeniero)
describir_profesion(docente)