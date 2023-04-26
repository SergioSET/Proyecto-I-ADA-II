from main import *
import time
import easygui as eg
import os

if __name__ == '__main__':
    main()


def estrategiaVoraz(A: int, B: int, n: int, ofertas: tuple):
    asignacion = tuple
    asignaciones = tuple

    def valor(asignaciones: tuple, ofertas: tuple):
        val = 0
        for i, oferta in enumerate(ofertas):
            val += (oferta[0] * asignaciones[i])
        return val

    # def calculo(A, B, n, ofertas):
    #     asignaciones = []
    #     for oferta in ofertas:
    #         accion = 0
    #         if (oferta[2] <= A):
    #             A -= oferta[2]
    #             accion = oferta[2]
    #             while (accion < oferta[1] and A):
    #                 A -= 1
    #                 accion += 1
    #         asignaciones.append(accion)
    #     return asignaciones, valor(asignaciones, ofertas)

    def calculo(A, B, n, ofertas):
        asignaciones = []
        for oferta in ofertas:
            accion = 0
            if oferta[2] <= A:
                accion = oferta[2]
                A -= oferta[2]
                if oferta[1] - oferta[2] <= A:
                    accion += oferta[1] - oferta[2]
                    A -= oferta[1] - oferta[2]
                else:
                    accion += A
                    A = 0
            asignaciones.append(accion)
        return asignaciones, valor(asignaciones, ofertas)

    if n == 0:
        return [A], B * A
    else:
        return calculo(A, B, n, ofertas)


def accionesV(A: int, B: int, n: int, ofertas: tuple):
    eg.msgbox(msg='Se iniciará el algoritmo de Estrategia Voraz, puede presionar el botón "Continuar", un mensaje aparecerá cuando el algoritmo haya finalizado',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    inicio2 = time.time()
    with open("outputVoraz.txt", 'w') as write_file:
        solucion, valorSolucion = estrategiaVoraz(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))
    fin2 = time.time()
    eg.msgbox(msg='Tiempo de ejecución del algoritmo voraz: ' + str(fin2 - inicio2) + ' segundos\n\nSe ha finalizado el algoritmo de Estrategia Voraz, se abrirá el archivo outputVoraz.txt con la solución encontrada',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    os.startfile("outputVoraz.txt", operation='open')
