---
type: Artículo de enciclopedia
title: Cifrado de clave pública seguro adelante
description: "El cifrado de clave pública seguro adelante, también conocido como cifrado seguro adelante o por las siglas FSE (del inglés forward-secure encryption) o fs-PKE (del inglés forward-secure public key encryption, fue …"
resource: https://es.wikipedia.org/wiki/Cifrado_de_clave_pública_seguro_adelante
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_de_clave_pública_seguro_adelante"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_de_clave_pública_seguro_adelante
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado de clave pública seguro adelante

El **cifrado de clave pública seguro adelante**, también conocido como **cifrado seguro adelante** o por las siglas **FSE** (del inglés *forward-secure encryption*) o **fs-PKE** (del inglés *forward-secure public key encryption*, fue introducido por R. Anderson.

El primer sistema eficiente fue propuesto por R. Canetti y otros. Este sistema está construido sobre un cifrado basado en identidad y por eso se le llama **fs-IBE** (del inglés *forward-secure identity-based encryption*).

 La idea fundamental de este tipo de sistemas es tener una clave pública estática que no cambia y tener un procedimiento que vaya cambiando la clave secreta cada vez que finaliza un determinado periodo de tiempo. El proceso de cálculo de la clave secreta tiene que ser de un solo sentido: Es fácil calcular la clave siguiente a partir de la anterior, sin embargo el problema inverso tiene que ser difícil y por tanto si se viola una clave secreta la seguridad de las claves anteriores permanece.

Estos sistemas aseguran que los mensajes que utilizan claves secretas antiguas se mantienen seguros aunque sea violada la seguridad de la clave secreta actual. Sin embargo, en estos sistemas, si la seguridad de una clave secreta está violada entonces ya no serán seguras las claves secretas siguientes.

 Referencias
