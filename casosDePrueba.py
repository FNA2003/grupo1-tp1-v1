from Pruebas import Pruebas


LISTA_PRUEBAS:list[Pruebas] = [
    Pruebas("procedure variableX variableY variable3 10200 0#const var \n\t ,;=:=call begin end if then while do odd< ><=>=<>+-*/()",
                  "Buscamos comprobar que el lexer acepte todos los tokens propuestos", 1),


    Pruebas("vAr X,Y,Z;\n\nbEgiN\n\tX:=5;\n\tY:=3;\n\tZ:=X+Y;\nEnD#",
            "Prueba de programa suma basica", 2),

    Pruebas("var n,factorial;\n\nprocedure calculatefactorial;\nbegin\n\tif n=0 then\n\t\tfactorial := 1\n\telse\n\tbegin\n\t\tfactorial:=n;\n\t\tn:=n-1;\n\t\tcall calculatefactorial;\n\t\tfactorial:=factorial*n\n\tend\nend;\n\nbegin\n\tn:=5;\n\tcall calculatefactorial;\nend#",
            "Ejecutamos un programa funcional que calcula un factorial con una funcion (Note que el else se utiliza como id pues, en nuestra version de PL0 este no existe)", 3),

    Pruebas("var x;\n\nprocedure check;\nbegin\n\tif odd x then x:=x+1;\nend;\n\nbegin\n\tx:=5;\n\tcall check;\nend#",
            "Programa sin errores que suma 1 a la variable si es impar", 4)

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