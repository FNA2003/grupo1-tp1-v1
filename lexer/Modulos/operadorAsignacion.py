def afd_assignment(cadena:str)->int:
    """ r = := """

    estado_actual:int = 0
    estados_finales:list[int] = [3]

    for caracater in cadena:
        if caracater == ":" and estado_actual == 0:
            estado_actual = 1
        elif caracater == "=" and estado_actual == 1:
            estado_actual = 3
        else:
            estado_actual = 2
    
    return (1 if estado_actual in estados_finales else 0)