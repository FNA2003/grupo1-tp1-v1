from lexer import * 

#====================================================================================================================================
# Prueba 1
#====================================================================================================================================
print('==============================================================================================================================', end='\n\n')
print('Prueba N° 1:')


cadena = 'var pepito,pancho;procedure cuadrado;begin pepito:=pancho*pancho end;end#'

print(lexer(cadena), end='\n\n')
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 2
#====================================================================================================================================
print('Prueba N° 2:')

cadena = """
            var numero, triple ;
            procedure tripleDeUnNumero;
            begin
            numero := 3
            triple := numero * 3
            end;
            end#
        """

print(lexer(cadena), end='\n\n')
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 3
#====================================================================================================================================
print('Prueba N° 3:')

cadena = 'var 123pepito,    pancho;1procedure cuadrado34;begin pepito:=3pancho*7pancho 6end;end9#'

print(lexer(cadena), end='\n\n')
print('==============================================================================================================================', end='\n\n')