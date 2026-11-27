---
type: Artículo de enciclopedia
title: Vector de inicialización
description: "En criptografía, un vector de inicialización (conocido por sus siglas en inglés IV) es un bloque de bits que es requerido para permitir un cifrado en flujo o un cifrado por bloques, en uno de los modos de cifrado, con …"
resource: https://es.wikipedia.org/wiki/Vector_de_inicialización
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Vector_de_inicialización"}
license: CC BY-SA 4.0
id: eswiki-Vector_de_inicialización
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Vector de inicialización

En criptografía, un **vector de inicialización** (conocido por sus siglas en inglés **IV**) es un bloque de bits que es requerido para permitir un cifrado en flujo o un cifrado por bloques, en uno de los modos de cifrado, con un resultado independiente de otros cifrados producidos por la misma clave. El tamaño del IV dependen del algoritmo de cifrado y del protocolo criptográfico y a menudo es tan largo como el tamaño de bloque o como el tamaño de la clave.

Los vectores de inicialización son implementados en cifrados por bloques y cifrados en flujo. Por ejemplo, el modo *Electronic Code Book* (ECB), el cifrado del mismo texto con la misma clave da como resultado el mismo texto cifrado, lo cual es una considerable vulnerabilidad. El uso de un vector de inicialización añadido linealmente (mediante una operación XOR) o incluido delante del texto plano antes del cifrado resuelve este problema.

El tamaño del IV depende de la primitiva criptográfica utilizada; para los cifrados de bloques, generalmente es el tamaño del bloque del cifrado. En los esquemas de cifrado, la parte impredecible del IV tiene, en el mejor de los casos, el mismo tamaño que la clave para compensar los ataques de compensación de tiempo/memoria/datos. Cuando el IV se elige aleatoriamente, debe tenerse en cuenta la probabilidad de colisiones debido al problema del cumpleaños. Los cifrados de flujo tradicionales, como RC4, no admiten un IV explícito como entrada, y se necesita una solución personalizada para incorporar un IV en la clave o el estado interno del cifrado. Se sabe que algunos diseños implementados en la práctica son inseguros; el protocolo WEP es un ejemplo notable y es propenso a ataques de IV relacionados.

 Referencias

 Bibliografía
 Schneier, B. *Applied Cryptography*, Wiley 1996
