class Car:
  def __init__(self, brand, model, year, mileage):
    # Tu código aquí 👈
    self.brand = brand
    self.model = model
    self.year = year
    self.mileage = mileage
    self.state = False
    
  def turnOn(self):
    self.state = True

  def turnOff(self):
    self.state = False

  def drive(self, km):
    if(self.state):
      self.mileage += km
    else:
      raise Exception("El auto está apagado")
    

"""
En este desafío, deberás crear la lógica para un automóvil mediante el uso de clases.

Deberás implementar la lógica necesaria en la clase Car de tal manera que nos pueda servir de base para crear nuevos autos que reciba los siguientes parametros:

brand: Marca del auto
model: Modelo del auto
year: Año del auto
mileage: kilometraje del auto
state: El estado por defecto del auto será false, indicando que el - auto se encuentra apagado.
Además, deberás implementar los siguientes métodos para hacer funcional los vehículos creados con la clase Car

turnOn(): Método que encenderá el auto.
turnOff(): Método que apagará el auto.
drive(kilometers): Con este método podremos aumentar el kilometraje según los kilómetros dados pero solo si el auto está encendido. En caso contrario, deberá mostrar el siguiente mensaje de error: "El auto está apagado".
Recuerda manejar los errores como una Exception

Ejemplo 1:

Input:
toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOn();
toyota.drive(100);
toyota.mileage


Output: 100

Ejemplo 2

toyota = Car("Toyota", "Corolla", 2020, 0);
toyota.turnOff()
toyota.drive(100)

Output: Exception: El auto está apagado
"""