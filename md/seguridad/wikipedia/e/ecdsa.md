---
type: Artículo de enciclopedia
title: ECDSA
description: "ECDSA (Elliptic Curve Digital Signature Algorithm, en español: Algoritmo de Firma Digital de Curva Elíptica) es un algoritmo de firma digital basado en criptografía de curva elíptica."
resource: https://es.wikipedia.org/wiki/ECDSA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/ECDSA"}
license: CC BY-SA 4.0
id: eswiki-ECDSA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# ECDSA

**ECDSA** (*Elliptic Curve Digital Signature Algorithm*, en español: **Algoritmo de Firma Digital de Curva Elíptica**) es un algoritmo de firma digital basado en criptografía de curva elíptica. Constituye una variante del algoritmo DSA que emplea operaciones sobre puntos de curvas elípticas en lugar de las exponenciaciones modulares utilizadas por DSA, basadas en el problema del logaritmo discreto en grupos multiplicativos.

La seguridad de ECDSA se fundamenta en la dificultad computacional del problema del logaritmo discreto sobre curvas elípticas (*Elliptic Curve Discrete Logarithm Problem*, ECDLP). La principal ventaja de este esquema es que requiere números de tamaños significativamente menores para brindar el mismo nivel de seguridad que DSA o RSA, lo que se traduce en una mayor eficiencia en términos de almacenamiento, ancho de banda y tiempo de cómputo.

Existen dos tipos principales de curvas elípticas según el campo finito sobre el cual se definan: curvas sobre campos primos GF(p) y curvas sobre campos binarios GF(2m). En la práctica, los estándares modernos favorecen el uso de curvas sobre campos primos debido a su mejor interoperabilidad y a consideraciones de seguridad e implementación.

 Historia
La criptografía de curva elíptica fue propuesta de manera independiente por Neal Koblitz y Victor S. Miller en 1985 como una alternativa a los sistemas criptográficos basados en exponenciación modular. A partir de estas ideas, se desarrollaron esquemas de firma digital basados en curvas elípticas durante la década de 1990.

ECDSA fue estandarizado formalmente por el National Institute of Standards and Technology (NIST) en el estándar FIPS 186 y por Certicom en las especificaciones SEC. Desde entonces, ha sido adoptado ampliamente en estándares internacionales, protocolos de seguridad y aplicaciones comerciales.

 Proceso de firma y verificación

 Generación de llaves
 Seleccione una curva elíptica *E* definida sobre un campo finito.
 Seleccione un punto base *P* perteneciente a *E* de orden primo *n*.
 Seleccione aleatoriamente un número entero *d* en el intervalo [1, *n − 1*].
 Calcule *Q = dP* mediante multiplicación escalar.
 El valor *d* constituye la llave privada.
 El punto *Q* constituye la llave pública.

 Proceso de firma
 Seleccione un número entero aleatorio *k* en el intervalo [1, *n − 1*].
 Calcule *kP = (x1, y1)*.
 Calcule *r = x1 mod n*; si *r = 0*, regrese al primer paso.
 Calcule el inverso modular *k−1 mod n*.
 Calcule *s = k−1(H(m) + dr) mod n*; si *s = 0*, regrese al primer paso.
 La firma del mensaje *m* está compuesta por el par ordenado (*r*, *s*).

 Proceso de verificación
 Verifique que *r* y *s* pertenezcan al intervalo [1, *n − 1*].
 Calcule *w = s−1 mod n*.
 Calcule *u1 = H(m)w mod n*.
 Calcule *u2 = rw mod n*.
 Calcule el punto *(x0, y0) = u1P + u2Q*.
 Calcule *v = x0 mod n*.
 La firma es válida si y solo si *v = r*.

 Comparación con otros algoritmos
 ECDSA y DSA
ECDSA y DSA se basan en el problema del logaritmo discreto y comparten una estructura matemática similar. Sin embargo, DSA opera sobre grupos multiplicativos de enteros módulo un primo grande, mientras que ECDSA utiliza grupos de puntos sobre curvas elípticas, permitiendo tamaños de clave mucho menores para un nivel de seguridad equivalente.

 ECDSA y RSA
A diferencia de RSA, cuya seguridad se basa en la dificultad de la factorización de números enteros grandes, ECDSA se fundamenta en el ECDLP. Para niveles de seguridad comparables, ECDSA suele ofrecer un mejor rendimiento computacional y menor consumo de recursos, especialmente en sistemas con restricciones de memoria o potencia de cálculo.

 Usos
ECDSA es ampliamente utilizado en sistemas y protocolos de seguridad modernos, entre los que se incluyen:

 Protocolos de comunicación segura como TLS y SSL
 Autenticación y cifrado en SSH
 Infraestructuras de clave pública (PKI)
 Sistemas operativos y dispositivos móviles
 Tecnologías de cadena de bloques y criptomonedas como Bitcoin, donde se emplea ECDSA para autorizar transacciones y demostrar la posesión de claves privadas

 Referencias

 Enlaces externos
 Digital Signature Standard (DSS); incluye información sobre ECDSA (en inglés)
 SEC 1: Elliptic Curve Cryptography (en inglés)
