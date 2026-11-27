---
type: Artículo de enciclopedia
title: Problema RSA
description: En criptografía, el problema RSA se refiere a la dificultad de efectuar una operación de clave privada mediante el sistema criptográfico RSA conociendo tan solo la clave pública.
resource: https://es.wikipedia.org/wiki/Problema_RSA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Problema_RSA"}
license: CC BY-SA 4.0
id: eswiki-Problema_RSA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Problema RSA

En criptografía, el **problema RSA** se refiere a la dificultad de efectuar una operación de clave privada mediante el sistema criptográfico RSA conociendo tan solo la clave pública. El algoritmo RSA eleva un mensaje numérico a un exponente público, módulo un número compuesto  que es producto de dos primos desconocidos. Para recuperar este mensaje es necesario elevar de nuevo el resultado a un exponente privado, elegido de tal forma que si no se conoce, hallarlo equivale a factorizar el número  (esto es, hallar los dos números primos cuyo producto es N).

Para números suficientemente grandes (mayores de 1024 bits) no se conoce un método eficiente de factorización. De llegar a desarrollarse, supondría una amenaza para los sistemas de seguridad basados en RSA, tanto de cifrado como de firma digital.

 Historia

El sistema RSA es la primera propuesta práctica del método criptográfico de clave pública propuesto en 1976 por Whitﬁeld Diﬃe y Martin Hellman. Fue presentado en 1977 por Ronald Rivest, Adi Shamir y Leonhard Adleman, del MIT. Poco después de su presentación el MIT propuso en *Scientific American* un reto para tranquilizar al público sobre la eficiencia de RSA. Pagarían 100 dólares a quien descifrara un mensaje numérico de 129 cifras decimales publicado en esas mismas páginas junto a su exponente público y módulo. El problema fue bautizado como RSA-129, y los autores estimaron que harían falta varios millones de años para conseguirlo.

El 26 de abril de 1994 un equipo de 600 voluntarios coordinados por Atkins, Graﬀ, Lenstra y Leyland consiguió romper RSA-129, ganando los 100 $ prometidos y donándolos a la Free Software Foundation.
No era la primera vez que se rompía RSA. En 1991 la RSA Security, empresa al cargo de la seguridad de RSA con sede en Massachusetts, propuso varios números semiprimos (esto es, producto de exactamente dos primos) de a partir de 100 cifras decimales y ofreció premios en metálico a quienes encontraran su descomposición. Es lo que se conoció por *RSA Challenge*. Meses después A. K. Lenstra rompió RSA-100, y a este hito le siguieron otros varios en años sucesivos: RSA-110, 120, 130, etc. hasta que el desafío terminó en 2007. En palabras del laboratorio, «Ahora que la industria ha alcanzado una comprensión considerablemente mayor de la seguridad criptoanalítica de los algoritmos simétricos comunes y los de clave pública, estos retos dejan de estar activos».

Aunque notables, estos hitos de factorización no dejan de ser casos aislados. Actualmente no se conoce ningún método general de factorización de enteros y por ello RSA se considera un sistema seguro.

 Formas de abordar el problema
Técnicamente, el problema RSA es el siguiente: dada una clave pública RSA  y un texto cifrado , calcular  de forma eficiente. La estructura de la clave pública RSA requiere que  sea un producto de dos primos grandes,  sea coprimo con  (la función φ de Euler), y .  se escoge al azar dentro de dicho rango. Para describir el problema con precisión, debe también especificarse cómo se generan  y , lo que dependerá del sistema de generación de claves aleatorias usado.

 Factorización
Llamemos  y  a los factores primos de , esto es, . Buscamos un  tal que . Por el pequeño teorema de Fermat basta que  cumpla . Falta conocer , pero la única forma de hacerlo es mediante la fórmula , lo que se traduce en factorizar .

El algoritmo RSA está diseñado para escoger primos  y  suficientemente grandes (del orden de ) para que sea inviable hallarlos mediante ordenadores convencionales. Los métodos más eficientes de factorización de números generales que se conocen son la criba en cuerpos de números (QFS por sus siglas en inglés) y las curvas elípticas. El número más grande factorizado hasta la fecha es RSA-768, un número de 232 cifras decimales (con la actual notación binaria) hallado en enero de 2010 mediante la QFS. Este número está muy por debajo del rango manejado por el algoritmo RSA.

Sin embargo no hay absoluta certeza de que no existan métodos eficientes de factorización, ya sea mediante un nuevo método o una nueva herramienta. La computación cuántica podría proveer de una solución a este problema.

 Otros métodos
Así como no hay pruebas de que la factorización de enteros sea computacionalmente difícil, tampoco la hay de que el problema RSA no lo sea. Por el método descrito anteriormente, el sistema RSA es al menos igual de difícil que factorizar. Pero podría ser incluso menor, ya que el problema RSA no pide expresamente hallar el exponente privado sino solo descifrar un texto. Tal como sugieren D. Boneh y R. Venkatesan, entre descifrar un texto concreto y acceder a la clave privada de cualquier texto cifrado, lo que otorga poder no solo para descifrar cualquier mensaje sino para crear nuevos mensajes a voluntad, hay suficiente margen como para que se pueda romper RSA con un método menos ambicioso. Esto podría explicar que aún no se haya demostrado que romper RSA no es equivalente a factorizar.

Además, RSA posee también una estructura matemática que puede ser explotada sin necesidad de resolver el problema RSA directamente. Para conseguir una funcionalidad completa, el algoritmo RSA debe incluir un «patrón de relleno» (*padding scheme*) como OAEP que proteja contra esta debilidad.

 Véase también
Competición de factorización RSA
Factorización de enteros
NP-completo
RSA
*The Magic Words are Squeamish Ossifrage* (solución de RSA-129)

 Notas

 Referencias
