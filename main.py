import estrategiaVoraz as voraz;

def main():
    inputTxt = open("input.txt", 'r')
     
    A = int(inputTxt.readline())
    B = int(inputTxt.readline())
    n = int(inputTxt.readline())
    ofertas = ()

    # Se crea una tupla de tuplas leyendo el archivo inputTxt.txt
    for i in range(n + 1):
        p, max, min = inputTxt.readline().split(sep=', ')
        tupla = (int(p), int(max), int(min))
        ofertas += tuple([tupla])

    print("Acciones en venta " ,A)
    print("Precio minímo por acción ", B)
    print("Número de ofertantes ", n)
    print("Lista de ofertantes ", ofertas, "\n")

    algoritmo = int(input("¿Qué tipo de algoritmo desea utilizar?\n(1) Estrategia de Fuerza Bruta\n(2) Estrategia Voraz\n(3) Estrategia de Programación dinamica\n"))
    
    if (algoritmo == 1):
        print("Estrategia de fuerza bruta no disponible")
    elif(algoritmo == 2):
        voraz.accionesVoraz(A, B, n, ofertas)
    elif(algoritmo == 3):
        print("Estrategia de programación dinámica no disponible")
    else:
        print("Opción no válida")
    
if __name__ == '__main__':    
    main()