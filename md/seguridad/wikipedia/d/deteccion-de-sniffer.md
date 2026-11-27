---
type: Artículo de enciclopedia
title: Detección de sniffer
description: Un sniffer es un programa informático que registra la información que envían los periféricos, así como la actividad realizada en un determinado ordenador.
resource: https://es.wikipedia.org/wiki/Detección_de_sniffer
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Detección_de_sniffer"}
license: CC BY-SA 4.0
id: eswiki-Detección_de_sniffer
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Detección de sniffer

Un **sniffer** es un programa informático que registra la información que envían los periféricos, así como la actividad realizada en un determinado ordenador.

 Riesgos

Supone una amenaza grave para la seguridad no sólo de una máquina sino también de toda una red. Gran cantidad de tráfico confidencial viaja en claro, sin ningún tipo de cifrado, por las redes de la mayoría de las empresas. Ese es el entorno ideal para un sniffer, que puede acceder de forma transparente a esa información, y permitir que alguien abuse de su conocimiento. Por eso es muy importante realizar búsquedas periódicas de sniffers dentro de las redes de cualquier empresa, no solo por el daño que puedan causar, sino también porque encontrarlos es señal de que se ha producido y explotado una grave brecha y hay que tomar medidas inmediatas.

Existen casos en los que un sniffer no es peligroso. A veces, explorando una red en busca de sniffers se detectará que hay algunos, por ejemplo, en máquinas que dependen del departamento de administración de redes. Esto puede ocurrir porque, en realidad, un sniffer no se diferencia demasiado de una herramienta de observación y diagnosis del tráfico de red que puede estar siendo legítimamente utilizada por personal encargado de la administración de la red. Otros dispositivos, especialmente routers y hub, suelen producir falsos positivos que hay que tener en cuenta .

 Búsqueda de sniffers

Existen diferentes aproximaciones al problema de cómo detectar un sniffer, y que éstas varían según se tenga acceso local a la máquina, o bien haya que descubrirlos desde alguna máquina remota. El objetivo que la mayoría de pruebas tratan de conseguir es que la máquina que tiene la tarjeta de red en modo promiscuo se traicione a sí misma, revelando que ha tenido acceso a información que no iba dirigida a ella y que, por tanto, tiene un sniffer. Éste es un objetivo ambicioso y complejo que puede resultar imposible.

A veces resulta completamente imposible detectar un sniffer. Por ejemplo, si el sniffer ha sido diseñado exclusivamente para esta tarea (generalmente dispositivos hardware), entonces no devolverá jamás un paquete, no establecerá nunca una comunicación, sino que permanecerá siempre en silencio y su detección remota será, simplemente, imposible. La detección de este tipo de sniffers sólo puede hacerse por inspección directa de los dispositivos conectados a la red.

 Técnicas de detección local

Aunque no se trata de una tarea trivial, ésta es, con mucho, la situación en que resulta más sencillo localizar un sniffer. Normalmente basta con revisar la lista de programas en ejecución para detectar alguna anomalía (CTRL+ALT+SUPR o ps -aux|more). Otro buen sitio donde mirar es en la lista de los programas que se inician automáticamente al encender el PC archivos /etc/rc.d/rcX.d/* o.bashrc, etc. en un sistema Unix y autoexec.bat o ciertas claves del Registry en una máquina Windows) o las tareas programadas (cron, at).

En una máquina con alguno de los sistemas operativos de la familia Unix se dispone de una utilidad que resulta especialmente valiosa en la lucha contra los sniffers. Se trata de ifconfig, orden que informa del estado de todas las interfaces de red del sistema e indica si alguna de ellas se encuentra en modo promiscuo. Esta metodología de detección local de sniffers depende del buen funcionamiento de la orden ifconfig.

Es importante destacar que los ejemplos anteriores son sólo triviales y no pretenden ser una enumeración exhaustiva. Hay decenas de posibilidades, algunas muy ingeniosas y nada elementales. Cualquier novedad o anomalía debe ser investigada en profundidad porque podría revelar no sólo un sniffer en funcionamiento sino también otros programas que supongan una grave amenaza (virus, troyanos, gusanos, etc.).

 Técnicas de detección remota desde el mismo segmento de red

Es en este entorno donde más frecuentemente el administrador de seguridad tiene que realizar su
investigación. Existe un cierto número de técnicas heurísticas que son de utilidad y que se presentan a continuación, pero hay que tener claro que estas técnicas tienen bastantes limitaciones y que no resulta en absoluto improbable que exista un sniffer en la red y que no sea detectado (falso negativo) o que máquinas o usuarios completamente inocentes sean detectados como sniffers (falsos positivos). Por su ámbito de aplicación, estas técnicas se pueden dividir en dos grupos: las dependientes del sistema operativo y las que no lo son.

*Dependientes del sistema operativo*.
Como su propio nombre indica, estas técnicas usan algún fallo o característica propia de determinados sistemas operativos (o parte de ellos, como el subsistema TCP/IP) para reconocer a una tarjeta de red en modo promiscuo. La ventaja que tienen es su excelente rendimiento cuando se exploran máquinas que tienen justamente la versión del sistema operativo del que la técnica obtiene partido. La desventaja fundamental es el gran número de falsos negativos que ocasiona debido a que en muchos casos las implementaciones de la pila TCP/IP varían entre versiones del mismo sistema operativo con la acción a nivel físico, es volver a inspeccionar la MAC (MAC address) de destino, aunque también se puede hacer a nivel de IP.

*No dependientes del sistema operativo*.
En general son menos fiables y menos concluyentes.
Suelen basarse en suposiciones sobre el comportamiento de determinados sniffers, que pueden no darse en casos concretos, convirtiendo alguna de estas técnicas en completamente inútiles. Otras son más generales, pero poco resolutivas, porque no clasifican, simplemente dan indicios que en muchos casos no son suficientes. No suelen proporcionar muchos falsos positivos, aunque pueden ser burladas y utilizadas para inculpar a terceras personas. Tampoco falsos negativos, aunque la última generación de sniffers ya incorpora técnicas de evasión bastante sofisticadas que evita su detección.

 Herramientas de detección remota desde el mismo segmento de red

La mejor herramienta de detección de sniffers en la actualidad es AntiSniff, de L0pht. Se trata de un programa comercial con una versión de evaluación de 15 días que implementa todos los tests citados anteriormente, junto a algunas variaciones muy interesantes. Sin embargo, al poco de anunciarse su aparición se desarrolló un sniffer gratuito y con código fuente disponible llamado Anti-AntiSniff que no es detectado por ninguno de los test que AntiSniff realiza. AntiSniff está disponible para Windows NT/2000 y hay una versión de prueba gratuita y con código fuente disponible en desarrollo para diferentes versiones de Unix que, eso sí, está muy por detrás de la versión de Windows NT/2000 en cuanto a interfaz gráfica.

Le sigue, en cuanto a utilidad y no precisamente de cerca, el proyecto Sentinel, que tiene la ventaja de ser un proyecto público y abierto que permite acceder al código fuente del programa. En la actualidad es sólo capaz de realizar unos pocos tests, muchos menos que AntiSniff, pero tiene un interesante futuro por delante que hace recomendable su seguimiento.

 Véase también
 Packet sniffer
 Trama de red
 Topología de red
 Unshielded twisted pair (UTP)
 Shielded twisted pair (STP)
 Conmutador
 Concentrador
 WiFi

 Test de Detección de Sniffer

 Referencias

 Enlaces externos
 Packet Sniffer Detection with AntiSniff (en inglés)
 Guía breve de detección de sniffers en una red
