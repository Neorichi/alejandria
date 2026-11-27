---
type: Artículo de enciclopedia
title: Perfect forward secrecy
description: "El término secreto perfecto hacia adelante (en inglés perfect forward secrecy, PFS) es la propiedad de los sistemas criptográficos que garantiza que el descubrimiento de las claves utilizadas actualmente no compromete …"
resource: https://es.wikipedia.org/wiki/Perfect_forward_secrecy
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Perfect_forward_secrecy"}
license: CC BY-SA 4.0
id: eswiki-Perfect_forward_secrecy
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Perfect forward secrecy

El término **secreto perfecto hacia adelante** (en inglés ***perfect forward secrecy***, PFS) es la propiedad de los sistemas criptográficos que garantiza que el descubrimiento de las claves utilizadas actualmente no compromete la seguridad de las claves usadas con anterioridad (no las revela). Por tanto la seguridad de lo que se hizo usando claves antiguas persiste. Cuando un sistema tiene secreto perfecto hacia adelante se dice que el sistema es seguro hacia adelante.

Poco a poco nos estamos concienciando de que el entorno en el que nos movemos no es seguro. Por ejemplo, las comunicaciones en línea pueden ser observadas en su camino hacia el destino, los datos que residen en nuestros equipos son vulnerables a múltiples tipos de ataques. Esto nos lleva a que intentemos acotar el impacto que puede tener un ataque a la seguridad de las claves. Perseguimos que la vulneración de las claves en el presente no afecte a la seguridad de lo que hicimos en el pasado con esas claves.

 Controversia
*Forward secrecy* se usa normalmente como sinónimo de *perfect forward secrecy*. Sin embargo ha habido controversia sobre ello. Al menos en una referencia se distingue entre *perfect forward secrecy* y *forward secrecy*. Al concepto de *perfect forward secrecy* le añade la propiedad adicional de que la seguridad de la clave no será comprometida incluso si se han comprometido claves derivadas a partir del mismo 'material clave' en una ejecución siguiente.

 Objetivo
Muchos criptosistemas confían su seguridad a la posesión de un secreto al que normalmente se le llama clave secreta. En la aplicación práctica de estos criptosistemas al mundo real nos lleva frecuentemente a entornos en los que no hay seguridad absoluta y por tanto la clave secreta se ve expuesta a ataques que pueden comprometer su secreto. En estos entornos es muy importante limitar el daño causado por la posible exposición de claves secretas. Por eso en estos sistemas las claves secretas se va actualizando de forma regular. En estos sistemas la actualización de la clave secreta tiene que ser de tal forma que la exposición de una clave secreta correspondiente a un periodo de tiempo dado no permita a un adversario 'romper' el esquema para periodos de tiempo anteriores. Esto es lo que se modeliza con el concepto de *forward secrecy*. Resumiendo, el objetivo de los sistemas que cumplen esta propiedad es que si una clave es comprometida, en ningún caso se compromete la seguridad de los datos protegidos con claves anteriores (claves válidas en periodos anteriores de tiempo).

No hay que confundir los sistemas con seguridad hacia adelante con los sistemas de clave aislada que buscan minimizar el daño causado por un ataque actualizando la clave cada cierto tiempo. Pero para actualizar la clave interactúan con un dispositivo físicamente protegido, el cual mantiene una clave secreta maestra que se mantiene fija en todos los periodos.

 Implicaciones
Para que pueda haber secreto perfecto hacia adelante, la clave usada para proteger la transmisión de datos no se puede usar para derivar ninguna otra clave adicional, lo cual implica que si una clave usada para proteger la transmisión de datos fue derivada de cierto 'material clave', entonces ese material no puede ser usado para derivar ninguna otra clave más'''.

 Ámbitos de uso
El concepto de *perfect forward secrecy* fue introducido por Whitfield Diffie, Paul van Oorschot y Michael J. Wiener para describir la propiedad de un tipo de esquemas de establecimiento de claves en la que para conseguir el secreto a largo plazo usa claves privadas. Desde entonces esta propiedad ha sido ampliamente usada en distintos campos:
 Para describir la propiedad establecimiento de claves donde el secreto a largo plazo se basa en el uso de contraseñas compartidas (*password-authenticated key agreement*).
 En el campo de la firma digital (firma segura adelante) y del cifrado de clave pública (cifrado de clave pública seguro adelante).
 En las redes que persiguen el anonimato se busca que cumplan esta propiedad para que el tráfico del pasado no pueda ser traceado y descubrir el emisor y el destinatario aunque se rompa la seguridad de las claves. Por ejemplo la red Tor tiene esta propiedad.
 En protocolos de mensajería instantánea. Por ejemplo el protocolo *Off-the Record Messaging* tiene esta propiedad.

 Véase también
 Intercambio Diffie-Hellman
 Hiper-cifrado

 Referencias

 Enlaces externos
 H. Orman. The OAKLEY Key Determination Protocol. IETF RFC 2412.
 Gene Itkis,"Forward Security. Adaptive Cryptography: Time Evolution ".
 Desplegando forward secrecy, SSL Labs, en inglés, 25 de junio de 2013.
