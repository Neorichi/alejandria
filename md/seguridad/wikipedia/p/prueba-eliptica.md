---
type: Artículo de enciclopedia
title: Prueba elíptica
description: La Criptografía de Curva Elíptica (CCE) es una variante de la criptografía asimétrica o de clave pública basada en las matemáticas de las curvas elípticas.
resource: https://es.wikipedia.org/wiki/Prueba_elíptica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Prueba_elíptica"}
license: CC BY-SA 4.0
id: eswiki-Prueba_elíptica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Prueba elíptica

La **Criptografía de Curva Elíptica (CCE)** es una variante de la criptografía asimétrica o de clave pública basada en las matemáticas de las curvas elípticas. Sus autores argumentan que la CCE puede ser más rápida y usar claves más cortas que los métodos antiguos — como RSA — al tiempo que proporcionan un nivel de seguridad equivalente. La utilización de curvas elípticas en criptografía fue propuesta de forma independiente por Neal Koblitz y Victor Miller en 1985.

Introducción

Los sistemas de criptografía asimétrica o de clave pública utiliza dos claves distintas: una de ellas puede ser pública, la otra es privada. La posesión de la clave pública no proporciona suficiente información para determinar cuál es la clave privada. Este tipo de sistemas se basan en la dificultad de encontrar la solución a ciertos problemas matemáticos. Uno de estos problemas es el llamado logaritmo discreto. Encontrar el valor de b dada la ecuación , cuando a y c son valores conocidos, puede ser un problema de complejidad exponencial para ciertos Grupos finitos de gran tamaño; mientras el problema inverso, la exponenciación discreta puede ser evaluado eficientemente usando por ejemplo exponenciación binaria

Una curva elíptica es una curva plana definida por una ecuación de la forma

.

Con el conjunto de puntos G que forman la curva (i.e., todas las soluciones de la ecuación más un punto O, llamado punto en el infinito) más una operación aditiva *+*, se forma un grupo abeliano. Si las coordenadas *x* e *y* se escogen desde un campo finito, entonces estamos en presencia de un grupo abeliano finito. El problema del logaritmo discreto sobre este conjunto de puntos (PLDCE) se cree que es más difícil de resolver que el correspondiente a los campos finitos (PLD). De esta manera, las longitudes de claves en criptografía de curva elíptica pueden ser más cortas con un nivel de seguridad comparable.

Introducción Matemática

Sea  primo. La curva elíptica E  sobre  es el conjunto de soluciones
 en la congruencia

,

donde  son constantes tal que

Se define una operación aditiva como sigue: Considerando que

y

son puntos en E y  es un punto en el infinito. Si  e , entonces ; de lo contrario , donde
,
,
y
.

Finalmente, definimos
.

Con esto se puede mostrar que *E* es un grupo abeliano con elemento identidad . Cabe notar que la inversa de (x, y) (que se escribe como -(x, y) ya que la operación es aditiva) es (x, -y), para todo

De acuerdo al teorema de Hasse, el número de puntos #E que contiene *E* es cercano a *p*. Más precisamente se satisface la siguiente desigualdad
.

Como se sabe que cualquier grupo de orden primo es cíclico, lo que se requiere es encontrar un subgrupo de *E* de orden q (q primo) para tener un isomorfismo con  donde el problema del logaritmo discreto sea intratable. En este caso, siendo  un generador del grupo cíclico (el cual puede ser cualquier elemento del grupo distinto de , la identidad), se pueden calcular las "potencias" de (las que se escriben como múltiplos de , debido a que la operación del grupo es aditiva).

Ejemplo

Sea E la curva elíptica  sobre . Se calculan los puntos sobre E verificando los posibles valores de , y luego verificando si  es un residuo cuadrático. Los valores se tabulan en la siguiente Tabla,

Como E tiene 13 puntos, sigue que es cíclico e isomorfo a . Considerando el generador , entonces :

Entonces tenemos

y

Por lo tanto

Uso en criptografía

En el uso criptográfico, se elige un punto base *G* específico y publicado para utilizar con la curva *E*(*q*). Se escoge un número entero aleatorio *k* como clave privada, y entonces el valor *P* = *k***G* se da a conocer como clave pública (nótese que la supuesta dificultad del PLDCE implica que *k* es difícil de deducir a partir de *P*). Si María y Pedro tienen las claves privadas *k**A* y *k**B*, y las claves públicas *P**A* y *P**B*, entonces María podría calcular *k**A***P**B* = (*k**A***k**B*)**G*; y Pedro puede obtener el mismo valor dado que *k**B***P**A* = (*k**B***k**A*)**G*.

Esto permite establecer un valor "secreto" que tanto María como Pedro pueden calcular fácilmente, pero que es muy complicado de derivar para una tercera persona. Además, Pedro no consigue averiguar nada nuevo sobre *k**A* durante ésta transacción, de forma que la clave de María sigue siendo privada.

Los métodos utilizados en la práctica para cifrar mensajes basándose en este valor secreto consisten en adaptaciones de antiguos criptosistemas de logaritmos discretos originalmente diseñados para ser usados en otros grupos. Entre ellos se podrían incluir Diffie-Hellman, ElGamal y DSA.

La realización de las operaciones necesarias para ejecutar este sistema es más lenta que para un sistema de factorización o de logaritmo discreto módulo entero del mismo tamaño. De todas maneras, los autores de sistemas de CCE creen que el PLDCE es significativamente más complicado que los problemas de factorización o del PLD, y así se puede obtener la misma seguridad mediante longitudes de clave mucho más cortas utilizando CCE, hasta el punto de que puede resultar más rápido que, por ejemplo, RSA. Los resultados publicados hasta la fecha tienden a confirmar esto, aunque algunos expertos se mantienen escépticos.

La CCE ha sido ampliamente reconocida como el algoritmo más fuerte para una determinada longitud de clave, por lo que podría resultar útil sobre enlaces que tengan requisitos muy limitados de ancho de banda.

NIST y ANSI X9 han establecido unos requisitos mínimos de tamaño de clave de 1024 bits para RSA y DSA y de 160 bits para ECC, correspondientes a un bloque simétrico de clave de 80 bits. NIST ha publicado una lista de curvas elípticas recomendadas de 5 tamaños distintos de claves (80, 112, 128, 192, 256). En general, la CCE sobre un grupo binario requiere una clave asimétrica del doble de tamaño que el correspondiente a una clave simétrica.

Certicom es la principal empresa comercial de CCE, esta organización posee 130 patentes, y ha otorgado licencias sobre tecnología a la National Security Agency (NSA) por 25 millones de dólares. Certicom también ha patrocinado varios desafíos al algoritmo CCE. El más complejo resuelto hasta ahora, es una clave de 109 bits, que fue roto por un equipo de investigadores a principios de 2003. El equipo que rompió la clave utilizó un ataque masivo en paralelo basado en el 'birthday attack', mediante más de 10000 PC's de tipo Pentium funcionando continuamente durante 540 días. Se estima que la longitud de clave mínima recomendada para CCE (163 bits) requeriría 108 veces los recursos utilizados para resolver el problema con 109 bits.

Referencias
 Neal Koblitz, "Elliptic curve cryptosystems", *Mathematics of Computation* 48, 1987, pp203–209.
 V. Miller, "Use of elliptic curves in cryptography", CRYPTO 85, 1985.
 Blake, Seroussi, Smart, "Elliptic Curves in Cryptography", Cambridge University Press, 1999
 Hankerson, Menezes, Vanstone: "Guide to Elliptic Curve Cryptography", Springer-Verlag, 2004

 Enlaces externos
 Recommended Elliptic Curves for Government Use, NIST document (PDF file)
 Certicom press release regarding 109 bit ECC challenge
 Certicom Online ECC Tutorial
 Digital Signature Standard; includes info on ECDSA
 libecc: Open source ECC library
 Demo of elliptic curve point counting and domain parameter generation
 eccGnuPG: Parche experimental para el GnuPG
