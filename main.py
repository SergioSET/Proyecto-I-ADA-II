import estrategiaVoraz as voraz
import estrategiaFuerzaBruta as fuerzaBruta
import easygui as eg


def main():
    inputTxt = open("input.txt", 'r')

    A = int(inputTxt.readline())
    B = int(inputTxt.readline())
    n = int(inputTxt.readline())
    ofertas = ()

    # Se crea una tupla de tuplas leyendo el archivo inputTxt.txt
    for i in range(n + 1):
        p, max, min = inputTxt.readline().split(sep=',')
        tupla = (int(p), int(max), int(min))
        ofertas += tuple([tupla])

    eg.msgbox(msg='Bienvenido al programa para calcular la venta de acciones \nAcciones en venta: ' + str(A) + '\nPrecio minímo por acción: ' + str(B) + '\nNúmero de oferentes: ' + str(n) + '\nLista de oferentes incluyendo gobierno: \n' + str(ofertas),
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)

    algoritmo = eg.indexbox(msg='¿Qué tipo de algoritmo desea utilizar?',
                            title='Programación de venta de acciones',
                            choices=('Estrategia de Fuerza Bruta', 'Estrategia Voraz',
                                     'Estrategia de Programación dinámica'),
                            image="images/dynamic_programming.jpg",)

    # algo = {'Estrategia de Fuerza Bruta': 1, 'Estrategia Voraz': 2,
    #         'Estrategia de Programación dinámica': 3}
    # algoritmo = algo.get(algoritmo, 0)

    if (algoritmo == 0):
        fuerzaBruta.accionesFuerzaBruta(A, B, n, ofertas)
    elif (algoritmo == 1):
        voraz.accionesVoraz(A, B, n, ofertas)
    elif (algoritmo == 2):
        print("Estrategia de programación dinámica no disponible")
    else:
        eg.msgbox(msg='Opción no válida',
                  title='Programación de venta de acciones', ok_button='Continuar')


if __name__ == '__main__':
    main()
