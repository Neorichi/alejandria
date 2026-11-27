---
type: Artículo de enciclopedia
title: Cifrado de extremo a extremo
description: "El cifrado de extremo a extremo o de principio a fin (del inglés end-to-end encryption o E2EE), también cifrado de punta a punta, es un sistema de comunicación en el que solo los usuarios que se comunican pueden leer …"
resource: https://es.wikipedia.org/wiki/Cifrado_de_extremo_a_extremo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_de_extremo_a_extremo"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_de_extremo_a_extremo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado de extremo a extremo

El **cifrado de extremo a extremo o de principio a fin** (del inglés ***end-to-end encryption*** o **E2EE**), también **cifrado de punta a punta**, es un sistema de comunicación en el que solo los usuarios que se comunican pueden leer los mensajes. Garantiza que el emisor original lo convierta en un mensaje cifrado y que lo descifre el receptor final. En principio, evita que los espías potenciales, incluidos los proveedores de telecomunicaciones, los proveedores de Internet e incluso el proveedor del servicio de comunicación, puedan acceder a las claves criptográficas necesarias para descifrar la conversación. Los sistemas están diseñados para vencer cualquier intento de vigilancia o alteración porque ningún tercero puede descifrar los datos que se están comunicando o almacenando. Por ejemplo, las empresas que usan cifrado de extremo a extremo no pueden entregar los mensajes de texto de sus clientes a las autoridades.

 Intercambio de claves
En un sistema E2EE, las claves de cifrado solo deben ser conocidas por las partes que se comunican. Para lograr este objetivo, los sistemas E2EE pueden encriptar datos usando una cadena de símbolos preestablecidos, llamada secreto precompartido (PGP), o un secreto de una sola vez derivado de dicho secreto precompartido (DUKPT). También pueden negociar una clave secreta en el lugar usando el intercambio de clave Diffie-Hellman (OTR).

 Uso moderno
A partir de 2016, los sistemas de comunicaciones típicos basados en servidor no incluyen el cifrado de principio a fin. Estos sistemas solo pueden garantizar la protección de las comunicaciones entre clientes y servidores, lo que significa que los usuarios deben confiar en los terceros que ejecutan los servidores con los textos originales. El cifrado de extremo a extremo se considera más seguro porque reduce el número de partes que podrían interferir o romper el cifrado. En el caso de la mensajería instantánea, los usuarios pueden usar un cliente de terceros para implementar un esquema de cifrado de extremo a extremo a través de un protocolo que no sea E2EE.

Algunos sistemas que no son E2EE, como Lavabit y Hushmail, se describieron a sí mismos como que ofrecen cifrado "de extremo a extremo" cuando no lo hacían. Otros sistemas, como Telegram y Google Allo, han sido criticados por no tener encriptación de principio a fin, que ofrecen, habilitada por defecto.

Algunos servicios cifrados de copia de seguridad y uso compartido de archivos proporcionan encriptación del lado del cliente. La encriptación que ofrecen aquí no se conoce como encriptación de principio a fin porque los servicios no están destinados a compartir mensajes entre usuarios. Sin embargo, el término "cifrado de extremo a extremo" se usa a menudo como sinónimo de encriptación del lado del cliente.

 Desafíos
 Ataque de intermediario

El cifrado de extremo a extremo garantiza que los datos se transfieren de forma segura entre los puntos finales. Pero, en lugar de intentar romper el cifrado, un espía puede suplantar a un destinatario del mensaje (durante el intercambio de clave o sustituyendo su clave pública por el del destinatario), de modo que los mensajes se cifren con una clave conocida por el atacante. Después de descifrar el mensaje, el fisgón puede encriptarlo con una clave que comparte con el destinatario real o su clave pública en el caso de sistemas asimétricos, y enviar el mensaje de nuevo para evitar la detección. Esto se conoce como un Ataque de intermediario.

 Autenticación

La mayoría de los protocolos de encriptación de principio a fin incluyen alguna forma de autenticación de punto final específicamente para prevenir ataques MITM. Por ejemplo, uno puede confiar en las autoridades de certificación o en una red de confianza. Una técnica alternativa es generar hashes criptográficos (Huella digital de clave pública) basados en las claves públicas de los usuarios que se comunican o las claves secretas compartidas. Las partes comparan sus huellas digitales de clave pública utilizando un canal de comunicación externo (fuera de banda) que garantiza la integridad y la autenticidad de la comunicación (pero no necesariamente el secreto), antes de comenzar su conversación. Si las huellas dactilares coinciden, en teoría, no hay intermediario.

Cuando se muestran para inspección humana, las huellas digitales de clave pública suelen codificarse en cadenas hexadecimales. Estas cadenas se formatean en grupos de caracteres para su legibilidad. Por ejemplo, una huella digital MD5 de 128 bits se mostraría de la siguiente manera:

 43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8

Algunos protocolos muestran representaciones de lenguaje natural de los bloques hexadecimales. Como el enfoque consiste en un mapeo uno a uno entre bloques de huellas digitales de clave pública y palabras, no hay pérdida de entropía. El protocolo puede elegir mostrar las palabras en el idioma nativo (del sistema) del usuario. Sin embargo, esto puede hacer que las comparaciones entre idiomas sean propensas a errores. Para mejorar la localización, algunos protocolos han elegido mostrar las huellas digitales de clave pública como bases de 10 cadenas en lugar de cadenas de lenguaje natural o hexadecimal. Las aplicaciones de mensajería modernas también pueden mostrar huellas digitales de clave pública como códigos QR que los usuarios pueden escanear los dispositivos de los demás.

 Seguridad en el Punto final
El paradigma de cifrado de extremo a extremo no aborda directamente los riesgos en los puntos finales de comunicación. La computadora de cada usuario todavía puede ser pirateada para robar su clave criptográfica (para crear un ataque MITM) o simplemente leer los mensajes descifrados de los destinatarios tanto en tiempo real como a partir de archivos de registro. Incluso el conducto de comunicación más perfectamente encriptado solo es tan seguro como el buzón del otro extremo. Los principales intentos para aumentar la seguridad del punto final han sido aislar la generación de claves, el almacenamiento y las operaciones criptográficas en una tarjeta inteligente como Project Vault de Google. Sin embargo, dado que la entrada y salida de texto claro aún son visibles para el sistema host, el malware puede monitorear las conversaciones en tiempo real. Un enfoque más robusto es aislar todos los datos confidenciales en una computadora totalmente aislada. PGP ha sido recomendado por expertos para este propósito:

Sin embargo, como señala Bruce Schneier, Stuxnet desarrollado por EE. UU. e Israel saltó con éxito el espacio aéreo y llegó a la red de la planta nuclear de Natanz en Irán. Para lidiar con la exfiltración clave con malware, un enfoque es dividir la Base de computador confiable detrás de dos computadoras unidireccionalmente conectadas que evitan la inserción de malware o la exfiltración de datos confidenciales con malware insertado.

 Puertas traseras

Las empresas también pueden voluntaria o involuntariamente introducir puertas traseras a su software que ayudan a subvertir la negociación de la clave o eludir el cifrado por completo. En 2013, la información filtrada por Edward Snowden mostró que Skype tenía una puerta trasera que permitía a Microsoft entregar los mensajes de sus usuarios a la NSA a pesar del hecho de que esos mensajes estaban encriptados oficialmente de principio a fin.

 Referencias
