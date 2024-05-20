from .DATOS import *


# Automata de "id" para PL0
def afd_id(cadena:str) -> int:
    """ r =  (a|...|z|A|...|Z).(a|...|z|A|...|Z|0|...|9)* """

    estado_actual:int = 0
    estados_finales:list[int] = [1]
    

    # Lee cada caracter de la cadena
    for caracter in cadena:
        # Si estamos en el estado inicial y el caracter inicial es una letra, pasamos al estado aceptado
        if estado_actual == 0 and caracter in LETRAS:
            estado_actual = 1
        # Si el estado actual no es el inicial y, se  utiliza cualquier combinacion de letras/numeros, permanecemos en el estado aceptado
        elif estado_actual == 1 and caracter in (LETRAS+NUMEROS):
            estado_actual = 1
        # Y, si no se cumple nada de lo anterior, pasamos al estado trampa
        else:
            estado_actual = 2
            break
        
    # Revisamos si llegamos a un estado aceptado para validar la cadena
    return (1 if estado_actual in estados_finales else 0)