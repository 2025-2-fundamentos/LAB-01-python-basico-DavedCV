"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open("files/input/data.csv", "r") as f:
        data = f.readlines()
    min_vals = {}
    max_vals = {}
    for line in data:
        cols = line.strip().split("\t")
        dict_str = cols[4]
        pairs = dict_str.split(",")
        for pair in pairs:
            key, value = pair.split(":")
            value = int(value)
            if key not in min_vals:
                min_vals[key] = value
                max_vals[key] = value
            else:
                min_vals[key] = min(min_vals[key], value)
                max_vals[key] = max(max_vals[key], value)
    result = []
    for key in sorted(min_vals.keys()):
        result.append((key, min_vals[key], max_vals[key]))
    return result
