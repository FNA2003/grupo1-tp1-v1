def afd_parenIzq(cadena:str)->int:
    """ r = ( """

    estado_actual:int = 0
    estados_finales:list[int] = [1]


    if cadena == "(":
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_finales else 0)
        


def afd_parenDer(cadena:str):
    """ r = ) """

    estado_actual:int = 0
    estados_finales:list[int] = [1]


    if cadena == ")":
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_finales else 0)



def afd_coma(cadena):
    """ r = , """

    estado_actual:int = 0
    estados_finales:list[int] = [1]


    if cadena == ",":
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_finales else 0)



def afd_puntoComa(cadena):
    """ r = ; """

    estado_actual:int = 0
    estados_finales:list[int] = [1]


    if cadena == ";":
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_finales else 0)