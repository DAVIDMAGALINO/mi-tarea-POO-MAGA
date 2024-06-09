class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Acceder a los atributos de la persona de forma segura
print(persona1.get_nombre())
print(persona1.get_edad())

# Modificar los atributos de la persona de forma segura
persona1.set_nombre("Pedro")
persona1.set_edad(35)

print(persona1.get_nombre())
print(persona1.get_edad())