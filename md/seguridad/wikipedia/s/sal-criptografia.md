---
type: Artículo de enciclopedia
title: Sal (criptografía)
description: En criptografía, una sal es un conjunto de bits aleatorios que se usan como una de las entradas en una función derivadora de claves.
resource: https://es.wikipedia.org/wiki/Sal_(criptografía)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sal_(criptografía)"}
license: CC BY-SA 4.0
id: eswiki-Sal_(criptografía)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sal (criptografía)

En criptografía, una **sal**  es un conjunto de bits aleatorios que se usan como una de las entradas en una función derivadora de claves. La otra entrada es habitualmente una contraseña. La salida de la función derivadora de claves se almacena como la versión cifrada de la contraseña. Una sal también puede usarse como parte de una clave en un cifrado u otro algoritmo criptográfico. La función de derivación de claves generalmente usa una función hash. A veces se usa como sal el vector de inicialización, un valor generado previamente.

Los datos con sal complican los ataques de diccionario que cifran cada una de las entradas del mismo: cada bit de sal duplica la cantidad de almacenamiento y computación requeridas.

Para mayor seguridad, el valor de la sal se guarda en secreto, separado de la base de datos de contraseñas. Esto aporta una gran ventaja cuando la base de datos es robada, pero la sal no. Para determinar una contraseña a partir de un hash robado, el atacante no puede simplemente probar contraseñas comunes (como palabras o nombres), sino calcular los hashes de caracteres aleatorios (al menos la porción de la entrada que se sabe es la sal), lo que es mucho más lento.

En algunos protocolos, la sal se transmite como texto plano con los datos cifrados, a veces junto con el número de iteraciones empleadas en la generación de la clave (para mejorar su fortaleza). Los protocolos criptográficos que usan sal incluyen el SSL y Ciphersaber.

Los primeros sistemas UNIX usaban sal de 12 bits; las implementaciones modernas usan valores mayores.

La sal está relacionada muy de cerca con el concepto de *nonce*.

El beneficio aportado por usar una contraseña con sal es que un ataque simple de diccionario contra los valores cifrados es impracticable si la sal es lo suficientemente larga. Además, un atacante no podrá crear *rainbow tables*, diccionarios de valores cifrados (contraseña + sal), ya que tardaría demasiado tiempo u ocuparía demasiado espacio. Esto forzaría al atacante a usar el mecanismo de autenticación proporcionado (el cual 'conoce' el valor de sal correcto).

 Ejemplos

Supongamos que la clave secreta (cifrada) de un usuario es robada, y se sabe que usa una de 200.000 palabras como contraseña. El sistema usa una sal de 32 bits. La clave salada es ahora la contraseña original unida a una sal aleatoria de 32 bits. A causa de esto, los hashes precalculados del atacante carecen de valor. Deberá calcular el hash de cada palabra junto con cada una de las 232 (4,294,967,296) posibles combinaciones de sales hasta que se encuentre una coincidencia. El número total de posibles entradas se puede obtener multiplicando el número de palabras en el diccionario por el número de posibles sales:

Para completar un ataque por fuerza bruta, el atacante deberá ahora computar cerca de 860 billones de hashes, en lugar de sólo 200.000. Incluso cuando la contraseña en sí misma sea simple, la sal secreta hace que romper la contraseña sea radicalmente más difícil.

 Implementaciones Unix

Versiones más antiguas de Unix usaban un archivo passwd para almacenar los hashes de las contraseñas saladas (contraseñas precedidas por una sal de dos caracteres aleatorios). Nótese también que en estas versiones antiguas de Unix, la sal era también almacenada en el archivo passwd (en texto plano) junto con el hash de la contraseña salada. El archivo passwd puede ser leído públicamente por todos los usuarios del sistema. Debe ser legible para que software con privilegios de usuario pueda encontrar nombres de usuario y otra información. La seguridad de las contraseñas está entonces protegida solo por las funciones (cifrado o hashing) usadas para el propósito.

Las primeras implementaciones de Unix limitaban las contraseñas a 8 caracteres y usaban una sal de 12 bits, permitiendo así 4096 posibles valores. Aunque 12 bits eran suficientes para muchos propósitos en 1970 (aún con ciertas dudas expresadas entonces), en 2005 la capacidad de disco se ha vuelto lo suficientemente barata para que un atacante puede precomputar los hashes de millones de contraseñas comunes, incluyendo todas las 4096 posibles variaciones de sal para cada contraseña, y almacenarlos en un único disco duro portátil. Un atacante con gran presupuesto puede construir un almacén de discos con todas las contraseñas de 6 caracteres y las más comunes de 7 y 8 caracteres almacenadas en forma cifrada, para cada una de las 4096 posibles sales. Ver password cracking.

 Beneficios adicionales

El moderno sistema de shadow password, en el que los hashes de contraseñas y otra información de seguridad se almacenan en un archivo no público, de alguna forma mitiga estas preocupaciones. Aun así, siguen siendo relevantes en instalaciones multi-servidor donde se usan sistemas de manejo centralizado de contraseñas para "imponer" contraseñas o hashes de contraseñas a múltiples sistemas. En tales instalaciones, la cuenta "root" en cada sistema individual podría ser tratado como menos "confiado" que los administradores del sistema centralizado de contraseñas, así que sigue mereciendo la pena asegurarse de que la seguridad del algoritmo de hashing de contraseñas, incluyendo la generación de valores de sal únicos, es adecuada.

Las sales también ayudan contra *rainbow tables* ya que, en efecto, extiende la longitud y potencialmente la complejidad de la contraseña. Si las *rainbow tables* no tienen contraseñas con la misma longitud (por ejemplo, 8 bytes de contraseña y 2 bytes de sal, son 10 bytes totales de password) y complejidad (las sales no alfanuméricas incrementan la complejidad de las contraseñas estrictamente alfanuméricas) que la contraseña con sal, la contraseña no se encontrará. Si se averigua, se tendrá que eliminar la sal de la contraseña antes de poder usarla.

Las sales también hacen mucho más lentos los ataques de fuerza bruta al crackear grandes cantidades de contraseñas (pero no en el caso de crackear sólo una contraseña). Sin las sales, un atacante que está crackeando muchas contraseñas al mismo tiempo sólo necesita generar un hash y compararlo con los demás hashes. En cambio, con sales, todas las contraseñas tendrán diferentes sales, por lo que cada intento deberá ser hasheado por separado para cada sal, lo que es mucho más lento debido a que la generación de hashes usualmente consume muchos recursos computacionales.

Otro beneficio (menor) de una sal es la siguiente: dos usuarios podrían escoger la misma cadena de caracteres como contraseña, o el mismo usuario puede elegir la misma contraseña en dos máquinas. Sin una sal, esta contraseña podría ser almacenada con la misma cadena hash en el archivo de contraseñas. Esto podría descubrir que las dos cuentas tienen la misma contraseña, permitiendo a cualquiera que conozca una de las contraseñas acceder a la otra cuenta. Salando los hashes de la contraseña con dos secuencias de caracteres aleatorias, incluso si las dos cuentas usan la misma contraseña, sería extraño que alguien pudiese descubrir esto leyendo los archivos passwd.

 Véase también
 Password cracking

 Enlaces externos
