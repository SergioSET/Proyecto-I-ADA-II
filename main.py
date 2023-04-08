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

def estrategiaVoraz(A: int, B: int, n: int, ofertas: tuple[oferta]):

    def valor(asignaciones: tuple[tuple], ofertas: tuple[oferta]):
        for i, oferta in enumerate(ofertas):
            val = 0
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

# Confirmación de datos
print(A)
print(B)
print(n)
print(ofertas)
print("\n")

def accionesVoraz():
    with open("output.txt", 'w') as write_file:
        solucion, valorSolucion = estrategiaVoraz(A, B, n, ofertas)
        write_file.write("{0}\n".format(valorSolucion))
        for asig in solucion:
            write_file.write("{0}\n".format(asig))

accionesVoraz()