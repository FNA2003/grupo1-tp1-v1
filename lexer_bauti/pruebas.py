from lexer import * 

cadena = 'var pepito,pancho;procedure cuadrado;begin pepito:=pancho*pancho end;end#'

print(lexer(cadena))

cadena = """
            var numero, triple ;
            procedure tripleDeUnNumero;
            begin
            numero := 3
            triple := numero * 3
            end;
            end#
        """

print(lexer(cadena))