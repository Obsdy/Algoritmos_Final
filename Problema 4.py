def test_point_in_polygon(x_set, y_set, x, y, n):
    precision = 0.1
    resultados_previos = []
    if x_set[n] - x == 0:
        m_n = ["x", x]
    else:
        m_n = ["y", (y_set[n] - y) / (x_set[n] - x)]
    # Para "n" usaremos las coordenadas del punto dado,
    # Para las demas ecuaciones sera un elemento de X, Y
    m = []  # Todas las pendientes
    for j in range(len(x_set)):
        if j == len(x_set) - 1:
            if x_set[j] - x_set[0] == 0:
                m.append(["x", x_set[j]])
            else:
                m_i = (y_set[0] - y_set[j]) / (x_set[0] - x_set[j])
                m.append(["y", m_i])
        else:
            if x_set[j] - x_set[j + 1] == 0:
                m.append(["x", x_set[j]])
            else:
                m_i = (y_set[j + 1] - y_set[j]) / (x_set[j + 1] - x_set[j])
                m.append(["y", m_i])
    for j in range(len(m)):
        if m_n[0] == "y" and m[j][0] == "y":  # Por si ambas tienen ecuaciones en "y"
            if m[j][1] - m_n[1] != 0:
                x_resultado = (m[j][1] * x_set[j] - m_n[1] * x + y - y_set[j]) / (m[j][1] - m_n[1])
                # Basta con evaluar la x
                # Debe encontrarse entre las coordenadas en x del segmento correspondiente
                # La "y" se da por hecho y no es necesario evaluarla.
                if j == len(m) - 1:
                    if x_set[0] - x_resultado >= 0 and x_resultado - x_set[j] >= 0:  # Esta en el segmento
                        if (x - x_set[n] >= 0 and x - x_resultado >= 0) or (x - x_set[n] <= 0 and x - x_resultado <= 0):
                            # No esta en la direccion opuesta al rayo
                            if x_resultado not in resultados_previos:
                                resultados_previos.append(x_resultado)
                    elif x_set[0] - x_resultado <= 0 and x_resultado - x_set[j] <= 0:
                        if (x - x_set[n] >= 0 and x - x_resultado >= 0) or (x - x_set[n] <= 0 and x - x_resultado <= 0):
                            if x_resultado not in resultados_previos:
                                resultados_previos.append(x_resultado)
                else:
                    if x_set[j + 1] - x_resultado >= 0 and x_resultado - x_set[j] >= 0:
                        if (x - x_set[n] >= 0 and x - x_resultado >= 0) or (x - x_set[n] <= 0 and x - x_resultado <= 0):
                            if x_resultado not in resultados_previos:
                                resultados_previos.append(x_resultado)
                    elif x_set[j + 1] - x_resultado <= 0 and x_resultado - x_set[j] <= 0:
                        if (x - x_set[n] >= 0 and x - x_resultado >= 0) or (x - x_set[n] <= 0 and x - x_resultado <= 0):
                            if x_resultado not in resultados_previos:
                                resultados_previos.append(x_resultado)
        elif m_n[0] == "x" and m[j][0] == "y":
            y_resultado = m[j][1] * m_n[1] - m[j][1] * x_set[j] + y_set[j]
            # De la misma manera vemos que este entre las "y" del segmento
            if j == len(m) - 1:
                if y_set[0] - y_resultado >= 0 and y_resultado - y_set[j] >= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
                elif y_set[0] - y_resultado <= 0 and y_resultado - y_set[j] <= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
            else:
                if y_set[j + 1] - y_resultado >= 0 and y_resultado - y_set[j] >= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
                elif y_set[j + 1] - y_resultado <= 0 and y_resultado - y_set[j] <= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
        elif m_n[0] == "y" and m[j][0] == "x":
            y_resultado = m_n[1] * m[j][1] - m_n[1] * x + y
            # De la misma manera vemos que este entre las "y" del segmento
            if j == len(m) - 1:
                if y_set[0] - y_resultado >= 0 and y_resultado - y_set[j] >= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
                elif y_set[0] - y_resultado <= 0 and y_resultado - y_set[j] <= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
            else:
                if y_set[j + 1] - y_resultado >= 0 and y_resultado - y_set[j] >= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
                elif y_set[j + 1] - y_resultado <= 0 and y_resultado - y_set[j] <= 0:
                    if (y - y_set[n] >= 0 and y - y_resultado >= 0) or (y - y_set[n] <= 0 and y - y_resultado <= 0):
                        if y_resultado not in resultados_previos:
                            resultados_previos.append(y_resultado)
        resultados_previos = sorted(resultados_previos)
        if len(resultados_previos) > 1:
            for dato in range(len(resultados_previos) - 1):
                if resultados_previos[dato] + precision > resultados_previos[dato + 1]:
                    resultados_previos.pop(dato)
                    break
    if len(resultados_previos) % 2 == 1:
        return True
    else:
        return False


def redundancia(x_set, y_set, x, y, r):
    if r < len(x_set):
        division = len(x_set) % r
    else:
        division = 1
    resultados = []
    for i in range(r):
        resultados.append(test_point_in_polygon(x_set, y_set, x, y, division * i))

    if False in resultados:
        return False
    else:
        return True


X_e = [-2, 2, 4, -5, -4]
Y_e = [3, 3, -2, -4, 1]
x_e = -3
y_e = -2

print(redundancia(X_e, Y_e, x_e, y_e, 3))
