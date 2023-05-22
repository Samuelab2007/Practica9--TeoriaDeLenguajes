# Practica9--TeoriaDeLenguajes
<h3>Analizador Sintáctico LL1</h3>

<p>Se codifican directamente todos los comportamientos posibles de la tabla LL1 para la gramática.<br>
El analizador realiza operaciones sobre la pila teniendo en cuenta el caracter que está procesando en la cadena de entrada.</p>

<p>Se alcanza el estado de aceptación cuando la pila está vacía y toda la cadena se pudo procesar.</p>

**Gramática reconocida por el Parser:**

E -> TE'<br>
E' -> +TE' | -TE' | lambda<br>
T -> FT'<br>
T' -> * FT' | /FT' | lambda<br>
F -> (E) | num | id<br>

num: Representa un numero entero cualquiera.
