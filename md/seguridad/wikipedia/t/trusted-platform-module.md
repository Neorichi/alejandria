---
type: Artículo de enciclopedia
title: Trusted Platform Module
description: "En informática, un (TPM, traducido al español como módulo de plataforma segura, entre otras alternativas) es el nombre de una especificación publicada que detalla un criptoprocesador seguro que puede almacenar claves …"
resource: https://es.wikipedia.org/wiki/Trusted_Platform_Module
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Trusted_Platform_Module"}
license: CC BY-SA 4.0
id: eswiki-Trusted_Platform_Module
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Trusted Platform Module

En informática, un **** (**TPM**, traducido al español como **módulo de plataforma segura**, entre otras alternativas) es el nombre de una especificación publicada que detalla un criptoprocesador seguro que puede almacenar claves de cifrado para proteger información, así como el nombre general de las implementaciones de dicha especificación, frecuentemente denominadas "chip TPM" o "dispositivo de seguridad TPM". La especificación fue publicada por el Trusted Computing Group y actualmente se encuentra en la versión 2.0, estandarizada en 2016.

La especificación también está disponible como el estándar internacional ISO/IEC 11889. TCG lanzó la *Especificación de biblioteca* TPM 2.0 . Su última edición y erratas se publicaron el 11 de junio de 2020.

El TPM es un chip pasivo desactivado en la fábrica y que solo el propietario de un computador equipado con él puede elegir activar. La identidad del propietario depende del escenario (Ej.: En una empresa, el propietario es el administrador del departamento de informática, y en ordenadores personales el propietario es el usuario final). Incluso cuando está activado el TPM solo recibe comandos y datos de la CPU local, realiza su trabajo y devuelve los resultados.

Provee:

Memoria tanto volátil como no volátil. El almacenamiento no volátil es resistente a modificaciones. El almacenamiento no volátil se usa por ejemplo para almacenar claves no migrables (Ej. *Endorsemente Key* y *Storage Root Key*) y el almacenamiento volátil se usa para almacenar de forma segura las mediciones de integridad realizadas para conseguir la computación confiable
Generador de números aleatorios seguro
Algoritmos de generación de claves
Funciones criptográficas como  cifrado/descifrado RSA y funciones hash.
Funcionalidades para permitir que la plataforma sea confiable:
Proporcionar mediciones e informes seguros de la integridad. Permite obtener mediciones de integridad y los resultados pueden ser almacenados de forma segura dentro del TPM. Basándose en estas medidas, un TPM puede ser usado para obtener un informe verificable que refleje la integridad del estado de la plataforma.
Sellado de datos. Los datos pueden ser almacenados de tal forma que solo sean accesibles si el usuario se autentifica satisfactoriamente y si la plataforma tiene cierto estado de integridad.

Sus funcionalidades son usadas para implementar el RTS y el RTR de la computación confiable pero también puede ser usada por el sistema operativo, en Windows 11, es un requisito indispensable tener la versión 2.0 para instalar y correr el sistema, también es usado por aplicaciones para realizar operaciones criptográficas aunque su rendimiento es bastante bajo. El CRTM para proporcionar el RTM de la computación confiable está incluido un tipo de pre-BIOS protegida donde también reside un software de soporte llamado *Trusted Software Stack* (TSS) que tiene varias funciones como proveer de una interfaz estándar para los TPM's de distintos fabricantes para comunicarse con la plataforma o con plataformas remotas. El CRTM y el TPM trabajando juntos forman la llamada TBB (del inglés *Trusted Building Block*).

 Funcionamiento
La mayor parte de las soluciones de seguridad actuales se basan en software. En consecuencia, no proporcionan una protección de seguridad suficiente y son vulnerables a los ataques físicos o lógicos. Sin embargo, TPM es una solución de seguridad basada en hardware y software. Forma parte del proceso de inicio del equipo portátil y también se integra con el sistema operativo. A pesar de estar físicamente separado de la CPU principal, el TPM va unido al circuito principal del portátil.

La raíz de esta solución se encuentra en el almacenamiento seguro basado en hardware.

Cuando el software del sistema genera una clave o un certificado para datos cifrados, esas claves y
certificados se sellan en el TPM. Los bits de información almacenada autentifican y proporcionan información sobre la integridad de la plataforma cuando es necesario, e informan al usuario y a los socios de comunicación (por ejemplo, al proveedor de contenido) del estado del entorno de hardware y software. El estado se proporciona sobre la base de la exclusividad de la plataforma que, a su vez, se basa en las claves únicas almacenadas en el TPM.

Cada chip TPM tiene un número único, pero el sistema autentifica al usuario mediante las claves o los identificadores (ID) almacenados en el TPM, no por el número único. Como resultado, el TPM puede soportar los ataques lógicos y físicos para proteger las claves y credenciales almacenadas.

El nivel de seguridad más alto se puede obtener por medio de una autenticación bidireccional que consiste en utilizar un chip TPM para la identificación de la plataforma y una autenticación del usuario en forma de clave USB o testigo (token) SD. Esta autenticación bidireccional sólo funciona por separado, ya que, por ejemplo, el testigo SD no se puede almacenar en el TPM.

 Claves involucradas
En la memoria del TPM se almacenan:
 Clave RSA **Storage Root Key** (SRK). Es parte del RTS de la computación confiable. Es una clave no volátil no migrable (no sale del dispositivo) que protege las otras claves usadas por las funciones criptográficas y están almacenadas fuera del TPM. Permite construir una jerarquía de claves
 Clave RSA **Endorsemente Key** (EK). Es parte del RTR de la computación confiable. Es una clave no volátil no migrable (no sale del dispositivo),  única y distinta para cada TPM creada por el fabricante del TPM. Está certificada para asegurar que el TPM es genuino.
 Clave RSA **Attestation Identity Key** (AIK). Una clave AIK se usa para firmar un valor de medición de integridad para así crear una prueba de atestación. Debido a problemas de privacidad no se usa la EK. Una AIK es similar a la EK excepto que:
 Un TPM puede tener un número ilimitado de ellas
 Son creadas por el propietario del TPM

 Usos de TPM
 DRM: Protección de derechos de autor para evitar la piratería.
 Cifrado de archivos y carpetas
 Windows EFS (Sistema de archivos de cifrado)
 Unidad cifrada virtual (unidad segura personal)
 Correo electrónico seguro: Versiones de Outlook, Outlook Express y Netscape Communicator que admiten las características de firma digital y cifrado/descifrado de correo.
 WWW seguro: Versiones de Internet Explorer y Netscape Communicator que admiten protocolos de seguridad (SSL)
 Otros
 Red privada virtual (VPN)
 Contraseña de utilización única (por ejemplo, RSA SecurID)
 Autenticación de clientes

 Notas

 Referencias
