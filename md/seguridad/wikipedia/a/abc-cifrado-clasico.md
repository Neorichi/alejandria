---
type: Artículo de enciclopedia
title: ABC (cifrado clásico)
description: El método de cifrado ABC fue empleado por el Ejército Imperial Alemán durante la Primera Guerra Mundial tras el abandono del sistema ÜBCHI.
resource: https://es.wikipedia.org/wiki/ABC_(cifrado_clásico)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/ABC_(cifrado_clásico)"}
license: CC BY-SA 4.0
id: eswiki-ABC_(cifrado_clásico)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# ABC (cifrado clásico)

El **método de cifrado ABC** fue empleado por el Ejército Imperial Alemán durante la Primera Guerra Mundial tras el abandono del sistema ÜBCHI. Se trata de un método que combina procedimientos de sustitución y transposición, pero de baja seguridad. Esta cifra fue resuelta pronto por los criptógrafos del Ejército francés.

Funcionamiento

El sistema ABC consta de dos fases, una primera de sustitución y una segunda de transposición. A modo de ejemplo se encriptará el mensaje: WIKIPEDIA ES UN PROYECTO ABIERTO con esta cifra empleando la palabra clave: CLAVE.

Fase de sustitución

En la fase de sustitución se realiza una sustitución de Vigenère con la clave ABC (lo que le da nombre a la cifra completa).

Con esto el mensaje queda convertido en: WJMIQ GDJCE TWNQT OZGCU QACKE SSO.

Fase de transposición

En la fase de transposición se realiza una transposición columnar empleando la clave antes escogida, en este caso CLAVE. Como el mensaje consta de 28 caracteres, y la clave de 5, se tratará de una transposición columnar incompleta.

Con esto el mensaje quedaría como: MJNGCO WGTOQS QETUE JDWZAS ICQCK.

Debilidades

Dado el corto período de la fase de sustitución, el análisis según el método de Kasinski daría fácilmente con la clave por lo que la seguridad de la cifra dependería, casi exclusivamente, de la fase de transposición. Una vez que se encuentra la longitud de la clave de transposición (en el ejemplo de esta página, 5 caracteres), la clave es muy simple de descubrir, especialmente si es una transposición incompleta como en el ejemplo.

El Ejército Imperial alemán, conocedor de esta debilidad, cambiaba frecuentemente la clave para dificultar la labor de sus oponentes, pero terminó abandonando la clave que sería sustituida posteriormente por cifras más seguras como las cifras ADFGX y ADFGVX.

Referencias
