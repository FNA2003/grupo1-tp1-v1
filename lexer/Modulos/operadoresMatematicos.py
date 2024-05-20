def afd_sumOperator(cadena:str) -> int:
    """ r = + | - """

    estado_actual:int = 0
    estados_aceptados:list[int] = [1]
    
    
    if cadena in ["-","+"]:
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_aceptados else 0)
    
    
def afd_multOperator(cadena:str) -> int:
    """ r = * | / """

    estado_actual:int = 0
    estados_aceptados:list[int] = [1]

    if cadena in ["*", "/"]:
        estado_actual = 1
    else:
        estado_actual = 2
    
    return (1 if estado_actual in estados_aceptados else 0)