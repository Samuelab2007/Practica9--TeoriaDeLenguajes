import AnalizadorLexico as AL

# Signo @ como representacion de fin de cadena


# Descartar el uso del símbolo lambda(Simplemente borras de la pila).


# PROPUESTA: Codificar todas las combinaciones y comportamientos que existen en la tabla LL1
# DENTRO del analizador. Se seguiría usando la tabla, pero en el plantemiento inicial y nada más.


# El analizador sintáctico compara el tope con el caracter de la entrada.
# Si encuentra en el tope de pila un caracter igual al de la entrada, elimina los dos.
# Por el contrario, realiza operaciones sobre la pila.


def analizarCadena(entrada):  # Entrada: Lista de tokens
    charindex = 0
    while charindex < len(entrada):  # Hago la lectura de la lista.
        if len(pila) > 0:
            topePila = pila[-1]
        token = entrada[charindex]
        if topePila == "E":
            E(token)
        elif topePila == "e":
            EPrima(token)
        elif topePila == "T":
            T(token)
        elif topePila == "t":
            TPrima(token)
        elif topePila == "F":
            F(token)
        elif topePila == token["valor"]:
            pila.pop()  # Elimino el terminal de la pila
            if len(pila) > 0:
                topePila = pila[-1]  # Actualizo el tope de pila
            elif token["tipo"] == "FIN_DE_CADENA":
                return "Cadena Válida"
            else:
                return "Cadena Inválida"
            charindex += 1  # Avanzo al siguiente caracter.
    if (  # Al terminar la cadena se está llendo por el lado del else y no hace nada más, dejando la pila con elementos
        len(pila) == 0
    ):  # TODO:Cuando la cadena se termina de leer y la pila no está vacía cabe la posibilidad
        # de que al reemplazar con lambda se llegue a una aceptación
        return "Cadena aceptada"


# Dependiendo del estado que esté en el tope de pila se llamará alguno de los métodos que están abajo.
def E(token):  # Funcion cuando el tope de pila es "E"
    if (
        (token["tipo"] == "PARENTESIS_IZQUIERDO")
        or (token["tipo"] == "INTEGER")
        or token["tipo"] == "IDENTIFICADOR"
    ):
        apilarProduccion("Te")


# Representaremos E' y T' como "e" y "t" respectivamente para evitar que reconozca el apostrofe como un caracter aparte.


def EPrima(token):
    if token["tipo"] == "OPERADOR_SUMA":
        apilarProduccion("+Te")
    elif token["tipo"] == "OPERADOR_RESTA":
        apilarProduccion("-Te")
    elif (
        token["tipo"] == "PARENTESIS_DERECHO"
    ):  # Representa lambda en la tabla. En este caso para PARENTESIS_DERECHO
        pila.pop()
    elif (
        token["tipo"] == "FIN_DE_CADENA"
    ):  # En el caso de la cadena vacía o el fin de la cadena
        if len(pila) > 0:
            pila.pop()
        else:
            return "Cadena Inválida"


def T(token):
    if (
        (token["tipo"] == "PARENTESIS_IZQUIERDO")
        or (token["tipo"] == "INTEGER")
        or token["tipo"] == "IDENTIFICADOR"
    ):
        apilarProduccion("Ft")


def TPrima(token):
    if token["tipo"] == "OPERADOR_MULTIPLICACION":
        apilarProduccion("*Ft")
    elif token["tipo"] == "OPERADOR_DIVISION":
        apilarProduccion("/Ft")
    elif token["tipo"] in [
        "OPERADOR_SUMA",
        "OPERADOR_RESTA",
        "PARENTESIS_DERECHO",
    ]:  # Representa lambda en la tabla. En este caso para ) y para cadena vacía.
        pila.pop()
    elif token["tipo"] == "FIN_DE_CADENA":
        if len(pila) > 0:
            pila.pop()
        else:
            return "Cadena Inválida"


def F(token):
    if token["tipo"] == "PARENTESIS_IZQUIERDO":
        apilarProduccion("(E)")
    elif token["tipo"] == "INTEGER" or token["tipo"] == "IDENTIFICADOR":
        pila.pop()
        pila.append(token["valor"])
        # Apilamos los valores de los terminales encontrados "num" or "id"


def apilarProduccion(produccion: str):
    pila.pop()  # Elimina el tope de pila
    i = len(produccion) - 1
    while i >= 0:
        char = produccion[i]
        pila.append(char)
        i -= 1


pila = ["@", "E"]  # Estado raíz del árbol sintáctico.

Lexer = AL.AnalizadorLexico("21+4*(id+57)")
Lexer.generarTokens()
print(Lexer.getListaTokens())

entrada = Lexer.getListaTokens()


print(analizarCadena(entrada))
print(pila)
