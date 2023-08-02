class Animal:
  def __init__(self, name, age, specie):
    # Tu código aquí 👇
    self.name = name
    self.age = age
    self.specie = specie

  def getInfo(self):
    return {
      "name": self.name,
      "age": self.age,
      "specie": self.specie
    }
  
class Mammal(Animal):
  def __init__(self, name, age, specie, hasFur):
    # Tu código aquí 👇
    super().__init__(name, age, specie)
    self.hasFur = hasFur
  
  def getInfo(self):
    info = super().getInfo()
    info.update({ "hasFur": self.hasFur })
    return info

class Dog(Mammal):
  def __init__(self, name, age, breed):
    # Tu código aquí 👇
    super().__init__(name, age, "dog", True)
    self.breed = breed

  def getInfo(self):
    return {
      "name": self.name,
      "age": self.age,
      "specie": self.specie,
      "hasFur": self.hasFur,
      "breed": self.breed
    }
  
  def bark(self):
    return "woof!"

"""
Ejemplo 1

Input:
bird = Animal("pepe", 1, "bird")
bird.getInfo()

Output:

{
  "name": "pepe",
  "age": 1,
  "specie": "bird",
}

Ejemplo 2

Input:
hippo = Mammal("bartolo", 3, "hippo", false)
hippo.getInfo()

Output:

{
  "name": "bartolo",
  "age": 3,
  "specie": "hippo",
  "hasFur": false,
}

Ejemplo 3

Input:
dog = Dog("fido", 4, "pastor aleman");
dog.bark()

Output:
"woof!"
"""