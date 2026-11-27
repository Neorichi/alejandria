---
type: Artículo de enciclopedia
title: Sistema de prevención de intrusos
description: Un sistema de prevención de intrusos (o por sus siglas en inglés IPS) es un software que ejerce el control de acceso en una red informática para proteger a los sistemas computacionales de ataques y abusos.
resource: https://es.wikipedia.org/wiki/Sistema_de_prevención_de_intrusos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sistema_de_prevención_de_intrusos"}
license: CC BY-SA 4.0
id: eswiki-Sistema_de_prevención_de_intrusos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sistema de prevención de intrusos

Un **sistema de prevención de intrusos** (o por sus siglas en inglés **IPS**) es un *software* que ejerce el control de acceso en una red informática para proteger a los sistemas computacionales de ataques y abusos. La tecnología de prevención de intrusos es considerada por algunos como una extensión de los sistemas de detección de intrusos (IDS), pero en realidad es otro tipo de control de acceso, más cercano a las tecnologías cortafuegos.

Los IPS fueron inventados de forma independiente por Jed Haile y Vern Paxon para resolver ambigüedades en la monitorización pasiva de redes de computadoras, al situar sistemas de detecciones en la vía del tráfico. Los IPS presentan una mejora importante sobre las tecnologías de cortafuegos tradicionales, al tomar decisiones de control de acceso basados en los contenidos del tráfico, en lugar de direcciones IP o puertos. Tiempo después, algunos IPS fueron comercializados por la empresa One Secure, la cual fue finalmente adquirida por NetScreen Technologies, que a su vez fue adquirida por Juniper Networks en 2004. Dado que los IPS fueron extensiones literales de los sistemas IDS, continúan en relación.

También es importante destacar que los IPS pueden actuar al nivel de equipo, para combatir actividades potencialmente maliciosas.

 Funcionamiento

Un Sistema de Prevención de Intrusos o Intrusion Prevention System ("IPS" en sus siglas en inglés), es un dispositivo de seguridad de red que monitoriza el tráfico de red y/o las actividades de un sistema, en busca de actividad maliciosa. Entre sus principales funciones, se encuentran no sólo la de identificar la actividad maliciosa, sino la de intentar detener esta actividad. Siendo esta última una característica que distingue a este tipo de dispositivos de los llamados Sistemas de Detección de Intrusos o Intrusion Detection Systems ("IDS" en sus siglas en inglés).

Entre otras funciones (como en el caso del IDS) se tiene que poder alertar al administrador ante la detección de intrusiones o actividad maliciosa, mientras que es exclusivo de un Sistema de Prevención de Intrusos (IPS) establecer políticas de seguridad para proteger al equipo o a la red de un ataque.

De ahí que se diga que un IPS protege a una red o equipo de manera proactiva mientras que un IDS lo hace de manera reactiva.

Otras funciones importantes de estos dispositivos de red, son las de grabar información histórica de esta actividad y generar reportes.

Los IPS se clasifican en cuatro diferentes tipos:
 Basados en Red Lan (NIPS): monitorizan la red lan en busca de tráfico de red sospechoso al analizar la actividad por protocolo de comunicación lan.
 Basados en Red Wireless (WIPS): monitorean la red inalámbrica en busca de tráfico sospechoso al analizar la actividad por protocolo de comunicación inalámbrico.
 Análisis de comportamiento de red (NBA): Examina el tráfico de red para identificar amenazas que generan tráfico inusual, como ataques de denegación de servicio ciertas formas de malware y violaciones a políticas de red.
 Basados en Host (HIPS): Se efectúa mediante la instalación de paquetes de software que monitoriza un host único en busca de actividad sospechosa.
Los IPS categorizan la forma en que detectan el tráfico malicioso:

 Detección basada en firmas: como lo hace un antivirus.
 Detección basada en políticas: el IPS requiere que se declaren muy específicamente las políticas de seguridad.
 Detección basada en anomalías: en función con el patrón de comportamiento normal de tráfico.

 Detección basada en firmas
Una firma tiene la capacidad de reconocer una determinada cadena de bytes en cierto contexto, y entonces lanza una alerta. Por ejemplo, los ataques contra los servidores Web generalmente toman la forma de URLs. Por lo tanto se puede buscar utilizando un cierto patrón de cadenas que pueda identificar ataques al servidor web. Sin embargo, como este tipo de detección funciona parecido a un antivirus, el administrador debe verificar que las firmas estén constantemente actualizadas.

 Detección basada en políticas
En este tipo de detección, el IPS requiere que se declaren muy específicamente las políticas de seguridad.  Por ejemplo, determinar que hosts pueden tener comunicación con determinadas redes. El IPS reconoce el tráfico fuera del perfil permitido y lo descarta.

 Detección basada en anomalías
Este tipo de detección tiende a generar muchos falsos positivos, ya que es sumamente difícil determinar y medir una condición ‘normal’. En este tipo de detección tenemos dos opciones:

 Detección estadística de anormalidades: El IPS analiza el tráfico de red por un determinado periodo de tiempo y crea una línea base de comparación. Cuando el tráfico varía demasiado con respecto a la línea base de comportamiento, se genera una alarma.
 Detección no estadística de anormalidades: En este tipo de detección, es el administrador quien define el patrón «normal» de tráfico. Sin embargo, debido a que con este enfoque no se realiza un análisis dinámico y real del uso de la red, es susceptible a generar muchos falsos positivos.

Se podría mencionar un apartado a cerca de las estrategias utilizadas a fin de descubrir nuevos tipos de ataque; entrando en esta clasificación los honey pots.

 Detección *honey pot* (jarra de miel): funciona usando un equipo que se configura para que llame la atención de los *hackers*.

 Detección *honey pot* (jarra de miel)
Aquí se utiliza un *distractor*. Se asigna como *honey pot* un dispositivo que pueda lucir como atractivo para los atacantes. Los atacantes utilizan sus recursos para tratar de ganar acceso en el sistema y dejan intactos los verdaderos sistemas. Mediante esto, se pueden monitorizar los métodos utilizados por el atacante e incluso identificarlo, y de esa forma implementar políticas de seguridad acordes en nuestros sistemas de uso real.

 Véase también
 Detección de anomalías
 Seguridad informática
 Sistemas de detección de intrusos (*IDS*)
 DoS
 DDos
 *Firewall*
 *Host-based intrusion detection system* (HIDS)
 *Network Intrusion Detection System* (NIDS)

 Referencias

 Enlaces externos
 Snort IDS/IPS
