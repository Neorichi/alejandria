---
type: Artículo de enciclopedia
title: Protocolo de Needham-Schroeder
description: El protocolo de Needham-Schroeder se refiere a uno de los dos protocolos de comunicación para uso sobre una red insegura, ambos propuestos por Roger Needham y Michael Schroeder en un artículo en 1978.
resource: https://es.wikipedia.org/wiki/Protocolo_de_Needham-Schroeder
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protocolo_de_Needham-Schroeder"}
license: CC BY-SA 4.0
id: eswiki-Protocolo_de_Needham-Schroeder
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protocolo de Needham-Schroeder

El **protocolo de Needham-Schroeder** se refiere a uno de los dos protocolos de comunicación para uso sobre una red insegura, ambos propuestos por Roger Needham y Michael Schroeder en un artículo en 1978. Ellos son:
 El **protocolo de clave simétrica de Needham-Schroeder**, basado en un algoritmo de cifrado simétrico. Forma la base del protocolo Kerberos. El objetivo de este protocolo es realizar una autenticación mutua y establecer una clave de sesión aleatoria entre las dos partes, normalmente para proteger la comunicación subsecuente.
 El **protocolo de clave pública de Needham-Schroeder**, basado en un criptografía asimétrica. Su objetivo es brindar autenticación mutua entre dos partes que se comunican a través de una red, pero en su forma propuesta es inseguro.

 El protocolo simétrico

En este caso, Alice (A) inicia una comunicación con Bob (B). De esta manera,
 S es un servidor confiado por ambas partes
 KAS es una clave simétrica que conocen solo A y S
 KBS es una clave simétrica que conocen solo B y S
 NA y NB son nonces

El protocolo puede especificarse mediante la notación de protocolos de seguridad de la siguiente manera:

Alice le envía un mensaje al servidor identificándose a sí misma y a Bob, diciéndole al servidor que quiere comunicarse con Bob.

El servidor genera la clave  y se la envía a Alice, cifrada usando , para que Alice se la envíe a Bob, y una copia de la clave para ella. Dado que Alice puede estar solicitando claves para usar con distintas personas, el nonce le garantiza a Alice que el mensaje es reciente y que el servidor está respondiendo a un determinado mensaje y la inclusión de Bob le dice a Alice con quién debe compartir esta clave.

Alice le reenvía la clave a Bob, quien la puede descifrar con la clave que él comparte con el servidor, autenticando así esta información.

Bob le envía a Alice un nonce cifrado usando  para demostrarle que él obtuvo la clave.

Alice realiza una operación sencilla sobre el nonce (Ej. restarle 1), lo vuelve a cifrar y se lo envía de vuelta a Bob, para que él verifique que ella existe y que obtuvo la clave también.

 Para que este protocolo pueda ser usado, es necesario exigir que el método de cifrado usado no sea maleable. Esto se debe a que si el cifrado es maleable entonces el último paso, la comprobación de que Alice conoce la clave realizando un cifrado sobre el nonce, no es válida. Si por ejemplo el cifrado es one-time-pad y N es impar, cualquiera puede hallar el  simplemente cambiando el último bit.

Este protocolo es vulnerable a un ataque de replay. Si un atacante almacena los mensajes de este protocolo y luego descubre el valor KAB que fue usado, puede volver a enviarle el mensaje  a Bob, quien lo aceptará y no será capaz de decir si la clave es reciente o no (a no ser que lleve un registro de todas las claves que él usó). Este fallo se resuelve en el protocolo Kerberos mediante la inclusión de un timestamp.

 El protocolo de clave pública

Este protocolo asume el uso de un algoritmo de cifrado de clave pública.

En este caso, Alice (A) y Bob (B) interactúan junto con un servidor de confianza (S) para la distribución de claves públicas a pedido. Estas claves son:
 KPA y KSA, las mitades pública y privada respectivamente de un par de claves de cifrado de A
 KPB y KSB, idem para B
 KPS y KSS, idem para S. (Nótese que en este caso KSS se usa para *cifrar* y KPS para *descifrar*).

El protocolo se desarrolla de la siguiente manera:

A le solicita a S la clave pública de B.

S responde con la identidad de B junto con KPB para constatar.

A inventa NA y se lo envía a B.

B solicita la clave pública de A.

El servidor responde.

B inventa NB y se lo envía a A junto con NA para demostrar su capacidad de poder descifrar con KSB.

A le confirma NB a B para demostrar su capacidad de poder descifrar con KSA.

Al final del protocolo, A y B conocen la identidad del otro, NA y NB. Estos nonces son desconocidos para oyentes furtivos.

 Ataques al protocolo

Desafortunadamente, este protocolo es vulnerable al ataque Man-in-the-middle. Si un impostor I es capaz de persuadir a A para que inicie una sesión con él, este puede reenviar los mensajes a B y hacerle creer a B de que se está comunicando con A.

Ignorando el tráfico desde y hacia S, que no varía, el ataque se desarrolla de la siguiente manera:

A le envía NA a I, quien descifra el mensaje con KSI.

I le reenvía el mensaje a B, haciendo de cuenta que es A quien se está intentando comunicar.

B le envía NB.

I se lo reenvía a A.

A descifra NB y se lo confirma a I, quien pasa a conocerlo.

I vuelve a cifrar NB, y convence a B de que él lo ha descifrado.

Al final del ataque, B cree erróneamente de que A se está comunicando con él y que NA y NB son conocidos únicamente por A y B.

El ataque fue descrito por primera vez en un artículo en 1995 por Gavin Lowe. El artículo describe también una versión arreglada del esquema, al cual se lo llama el protocolo de *Needham-Schroeder-Lowe*.

 Véase también

 Kerberos
 Cifrado maleable

 Enlaces externos

 Descripción del protocolo de clave pública
 Protocolo de clave simétrica
 protocolo de clave pública corregido por Lowe

 Referencias

Bibliografía

 Lowe, Gavin. «Un ataque al protocolo de autenticación de clave pública de Needham-Schroeder.» *Information Processing Letters*, 56(3):131-136, noviembre de 1995.
 Needham, Roger y Michael Schroeder. «Usando cifrado para autenticación en redes de computadora grandes.» *Communications of the ACM*, 21(12), diciembre de 1978.
