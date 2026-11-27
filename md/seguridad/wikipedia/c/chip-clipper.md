---
type: Artículo de enciclopedia
title: Chip Clipper
description: "El Chip Clipper es un microprocesador desarrollado y comercializado por el gobierno de los Estados Unidos para ser usado como un dispositivo de cifrado por las compañías de telecomunicaciones dedicadas a la transmisión …"
resource: https://es.wikipedia.org/wiki/Chip_Clipper
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Chip_Clipper"}
license: CC BY-SA 4.0
id: eswiki-Chip_Clipper
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Chip Clipper

El **Chip Clipper** es un microprocesador desarrollado y comercializado por el gobierno de los Estados Unidos para ser usado como un dispositivo de cifrado por las compañías de telecomunicaciones dedicadas a la transmisión de voz. Fue anunciado el año 1993 y para el año 1996 era un producto completamente olvidado.
 Funcionamiento
El Chip Clipper usaba un algoritmo de cifrado de datos conocido como Skipjack para transmitir información y el algoritmo de Diffie-Hellman para distribuir llaves de criptográficas de sesión entre los usuarios del microprocesador. Skipjack fue inventado por la Agencia de Seguridad Nacional (NSA en inglés) del gobierno de los Estados Unidos. Originalmente este algoritmo era de carácter clasificado y por ende no podía ser sujeto a las revisiones usuales por las que pasa un algoritmo de cifrado al ser evaluado por la comunidad criptográfica mundial. En ese tiempo el gobierno de los EE. UU. sí reveló que el algoritmo usaba una llave de cifrado de 80-bits, que el algoritmo era simétrico (llave simétrica), y que era similar al entonces ya conocido algoritmo de cifrado DES. Skipjack fue desclasificado y publicado por la NSA el 24 de junio de 1998. En ese entonces, el costo inicial del microprocesador sería de US$16 (desprogramado) y US$26 (programado). La lógica del microprocesador sería creada por Mykotronx, y fabricado por VLSI Technology, Inc.

El corazón de todo el concepto en torno al Chip Clipper y su algoritmo Skipjack era el de la clave bajo custodia. En cualquier fábrica donde se produjese un dispositivo telefónico o cualquier aparato que fuese a usar el Chip Clipper se le asignaría una "llave criptográfica" que luego sería entregada al gobierno en "garantía". Si alguna agencia de gobierno estimaba que era "necesario" escuchar algún tipo de comunicación, la llave sería "desbloqueada" y entregada a la agencia de gobierno correspondiente para así poder descifrar las comunicaciones.

 Desarrollo Político
Cuando el gobierno de los EE. UU. anunció sus intenciones de sacar al mercado el Chip Clipper, nunca dijo explícitamente que paralelamente se estaba ideando prohibir el uso privado de algoritmos de cifrado y convertirlo en una práctica ilegal pero muchas organizaciones creadas en ese entonces, como respuesta en contra de esta iniciativa del gobierno, hacían énfasis en hacer público que esta era una acción necesaria para que Chip Clipper fuera realmente "efectivo".

Estas organizaciones, dedicadas a proteger las "libertades civiles electrónicas", entre ellas el Centro de Información de la Privacidad Electrónica y la Electronic Frontier Foundation, desafiaba la propuesta del Chip Clipper, argumentando que el único efecto que tendría sería dejar expuestos a los ciudadanos comunes y corrientes a la posibilidad de ser vigilados ilegalmente por su gobierno. Además, ya que Skipjack nunca podría ser revisado por la comunidad criptográfica, sería posible que el algoritmo contuviese errores que podrían ser explotados por terceros. Y muchos individuos, empresas y entidades bancarias podrían estar usando un sistema de cifrado que se podría convertir más en un problema que una solución. Más aún, se explicaba que aun cuando sería posible obligar a las empresas de los EE. UU. a usar la tecnología (al menos a todo el organismo público del gobierno y así forzar el estándar), era imposible obligar a las empresas extranjeras a usar esta tecnología que supuestamente contenía una tecnología de cifrado muy poderosa, principalmente porque ningún país desea tener una tecnología que permita a otro gobierno escuchar sus transmisiones telefónicas, y además porque todo dispositivo que contase con un Chip Clipper tendría un costo de al menos $US 16 por sobre un dispositivo alternativo. En ese entonces, el senador John Ashcroft era el principal oponente a nivel de gobierno de la propuesta del Chip Clipper, abogando por el derecho de los individuos a cifrar sus comunicaciones y el derecho a la exportación de software de cifrado.

El desarrollo de muchos paquetes de software tales como Nautilus, *Pretty Good Privacy* (PGP) y PGPfone fueron una respuesta a la propuesta del gobierno. El pensamiento general de la comunidad criptográfica en torno al tema del cifrado público era que si existían alternativas de cifrado que fuesen libres y a la vez poderosas, estas se masificarían y el gobierno no podría impedir su uso. Esta estrategia fue muy efectiva y eventualmente el concepto de "key escrow" en su formato Chip Clipper murió y pasó al olvido.

 Vulnerabilidad

En 1994, Matt Blaze publicó el artículo *Protocol Failure in the Escrowed Encryption Standard* . En él demostraba que el sistema de "*escrow key*" tenía una seria vulnerabilidad. El microprocesador transmitía una llave de 128-bits, conocida como "*Law Enforcement Access Field*" (LEAF) que contenía la información necesaria para recuperar la llave de cifrado del dispositivo. Para evitar que el software que transmitía los datos alterara el LEAF, se enviaba un hash de 16-bits junto con el LEAF. El Chip Clipper no decodificaría mensajes si el hash era inválido. Sin embargo, 16 bits era muy poco, permitiendo realizar un ataque de Fuerza bruta y así encontrar un LEAF distinto al auténtico que entregase el mismo hash. Esto permitiría entonces usar el Chip Clipper como dispositivo de cifrado/descifrado, inhabilitando a la vez la funcionalidad provista por el "*key escrow*".

 Crónica de una muerte anunciada
El Chip Clipper nunca fue aceptado por el mercado y para el año 1996 el concepto del Chip Clipper era un tema abandonado. El gobierno de los Estados Unidos siguió peleando por el concepto de "*key escrow*", ofreciendo incentivos a los desarrolladores de microprocesadores, entregándoles libertades en los controles de aduana si los productos que exportaban contenían software con el concepto de "*key escrow*". Todo esto falló principalmente debido a la disponibilidad de algoritmos libres de uso masivo tales como PGP, el cual estaba libre del control de los EE. UU.

En 1998 Skipjack, el algoritmo usado por el Chip Clipper fue desclasificado.

 Véase también
 *Backdoor*
 Criptografía simétrica
 Cripto. Cómo los informáticos libertarios vencieron al gobierno y salvaguardaron la intimidad en la era digital

 Referencias

 Enlaces externos
Historia del Chip Clipper por Matt Blaze
Paper de Matt Blaze describiendo falla en Chip Clipper
Fotografías del Único Aparto que uso el Chip Clipper
Defensa del Chip Clipper (1995) Dorothy E. Denning
Riesgos de Sistema Key Escrow
