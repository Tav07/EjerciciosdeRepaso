if __name__ == "__main__":
    import random

    cantidad = int(input("¿Cuántos números aleatorios quieres ver? "))
    numeros = [random.randint(1, 1000) for i in range(cantidad)]
    print("Los números aleatorios son:", numeros)