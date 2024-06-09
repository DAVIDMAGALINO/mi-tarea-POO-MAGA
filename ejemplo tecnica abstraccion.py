import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2


# Función principal
def main():
    radio = float(input("Ingresa el radio del círculo: "))
    circulo = Circulo(radio)

    print(f"El área del círculo con radio {circulo.radio} es: {circulo.area()}")


if __name__ == "__main__":
    main()