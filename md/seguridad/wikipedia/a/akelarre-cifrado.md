---
type: Artículo de enciclopedia
title: Akelarre (cifrado)
description: Akelarre es el nombre de un cifrador por bloques propuesto en 1996 que combinaba desarrollos de IDEA y RC5.
resource: https://es.wikipedia.org/wiki/Akelarre_(cifrado)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Akelarre_(cifrado)"}
license: CC BY-SA 4.0
id: eswiki-Akelarre_(cifrado)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Akelarre (cifrado)

- **Nombre:** Akelarre
- **Diseñador:** G. Álvarez • D. de la Guía • F. Montoya • A. Peinado
- **Publicación:** 1996
- **Antecesor:** IDEA / RC5
- **Longitud clave:** múltiple de 64 bits (recomendado - 128 bits)
- **Longitud bloque:** 128 bits
- **Estructura:** Lai–Massey scheme
- **Rounds:** cualquiera (recomendado - 4)
- **Criptoanálisis:** Susceptible de un ataque ciphertext-only

**Akelarre** es el nombre de un cifrador por bloques propuesto en 1996 que combinaba desarrollos de IDEA y RC5. Se demostró que era susceptible a un ataque incluso sólo con texto cifrado en el 2000 (Knudsen y Rijmen). Akelarre cifra en bloques de 128 bits de longitud con un tamaño variable de clave, que debe ser múltiplo de 64 bits. El número de rondas es variable, pero 4 son las sugeridas. Las operaciones en las rondas es similar a la usada en IDEA.

 Bibliografía
 Lars Knudsen y Vincent Rijmen, Ciphertext-only Attack on Akelarre, *Cryptologia*, Vol. 24(2), April 2000, pp135–147.
 G. Álvarez, A. Fúster, D. Guía, F. Montoya, A. Peinado, "Akelarre: nuevo algoritmo de cifrado en bloque", in J. Tena, F. Blanco, editor, IV Reunión española sobre Criptología, vol. 0 of, 93-100, Universidad de Valladolid, Valladolid, septiembre de 1996.
 Niels Ferguson and Bruce Schneier

 Referencias
