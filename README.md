<p align="center">
    <a href="https://github.com/itsLithium/Ceibo">
        <img width="90%" align="center" src ="https://raw.githubusercontent.com/itsLithium/Ceibo/main/.readme/imgs/banner.png" />
    </a>
</p>

<a name="queEs"></a>
# ¿Qué es lenguaje Ceibo?
*Ceibo* es un lenguaje de programación con sintaxis en Español creado en [Python](https://es.wikipedia.org/wiki/Python), creado principalmente como metodo para reemplazar R-Info y Pseint. Éste proyecto nace de la necesidad de incrementar la educación de nivel básico y avanzado, para que niños, adolescentes y también adultos se motiven a entrar en el mundo de la programación y desarrollar aplicaciones en una sintaxis a su idioma. ademas, de justamente poder facilitar el aprendizaje dentro de la Universidad Nacional de La Plata proveyendo una herramienta mas actualizada y optimizada para estudiar R-Info


<a name="porQue"></a>
# ¿Por qué usar Ceibo?
*Ceibo* al ser un lenguaje de programación con sintaxis en Español nos provee de ciertas ventajas a la hora de programar en el.
1. **Intuitivo**:
    > Su sintaxis en Español hace más fácil la comprensión del código, reduciendo así el tiempo de aprendizaje al programar.
2. **Fácil**:
    > *Ceibo* tiene una sintaxis limpia y no requiere del uso de punto y coma (`;`) al final de cada código como en el caso se Java, Javascript, C/C++, entre otros.
3. **Lenguaje de alto nivel**:
    > Esto significa que es un lenguaje que se asemeja a la gramática que usamos para leer y escribir. Sin embargo, los [lenguajes de bajo nivel](https://es.wikipedia.org/wiki/Lenguaje_de_bajo_nivel) son aquellos que entiende la máquina tales como el [código binario](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina) o el [Lenguaje ensamblador](https://es.wikipedia.org/wiki/Lenguaje_ensamblador).
4. **Código abierto**:
    > Cualquiera puede descargar el código fuente de *Ceibo*, modificarlo, extender sus librerías y aportar en su desarrollo si así lo desea.

---

<a name="sintx"></a>
# SINTAXIS DE CEIBO
A continuación se explica de manera general la definición del lenguaje de programación *Ceibo*
<a name="comt"></a>
##  I. Comentarios:
Los comentarios se hacen encerrando lo que se deseea comentar con los simbolos `{` y `}`.
```pascal
{ Este es un comentario }
```

<a name="var"></a>
## II. Variables:
Las variables son identificadores asociados a valores.
```pascal
numerito : numero
numerito := 10
otronumerito : real
otronumerito := 19.2
```

<a name="puede"></a>
### __Un identificador puede:__
1. Empezar por guión bajo `_` o letras `a-z ó A-Z`. No son validas las letras acentuadas ni la `ñ` como letras en los identificadores.
2. Contener caracteres en mayúsculas y minúsculas.
Ceibo  es sensible a mayúsculas y minúsculas. Por lo que los siguientes identificadores no son los mismos.
```pascal
mensaje : real
Mensaje : numero
```

<a name="NOpuede"></a>
### __Un identificador NO puede:__
1. Empezar por un número.
2. Empezar por un símbolo, ni tampoco que sea una palabra reservada.


