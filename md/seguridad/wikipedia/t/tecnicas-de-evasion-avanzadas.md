---
type: Artículo de enciclopedia
title: Técnicas de evasión avanzadas
description: "Las Técnicas de evasión avanzadas, también conocidas por las siglas AET (del inglés Advanced Evasion Techniques), son una serie de estrategias para de evitar la detección y el bloqueo por parte de sistemas de detección …"
resource: https://es.wikipedia.org/wiki/Técnicas_de_evasión_avanzadas
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Técnicas_de_evasión_avanzadas"}
license: CC BY-SA 4.0
id: eswiki-Técnicas_de_evasión_avanzadas
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Técnicas de evasión avanzadas

Las **Técnicas de evasión avanzadas**, también conocidas por las siglas **AET** (del inglés *Advanced Evasion Techniques*), son una serie de estrategias para de evitar la detección y el bloqueo por parte de sistemas de detección de intrusiones, principalmente los relacionados con el tráfico de red como es el caso de los sistemas de detección de intrusiones (IDS)  o sistemas de prevención de intrusiones (IPS). Estas técnicas hacen uso de propiedades de los protocolos raramente usadas en combinaciones inusuales o elaborando deliberadamente el tráfico de red que no tiene en cuenta los protocolos convencionales.

Ejemplos
En 2014 se estimaba que había activas alrededor de 330.000 técnicas de evasión activas. De ellas menos del 1% eran detectables.
Ejemplos de estas técnicas son:
 Fragmentar los payloads maliciosos y enviarlos a través de diferentes protocolos, normalmente poco habituales, con el fin de que una vez que hayan sorteado las protecciones del sistema atacado se vuelvan a unir para poder así continuar con el proceso de comprometer el sistema. Cambiar de una inspección basada en paquetes a una inspección basada en el flujo completo no es fácil. Hacerlo requiere grandes cambios en el manejo de paquetes de bajo nivel y diferencias fundamentales en la arquitectura de los dispositivos de seguridad de red. La inspección basada en el flujo completo usa más memoria y afecta al rendimiento del dispositivo.
 Algoritmos de generación de dominios (DGA).
 Canales encubiertos.
 Utilización de campos poco habituales de algunos protocolos.
 La ofuscación.
 El cifrado de los datos transferidos.
 Realizar ataques de denegación de servicio. Por ejemplo para provocar la ralentización del procesamiento de datos por parte de un dispositivo de red de modo que se imposibilite la capacidad de gestionar correctamente todo el tráfico. Este hecho puede provocar que el dispositivo funcione en modo de error y que bloquee o permita todo el tráfico.

Detección

Para bloquear esta técnicas no es suficiente con confiar exclusivamente en anomalías de protocolo o violaciones. Aunque algunas anomalías de protocolo y violaciones ocurren únicamente cuando se utilizan técnicas de evasión, la mayoría de las irregularidades del protocolo surgen debido a una implementación levemente defectuosa en las aplicaciones de Internet de uso común. Para una detección más precisa, es necesario analizar y decodificar los datos capa por capa. Como el ataque puede ser ofuscado por evasiones en muchas capas diferentes, la normalización y el análisis cuidadoso deben llevarse a cabo en la capa adecuada.

Las características más utilizadas para la detección de AET's son:
 Actualización de seguridad dinámica. Es necesario poder actualizar automáticamente y de forma continua con nuevas respuestas a las amenazas que se envían a todas las ubicaciones (incluidas las ubicaciones remotas), sin la necesidad de acceso físico.
 Inspección HTTPS/TLS. El cifrado permite esconder acciones maliciosas. La inspección de HTTPS/TLS permite inspeccionar conexiones TLS de la misma forma que el tráfico no cifrado.
 Normalización de datos. Una vez que todos los datos estén normalizados y entonces activar técnicas de detección de técnicas de evasión es crítico para proteger nuestros sistemas.
 Inspección completa de la pila de protocolos. Para identificar las amenazas es necesario que todo el tráfico sea normalizado y se analicen todos los protocolos de las distintas capas de la pila.
 Detección y generación de informes de evasiones y anomalías. Es importante tener informes que registren todo lo que es detectado, logeado y actuar en consecuencia.
 Unificación del corazón del software. Tener una solución de seguridad con un núcleo de software unificado proporciona la flexibilidad para escalar rápida y fácilmente a sus necesidades. Confiar en una solución de software le permite responder a nuevos requisitos e implementar nuevas características en un plazo de implementación más corto. Una ventaja adicional es la capacidad de las funciones de comunicarse entre sí para optimizar el rendimiento general.
 Protección de puntos finales. Hay que mantener sus puntos finales protegidos contra amenazas avanzadas. Uno de los aspectos más críticos de la protección de punto final es la capacidad de ir más allá del rango típico de amenazas y defenderse de las amenazas emergentes. Hay que trabajar en todos los puntos finales, incluidos los dispositivos móviles en constante evolución y el entorno virtualizado

Hay disponibles varias utilidades especializadas que permiten comprobar la respuesta de nuestros sistemas frente a técnicas de evasión avanzada. Es decir, permiten comprobar la efectividad o inefectividad de los sistemas de detección implantados. Ejemplos de estas herramientas son:
 Evader
 Fragroute
 whisker
 ADMmutate Evasion Tool

Referencias
