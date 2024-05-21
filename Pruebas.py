from lexer.main import lexer

class Pruebas:
    def __init__(self, codigo:str, descripcion:str, numeroPrueba:int) ->None:
        self.codigo = codigo
        self.descripcion = descripcion
        self.numeroPrueba = numeroPrueba
    
    def getCodigo(self) -> str:
        return self.codigo
    def __getDescripcion(self) -> str:
        return self.descripcion
    def __getNumeroPrueba(self) -> int:
        return self.numeroPrueba

    def ejecutarPrueba(self):
        outputString:str = ""

        # Forma visual (en consola, aca  no, claramente) de ejecutar las pruebas con coleres
        outputString = f"\x1b[32m->Prueba N{self.__getNumeroPrueba()}\x1b[0m"
        outputString += f"\n\t\x1b[30m-->Descripcion:\x1b[0m{self.__getDescripcion()}"
        outputString += f"\n\t\x1b[36m-->Codigo a ejecutar:\x1b[0m\n{self.getCodigo()}"
        outputString += f"\x1b[33m\n\t-->Ejecutando...\x1b[0m"
        outputString += f"\x1b[35m\n\t-->Resultado obtenido:\x1b[0m {lexer(self.getCodigo())}\n\n"

        return outputString