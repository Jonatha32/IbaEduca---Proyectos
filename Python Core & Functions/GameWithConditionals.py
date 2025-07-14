secret_number = 7
attempt = int(input("Adivina el numero secreto (entre 1 y 10): "))


if attempt == secret_number:
    print("¡Felicidades! Has adivinado el número secreto.")
elif attempt < secret_number:
    print("Demasiado bajo. Intenta de nuevo.")
else:
    print("Demasiado alto. Intenta de nuevo.")