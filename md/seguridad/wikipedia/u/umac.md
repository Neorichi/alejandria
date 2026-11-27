---
type: Artículo de enciclopedia
title: UMAC
description: "En criptografía, un código de autenticación de mensajes basado en hashing universal o UMAC es un tipo de código de autenticación de mensajes (MAC) que se calcula eligiendo una función de hash de una clase de funciones …"
resource: https://es.wikipedia.org/wiki/UMAC
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/UMAC"}
license: CC BY-SA 4.0
id: eswiki-UMAC
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# UMAC

En criptografía, un **código de autenticación de mensajes basado en hashing universal** o **UMAC** es un tipo de código de autenticación de mensajes (MAC) que se calcula eligiendo una función de hash de una clase de funciones de hash de acuerdo a algún proceso secreto (aleatorio) y aplicándosela al mensaje. El resumen resultante o *fingerprint* se cifra para ocultar la identidad de la función de hash usada. Como con cualquier código MAC, puede usarse para verificar simultáneamente tanto la integridad de los datos como la autenticidad del mensaje. Un UMAC tiene fuerza criptográfica demostrable y comúnmente es bastante menos computacionalmente intensiva que otras MACs. A diferencia de los MAC tradicionales, que son serializables, UMAC se puede ejecutar en paralelo. Por lo tanto, a medida que las máquinas continúen ofreciendo más capacidades de procesamiento paralelo, la velocidad de implementación de UMAC aumentará.

 Hashing universal
Digamos que la función de hash se elige de una clase de funciones de hash H, que mapea mensajes en D, el conjunto de posibles resúmenes de mensaje. A este conjunto se lo llama universal si, para cada par distinto de mensajes, hay como máximo |H|/|D| funciones que las mapean al mismo miembro de D.

Esto significa que si un atacante quiere reemplazar un mensaje con otro y, desde su punto de vista, la función de hash se eligió completamente al azar, la probabilidad de que el UMAC no detecte su modificación es de a lo sumo 1/|D|.

Esta definición, sin embargo, no es lo suficientemente fuerte. Si los mensajes posibles son 0 y 1, D={0,1}, y H consiste de la operación identidad y la negación, entonces H es universal. Por otro lado, si el resumen del mensaje se cifra mediante adición modular, el atacante puede cambiar el mensaje y el resumen al mismo tiempo, sin que el receptor se entere.

 Hashing universal fuerte
Una clase de funciones de hash H que sea buena para usar hará difícil la tarea de un atacante de adivinar el resumen correcto *d* de un mensaje falso *f* luego de interceptar un mensaje *a* con un resumen *c*. En otras palabras

debe ser muy pequeño, preferentemente 1/|D|.

Es fácil construir una clase de funciones de hash cuando D es un campo finito. Por ejemplo, si |D| es primo, todas las operaciones se toman módulo |D|. El mensaje *a* se codifica como un vector n-dimensional sobre D (a1,a2,..,an). Luego, H tiene |D|n+1 miembros, cada cual correspondiendo a un vector n+1-dimensional sobre D (h0,h1,..,hn). Si definimos

podemos usar las reglas de probabilidad y combinatoria para demostrar que

Si ciframos apropiadamente todos los resúmenes (por ejemplo mediante one-time pad), un atacante no podrá obtener nada de ellos y la misma función de hash podrá usarse para todas las comunicaciones entre las dos partes. Esto puede no ser verdad para cifrado ECB, porque puede ser bastante probable que dos mensajes produzcan el mismo valor de hash. Entonces, debería usarse algún tipo de vector de inicialización, conocido comúnmente como nonce. Es práctica habitual elegir h0=f(nonce), donde f también es secreta.

Nótese que teniendo cantidades masivas de poder de cómputo no ayuda para nada al atacante. Si el receptor limita la cantidad de falsificaciones que acepta (esperando un tiempo inactivo cuando detecta alguna), |D| puede ser 232 o menor.

Referencias

 UMAC ha sido aprobada por la IETF como una RFC de información. Es rápido y basado en  el AES.

Véase también
 Poly1305-AES, otro MAC veloz, basado en hashing universal fuerte y en AES.
