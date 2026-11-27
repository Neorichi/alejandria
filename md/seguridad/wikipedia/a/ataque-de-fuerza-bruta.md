---
type: Artículo de enciclopedia
title: Ataque de fuerza bruta
description: En criptografía, se denomina ataque de fuerza bruta a la forma de recuperar una clave probando todas las combinaciones posibles hasta encontrar aquella que permite el acceso.
resource: https://es.wikipedia.org/wiki/Ataque_de_fuerza_bruta
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_de_fuerza_bruta"}
license: CC BY-SA 4.0
id: eswiki-Ataque_de_fuerza_bruta
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque de fuerza bruta

En criptografía, se denomina **ataque de fuerza bruta** a la forma de recuperar una clave probando todas las combinaciones posibles hasta encontrar aquella que permite el acceso.

Dicho de otro modo, define al procedimiento por el cual a partir del conocimiento del algoritmo de cifrado empleado y de un par texto claro/texto cifrado, se realiza el cifrado (respectivamente, descifrado) de uno de los miembros del par con cada una de las posibles combinaciones de clave, hasta obtener el otro miembro del par. El esfuerzo requerido para que la búsqueda sea exitosa con probabilidad mejor que la par será  operaciones, donde  es la longitud de la clave (también conocido como el *espacio de claves*). Este enfoque no depende de tácticas intelectuales; más bien, se basa en hacer varios intentos.

Otro factor determinante en el coste de realizar un ataque de fuerza bruta es el juego de caracteres que se pueden utilizar en la clave. Contraseñas que sólo utilicen dígitos numéricos serán más fáciles de descifrar que aquellas que incluyen otros caracteres como letras, así como las que están compuestas por menos caracteres serán también más fáciles de descifrar, la complejidad impuesta por la cantidad de caracteres en una contraseña es logarítmica.

 Descripción y cálculo

La fuerza bruta suele combinarse con un ataque de diccionario, en el que se encuentran diferentes palabras para ir probando con ellas.

Estos tipos de ataques, no son rápidos, para una contraseña compleja, puede llegar a tardar siglos (aunque también depende de la capacidad de operación del ordenador que lo ejecute).

En la actualidad este tipo de ataques son usados para hackear Facebook, correos electrónicos, auditar redes WiFi y otras redes sociales.

Se puede calcular la cantidad de posibles contraseñas. De esto depende la cantidad de caracteres de la contraseña en cuestión, y el conjunto de caracteres. Evidentemente, puesto que la contraseña se desconoce, no se sabe cuán larga es, ni cuáles caracteres contiene; sin embargo, de momento consideremos una contraseña de exactamente caracteres, de los cuales dichos caracteres son los siguientes : el alfabeto español (a-z, A-Z, contando la eñe, es decir caracteres), los caracteres numéricos (0-9, es decir caracteres), y los caracteres *#*, *$*, *%*, *&*, */*, ***, *-*, *.*, *_* y *@*. Es decir, consideraremos un total de posibles caracteres.

Procedamos al cálculo. Ya que es posible repetir caracteres, y su orden sí importa, el problema se trata de una *variación con repetición* (no de una *combinación*, ni una *permutación*), y por lo tanto de la estadística/combinatoria tenemos que existe un total de posibles contraseñas; nótese que la cantidad de posibles contraseñas varía exponencialmente, no linealmente. Pero esto es suponiendo que la contraseña es exactamente de caracteres, y de los cuales todos esos son algunos de los mencionados anteriormente. Sabemos que la contraseña desconocida no necesariamente será de caracteres, sino que puede ser más corta o más larga (de  caracteres), de manera que también debemos considerar esas posibilidades; supondremos que la contraseña es de al menos caracteres y como mucho de , inclusive. También sabemos que es posible que la contraseña tenga otros caracteres (por ejemplo "+", "?", e incluso caracteres de otros alfabetos como el griego o el japonés, y cualquier carácter UNICODE), aunque omitiremos este hecho y nos conformaremos con el conjunto anterior. Por lo tanto, en definitiva, existe un total de posibles contraseñas. El resultado de esta suma es el siguiente:

posibles contraseñas. Obviamente en realidad no es necesario probarlas todas; se requerirían  intentos sólo si por muchísima casualidad el último intento de contraseña es el correcto, pero la probabilidad de que eso ocurra es prácticamente 0; en cambio, podemos asumir que en promedio se adivinará la clave cuando se haya probado la mitad de las posibles combinaciones, es decir , bajo las suposiciones mencionadas antes. Este número es muy grande, por lo que puede tomar mucho tiempo en encontrar la contraseña correcta, manifestando la desventaja del ataque de fuerza bruta. Para adivinar una contraseña también influirán otros factores tales como la rapidez de la computadora usada, en cuál número de intentos se adivinaría (lo cual en general se desconoce), si el servidor o sitio web tiene CAPTCHA, y/o si el servidor o sitio web deshabilita temporalmente el acceso a una cuenta debido a varios intentos de contraseña (actualmente sitios como Facebook deshabilitan temporalmente luego de varios intentos fallidos, y otros como Snapchat requieren resolver CAPTCHA, pero Instagram no emplea ninguna de esas dos técnicas y por ende sus usuarios son más vulnerables a los hackers).

Troy Hunt, un director regional de Microsoft de Australia, analizó las contraseñas de los sitios web de Sony y Gawker obtenidos en un *breach* (violación de datos) y las publicadas por el grupo de hackers LulzSec incluyendo sitios como pron.com. De este análisis determinó que el 14 % de contraseñas son de nombres de personas (p. ej. *maggie*, *michael*, *jennifer*), el 8 % son de nombres de lugares (p. ej. *dallas*, *canada*, *boston*), el 25 % son palabras de diccionarios (p. ej. *password*, *monkey*, *dragon*), el 14 % son exclusivamente números (p. ej. *123456*, *12345678*, *123456789*), el 2.7 % son palabras repetidas dos veces (p. ej. *blahblah*, *poopoo*, *lovelove*), el 2.6 % son palabras del correo del usuario (p. ej. *murphy666* en *murphy666@…*, *baolihua* en *baolihua@…*, y *racecar73* en *racecar73@…*), entre otras categorías.

El sitio web WP Engine (*WordPress Engine*) analizó dos conjuntos de datos sobre contraseñas, uno que se publicó en foro ruso de BitCoin y otro publicado por el consultor de seguridad Mark Burnett que incluye más de 10 millones de contraseñas en toda la web. De este análisis se observó que algunas de las contraseñas más comunes son *123456*, *password*, *12345678*, *qwerty*, *123456789*, *12345*, *1234*, *111111*, *1234567*, *dragon*, *123123*, *baseball*, *abc123*, *football*, *monkey*, *letmein*, *shadow*, *master*, *696969*, *michael*, *mustang*, *666666*, *qwertyuiop*, *123321*, *1234567890*. También se observó que es común añadir un número entre 1 y 9 al final de la contraseña. En ese análisis también se revelan contraseñas de empleados de empresas como Facebook, Yahoo!, Mozilla, BBC, Vimeo, Nike, Microsoft, BuzzFeed, PayPal, IBM, Google, Twitter, GitHub, Pinterest, y Dropbox.

 Referencias
