class Pruebas:
    def __init__(self, codigo:str, esperado:list[tuple[str]], descripcion:str, numeroPrueba:int) ->None:
        self.codigo = codigo
        self.esperado = esperado
        self.descripcion = descripcion
        self.numeroPrueba = numeroPrueba
    
    def getCodigo(self) -> str:
        return self.codigo
    def __getEsperado(self) -> list[tuple[str]]:
        return self.esperado
    def __getDescripcion(self) -> str:
        return self.descripcion
    def __getNumeroPrueba(self) -> int:
        return self.numeroPrueba

    def compararValorLexer(self, resultadoLexer:list[tuple[str]]):
        outputString:str = ""
        resultadoEsperado:str = ""

        # Forma visual (en consola, aca  no, claramente) de ejecutar las pruebas con coleres
        outputString = f"\n\n\x1b[32m->Prueba N{self.__getNumeroPrueba()}\x1b[0m"
        outputString += f"\n\t\x1b[30m-->Descripcion:\x1b[0m{self.__getDescripcion()}"
        outputString += f"\n\t\x1b[36m-->Codigo a ejecutar:\x1b[0m\n{self.getCodigo()}"
        outputString += f"\x1b[35m\n\t-->Resultado esperado:\x1b[0m {self.__getEsperado()}"
        outputString += f"\x1b[33m\n\t-->Ejecutando...\x1b[0m"
        outputString += f"\x1b[36m\n\t-->Resultado obtenido:\x1b[0m {resultadoLexer}"

        # Verificamos si el resultado del lexer es la esperada
        resultadoEsperado = ("\x1b[32mTrue\x1b[0m" if resultadoLexer == self.__getEsperado() else "\x1b[31mFalse\x1b[0m")
        outputString += f"\x1b[35mValidacion de igualdad:\x1b[0m {resultadoEsperado}"

        return outputString