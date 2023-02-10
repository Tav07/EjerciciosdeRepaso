if __name__ == "__main__":
    cantidad_numeros = 10
    suma = 0

    for i in range(cantidad_numeros):
        num = float(input("Ingrese un número: "))
        suma = suma + num

    media = suma / cantidad_numeros

    print("La media aritmética de los", cantidad_numeros, "números es", media)