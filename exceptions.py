def calculate_average(numbers):
  # Tu código aquí 👈
  try:
    if(len(numbers) == 0):
      raise ValueError("La lista está vacía")

    else: return sum(numbers) / len(numbers)

  except TypeError:
    raise TypeError("La lista contiene elementos no numéricos")

"""
Ejemplo 1:

Input: calculate_average([1, 2, 3, 4, 5])
Output: 3.0

Ejemplo 2:

Input: calculate_average([10, 20, 30, 40, 50])
Output: 30.0

Ejemplo 3:

Input: calculate_average([])
Output: ValueError: La lista está vacía

Ejemplo 4:

Input: calculate_average([1, 2, '3', 4, 5])
Output: TypeError: La lista contiene elementos no
"""

def calculate_discounted_price(price, discount):
  # Tu código aquí 👈
  try:
    if(price < 0 or discount < 0):
      raise ValueError("El precio y el descuento deben ser valores positivos")
    else:
      return price * (1 - discount)
  except TypeError:
    raise TypeError("El precio y el descuento deben ser números")
  except ValueError as va:
    raise va
  except Exception as ex:
    raise Exception("Ha ocurrido un error inesperado", ex)

""""
Ejemplo 1:


Input: calculate_discounted_price(100, 0.2)
Output: 80.0

Ejemplo 2:


Input: calculate_discounted_price(-50, 0.2)
Output: ValueError: El precio y el descuento deben ser valores po
"""