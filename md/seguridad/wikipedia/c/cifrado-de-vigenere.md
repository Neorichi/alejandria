---
type: Artículo de enciclopedia
title: Cifrado de Vigenère
description: El cifrado de Vigenère es un cifrado basado en diferentes series de caracteres o letras del cifrado César formando estos caracteres una tabla, llamada tabla de Vigenère, que se usa como clave.
resource: https://es.wikipedia.org/wiki/Cifrado_de_Vigenère
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_de_Vigenère"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_de_Vigenère
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado de Vigenère

El **cifrado de Vigenère** es un cifrado basado en diferentes series de caracteres o letras del cifrado César formando estos caracteres una tabla, llamada **tabla de Vigenère**, que se usa como clave. El cifrado de Vigenère es un cifrado por sustitución simple polialfabético.

El cifrado de Vigenère se ha reinventado muchas veces. El método original fue descrito por Giovan Battista Belasso en su libro de 1553 *La cifra del Sig. Giovan Battista Belasso.* Sin embargo, fue incorrectamente atribuido más tarde a Blaise de Vigenère, concretamente en el , y por ello aún se le conoce como el "cifrado de Vigenère".

Este cifrado es conocido porque es fácil de entender e implementar, además parece irresoluble; esto le hizo valedor del apodo **el código indescifrable** (*le chiffre indéchiffrable,* en francés).

 Historia

El primer cifrado polialfabético fue el llamado cifrado de Alberti, creado por Leon Battista Alberti hacia 1467. Para facilitar los cálculos se aprovechaba de un disco de metal que permitía cambiar fácilmente entre los diferentes alfabetos disponibles. El sistema de Alberti solo cambiaba entre alfabetos después de muchas palabras, y los cambios se indicaban escribiendo la letra del correspondiente alfabeto en el mensaje cifrado. Más tarde, en 1508, Johannes Trithemius, en su trabajo *Poligraphia,* inventó la *tabula recta*, que es básicamente la tabla de Vigenère. Trithemius, sin embargo, solo proporcionó un sistema de cambio progresivo, rígido y predecible entre alfabetos.

Lo que ahora se le conoce como el cifrado de Vigenère, fue originalmente descrito por Giovan Battista Belasso en su mencionado libro de 1533, quien construyó el cifrado basándose en la *tabula recta* de Trithemius, pero añadió una clave repetida para cambiar cada carácter entre los diferentes alfabetos.

Blaise de Vigenère publicó su descripción de un cifrado de autoclave parecido, pero más robusto, antes del reinado de Enrique III de Francia, en 1586. Más tarde, en el , la invención del cifrado dejó de atribuirse a Vigenère.

El cifrado de Vigenère ganó una gran reputación por ser excepcionalmente robusto. Incluso el escritor y matemático Charles Lutwidge Dodgson (Lewis Carroll) dijo que el cifrado de Vigenère era irrompible en un artículo titulado "The Alphabet Cipher" para una revista infantil. En 1917, la revista *Scientific American* afirmó que el cifrado de Vigenère era imposible de romper. Esta reputación era inmerecida, considerando que el método Kasiski resolvió el cifrado en el , y que algunos criptoanalistas habilidosos pudieron romper ocasionalmente el cifrado en el .

A lo largo del , se propusieron distintas variaciones sobre este sistema, pero que no incrementaban significativamente la seguridad y presentaban similares vulnerabilidades; entre estas estaban las siguientes:

 Método de Auray
 Método de Beaufort
 Método de Gronsfeld

Gilbert Vernam trató de arreglar el cifrado (creando el cifrado Vernam-Vigenère en 1918), pero a pesar de sus esfuerzos, el cifrado sigue siendo vulnerable al criptoanálisis.

 Funcionamiento

mensaje:      P A R I S  V A U T  B I E N  U N E  M E S S E
clave:        L O U P L  O U P L  O U P L  O U P  L O U P L
criptograma:  A O M X D  K U K E  P C T X  J H T  W S N I O

En este alfabeto solo existen 27 letras:

En términos matemáticos, puede expresarse la función de cifrado como:

Donde  es la letra en la posición  del texto a cifrar,  es el carácter de la clave correspondiente a , pues se encuentran en la misma posición, y  es el tamaño del alfabeto.
En este caso .

Para descifrar realizamos la operación inversa:

Cuando

Cuando

Donde  es el carácter en la posición  del texto cifrado,  viene siendo el carácter de la clave correspondiente a , y  el tamaño del alfabeto.

Se observa que a una misma letra en el texto plano le pueden corresponder diferentes letras en el texto cifrado.

 Código en Batch para Windows
Un ejemplo para usar se debe guardar como .cmd para ejecutar el programa y ver su funcionamiento.

 Ejemplo código en C

 Vulnerabilidades
Las principales vulnerabilidades del método de Vigenère derivan de su regularidad. Al proponer una serie de cifras cíclicas, el analista simplemente tiene que buscar una serie de grupos de letras que se repitan periódicamente. Al comparar las distintas repeticiones, puede deducir el número de letras de la clave, tras lo cual basta con separar esos alfabetos distintos y aplicar el análisis de frecuencias a cada uno de esos alfabetos (Método Kasiski).

Otra posibilidad sería aplicar el índice de coincidencia para encontrar el número de letras de la clave.

 Véase también
 Cifrado por libro
 Cifra de Delastelle
 Método Kasiski

 Enlaces externos
 Cifrador Vigenère en línea
 Applet que muestra el funcionamiento del cifrado de Vigenere
 Descifran mensaje enviado durante la guerra civil en Estados Unidos (usando este algoritmo)

 Referencias
