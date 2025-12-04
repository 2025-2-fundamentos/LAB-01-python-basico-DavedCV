"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()
    result = []
    for line in data:
        cols = line.strip().split("\t")
        letter = cols[0]
        col4 = cols[3]
        col5 = cols[4]
        count_col4 = len(col4.split(","))
        count_col5 = len(col5.split(","))
        result.append((letter, count_col4, count_col5))
    return result
