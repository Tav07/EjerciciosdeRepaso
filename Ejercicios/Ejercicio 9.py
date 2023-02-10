if __name__ == "__main__":
    import random

    filas = 3
    columnas = 3

    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = random.randint(0, 100)
            fila.append(numero)
        matriz.append(fila)

    print("La matriz de números aleatorios es:")
    for fila in matriz:
        print(fila)