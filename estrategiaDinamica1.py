from main import *
import time
import easygui as eg
import os
import numpy as np

if __name__ == '__main__':
    main()


def programacionDinamica(A: int, B: int, n: int, ofertas: tuple):

    matrizValorSolucion = np.zeros((A+1, n+1))
    matrizAuxiliar = np.zeros((A+1, n+1))
    B = B
    i = 0
    j = 0
    acciones = 0
    oferente = 0
    A = A+1
    valor = []
    cantidad = []
    solucion = []

    p, c, r = ofertas[n]

    for i in range(A):
        # se llena la primera fila con la oferta del gobierno
        matrizValorSolucion[i][0] = i*p
        matrizAuxiliar[i][0] = i

    for oferente in range(1, n+1):
        p, c, r = ofertas[n-oferente]
        for acciones in range(A):
            if acciones < r:
                matrizAuxiliar[acciones][oferente] = 0
                # no le vende nada al actual y por ello va al oferente anterior
                valor.append(matrizValorSolucion[acciones][oferente-1])
                cantidad.append(0)
            elif r <= acciones and acciones <= c:
                # no le vende nada al actual y por ello va al oferente anterior
                valor.append(matrizValorSolucion[acciones][oferente-1])
                cantidad.append(0)
                for k in range(r, acciones+1):
                    # se miran los casos desde el minimo hasta la cantidad de acciones que se estan vendiendo (k)
                    valor.append(
                        matrizValorSolucion[acciones-k][oferente-1] + k*p)
                    cantidad.append(k)
            else:
                valor.append(matrizValorSolucion[acciones][oferente-1])
                cantidad.append(0)
                for k in range(r, c+1):
                    # se miran los casos desde el minimo hasta la cantidad de acciones que se estan vendiendo (k)
                    valor.append(
                        matrizValorSolucion[k][oferente] + matrizValorSolucion[acciones-k][oferente-1])
                    cantidad.append(k)

            matrizValorSolucion[acciones][oferente] = max(valor)
            matrizAuxiliar[acciones][oferente] = cantidad[valor.index(
                max(valor))]

            valor = []
            cantidad = []
    acciones = A
    for oferentes in range(n+1):
        if acciones < 0:
            break
        solucion.append(int(matrizAuxiliar[acciones-1][n-oferentes]))
        acciones = acciones-solucion[oferentes]

    return solucion, int(matrizValorSolucion[A-1][n])


def accionesPD1(A: int, B: int, n: int, ofertas: tuple):
    eg.msgbox(msg='Se iniciará el algoritmo de Programación Dinámica, puede presionar el botón "Continuar", un mensaje aparecerá cuando el algoritmo haya finalizado',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    inicio3 = time.time()
    with open("outputDinamica1.txt", 'w') as write_file:
        solucion, valorSolucion = programacionDinamica(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))
    fin3 = time.time()
    eg.msgbox(msg='Tiempo de ejecución de programación dinámica: ' + str(fin3 - inicio3) + ' segundos\n\nValor de la solución: ' + str(valorSolucion) + '\n\nSe ha finalizado el algoritmo de Programación Dinámica, se abrirá el archivo outputDinamica1.txt con la solución encontrada',
              title='Programación de venta de acciones',
              ok_button='Continuar',
              image="images/dynamic_programming.jpg",)
    os.startfile("outputDinamica1.txt", operation='open')
