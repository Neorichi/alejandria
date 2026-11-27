---
type: Artículo de enciclopedia
title: Procesador criptográfico seguro
description: "Un procesador criptográfico seguro o criptoprocesador seguro es un procesador criptográfico (microprocesador optimizado para realizar operaciones criptográficas), empaquetado en un dispositivo con múltiples medidas de …"
resource: https://es.wikipedia.org/wiki/Procesador_criptográfico_seguro
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Procesador_criptográfico_seguro"}
license: CC BY-SA 4.0
id: eswiki-Procesador_criptográfico_seguro
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Procesador criptográfico seguro

Un **procesador criptográfico seguro** o **criptoprocesador seguro** es un procesador criptográfico (microprocesador  optimizado para realizar operaciones criptográficas), empaquetado en un dispositivo con múltiples medidas de seguridad física, que le dan ciertas propiedades (por ejemplo resistencia a modificaciones), que le permiten garantizar que cierta información confidencial se genera, se almacena y se utiliza exclusivamente de forma interna. Esto permite eliminar la necesidad de proteger con medidas de seguridad físicas el resto del sistema

Una aplicación típica de este tipo de dispositivos es la generación, almacenamiento de claves privadas en criptografía de clave pública

Motivación
La mayoría de los sistemas utilizan procesadores convencionales, sistemas operativos estándar y canales de comunicación estándar. Estos sistemas tienen vulnerabilidades, algunas de ellas públicas. Ante la certeza de que el software no es suficiente para proteger el sistema, se necesita protección física.

Característica habituales
Algunos ejemplos de características de protección que tienen estos dispositivos son:
Escudos de recubrimiento conductor del circuito para impedir la obtención de señales de bus internos
Detección y respuesta ante manipulación.
Borrado automático del dispositivo cuando se detecta cualquier tipo de manipulación.
Controles de ejecución basados en cadena de confianza para asegurar la autenticidad.
Cadena de confianza de cargador de arranque que verifica la autenticidad del sistema operativo antes de cargarlo
Cadena de confianza del sistema operativo que verifica la autenticidad del software de las aplicaciones antes de cargarlo.
Ejecución controlada para evitar retrasos de tiempo que revelen cualquier información secreta (evita canales ocultos)

Niveles de seguridad
Actualmente se han establecido estándares que miden los niveles de seguridad implementados en cualquier dispositivo criptográfico que combina el uso de hardware y software. Por ejemplo el FIPS 140-2 del NIST

Aplicaciones
Este tipo de dispositivos se usan frecuentemente para:
Aplicaciones militares. Por ejemplo para armamento nuclear, hardware de comunicaciones
Aplicaciones civiles
Tarjetas inteligentes
Tarjetas SIM GSM de teléfono
Módulo de plataforma confiable para realizar computación confiable.
Hardware Security Module.
Chips de seguridad para sistema embebidos

Referencias
Fundamentos sobre certificados digitales (V) – Dispositivos físicos para gestión y custodia de claves. David Cutanda. 28 de octubre de 2013.
