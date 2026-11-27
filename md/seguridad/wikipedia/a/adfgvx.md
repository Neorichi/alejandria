---
type: Artículo de enciclopedia
title: ADFGVX
description: "En criptografía, la cifra ADFGVX, inventada por el teniente Fritz Nebel (1891–1977) en 1917, al igual que la cifra ADFGX a la que sustituyó a partir de mayo de 1918, fue escogida por el Alto Mando alemán como la más …"
resource: https://es.wikipedia.org/wiki/ADFGVX
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/ADFGVX"}
license: CC BY-SA 4.0
id: eswiki-ADFGVX
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# ADFGVX

En criptografía, la cifra ADFGVX, inventada por el teniente Fritz Nebel (1891–1977) en 1917, al igual que la cifra ADFGX a la que sustituyó a partir de mayo de 1918, fue escogida por el Alto Mando alemán como la más segura para cifrar sus comunicaciones antes de las grandes ofensivas de 1918, durante la Primera Guerra Mundial.

La seguridad de la cifra, relativamente grande para tratarse de una cifra que puede operarse con papel y lápiz, se debe a su naturaleza enrevesada, con una mezcla de sustitución y transposición.

No obstante su seguridad, fue descifrada a tiempo para influir en el desarrollo de los acontecimientos por el criptógrafo francés Georges Painvin, del Deuxieme Bureau. En concreto, fue un mensaje relativo a la remisión de municiones lo que permitió a los franceses averiguar el lugar de la ofensiva realizada por las tropas alemanas entre el 9 y el 13 de junio de 1918.

Se trata de la, cronológicamente, última cifra importante aparecida antes del desarrollo de las máquinas criptográficas.

 Método de operación

La cifra ADFGVX, al igual que la cifra ADFGX se dividía en dos fases, una primera fase de sustitución y una segunda de transposición. Durante el tiempo que la estuvieron empleando, y al igual que habían hecho con la cifra ADFGX, los ejércitos alemanes cambiaban las claves diariamente, tanto para la fase de sustitución como las palabras clave de la fase de transposición.

 Sustitución

Lo primero es necesario crear una matriz cuadrada análoga al Cuadrado de Polibio de orden 6 en la que introduciremos, en el orden que hayamos acordado con el receptor, las 26 letras del alfabeto (el alfabeto alemán no reconoce la letra Ñ) y los diez dígitos. Cada columna y cada línea irán identificadas con alguna de las letras que dan nombre a la clave: ADFGVX. Como ejemplo nos servirá el siguiente. Es importante que esta matriz permanezca secreta ya que es crucial para el desarrollo del algoritmo de cifrado y descifrado.

Una vez que tenemos la matriz, sustituimos cada letra de nuestro mensaje por las ordenadas y abscisas (respectivamente) de cada una de las letras que lo componen de forma que el número de caracteres se duplica. Emplearemos como texto claro: *mensaje de prueba*. Por lo tanto, nos quedará:

Como se puede comprobar, de momento no es más que una sencilla sustitución monoalfabética.

 Transposición

El texto cifrado que hemos obtenido en la primera fase de sustitución, será sometido a una nueva fase de cifrado, esta vez con una transposición columnar simple para lo cual tenemos que establecer primero una palabra clave. En el caso que nos ocupa, emplearemos la palabra clave *PALCO*. Seguidamente, ordenaremos todos los caracteres cifrados en una tabla que estará encabezada por dicha palabra clave. En el caso que nos ocupa, se trata de una fácil concordancia al ser la clave de 5 letras y el mensaje de 30, con lo que es un resultado exacto, pero no tendría por qué ser así, forzosamente.

Una vez así ordenadas, reordenamos la parrilla ordenando las columnas de acuerdo con el orden alfabético de la palabra clave, esto es pasando de *PALCO* a *ACLOP*.

Ya, lo único que nos falta es copiar el resultado, columna a columna, de arriba abajo, empezando por la primera y tenemos el mensaje listo para retransmitir. En el presente caso, para una mayor claridad, se insertará un espacio entre la transcripción de cada columna.

  GFVDAA XXXGFX DXDXGG FVGDDV DDGXFX

Una vez hecho esto, está listo para ser retransmitido.

 Denominación

La razón de la denominación ADFGVX para esta clave se debe a la elección de esas letras para dar nombre a líneas y columnas en la matriz de sustitución. El motivo de la elección de tales letras, en lugar de algo más sencillo como ABCDEF, reside en que debían ser retransmitidas por telégrafo o por radio de onda corta, en ambos casos, empleando el alfabeto Morse. En el alfabeto Morse, las letras A, D, F, G, V y X son muy distintas por lo que se reducía la probabilidad de errores de transmisión.

 Referencias
