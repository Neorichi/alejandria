---
type: Artículo de enciclopedia
title: Complejidad y criptografía
description: La criptografía es la ciencia encargada del estudio y diseño de sistemas que permiten ocultar información.
resource: https://es.wikipedia.org/wiki/Complejidad_y_criptografía
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Complejidad_y_criptografía"}
license: CC BY-SA 4.0
id: eswiki-Complejidad_y_criptografía
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Complejidad y criptografía

La criptografía es la ciencia encargada del estudio y diseño de sistemas que permiten ocultar información. Desde sus inicios, esta capacidad de encubrimiento se ha basado en la dificultad que supondría a una entidad no autorizada el obtener la información original escondida en un conjunto de datos cifrado.

Los avances en computación de la segunda mitad del  pusieron en riesgo la integridad de los sistemas usados hasta entonces, a la vez que proporcionaban medios para la creación de otros nuevos y más seguros. Es en este punto donde la teoría de la complejidad, encargada de estudiar los recursos necesarios para el cómputo de los algoritmos, cobra importancia dentro de la criptografía. Esto se debe a que los nuevos algoritmos criptográficos basarán su seguridad en la *dificultad* de ejecutar las operaciones necesarias para obtener la información original de un criptograma, siendo la ya mencionada teoría de la complejidad quien determinará cuál es esta *dificultad*.

Un algoritmo tiene utilidad si es *fácilmente* resoluble, esto es, pertenece a la clase P (Talbot, 2006:15). Sin embargo, desde un punto de vista criptográfico, no poder hallar una solución a un problema de una forma práctica en términos computacionales (es decir, no pertenecer a la clase P) se traduce en seguridad (Rothe, 2005:2).

A pesar de haberse desarrollado por separado, en la actualidad ambos campos están fuertemente ligados: La criptografía depende de los resultados proporcionados por la teoría de la complejidad, a la vez que las investigaciones en esta última son en muchas ocasiones promovidas por problemas desarrollados en un marco criptográfico (Rothe, 2005:1).

 Problemas matemáticos útiles en criptografía
En la actualidad, la criptografía está considerada una rama tanto de la informática como de las matemáticas. Existe una serie de problemas matemáticos comúnmente utilizados en los sistemas criptográficos.

 Tests de primalidad
Los números primos han sido la base de varios criptosistemas de clave pública, entre ellos RSA o el criptosistema de Rabin. Su utilidad reside en la *facilidad* de multiplicar dos números primos *grandes* para obtener un número compuesto y en la dificultad de hallar la descomposición en factores primos dado un número obtenido de la multiplicación de dos primos *grandes*. Sin embargo, no es trivial comprobar que uno de estos números sea realmente primo. Este problema ha sido investigado a conciencia y se han descubierto algunos tests de primalidad que reducen su complejidad.

 Test de Fermat
El test de Fermat se fundamenta en el pequeño teorema de Fermat, que demuestra que, si *n* es primo, para cualquier número natural *a* coprimo con *n* se cumple que

Se trata de un test probabilístico que, para determinar si un número *n* es primo, realiza la prueba anterior para diferentes valores de *a*. Cuantos más valores se prueben, mayor probabilidad de que *n* sea realmente primo. La fiabilidad de este test reside en el hecho de que si un número es compuesto, entonces es muy probable obtener un valor de *a* tal que

Para un número *k* de pruebas y un tamaño de entrada *m*, la complejidad del algoritmo es . No obstante, este test apenas se utiliza, debido entre otras cosas a los números de Carmichael, que siempre satisfacen la igualdad del pequeño teorema de Fermat pero no son primos.

 Solovay-Strassen
Se trata de un test probabilístico basado en el criterio de Euler, del cual se obtiene que para un número *n* primo se cumple que

siempre que *a* y *n* sean coprimos. Su coste computacional para una entrada de tamaño *m* es , donde *k* es el número de valores diferentes de *a* con los que se prueba. En caso de devolver como resultado “primo”, la probabilidad de que *n* no lo sea es menor que (1/2)*k*. Sin embargo, el uso de este test ha caído ante el de Miller-Rabin, ya que este último es más eficiente en la práctica y al menos tan fiable como el de Solovay-Strassen (Rothe, 2005:329) (Menezes, 1997:137).

 Miller-Rabin
El test de primalidad de Miller-Rabin es el más usado en la actualidad. Al igual que los anteriores, se trata de un test probabilístico. Está basado en el siguiente hecho: Sean *n* un número primo y *a* un número coprimo con *n*. Para cualquier *n* existe un *r* impar tal que *n - 1 = 2sr*. Entonces, o bien

 o bien existe algún *j* tal que  para el que se cumple que

El coste computacional de este algoritmo, al igual que ocurría con Solovay-Strassen, es de  para una entrada de tamaño *m*. Sin embargo, Miller-Rabin no sólo es más rápido en la práctica, sino que es más fácil de implementar (no incluye al símbolo de Jacobi en sus operaciones) y ofrece una cota de error de (1/4)*k* frente a (1/2)*k* para *k* pruebas distintas (Menezes, 1997:141).

 AKS
Diseñado en 2002 por Manindra Agrawal, Neeraj Kayal y Nitin Saxena, AKS es el primer algoritmo determinista de primalidad. Sirvió además para demostrar que este problema pertenece a la clase de complejidad P y, por tanto, es computacionalmente practicable. Sin embargo, su orden de complejidad es , por lo que, para propósitos generales, se sigue recomendando Miller-Rabin (Talbot, 2006:75).

 Factorización de enteros
La dificultad de descomponer números enteros en sus factores primos ha sido la base de diversos criptosistemas, entre ellos RSA. Aún no se conocen algoritmos eficientes para resolver este problema, por lo que la seguridad de aquellos sistemas basados en esto está garantizada en este aspecto. Sí existen, sin embargo, algoritmos para factorizar números con determinadas características, por lo que conviene tomar ciertas precauciones a la hora de elegir los números que serán la base de un criptosistema.

 División por tentativa
Dado un número *n* obtenido a partir de la multiplicación de dos números primos, probar con todos los números impares menores que  hasta encontrar el primero que lo divida. Es fácil demostrar que, en el peor caso, habría que hacer  divisiones (si no se comprueba que cada divisor sea verdaderamente primo). Por tanto, este algoritmo requiere  operaciones para una entrada de tamaño *m*.

 Algoritmo *p - 1* de Pollard
El algoritmo p - 1 de Pollard es efectivo para números *n* obtenidos del producto de *p* y *q* primos tales que los factores primos de *p – 1* son *pequeños*. El tiempo de cómputo de este algoritmo es  para una entrada de tamaño *m*, donde *B* es el límite superior de los números *pequeños*. Dado que requiere tiempo polinómico, es de suma importancia evitar este tipo de números en criptosistemas basados en el producto de números primos, como RSA, ya que éstos podrían ser factorizados de forma *rápida*, poniendo en peligro su seguridad.

 Criba general de campo de números
Actualmente es el algoritmo de factorización más rápido conocido. Su complejidad, dado un número de tamaño *m*, es , siendo *c* una constante que depende de la variante del algoritmo.

 Algoritmo de Shor para factorización de enteros
Se trata de un algoritmo cuántico capaz de descomponer un número *n* en tiempo . Dado que se trata de un algoritmo teórico, los criptosistemas basados en la factorización de enteros no corren peligro. Sin embargo, si llegase a implementarse en un computador cuántico, estos criptosistemas pasarían a ser inseguros, entre ellos RSA.

 Problema del logaritmo discreto
Al igual que ocurría con los números primos, el problema del logaritmo discreto ha sido la base de diversos sistemas criptográficos, entre ellos el criptosistema de ElGamal o el protocolo de intercambio de claves de Diffie-Hellman. Consiste en lo siguiente: Sea *p* un número primo,  un generador de  y un elemento  , encontrar un *x* tal que

o lo que es lo mismo:

Este problema también ha sido estudiado en profundidad, aunque ni se ha descubierto aún ningún algoritmo eficiente ni se ha logrado determinar su complejidad (Rothe, 2005:369).

 Búsqueda exhaustiva
Es el algoritmo de fuerza bruta para el problema del logaritmo discreto. Siendo *p*,  y  conocidos, se puede optar por probar todos los posibles valores de *x* menores que *p*. No obstante, esto requeriría del orden de *p* operaciones. Por tanto, para una entrada de tamaño *m*, este algoritmo tiene una complejidad temporal de .

 Algoritmo paso-gigante paso-enano
Se trata de un algoritmo cuya complejidad temporal y espacial es . Pese a mejorar al anterior algoritmo, éste sigue siendo poco eficiente y, en consecuencia, desaconsejado (Rothe, 2005: 368).

 Algoritmo rho de Pollard para logaritmos discretos
Este algoritmo, cuya complejidad temporal para una entrada de *m* bits es , tiene una complejidad espacial despreciable, siendo entonces más eficiente que el algoritmo paso-gigante paso-enano y por tanto preferible (Menezes, 1997:106).

 Algoritmo de Shor para logaritmos discretos
El mismo algoritmo cuántico usado para la factorización de enteros también puede ser aplicado al problema del logaritmo discreto.

 Criptosistemas de clave pública
Los criptosistemas de clave pública son aquellos que utilizan claves distintas para cifrar y descifrar, siendo una de estas claves accesible por todos los usuarios (pública) y la otra conocida solo por su propietario (privada). Suelen estar fundamentados en el uso de funciones trampa, esto es, funciones fáciles de computar si se conoce cierta información, pero difíciles si se desconoce. Una característica fundamental es que no se pueda deducir la clave privada a partir de la clave pública. La mayoría de estos sistemas están basados en los problemas de la factorización de enteros y el logaritmo discreto. También hubo diseños basados en el problema de la mochila, pero algunos fueron criptoanalizados con éxito, por lo que este enfoque ya no se utiliza.

 RSA
Presentado en 1977 por Ron Rivest, Adi Shamir y Leonard Adleman, se trata del criptosistema de clave pública más usado hasta la fecha (Menezes, 1997:285). Por esta razón, ha sido objeto de estudios minuciosos que, aunque no han logrado criptoanalizarlo, han detectado debilidades cuando se usan determinadas claves.

Está basado en el problema de la factorización de enteros. Su proceso de generación de claves es el siguiente:
 Se eligen dos números primos *p* y *q* suficientemente grandes y se multiplican .
 Se elige un exponente *e* coprimo con (p-1)(q-1) tal que 1 < e < (p-1)(q-1).
 Se halla *d*, el inverso de *e* módulo *(p-1)(q-1)*.
 La clave pública es el par (*e*, *n*) y la privada es *d*.

Para cifrar un texto *m*, éste se parte en trozos *m1*, ... , *mk* tales que *mi* representa un entero en el rango [0, *n-1*]. A continuación, para cada uno de los *mi* se computa

.

Para descifrar el criptograma, para cada *ci* se computa

.

Un ataque para hallar la clave privada *d* podría ser intentar factorizar *n* y hallar *e* siguiendo un proceso similar al de generación de claves. Esto demuestra que romper RSA tiene a lo sumo la misma complejidad que la factorización de enteros.

 Riesgos en la generación de claves de RSA
 Recordemos que el algoritmo p-1 de Pollard es capaz de descomponer en tiempo polinómico un número *n* producto de dos primos *p* y *q* tales que los factores primos de *p-1* son *pequeños*. Por tanto, es importante comprobar que los números que vamos a utilizar para generar las claves de RSA no cumplan esta propiedad. De lo contrario, se podría usar este algoritmo para factorizar *n* y hallar la clave privada *d* partiendo de *e*. (Talbot, 2006:153)
 Se ha demostrado que cuando *p* y *q* tienen valores cercanos, se puede descomponer *n* recurriendo a la división por tentativa con valores en un entorno cercano a  en un tiempo *razonable*. (Talbot, 2006:153)
 Para evitar la factorización de *n* mediante el algoritmo de factorización de curva elíptica de Lenstra, *p* y *q* deben tener aproximadamente la misma longitud (en bits) y ser ésta lo suficientemente larga. (Menezes, 1997:290)
 Si se cumple que , entonces partiendo de la clave pública se puede usar una aproximación por fracciones continuas para hallar *d* en tiempo polinómico. Además, se conjetura que si , entonces debe existir algún algoritmo eficiente para hallar la clave privada a partir de la pública. (Talbot, 2006:154)

 Criptosistema de Merkle-Hellman
Diseñado por Ralph Merkle y Martin Hellman en 1978, este criptosistema se basaba en el problema de la mochila, el cual se sabe que pertenece a la clase NP. Como clave privada se usa una sucesión supercreciente de *n* elementos y como clave pública una sucesión obtenida a partir de la multiplicación modular de la primera, que no resultará supercreciente. Para cifrar un mensaje *M* de *n* bits, se suman los valores *i*-ésimos de la clave pública tales que para el bit *i*-ésimo del mensaje se cumple *mi = 1*, obteniendo un criptograma *C*. Para descifrar el mensaje, se usa un algoritmo voraz que halla los valores *i* de la sucesión supercreciente que suman *C*. Los procesos de cifrado y descifrado son considerablemente más rápidos que los de RSA (Talbot, 2006:162).

La seguridad del criptosistema de Merkle-Hellman se basaba en que, dado un criptograma *C* y una clave pública *Kpu*, hallar los valores de *Kpu* tales que suman *C* se reduce a resolver el problema de la mochila, el cual es computacionalmente intratable. Sin embargo, en 1984 Adi Shamir diseñó un algoritmo que, para la mayoría de los casos, permitía obtener la clave privada partiendo de la clave pública en tiempo polinómico, y con ello descifrar los criptogramas (Menezes, 1997:302). Sin embargo, debe hacerse notar que este algoritmo NO resuelve el problema de la mochila, tan solo halla la clave privada del criptosistema. En consecuencia, no aporta nueva información sobre el problema P=NP (Talbot, 2006:162).

 Criptosistema de McEliece
Diseñado en 1978 por Robert McEliece, el criptosistema de McEliece se fundamenta en otro problema de la clase NP, la corrección de códigos lineales. En concreto, se usan códigos de Goppa, ya que para éstos se conocen algoritmos de corrección eficientes. La idea principal es ocultar el mensaje introduciendo errores de un modo que el receptor sepa corregirlos. La clave privada consiste en una matriz *G* correctora de hasta un número *t* de errores, una matriz binaria invertible *S* y una matriz de permutaciones *P*. La clave pública consiste en el producto *SGP* de las tres matrices anteriores y el parámetro *t*.

A pesar de tratarse de un criptosistema cuyos procesos de cifrado y descifrado son relativamente rápidos, apenas recibe uso. Esto es debido principalmente a sus tamaños de clave (219 bits = 64 Mbytes para la clave pública) y a su factor de expansión del mensaje (para los parámetros recomendados por McEliece, el criptograma tiene un tamaño un 60% mayor que el mensaje en claro) (Menezes, 1997:299). Sin embargo, dado que el algoritmo de Shor no afecta a este criptosistema, parece fiable frente a la computación cuántica.

 Criptografía de curva elíptica
Propuesta de forma independiente por Neal Koblitz y Victor Miller en 1985, la criptografía de curva elíptica se basa en las matemáticas de curvas elípticas. Su fortaleza reside en el problema del logaritmo discreto, el cual se cree que para el caso de los conjuntos de puntos usados en estos criptosistemas es aún más difícil de resolver que en el caso de los campos finitos del problema original. Esto permite que la criptografía de curva elíptica garantice la misma seguridad que otros criptosistemas asimétricos con una longitud de clave mucho más corta (RSA-1024  ECC-160, RSA-3072  ECC-256, RSA-15360  ECC-512). No obstante, existen algunas curvas específicas para las que se conocen algoritmos que resuelven el logaritmo discreto en tiempo polinómico. Estas deben evitarse. Por ello, el NIST ha elaborado una lista de curvas recomendadas.

 Referencias

 Notas
