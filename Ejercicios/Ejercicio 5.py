if __name__ == "__main__":
    def fahrenheit_a_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print("{0} grados Fahrenheit son {1:.2f} grados Celsius".format(fahrenheit, celsius))