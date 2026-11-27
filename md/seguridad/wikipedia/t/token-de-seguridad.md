---
type: Artículo de enciclopedia
title: Token de seguridad
description: Un token de seguridad (también llamado llave digital o llave electrónica) es un dispositivo físico utilizado para acceder a un recurso restringido electrónicamente.
resource: https://es.wikipedia.org/wiki/Token_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Token_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Token_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Token de seguridad

Un **token de seguridad** (también llamado **llave digital** o **llave electrónica**) es un dispositivo físico utilizado para acceder a un recurso restringido electrónicamente. El token se utiliza como complemento o en lugar de una contraseña. Actúa como una llave electrónica para acceder a algo. Por ejemplo, una tarjeta de acceso inalámbrica que abre una puerta cerrada, o en el caso de un cliente que intenta acceder a su cuenta bancaria en línea, el uso de un token proporcionado por el banco puede probar que el cliente es quien dice ser.

Algunos tokens pueden almacenar claves criptográficas que pueden utilizarse para generar una firma digital, o datos biométricos, como los detalles de las huellas dactilares. Algunos diseños incorporan un embalaje a prueba de manipulaciones, mientras que otros pueden incluir pequeños teclados para permitir la introducción de un PIN o un simple botón para iniciar una rutina de generación con cierta capacidad de visualización para mostrar un número de clave generado. Los tokens conectados utilizan una variedad de interfaces que incluyen USB, NFC, RFID o Bluetooth. Algunos tokens tienen audio, diseñados para personas con problemas de visión.

Tipos de contraseñas

Todos los token contienen alguna información secreta que se utiliza para probar la identidad. Hay cuatro formas diferentes en las que esta información puede ser utilizada:

 Token de contraseña estáticaEl dispositivo contiene una contraseña que está físicamente oculta (no visible para el poseedor), pero que se transmite para cada autenticación. Este tipo es vulnerable a los ataques de reinyección.

 Token de contraseña dinámica síncronaUn temporizador se utiliza para rotar a través de varias combinaciones producidas por un algoritmo criptográfico. El token y el servidor de autenticación deben tener relojes sincronizados.

 Token de contraseña asincrónicaSe genera una contraseña de un solo uso sin el uso de un reloj, ya sea de una libreta de un solo uso o de un algoritmo criptográfico.

 Token de respuesta al desafío Utilizando la criptografía de clave pública, es posible probar la posesión de una clave privada sin revelar esa clave. El servidor de autenticación cifra una impugnación o desafío (por lo general un número aleatorio, o al menos datos con algunas partes aleatorias) con una clave pública; el dispositivo demuestra que posee una copia de la clave privada correspondiente proporcionando la impugnación descifrada.

 Véase también
 PKCS, grupo de estándares, de los cuales de la RSA PKCS #11 and PKCS #15.
 PKI, estándar en el que se enmarca el Cryptoki.
 HSM, dispositivo criptográfico.
Tarjeta de Coordenadas

 Referencias
*(PDF 3.08 Mb)* Especificación para dispositivos de interfaz de tarjeta de circuitos integrados.

 Enlaces externos
 RSA Labs , página de los laboratorios RSA, elaboradores del estándar PKCS#11.
