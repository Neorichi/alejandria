---
type: Artículo de enciclopedia
title: Curva de Montgomery
description: En matemáticas, la curva de Montgomery es una forma de curva elíptica introducida por Peter L.
resource: https://es.wikipedia.org/wiki/Curva_de_Montgomery
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Curva_de_Montgomery"}
license: CC BY-SA 4.0
id: eswiki-Curva_de_Montgomery
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Curva de Montgomery

En matemáticas, la **curva de Montgomery** es una forma de curva elíptica introducida por Peter L. Montgomery en 1987, diferente de la curva cúbica plana usual. Se utiliza para ciertos cálculos, y en particular en diversas aplicaciones de criptografía.

 Definición
Una curva de Montgomery sobre un cuerpo  se define por la ecuación

para  tal que .

Generalmente, esta curva se considera sobre un cuerpo finito *K* (por ejemplo, sobre un cuerpo finito de  element, ) con characteristic distinto de 2 y con  y . Sobre dichos cuerpos, el orden de grupo de la curva siempre es divisible por 4. Las curvas de Montgomery también se consideran sobre rationals con las mismas restricciones para  y .

Toda curva de Montgomery tiene un punto en .

 Aritmética de Montgomery
Es posible realizar algunas *operaciones* entre los puntos de una curva elíptica: *sumar* dos puntos  consiste en encontrar un tercer punto  tal que ; *duplicar* un punto consiste en calcular  (para más información sobre operaciones, véase curva elíptica y más abajo).

Un punto  en la curva elíptica en forma de Montgomery  puede representarse en coordenadas de Montgomery , donde  son las coordenadas proyectivas y  para .

Nótese que este tipo de representación de un punto pierde información: de hecho, en este caso, no hay distinción entre puntos afines,  y  porque ambos están dados por el punto . Sin embargo, con esta representación es posible obtener múltiplos de puntos, es decir, dado , calcular .

Ahora bien, considerando los dos puntos  y : su suma viene dada por el punto  cuyos coordenadas son:

Si , la operación se convierte en una *duplicación*. Las coordenadas de  vienen dadas por las siguientes ecuaciones:

La primera operación considerada anteriormente (la adición) tiene un coste en tiempo de ejecución de 3*M*+2*S*, donde **M** denota la multiplicación entre dos elementos generales del cuerpo sobre el que se define la curva elíptica, mientras que **S** denota el cuadrado de un elemento general del cuerpo.

La segunda operación (duplicación) tiene un coste en tiempo de ejecución de 2*M* + 2*S* + 1*D*, donde **D** denota la multiplicación de un elemento general por una constante. Nótese que la constante es , por lo que se puede elegir  para obtener un **D** pequeño.

 Algoritmo y ejemplo
El siguiente algoritmo representa la duplicación de un punto  en una curva elíptica en forma de Montgomery.

Se asume que . El coste en tiempo de ejecución de esta operación es 1M + 2S + 1*A + 3add + 1*4. Aquí M denota las multiplicaciones requeridas, S indica las elevaciones al cuadrado y a se refiere a la multiplicación por A.

 Ejemplo
Sea  un punto en la curva .

En coordenadas , con  y .

Entonces:

El resultado es el punto  tal que .

 Adición
Dados dos puntos  y  en la curva de Montgomery  en coordenadas afines, el punto  representa, geométricamente, el tercer punto de intersección entre  y la recta que pasa por  y . Es posible hallar las coordenadas  de  de la siguiente manera:

1) Considérese una recta genérica  en el plano afín y hágase que pase por  y  (imponiendo la condición); de esta forma, se obtienen  y ;

2) Intersecando la recta con la curva , y sustituyendo la variable  en la ecuación de la curva por , se obtiene la siguiente ecuación de tercer grado:

Como se observó anteriormente, esta ecuación tiene tres soluciones que corresponden a las coordenadas  de ,  y . En particular, esta ecuación se puede reescribir como:

3) Comparando los coeficientes de las dos ecuaciones idénticas anteriores, en particular los coeficientes de los términos de segundo grado, se obtiene:

 .

Así,  se puede expresar en términos de , ,  y  como:

4) Para hallar la coordenada  del punto , basta con sustituir el valor  en la recta . Nótese que esto no proporciona directamente el punto . En efecto, con este método se hallan las coordenadas del punto  tal que , pero si se necesita el punto resultante de la suma entre  y , entonces es necesario observar que:  si y solo si . Así pues, dado el punto , es necesario hallar , lo cual se puede hacer fácilmente cambiando el signo de la coordenada  de . En otras palabras, será necesario cambiar el signo de la coordenada  obtenida al sustituir el valor  en la ecuación de la recta.

En resumen, las coordenadas de los puntos  y  son:

 Duplicación
Dado un punto  en la curva de Montgomery , el punto  representa geométricamente el tercer punto de intersección entre la curva y la recta tangente a . Por lo tanto, para hallar las coordenadas del punto  basta con seguir el mismo método de la fórmula de la suma. Sin embargo, en este caso, la recta *y* = *lx* + *m* debe ser tangente a la curva en , así que, si  con

entonces el valor de *l*, que representa la pendiente de la recta, viene dado por:

por el teorema de la función implícita.

Así pues,  y las coordenadas de los puntos ,  son:

 Equivalencia con las curvas de Edwards retorcidas
Sea  un cuerpo con característica distinta de 2.

Sea  una curva elíptica en forma de Montgomery:

con ,

Y sea  una curva elíptica en forma de Edwards retorcida:

con

El siguiente teorema muestra la relación de equivalencia birracional entre las curvas de Montgomery y la curva de Edwards retorcida:

Teorema (i) Toda curva de Edwards retorcida es birracionalmente equivalente a una curva de Montgomery sobre . En particular, la curva de Edwards retorcida  es birracionalmente equivalente a la curva de Montgomery , donde  y  son equivalentes.

La correspondencia:

es una equivalencia birracional de  a , con inversa:

 :

Nótese que esta equivalencia entre las dos curvas no es válida en todas partes: de hecho, la aplicación  no está definida en los puntos  ni  de .

 Equivalencia con las curvas de Weierstrass
Cualquier curva elíptica puede escribirse en forma de Weierstrass. En particular, la curva elíptica en la forma de Montgomery:

 :

puede transformarse de la siguiente manera: se divide cada término de la ecuación para  entre , y se sustituyen las variables *x* e *y* por  y , respectivamente, para obtener la ecuación:

Para obtener una forma corta de Weierstrass a partir de aquí, basta con reemplazar *u* por la variable :

Finalmente, esto da como resultado la ecuación:

Por lo tanto, la transformación se da como:

 :

En contraste, una curva elíptica sobre el cuerpo base  en la forma de Weierstrass

 :

se puede convertir a la forma de Montgomery si y solo si  satisface las siguientes condiciones:

  tiene al menos una raíz ; y
  es un residuo cuadrático en .

Cuando se cumplen estas condiciones, entonces para  se tiene la siguiente correspondencia:

 :

 .

 Véase también
 Curve25519
 , con información sobre el tiempo de ejecución requerido en cada caso específico

 Referencias

 Bibliografía

 Enlaces externos
Curvas de género 1 sobre cuerpos de gran característica
