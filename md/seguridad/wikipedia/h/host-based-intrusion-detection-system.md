---
type: Artículo de enciclopedia
title: Host-based intrusion detection system
description: HIDS es también conocido como Sistema de detección de intrusos en un Host.
resource: https://es.wikipedia.org/wiki/Host-based_intrusion_detection_system
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Host-based_intrusion_detection_system"}
license: CC BY-SA 4.0
id: eswiki-Host-based_intrusion_detection_system
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Host-based intrusion detection system

**HIDS** es también conocido como *Sistema de detección de intrusos en un Host*. Busca detectar anomalías que indican un riesgo potencial, revisando las actividades en la máquina (host). Puede tomar medidas protectoras.

Las funciones de este tipo de software son muy similares a las de los IDS. Configuraciones típicas permiten varios HIDS repartidos por la red que envían sus resultados a un servidor centralizado que los analizará en busca de los riesgos y alertas antes mencionados.

Este fue el primer tipo de software de detección de intrusos que se diseñó, siendo el objetivo original el Mainframe, donde la interacción exterior era infrecuente.

En comparación con los sistemas de detección de intrusiones basados en red, HIDS tiene la ventaja de su capacidad de identificar ataques internos. Mientras NIDS examina los datos del tráfico de la red, HIDS examina los datos que se originan en los sistemas operativos. En los últimos años, HIDS se ha enfrentado al desafío del big data, que puede atribuirse al mayor avance de las instalaciones y metodologías de los centros de datos.Una desventaja de usar HIDS es que debe instalarse en todas y cada una de las computadoras que necesitan protección contra intrusiones. Esto puede provocar una ralentización del rendimiento del dispositivo y de los sistemas de detección de intrusos.

 Protección de los HIDS
Los HIDS generalmente hacen todo lo posible para evitar que las bases de datos de objetos, de checksum y sus reportes sufran cualquier forma de manipulación. Después de todo, si los intrusos lograran modificar cualquiera de los objetos que los HIDS monitorean, nada podría detener a los intrusos de la modificación de este tipo a los propios HIDS - a menos que los administradores de seguridad tomen las precauciones adecuadas. Muchos gusanos y virus a tratar de desactivar las herramientas antivirus, por ejemplo.

Aparte de las cripto-técnicas, los HIDS podrían permitir a los administradores almacenar las bases de datos en un CD-ROM o en otras dispositivos de memoria de solo lectura (otro factor de lucha para las actualizaciones poco frecuentes ...) o almacenarlos en una memoria fuera del sistema. Del mismo modo, un HIDS frecuentemente envía sus registros (*logs*) fuera del sistema de inmediato - por lo general utilizando canales VPN a algún sistema de gestión central.

Se podría argumentar que el módulo de plataforma de confianza es un tipo de HIDS. A pesar de su alcance difiere en muchos aspectos a la de un HIDS, fundamentalmente, proporciona un medio para identificar si hay algo/alguien que ha manipulado una porción de un ordenador. Arquitectónicamente este proporciona la máxima (por lo menos hasta ahora) detección de intrusiones basado en host, ya que depende de un hardware externo a la CPU en sí, por lo tanto por lo que es mucho más difícil para un intruso corromper a sus bases de datos de objetos y de checksums.

 Recepción
InfoWorld opina que el software HIDS es una forma útil para administradores de red de encontrar malware, sugiriendo que debería usarse en todos los servidores, no solo en los servidores críticos.

 Véase también
 NIDS (Network Intrusion Detection System)
 Tripwire
 Privacidad

 Referencias

 Enlaces externos
Lista de HIDS comerciales, Mosaic Security Research (en inglés)
