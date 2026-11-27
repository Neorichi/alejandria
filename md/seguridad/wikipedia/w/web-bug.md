---
type: Artículo de enciclopedia
title: Web bug
description: "En informática, un web bug (también llamado baliza web, faro web por el término inglés web beacon o también como GIF invisible) suelen ser pequeñas imágenes de un pixel por un pixel, generalmente invisibles, colocadas …"
resource: https://es.wikipedia.org/wiki/Web_bug
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Web_bug"}
license: CC BY-SA 4.0
id: eswiki-Web_bug
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Web bug

En informática, un **web bug** (también llamado **baliza web**, **faro web** por el término inglés *web beacon* o también como **GIF invisible**) suelen ser pequeñas imágenes de un pixel por un pixel, generalmente invisibles, colocadas en el código fuente de las páginas web de un sitio o en un mensaje de correo electrónico que se diseña para vigilar a quién lo lee. Los web *beacons* suelen utilizarse con el fin de medir el tráfico de usuarios que visitan una página web y así poder obtener  un patrón de los usuarios de un sitio dado. Normalmente, estos se utilizan para realizar un análisis web. Los web *beacons* son elementos HTML invisibles que rastrean las vistas de una página web. Al volver el usuario a la página web, estos beacons se conectan a cookies establecidas por el servidor, facilitando el seguimiento no revelado de usuarios.

Su tamaño es inapreciable, pudiendo ser un único píxel en formato GIF e  invisible, estos representan mediante etiquetas HTML y pueden incluir código JavaScript.

El término *web bug* proviene del inglés *bugging device*, es decir micrófono oculto o «cucaracha» (*bug* significa «insecto»).

 Resumen
Un web *bug* es cualquiera de una serie de técnicas que se utilizan para realizar el seguimiento en una página web o correo electrónico que está leyendo, cuándo y desde qué computadora. También pueden ser utilizados para determinar si un correo electrónico se ha leído o enviado a otra persona, o si una página web se ha copiado en otro sitio web.

Algunos mensajes de correo electrónico y las páginas web no son totalmente independientes del entorno. Pueden referirse al contenido en otro servidor, en lugar de incluir el contenido directamente. Cuando un cliente de correo electrónico o un navegador web prepara la visualización de un correo electrónico o página web, normalmente envía una petición al servidor para enviar el contenido adicional.

Estas peticiones suelen incluir la dirección IP del ordenador solicitante, la hora en la que se solicitó al contenido, el programa que hace la solicitud y la existencia de las cookies previamente establecidas por ese servidor. El servidor puede almacenar toda esta información y asociarla con una ficha de seguimiento único adjunto a la solicitud de contenido.

 Seguridad
Aunque el uso que se hace de los web bug normalmente es con fines de análisis web, estas y otras referencias pueden utilizarse con diferentes fines, incluyendo ataques al usuario (abusándose de vulnerabilidades conocidas de los programas que utiliza), confirmación de direcciones electrónicas (para envío masivo de spam o para comercialización de bases de direcciones confirmadas), etc.

Para evitar esto, se deben utilizar o configurar los distintos programas clientes adecuadamente para que ofrezcan un nivel de seguridad correcto.

 Detección
Al estar (normalmente) implementados como etiquetas HTML, aunque no sean notorios a simple vista, pueden ser detectados revisando la presencia de imágenes en el código fuente de la página o mensaje.

 Web bugs en páginas web
Los web bugs suelen ser utilizados por terceros para controlar la actividad de los clientes en un sitio.

Se puede decir que no necesariamente un web bug tiene que ser siempre invisible en una página, ya que cualquier gráfico en una página web que se utiliza para controlar propósitos se puede considerar un web bug. Tampoco quiere decirse que todas las imágenes invisibles GIF sean web bugs, ya que estas se utilizan también para propósitos de maquetado y alineación en las páginas web (cada vez menos utilizadas).

Como ejemplo de la forma en que web bugs pueden hacer el registro de usuario más fácil, considere una empresa propietaria de una red de sitios. Esta empresa puede tener una red que requiere que todas las imágenes se almacenen en un ordenador sitio mientras las propias páginas se almacenan en otro lugar. Podrían utilizar web bugs con el fin de contar y reconocer a los usuarios que viajan en torno a los diferentes servidores de la red. En lugar de recopilar estadísticas y gestionar las cookies de todos sus servidores por separado, se pueden utilizar los web bugs para mantenerlas unidas.

El seguimiento en las páginas web puede desactivarse mediante una serie de técnicas:
 Desactivar las cookies del navegador puede evitar algunos web bugs de seguimiento de la actividad específica de un cliente. Los registros del sitio web podrán seguir una petición de una página desde la dirección IP del cliente, pero la información única relacionada con una cookie no podrá ser registrada. Sin embargo, las técnicas del servidor de un sitio web que no utilizan cookies se pueden utilizar para ayudar a rastrear a los usuarios que bloqueen cookies de un sitio. Por ejemplo, un sitio web puede identificar una solicitud de un nuevo visitante y enviar esos enlaces visitantes que pasan por un ID único con el parámetro GET.
 Se pueden utilizar add-ons y extensiones del navegador. Por ejemplo, el complemento Ghostery analiza JavaScript para detectar rastreadores, web bugs, píxeles y balizas.

 Web bugs en mensajes de correo electrónico
Un web bug se puede utilizar para averiguar si un mensaje de correo electrónico en particular ha sido leído por alguien y, si es el caso, cuándo se leyó el mensaje, entre otras referencias ya mencionadas.

Los web bugs se utilizan con frecuencia en el marketing por correo electrónico como una forma de determinar que los destinatarios abren el correo electrónico. Hacer esto permite que los comerciantes sepan que se ha visto la promoción o anuncio que han enviado. Normalmente, la URL de las imágenes contenidas en los correos electrónicos tiene un identificador único, que sirve para identificar al usuario y para determinar cuando el usuario ha leído el correo.

El emisor del correo electrónico es así capaz de grabar el momento exacto en el que es leído y la dirección IP del ordenador o el servidor proxy a través del cual estaba conectado. De esta manera el emisor obtiene información detallada sobre cuándo y dónde lee cada receptor el correo electrónico. Cada vez que se muestra el mensaje en la pantalla del usuario, se solicitan de nuevo los datos de la imagen (y puede registrarse cada lectura).

Algunos web bugs de seguimiento de correo electrónico se pueden desactivar a través de:
 Desactivar la visualización en formato HTML y mostrar solo el texto.
 Desactivar la visualización de imágenes externas sin dejar de utilizar HTML.

 Analizadores de accesos al servidor

Cada vez que se visita una página web de cualquier servidor, esto queda registrado en un archivo llamado access.log. De los visitantes se obtiene datos como:

 Países de origen.
 Secciones más visitadas.
 Tiempo de permanencia en cada sección.
 Información del sistema operativo.
 Tipo de ordenador.
 Tipo de navegador.
 Palabras utilizadas en la búsqueda.

Analizar esta información permite realizar una correcta estrategia de marketing. Se puede utilizar un analizador de estadísticas como el de *ActiveISP*.

 Véase también
 Privacidad en Internet
 Análisis web
 Cookie Flash
 Clear.gif
 Enlaces externos
 The Web Bug FAQ de la Fundación Fronteras Electrónicas (en inglés).

 Referencias
