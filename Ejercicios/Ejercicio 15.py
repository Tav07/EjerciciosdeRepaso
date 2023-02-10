if __name__ == "__main__":
    cadena = input("Ingrese una cadena de texto: ")

    cadena_invertida = cadena[::-1]

    if cadena == cadena_invertida:
        print("La cadena es un palíndromo")
    else:
        print("La cadena no es un palíndromo")