from AFDs import *

tipos_de_tokens_con_sus_automatas = [("if",afd_if), ("then",afd_then), ("call",afd_call), ("begin",afd_begin), 
    ("end",afd_end), ("while",afd_while), ("do",afd_do), ("odd",afd_odd), 
    ("const",afd_const), ("var",afd_var), ("comparation",afd_comparation), ("assign", afd_asignation),
    ("procedure", afd_procedure),("id",afd_id), ("operation",afd_operation),  
    ("#", afd_end_program), ("numbers",afd_numbers),  ("coma", afd_coma), (";",afd_punto_y_coma), 
    ("(",afd_parentesis_inicial), (")",afd_parentesis_final), ("blanckSpace", afd_white_space)]

def lexer(codigoFuente):

    contador = 1
    inicio_del_lexema = 0
    fin_del_lexema = 0
    lexema = ''

    nuevos_tipos_de_tokens_posibles = []
    antiguos_tipos_de_tokens_posibles = []

    lista_final_de_tokens_con_sus_tipos = []
    
    # Recorro el codigo fuente del prg, formando un lexema 1 caracter mas largo por cada iteracion hasta hallarle una clasificacion
    # Una vez hallada la clasificacion, paso a recorrer lo que resta del codigo fuente aplicando el mismo procedimiento
    while contador <= len(codigoFuente):
        fin_del_lexema = contador
        lexema = codigoFuente[inicio_del_lexema:fin_del_lexema]
        
        # A cada nuevo lexema extraido del codigo fuente (cadena del codigo fuente desde la posicion 'inicio_del_lexema' 
        # hasta la posicion anterior a 'fin_del_lexema') lo evaluo con todos los automatas de los tipos de tokens 
        # anteriormente definidos.
        for tipo_de_token, afd_del_token in tipos_de_tokens_con_sus_automatas:
            
            estado = afd_del_token(lexema)

            # Si el lexema corresponde a algun tipo de token, agrego ese tipo a la lista de 'nuevos_tipos_de_tokens_posibles'
            if estado == 'aceptado':
                nuevos_tipos_de_tokens_posibles.append(tipo_de_token)
            
            # Si el lexema no corresponde a un tipo de token, pero el estado de algun afd de los tipos de token al evaluar el lexema es
            # 'no aceptado', entonces podria agregar un caracter mas al lexema extraido del codigo fuente evaluado actualmente, y
            # verificar si el nuevo lexema resultante pertenece a algun tipo de token
            elif estado == 'no aceptado':
                analizar_lexema_mas_grande = True


        # Si el estado del afd del tipo de token al evaluar el lexema es 'no aceptado', entonces paso a analizar el lexema 
        # resultante de añadir un caracter al lexema extraido del codigo fuente evaluado actualmente
        if analizar_lexema_mas_grande == True:
            analizar_lexema_mas_grande = False
            antiguos_tipos_de_tokens_posibles = nuevos_tipos_de_tokens_posibles
            nuevos_tipos_de_tokens_posibles = []
            contador += 1

        # Si todos los estados de los afd de los tipos de token al evaluar el lexema son 'no aceptado' o 'trampa', y si la lista de
        # 'nuevos_tipos_de_tokens_posibles' no esta vacia, quiere decir que puedo agregar un caracter mas al lexema extraido del 
        # codigo fuente evaluado actualmente, y verificar si el nuevo lexema resultante pertenece a algun tipo de token
        elif len(nuevos_tipos_de_tokens_posibles) >= 1:
            antiguos_tipos_de_tokens_posibles = nuevos_tipos_de_tokens_posibles
            nuevos_tipos_de_tokens_posibles = []
            contador += 1

        # Si la lista de 'nuevos_tipos_de_tokens_posibles' esta vacia y la lista de 'antiguos_tipos_de_tokens_posibles' no esta vacia, 
        # quiere decir que debo quitarle un caracter al lexema extraido del codigo fuente evaluado actualmente y clasificar al nuevo lexema 
        # resultante con el tipo de token que tenga mayor prioridad dentro de la lista de 'antiguos_tipos_de_tokens_posibles'
        elif len(nuevos_tipos_de_tokens_posibles) == 0 and len(antiguos_tipos_de_tokens_posibles) >= 1:
            token = lexema[:-1]

            tipo_de_token_definitivo = antiguos_tipos_de_tokens_posibles[0] # El tipo de token con mayor prioridad esta en la posicion 0

            # Agrego el lexema ya clasificado como token, junto con su clasificacion, a la 'lista_final_de_tokens_con_sus_tipos'
            lista_final_de_tokens_con_sus_tipos.append((tipo_de_token_definitivo, token)) 

            # como ya clasifique el token extraido del codigo fuente desde la posicion 'inicio_del_token' hasta la posicion
            # anterior a 'fin_del_token' ahora analizo el token que comienza en la posicion anterior a 'fin_del_token'
            inicio_del_lexema = fin_del_lexema - 1

            # Vacio las listas con los tipos de tokens posibles antiguos y nuevos para analizar el siguiente token
            nuevos_tipos_de_tokens_posibles = []
            antiguos_tipos_de_tokens_posibles = []
        
        elif len(nuevos_tipos_de_tokens_posibles) == 0 and len(antiguos_tipos_de_tokens_posibles) == 0:
            print('Error: caracter o expresion invalidos')
    
    return lista_final_de_tokens_con_sus_tipos