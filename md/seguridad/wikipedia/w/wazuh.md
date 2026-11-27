---
type: Artículo de enciclopedia
title: Wazuh
description: Wazuh es un sistema de detección de intrusos basado en host de código abierto y libre (HIDS).
resource: https://es.wikipedia.org/wiki/Wazuh
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Wazuh"}
license: CC BY-SA 4.0
id: eswiki-Wazuh
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Wazuh

- **Nombre:** Wazuh
- **Desarrollador:** Wazuh Inc
- **Última versión:** 4.14.5
- **Género:** Security / HIDS
- **Sistema operativo:** Cross-platform
- **Licencia:** GNU GPL v2
- **Modelo desarrollo:** Software Libre

**Wazuh**  es un sistema de detección de intrusos basado en host de código abierto y libre (HIDS). Realiza análisis de registro, comprobación de integridad, supervisión del registro de Windows, detección de rootkits, alertas basadas en el tiempo y respuesta activa. Proporciona detección de intrusiones para la mayoría de los sistemas operativos, incluyendo Linux, AIX, HP-UX, macOS, Solaris y Windows. Wazuh tiene una arquitectura centralizada y multiplataforma que permite que múltiples sistemas sean fácilmente monitoreados y administrados.
 Historia

Wazuh es una solución de monitorización de seguridad gratuita y de código abierto, preparada para empresas para la detección de amenazas, monitorización de integridad, respuesta a incidentes y cumplimiento.

Fundada en 2015 por Santiago Basset como una bifurcación de OSSEC, actualmente cuenta con una comunidad de código abierto de más de  usuarios.

 Componentes de software
Los principales componentes de Wazuh son el agente, el servidor y Elastic Stack.

El agente ligero de Wazuh está diseñado para realizar una serie de tareas con el objetivo de detectar amenazas y, cuando sea necesario, activar respuestas automáticas. Puede funcionar en diversas plataformas, incluyendo Windows, Linux, macOS, AIX, Solaris y HP-UX. Estos agentes pueden ser configurados y administrados desde el servidor de Wazuh.

El servidor de Wazuh se encarga de analizar los datos recibidos de los agentes, procesar los eventos a través de decodificadores y reglas, y utilizar la inteligencia de amenazas para buscar los conocidos IOC (Indicadores de Compromiso). Un solo servidor Wazuh puede analizar los datos de cientos o miles de agentes, y escalar de manera horizontal cuando se configura en modo cluster.

El servidor también se utiliza para gestionar los agentes, configurándolos y actualizándolos a distancia cuando sea necesario. Además, el servidor es capaz de enviar órdenes a los agentes, por ejemplo, para activar una respuesta cuando se detecta una amenaza.

Las alertas generadas por Wazuh son enviadas a Elasticsearch, donde son indexadas y almacenadas. El plugin Wazuh Kibana proporciona una potente interfaz de usuario para la visualización y el análisis de datos, que también puede utilizarse para gestionar y supervisar la configuración y el estado de los agentes.

La interfaz de usuario de la web de Wazuh incluye tableros listos para usar para el cumplimiento de la normativa (por ejemplo, PCI DSS, GDPR, CIS), aplicaciones vulnerables detectadas, supervisión de la integridad de los archivos, evaluación de la configuración, eventos de seguridad, supervisión de la infraestructura de la nube y otros.

 Véase también

 Seguridad informática
 Sistema de detección de intrusos en un Host

 Enlaces externos

 Página web oficial de Wazuh
 Lista de correo de Wazuh
 Comunidad de Wazuh (canal de Slack)
 Documentación de Wazuh
 Repositorio de GitHub

 Referencias
