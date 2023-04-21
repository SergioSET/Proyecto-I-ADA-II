from main import *
import time
import easygui as eg
import os

if __name__ == '__main__':
    main()


def estrategiaFuerzaBruta(A: int, B: int, n: int, ofertas: tuple):
    asignacion = tuple
    asignaciones = tuple

    # une la asignacion recibida a cada asignacion de la tupla recibida
    def productoCartElemento(element: asignacion, tupla: asignaciones) -> asignaciones:
        return tuple(element + element2 for element2 in tupla)

    # calcula el valor de la asignacion de acciones recibida como parametro
    def valorAsig(asignacion: tuple[int]):
        resultado = 0
        for i, cantAcciones in enumerate(asignacion):
            resultado += cantAcciones * ofertas[i][0]
        return resultado

    def licitacion(A: int, B: int, n: int, ofertas: tuple) -> asignaciones:
        p, c, r = ofertas[0]

        def noIncluirOfertaActual() -> asignaciones:
            return productoCartElemento((0,), licitacion(A, B, n - 1, ofertas[1:]))

        def incluirOfertaActual() -> asignaciones:
            return productoCartElemento((c,), licitacion(A-c, B, n - 1, ofertas[1:]))

        if n == 0:
            return ((A,),)
        elif A >= c:
            return noIncluirOfertaActual() + incluirOfertaActual()
        else:
            return noIncluirOfertaActual()

    soluciones = licitacion(A, B, n, ofertas)
    valorSoluciones = map(valorAsig, soluciones)
    pos, maxValor = 0, A * B
    for indice, valor in enumerate(valorSoluciones):
        if valor > maxValor:
            pos, maxValor = indice, valor
    return soluciones


def accionesFB(A: int, B: int, n: int, ofertas: tuple):
    with open("outputFuerzaBruta.txt", 'w') as write_file:
        solucion, valorSolucion = estrategiaFuerzaBruta(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))


# accionesFB()
def accionesFuerzaBruta(A: int, B: int, n: int, ofertas: tuple):
    eg.msgbox(msg='Se iniciará el algoritmo de Fuerza Bruta, puede presionar el botón "Continuar", un mensaje aparecerá cuando el algoritmo haya finalizado',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    inicio = time.time()
    # print(all(map(lambda x: sum(x) == 1000, estrategiaFuerzaBruta(A, B, n, ofertas))))
    with open("outputFuerzaBruta.txt", 'w') as write_file:
        for line in estrategiaFuerzaBruta(A, B, n, ofertas):
            write_file.write("{0}\n".format(line))
    fin = time.time()
    eg.msgbox(msg='Tiempo de ejecución del algoritmo Fuerza Bruta: ' + str(fin - inicio) + ' segundos\n\nSe ha finalizado el algoritmo de Fuerza Bruta, se abrirá el archivo outputFuerzaBruta.txt con la solución encontrada',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    os.startfile("outputFuerzaBruta.txt", operation='open')
# Ejecución del algoritmo de fuerza bruta
# fuerzaBruta(A, B, n, ofertas)
