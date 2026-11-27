---
type: Artículo de enciclopedia
title: S-Box
description: En criptografía, una S-Box (substitution box) es un componente básico de los algoritmos de cifrado de clave simétrica.
resource: https://es.wikipedia.org/wiki/S-Box
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/S-Box"}
license: CC BY-SA 4.0
id: eswiki-S-Box
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# S-Box

En criptografía, una **S-Box** (*substitution box*) es un componente básico de los algoritmos de cifrado de clave simétrica. En los cifradores por bloques son usadas a menudo para oscurecer la relación existente entre texto plano y texto cifrado (la propiedad confusión de Shannon). En muchos casos las S-Boxes son elegidas cuidadosamente para ser resistentes al criptoanálisis.

En general, una S-Box toma un número *m* de bits de entrada y los transforma en *n* bits de salida. Esto es una S-Box *m*×*n*, implementada como una *lookup table*. Las Tablas prefijadas se usan en algunos algoritmos, como DES, mientras que otros cifradores usan S-Boxes dependientes de la clave, como en Blowfish y Twofish.

Esta ilustración muestra una S-Box de 6×4 bits de DES(S5):

Dada una entrada de 6 bits, la salida de 4 bits se encuentra seleccionando la fila de los dos bits externos y la columna de los 4 internos. Por ejemplo, una entrada "**0**1101**1**" tiene como bits externos (el bit de cada extremo) "**01**" y "1101" como bits internos. La correspondiente salida sería "1001".

Las S-Boxes de DES fueron objeto de intensivo estudio durante años con la intención de localizar una puerta trasera –una vulnerabilidad conocida solo por sus desarrolladores– implantada en el cifrador. El criterio del diseño de la S-Box fue publicado (Don Coppersmith, 1994) después del redescubrimiento público del criptoanálisis diferencial, mostrando que habían sido diseñadas para mostrarse resistentes a este tipo de ataques. Otras investigaciones han demostrado que incluso una leve modificación de una S-Box podría haber debilitado significativamente DES.

 Véase también
Función lógica

 Referencias
 Coppersmith, Don. (1994). The data encryption standard (DES) and its strength against attacks. *IBM Journal of Research and Development*, **38**(3), 243–250.  *(PDF)*
S. Mister and C. Adams, "Practical S-Box Design," Workshop on Selected Areas in Cryptography (SAC '96) Workshop Record, Queens University, 1996, pp. 61–76
Tabla completa S Boxes
