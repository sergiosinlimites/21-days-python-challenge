def my_map(list, func):
  return [func(el) for el in list]

my_map([1, 2, 3, 4], lambda num: num * 2)

# Output: [2, 4, 6, 8]