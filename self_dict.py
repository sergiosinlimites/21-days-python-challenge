class MyDict:
  def __init__(self):
    # Tu código aquí 👇
    self.data = {}
    self.length = 0

  def append(self, item):
    # Tu código aquí 👇
    self.data[self.length] = item
    self.length += 1

  def pop(self):
    # Tu código aquí 👇
    self.length -= 1
    return self.data.pop(max(self.data.keys()))

  def shift(self):
    # Tu código aquí 👇
    self.length -= 1
    first = self.data[0]
    self.data = {key-1: value for key, value in self.data.items() if key != 0 }
    return first

  def unshift(self, item):
    # Tu código aquí 👇
    self.length += 1
    self.data = {key-1: value for key, value in self.data.items()}
    self.data[0] = item
      

  def map(self, func):
    # Tu código aquí 👇
    map_data = MyDict()
    for i in range(len(self.data)):
      map_data.append(func(self.data[i]))
    return map_data

  def filter(self, func):
    # Tu código aquí 👇
    filter_data = MyDict()
    for i in range(len(self.data)):
      if(func(self.data[i])):
        filter_data.append(self.data[i])

    return filter_data

  def join(self, character=","):
    # Tu código aquí 👇
    result = ""
    for i in range(len(self.data)):
      if(i == len(self.data) - 1):
        result += str(self.data[i])
      else:
        result += str(self.data[i]) + (character)

    return result

"""
Ejemplo 1:

Input:

myDict = MyDict()
myDict.append("a")
myDict.append("b")
myDict.append("c")

print(myDict.data)

Output:

{0: 'a', 1: 'b', 2: 'c'}
Ejemplo 2:

Input:

myDict = MyDict()
myDict.append("Platzinauta")
myDict.unshift("Hola!")

print(myArray.data)

Output:
{0: "Hola!", 1: "Platzinauta"}
"""