---
type: Artículo de enciclopedia
title: Ataque DROWN
description: "El ataque DROWN es una falla de seguridad de protocolos cruzados que afecta a servidores criptográficos que soportan la pila de protocolos TLS al utilizar su soporte para el protocolo inseguro SSLv2 y atacar así las …"
resource: https://es.wikipedia.org/wiki/Ataque_DROWN
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_DROWN"}
license: CC BY-SA 4.0
id: eswiki-Ataque_DROWN
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque DROWN

El **ataque DROWN** es una falla de seguridad de protocolos cruzados que afecta a servidores criptográficos que soportan la pila de protocolos TLS al utilizar su soporte para el protocolo inseguro SSLv2 y atacar así las conexiones que utilizan protocolos actualizados sin fallas de seguridad conocidas. DROWN puede afectar todos los tipos de servidores que ofrezcan servicios encriptados con TLS y que todavía ofrezcan soporte a SSLv2 y compartan las credenciales de clave pública entre los dos protocolos.

En marzo de 2016 se hicieron públicos los detalles de los ataque DROWN junto con correcciones que permiten evitar este ataque; la vulnerabilidad recibió el código CVE CVE-2016-0800. Fue descubierto por investigadores de varias universidades como la de Universidad de Tel Aviv, Universidad de Ciencias Aplicadas de Munster, Universidad de Ruhr en Bochum y Universidad de Pensilvania.

 Detalles
Transport Layer Security (TLS) es el protocolo de seguridad más importante en Internet. Casi todas las transacciones que se realizan en Internet lo hacen usando TLS (en sus versiones 1.0, 1.1, 1.2 o 1.3), de forma que los potenciales afectados por una debilidad en este protocolo son prácticamente todos los usuarios de Internet.

Inicialmente TLS se llamaba SSL y la primera versión pública fue SSL 2.0 que data de los años 1990. Debido a las regulaciones de exportación en los Estados Unidos sobre productos de software de seguridad, Al protocolo SSL se le agregó la compatibilidad con algoritmos de encriptamiento débiles.

Por mucho tiempo, los navegadores web tuvieron a SSL 2.0 como protocolo secundario, lo que permitía realizar ataques forzando al navegador a usar su protocolo secundario. Afortunadamente, esta compatibilidad con el pasado fue eliminada de los navegadores modernos.

Del lado de los servidores, la compatibilidad con SSL 2.0 también fue eliminada, pero hoy en día persisten servidores que no han sido actualizados en años y que son vulnerables al ataque DROWN.

En el caso de los servidores que utilizan el software OpenSSL la configuración supuestamente deshabilita por defecto el uso del protocolo SSL 2.0 pero los investigadores que descubrieron el ataque DROWN, se dieron cuenta de que, a pesar de la configuración, era posible que un cliente se comunicara con un servidor OpenSSL usando cifrado proveniente de SSL 2.0.

DROWN son las siglas de  "Decrypting RSA with Obsolete and Weakened eNcryption" (Desencriptado de RSA con encriptado débil obsoleto). Esta debilidad no está asociada a un error de implementación concreto sino más bien explota una vulnerabilidad que surge al combinar el uso de protocolos. Según sus descubridores, el ataque no puede arreglarse haciendo cambios en los clientes del protocolo, es decir, en los navegadores de web.

 Atenuación
Se puede deshabilitar el soporte al protocolo SSLv2 en el servidor, y de esta forma negar el acceso atacante a su criptografía débil. Este cambio es suficiente para prevenir ataques DROWN.

El grupo OpenSSL publicó un aviso de seguridad, y un conjunto de modificaciones que deberán mitigar la vulnerabilidad eliminando el soporte a protocolos y algoritmos de cifrado obsoletos. Junto con esta, las modificaciones corrigen otras vulnerabilidades.

Es aconsejable corregir la vulnerabilidad tan pronto como sea posible en cada equipo instalado.

 Referencias
