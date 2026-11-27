---
type: Artículo de enciclopedia
title: Flujo de claves
description: En criptografía, un flujo de claves es un flujo de caracteres aleatorios o pseudoaleatorios que se combinan con un mensaje de texto plano para producir un mensaje cifrado (el texto cifrado).
resource: https://es.wikipedia.org/wiki/Flujo_de_claves
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Flujo_de_claves"}
license: CC BY-SA 4.0
id: eswiki-Flujo_de_claves
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Flujo de claves

En criptografía, un **flujo de claves** es un flujo de caracteres aleatorios o pseudoaleatorios que se combinan con un mensaje de texto plano para producir un mensaje cifrado (el texto cifrado).

Los "caracteres" en el flujo de claves pueden ser bits, bytes, números o caracteres reales como AZ, según el caso de uso.

Por lo general, cada carácter en el flujo de claves se suma, resta o XOR con un carácter en el texto plano para producir el texto cifrado, utilizando aritmética modular.

Los flujos de claves se utilizan en el cifrado de libreta de un solo uso y en la mayoría de los cifrados de flujo. Los cifrados en bloque también se pueden utilizar para producir cadenas de claves. Por ejemplo, el modo CTR es un modo de bloque que hace que un cifrado de bloque produzca un flujo de claves y, por lo tanto, convierte el cifrado de bloque en un cifrado de flujo.

 Ejemplo
En este ejemplo usamos el alfabeto inglés de 26 caracteres de az. Por tanto, no podemos cifrar números, comas, espacios y otros símbolos. Los números aleatorios en el flujo de claves deben estar al menos entre 0 y 25.

Para cifrar, agregamos los números de flujo de claves al texto sin formato. Y para descifrar, restamos los mismos números de flujo de claves del texto cifrado para obtener el texto sin formato.

Si un número de texto cifrado es mayor que 25, lo ajustamos a un valor entre 0-25. Así 26 se convierte en 0 y 27 se convierte en 1 y así sucesivamente. (Tal envoltura se llama aritmética modular).

Aquí, el mensaje de texto sin formato "attack at dawn" ("ataque al amanecer") se combina mediante la adición con el flujo de claves "kjcngmlhylyu" y produce el texto cifrado "kcvniwlabluh".

 Referencias
