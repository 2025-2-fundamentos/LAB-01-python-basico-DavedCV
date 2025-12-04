"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()
    sums = {}
    for line in data:
        cols = line.strip().split("\t")
        col2_value = int(cols[1])
        col4 = cols[3]
        letters = col4.split(",")
        for letter in letters:
            sums[letter] = sums.get(letter, 0) + col2_value
    return dict(sorted(sums.items()))
