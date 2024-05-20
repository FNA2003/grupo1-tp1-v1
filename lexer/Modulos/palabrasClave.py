# AFD para la palabra clave "const"
def afd_const(cadena:str) -> int:
    """ r = const """

    estado_actual:int = 0
    estados_finales:list[int] = [5]


    for caracter in cadena:
        # Q0 a Q1 con c
        if estado_actual == 0 and caracter == "c":
            estado_actual = 1
        # Q1 a Q2 con o
        elif estado_actual == 1 and caracter == "o":
            estado_actual = 2
        # Q2 a Q3 con n
        elif estado_actual == 2 and caracter == "n":
            estado_actual = 3
        # Q3 a Q4 con s
        elif estado_actual == 3 and caracter == "s":
            estado_actual = 4
        # Q4 a Q5 con t
        elif estado_actual == 4 and caracter == "t":
            estado_actual = 5
        # Todas las otras transiciones al trampa
        else:
            estado_actual = 6
            break

    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD para la palabra clave "var" 
def afd_var(cadena:str) -> int:
    """ r = var """

    estado_actual:int = 0
    estados_finales:list[int] = [3]


    for caracter in cadena:
        # Q0 a Q1 con v
        if estado_actual == 0 and caracter == "v":
            estado_actual = 1
        # Q1 a Q2 con a
        elif estado_actual == 1 and caracter == "a":
            estado_actual = 2
        # Q2 a Q3 con r
        elif estado_actual == 2 and caracter == "r":
            estado_actual = 3
        # Todas las otras transiciones al trampa
        else:
            estado_actual = 4
            break 

    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)
    



# AFD para la keyword "call"
def afd_call(cadena:str) -> int:
    """ r = call """

    estado_actual:int = 0
    estados_finales:list[int] = [4]


    for caracter in cadena:
        # Q0 a Q1 con c
        if estado_actual == 0 and caracter == "c":
            estado_actual = 1
        # Q1 a Q2 con a
        elif estado_actual == 1 and caracter == "a":
            estado_actual = 2
        # Q2 a Q3 con l
        elif estado_actual == 2 and caracter == "l":
            estado_actual = 3
        # Q3 a Q4 con l
        elif estado_actual == 3 and caracter == "l":
            estado_actual = 4
        # Estado trampa para todas las otras transiciones
        else:
            estado_actual = 5
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD de la palabra clave "begin"
def afd_begin(cadena:str)->int:
    """ r = begin """

    estado_actual:int = 0
    estados_finales:list[int] = [5]


    for caracter in cadena:
        # Q0 a Q1 con b
        if estado_actual == 0 and caracter == "b":
            estado_actual = 1
        # Q1 a Q2 con e
        elif estado_actual == 1 and caracter == "e":
            estado_actual = 2
        # Q2 a Q3 con g
        elif estado_actual == 2 and caracter == "g":
            estado_actual = 3
        # Q3 a Q4 con i
        elif estado_actual == 3 and caracter == "i":
            estado_actual = 4
        # Q4 con Q5 con n
        elif estado_actual == 4 and caracter == "n":
            estado_actual = 5
        # El resto, al trampa
        else:
            estado_actual = 6
            break

    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD de la keyword "end"
def afd_end(cadena:str)->int:
    estado_actual:int = 0
    estados_finales:list[int] = [3]


    for caracter in cadena:
        # Q0 a Q1 con e
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        # Q1 a Q2 con n
        elif estado_actual == 1 and caracter == "n":
            estado_actual = 2
        # Q2 a Q3 con d
        elif estado_actual == 2 and caracter == "d":
            estado_actual = 3
        # El resto, al trampa
        else:
            estado_actual = 4
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)
   


# AFD de la keyword "if"
def afd_if(cadena:str)->int:
    """ r = if """

    estado_actual:int = 0
    estados_finales:list[int] = [2]


    for caracter in cadena:
        # Q0 a Q1 con i
        if estado_actual == 0 and caracter =="i":
            estado_actual = 1
        # Q1 a Q2 con f
        elif estado_actual == 1 and caracter == "f":
            estado_actual = 2
        # Trampa sino
        else:
            estado_actual = 3
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD de la keyword "then"
def afd_then(cadena:str)->int:
    """ r = then """
    
    estado_actual:int = 0
    estados_finales:list[int] = [4]


    for caracter in cadena:
        # Q0 a Q1 con t
        if estado_actual == 0 and caracter == "t":
            estado_actual = 1
        # Q1 a Q2 con h
        elif estado_actual == 1 and caracter == "h":
            estado_actual = 2
        # Q2 a Q3 con e
        elif estado_actual == 2 and caracter == "e":
            estado_actual = 3
        # Q3 a Q4 con n
        elif estado_actual == 3 and caracter == "n":
            estado_actual = 4
        # Trampa sino
        else:
            estado_actual = 5
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD de la keyword while
def afd_while(cadena:str)->int:
    """ r = while """

    estado_actual:int = 0
    estados_finales:list[int] = [5]


    for caracter in cadena:
        # Q0 a Q1 con w
        if estado_actual == 0 and caracter == "w":
            estado_actual = 1
        # Q1 a Q2 con h
        elif estado_actual == 1 and caracter == "h":
            estado_actual = 2
        # Q2 a Q3 con i
        elif estado_actual == 2 and caracter == "i":
            estado_actual = 3
        # Q3 a Q4 con l
        elif estado_actual == 3 and caracter == "l":
            estado_actual = 4
        # Q4 a Q5 con e
        elif estado_actual == 4 and caracter == "e":
            estado_actual = 5
        # Trampa sino
        else:
            estado_actual = 6
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD del keyword "do"
def afd_do(cadena:str)->int:
    """ r = do """

    estado_actual:int = 0
    estados_finales:list[int] = [2]


    for caracter in cadena:
        # Q0 a Q1 con d
        if estado_actual == 0 and caracter == "d":
            estado_actual = 1
        # Q1 a Q2 con o
        elif estado_actual == 1 and caracter == "o":
            estado_actual = 2
        # Trampa sino
        else:
            estado_actual = 3
            break
    
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD de la palabra clave "odd"
def afd_odd(cadena:str)->int:
    """ r = odd """

    estado_actual:int = 0
    estados_finales:list[int] = [3]


    for caracter in cadena:
        # Q0 a Q1 con o
        if estado_actual == 0 and caracter == "o":
            estado_actual = 1
        # Q1 a Q2 con d
        elif estado_actual == 1 and caracter == "d":
            estado_actual = 2
        # Q2 a Q3 con d
        elif estado_actual == 2 and caracter == "d":
            estado_actual = 3
        # Trampa sino
        else:
            estado_actual = 4
            break
        
    # Devolvemos si la cadena fue aceptada por el AFD
    return (1 if estado_actual in estados_finales else 0)



# AFD para la palabra clave procedure
def afd_procedure(cadena:str)->int:
    estado_actual:int = 0
    estados_finales:list[int] = [9]

    for caracter in cadena:
        if caracter == "p" and estado_actual == 0:
            estado_actual = 1
        elif caracter == "r" and estado_actual == 1:
            estado_actual = 2
        elif caracter == "o" and estado_actual == 2:
            estado_actual = 3
        elif caracter == "c" and estado_actual == 3:
            estado_actual = 4
        elif caracter == "e" and estado_actual == 4:
            estado_actual = 5
        elif caracter == "d" and estado_actual == 5:
            estado_actual = 6
        elif caracter == "u" and estado_actual == 6:
            estado_actual = 7
        elif caracter == "r" and estado_actual == 7:
            estado_actual = 8
        elif caracter == "e" and estado_actual == 8:
            estado_actual = 9
        else:
            estado_actual = 10
            break
    
    return (1 if estado_actual in estados_finales else 0)