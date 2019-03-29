# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(pi * (self.radio**2),2)

    def perimetro(self):
        return round(2*pi*self.radio,2)

cir = Circulo(3)
assert(cir.area()) == 28.27
assert(cir.perimetro()) == 18.85
