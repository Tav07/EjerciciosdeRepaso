if __name__ == "__main__":
    suma = 0

    while True:
        numero = int(input("Ingresa un número: "))
        suma += numero
        continuar = input("¿Deseas ingresar otro número? (si/no) ")
        if continuar.lower() != "si":
            break

    print("La suma de los números ingresados es:", suma)