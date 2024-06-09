class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

mi_perro = Perro("Firulais")
mi_gato = Gato("Pelusa")

print(mi_perro.nombre + " dice: " + mi_perro.hacer_sonido())
print(mi_gato.nombre + " dice: " + mi_gato.hacer_sonido())