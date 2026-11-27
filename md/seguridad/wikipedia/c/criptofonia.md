---
type: Artículo de enciclopedia
title: Criptofonía
description: "La criptofonía, o secrafonía, (del griego κρύπτω krypto, «ocultar», y fonía \"voz\") es el arte o ciencia de cifrar y descifrar la voz, para que sólo pueda ser entendida por las personas a quienes va dirigida."
resource: https://es.wikipedia.org/wiki/Criptofonía
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptofonía"}
license: CC BY-SA 4.0
id: eswiki-Criptofonía
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptofonía

La **criptofonía**, o **secrafonía**, (del griego κρύπτω krypto, «ocultar», y fonía "voz") es el arte o ciencia de cifrar y descifrar la voz, para que sólo pueda ser entendida por las personas a quienes va dirigida.

 Métodos
Existe diversos métodos criptofonía, pudiéndose aplicar varios de ellos secuencialmente. Algunos de estos son:
Inversión de espectro Es el método más sencillo y comúnmente utilizado, en el que las frecuencias graves son convertidas en agudas y viceversa. Según el ancho de banda así será la inversión. Este método fue usado por el Canal Plus (ahora Digital Plus) en su codificación analógica. El Canal Plus invertía de 200 Hz a 20,000 Hz aproximadamente. En las comunicaciones de VHF y UHF se invierte sobre los 4 kHz, quedando las frecuencias de 3 kHz convertidas en 1 kHz y viceversa, las de 2 kHz se quedan tal cual. Esto puede servir para crear una clave diferente (muy mala) alterando el ancho de banda sobre el que se invierten las frecuencias.
Seguridad: regular.

Partición de frecuencias Las frecuencias de la voz (normalmente de 300 Hz a 3000 Hz - 4000 Hz) son troceadas en grupos de, por ejemplo, 100 Hz.  Luego son barajadas, de forma que las frecuencias de, por ejemplo, 2300 Hz a 2400 Hz son convertidas en frecuencias de 600 Hz a 700 Hz, creando un puzle.
Seguridad: regular.

Partición de frecuencia rodante Igual que la partición de frecuencia pero los cambios en las frecuencias van cambiando varias veces por segundo.
Seguridad: buena.

Partición del tiempo La señal de voz es almacenada y repartida en trozos de tiempo de, por ejemplo, una centésima de segundo. Estos trozos son reordenados siguiendo una secuencia clave (conocida por el receptor) y enviados. Presenta el problema de lo crítico de la sincronización y que no puede ser en tiempo real, presentado siempre un retraso.
Seguridad: buena.

Modulación de amplitud Se altera la amplitud de la voz.
Seguridad: mala.

 Seguridad

Prácticamente todos los métodos analógicos son poco resistentes a un sencillo criptoanálisis, dada su baja entropía. Codificar la voz digitalmente para, posteriormente, comprimir y cifrar el flujo de datos, posiblemente sea mucho más seguro que cualquier sistema analógico.
