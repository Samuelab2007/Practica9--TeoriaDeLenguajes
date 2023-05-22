import AnalizadorLexico as AL
import AnalizadorSintacticoLL1 as AS

print("Ingrese la cadena ha analizar: ")
Lexer = AL.AnalizadorLexico(input())
try:
    Lexer.generarTokens()
    print("Los tokens generados por el Lexer son:")
    print(Lexer.getListaTokens())
    tokens = Lexer.getListaTokens()

    print("Resultado de analizar la cadena: ", AS.analizarCadena(tokens))
    print("El estado final de la pila es: ", AS.pila)
except ValueError:
    print("La cadena ingresada no pudo ser reconocida")
