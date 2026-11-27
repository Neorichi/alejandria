---
type: Artículo de enciclopedia
title: Wire (software)
description: Wire es una aplicación de mensajería instantánea, intercambio de archivos, llamadas y videollamadas por Internet con cifrado de extremo a extremo por defecto.
resource: https://es.wikipedia.org/wiki/Wire_(software)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Wire_(software)"}
license: CC BY-SA 4.0
id: eswiki-Wire_(software)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Wire (software)

- **Name:** Wire
- **Desarrollador:** Wire Swiss GmbH
- **Lanzamiento:** 3 de diciembre de 2014
- **Última versión:** 2.26
- **Fecha última versión:** Febrero de 2017
- **Género:** Mensajería instantánea y VoIP
- **Lenguaje programación:** Scala y Rust
- **Sistema operativo:** Multiplataforma
- **Licencia:** Clientes oficiales: GPLv3 Proteus: GPLv3Servidor: AGPL
- **Estado:** Activo

**Wire** es una aplicación de mensajería instantánea, intercambio de archivos, llamadas y videollamadas por Internet con cifrado de extremo a extremo por defecto. El software es multiplataforma, de código abierto, disponible para los sistemas operativos iOS, Android, OS X, Windows, GNU/Linux y navegadores web.

La aplicación es desarrollada por Wire Swiss GmbH, una empresa de software con sede en Zug, Suiza, con el financiamiento del cofundador de Skype Janus Friis. Su centro de operaciones está en Berlín, Alemania.

 Características
La cuenta de usuario puede iniciarse por número telefónico (con mensaje de confirmación) o correo electrónico (con contraseña). Por motivos de privacidad la información no es revelada a desconocidos, siendo obligatorio emplear un alias. Se puede iniciar sesión hasta ocho dispositivos al mismo tiempo.

Wire permite a los usuarios intercambiar texto, voz, foto, vídeo, geolocalización y mensajes de audio. También se comparten archivos hasta 25 MB, y *pings* para avisarlos. Su interfaz es minimalista, enfocada en mensajes, sin cuadros decorativos ni márgenes. Además, los archivos son almacenados localmente y accesibles desde «Colecciones».

Al ser multiplataforma, los mensajes son sincronizados en varios dispositivos a la vez. Además de los mensajes corrientes, es posible programar ciertos mensajes para ser eliminados de forma permanente y difuminados en el historial.

Es capaz de realizar llamadas de audio, llamadas de audio grupal, y videollamadas. Por defecto, la calidad de las llamadas depende de la velocidad de la red.

Además de compartir mensajes, se añaden:
 Animaciones GIFs hasta 5 MB con un catálogo de animaciones integrada de Giphy.
 Bosquejos (en inglés *stecks*), solo en móviles, con fondo en blanco o de una fotografía.
 Previsualización de enlaces en YouTube, Soundcloud, Spotify y Vimeo.
 Grupos de 128 integrantes.

 Contactos
Wire gestiona lista de contactos incluyendo conexiones en común. Se puede acceder desde el directorio del teléfono o buscando a otros, de forma opcional. Cada contacto está identificado por un icono de escudo. La identidad debe estar verificada previamente para alertar una posible suplantación.

 Privacidad
Desde enero de 2017 Wire estableció una política comprensible para todos, con cláusulas para evitar la minería de datos. Para los mensajes, son almacenados por un mes en los servidores llevando indicados de «enviado» y «recibido» al emisor. Para las llamadas, ninguna información es registrada ni compartida a los servidores.

Opcionalmente, el usuario puede colaborar en el funcionamiento y optimización de la plataforma.

 Llamadas VOIP
Inicialmente las llamadas de audio estuvieron disponibles desde 2014. En 2016 se añadió la opción de llamadas de audio grupales hasta diez participantes con cancelación de ruido y «espacio virtual» para auriculares.

Existen dos opciones para codificación de las llamadas: la tasa variable activada por defecto y la tasa constante para mejor calidad implementada en 2017.

 Plataformas

Wire fue lanzado inicialmente para móviles iOS y Android. En 2014 se lanza Wire for Web, para navegadores web modernos. A finales de 2015 se lanza la versión nativa para el sistema operativo Windows. Dicha versión nativa incluye la opción de realizar videocapturas en pantalla. En octubre de 2016 se lanza el cliente para GNU/Linux, en fase experimental, en paquetes de distribución deb.

 Seguridad
Wire emplea una tecnología de transmisión de datos, llamadas de voz y de vídeo, desarrollado por el propio equipo. Además, las comunicaciones son cifradas de la siguiente manera:
 Las llamadas de voz de Wire están codificadas por el algoritmo libre Opus y cifradas con DTLS y SRTP. Para las videollamadas se cifran con RTP y se comunican con el códec WebRTC. Para los metadatos son cifrados entre clientes y autenticadas previamente (implementado en marzo de 2017).
 Para los mensajes, multimedia y archivos se cifran bajo Proteus, que añade una capa adicional de seguridad. Proteus es un protocolo escrito en Rust y adaptado del original Double Ratchet del criptógrafo Trevor Perrin. El intercambio de cifrado es Diffie-Hellman y las claves están bajo el estándar Curve25519.
Hasta marzo de 2017, las llamadas fueron autenticadas con certificados de los servidores.

A finales de 2016 la Universidad de Waterloo, conocida por trabajos de criptografía, realizó su primera revisión de seguridad. En enero de 2017 un usuario, que se identifica como «investigador», reportó una falla en uno de los componentes para verificar contactos. En febrero de ese año las firmas Kudelski Security y X41 D-Sec realizaron una auditoría sin encontrar fallas graves en Proteus. El investigador Katriel Cohn-Gordon, encargado en la revisión, felicitó la transparencia del informe.

 Aplicaciones

 Modelo de negocio
Wire Swiss GmbH recibe dinero de una empresa llamada Iconical. En marzo de 2016, el presidente ejecutivo de Wire, Janus Friis, dijo a *Bloomberg* que la empresa nunca «creará un modelo publicitario» y que «incorporaría características de pago en el futuro». Según un artículo publicado por *Reuters*, Wire Swiss GmbH no reveló cuánto ni con qué se finanza la empresa.

Tras la polémica surgida por Facebook para la explotación comercial de sus servicios, Wire estaría apostando en desarrollar plataformas corporativas sin ánimo de explotarlas. En diciembre del mismo año Alan Duric, director de tecnología de Wire Swiss, confirmó que los servidores serán de código abierto a pesar de que no fue planeado desde el principio.

En abril de 2016 Quiet Riddle Ventures estuvo cerca de demandar a Wire Swiss por usar el protocolo Double Ratcher sin atribuir al autor. Tras el acuerdo entre ambas empresas, el caso fue resuelto.

 Distinciones
El portal web The Next Web incorporó a Wire en la lista de aplicaciones de 2014.

 Véase también

 Privacidad en internet

 Referencias

 Enlaces externos

 Wire en Github
