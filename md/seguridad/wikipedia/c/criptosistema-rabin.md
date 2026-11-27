---
type: Artículo de enciclopedia
title: Criptosistema Rabin
description: El criptosistema de Rabin es una técnica criptográfica asimétrica cuya seguridad, al igual que RSA, se basa en la complejidad de la factorización.
resource: https://es.wikipedia.org/wiki/Criptosistema_Rabin
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptosistema_Rabin"}
license: CC BY-SA 4.0
id: eswiki-Criptosistema_Rabin
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptosistema Rabin

El **criptosistema de Rabin** es una técnica criptográfica asimétrica cuya seguridad, al igual que RSA, se basa en la complejidad de la factorización. Sin embargo, la ventaja del criptosistema de Rabin es que se ha demostrado que la complejidad del problema en el que se basa es tan duro como la factorización de enteros, cosa que se desconoce si es cierto en el caso del RSA simple. El inconveniente que tiene es que cada salida de la función de Rabin puede ser generado por 4 posibles entradas, y si cada salida es un texto cifrado se requiere un tiempo extra en el descifrado para identificar cual de las 4 posibles entradas era el correcto texto en claro. El algoritmo se publicó en enero de 1979 por Michael O. Rabin.

 Descripción del Criptosistema RSA Versión de Rabin

Antes de explicar el criptosistema de Rabin sería conveniente aclarar el concepto de raíces en operaciones modulares. Se dice que la raíz de un número es aquel que multiplicado por sí mismo, da ese número. Pues bien, en Aritmética modular, esto sigue siendo así. Pero claro, un número al cuadrado en módulo n puede ser que sea mayor que ese n, por lo que al hacer módulo, se reduce su valor. Por lo tanto, un mismo número puede tener varias raíces. En el álgebra habitual, un número tiene 2 raíces reales (la positiva y la negativa), pero cuando n es el producto de 2 primos, existen valores que tienen 4 raíces distintas. De hecho, lo normal es que tengan 4 raíces. Y tendrán 4 raíces todos los número que no tengan como divisor a uno de los dos primos con los que se generó n, en cuyo caso tendrán sólo 2.

Si se realizan cálculos se observará que existen del orden de  valores con 2 raíces y del orden de  valores con 4 raíces distintas.

Dicho esto, centrémonos ahora en el criptosistema de Rabin: el criptosistema de Rabin es una buena alternativa al criptosistema RSA, aunque al igual que RSA, basa su seguridad en la dificultad de factorizar. El criptosistema de Rabin funciona de la siguiente manera:

Cada usuario elige una pareja de primos  y cada uno igual a 3 módulo 4 y forma el producto  .
La clave pública será  y la clave privada  y
Función de cifrado:
Función de descifrado: Dado un texto cifrado c, se calculan las 4 raíces cuadradas de c mod n. Una de ellas será el propio m, otra es n-m y las otras son sus negativas. Para hallar m deberá hacerse a partir de las otras 3 raíces.
Si, como se dijo antes, los primos p y q son iguales a 3 módulo 4 existen fórmulas sencillas para hallar las raíces, calculando previamente mediante el TCR los valores para  y  que satisfacen la ecuación:

Las 4 raíces serán m1=x, m2=-x, m3=y  y  m4=-y

Para distinguir el m que codifica el mensaje de las otras raíces (los otros m), será necesario incluir información redundante.

 Detalles del Criptosistema RSA Versión de Rabin

Para distinguir el m que codifica el mensaje de las otras raíces (los otros m), será necesario incluir información redundante.

Es interesante el hecho de que para el caso en que un primo p sea congruente a 1 módulo 4 no se conoce ningún algoritmo polinomial determinista para hallar las raíces cuadradas de residuos cuadráticos módulo p.

Por tanto, el hecho que p = 3 mod 4   y   q = 3 mod 4 es vital para el correcto funcionamiento del algoritmo de descripción, ya que existen las fórmulas antes expuestas.

Un atacante no sabría cual de las cuatro raíces es la correcta, pero el receptor tampoco. Esto se resuelve acordando ciertas reglas de redundancia en el mensaje para poder distinguir cual de las cuatro raíces corresponde al mensaje original.
