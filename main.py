import estrategiaFuerzaBruta as fuerzaBruta
import estrategiaVoraz as voraz
import estrategiaDinamica1 as dinamica1
import estrategiaDinamica2 as dinamica2
import easygui as eg
from tkinter.filedialog import askopenfilename


def main():
    archivo = eg.fileopenbox(msg='Seleccione el archivo de entrada',
                             title='Programación de venta de acciones',
                             default="ADAII_ejemplos_bsp2/*.sub",
                             filetypes=["*.sub", "*.psub"],
                             multiple=False,
                             )

    inputTxt = open(archivo, 'r')

    A = int(inputTxt.readline())
    B = int(inputTxt.readline())
    n = int(inputTxt.readline())
    ofertas = ()

    # Se crea una tupla de tuplas leyendo el archivo inputTxt.txt
    for i in range(n + 1):
        p, max, min = inputTxt.readline().split(sep=',')
        tupla = (int(p), int(max), int(min))
        ofertas += tuple([tupla])

    choicesSub = ('Estrategia de Fuerza Bruta', 'Estrategia Voraz',
                  'Estrategia de Programación dinámica')
    choicesPsub = ('Estrategia de Programación dinámica modificado',)

    algoritmo = eg.indexbox(msg='Bienvenido al programa para calcular la venta de acciones \n\nAcciones en venta: ' + str(A) + '\nPrecio minímo por acción: ' + str(B) + '\nNúmero de oferentes: ' + str(n) + '\nLista de oferentes incluyendo gobierno(limitado a 158 caracteres): \n' + str(ofertas)[0:158] + '\n\nSeleccione el algoritmo a utilizar',
                            title='Programación de venta de acciones',
                            choices= choicesSub if archivo.endswith('.sub') else choicesPsub,
                            image = "images/dynamic_programming.jpg",)

    if (algoritmo == 0):
        fuerzaBruta.accionesFB(A, B, n, ofertas)
    elif (algoritmo == 1):
        voraz.accionesV(A, B, n, ofertas)
    elif (algoritmo == 2):
        dinamica1.accionesPD1(A, B, n, ofertas)
    elif (algoritmo == 3):
        dinamica2.accionesPD2(A, B, n, ofertas)
    else:
        eg.msgbox(msg = 'Opción no válida',
                  title='Programación de venta de acciones', ok_button='Continuar')


if __name__ == '__main__':
    main()
