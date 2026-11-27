---
type: Artículo de enciclopedia
title: Factorización de polinomios sobre cuerpos finitos
description: En matemáticas y cálculo simbólico la factorización de un polinomio consiste en descomponerlo en un producto de factores irreducibles.
resource: https://es.wikipedia.org/wiki/Factorización_de_polinomios_sobre_cuerpos_finitos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Factorización_de_polinomios_sobre_cuerpos_finitos"}
license: CC BY-SA 4.0
id: eswiki-Factorización_de_polinomios_sobre_cuerpos_finitos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Factorización de polinomios sobre cuerpos finitos

En matemáticas y cálculo simbólico la factorización de un polinomio consiste en descomponerlo en un producto de factores irreducibles. Esta descomposición es teóricamente posible y es única para polinomios con coeficientes en cualquier cuerpo, pero se necesitan restricciones bastante fuertes en el cuerpo de los coeficientes para permitir el cálculo de la factorización mediante un algoritmo. En la práctica, los algoritmos se han diseñado solo para polinomios con coeficientes en un cuerpo finito, en los números racionales o en una extensión de cuerpos de uno de ellos.

Todos los algoritmos de factorización, incluido el caso de los polinomios con múltiples variables sobre los números racionales, reducen el problema a este caso; véase factorización de polinomios. También se utiliza para diversas aplicaciones de cuerpos finitos, como la teoría de códigos (códigos de verificación de redundancia cíclica y el código BCH), criptografía (criptografía asimétrica mediante curvas elípticas) y teoría de números computacional.

Como la reducción de la factorización de polinomios a la de polinomios de una variable no tiene especificidad en el caso de coeficientes en un cuerpo finito, en este artículo solo se consideran polinomios con una variable.

Antecedentes

Cuerpo finito

La teoría de cuerpos finitos, cuyos orígenes se remontan a los trabajos de Carl Friedrich Gauss y Évariste Galois, ha jugado un importante papel en varias ramas de las matemáticas. Debido a la aplicabilidad del concepto en otros temas de matemáticas y ciencias como la informática, ha habido un resurgimiento del interés en los cuerpos finitos, lo que se debe en parte a importantes aplicaciones en teoría de códigos y criptografía. Las aplicaciones de cuerpos finitos introducen algunos de estos desarrollos en criptografía, cálculo simbólico y teoría de códigos.

Un cuerpo de Galois o cuerpo finito es un cuerpo con un orden finito (número de elementos). El orden de un cuerpo finito es siempre un número primo o una potencia de un número primo. Para cada potencia prima *q* = *pr*, existe exactamente un cuerpo finito con *q* elementos, salvo isomorfismo. Este cuerpo se indica como *GF*(*q*) o **F** *q*. Si *p* es primo, *GF*(*p*) es la característica de orden *p*; es el cuerpo de las clases de residuos respecto al módulo *p*, y sus elementos *p* se denotan 0, 1, ..., *p*-1. Así, *a* = *b* en *GF*(*p*) significa lo mismo que *a* ≡ *b* (mod *p*).

Polinomios irreducibles
Sea *F* un cuerpo finito. En cuanto a los cuerpos generales, se dice que un polinomio no constante *f* en *F*[*x*] es irreducible sobre *F* si no es el producto de dos polinomios de grado positivo. Un polinomio de grado positivo que no es irreducible sobre *F* se llama *reducible sobre F*.

Los polinomios irreducibles permiten construir los cuerpos finitos de orden no primo. De hecho, para una potencia primaria *q*, sea **F***q* el cuerpo finito con *q* elementos, únicos salvo por isomorfismos. Un polinomio *f* de grado *n* mayor que uno, que es irreducible sobre **F***q*, define una extensión de cuerpo de grado *n* que es isomorfo al cuerpo con *q**n* elementos, que son los polinomios de grado inferior a *n*; la suma, resta y multiplicación por un elemento de **F***q* son los de los polinomios; el producto de dos elementos es el resto de la división por *f* de su producto como polinomios; el inverso de un elemento puede calcularse mediante el algoritmo MCD extendido (véase aritmética de extensiones algebraicas).

De ello se deduce que, para calcular en un cuerpo finito de orden no primo, es necesario generar un polinomio irreducible. Para ello, el método común es tomar un polinomio al azar y probar su irreducibilidad. En aras de la eficiencia de la multiplicación en el cuerpo, es habitual buscar polinomios de la forma *x**n* + *ax* + *b*.

Los polinomios irreducibles sobre cuerpos finitos también son útiles para los generadores de números pseudoaleatorios que utilizan registros de desplazamiento de retroalimentación y logaritmos discretos sobre **F**2*n*.

El número de polinomios mónicos irreducibles de grado n sobre **F***q* es el número de collares aperiódicos, dado por la función de conteo de collares de Moreau *M**q*(*n*). La función de collar estrechamente relacionada *N**q*(*n*) cuenta los polinomios mónicos de grado *n* que son primarios (una potencia de un irreducible); o, alternativamente, polinomios irreducibles de todos los grados *d* que dividen a *n*.

Ejemplo
El polinomio *P* = *x*4 + 1 es irreducible sobre **Q** pero no sobre ningún cuerpo finito.

 En cualquier extensión de cuerpo de **F**2, *P* = (*x* + 1)4.
 En todos los demás cuerpos finitos, al menos uno de −1, 2 y −2 es un cuadrado, porque el producto de dos no cuadrados es un cuadrado, por lo que se tiene que
Si  entonces
Si  entonces
Si  entonces

Complejidad
Los algoritmos de factorización polinomial utilizan operaciones polinomiales básicas como productos, divisiones, máximo común divisor (mcd), potencias de un polinomio con otro módulo, etc. Una multiplicación de dos polinomios de grado *n* como máximo se puede realizar en operaciones *O*(*n*2) en **F***q* usando aritmética *clásica*, o en *O* con las operaciones (*n*log(*n*) log (log (*n*))) en **F***q* usando aritmética *rápida*. Se puede realizar una división euclídea (división con resto) en períodos de tiempo similares. La dificultad de obtener un máximo común divisor polinómico entre dos polinomios de grado como máximo *n* se puede tomar como operaciones *O*(*n*2) en **F***q* usando métodos clásicos, o como *O*(*n*log2(*n*) log(log(*n*))) operaciones en **F***q* usando métodos rápidos. Para dos polinomios *h* y *g* de grado como máximo *n*, la exponenciación *hq* mod *g* se puede hacer con *O*(log(*q*)) productos polinómicos, usando el método de exponenciación binaria, es decir *O*(*n*2log(*q*)) operaciones en **F***q* usando métodos clásicos, o *O*(*n*log(*q*) log(*n*) log(log (*n*))) operaciones en **F***q* usando métodos rápidos.

En los algoritmos que siguen, las complejidades se expresan en términos de número de operaciones aritméticas en **F***q*, utilizando algoritmos clásicos para la aritmética de polinomios.

Algoritmos de factorización
Muchos algoritmos para factorizar polinomios sobre cuerpos finitos incluyen las siguientes tres etapas:
 Factorización libre de cuadrados
 Factorización en grados distintos
 Factorización de igual grado
Una excepción importante es el algoritmo de Berlekamp, que combina las etapas 2 y 3.

Algoritmo de Berlekamp

El algoritmo de Berlekamp es históricamente importante por ser el primer algoritmo de factorización, que funciona bien en la práctica. Sin embargo, contiene un bucle en los elementos del cuerpo subyacente, lo que implica que es practicable solo en pequeños cuerpos finitos. Para un cuerpo subyacente fijo, su complejidad temporal es polinomial, pero, para cuerpos subyacentes generales, la complejidad es exponencial según el tamaño del cuerpo.

Factorización libre de cuadrados
El algoritmo determina una factorización libre de cuadrados para polinomios cuyos coeficientes provienen del cuerpo finito **F***q* de orden *q* = *pm* con *p* primo. Este algoritmo determina primero la derivada y luego calcula el mcd del polinomio y su derivada. Si no es uno, el mcd vuelve a dividir el polinomio original, siempre que la derivada no sea cero (un caso que existe para polinomios no constantes definidos sobre cuerpos finitos).

Este algoritmo utiliza el hecho de que, si la derivada de un polinomio es cero, entonces es un polinomio en *x**p*, que es, si los coeficientes pertenecen a **F***p*, la *p* potencia del polinomio obtenido al sustituir *x* por *x*1/*p*. Si los coeficientes no pertenecen a **F***p*, la raíz *p*-ésima de un polinomio con derivada cero se obtiene mediante la misma sustitución en *x*, completada aplicando el inverso del automorfismo de Frobenius a los coeficientes.

Este algoritmo funciona también sobre un cuerpo de característica cero, con la única diferencia de que nunca entra en los bloques de instrucciones donde se calculan las *p* raíces. Sin embargo, en este caso, el algoritmo de Yun es mucho más eficiente porque calcula los máximos divisores comunes de polinomios de grados inferiores. Una consecuencia es que, al factorizar un polinomio sobre los enteros, no se utiliza el algoritmo que sigue: primero se calcula la factorización libre de cuadrados sobre los enteros, y para factorizar los polinomios resultantes, se elige un *p* tal que permanecen libres de cuadrados de módulo *p*.

 **Algoritmo**: **SFF** (Factorización sin cuadrados)
     **Entrada**: Un polinomio mónico *f* en **F***q* [*x*] donde *q = pm*
     **Salida**: Factorización libre de cuadrados de *f*
     *R* ← 1

     # Hacer que *w* sea el producto (sin multiplicidad) de todos los factores de *f* que tienen
     # multiplicidad no divisible por *p*
     *c* ← **mcd** (*f*, *f*′)
     *w* ← *f*/*c*

     # Paso 1: Identificar todos los factores en *w*
     *i* ← 1
     **mientras***w* ≠ 1 **hacer**
         *y* ← **mcd** (*w*, *c*)
         * fac * ← *w*/*y*
         *R* ← *R* · *fac**i*
         *w* ← *y*; *c* ← *c*/*y*; *i* ← *i + 1*
     **terminar mientras**
     # *c* es ahora el producto (con multiplicidad) de los factores restantes de *f*

     # Paso 2: identificar todos los factores restantes mediante recursividad
     # Téngase en cuenta que estos son los factores de *f* que tienen multiplicidad divisible por *p*
     **si** *c* ≠ 1 **entonces**
         *c* ← *c*1/*p*
         *R* ← *R* · **SFF** (*c*)*p*
     **terminar si**

     **Salida** (*R*)

La idea es identificar el producto de todos los factores irreducibles de *f* con la misma multiplicidad. Esto se hace en dos pasos. El primer paso usa la derivada formal de *f* para encontrar todos los factores con multiplicidad no divisible por *p*. El segundo paso identifica los factores restantes. Como todos los factores restantes tienen multiplicidad divisible por *p*, lo que significa que son potencias de *p*, simplemente se puede tomar la raíz cuadrada de *p* y aplicar la recursividad.

Ejemplo de factorización libre de cuadrados
Sea

que se desea factorizar sobre el cuerpo con tres elementos.

El algoritmo calcula primero

Dado que la derivada no es cero, se tiene que  y se entra en el ciclo *mientras*. Después de un bucle se tiene que ,  y  con actualizaciones ,  y . La segunda vez a través del ciclo resulta , , , con actualizaciones ,  y . La tercera vez a través del bucle tampoco cambia . Pasando por cuarta vez a través del bucle se obtiene , , , con actualizaciones ,  y . Dado que *w* = 1, se sale del bucle *mientras*. Dado que *c* ≠ 1, debe ser un cubo perfecto, la raíz cúbica de *c*, obtenida al reemplazar * x*3 por *x* es *x*2 + 1, y llamar al procedimiento sin cuadrados determina de forma recursiva que el resultado está libre de cuadrados. Por lo tanto, dividirlo en un cubo y combinarlo con el valor de *R* hasta ese punto da la descomposición sin cuadrados

Factorización de grados distintos
Este algoritmo divide un polinomio libre de cuadrados en un producto de polinomios cuyos factores irreducibles tienen todos el mismo grado. Sea *f* ∈ **F***q*[*x*] de grado *n* el polinomio a factorizar.

 **Algoritmo** Factorización de grados distintos (DDF)
     **Entrada**: Un polinomio mónico libre de cuadrados
     **Salida**: El conjunto de todos los pares , tales que
               tiene un factor irreducible de grado  y
               es el producto de todos los factores mónicos irreducibles de  de grado .
     **Empezar**

         **mientras**  **hacer**

             **si** , **entonces**
                 ;

             **terminar si**

         **fin  mientras**;
         **si** , **entonces** ;
         **si** , **entonces devuelve** ,
             **si no devuelve**
     **Final**

La corrección del algoritmo se basa en lo siguiente:

A primera vista, este procedimiento no es eficiente, ya que implica calcular el MCD de polinomios de un grado que es exponencial con el grado del polinomio de entrada. Sin embargo

puede ser reemplazado por

Por lo tanto, se tiene que calcular:

hay dos métodos:

Factorización de igual grado

Algoritmo de Cantor-Zassenhaus

En esta sección, se considera la factorización de un polinomio mónico de una variante libre de cuadrados *f*, de grado *n*, sobre un cuerpo finito **F***q*, que tiene *r* ≥ 2 factores irreducibles distintos por pares  cada uno de grado *d*.

Primero se describe un algoritmo de Cantor y Zassenhaus (1981) y luego una variante que tiene una complejidad ligeramente mejor. Ambos son algoritmos probabilísticos cuyo tiempo de ejecución depende de elecciones aleatorias (algoritmo de Las Vegas) y tienen un buen tiempo de ejecución medio. En la siguiente sección se describe un algoritmo de Shoup (1990), que también es un algoritmo de factorización de igual grado, pero es determinista. Todos estos algoritmos requieren un orden impar *q* del cuerpo de coeficientes. Para obtener más algoritmos de factorización, consúltese por ejemplo el libro de Knuth *The Art of Computer Programming* volumen 2.

 **Algoritmo** Algoritmo de Cantor-Zassenhaus.
     **Entrada:** Un cuerpo finito **F***q* de orden impar *q*.
            Un polinomio mónico libre de cuadrados*f* en **F***q* [*x*] de grado *n* = *rd*,
                 que tiene *r* ≥ 2 factores irreducibles cada uno de grado *d*
     **Salida:** El conjunto de factores mónicos irreducibles de *f*.

     Factores: = {*f*};
     mientras Tamaño (factores) < *r* hacer,
         Elegir *h* en **F***q* [*x*] con grados (*h*) < *n* aleatoriamente;

         para cada *u* en Factores con deg(*u*) > *d* hacer
             si mcd (*g*, *u*) ≠ 1 y mcd(*g*, *u*) ≠ *u*, entonces
                 Factores: = Factors;
             terminar si;
     mientras tanto

     Devolver los factores

La exactitud de este algoritmo se basa en el hecho de que el anillo **F***q*[*x*]/*f* es un producto directo de los cuerpos **F***q*[*x*]/*fi* donde *fi* se ejecuta en los factores irreductibles de *f*. Como todos estos cuerpos tienen *qd* elementos, el componente de *g* en cualquiera de estos cuerpos es cero con probabilidad

Esto implica que el polinomio mcd (*g*, *u*) es el producto de los factores de *g* para los cuales el componente de *g* es cero.

Se ha demostrado que el número medio de iteraciones del bucle *mientras* del algoritmo es menor que , lo que da un número medio de operaciones aritméticas en **F***q* que es .

En el caso típico cuando *d* log (*q*) > *n*, esta complejidad puede reducirse a

eligiendo *h* en el núcleo de la aplicación lineal

y reemplazando la instrucción

por

La prueba de validez es la misma que la anterior, reemplazando el producto directo de los cuerpos **F***q*[*x*]/*fi* por el producto directo de sus subcuerpos con *q* elementos. La complejidad se descompone en  para el algoritmo en sí,  para el cálculo de la matriz de la aplicación lineal (que puede estar ya calculado en la factorización libre de cuadrados) y *O*(*n*3) para computar su núcleo. Cabe señalar que este algoritmo también funciona si los factores no tienen el mismo grado (en este caso, el número "r" de factores, necesario para detener el ciclo *mientras*, se encuentra como la dimensión del núcleo). Sin embargo, la complejidad es ligeramente mejor si se realiza la factorización sin cuadrados antes de usar este algoritmo (dado que *n* puede disminuir con la factorización sin cuadrados, esto reduce la complejidad de los pasos críticos).

Algoritmo de Victor Shoup
Como los algoritmos de la sección anterior, el algoritmo de Victor Shoup es un algoritmo de factorización de igual grado. A diferencia de ellos, es un algoritmo determinista. Sin embargo, es menos eficiente, en la práctica, que los algoritmos de la sección anterior. Para el algoritmo de Shoup, la entrada está restringida a polinomios sobre cuerpos primos **F** *p*.

El peor caso de complejidad temporal del algoritmo de Shoup tiene un factor . Aunque exponencial, esta complejidad es mucho mejor que la de los algoritmos deterministas anteriores (algoritmo de Berlekamp) que tienen como factor . Sin embargo, hay muy pocos polinomios para los cuales el tiempo de cálculo es exponencial y la complejidad de tiempo promedio del algoritmo es polinomial en  donde  es el grado del polinomio y  es el número de elementos del cuerpo subyacente.

Sea *g* = *g*1 ... *gk* la factorización deseada, donde *gi* son polinomios mónicos irreducibles distintos de grado *d*. Sea *n* = deg(*g*) = *kd*. Considérese el anillo *R* = **F***q*[*x*]/*g* y se denota también por *x* la imagen de *x* en *R*. El anillo *R* es el producto directo de los cuerpos *Ri* = **F***q*[*x*]/*gi*, y se denota por *pi* el homomorfismo natural de *R* sobre *Ri*. El grupo de Galois de *Ri* sobre **F***q* es cíclico de orden *d*, generado por el automorfismo *u* → *up*. De ello se deduce que las raíces de *gi* en *Ri* son

Como en el algoritmo anterior, este algoritmo usa la misma subálgebra *B* sobre *R* que el algoritmo de Berlekamp, a veces denominada *subálgebra de Berlekamp* y definida como

Un subconjunto *S* de *B* se dice un conjunto con separación si, por cada 1 ≤ *i* < *j* ≤ *k* existe un *s* ∈ *S* tal que . En el algoritmo anterior, se construye un conjunto con separación eligiendo al azar los elementos de *S*. En el algoritmo de Shoup, el conjunto con separación se construye de la siguiente manera. Sea *s* en *R*[*Y*] tal que

Entonces  es un conjunto con separación porque  para *i* = 1, ..., *k* (los dos polinomios mónicos tienen las mismas raíces). Como los *gi* son distintos por pares, para cada par de índices distintos (*i*, *j*), al menos uno de los coeficientes *sh* satisfará

Teniendo un conjunto con separación, el algoritmo de Shoup procede como el último algoritmo de la sección anterior, simplemente reemplazando la instrucción "elegir al azar *h* en el núcleo de la aplicación lineal " por "elegir (*h* + *i*) con *h* en *S* e *i* en {1, ...,*k* - 1}".

Complejidad temporal
Como se describió en secciones anteriores, para la factorización sobre cuerpos finitos, existen algoritmos probabilistas (por ejemplo, el algoritmo de Cantor-Zassenhaus), lo que condiciona su complejidad temporal. También existen algoritmos deterministas con una complejidad media polinomial (por ejemplo, el algoritmo de Shoup).

La existencia de un algoritmo determinista con una complejidad polinomial en el peor de los casos sigue siendo un problema abierto.

Prueba de irreducibilidad de Rabin
Al igual que el algoritmo de factorización de distintos grados, el algoritmo de Rabin se basa en el Lema mencionado anteriormente. El algoritmo de factorización de grados distintos prueba cada *d* no mayor que la mitad del grado del polinomio de entrada. El algoritmo de Rabin aprovecha que los factores no son necesarios para considerar al menos *d*. De lo contrario, es similar al algoritmo de factorización de distintos grados. Se basa en el siguiente hecho.

Sean *p*1, ..., *pk*, todos los divisores primos de *n*, y sea , para 1 ≤ *i* ≤ *k* un polinomio *f* en **F***q*[*x*] de grado *n* irreducible en **F***q*[*x*] si y solo si , para 1 ≤ *i* ≤ *k*, y *f* divide a . De hecho, si *f* tiene un factor de grado que no divide a *n*, entonces *f* no divide a ; si *f* tiene un factor de grado que divide a *n*, entonces este factor divide al menos uno de los

 **Algoritmo** Prueba de irreducibilidad de Rabin
     **Entrada**: Un polinomio mónico *f* en **F***q*[*x*] de grado *n*,
         *p*1, ..., *pk* todos los divisores primos distintos de *n*.
     **Salida**: O "*f* es irreducible" o "*f* es reducible".

     **para** *j* = 1 a *k* **hacer**
         ;
     **para** *i* = 1 a *k* **hacer**
         ;
         *g*: = mcd (*f*, *h*);
         **si** *g* ≠ 1, **entonces return** "*f* es reducible" **y STOP**;
     **fin de**;
     ;
     **si** *g* = 0, **entonces return** "*f* es irreducible",
         **else return** "*f* es reducible"

La idea básica de este algoritmo es calcular  a partir del  más pequeño mediante cuadratura repetida o usando el automorfismo de Frobenius, y luego tomar el mcd correspondiente. Usando la aritmética polinómica elemental, el cálculo de la matriz del automorfismo de Frobenius necesita  operaciones en **F***q*, el cálculo de

necesita *O*(*n*3) operaciones adicionales, y el algoritmo mismo necesita *O*(*kn*2) operaciones, dando un total de  operaciones en **F***q*. Usando aritmética rápida (de complejidad  para la multiplicación y la división, y  operaciones para el cálculo del MCD), el cálculo de  por cuadratura repetida es de complejidad , y el algoritmo en sí es , dando un total de  operaciones en **F***q*.

Véase también
 Algoritmo de Berlekamp
 Algoritmo de Cantor-Zassenhaus
 Factorización de polinomios

Referencias

Bibliografía
 KEMPFERT, H (1969) 'Factorización de polinomios' ' Departamento de Matemáticas, Universidad Estatal de Ohio, Columbus, Ohio 43210
 Shoup, Victor (1996) * Suavidad y factorización de polinomios sobre cuerpos finitos * Departamento de Ciencias de la Computación de la Universidad de Toronto
 Von Zur Gathen, J.; Panario, D. (2001). Factorización de polinomios sobre cuerpos finitos: una encuesta.  Journal of Symbolic Computation, Volumen 31, números 1 a 2, enero de 2001, 3 a 17.
 Gao Shuhong, Panario Daniel, "Prueba y construcción de polinomios irreducibles sobre cuerpos finitos", Departamento de Ciencias Matemáticas, Universidad de Clemson, Carolina del Sur, 29634-1907, EE. UU. y el Departamento de Ciencias de la Computación de la Universidad de Toronto, Canadá M5S-1A4
 Shoup, Victor (1989) Nuevo Algoritmos para encontrar polinomios irreducibles en cuerpos finitos Departamento de Ciencias de la Computación Universidad de Wisconsin & ndash; Madison
 Geddes, Keith O.; Czapor, Stephen R .; Labahn, George (1992). Algoritmos para álgebra informática. Boston, MA: Kluwer Academic Publishers. págs. xxii + 585. .

Enlaces externos
 Algunos polinomios irreducibles http://www.math.umn.edu/~garrett/m/algebra/notes/07.pdf
 Campo y teoría de Galois: http://www.jmilne.org/math/CourseNotes/FT.pdf
 Campo Galois: http://designtheory.org/library/encyc/topics/gf.pdf
 Factorización de polinomios sobre cuerpos finitos: http://www.science.unitn.it/~degraaf/compalg/polfact.pdf
