from lexer.main import lexer
from Pruebas import Pruebas


LISTA_PRUEBAS:list[Pruebas] = [
    Pruebas("procedure variableX variableY variable3 10200 0#const var \n\t ,;=:=call begin end if then while do odd< ><=>=<>+-*/()",
                  [('procedure','procedure'),('blanckSpace', ' '), ('id', 'variableX'), ('blanckSpace', ' '), ('id', 'variableY'), 
                    ('blanckSpace', ' '), ('id', 'variable3'), ('blanckSpace', ' '), 
                    ('num', '10200'), ('blanckSpace', ' '), ('num', '0'), ('#', '#'), ('const', 'const'), ('blanckSpace', ' '), 
                    ('var', 'var'), ('blanckSpace', ' '), ('coma', ','), (';', ';'), ('relation', '='), 
                    ('assign', ':='), ('call', 'call'), ('blanckSpace', ' '), ('begin', 'begin'),
                    ('blanckSpace', ' '), ('end', 'end'), ('blanckSpace', ' '), ('if', 'if'), 
                    ('blanckSpace', ' '), ('then', 'then'), ('blanckSpace', ' '), ('while', 'while'), 
                    ('blanckSpace', ' '), ('do', 'do'), ('blanckSpace', ' '), ('odd', 'odd'), 
                    ('relation', '<'), ('blanckSpace', ' '), ('relation', '>'), ('relation', '<='), 
                    ('relation', '>='), ('relation', '<>'), ('sumOperator', '+'), 
                    ('sumOperator', '-'), ('multOperator', '*'), ('multOperator', '/'), ('(', '('), (')', ')')],
                  "Buscamos comprobar que el lexer acepte todos los tokens propuestos", 1),


    Pruebas("vAr X,Y,Z;\n\nbEgiN\n\tX:=5;\n\tY:=3;\n\tZ:=X+Y;\nEnD#",
            [('var', 'vAr'), ('blanckSpace', ' '), ('id', 'X'), ('coma', ','),('id', 'Y'),('coma', ','),('id', 'Z'),(';', ';'), ('blanckSpace', ' '),
             ('begin', 'bEgiN'), ('blanckSpace', ' '), ('id', 'X'), ('assign',':='), ('num', '5'), (';', ';'), 
             ('blanckSpace', ' '), ('id', 'Y'), ('assign',':='), ('num', '3'), (';', ';'), ('blanckSpace', ' '),
             ('id', 'Z'), ('assign', ':='), ('id','X'),('sumOperator', '+'),('id','Y'), (';',';'), ('blanckSpace', ' '), ('end', 'EnD'), ('#','#')],
            "Damos un programa en una combinacion minuscula/mayuscula para demostrar que este no es case-sensitive", 2),

    Pruebas("VAR n,factorial;\n\nPROCEDURE calculateFactorial;\nBEGIN\n\tIF n=0 THEN\n\t\tfactorial := 1\n\tELSE\n\tBEGIN\n\t\tfactorial:=n;\n\t\tn:=n-1;\n\t\tCALL calculateFactorial;\n\t\tfactorial:=factorial*n\n\tEND\nEND;\n\nBEGIN\n\tn:=5;\n\tCALL calculateFactorial;\nEND#",
            [('var', 'VAR'), ('blanckSpace', ' '), ('id', 'n'), ('coma', ','), ('id', 'factorial'), (';', ';'), 
             ('blanckSpace', ' '), ('procedure', 'PROCEDURE'), ('blanckSpace', ' '), ('id', 'calculateFactorial'), 
             (';', ';'), ('blanckSpace', ' '), ('begin', 'BEGIN'), ('blanckSpace', ' '), ('if', 'IF'), ('blanckSpace', ' '), 
             ('id', 'n'), ('relation', '='), ('num', '0'), ('blanckSpace', ' '), ('then', 'THEN'), ('blanckSpace', ' '), 
             ('id', 'factorial'), ('blanckSpace', ' '), ('assign', ':='), ('blanckSpace', ' '), ('num', '1'), ('blanckSpace', ' '), 
             ('id', 'ELSE'), ('blanckSpace', ' '), ('begin', 'BEGIN'), ('blanckSpace', ' '), ('id', 'factorial'), 
             ('assign', ':='), ('id', 'n'), (';', ';'), ('blanckSpace', ' '), ('id', 'n'), ('assign', ':='), ('id', 'n'), ('sumOperator', '-'), 
             ('num', '1'), (';', ';'), ('blanckSpace', ' '), ('call', 'CALL'), ('blanckSpace', ' '), ('id', 'calculateFactorial'), 
             (';', ';'), ('blanckSpace', ' '), ('id', 'factorial'), ('assign', ':='), ('id', 'factorial'), ('multOperator', '*'), 
             ('id', 'n'), ('blanckSpace', ' '), ('end', 'END'), ('blanckSpace', ' '), ('end', 'END'), (';', ';'), ('blanckSpace', ' '), 
             ('begin', 'BEGIN'), ('blanckSpace', ' '), ('id', 'n'), ('assign', ':='), ('num', '5'), (';', ';'), ('blanckSpace', ' '), 
             ('call', 'CALL'), ('blanckSpace', ' '), ('id', 'calculateFactorial'), (';', ';'), ('blanckSpace', ' '), ('end', 'END'), ('#', '#')],
            "Ejecutamos un programa funcional que calcula un factorial con una funcion (Note que el else se utiliza como id pues, en nuestra version de PL0 este no existe)", 3),

    Pruebas("VAR x;\n\nPROCEDURE check;\nBEGIN\n\tIF ODD x THEN x:=x+1;\nEND;\n\nBEGIN\n\tx:=5;\n\tCALL check;\nEND#",
            [('var', 'VAR'), ('blanckSpace', ' '), ('id', 'x'), (';', ';'), ('blanckSpace', ' '), ('procedure', 'PROCEDURE'), ('blanckSpace', ' '), ('id','check'),
             (';',';'), ('blanckSpace', ' '), ('begin', 'BEGIN'), ('blanckSpace', ' '), ('if', 'IF'), ('blanckSpace', ' '), ('odd', 'ODD'), ('blanckSpace', ' '), 
             ('id', 'x'), ('blanckSpace', ' '), ('then', 'THEN'), ('blanckSpace', ' '), ('id', 'x'), ('assign',':='), ('id','x'), ('sumOperator', '+'), ('num', '1'), (';',';'),
             ('blanckSpace', ' '), ('end', 'END'), (';', ';'), ('blanckSpace', ' '), ('begin', 'BEGIN'), ('blanckSpace', ' '), ('id', 'x'), ('assign', ':='), ('num', '5'),
             (';',';'), ('blanckSpace', ' '), ('call', 'CALL'), ('blanckSpace', ' '),('id', 'check'), (';',';'),('blanckSpace', ' '),('end', 'END'), ('#','#')],
            "Programa sin errores que suma 1 a la variable si es impar", 4)

]


cuerpoArchivo:str = ""
valorPrueba:str = ""



for Prueba in LISTA_PRUEBAS:
    valorPrueba = Prueba.compararValorLexer(  lexer( Prueba.getCodigo() )  )
    print(valorPrueba)

    # Vamos a borrar los caracteres del codigo ANSI, pues no son validos en un txt
    valorPrueba = valorPrueba.replace("\x1b[32m", "")
    valorPrueba = valorPrueba.replace("\x1b[33m", "")
    valorPrueba = valorPrueba.replace("\x1b[0m", "")
    valorPrueba = valorPrueba.replace("\x1b[30m", "")
    valorPrueba = valorPrueba.replace("\x1b[35m", "")
    valorPrueba = valorPrueba.replace("\x1b[36m", "")

    cuerpoArchivo += valorPrueba

print("\n\n\n\x1b[33mTodas las pruebas seran guardadas en un archivo llamado 'resultado.txt' en este directorio...\x1b[0m")

with open("resultado.txt", "w") as f:
    f.write(cuerpoArchivo)