class Computadora:
    def __init__(self, precio):
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio

class Laptop(Computadora):
    def calcular_precio_final(self):
        return self.precio * 1.1

class Desktop(Computadora):
    def calcular_precio_final(self):
        return self.precio * 1.2

class Tablet(Computadora):
    def calcular_precio_final(self):
        return self.precio * 1.05

# Ejemplo de uso:
laptop = Laptop(1000)
desktop = Desktop(1200)
tablet = Tablet(500)

print(f"El precio final de la laptop es: ${laptop.calcular_precio_final()}")
print(f"El precio final de la desktop es: ${desktop.calcular_precio_final()}")
print(f"El precio final de la tablet es: ${tablet.calcular_precio_final()}")