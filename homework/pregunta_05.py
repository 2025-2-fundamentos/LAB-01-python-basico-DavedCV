"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()
    max_vals = {}
    min_vals = {}
    for line in data:
        cols = line.strip().split("\t")
        letter = cols[0]
        value = int(cols[1])
        if letter not in max_vals:
            max_vals[letter] = value
            min_vals[letter] = value
        else:
            max_vals[letter] = max(max_vals[letter], value)
            min_vals[letter] = min(min_vals[letter], value)
    result = []
    for letter in sorted(max_vals.keys()):
        result.append((letter, max_vals[letter], min_vals[letter]))
    return result
