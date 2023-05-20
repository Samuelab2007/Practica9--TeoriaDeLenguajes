# Signo @ como representacion de fin de cadena


# Descartar el uso del símbolo lambda(Simplemente borras de la pila) y del símbolo pesos.
# Existe una manera de simular todos los comportamientos de la tabla LL1.


# PROPUESTA: Codificar todas las combinaciones y comportamientos que existen en la tabla LL1
# DENTRO del analizador. Se seguiría usando la tabla, pero en el plantemiento inicial y nada más.


# El analizador sintáctico compara el tope con el caracter de la entrada.
# Si encuentra en el tope de pila un caracter igual al de la entrada, elimina los dos.
# Por el contrario, utiliza la tabla para realizar operaciones sobre la pila.


def analizarCadena(entrada):
    charindex = 0
    while charindex < len(entrada):  # Hago la lectura de la cadena.
        topePila = pila[-1]
        caracter = entrada[charindex]
        if topePila == "E":
            E(caracter)
        elif topePila == "e":
            EPrima(caracter)
        elif topePila == "T":
            T(caracter)
        elif topePila == "t":
            TPrima(caracter)
        elif topePila == "F":
            F(caracter)
        elif topePila == caracter:
            pila.pop()  # Elimino el terminal de la pila
            topePila = pila[-1]  # Actualizo el tope de pila
            charindex += 1  # Avanzo al siguiente caracter.
    if (
        len(pila) == 0
    ):  # TODO:Cuando la cadena se termina de leer y la pila no está vacía cabe la posibilidad
        # de que al reemplazar con lambda se llegue a una aceptación
        print("Cadena aceptada")


# Dependiendo del estado que esté en el tope de pila se llamará alguno de los métodos que están abajo.
def E(caracter):  # Funcion cuando el tope de pila es "E"
    if (caracter == "(") or (caracter in digitos) or caracter == "id":
        apilarProduccion("Te")


# Representaremos E' y T' como "e" y "t" respectivamente para evitar que reconozca el apostrofe como un caracter aparte.
# TODO: Hay inconvenientes para utilizar id, ya que este se compone de dos caracteres."i" y "d".


def EPrima(caracter):
    if caracter == "+":
        apilarProduccion("+Te")
    elif caracter == "-":
        apilarProduccion("-Te")
    elif (
        caracter == ")" or caracter == ""
    ):  # Representa lambda en la tabla. En este caso para ) y para cadena vacía.
        apilarProduccion("")


def T(caracter):
    if (caracter == "(") or (caracter in digitos) or caracter == "id":
        apilarProduccion("Ft")


def TPrima(caracter):
    if caracter == "*":
        apilarProduccion("*Ft")
    elif caracter == "/":
        apilarProduccion("/Ft")
    elif caracter in [
        "+",
        "-",
        ")",
        "",
    ]:  # Representa lambda en la tabla. En este caso para ) y para cadena vacía.
        apilarProduccion("")


def F(caracter):
    if caracter == "(":
        apilarProduccion("(E)")
    elif caracter in digitos:
        apilarProduccion(
            caracter
        )  # TODO: Apilar la producción "num" o "id" es innecesario y genera errores.
    elif (
        caracter == "id"
    ):  # Representa lambda en la tabla. En este caso para ) y para cadena vacía.
        apilarProduccion("id")


def apilarProduccion(produccion: str):
    pila.pop()  # Elimina el tope de pila
    i = len(produccion) - 1
    while i >= 0:
        char = produccion[i]
        pila.append(char)
        i -= 1
    topePila = pila[-1]
    # for char in produccion:
    #    pila.append(char)  # Apila en reverso la produccion.


digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pila = ["E"]  # Estado raíz del árbol sintáctico.

entrada = "2+1"


print(digitos)
analizarCadena(entrada)
print(pila)
