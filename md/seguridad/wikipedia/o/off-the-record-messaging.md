---
type: Artículo de enciclopedia
title: Off the record messaging
description: "El protocolo Off-the-Record Messaging (OTR), «mensajería extraoficial» o «mensajería confidencial», es un protocolo criptográfico que proporciona un cifrado fuerte para conversaciones de mensajería instantánea."
resource: https://es.wikipedia.org/wiki/Off_the_record_messaging
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Off_the_record_messaging"}
license: CC BY-SA 4.0
id: eswiki-Off_the_record_messaging
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Off the record messaging

El protocolo **Off-the-Record Messaging** (**OTR**), «mensajería extraoficial» o «mensajería confidencial», es un protocolo criptográfico que proporciona un cifrado fuerte para conversaciones de mensajería instantánea. OTR utiliza una combinación del algoritmo AES de claves simétricas, el protocolo de intercambio de claves Diffie-Hellman y la función SHA-1. Además de la autenticación y el cifrado, OTR aporta una confidencialidad directa perfecta y cifrado maleable.

La principal motivación debajo de este protocolo fue ocultar la identidad de los participantes en la conversación a la vez que se mantenía la confidencialidad de la propia conversación, como si fuera una conversación privada de la vida real. Esto contrasta con otras fuentes criptográficas en las cuales se produce una salida que, más tarde, puede ser usada como un registro verificable de la comunicación y las identidades de los participantes. La mayoría de las veces, la gente que usa este tipo de software criptográfico desconocen esto y habría sido mejor que hubieran usado OTR. El documento introductorio se llamaba *Off-The-Record Communication, or Why Not To Use PGP*.

El protocolo OTR fue diseñado por los criptógrafos Ian Goldberg y Nikita Borisov. Ambos proporcionan una biblioteca cliente para dar soporte a usuarios de la mensajería instantánea que quieran implementar el protocolo. Existe un complemento para Pidgin y un complemento para Kopete que permiten que OTR sea usado sobre cualquier protocolo IM soportado por Pidgin o Kopete, ofreciendo
una autodetección que inicia la sesión OTR con los amigos que la tengan activada, sin interferir con conversaciones descifradas.

 Implementación
Aparte de dar cifrado y autenticación (características
también proporcionadas por PGP, GnuPG, y X.509 (S/MIME)), OTR ofrece otras características menos comunes:
 Confidencialidad secreta perfecta. Los mensajes solo se cifran con una clave temporal AES para cada mensaje, negociada usando el protocolo de intercambio de claves Diffie-Hellman. El compromiso de cualquier clave criptográfica de vida larga no compromete ninguna conversación previa, incluso si el atacante tiene textos cifrados.

 Ocultación de la identidad. Los mensajes en una conversación no tienen firma digital y, cuando una conversación se ha completado, cualquiera podría falsificar un mensaje que aparentemente venga de otro de los participantes en la conversación, asegurando que es imposible demostrar que cierto mensaje fue escrito por cierta persona. Dentro de la conversación, el destinatario puede estar seguro de que un mensaje viene de la persona que ha identificado.

 Autenticación
A partir de OTR 3.1, el protocolo soporta autenticación mutua entre los usuarios mediante un secreto compartido a través del protocolo del socialista millonario. Esta característica posibilita a los usuarios verificar la identidad de una parte remota y evitar un ataque de intermediario sin la inconveniencia de comparar manualmente las claves a través de una canal externo.

 Limitaciones
Debido a limitaciones de protocolo, OTR no soporta conversaciones multiusuario desde 2009, pero podría ser implementado en el futuro. A partir de la versión 3 de la especificación del protocolo, una clave simétrica extra es derivada durante el intercambio de claves autenticadas que puede ser usada para comunicación segura (por ejemplo cifrar transferencia de archivos) sobre otro canal diferente. No está planificado soporte para audio o vídeo cifrado.
Desde OTR 4.0.0 el complemento de Pidgin soporta múltiples conversaciones con un mismo amigo que haya iniciado sesión en distintos lugares.

 Soporte en clientes
 Nativa
Estos clientes dan soporte OTR:
 Adium (OS X)
 BitlBee (multi-plataforma), desde 3.0 (opcional en tiempo de compilación)
 CenterIM (similar a Unix), desde 4.22.2
 ChatSecure (Android, iOs)
 Climm (similar a Unix), desde 0.5.4
 Cryptocat (multi-plataforma), desde 2.0
 IronChat (basado en Xabber)
 Jitsi (multi-plataforma)
 Kopete (similar a Unix)
 Rocketchat (multi-plataforma)
 Psi+(multi-plataforma), desde 0.16.212.386
 MCabber (similar a Unix), desde 0.9.4
 Xabber (Android)
 Yaxim (Android)

 Chat de Gmail confidencial
Google Talk utiliza el término *off-the-record* para decir que hacer un registro en el chat no es recuperable por un usuario desde la página web de Google. El modo confidencial de Google no tiene conexión a OTR, y sus chats no están cifrados del modo descrito arriba y podrían ser grabados internamente por Google aunque no sean accesibles por los usuarios. Google usa el término *off-the-record* para decir que los registros del chat no son accesibles desde la web de Google (normalmente todos los chats se guardan y pueden ser mostrados de nuevo en cualquier momento). La política de Google respecto a los chats confidenciales no establece que los registros no se guarden en sus servidores.

 Vía complemento
Los siguientes clientes necesitan un complemento para usar OTR. Este complemento permite usar OTR con todos los protocolos de mensajería instantánea en clientes (como OSCAR, XMPP, MSNP, YSMG, etc.)
 Gajim, con un complemento de terceros.
 irsii, WeeChat y xchat, con un complemento de terceros.
 Miranda IM (Microsoft Windows), con un complemento de terceros.
 Pidgin (multi-plataforma), con un complemento disponible en la página de OTR.
 Psi (multi-plataforma), con un complemento de terceros.

 Referencias

 Publicaciones seleccionadas

 Enlaces externos
 Web del proyecto OTR
 Especificación del protocolo
 Off-the-Record Messaging: Useful Security and Privacy for IM , Charla de Ian Goldberg en la Universidad de Waterloo (video)
