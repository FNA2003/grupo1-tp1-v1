# ===============================================================================================
# Automata de id 
#================================================================================================
def afd_id(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9']
    delta = {
    0: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
        'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
        'A': 't', 'B': 't', 'C': 't', 'D': 't', 'E': 't', 'F': 't', 'G': 't', 'H': 't', 'I': 't', 'J': 't', 'K': 't',
        'L': 't', 'M': 't', 'N': 't', 'O': 't', 'P': 't', 'Q': 't', 'R': 't', 'S': 't', 'T': 't', 'U': 't', 'V': 't',
        'W': 't', 'X': 't', 'Y': 't', 'Z': 't', '0': 't', '1': 't', '2': 't', '3': 't', '4': 't', '5': 't', '6': 't',
        '7': 't', '8': 't', '9': 't'},
    1: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
        'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
        'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1,
        'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1,
        '0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    't': {'a': 't', 'b': 't', 'c': 't', 'd': 't', 'e': 't', 'f': 't', 'g': 't', 'h': 't', 'i': 't', 'j': 't', 'k': 't',
        'l': 't', 'm': 't', 'n': 't', 'o': 't', 'p': 't', 'q': 't', 'r': 't', 's': 't', 't': 't', 'u': 't', 'v': 't',
        'w': 't', 'x': 't', 'y': 't', 'z': 't', 'A': 't', 'B': 't', 'C': 't', 'D': 't', 'E': 't', 'F': 't', 'G': 't',
        'H': 't', 'I': 't', 'J': 't', 'K': 't', 'L': 't', 'M': 't', 'N': 't', 'O': 't', 'P': 't', 'Q': 't', 'R': 't',
        'S': 't', 'T': 't', 'U': 't', 'V': 't', 'W': 't', 'X': 't', 'Y': 't', 'Z': 't', '0': 't', '1': 't', '2': 't',
        '3': 't', '4': 't', '5': 't', '6': 't', '7': 't', '8': 't', '9': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'
    
    return estado_final


#================================================================================================
# Automata de numeros
#================================================================================================
def afd_numbers(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    delta = {
    0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    't': {'0': 't', '1': 't', '2': 't', '3': 't', '4': 't', '5': 't', '6': 't', '7': 't', '8': 't', '9': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'
    
    return estado_final


#================================================================================================
# Automata de fin del programa
#================================================================================================
def afd_end_program(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = ['#']
    delta = {
    0: {'#': 1},
    1: {'#': 't'},
    't': {'#': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de const
#================================================================================================
def afd_const(cadena):
    """El estado aceptado es 5"""
    estado = 0
    caracteres = ['c', 'o', 'n', 's', 't']
    delta = {
    0: {'c': 1, 'o': 't', 'n': 't', 's': 't', 't': 't'},
    1: {'c': 't', 'o': 2, 'n': 't', 's': 't', 't': 't'},
    2: {'c': 't', 'o': 't', 'n': 3, 's': 't', 't': 't'},
    3: {'c': 't', 'o': 't', 'n': 't', 's': 4, 't': 't'},
    4: {'c': 't', 'o': 't', 'n': 't', 's': 't', 't': 5},
    5: {'c': 't', 'o': 't', 'n': 't', 's': 't', 't': 't'},
    't': {'c': 't', 'o': 't', 'n': 't', 's': 't', 't': 't'}
    }

    for caracter in cadena:
        if (estado <= 5) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif estado == 't' or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 5:
        estado_final = 'aceptado'
    elif estado < 5:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de var
#================================================================================================
def afd_var(cadena):
    """El estado aceptado es 3"""
    estado = 0
    caracteres = ['v', 'a', 'r']
    delta = {
    0: {'v': 1, 'a': 't', 'r': 't'},
    1: {'v': 't', 'a': 2, 'r': 't'},
    2: {'v': 't', 'a': 't', 'r': 3},
    3: {'v': 't', 'a': 't', 'r': 't'},
    't': {'v': 't', 'a': 't', 'r': 't'}
    }

    for caracter in cadena:
        if (estado <= 3) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif estado == 't' or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 3:
        estado_final = 'aceptado'
    elif estado < 3:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de la coma
#================================================================================================
def afd_coma(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = [',']
    delta = {
    0: {',': 1},
    1: {',': 't'},
    't': {',': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata del punto y coma
#================================================================================================
def afd_punto_y_coma(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = [';']
    delta = {
    0: {';': 1},
    1: {';': 't'},
    't': {';': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 1) or (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de asignacion
#================================================================================================
def afd_asignation(cadena):
    """El estado aceptado es 2"""
    estado = 0
    caracteres = [':', '=']
    delta = {
    0: {':': 1, '=': 't'},
    1: {':': 't', '=': 2},
    2: {':': 't', '=': 't'},
    't': {';': 't'}
    }

    for caracter in cadena:
        if (estado <= 2) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 2:
        estado_final = 'aceptado'
    elif estado < 2:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de llamada a funciones
#================================================================================================
def afd_call(cadena):
    """El estado aceptado es 4"""
    estado = 0
    caracteres = ['c', 'a', 'l', 'l']
    delta = {
    0: {'c': 1, 'a': 't', 'l': 't', 'l': 't'},
    1: {'c': 't', 'a': 2, 'l': 't', 'l': 't'},
    2: {'c': 't', 'a': 't', 'l': 3, 'l': 't'},
    3: {'c': 't', 'a': 't', 'l': 't', 'l': 4},
    4: {'c': 't', 'a': 't', 'l': 't', 'l': 't'},
    't': {'c': 't', 'a': 't', 'l': 't', 'l': 't'}
    }

    for caracter in cadena:
        if (estado <= 4) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 4:
        estado_final = 'aceptado'
    elif estado < 4:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de inicio de bloque de codigo
#================================================================================================
def afd_begin(cadena):
    """El estado aceptado es 5"""
    estado = 0
    caracteres = ['b', 'e', 'g', 'i', 'n']
    delta = {
    0: {'b': 1, 'e': 't', 'g': 't', 'i': 't', 'n': 't'},
    1: {'b': 't', 'e': 2, 'g': 't', 'i': 't', 'n': 't'},
    2: {'b': 't', 'e': 't', 'g': 3, 'i': 't', 'n': 't'},
    3: {'b': 't', 'e': 't', 'g': 't', 'i': 4, 'n': 't'},
    4: {'b': 't', 'e': 't', 'g': 't', 'i': 't', 'n': 5},
    5: {'b': 't', 'e': 't', 'g': 't', 'i': 't', 'n': 't'},
    't': {'b': 't', 'e': 't', 'g': 't', 'i': 't', 'n': 't'}
    }

    for caracter in cadena:
        if (estado <= 5) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 5:
        estado_final = 'aceptado'
    elif estado < 5:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de fin de bloque de codigo
#================================================================================================
def afd_end(cadena):
    """El estado aceptado es 3"""
    estado = 0
    caracteres = ['e', 'n', 'd']
    delta = {
    0: {'e': 1, 'n': 't', 'd': 't'},
    1: {'e': 't', 'n': 2, 'd': 't'},
    2: {'e': 't', 'n': 't', 'd': 3},
    3: {'e': 't', 'n': 't', 'd': 't'},
    't': {'e': 't', 'n': 't', 'd': 't'}
    }

    for caracter in cadena:
        if (estado <= 3) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 3:
        estado_final = 'aceptado'
    elif estado < 3:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de inicio de condicion
#================================================================================================
def afd_if(cadena):
    """El estado aceptado es 2"""
    estado = 0
    caracteres = ['i', 'f']
    delta = {
    0: {'i': 1, 'f': 't'},
    1: {'i': 't', 'f': 2},
    2: {'i': 't', 'f': 't'},
    't': {'i': 't', 'f': 't'}
    }

    for caracter in cadena:
        if (estado <= 2) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 2:
        estado_final = 'aceptado'
    elif estado < 2:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de fin de condicion
#================================================================================================
def afd_then(cadena):
    """El estado aceptado es 4"""
    estado = 0
    caracteres = ['t', 'h', 'e', 'n']
    delta = {
    0: {'t': 1, 'h': 't', 'e': 't', 'n': 't'},
    1: {'t': 't', 'h': 2, 'e': 't', 'n': 't'},
    2: {'t': 't', 'h': 't', 'e': 3, 'n': 't'},
    3: {'t': 't', 'h': 't', 'e': 't', 'n': 4},
    4: {'t': 't', 'h': 't', 'e': 't', 'n': 't'},
    't': {'t': 't', 'h': 't', 'e': 't', 'n': 't'}
    }

    for caracter in cadena:
        if (estado <= 4) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 4:
        estado_final = 'aceptado'
    elif estado < 4:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de inicio de condicion de ciclo
#================================================================================================
def afd_while(cadena):
    """El estado aceptado es 5"""
    estado = 0
    caracteres = ['w', 'h', 'i', 'l', 'e']
    delta = {
    0: {'w': 1, 'h': 't', 'i': 't', 'l': 't', 'e': 't'},
    1: {'w': 't', 'h': 2, 'i': 't', 'l': 't', 'e': 't'},
    2: {'w': 't', 'h': 't', 'i': 3, 'l': 't', 'e': 't'},
    3: {'w': 't', 'h': 't', 'i': 't', 'l': 4, 'e': 't'},
    4: {'w': 't', 'h': 't', 'i': 't', 'l': 't', 'e': 5},
    5: {'w': 't', 'h': 't', 'i': 't', 'l': 't', 'e': 't'},
    't': {'w': 't', 'h': 't', 'i': 't', 'l': 't', 'e': 't'}
    }

    for caracter in cadena:
        if (estado <= 5) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 5:
        estado_final = 'aceptado'
    elif estado < 5:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de inicio de codigo a ejecutar en el ciclo
#================================================================================================
def afd_do(cadena):
    """El estado aceptado es 2"""
    estado = 0
    caracteres = ['d', 'o']
    delta = {
    0: {'d': 1, 'o': 't'},
    1: {'d': 't', 'o': 2},
    2: {'d': 't', 'o': 't'},
    't': {'d': 't', 'o': 't'}
    }

    for caracter in cadena:
        if (estado <= 2) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 2:
        estado_final = 'aceptado'
    elif estado < 2:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de negacion de una condicion
#================================================================================================
def afd_odd(cadena):
    """El estado aceptado es 3"""
    estado = 0
    caracteres = ['o', 'd', 'd']
    delta = {
    0: {'o': 1, 'd': 't', 'd': 't'},
    1: {'o': 't', 'd': 2, 'd': 't'},
    2: {'o': 't', 'd': 't', 'd': 3},
    3: {'o': 't', 'd': 't', 'd': 't'},
    't': {'o': 't', 'd': 't', 'd': 't'}
    }

    for caracter in cadena:
        if (estado <= 3) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 3:
        estado_final = 'aceptado'
    elif estado < 3:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de operadores de comparacion
#================================================================================================
def afd_comparation(cadena):
    """Los estados aceptado son 1, 2 y 3"""
    estados_aceptados = [1, 2, 3]
    estado = 0
    caracteres = ['<', '>', '=']
    delta = {
    0: {'<': 1, '>': 2, '=': 3},
    1: {'<': 't', '>': 3, '=': 3},
    2: {'<': 't', '>': 't', '=': 3},
    3: {'<': 't', '>': 't', '=': 't'},
    't': {'<': 't', '>': 't', '=': 't'}
    }

    for caracter in cadena:
        if (estado <= 3) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado in estados_aceptados:
        estado_final = 'aceptado'
    elif estado == 0:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de operadores matematicos
#================================================================================================
def afd_operation(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = ['+', '-', '*', '/']
    delta = {
    0: {'+': 1, '-': 1, '*': 1, '/': 1},
    1: {'+': 't', '-': 't', '*': 't', '/': 't'},
    't': {'+': 't', '-': 't', '*': 't', '/': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de parentesis inicial
#================================================================================================
def afd_parentesis_inicial(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = ['(']
    delta = {
    0: {'(': 1},
    1: {'(': 't'},
    't': {'(': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de parentesis final
#================================================================================================
def afd_parentesis_inicial(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = [')']
    delta = {
    0: {')': 1},
    1: {')': 't'},
    't': {')': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'

    return estado_final


#================================================================================================
# Automata de espacios en blanco
#================================================================================================
def afd_white_space(cadena):
    """El estado aceptado es 1"""
    estado = 0
    caracteres = [' ', '\n', '\t']
    delta = {
    0: {' ': 1, '\n': 1, '\t': 1},
    1: {' ': 1, '\n': 1, '\t': 1},
    't': {' ': 't', '\n': 't', '\t': 't'}
    }

    for caracter in cadena:
        if (estado <= 1) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado_final = 'trampa'
            break

    if estado == 1:
        estado_final = 'aceptado'
    elif estado < 1:
        estado_final = 'no aceptado'
    
    return estado_final

