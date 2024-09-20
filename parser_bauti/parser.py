from SD_table import *

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
    
    while (counter <= len(string)-1) and not(error):
      top = stack[0]
      if top in VT:
            if top == t:
                  stack.pop(0)
                  counter += 1
                  t = string[counter]
            else:
                  error = True
      elif top in VN:
            if M[t][top] != None:
                  stack.pop(0)
                  stack = M[t][top] + stack
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