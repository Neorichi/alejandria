---
type: Artículo de enciclopedia
title: Números sin-nada-sacado-de-la-manga
description: "En criptografía, los números sin-nada-sacado-de-la-manga (traducción literal del término inglés: \"Nothing-up-my-sleeve numbers\") son aquellos que, por su construcción, están libres de sospecha de poseer inadvertidamente …"
resource: https://es.wikipedia.org/wiki/Números_sin-nada-sacado-de-la-manga
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Números_sin-nada-sacado-de-la-manga"}
license: CC BY-SA 4.0
id: eswiki-Números_sin-nada-sacado-de-la-manga
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Números sin-nada-sacado-de-la-manga

En criptografía, los **números sin-nada-sacado-de-la-manga** (traducción literal del término inglés: *"Nothing-up-my-sleeve numbers"*) son aquellos que, por su construcción, están libres de sospecha de poseer inadvertidamente propiedades ocultas. Se utilizan para crear funciones criptográficas como *hashes* y cifrados. Estos algoritmos a menudo necesitan constantes aleatorias para fines de mezcla o inicialización. El criptógrafo puede desear elegir estos valores de una manera que demuestre que las constantes no se seleccionaron con un propósito ilícito, como por ejemplo, para crear una puerta trasera para el algoritmo. Estos temores se pueden disipar mediante el uso de números creados de una manera que deje poco espacio para el ajuste. Un ejemplo sería el uso de los dígitos iniciales del número π como constantes. Sin embargo, utilizar dígitos de π millones de lugares después del punto decimal podría no ser fiable, porque el diseñador del algoritmo podría haber seleccionado ese punto de partida para crear una debilidad secreta que podría explotar más tarde.

Se cree que los dígitos en las representaciones posicionales de números reales como π, *e* y raíces irracionales aparecen con la misma frecuencia (véase número normal). Tales números se pueden ver como el extremo opuesto de los números aleatorios de Chaitin-Kolmogorov, ya que parecen aleatorios pero tienen una entropía de información muy baja. Su uso está motivado por una controversia temprana sobre el Estándar de Cifrado de Datos habilitado en 1975 por el Gobierno de Estados Unidos, que fue criticado porque no se proporcionó ninguna explicación acerca de las constantes utilizadas en su *S-box* (aunque luego se descubrió que fueron cuidadosamente seleccionadas para protegerlo contra la por entonces clasificada técnica del criptoanálisis diferencial). Esto condujo a que se evidenciara la necesidad de disponer de una forma más transparente de generar las constantes utilizadas en criptografía.

"Nada sacado de la manga" es una frase asociada con los magos, quienes a veces presentan un truco de magia descubriendo las mangas para demostrar que no tienen objetos ocultos en su interior.

 Ejemplos

 Ron Rivest utilizó la función trigonométrica seno para generar constantes para el hash MD5, ampliamente utilizado.
 La Agencia de Seguridad Nacional de los EE. UU.  utilizó las raíces cuadradas de los enteros pequeños para producir las constantes utilizadas en su "Algoritmo de hash seguro" SHA-1. Las funciones SHA-2 usan las raíces cuadradas y las raíces cúbicas de los primos pequeños.
 El algoritmo hash SHA-1 utiliza 0123456789ABCDEFFEDCBA9876543210F0E1D2C3 como su valor hash inicial.
 El algoritmo de cifrado Blowfish utiliza la representación binaria de π (sin el 3 inicial) para inicializar su programación clave.
 RFC 3526 describe los números primos para elintercambio de claves de Internet que también se generan a partir de π.
 La caja S del cifrado NewDES se deriva de la Declaración de Independencia de los Estados Unidos.
 El candidato AES DFC deriva todas sus constantes arbitrarias, incluidas todas las entradas de la caja S, de la expansión binaria de .
 El programa clave de  ARIA utiliza la expansión binaria de 1/π.
 El programa clave del cifrado RC5 utiliza dígitos binarios tanto de  como de la proporción áurea.
 La función hash BLAKE, finalista en la competición SHA-3, utiliza una tabla de 16 palabras constantes que son los 512 o 1024 bits principales de la parte fraccionaria de π .
 La programación de claves del cifrado KASUMI usa 0x123456789ABCDEFFEDCBA9876543210 para deducir la clave modificada.

 Contraejemplos

 Se afirmó que la función S-box del hash Streebog se generó aleatoriamente, pero se realizó ingeniería inversa y se demostró que se genera algorítmicamente con algunas debilidades "desconcertantes".
 El Estándar de cifrado de datos (DES) tiene constantes proporcionadas por la NSA. Resultó estar lejos de ser aleatorio, pero en lugar de ser una puerta trasera, hicieron que el algoritmo fuera resistente al criptoanálisis diferencial, un método que no se conocía públicamente en ese momento.
 Dual_EC_DRBG, un generador de bits pseudoaleatorio criptográfico recomendado por NIST, fue criticado en 2007 porque las constantes recomendadas para su uso en el algoritmo podrían haber sido seleccionadas de una manera que permitiera a su autor predecir resultados futuros dada una muestra de valores generados en el pasado. En septiembre de 2013, *The New York Times* escribió que "las notas internas filtradas por un ex contratista de la NSA, Edward Snowden, sugieren que la NSA generó uno de los generadores de números aleatorios utilizados en un estándar NIST 2006, llamado el estándar Dual EC DRBG: que contiene una puerta trasera para la NSA".
 Las curvas P están estandarizadas por NIST para la criptografía de curva elíptica. Los coeficientes en estas curvas son generados por el hash de semillas aleatorias inexplicables, tales como:
 P-224: bd713447 99d5c7fc dc45b59f a3b9ab8f 6a948bc5 .
 P-256: c49d3608 86e70493 6a6678e1 139d26b7 819f7e90 .
 P-384: a335926a a319a27a 1d00896a 6773a482 7acdac73 .

Aunque no está directamente relacionado, después de que la puerta trasera en Dual_EC_DRBG había sido expuesta, los aspectos sospechosos de las constantes de la curva P del NIST llevaron a la preocupación de que la NSA había elegido valores que les daban una ventaja para descubrir claves privadas. Desde entonces, muchos protocolos y programas comenzaron a usar Curve25519 como una alternativa a la curva NIST P-256.

 Limitaciones
Bernstein, et al., demostraron que el uso de números-sin-nada-sacado-de-la-manga como punto de partida en un procedimiento complejo para generar objetos criptográficos, como las curvas elípticas, puede no ser suficiente para evitar la inserción de puertas traseras. Si hay suficientes elementos ajustables en el procedimiento de selección de objetos, el universo de posibles opciones de diseño y constantes aparentemente simples puede ser lo suficientemente grande como para que una búsqueda de las posibilidades permita la construcción de un objeto con las propiedades deseadas de una puerta trasera.

 Referencias

 Bibliografía

 Bruce Schneier. *Applied Cryptography*, second edition. John Wiley and Sons, 1996.
 Eli Biham, Adi Shamir, (1990). Differential Cryptanalysis of DES-like Cryptosystems. Advances in Cryptology — CRYPTO '90. Springer-Verlag. 2–21.
