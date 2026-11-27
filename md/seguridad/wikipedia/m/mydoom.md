---
type: Artículo de enciclopedia
title: MyDoom
description: "Mydoom, también conocido como el gusano de correo victorius y \"Shimgapi\", es un gusano informático que afecta a Microsoft Windows."
resource: https://es.wikipedia.org/wiki/MyDoom
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/MyDoom"}
license: CC BY-SA 4.0
id: eswiki-MyDoom
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# MyDoom

**Mydoom**, también conocido como el gusano de correo victorius y *"Shimgapi"*, es un gusano informático que afecta a Microsoft Windows. Fue visto por primera vez el 26 de enero de 2004. Se convirtió en el gusano de correo electrónico que más rápido se propagó (a partir de enero de 2004), superando los registros anteriores establecidos por el gusano Sobig y ILoveYou, un récord que a 2025 aún no se ha superado.

Mydoom parece haber sido encargado por *spammers* de correo electrónico para enviar correo basura a través de ordenadores infectados. El gusano contiene el mensaje de texto "Andy, estoy haciendo mi trabajo, nada personal, lo siento", lo que lleva a muchos a creer que al creador del gusano se le pagó por esto. Al principio, varias empresas de seguridad expresaron su creencia de que el gusano se originó a partir de un programador en Rusia. Se desconoce el autor real del gusano.

La anticipada cobertura especulativa sostenía que el único propósito del gusano era perpetrar un ataque distribuido de denegación de servicio contra SCO Group. El 25 por ciento de los hosts infectados de Mydoom.A atacaron a www.sco.com con una inundación de tráfico. Las conjeturas de la prensa especializada, impulsadas por las propias afirmaciones de SCO Group, sostenían que esto significaba que el gusano fue creado por un partidario de Linux o de código abierto en represalia por las polémicas acciones y declaraciones públicas de SCO Group contra Linux. Esta teoría fue rechazada inmediatamente por los investigadores de seguridad. Desde entonces, también ha sido rechazada por los agentes de la ley que investigan el virus, el cual atribuyen a bandas organizadas de delincuencia en línea.

El análisis inicial de Mydoom sugirió que se trataba de una variante del gusano Mimail, de ahí el nombre alternativo MiMail.R, lo que provocó la especulación de que las mismas personas eran responsables de ambos gusanos. Los análisis posteriores fueron menos concluyentes en cuanto al vínculo entre los dos gusanos.

Mydoom fue nombrado por Craig Schmugar, un empleado de la firma de seguridad informática McAfee y uno de los primeros descubridores del gusano. Schmugar eligió el nombre después de notar el texto "mydom" dentro de una línea del código del programa. Señaló: "Era evidente desde el principio que esto sería muy grande. Pensé que tener 'Doom' en el nombre sería apropiado."

Descripción técnica general
Mydoom se transmite principalmente por correo electrónico, apareciendo como un error de transmisión, con líneas de asunto como "Error", "Sistema de entrega de correo", "Prueba" o "Error de transacción de correo" en diferentes idiomas, incluyendo inglés y francés. El correo contiene un archivo adjunto que, si se ejecuta, reenvía el gusano a las direcciones de correo electrónico que se encuentran en archivos locales, tales como la libreta de direcciones del usuario. También se copia a la "carpeta compartida" de la aplicación de intercambio de archivos P2P KaZaA en un intento de propagarse de esa manera.

Mydoom evita apuntar direcciones de correo electrónico en ciertas universidades, como la de Rutgers, MIT, Stanford y la Universidad de California en Berkeley, así como ciertas empresas como Microsoft y Symantec. Algunos de los primeros informes afirmaron que el gusano evita todas las direcciones .edu, pero este no es el caso.

La versión original, **Mydoom.A**, describe como llevar dos cargas útiles:

Una puerta trasera en el puerto 3127/tcp para permitir el control remoto de la PC subvertida (poniendo su propio archivo SHIMGAPI.DLL en el directorio system32 y lanzándolo como un proceso secundario del Explorador de Windows); esta es esencialmente la misma puerta trasera utilizada por Mimail.
Un ataque de denegación de servicio contra el sitio web de la compañía SCO Group, programada para comenzar 1 de febrero de 2004. Muchos analistas de virus dudaban de si esta carga útil funcionaría realmente. Pruebas posteriores sugieren que funciona en solo el 25% de los sistemas infectados.

Una segunda versión, **Mydoom.B**, además de llevar las cargas originales, también se dirige a la página web de Microsoft y bloquea el acceso a los sitios de Microsoft y a los populares sitios de antivirus en línea, modificando el archivo hosts, bloqueando así las herramientas de eliminación de virus o actualizaciones de software antivirus. El bajo número de copias de esta versión en circulación significó que los servidores de Microsoft sufrieran pocos efectos negativos.

Línea de tiempo
**26 de enero de 2004:** El virus Mydoom se identifica por primera vez alrededor de las 8 EST (13:00 GMT), justo antes del comienzo de la jornada de trabajo en América del Norte. Los primeros mensajes provienen de Rusia. Durante un período de unas pocas horas al mediodía, la rápida propagación del gusano reduce el rendimiento general de Internet en aproximadamente un 10% y los tiempos promedio de carga de página web en aproximadamente el 50%. Las empresas de seguridad informática informan que Mydoom es responsable de aproximadamente uno de cada diez mensajes de correo electrónico en este momento. Aunque el ataque de denegación de servicio de Mydoom estaba programado para comenzar el 1 de febrero de 2004, el sitio web de SCO Group se desconectó brevemente en las horas posteriores al lanzamiento del gusano. No está claro si Mydoom fue el responsable de esto. SCO Group afirmó que fue el objetivo de varios ataques distribuidos de denegación de servicio en 2003 que no estaban relacionados con virus informáticos.
**27 de enero:** SCO Group ofrece 250.000 dólares de recompensa por información que conduzca a la detención del autor del gusano. En los EE. UU., el FBI y el Servicio Secreto comienzan las investigaciones sobre el gusano.
**28 de enero:** Se descubre una segunda versión del gusano dos días después del ataque inicial. Los primeros mensajes enviados por Mydoom.B se identifican en torno a las 14:00 UTC y también parecen originarios de Rusia. La nueva versión incluye el ataque original de denegación de servicio contra SCO Group y un ataque idéntico dirigido a Microsoft.com a partir del 3 de febrero de 2004 ; Sin embargo, se sospecha que ambos ataques están rotos, código de señuelo no funcional destinado a ocultar la función de puerta trasera de Mydoom. Mydoom.B también bloquea el acceso a los sitios web de más de 60 compañías de seguridad informática, así como anuncios pop-up proporcionados por DoubleClick y otras empresas de marketing en línea.
**29 de enero:** La propagación de Mydoom comienza a disminuir a medida que los errores en el código de Mydoom.B prevenían que se propagase tan rápidamente como se previó. Microsoft ofrece 250.000 dólares de recompensa por información que conduzca a la detención del creador de Mydoom.B.
**1 de febrero de 2004:** Se calcula que un millón de ordenadores de todo el mundo infectados por Mydoom comienzan el ataque masivo de denegación de servicio distribuido, el ataque más grande hasta la fecha. A medida que el 1 de febrero llega al este de Asia y Australia, SCO elimina www.sco.com del DNS alrededor de las 17:00 UTC del 31 de enero. Todavía no hay confirmación independiente de hecho de www.sco.com sufriendo los DDoS planificados.
**3 de febrero:** El ataque distribuido de denegación de servicio de Mydoom.B en Microsoft  comienza, para lo cual Microsoft se prepara ofreciendo un sitio web que no se verá afectado por el gusano, information.microsoft.com. Sin embargo, el impacto del ataque sigue siendo mínimo y www.microsoft.com sigue siendo funcional. Esto se atribuye a la distribución comparativamente baja de la variante Mydoom.B, la alta tolerancia de carga de los servidores web de Microsoft y las precauciones tomadas por la empresa. Algunos expertos señalan que la carga es menor que la de las actualizaciones de software de Microsoft y otros servicios basados en la Web.
**9 de febrero:** Doomjuice, un gusano "parásito", comienza a extenderse. Este gusano utiliza la puerta trasera dejada por Mydoom para propagarse. No ataca equipos no infectados. Su carga útil similar a una de las de Mydoom.B, es un ataque de denegación de servicio contra Microsoft.
**12 de febrero:** Mydoom.A está programado para detener la propagación. Sin embargo, la puerta trasera permanece abierta después de esta fecha.
**1 de marzo:** Mydoom.B está programado para detener su propagación; Al igual que con Mydoom.A, la puerta trasera permanece abierta.
**26 de julio:** Una variante de Mydoom ataca a Google, AltaVista y Lycos, deteniendo por completo la función del popular motor de búsqueda de Google durante la mayor parte de la jornada laboral, y creando lentitudes en los motores AltaVista y Lycos durante horas.
**10 de septiembre:** Las versiones MyDoom U, V, W y X aparecen, lo que despierta la preocupación de que se esté preparando un MyDoom nuevo y más potente.
**18 de febrero de 2005:** aparece la versión de MyDoom AO.
**Julio de 2009:** MyDoom resurge en julio de 2009 los ataques cibernéticos que afectan a Corea del Sur y los Estados Unidos renombrandose Sadurum mixto.

Enlaces externos
 Los ataques DDoS y MyDoom

 SCO Ofertas Recompensa por la detención y condena de Mydoom Virus Autor - comunicado de prensa de la OCS, de 27 de enero de 2004. Tenga en cuenta la afirmación de que el ataque de denegación de servicio que ya había comenzado en esta fecha.

 Información sobre el gusano Mydoom de Symantec.com

Referencias
