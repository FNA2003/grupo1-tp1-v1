from .DATOS import *


# AFD para los tokens numericos (enteros)
def afd_num(cadena:str) -> int:
    """ r = (0|...|9).(0|...|9)* """

    estado_actual:int = 0
    estados_finales:list[int] = [1]


    # Desglozamos la cadena
    for caracter in cadena:
        # De q0 a q1 con cualquier numero
        if estado_actual == 0 and caracter in NUMEROS:
            estado_actual = 1
        # De q1 nos quedamos en q1 con cualquier numero
        elif estado_actual == 1 and caracter in NUMEROS:
            estado_actual = 1
        # Cualquier transicion no mencionada queda en q2, estado trampa
        else:
            estado_actual = 2
            break
    

    # Devolvemos 1 si la cadena es generada por el AFD, 0 sino
    return (1 if estado_actual in estados_finales else 0)