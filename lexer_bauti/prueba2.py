import sys
import os

# Añadir la ruta de la carpeta parser_bauti al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'parser_bauti')))

# Ahora puedes importar parser.py
import parser

from lexer import *

string = """
            var numero, triple ;
            procedure tripleDeUnNumero;
            begin
            numero := 3
            triple := numero * 3
            end;
            end#
        """

classified_string = lexer(string)

print(classified_string)

parser.parser(classified_string)