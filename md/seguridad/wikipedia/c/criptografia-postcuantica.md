---
type: Artículo de enciclopedia
title: Criptografía postcuántica
description: "La criptografía postcuántica (PQC del inglés Post-Quantum Cryptography), también llamada Criptografía resistente a la computación cuántica, se refiere a algoritmos criptográficos que sean resistentes a ataques …"
resource: https://es.wikipedia.org/wiki/Criptografía_postcuántica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_postcuántica"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_postcuántica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía postcuántica

La **criptografía postcuántica** (**PQC** del inglés *Post-Quantum Cryptography*), también llamada **Criptografía resistente a la computación cuántica**, se refiere a algoritmos criptográficos que sean resistentes a ataques efectuados mediante computación cuántica. A este tipo de criptografía no pertenecen los algoritmos de clave pública más populares, que pueden ser superados por un ordenador cuántico suficientemente potente haciendo uso del algoritmo de Shor. Aunque los actuales ordenadores cuánticos experimentales no son aún capaces de atacar cualquier algoritmo criptográfico real, muchos criptógrafos están diseñando algoritmos resistentes para adelantarse a la amenaza. Este trabajo ha captado gran atención por parte de  académicos y la industria a raíz de la serie de conferencias PQCrypto desde 2006 y más recientemente por varios Talleres del European Telecommunications Standards Institute (ETSI) sobre Criptografía Segura Cuántica.

En contraste a la amenaza que supone la computación cuántica para los actuales algoritmos de clave pública o asimétrica, la mayoría de los actuales algoritmos criptográficos simétricos (criptografía simétrica y funciones hash criptográficas) se consideran relativamente seguros ante ataques por ordenadores cuánticos. Mientras que el algoritmo cuántico de Grover acelera la capacidad de los ataques contra la criptografía simétrica, duplicar el tamaño de la clave empleada en los mismos puede impedir estos ataques. Por ello la criptografía simétrica postcuántica no difiere significativamente de la actual criptografía simétrica.

La criptografía postcuántica es diferente a la criptografía cuántica, que consiste en utilizar fenómenos cuánticos para lograr el secreto y detectar el espionaje.

 Familias de algoritmos
A continuación, se muestran las familias de algoritmos más prometedoras para proporcionar seguridad postcuántica:
Criptografía basada en código (CBC del inglés *Code-Based Cryptography*). Se basa en el uso de códigos de corrección de errores para diseñar esquemas de cifrado asimétrico. Propuesto por primera vez por Robert McEliece en 1978. Ejemplos de algoritmos de este tipo son el criptosistema de McEliece y el esquema de Niederreiter. El principal problema del sistema original es el gran tamaño de la clave pública, la cual puede superar el megabyte.
Criptografía basada en hash (HBC del inglés *Hash-Based Cryptography*). Se basa en el uso de funciones hash para crear criptografía de clave pública. Las funciones hash ya son una de las herramientas criptográficas más utilizadas. Este tipo criptografía basada en hash es flexible y puede cumplir con diferentes expectativas de rendimiento. En el lado negativo, los esquemas de firma basados en hash son principalmente con estado, lo que significa que la clave privada debe actualizarse después de cada uso; de lo contrario, la seguridad no está garantizada. Hay esquemas basados en hash que no tienen estado, pero tienen el costo de firmas más largas, tiempos de procesamiento más significativos y la necesidad del firmante de realizar un seguimiento de cierta información, como cuántas veces se usó una clave para crear una firma.
Criptografía basada en retículos (LBC del inglés *Lattice based cryptography*). Los retículos se definen como un conjunto de puntos que se distribuyen de forma regular en un plano n-dimensional infinito. Es un caso particular de la criptografía basada en problemas de suma de subconjuntos. Introducida por primera vez en 1996 por Miklós Ajtai. Tienen algunas características atractivas, como la dificultad de dureza en el peor de los casos. Además, presentan simplicidad y paralelismo y son lo suficientemente versátiles como para construir esquemas criptográficos robustos. Finalmente, son la única familia de algoritmos que contiene los tres tipos de primitivas requeridas para construir una infraestructura de clave pública post-cuántica: cifrado de clave pública, intercambio de claves y firma digital.
Criptografía basada en funciones polinomiales multivariables (MVC del inglés *Multivariate-Based Cryptography*) o Criptografía multivariante. El término multivariable hace referencia a que los polinomios que se utilizan tienen más de una variable. Es la criptografía de clave pública cuyas claves públicas representan un mapa polinomial multivariado y no lineal (generalmente cuadrático). Se ha demostrado que la resolución de estos sistemas es NP-completa, lo que convierte a esta familia de algoritmos en buenos candidatos para la criptografía post-cuántica. Actualmente, este tipo de esquemas de cifrado son menos eficientes que otros esquemas, ya que requieren claves públicas largas y tiempos de descifrado prolongados. Por otro lado, resultaron ser más adecuados para construir esquemas de firmas, ya que proporcionan los tamaños de firma más cortos entre los algoritmos post-cuánticos, aunque incurren en claves públicas bastante grandes.
Criptografía basada en isogenia (IBC del inglés *Isogeny-Based Cryptography*). Este tipo de criptografía utiliza mapas entre curvas elípticas para construir criptografía de clave pública. Ejemplo de algoritmos de este tipo es el protocolo de intercambio de claves Supersingular isogeny Diffie-Hellman (SIDH) introducido en 2011. SIDH requiere una de las claves más pequeñas entre los esquemas de intercambio de claves propuestos y admite el secreto directo perfecto. Sin embargo, su edad relativamente joven significa que no existen muchos esquemas basados en este concepto, y no ha habido mucho para inspeccionar sus posibles vulnerabilidades.
Criptografía basada en grupo de trenzas. Estableciendo como base algunos problemas basados en grupo de trenzas es posible construir funciones de un solo sentido y esquemas de intercambio de claves.

 Búsqueda de estándares
La iniciativa de búsqueda de estándares poscuánticos más importante es la del NIST (Proceso de estandarización de criptografía postcuántica del NIST). Hay búsqueda en dos categorías: para firma digital y para cifrado e intercambio de claves (PKE/KEM). Actualmente está en la fase final y hay seleccionados 7 finalista (4 para PKE/KEM y 3 para firma digital). De los 4 finalistas de PKE, 3 son basados en retículos y 1 está basado en código. De los 3 finalistas de firma digital, 2 están basados en retículos y 1 en esquemas multivariable.

Hay otros organismos y comités de estándares que también buscan estándares poscuánticos, la mayoría de los cuales hacen su trabajo en coordinación con el concurso del NIST. Por ejemplo, entre los organismos sectoriales está el ISO, ITU-T SC 17, IETF y X9 (Financial Industry Standards). A nivel europeo está el ETSI y ENISA.

China ha lanzado su propio concurso abierto para la elección de los estándares post-cuánticos, a través de la Chinese Association for Cryptographic Research (CACR) a la que se han presentado 38 candidatos.

 Esquemas híbridos

En el contexto de la criptografía postcuántica, un esquema híbrido es un esquema criptográfico en el que se combina un esquema de clave pública precuántica (ej. RSA o (EC)DH), con un esquema postcuántico de forma que garantice la seguridad al menos tanto como el mínimo de la seguridad que aporta uno de los esquemas. En lugar de confiar solo en un algoritmo postcuántico, poco probado, nos aseguramos al menos la seguridad del algoritmo precuántico. Por esta razón estos algoritmos son interesantes como una forma de transición a los algoritmos postcuánticos. El algoritmo post-cuántico protegería frente a los futuros computadores cuánticos mientras que los precuánticos o actuales seguirían protegiendo la comunicación si avanza el criptoanálisis de los algoritmos post-cuánticos.

Por ejemplo, podemos combinar dos esquemas de cifrado de clave pública (PKE) o dos esquemas de intercambio de claves (KEX) ejecutando los dos esquemas y haciendo xor de la clave de secreta de ambos esquemas para obtener una clave secreta combinada.

Para protocolos que derivan una clave de sesión a partir de un presecreto maestro, obtenida vía criptografía de clave pública, introducido en una función de derivación de clave (KDF), también es posible establecer el secreto premaestro por cada uno de los esquemas y alimentar la función de derivación de clave con la concatenación de los dos secretos premaestros. Por ejemplo, esto podría ser aplicable a TLS.

Para combinar dos esquemas de firma digital los mejor suele ser usarlos de forma independiente. Esto es, distribuir dos claves públicas (posiblemente en un solo certificado) y siempre enviar dos firmas, una por esquema. Para algunos esquemas específicos se está investigando si se podría usar una combinación de ambos esquemas.

 Referencias
