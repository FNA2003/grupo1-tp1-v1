from lexer import * 

cadena = 'var pepito,pancho;procedure cuadrado;begin pepito:=pancho*pancho end;end#'

print(lexer(cadena))