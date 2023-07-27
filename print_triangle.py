def print_triangle(size, character):
    # Tu código aquí 👈
    triangle = ""
    num = 2 * size - 1
    for i in range(size):
        triangle += "_" * (size - i - 1)
        triangle += character * 2 * (i + 1)
        triangle += "_" * (size - i - 1)
        triangle += "\n"

    print(triangle)
    return triangle


print_triangle(6, "$")