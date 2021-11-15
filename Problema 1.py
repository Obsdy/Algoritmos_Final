from math import sqrt


def dis_eu(x_1, y_1, x_2, y_2):
    return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)


def quicksort(lista):
    if len(lista) in [0, 1]:
        return lista

    pivote = lista[0]
    menores = []
    mayores = []
    iguales = []
    for indice in range(1, len(lista)):
        if lista[indice] < pivote:
            menores.append(lista[indice])
        elif lista[indice] > pivote:
            mayores.append(lista[indice])
        else:
            iguales.append(lista[indice])

    menores = quicksort(menores)
    mayores = quicksort(mayores)
    iguales.append(lista[0])

    resultado = menores + iguales + mayores
    return resultado


def sup_a(a, b):
    resultados_a = []
    for punto in a:
        resultados_b = []
        for otro_punto in b:
            x_1 = punto[0]
            y_1 = punto[1]
            x_2 = otro_punto[0]
            y_2 = otro_punto[1]
            resultados_b.append(dis_eu(x_1, y_1, x_2, y_2))
        resultados_b_ord = quicksort(resultados_b)
        resultados_a.append(resultados_b_ord[0])
    resultados_a_ord = quicksort(resultados_a)
    return resultados_a_ord[-1]


def d_h(p, q):
    primero = sup_a(p, q)
    segundo = sup_a(q, p)
    if primero > segundo:
        return primero
    else:
        return segundo


X = [[1,1], [0,0], [-1, 1], [-1, 2]]
Y = [[1,-1], [0,0], [-1, -2], [3, -2]]
print(d_h(X, Y))
