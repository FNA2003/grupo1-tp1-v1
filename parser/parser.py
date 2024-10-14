from .SD_table import *

VN = {'Program', 'Block', 'ConstDecl', 'ConstAssigList', 'ConstAssigListAux', 'VarDecl', 'IdList', 
      'IdListAux', 'ProcDecl', 'ProcDeclAux', 'Statement', 'StatementList', 'StatementListAux', 
      'Condition', 'Relation', 'Expression', 'ExpressionAux', 'SumOperator', 'Term', 'TermAux', 
      'MultOperator', 'Factor'}

VT = {'if', 'then', 'call', 'begin', 'end', 'while', 'do', 'odd', 'const', 'var', 'comparation', 
      'assign', 'procedure', 'id', 'sumOperation', 'prodOperation','#', 'num', ',', ';', '(', ')', 'EOF'}

P = {}

def parser(classified_string):
     if classified_string == None:
          print('No puede parsearse la cadena.')
          return None

     string = []
     for token_type, lexem in classified_string:
          string.append(token_type)
          
     stack = ['Program', 'EOF']
     counter = 0
     t = string[counter]
     error = False
     productions = [] # guardar producciones

     while (counter <= len(string)-1) and not(error):
          top = stack[0]
          t = string[counter]

          if top in VT:
               if top == t:
                    stack.pop(0)
                    counter += 1
               else:
                    error = True
          elif top in VN:
               if M[t][top] != None:
                    stack.pop(0)
                    production = M[t][top]
                    stack = M[t][top] + stack
                    productions.append((top, production))  # guardar la produccion
               else:
                    error = True
          else:
               error = True
               
     if error:
          print('La cadena NO pertence al lenguaje')
          return None
     else:
          print('La cadena SI pertenece al lenguaje')
          # imprimir las producciones utilizadas para realizar la derivacion
          print('')
          for production in productions:
            print(f"{production[0]} -> {' '.join(production[1])}")
          
          # imprmir la derivacion de la cadena
          print('\n', "===============================================================", end='\n\n')
          last_derivation= ["Program"]
          print("Program", end='')
          for production in productions:
               non_terminal = production[0]
               non_terminal_index = last_derivation.index(non_terminal)
               right_side_derivation = last_derivation[0 : non_terminal_index] + production[1] + (last_derivation[(non_terminal_index + 1):] if non_terminal_index < (len(last_derivation) + 1) else [])
               print(f" -> {' '.join(right_side_derivation)}", end='')
               last_derivation = right_side_derivation
          print('')
          return None