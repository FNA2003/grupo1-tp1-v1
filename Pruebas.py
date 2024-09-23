from lexer_bauti.lexer import *
from parser_bauti.parser import *

#====================================================================================================================================
# Prueba 1
#====================================================================================================================================
print('==============================================================================================================================', end='\n\n')
print('Prueba N° 1:')


cadena = 'var pepito,pancho;procedure cuadrado;begin pepito:=pancho*pancho end;begin end#'

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 2
#====================================================================================================================================
print('Prueba N° 2:')

cadena = """
            var numero, triple ;
            procedure tripleDeUnNumero;
            begin
            numero := 3;
            triple := numero * 3
            end;
            begin
            call tripleDeUnNumero
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 3
#====================================================================================================================================
print('Prueba N° 3:')

cadena = """
            var numero, triple ;
            procedure tripleDeUnNumero;
            begin
            numero := 3;
            triple := numero * 3
            end;
            procedure dobleDeUnNumero;
            begin
            numero := 3;
            triple := numero * 2
            end;
            begin
            call tripleDeUnNumero;
            call dobleDeUnNumero
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 4
#====================================================================================================================================
print('Prueba N° 4:')

cadena = """
            const numero1 = 10, numero2 = 12 ;
            begin
                if numero1 <= numero2 then
                    begin
                        call print
                    end
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 5
#====================================================================================================================================
print('Prueba N° 5:')

cadena = """
            const numero1 = 1, numero2 = 2 ;
            procedure esVerdadero;
                var verdadero, falso;
                begin
                    verdadero := true;
                    falso := false;

                    while verdadero <> falso do
                        begin
                            numero1 := numero1 + numero2;
                            call returnTrue
                        end
                end;
            begin
                call esVerdadero
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')