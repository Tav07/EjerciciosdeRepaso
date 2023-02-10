if __name__ == "__main__":
    numeros = []

    for i in range(10):
        numero = int(input("Ingresa el número {}: ".format(i + 1)))
        numeros.append(numero)

    print("El número más pequeño es:", min(numeros))
    print("El número más grande es:", max(numeros))