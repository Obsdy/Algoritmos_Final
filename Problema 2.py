def puntos_silla(M):
    datos = []
    for columna in range(len(M)):
        for fila in range(len(M)):
            if fila == 0:
                actual = M[fila][columna]
                siguiente = M[fila + 1][columna]
                if siguiente <= actual:
                    if columna == 0:
                        derecha = M[fila][columna + 1]
                        if actual <= derecha:
                            datos.append([fila, columna])
                    elif columna == len(M) - 1:
                        izquierda = M[fila][columna - 1]
                        if actual <= izquierda:
                            datos.append([fila, columna])
                    else:
                        derecha = M[fila][columna + 1]
                        izquierda = M[fila][columna - 1]
                        if izquierda >= actual <= derecha:
                            datos.append([fila, columna])
            elif fila == len(M) - 1:
                anterior = M[fila - 1][columna]
                actual = M[fila][columna]
                if actual >= anterior:
                    if columna == 0:
                        derecha = M[fila][columna + 1]
                        if actual <= derecha:
                            datos.append([fila, columna])
                    elif columna == len(M) - 1:
                        izquierda = M[fila][columna - 1]
                        if actual <= izquierda:
                            datos.append([fila, columna])
                    else:
                        derecha = M[fila][columna + 1]
                        izquierda = M[fila][columna - 1]
                        if izquierda >= actual <= derecha:
                            datos.append([fila, columna])
            else:
                anterior = M[fila - 1][columna]
                actual = M[fila][columna]
                siguiente = M[fila + 1][columna]
                if siguiente <= actual >= anterior:
                    if columna == 0:
                        derecha = M[fila][columna + 1]
                        if actual <= derecha:
                            datos.append([fila, columna])
                    elif columna == len(M) - 1:
                        izquierda = M[fila][columna - 1]
                        if actual <= izquierda:
                            datos.append([fila, columna])
                    else:
                        derecha = M[fila][columna + 1]
                        izquierda = M[fila][columna - 1]
                        if izquierda >= actual <= derecha:
                            datos.append([fila, columna])
    for dato in datos:
        dato[0] += 1
        dato[1] += 1
    return datos


M = [[1,-10,3,2,5], [-1,1,4,3,7], [0,2,3,6,3], [1,8,4,6,2], [0,4,-1,5,1]]
print(puntos_silla(M))
