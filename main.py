oferta = tuple[int, int, int]
asignacion = tuple[int]
asignaciones = tuple[asignacion]
# Inicialización de variables leyendo el archivo input.txt
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


def fuerzaBruta(A: int, B: int, n: int, ofertas: tuple[oferta]):

    # une la asignacion recibida a cada asignacion de la tupla recibida
    def productoCartElemento(element: asignacion,
                             tupla: asignaciones) -> asignaciones:
        return tuple(element + element2 for element2 in tupla)

    # calcula el valor de la asignacion de acciones recibida como parametro
    def valorAsig(asignacion: tuple[int]):
        resultado = 0
        for i, cantAcciones in enumerate(asignacion):
            resultado += cantAcciones * ofertas[i][0]
        return resultado

    def licitacion(A: int, B: int, n: int,
                   ofertas: tuple[oferta]) -> asignaciones:
        p, max, min = ofertas[0]

        def noIncluirOfertaActual() -> asignaciones:
            return productoCartElemento((0, ),
                                        licitacion(A, B, n - 1, ofertas[1:]))

        def incluirOfertaActual(cantA=min) -> asignaciones:
            if cantA == max or cantA == A:
                return productoCartElemento((cantA, ),
                                            licitacion(A - cantA, B, n - 1,
                                                       ofertas[1:]))
            else:
                return productoCartElemento(
                    (cantA, ), licitacion(
                        A - cantA, B, n - 1,
                        ofertas[1:])) + incluirOfertaActual(cantA + 1)

        if n == 0:
            return ((A, ), )
        elif A >= min:
            return noIncluirOfertaActual() + incluirOfertaActual()
        else:
            return noIncluirOfertaActual()

    soluciones = licitacion(A, B, n, ofertas)
    valorSoluciones = map(valorAsig, soluciones)
    pos, maxValor = 0, A * B
    for index, valor in enumerate(valorSoluciones):
        if valor > maxValor:
            pos, maxValor = index, valor
    return soluciones[pos], valorAsig(soluciones[pos])
    # return licitacion(A, B, n, ofertas)


# Confirmación de datos
print(A)
print(B)
print(n)
print(ofertas)
print("\n")


def accionesFB():
    with open("output.txt", 'w') as write_file:
        solucion, valorSolucion = fuerzaBruta(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))


accionesFB()
# print(all(map(lambda x: sum(x)==1000, fuerzaBruta(A, B, n, ofertas))))
# with open("output.txt", 'w') as write_file:
#     for line in fuerzaBruta(A, B, n, ofertas):
#         if type(line) != type(tuple((1,))):
#             print(line, type(line),type(tuple) )
#             break
#         write_file.write("{0}\n".format(line))

# Ejecución del algoritmo de fuerza bruta
# fuerzaBruta(A, B, n, ofertas)