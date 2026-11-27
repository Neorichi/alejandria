---
type: Artículo de enciclopedia
title: Sistema de detección de intrusos
description: Un sistema de detección de intrusiones (o IDS de sus siglas en inglés intrusion detection system) es un programa de detección de accesos no autorizados a un computador o a una red.
resource: https://es.wikipedia.org/wiki/Sistema_de_detección_de_intrusos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sistema_de_detección_de_intrusos"}
license: CC BY-SA 4.0
id: eswiki-Sistema_de_detección_de_intrusos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sistema de detección de intrusos

Un **sistema de detección de intrusiones** (o **IDS** de sus siglas en inglés *intrusion detection system*) es un programa de detección de accesos no autorizados a un computador o a una red.

El IDS suele tener sensores virtuales (por ejemplo, un sniffer de red) con los que el núcleo del IDS puede obtener datos externos (generalmente sobre el tráfico de red). El IDS detecta, gracias a dichos sensores, las anomalías que pueden ser indicio de la presencia de ataques y falsas alarmas.

 Funcionamiento

El funcionamiento de estas herramientas se basa en el análisis pormenorizado del tráfico de red, el cual al entrar al analizador es comparado con firmas de ataques conocidos, o comportamientos sospechosos, como  puede ser el escaneo de puertos, paquetes malformados, etc. El IDS no solo analiza qué tipo de tráfico es, sino que también revisa el contenido y su comportamiento.

Normalmente esta herramienta se integra con un firewall. El detector de intrusos es incapaz de detener los ataques por sí solo, excepto los que trabajan conjuntamente en un dispositivo de puerta de enlace con funcionalidad de firewall, convirtiéndose en una herramienta muy poderosa ya que se une la inteligencia del IDS y el poder de bloqueo del firewall, al ser el punto donde forzosamente deben pasar los paquetes y pueden ser bloqueados antes de penetrar en la red.

Los IDS suelen disponer de una base de datos de “firmas” de ataques conocidos.

Dichas firmas permiten al IDS distinguir entre el uso normal del PC y el uso fraudulento, y/o entre el tráfico normal de la red y el tráfico que puede ser resultado de un ataque o intento del mismo.

 Tipos de IDS

Actualmente, existen muchos Sistemas de Detección de Intrusiones (IDS),
que van desde sistemas antivirus hasta sistemas jerárquicos
 **HIDS** (*HostIDS*): el principio de funcionamiento de un HIDS, depende del éxito de los intrusos, que generalmente dejaran rastros de sus actividades en el equipo atacado, cuando intentan adueñarse del mismo, con propósito de llevar a cabo otras actividades. El HIDS intenta detectar tales modificaciones en el equipo afectado, y hacer un reporte de sus conclusiones.
 **NIDS** (*NetworkIDS*): un IDS basado en red, detectando ataques a todo el segmento de la red. Su interfaz debe funcionar en modo promiscuo capturando así todo el tráfico de la red.
 **IDS basados en firmas** : Los IDS basados en firmas supervisan todos los paquetes de la red y los comparan con la base de datos de firmas, que son patrones de ataque preconfigurados y predeterminados. Funcionan de forma similar al software antivirus.
**IDS basados en anomalías** : Estos IDS monitorean el tráfico de red y lo comparan con una línea de base establecida. La línea base determina lo que se considera normal para la red en términos de ancho de banda, protocolos, puertos y otros dispositivos, y el IDS alerta al administrador de todo tipo de actividad inusual.
**IDS Pasivo** : Este sistema IDS realiza el sencillo trabajo de detección y alerta. Simplemente alerta al administrador de cualquier tipo de amenaza y bloquea la actividad en cuestión como medida preventiva.
**Identificación reactiva** : detecta actividad malintencionada, alerta al administrador de las amenazas y también responde a esas amenazas.

 Sistemas pasivos y sistemas reactivos

En un sistema pasivo, el sensor detecta una posible intrusión, almacena la información y manda una señal de alerta que se almacena en una base de datos. En un sistema reactivo, el IDS responde a la actividad sospechosa reprogramando el cortafuegos para que bloquee tráfico que proviene de la red del atacante. Un sistema que reacciona ante el ataque previniendo que este continúe, se denomina IPS por sus siglas en inglés de "intrusion prevention system".

 Comparación con Cortafuegos
Si bien ambos están relacionados con seguridad en redes de información, un IDS, difiere de un cortafuegos, en que este último generalmente examina exteriormente por intrusiones para evitar que estas ocurran. Un cortafuegos limita el acceso entre redes, para prevenir una intrusión, pero no determina un ataque que pueda estar ocurriendo internamente en la red. Un IDS, evalúa una intrusión cuando esta toma lugar, y genera una alarma. Un IDS además observa ataques que se originan dentro del sistema. Este normalmente se consigue examinando comunicaciones, e identificando mediante heurística, o patrones (conocidos como firmas), ataques comunes ya clasificados, y toma una acción para alertar a un operador. Los sistemas de detección de intrusiones son fundamentales para proteger adecuadamente en el perímetro de la red, muy cerca del cortafuegos, ya que trabajan conjuntamente para impedir que usuarios malintencionados puedan acceder a una organización.

 Mecanismos de detección de un ataque

Un IDS usa alguna de las dos siguientes técnicas para determinar que un ataque se encuentra en curso:
 Patrón
Un IDS basado en patrones, analiza paquetes en la red, y los compara con patrones de ataques conocidos, y preconfigurados. Estos patrones se denominan firmas. Debido a esta técnica, existe un periodo de tiempo entre el descubrimiento del ataque y su patrón, hasta que este es finalmente configurado en un IDS. Durante este tiempo, el IDS será incapaz de identificar el ataque.

 Heurística
Un IDS basado en heurística, determina actividad normal de red, como el orden de ancho de banda usado, protocolos, puertos y dispositivos que generalmente se interconectan, y alerta a un administrador o usuario cuando este varía de aquel considerado como normal, clasificándolo como anómalo.

 Implementación

Para poner en funcionamiento, un sistema de detección de intrusos se debe tener en cuenta que es posible optar por una solución hardware, software o incluso una combinación de estos dos. La posibilidad de introducir un elemento hardware es debido al alto requerimiento de procesador en redes con mucho tráfico. A su vez los registros de firmas y las bases de datos con los posibles ataques necesitan gran cantidad de memoria, aspecto a tener en cuenta.

En redes es necesario considerar el lugar de colocación del IDS. Si la red está segmentada con hub (capa 1 del modelo OSI) no hay problema en analizar todo el tráfico de la red realizando una conexión a cualquier puerto. En cambio, si se utiliza un switch (capa 2 del modelo OSI), es necesario conectar el IDS a un puerto SPAN (Switch Port Analiser) para poder analizar todo el tráfico de esta red.

 Véase también
 Detección de anomalías
 Seguridad informática
 HIDS
 NIDS

 Referencias

 Enlaces externos
 Snort, OpenSource IDS/IPS
 Sistemas de Detección de Intrusiones , CriptoRed UPM, 2003
