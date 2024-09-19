from .Modulos.espaciosBlanco import *
from .Modulos.identificadores import *
from .Modulos.numeral import *
from .Modulos.numeros import *
from .Modulos.operadorAsignacion import *
from .Modulos.operadoresMatematicos import *
from .Modulos.operadoresRelacionales import *
from .Modulos.palabrasClave import *
from .Modulos.signosPuntuacion import *



# Lista de todos los tokens para armar los lexemas, en esta tambien se especifica el 
#valor de relevancia del lexer para cada token.
tokens_posibles = [ 
    ("if",afd_if), ("then",afd_then), ("call",afd_call), ("begin",afd_begin), 
    ("end",afd_end), ("while",afd_while), ("do",afd_do), ("odd",afd_odd), 
    ("const",afd_const), ("var",afd_var), ("relation",afd_relation), ("assign", afd_assignment),
    ("procedure", afd_procedure),("id",afd_id), ("multOperator",afd_multOperator), ("sumOperator",afd_sumOperator),  
    ("#", afd_sharp), ("num",afd_num),  ("coma", afd_coma), (";",afd_puntoComa), 
    ("(",afd_parenIzq), (")",afd_parenDer), ("blanckSpace", afd_whiteSpace)
] 




def lexerScanning(codigoFuente:str) -> str:
    """ Parte de escaneo de un lexer, dejo unicamente un espacio en blanco como maximo """

    # Variables utilizadas para poder 'rodear' los espacios en blanco consecutivos
    espacioDetectado:bool = False
    primerEspacio:int = 0
    # Variable del bucle
    iterador:int = 0


    while iterador < len(codigoFuente):
        # Se detecta un espacio en blanco
        if afd_whiteSpace(codigoFuente[iterador]):
            # Si es el primer espacio detectado guardamos su posicion en la cadena, si no lo es, seguimos, pues la 
            # variable de iteracion es el limite superior
            if not espacioDetectado:
                primerEspacio = iterador
                espacioDetectado = True
        else:
            # Si no se detecto un espacio en blanco (en este caracter) y, hubo uno previo
            #se modifica el string para que salte todos los espacios y tenga uno solo... Si no hubo otro, se prosigue de forma normal
            if espacioDetectado:
                codigoFuente = codigoFuente[0:primerEspacio] + " " + codigoFuente[iterador:]
                iterador = primerEspacio
                
            espacioDetectado = False           
        
        iterador += 1
    
    return codigoFuente



def lexer(codigoFuente:str)->list[tuple[str]]:
    # Lista de todos los tokens hallados hasta el momento
    tokens:list[tuple[str]] = []
    # Posicion del codigo para el iterador
    posicion_actual:int = 0
    # Valor que activo el token
    lexema:str = "" 
    # Booleano que indica si no se reconoce el lexema en esta longitud, tratamos de buscarlo con la siguiente
    errorLong:bool = False

    #Posibles tokens para los lexemas de longitud n
    posibles_tokensN:list[tuple[str]] = []
    # Posibles tokens para lexemas longitud (n+1)
    posibles_tokensN1:list[tuple[str]] = []

    # Hacemos la primer parte del lexer, el escaneo del codigo fuente y tomamos este resultado para el analisis lexicografico
    codigoLexeado:str = lexerScanning(codigoFuente)
    

    # Vamos a iterar el resultado del lexerScanning hasta que no queden caracteres en este,
    #pues, vamos a ir borrando los lexemas que activen un token del codigo escaneado.
    while len(codigoLexeado) != 0:
        # Vamos a armar el lexema cada vez que iteramos para comprobar si era valido
        lexema = codigoLexeado[0:posicion_actual+1]
        # En cada iteracion tratamos de llegar a tokens de lexema n+1
        posibles_tokensN1.clear() 


        # Recorremos la lista token-AFDdelmismo para tratar de validar un posible lexema n+1 (n inicialmente)
        #para poder guardar cada posible token para el lexema armado
        for (tipo_token, funcionAFD) in tokens_posibles:            
            if funcionAFD(lexema):
                posibles_tokensN1.append((tipo_token, lexema))

        
        # Si tenemos varios tokens en la lista de lexemas n+1 copiamos la lista de n+1 hacia la de n (es decir, seguimos 
        #buscamos tokens, pues estara probado que para esta longitud existen varios). 
        #Pero, si la lista de tokens para n es la misma para n+1 quiere decir que llegamos al ultimo token posible y debemos agregar
        #el de mayor valor (arbitrario) a la lista de tokens y terminar el analisis.
        if len(posibles_tokensN1) >= 1:
            if posibles_tokensN == posibles_tokensN1:
                tokens.append(posibles_tokensN[0])
                break
            posibles_tokensN = posibles_tokensN1.copy()
            errorLong = False #Este indica que se habia encontrado una string de longitud n cuando la longitud para el token es n+1

        # Si no hay mas valores en la lista n+1 puede significar que halla un token de longitud n
        #o que no lo hallo aun en el analisis o que este es un lexema invalido
        else:
            if len(posibles_tokensN) >= 1:
                # Agregamos el token a la lista de estos, lo borramos de la string del analisis
                #reiniciamos la lista de tokens de n (pues debemos seguir con el analisis)
                #y tambien, reiniciamos la variable de posicion de la string y volvemos al principio del ciclo while
                tokens.append(posibles_tokensN[0])
                posibles_tokensN.clear()
                codigoLexeado = codigoLexeado[posicion_actual:]
                posicion_actual = 0

                errorLong = False #Este indica que se habia encontrado una string de longitud n cuando la longitud para el token es n+1

                continue
            else:
                # Tratamos de averiguar si es que se debe de seguir analisando por si existe algun lexema
                #de mayor longitud a la cadena actual (y no se encontro por que la cadena tiene longitud + 1) o 
                # debemos de avisar de un error.
                if errorLong:
                    return f"ERROR!\nToken invalido:\t'{lexema[0]}'"
                
                errorLong = True
        
        # Sumamos la variable de iteracion
        posicion_actual += 1

    # Y, al finalizar el analisis lexicografico, devolvemos los tokens hallados
    i = 0
    ln = len(tokens)
    while i < ln:
        if tokens[i][0] == "blanckSpace":
            del tokens[i]
            i = 0
            ln = len(tokens)
        i += 1
    
    tokens.append(("EOF", "EOF"))

    return tokens
