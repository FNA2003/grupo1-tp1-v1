def afd_whiteSpace(cadena:str)->int:
    """  r = λ | \n | \t  """

    estado_actual:int = 0
    estados_aceptados:list[int] = [1]


    if cadena in ["\n", "\t", "", " "]:
        estado_actual = 1
    else:
        estado_actual = 2

    # Devolver si la cadena es aceptada por el afd
    return (1 if estado_actual in estados_aceptados else 0)