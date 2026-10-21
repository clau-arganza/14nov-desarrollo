from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, other):
        if isinstance(other, Fraccion):
            numerador = (
                self.numerador * other.denominador
                + other.numerador * self.denominador
            )
            denominador = self.denominador * other.denominador
            return Fraccion(numerador, denominador)

        raise TypeError("La suma solo se puede realizar entre fracciones.")

    def simplificar(self):
        divisor = gcd(self.numerador, self.denominador)
        numerador = self.numerador // divisor
        denominador = self.denominador // divisor

        if denominador < 0:
            numerador = -numerador
            denominador = -denominador

        return Fraccion(numerador, denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


f1 = Fraccion(1, 6)
f2 = Fraccion(1, 3)
resultado = f1 + f2

print(resultado)
print(resultado.simplificar())
print(Fraccion(8, 12).simplificar()) 