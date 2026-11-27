---
type: Artículo de enciclopedia
title: IDMEFv2
description: IDMEFV2 (Formato de Intercambio de Mensajes de Detección de Incidentes) es una iniciativa para estandarizar un formato de alerta para la detección de incidentes en el IETF .
resource: https://es.wikipedia.org/wiki/IDMEFv2
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/IDMEFv2"}
license: CC BY-SA 4.0
id: eswiki-IDMEFv2
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# IDMEFv2

**IDMEFV2** (**Formato de Intercambio de Mensajes de Detección de Incidentes**) es una iniciativa para estandarizar un formato de alerta para la detección de incidentes en el IETF . Desde mayo de 2023 se están desarrollando dos primeros borradores del formato y transporte en el IETF. Se trata de una evolución del estándar IETF IDMEFv1 (Intrusion Detection Message Exchange Format RFC 4765 ) definido en 2007. De este toma el principio (definición de un formato de alerta estándar) pero ampliándolo a todos los tipos de alertas, ya sean informáticas o físicas, actualizando el formato y la tecnología correspondiente. Por lo tanto, la "detección de intrusiones" se sustituye por la "detección de incidentes", abarcando un ámbito mucho más amplio.

La primera versión del formato IDMEFv2 se creó en 2021 en el marco de una colaboración entre un proyecto de investigación francés (FUI 25 SECEF: Security Exchange Format), financiado por BPI e IDF con el objetivo de mejorar el formato IDMEFv1 y un proyecto europeo H2020 7SHIELD, que trabaja en la protección de infraestructuras físicas y e informáticas contra ataques complejos e híbridos. El formato IDMEFv1, inicialmente reservado para la detección de ciberintrusiones, se ha ampliado en esta ocasión a todos los incidentes (detección de incidentes).

En el marco del proyecto 7Shield, el formato se utilizó en cinco segmentos terrestres piloto en Europa (Bélgica, Finlandia, Grecia, Italia y España), conectando así más de treinta componentes técnicos desarrollados por los distintos socios.

El primer borrador del formato fue publicado en el IETF en abril de 2023 por Télécom SudParis.

Desde el 1 de enero de 2024, Telécom SudParis lidera un nuevo proyecto de investigación relacionado con el programa Digital Europe (SAFE4SOC : Security Alert Exchange Format for SOC) destinado a ampliar el uso del formato para el intercambio de información de deteccion entre SOC (Centros de Operaciones de Seguridad) dentro de la Comunidad Europea. El proyecto tiene como objetivo adaptar el formato IDMEFv2 a este tipo de intercambio, así como finalizar sus especificaciones y obtener la estandarización del IETF.

 La comunidad IDMEFv2
La definición y mejora del formato están ahora abiertas a toda la comunidad técnico-científica a través de un sitio web y una lista de correo donde se debaten los avances y las opciones del formato.

La comunidad está trabajando actualmente en la estandarización del formato en el IETF .

 Las razones de la convergencia de la física y la tecnología de la información
Históricamente, la detección de incidentes se ha dividido en tres áreas principales de aplicación.

 Gestión del rendimiento y la disponibilidad en torno a los NMS (sistemas de gestión de redes) y otras herramientas de observabilidad, que concentran, analizan y notifican los incidentes relacionados con el rendimiento y la disponibilidad.
 Gestión de la seguridad informática en torno a los SIEM (Security Information & Event Management), que capturan, analizan e notifican los incidentes de ciberseguridad .
 Gestión de la seguridad física en torno al PSIM (gestión de la información de seguridad física), que concentra, analiza y notifica los incidentes de seguridad física. Cada uno de estos ámbitos ofrece sus propias herramientas y formatos.

Esta compartimentación, justificada históricamente, presenta hoy en día numerosas desventajas, entre ellas la multiplicación de herramientas, competencias y equipos de trabajo especializados. Por lo tanto, también resulta difícil o imposible detectar incidentes complejos, en cadena o ataques combinados. Además, es imposible realizar  correlaciones cruzadas o procesar inteligencia artificial multidominio.

Por último, en un momento en el que el Internet de las cosas está en pleno auge, la separación entre el mundo cibernético y el mundo físico es cada vez más difícil de definir y es urgente lograr unir la supervisión de los dos mundos, el digital y el físico.

IDMEFv2 ofrece, por lo tanto, un formato de aviso universal que permite la convergencia de estos múltiples dominios en un sistema unificado de detección de incidentes.

 El objetivo del formato IDMEFv2
IDMEFv2 ofrece la posibilidad de describir incidentes (o eventos sospechosos) de tipo cibernético (autenticación fallida, intento de intrusión, detección de un virus, escaneo ilegítimo de un puerto, etc.), físico (detección de movimiento, alarma de incendio, intrusión física, aproximación de un dron...), relacionados con la disponibilidad (falta de respuesta de un servidor o una cámara, temperatura o velocidad de la CPU que superan un umbral...) y, por último, los riesgos. Además, el formato permite describir los riesgos humanos o naturales potenciales, en particular los relacionados con el clima (y sus perturbaciones).

 Clases IDMEFv2
La versión V03 del borrador IDMEFV2 ofrece siete clases.

 Especificaciones de formato
La definición del formato IDMEFv2 se basa en cuatro principios fundamentales. Universalidad con el mismo formato para todos los incidentes con 5 «dimensiones» para cada aviso: la triple dimensión espacial, la dimensión cibernética ( dirección IP ) y la dimensión temporal. Una clasificación muy amplia basada en el trabajo del grupo de trabajo RIST (Reference Security Incident Taxonomy) de la ENISA y del Centro de Investigación sobre Epidemiología de Desastres (CRED) para los peligros.  Conceptos sencillos con un número limitado de clases y atributos de alto nivel (con posibilidades de ampliación sencillas), un formato limitado únicamente a la detección de incidentes (antes de la fase de análisis) y el uso de tecnologías populares con JSON sobre HTTP . Y un formato de detección "de extremo a extremo": IDMEFv2 aporta atributos técnicos para la cadena de detección (detección, correlación, agregación, IA, etc.), así como atributos más significativos para la visualización de alertas en un panel de control de "supervisión para los operadores".

 Ejemplos JSON de alertas IDMEFv2

 Incidente informático
Un SIEM detectó un posible ataque de fuerza bruta en la cuenta raíz de los servidores 192.0.2.2 y 2001:db8::/32:

 Incidente físico
Un hombre buscado por el FBI ha sido identificado en el edificio cercano a las salas de servidores. El aviso incluye un expediente del FBI y una foto de una cámara de seguridad.

 Incidente de disponibilidad
El servidor www.acme.com no responde a las solicitudes de ping.

 Implementaciones
El GitHub de IDMEFv2  aloja bibliotecas Java y Python para manipular alertas de IDMEFv2 (formato y transporte), un prototipo CP-SIEM (Cyber & Physical Security Information & Event Management) y una herramienta para validar alertas en formato JSON.

 Casos de uso de IDMEFv2
Entre los principales casos de uso se encuentra la detección cibernética y/o física; IDMEFv2 solo puede utilizarse en sistemas cibernéticos o físicos. IDMEFv2 también es adecuado para proteger infraestructuras críticas que podrían estar sujetas a ataques o incidentes híbridos. Lo mismo aplica a los sistemas inteligentes que combinan lo cibernético y lo físico (ciudades, hogares, etc.); uno de los mejores ejemplos es el coche conectado, que actualmente incorpora tanto lo físico como lo cibernético.

 IDMEFv2 y el ecosistema existente
Al limitarse a la detección de incidentes, IDMEFv2 se presenta claramente como complementario a los formatos y estándares existentes, como SNMP solo para disponibilidad, la iniciativa OCSF  para definir eventos de seguridad, IODEF para describir un incidente (después de la detección) o STIX para inteligencia de amenazas cibernéticas.

 Notas

 Enlaces externos

 El sitio web IDMEFv2, en idmefv2.org.
 El borrador IETF IDMEFv2, en datatracker.ietf.org.
 El borrador de transporte IETF IDMEFv2, en datatracker.ietf.org.
 El GitHub IDMEFv2, en github.com.
 LinkedIn IDMEFv2, en linkedin.com.
 La lista de correo IDMEFv2, en freelists.org.
 El sitio web del proyecto Safe4Soc, en safe4soc.eu.
 RFC 4765 (IDMEFv1 - 2007), en rfc-editor.org.
 Grupo de trabajo ENISA RIST (Reference-Security-Incident-Taxonomy), en github.com.
 Caso de uso de IDMEFv2 en el proyecto H2020 7SHield, en idmefv2.ovh.
