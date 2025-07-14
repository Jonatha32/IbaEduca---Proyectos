from functools import reduce

# MAP: aplica una función a cada elemento
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))

# FILTER: filtra elementos según condición
pares = list(filter(lambda x: x % 2 == 0, numeros))

# REDUCE: aplica acumulación de izquierda a derecha
suma = reduce(lambda x, y: x + y, numeros)

print("cuadrados:", cuadrados)
print("pares:", pares)
print("suma:", suma)
