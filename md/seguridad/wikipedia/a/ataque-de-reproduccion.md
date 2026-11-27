---
type: Artículo de enciclopedia
title: Ataque de reproducción
description: "Un ataque de replay, también llamado ataque de playback, en español ataque de reproducción o ataque de reinyección, es una forma de ataque de red, en la cual una transmisión de datos válida es maliciosa o …"
resource: https://es.wikipedia.org/wiki/Ataque_de_reproducción
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_de_reproducción"}
license: CC BY-SA 4.0
id: eswiki-Ataque_de_reproducción
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque de reproducción

Un **ataque de *replay***, también llamado **ataque de *playback***, en español **ataque de reproducción** o **ataque de reinyección**, es una forma de ataque de red, en la cual una transmisión de datos válida es maliciosa o fraudulentamente repetida. Es llevada a cabo por el autor o por un adversario que intercepta la información y la retransmite, posiblemente como parte de un ataque enmascarado.

Aplicación
Suplantación de identidad
Es habitual hacer un ataque de *replay* capturando información y posteriormente reenviándola con el objetivo de suplantar la identidad de uno de los lados.
Es un hecho muy conocido que el intercambio de claves Diffie-Hellman en sus primeras versiones podía ser atacado por un ataque de reinyección, sin embargo, esto puede evitarse con una marca secuencial o una marca de tiempo. Actualmente, ninguna aplicación que use el esquema de intercambio de claves Diffie-Hellman de manera adecuada se ve afectada por este ataque en su forma básica (aunque cabría falsificar dicha marca o duplicarla en el ataque *replay*).

Denegación de servicio
Es habitual en sistemas de encaminamiento, por ejemplo en encaminamiento de cebolla, realizar ataques de *replay* capturando mensajes y luego reinyectándolos en la red con el objetivo de sobrecargarla y que deje de funcionar (ataque de denegación de servicio). Para evitar este tipo de ataques es habitual que los routers detecten cuando un paquete ya ha sido procesado (y por tanto descarten ese paquete) y que los propios mensajes tengan un tiempo de validez que una vez agotado permita que los routers eliminen esos mensajes.

 Véase también
 Ataque Man-in-the-middle
 Escucha telefónica

 Referencias
