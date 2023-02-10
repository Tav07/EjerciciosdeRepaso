if __name__ == "__main__":
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    num = int(input("Ingresa un número para calcular su factorial: "))
    resultado = factorial(num)
    print("El factorial de {} es: {}".format(num, resultado))