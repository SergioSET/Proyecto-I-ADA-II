from os import system

def main():
    input = open("input.txt", 'r')
    

    A = int(input.readline())
    B = int(input.readline())
    n = int(input.readline())
    ofertas = ()

    # Se crea una tupla de tuplas leyendo el archivo input.txt
    for i in range(n + 1):
        p, max, min = input.readline().split(sep=', ')
        tupla = (int(p), int(max), int(min))
        ofertas += tuple([tupla])

    print(A)
    print(B)
    print(n)
    print(ofertas, "\n")

    algoritmo = input('Hola')
    # algoritmo = input("¿Qué tipo de algoritmo desea utilizar?",
    # "\n", "(1) Estrategia de Fuerza Bruta",
    # "\n", "(2) Estrategia Voraz",
    # "\n", "(3) Estrategia de Programación dinamica")
    print(algoritmo)


if __name__ == '__main__':
    main()