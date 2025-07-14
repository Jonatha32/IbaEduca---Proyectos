entrada = input("Ingresa números separados por comas: ")
numeros = list(map(int, entrada.split(",")))
pair = [n for n in numeros if n % 2 == 0]
print("Números pares:", pair)