---
type: Artículo de enciclopedia
title: Indicador de compromiso
description: "Un indicador de compromiso o IDC (, IoC) es toda aquella información relevante que describe cualquier incidente de ciberseguridad, actividad y/o artefacto malicioso, mediante el análisis de sus patrones de …"
resource: https://es.wikipedia.org/wiki/Indicador_de_compromiso
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Indicador_de_compromiso"}
license: CC BY-SA 4.0
id: eswiki-Indicador_de_compromiso
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Indicador de compromiso

Un **indicador de compromiso** o **IDC** (, IoC) es toda aquella información relevante que describe cualquier incidente de ciberseguridad, actividad y/o artefacto malicioso, mediante el análisis de sus patrones de comportamiento. La intención de un indicador de compromiso es esquematizar la información que se recibe o se extrae durante el análisis de un incidente, de tal manera que pueda reutilizarse por otros investigadores o afectados, para descubrir la misma evidencia en sus sistemas y llegar a determinar si han sido o no comprometidos ya sea desde el punto de vista de monitorización frente a amenazas o por análisis forense. Por ejemplo, se identifican ficheros creados, entradas de registro modificadas, procesos o servicios nuevos. La idea subyacente es que, si se analiza un sistema y se encuentran los detalles recogidos en un indicador de compromiso concreto, se está ante una infección provocada por el programa malicioso (*malware*) al que hace referencia dicho indicador de compromiso. Los indicadores de compromiso permiten realizar un intercambio sencillo y práctico de información con el fin de detectar intrusos a partir de análisis forenses, respuestas a incidentes o análisis de *malware*.

Los indicadores de compromiso son recogidos, almacenados y distribuidos por las llamadas plataformas de inteligencia contra amenazas (TIP) que permiten la administración de la inteligencia sobre amenazas informáticas y de las entidades asociadas como actores, campañas, incidentes, firmas, boletines y tácticas, técnicas y procedimientos. Ejemplos de este tipo de herramientas son MANTIS y MISP.

Características

En síntesis, un IDC es un documento creado específicamente para transmitir las características técnicas de una amenaza con las siguientes características:
Se especifican detalles técnicos replicables enlazados mediante operadores lógicos (AND, OR, etc…). Este documento puede estar escrito en distintos lenguajes (STIX, OTX, CIF, OpenIoC, etc.), normalmente XML. Esta información puede ser aprovechada por otras personas, grupos e implementar las firmas en diferentes herramientas como IDS, IPS, cortafuegos.
Está vivo, no es definitivo.
Es flexible, se pueden recoger todo tipo de evidencias, tanto específicas de un sistema, como generales para todos los sistemas afectados. Por ejemplo, ficheros creados, entradas de registro modificadas, procesos o servicios nuevos o lista de direcciones IP relacionadas con un programa de mando y control.

Estándares de descripción
Existen varios sistemas que definen cómo deben documentarse los indicadores de compromiso. Algunos de los más conocidos son:
 **Incident Object Description Exchange Format** (**IODEF**). Definido por la IETF en el RFC 5070. Dirigidas a los CSIRTs, por tanto, orientada a incidentes. Formato XML. Adopción limitada
 **Open Indicators of Compromise** (**OpenIoC**). Surgido de la compañía Mandiant, comprada por FireEye, para mejoar IODEF. Distribuido bajo licencia Apache2 y basado en XML. Hay disponibles herramientas libres gratuitas para facilitar su uso desarrolladas por los propios creadores: IDC Editor (editor para crear o modificar indicadores de compromiso) y IoC Finder (buscador en el sistema de los indicadores de compromiso que se le faciliten en una lista). No sirve para detallar aspectos a más alto nivel como vectores de ataque y tácticas seguidos por el *malware*.
 **Oasis Cyber Threat Intelligence** (**CTI**). iniciado por el gobierno estadounidense, a través del MITRE, DHS y US-CERT, fue posteriormente respaldado por algunos de los principales fabricantes de soluciones de seguridad del mercado. Se ha pasado al consorcio de estándares OASIS. Está compuesto por tres subcomités:
 **Cyber Observable Expressión** (**CybOX**). Serialización de datos en formato JSON, para la caracterización de información sobre *malware*, detección de intrusiones, respuesta y manejo de incidentes y forense digital. Es de bajo nivel. En la actualidad, CybOX ha sido integrado por completo en STIX y ya no se recomienda su uso.
 **Structured Threat Information Expression** (**STIX**). Lenguaje estructurado en JSON para describir las ciberamenazas en un formato que puede ser compartido, almacenado y analizado de forma consistente. Aparece para aportar una organización de la información de manera altamente estructurada e interrelacionada para lograr una alta legibilidad y fácil comprensión. Es un formato basado en grafos para ofrecer una representación muy intuitiva de los objetos y relaciones entre los mismos. Muy útil para los aspectos de alto nivel como quién está detrás del *malware* y dónde ha sido utilizado. Permite aprovechar la información descrita en otros formatos, por ejemplo, OpenIoC, reglas de Snort sistema de detección de intrusos en red) y reglas de YARA (identifican *malware* basándose en patrones de texto o binarios y el uso de expresiones booleanas para determinar su lógica) entre otros.
 **Trusted Automated Exchange of indicator Information** (**TAXII**). Especificaciones orientadas a conformar un mecanismo flexible de transporte de información de ciberamenazas. TAXII se centra en los mecanismos de distribución de información y adopta otros estándares para el formato de esta. Así a través de los servicios definidos por TAXII, las organizaciones pueden intercambiar información de forma segura y automatizada con soporte para múltiples formatos de representación de información de ciberamenazas, especialmente STIX y CybOx. Soporta diversas arquitecturas de comunicación (Hub and Spoke, Peer to Peer y cliente/servidor). Es un protocolo de la capa de aplicación y funciona sobre HTTPS
 **Malware Attribute Enumeration and Characterization** (**MAEC**). Enumera atributos que caracterizan software malintencionado. Creado basándose en CybOX.
 **Collective Intelligence Framework** (**CIF**).
 **Open Threat Exchange** (**OTX**). Usado por AlienVault Open Threat Exchange herramienta que proporciona acceso abierto a una comunidad global de investigadores de amenazas y profesionales de la seguridad que proporciona datos de amenazas generados por la comunidad permitiendo la investigación colaborativa y automatiza el proceso de actualización de la infraestructura de seguridad con datos de amenazas desde cualquier fuente.
 **Vocabulary for Event Recording and Incident Sharing** (**VERIS**).

Repositorios
Los repositorios de IDC más importantes son:
IOC Bucket. Es gratuito
Openioc Db. Es gratuito y publicado bajo licencia Apache 2.

Referencias
