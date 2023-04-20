import sys
import os
import time

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.insert(0, root_dir)

from main import *

if __name__ == '__main__':
    main()

def estrategiaVoraz(A: int, B: int, n: int, ofertas: tuple[oferta]):
    def valor(asignaciones: tuple[tuple], ofertas: tuple[oferta]):
        val = 0
        for i, oferta in enumerate(ofertas):
            val += (oferta[0] * asignaciones[i])
            # print("asig:" , asignaciones[i], " valor: ", val)
        return val

    def calculo(A,B,n,ofertas):
        asignaciones = []
        for oferta in ofertas:
            accion = 0
            if (oferta[2] <= A):
                A -= oferta[2]
                accion = oferta[2]
                while (accion < oferta[1] and A):
                    A -= 1
                    accion += 1
            asignaciones.append(accion)
        return asignaciones, valor(asignaciones, ofertas)

            # if (A >= oferta[1]):
            #     A -= oferta[1]
            #     asignaciones.append(oferta[1])
            #     print(A)
            #     print(asignaciones)
            # elif (oferta[1]>=A<=oferta[2]):
            #     acciones = 0
            #     while (A >= oferta[2]):
            #         A -= 1
            #         acciones += 1
            #     asignaciones.append(acciones)
            # else:
            #     asignaciones.append(0)

    if n == 0:
        return [A], B * A
    else:
        return calculo(A,B,n,ofertas)

def accionesVoraz():
    with open("outputVoraz.txt", 'w') as write_file:
        solucion, valorSolucion = estrategiaVoraz(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))

accionesVoraz()