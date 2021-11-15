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


def abs_dif(a):
    min_val = "TOP"
    orden = quicksort(a)

    for i in range(len(a)-1):
        resta = abs(orden[i] - orden[i + 1])
        if min_val == "TOP":
            min_val = resta
        elif resta < min_val:
            min_val = resta
    return min_val


arreglo = [1, -1, 3, 8, 5]
print(abs_dif(arreglo))
