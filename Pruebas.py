from lexer.lexer import *
from parser.parser import *

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

#====================================================================================================================================
# Prueba 6
#====================================================================================================================================
print('Prueba N° 6:')

cadena = """
            const max = 100;
            var i, sum, temp;
            procedure calculateSum;
            begin
                i := 1;
                sum := 0;
                while i <= max do
                begin
                    if odd i then
                        sum := sum + i;
                    i := i + 1
                end
            end;
            begin
                call calculateSum;
                if sum > 1000 then
                    temp := sum / 2;
                    temp := sum * 2
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 7
#====================================================================================================================================
print('Prueba N° 7:')

cadena = """
            var a, b, max;
            begin
                a := 10;
                b := 20;
                if a > b then
                    max := a
                else
                    max := b
            end#
        """
# Falla por el 'else'

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 8
#====================================================================================================================================
print('Prueba N° 8:')

cadena = """
            var n, f, i;
            begin
                n := 5;
                f := 1;
                i := 1;
                while i <= n do
                begin
                    f := f * i;
                    i := i + 1
                end
            end
        """
# Falla porque no tiene el simbolo de fin de programa '#'

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 9
#====================================================================================================================================
print('Prueba N° 9:')

cadena = """
            var num, positivo, negativo, cero;
            begin
                num := -5;
                if num > 0 then
                    positivo := 1;
                if num < 0 then
                    negativo := 1;
                if num = 0 do
                    cero := 1
            end#
        """
# Falla por poner 'do' en vez de 'then' en la declaracion 'if condition then'

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')

#====================================================================================================================================
# Prueba 10
#====================================================================================================================================
print('Prueba N° 10:')

cadena = """
            var n, result;
            procedure factorial;
                var i;
            begin
                result := 1;
                i := 1;
                while i <= n do
                begin
                    result := result * i;
                    i := i + 1;
                end;
            end;
            begin
                n := 5;
                call factorial;
            end#
        """

print('Cadena clasificada: ', lexer(cadena))
print('Resultado del parser: ', end='')
parser(lexer(cadena))
print('==============================================================================================================================', end='\n\n')