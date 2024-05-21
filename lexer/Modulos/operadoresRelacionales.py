# AFD para los operadores relaciones
def afd_relation(cadena:str) -> int:
    """ r = > | < | = | >= | <= | <> """

    estado_actual:int = 0
    estados_aceptados:list[int] = [1,2,3]


    for caracter in cadena:
        if caracter == ">" and estado_actual == 0:
            estado_actual = 1
        elif caracter == "<" and estado_actual == 0:
            estado_actual = 2
        elif caracter == "=" and estado_actual == 0:
            estado_actual = 3
        elif caracter == "=" and estado_actual == 1:
            estado_actual = 3
        elif (caracter == "=" or caracter == ">") and estado_actual == 2:
            estado_actual = 3
        else:
            estado_actual = 4
            break
    
    # Devolvemos si la cadena fue aceptada
    return (1 if estado_actual in estados_aceptados else 0)