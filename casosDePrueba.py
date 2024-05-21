from Pruebas import Pruebas


LISTA_PRUEBAS:list[Pruebas] = [
    Pruebas("procedure variableX variableY variable3 10200 0#const var \n\t ,;=:=call begin end if then while do odd< ><=>=<>+-*/()",
        "Buscamos comprobar que el lexer acepte todos los tokens propuestos", 1),


    Pruebas("vAr X,Y,Z;\n\nbEgiN\n\tX:=5;\n\tY:=3;\n\tZ:=X+Y;\nEnD#",
        "Prueba de programa suma basica", 2),

    Pruebas("var n,factorial;\n\nprocedure calculatefactorial;\nbegin\n\tif n=0 then\n\t\tfactorial := 1\n\telse\n\tbegin\n\t\tfactorial:=n;\n\t\tn:=n-1;\n\t\tcall calculatefactorial;\n\t\tfactorial:=factorial*n\n\tend\nend;\n\nbegin\n\tn:=5;\n\tcall calculatefactorial;\nend#",
        "Ejecutamos un programa funcional que calcula un factorial con una funcion (Note que el else se utiliza como id pues, en nuestra version de PL0 este no existe)", 3),

    Pruebas("var x;\n\nprocedure check;\nbegin\n\tif odd x then x:=x+1;\nend;\n\nbegin\n\tx:=5;\n\tcall check;\nend#",
        "Programa que suma 1 a la variable si es impar", 4),


    Pruebas("var n, fact, i;\n\nbegin\n\tn := 5;\n\tfact := 1;\n\ti := 0;\n\n\twhile i < n do\n\tbegin\n\t\tfact := fact * i;\n\tend;\nend#",
        "Programa para hallar el factorial de un numero, ahora usando un bucle y con tokens aceptados de microPL0", 5),
    
    Pruebas("var dueño, lugar;\nbegin\n\tdueño := 3;\n\tif dueño <> 1 then\n\t\tlugar := 0\nend#",
        "Caracter erroneo/No valido", 6),

    Pruebas("begin\nend.",
            "Finalizador de programa erroneo", 7),

    Pruebas("var cadena;\nbegin\n\tcadena := 'Hola mundo';\n\tif odd cadena <> 'Hola mundo' then\n\t\tcadena := 'Adios mundo';\nend#",
        "No existen strings/chars en este lenguaje", 8),

    Pruebas("var vAuxi;\nbegin\n\tvAuxi =: 10;\nend#",
        "Al asignar debemos respetar el orden de los simbolos", 9),

    Pruebas("vra begni clal proceduer dod fi thne od whiel conts",
        "Las palabras claves mal escritas seran id's", 10),
    
    Pruebas("begin\n\t200Hola\nend#",
        "Un numero seguido de letras sera un token numero y un token id", 11),
    
    Pruebas("var variable_auxiliar;\nbegin\nend#",
        "La convencion snake_case es invalida", 12),
    
    Pruebas("x; var\n\nbegin\nend#\n\tx := if 0 then;",
        "Cadenas sintactictamente erroneas y lexicamente correcta son aceptadas", 13),

    Pruebas("var contador, numero;\n\nprocedure contarHasta;\nbegin\n\twhile contador < numero do\n\t\tcontador := contador +1;\nend;\n\nbegin\n\tnumero := 5;\n\tcall contarHasta;\nend#",
        "Ejemplo de programa con contador en una funcion", 14)
]


cuerpoArchivo:str = ""
valorPrueba:str = ""



for Prueba in LISTA_PRUEBAS:
    valorPrueba = Prueba.ejecutarPrueba()
    print(valorPrueba)

    # Vamos a borrar los caracteres del codigo ANSI, pues no son validos en un txt
    valorPrueba = valorPrueba.replace("\x1b[32m", "")
    valorPrueba = valorPrueba.replace("\x1b[33m", "")
    valorPrueba = valorPrueba.replace("\x1b[0m", "")
    valorPrueba = valorPrueba.replace("\x1b[30m", "")
    valorPrueba = valorPrueba.replace("\x1b[35m", "")
    valorPrueba = valorPrueba.replace("\x1b[36m", "")

    cuerpoArchivo += valorPrueba

print("\n\n\n\x1b[33mTodas las pruebas serán, además, guardadas en un archivo llamado 'resultado.txt' en este directorio...\x1b[0m")

with open("resultado.txt", "w") as f:
    f.write(cuerpoArchivo)