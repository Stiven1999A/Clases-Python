import math

class Figura:
  def __init__(self, color) -> None:
    self.color = color

  def calcular_area(self):
    pass

class Triangulo(Figura):
  def __init__(self, nombre, color, base, altura):
    super().__init__(color)
    self.base = base
    self.altura = altura
    self.nombre = nombre

  def calcular_area(self):
    return (self.base * self.altura) / 2 

class Rectangulo(Figura):
  def __init__(self, nombre, color, base, altura):
    super().__init__(color)
    self.base = base
    self.altura = altura
    self.nombre = nombre

  def calcular_area(self):
    return self.base * self.altura

class Circulo(Figura):
  def __init__(self, nombre, color, radio):
    super().__init__(color)
    self.radio = radio
    self.nombre = nombre

  def calcular_area(self):
    return math.pi * (self.radio ** 2)
  
t = Triangulo(nombre='triangulo', color='Azul', base=3, altura=3)
r = Rectangulo(nombre='rectangulo', color='Rojo', base=4, altura=5)
c = Circulo(nombre='circulo', color='Verde', radio=2)

print(f"El {t.nombre} que elegiste es de color {t.color} y tiene un area de {t.calcular_area()}")
                                                                                                                                                