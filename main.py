from os import system
import estrategiaVoraz as voraz;
import estrategiaFuerzaBruta as fuerzaBruta;

def main():
    inputTxt = open("input.txt", 'r')
     
    A = int(inputTxt.readline())
    B = int(inputTxt.readline())
    n = int(inputTxt.readline())
    ofertas = ()

    # Se crea una tupla de tuplas leyendo el archivo inputTxt.txt
    for i in range(n):
        print(inputTxt.readline().split())
        # p, max, min = inputTxt.readline().split(sep=',')
        # tupla = (int(p), int(max), int(min))
        # ofertas += tuple([tupla])

    # system("cls")
    print("Acciones en venta " ,A)
    print("Precio minímo por acción ", B)
    print("Número de oferente ", n)
    print("Lista de oferentes incluyendo gobierno ", ofertas, "\n")

    algoritmo = int(input("¿Qué tipo de algoritmo desea utilizar?\n(1) Estrategia de Fuerza Bruta\n(2) Estrategia Voraz\n(3) Estrategia de Programación dinamica\n"))
    
    if (algoritmo == 1):
        fuerzaBruta.accionesFuerzaBruta(A, B, n, ofertas)
    elif(algoritmo == 2):
        voraz.accionesVoraz(A, B, n, ofertas)
    elif(algoritmo == 3):
        print("Estrategia de programación dinámica no disponible")
    else:
        print("Opción no válida")
    
if __name__ == '__main__':    
    main()