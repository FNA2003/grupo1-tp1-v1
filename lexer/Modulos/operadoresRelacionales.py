# AFD para los operadores relaciones
def afd_relation(cadena:str) -> int:
    """ r = > | < | = | >= | <= | <> """

    estado_actual:int = 0
    estados_aceptados:list[int] = [1]


    if cadena in ["<", ">", ">=", "<=", "<>", "="]:
        estado_actual = 1
    else:
        estado_actual = 2
    
    # Devolvemos si la cadena fue aceptada
    return (1 if estado_actual in estados_aceptados else 0)