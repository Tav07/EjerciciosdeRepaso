if __name__ == "__main__":
    datos = []

    for i in range(5):
        dato = input("Ingresa el dato {}: ".format(i + 1))
        datos.append(dato)

    datos_invertidos = datos[::-1]

    print("Los datos invertidos son:")
    for dato in datos_invertidos:
        print(dato)