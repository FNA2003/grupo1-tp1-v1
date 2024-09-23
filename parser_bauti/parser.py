from .SD_table import *

VN = {'Program', 'Block', 'ConstDecl', 'ConstAssigList', 'ConstAssigListAux', 'VarDecl', 'IdList', 
      'IdListAux', 'ProcDecl', 'ProcDeclAux', 'Statement', 'StatementList', 'StatementListAux', 
      'Condition', 'Relation', 'Expression', 'ExpressionAux', 'SumOperator', 'Term', 'TermAux', 
      'MultOperator', 'Factor'}

VT = {'if', 'then', 'call', 'begin', 'end', 'while', 'do', 'odd', 'const', 'var', 'comparation', 
      'assign', 'procedure', 'id', 'sumOperation', 'prodOperation','#', 'num', ',', ';', '(', ')', 'EOF'}

P = {}

def parser(classified_string):
     # print('classified_string: ', classified_string) # control
     if classified_string == None:
          print('No puede parsearse la cadena.')
          return None

     string = []
     for token_type, lexem in classified_string:
          string.append(token_type)
     # print('string: ', string) # control
          
     stack = ['Program', 'EOF']
     counter = 0
     t = string[counter]
     error = False

     while (counter <= len(string)-1) and not(error):
          # print('======================================================') # control
          # print('counter: ', counter, '| error: ', error) # control
          # print('stack: ', stack) # control
          top = stack[0]
          t = string[counter]
          # print('top: ', f"'{top}'") # control
          # print('t: ', f"'{t}'") # control
          if top in VT:
               if top == t:
                    stack.pop(0)
                    counter += 1
                    # print('stack consumiendo terminal: ', stack) # control
               else:
                    error = True
          elif top in VN:
               # print('M[t][top]: ', M[t][top]) # control
               if M[t][top] != None:
                    stack.pop(0)
                    stack = M[t][top] + stack
                    # print('stack con nueva produccion: ', stack) # control
               else:
                    error = True
          else:
               error = True
               
     if error:
          print('La cadena NO pertence al lenguaje')
          return None
     else:
          print('La cadena SI pertenece al lenguaje')
          return None