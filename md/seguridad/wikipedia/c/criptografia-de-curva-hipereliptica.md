---
type: Artículo de enciclopedia
title: Criptografía de curva hiperelíptica
description: "La criptografía de curva hiperelíptica es similar a criptografía de curva elíptica (CCE) en la medida en que el jacobiano de un curva hiperelíptica es un grupo abeliano en el que se realizan operaciones aritméticas, del …"
resource: https://es.wikipedia.org/wiki/Criptografía_de_curva_hiperelíptica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_de_curva_hiperelíptica"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_de_curva_hiperelíptica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía de curva hiperelíptica

La **criptografía de curva hiperelíptica** es similar a criptografía de curva elíptica (CCE) en la medida en que el jacobiano de un curva hiperelíptica es un grupo abeliano en el que se realizan operaciones aritméticas, del mismo modo que se usa el grupo de puntos en una curva elíptica en criptografía de curva elíptica.

 Definición
Una curva hiperelíptica imaginaria de genus  sobre un cuerpo  viene dada por la ecuación  donde  es un polinomio de grado no mayor que  y  es un polinomio mónico de grado . De esta definición se deduce que las curvas elípticas son curvas hiperelípticas de género 1. En criptografía de curvas hiperelípticas,  suele ser un cuerpo finito. El jacobiano de , denotado como , es una grupo cociente, por lo que los elementos del jacobiano no son puntos, sino clases de equivalencia divisoras de grado 0 bajo la relación de equivalencia lineal. Esto concuerda con el caso de la curva elíptica, porque se puede demostrar que el jacobiano de una curva elíptica es isomorfo con el grupo de puntos en la curva elíptica. El uso de curvas hiperelípticas en criptografía surgió en 1989 a partir del trabajo de Neal Koblitz. Aunque se introdujo solo 3 años después de la criptografía de curva elíptica, no muchos criptosistemas incluyen curvas hiperelípticas porque la implementación de la aritmética no es tan eficiente como con los criptosistemas basados en curvas elípticas o factorización (RSA). La eficiencia de implementar la aritmética depende del campo finito subyacente , en la práctica resulta que los campos finitos con característica 2 son una buena opción para implementaciones de hardware, mientras que el software suele ser más rápido en característica impar.

El jacobiano en una curva hiperelíptica es un grupo abeliano y, como tal, puede servir como grupo para el problema del logaritmo discreto (PLD). En resumen, supongamos que tenemos un grupo abeliano  y  un elemento de . El PLD en  implica encontrar el entero  dados dos elementos de , a saber,  y . El primer tipo de grupo utilizado fue el grupo multiplicativo de un cuerpo finito; posteriormente, también se utilizaron jacobianos de curvas (hiper)elípticas. Si la curva hiperelíptica se elige cuidadosamente, entonces el método rho de Pollard es la forma más eficiente de resolver el PLD. Esto significa que, si el jacobiano tiene  elementos, el tiempo de ejecución es exponencial en . Esto permite usar jacobianos de un orden bastante pequeño, lo que hace que el sistema sea más eficiente. Pero si la curva hiperelíptica se elige mal, el PLD será bastante fácil de resolver. En este caso, hay ataques conocidos que son más eficientes que los solucionadores genéricos de logaritmo discreto o incluso subexponenciales. Por lo tanto, estas curvas hiperelípticas deben evitarse. Considerando varios ataques al PLD, es posible enumerar las características de las curvas hiperelípticas que deben evitarse.

 Ataques contra el PLD
Todos los ataques genéricos contra el problema del logaritmo discreto en grupos abelianos finitos, como el algoritmo de Pohlig-Hellman y el método rho de Pollard pueden usarse para atacar el PLD en el jacobiano de curvas hiperelípticas. El ataque de Pohlig-Hellman reduce la dificultad del PLD al considerar el orden del grupo con el que se trabaja. Supóngase que el grupo  utilizado tiene  elementos, donde  es la factorización prima de . Pohlig-Hellman reduce el PLD en  al PLD en subgrupos de orden  para . Así, para , el mayor divisor primo de , el PLD en  es igual de difícil de resolver que el PLD en el subgrupo de orden . Por lo tanto, se desea elegir  de tal manera que el mayor divisor primo  de  sea casi igual a  mismo. Generalmente, basta con exigir que .

El algoritmo de cálculo de índices es otro algoritmo que puede utilizarse para resolver el problema del logaritmo discreto (PLD) en ciertas circunstancias. Para los jacobianos de curvas (hiper)elípticas, existe un ataque de cálculo de índices contra el PLD. Si el género de la curva es demasiado alto, el ataque será más eficiente que el rho de Pollard. Hoy en día se sabe que incluso un género  no garantiza la seguridad. Por consiguiente, quedan las curvas elípticas e hiperelípticas de género 2.

Otra restricción sobre las curvas hiperelípticas que se pueden usar proviene del ataque de Menezes-Okamoto-Vanstone / ataque de Frey-Rück. El primero, a menudo llamado MOV por sus siglas en inglés, fue desarrollado en 1993, el segundo surgió en 1994. Considérese una curva (hiper)elíptica  sobre un cuerpo finito  donde  es la potencia de un número primo. Supóngase que el jacobiano de la curva tiene  elementos y  es el mayor divisor primo de . Para  el entero positivo más pequeño tal que  existe un homomorfismo de grupos inyectivo computable del subgrupo de  de orden  a . Si  es pequeño, se puede resolver el problema PLD en  mediante el ataque de cálculo de índices en . Para curvas arbitrarias,  es muy grande (aproximadamente del tamaño de ); y por lo tanto, aunque el ataque de cálculo de índices es bastante rápido para grupos multiplicativos de cuerpos finitos, este ataque no representa una amenaza para la mayoría de las curvas. La función inyectiva utilizada en este ataque es un emparejamiento y existen algunas aplicaciones en criptografía que hacen uso de este tipo de funciones. En dichas aplicaciones, es importante equilibrar la dificultad del problema PLD en  y . Dependiendo de la fortaleza de seguridad, los valores de  entre 6 y 12 resultan útiles. El subgrupo de  es un toro. Existe un uso independiente en la criptografía basada en toros.

También se tiene un problema si , el mayor divisor primo del orden del jacobiano, es igual a la característica de  Mediante una aplicación inyectiva diferente, se podría considerar el PLD en el grupo aditivo  en lugar del PLD en el jacobiano. Sin embargo, el PLD en este grupo aditivo es trivial de resolver, como se puede comprobar fácilmente. Por lo tanto, estas curvas, llamadas curvas anómalas, tampoco deben utilizarse en el PLD.

 Orden del jacobiano
Por lo tanto, para elegir una buena curva y un buen cuerpo finito subyacente, es importante conocer el orden del jacobiano. Considérese una curva hiperelíptica  de género  sobre el cuerpo , donde  es una potencia de un número primo, y defínase  como , pero ahora sobre el cuerpo . Se puede demostrar que el orden del jacobiano de  se encuentra en el intervalo , llamado intervalo de Hasse-Weil.

Pero hay más, se puede calcular el orden usando la función zeta en curvas hiperelípticas. Sea  el número de puntos en . Entonces, se define la función zeta de  como . Para esta función zeta se puede demostrar que  donde  es un polinomio de grado  con coeficientes en . Además,  se factoriza como  donde  para todo . Aquí  denota el conjugado complejo de . Finalmente, se tiene que el orden de  es igual a . Por lo tanto, los órdenes de los jacobianos se pueden encontrar calculando las raíces de .

 Referencias

 Enlaces externos
 Colm Ó hÉigeartaigh Implementación de algunos algoritmos de curvas hiperelípticas usando MIRACL
 DJ Bernstein Surface1271: criptografía de curvas hiperelípticas de género 2 de alta velocidad – trabajo incompleto de 2006 que pretendía producir una variante de Diffie-Hellman, pero se estancó debido a dificultades para elegir superficies (a su vez, porque no se dispone de conteo de puntos para superficies grandes). Contiene software para la multiplicación escalar del Pentium M en una superficie de Kummer.
