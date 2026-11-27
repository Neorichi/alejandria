---
type: Artículo de enciclopedia
title: TorChat
description: TorChat es un servicio de mensajería instantánea descentralizado y anónimo que utiliza los servicios ocultos como su red subyacente.
resource: https://es.wikipedia.org/wiki/TorChat
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/TorChat"}
license: CC BY-SA 4.0
id: eswiki-TorChat
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# TorChat

- **Nombre:** TorChat
- **Desarrollador:** TorChat Developers
- **Licencia:** GPL v3
- **Ultima version:** 2.0-alpha-14
- **Fecha ultima version:** 22nd of July, 2012
- **Lenguaje programación:** Object Pascal
- **Sistema operativo:** Linux, Microsoft Windows
- **Idioma:** Multilingual

**TorChat** es un servicio de mensajería instantánea descentralizado y anónimo que utiliza los servicios ocultos como su red subyacente. Proporciona mensajes de texto y transferencias de archivos criptográficamente seguros. Las características de los servicios ocultos de Tor aseguran que todo el tráfico entre los clientes está encriptado y que es muy difícil saber quién se está comunicando con quién y dónde se encuentra físicamente un cliente determinado.

TorChat es software libre licenciado bajo los términos de la Licencia Pública General de GNU (GPL).

 Características
En TorChat cada usuario tiene una identificación alfanumérica única que consiste en 16 caracteres. Este ID será creado aleatoriamente por Tor cuando el cliente es iniciado la primera vez, es básicamente la dirección .onion de un servicio onion. Los clientes de TorChat se comunican entre ellos usando Tor para contactar con el servicio de cebolla del otro (derivado de su ID) e intercambiando información de estado, mensajes de chat y otros datos a través de esta conexión. Dado que los servicios ocultos pueden recibir conexiones entrantes incluso si están detrás de un enrutador haciendo traducción de direcciones de red (NAT), TorChat no necesita ningún reenvío de puertos para funcionar.

 Historia
La primera versión pública de TorChat fue lanzada en noviembre de 2007 por Bernd Kreuss. Está escrita en Python y utiliza el conjunto de herramientas de widgets multiplataforma wxPython, que permite soportar una amplia gama de plataformas y sistemas operativos.

Las versiones antiguas de Windows de TorChat fueron construidas con py2exe (desde la versión 0.9.9.292 reemplazada por pyinstaller) y venían con una copia de Tor fácilmente configurada para que pudiera ser ejecutada como una aplicación portátil desde una unidad flash USB sin ninguna instalación, configuración o creación de cuentas.

Entre 2008 y 2010 no hubo ningún paquete actualizado, , lo que provocó que la versión empaquetada de Tor se volviera obsoleta e incapaz de conectarse a la red Tor, lo que fue la razón de la aparición de los forks que básicamente sólo reemplazaron el Tor.exe empaquetado con uno actual. En diciembre de 2010, finalmente se hizo disponible una actualización oficial que, entre algunas correcciones de errores menores, también incluía de nuevo un Tor.exe actualizado.

 Forks
Un desarrollador francés lanzó un fork para OS X en el verano de 2010. El binario (una aplicación de Cocoa) y el código fuente (Objective-C) que se incluyen en un proyecto Xcode 7 pueden descargarse en SourceMac.

A principios de 2012 se creó una reescritura del protocolo TorChat en Java, llamada jTorChat en Google Code. Su objetivo es emular todas las características del protocolo TorChat original, así como extender los protocolos para las características específicas de jTorChat. El intercambio de archivos, si bien está implementado en el TorChat original, aún no está implementado en jTorChat. Una nueva capacidad de jTorChat es el modo de difusión, que permite al usuario enviar mensajes a todos los miembros de la red, aunque no estén en su lista de contactos. También se ha implementado el modo de solicitud de amigos, que permite a un usuario solicitar a un usuario aleatorio de la red de jTorChat que los añada. En esta etapa jTorChat está diseñado para trabajar efectivamente en Windows sin ninguna configuración, sin embargo, como está escrito en Java, puede funcionar en cualquier plataforma soportada tanto por Tor como por el propio Java, lo que lo hace muy portátil. El proyecto está buscando activamente colaboradores de Java, especialmente para ayudar a depurar la interfaz gráfica.

A partir del 5 de febrero de 2013, el desarrollador Prof7bit trasladó TorChat a GitHub, como protesta contra la censura selectiva por parte de Google del acceso a la descarga de TorChat a determinados países. Prof7bit se ha cambiado a trabajar en torchat2, que es una reescritura desde cero, usando Lazarus y Free Pascal.

 Seguridad
En 2015 se llevó a cabo un análisis de seguridad del protocolo TorChat y su aplicación en escrita en Python.
Se constató que, aunque el diseño del TorChat es sólido, su aplicación tiene varios defectos, que hacen que los usuarios del TorChat sean vulnerables a los ataques de suplantación, confirmación de comunicaciones y denegación de servicio. A pesar de las fallas encontradas, el uso del TorChat podría seguir siendo seguro en un escenario en que la dirección de la cebolla del par no sea conocida por un adversario interesado en atacar a la persona que está detrás de la dirección del TorChat.

 Véase también

 Bitmessage
 Tor (Red de anonimato)
 Ricochet (Software)
 Tox

 Referencias

 Enlaces externos

 TorChat Para Mac OS X
