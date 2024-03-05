class Persona:
    #This is known as the class constructor
    def __init__(self, name: str, age: int, occupation: str) -> None:
        self.name = name
        self.age = age
        self.occupation = occupation

    def to_introduce_oneself(self):
        print(f"Hi!, my name is {self.name}, I am {self.age} years old and I work as a/an {self.occupation}.") 

Estiben = Persona(name = 'Estiben', age = 20, occupation = 'student')         
print(Estiben.to_introduce_oneself())

Isa = Persona(name = 'Isa', age = 20, occupation = 'Student')
print(Isa.to_introduce_oneself())


class Animal:
  def __init__(self, nombre) -> None:
    self.nombre = nombre

  def hacer_sonido(self):
    pass

class Perro(Animal):

  def hacer_sonido(self):
    return 'GUAUUUUU'

class Gato(Animal):

  def hacer_sonido(self):
    return 'MIAUUUUU'

gato = Gato('Doraemon')
perro = Perro('Ayudante de Santa')

print(f'Mi gato se llama {gato.nombre} y hace {gato.hacer_sonido()}')
print(f'Mi perro se llama {perro.nombre} y hace {perro.hacer_sonido()}')

class Animal:
  def __init__(self, nombre) -> None:
    self.nombre = nombre

  def hacer_sonido(self):
    pass

class Perro(Animal):

  def hacer_sonido(self):
    return 'GUAUUUUU'

class Gato(Animal):

  def hacer_sonido(self):
    return 'MIAUUUUU'

gato = Gato('Doraemon')
perro = Perro('Ayudante de Santa')

print(f'Mi gato se llama {gato.nombre} y hace {gato.hacer_sonido()}')
print(f'Mi perro se llama {perro.nombre} y hace {perro.hacer_sonido()}')    