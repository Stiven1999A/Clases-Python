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

# Ejemplo cuenta bancaria

class Cuenta_Bancaria:
  def __init__(self, titular, saldo_inicial):
    self.titular = titular
    self.__saldo= saldo_inicial
    
    def depositar(self, cantidad):
      self.__saldo += cantidad
      print("Deposito exitoso, el saldo actual es " + str(self.__saldo))

    def retirar(self, cantidad):
      if cantidad >0 and cantidad <= self.__saldo:
        self.__saldo -= cantidad
        print("Retiro exitoso, el saldo actual es: " + str(self.__saldo))

    def obtener_saldo(self):
      return self.__saldo

cuenta_estiben = Cuenta_Bancaria("Estiben", saldo_inicial=5000)

print(cuenta_estiben.obtener_saldo())