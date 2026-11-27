---
type: Artículo de enciclopedia
title: Cadena de confianza
description: "En seguridad informática, una cadena de confianza está establecida por la validación de cada componente hardware y software desde lo perspectiva \"bottom up\"."
resource: https://es.wikipedia.org/wiki/Cadena_de_confianza
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cadena_de_confianza"}
license: CC BY-SA 4.0
id: eswiki-Cadena_de_confianza
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cadena de confianza

En seguridad informática, una **cadena de confianza** está establecida por la validación de cada componente hardware y software desde lo perspectiva "*bottom up*". Pretende asegurar que únicamente se utilice software y hardware fiable manteniendo la flexibilidad.

 Introducción
Una cadena de confianza está diseñada para permitir a múltiples usuarios crear y usar software sobre el sistema, lo cual sería más difícil si todas las claves estuvieran almacenadas directamente en el hardware. Empieza con hardware que solamente se arranca desde software digitalmente firmado.  La autoridad firmante solamente firma programas de arranque que implican seguridad, de modo que solamente ejecute programas que estén firmados, o solamente permitiendo que código firmado tenga acceso a ciertas características de la máquina. Este proceso puede continuar para varios estratos.

Este proceso da como resultado una cadena de confianza. El software final será de fiar y tendrá acceso a ciertas propiedades. Si se modificara ilegalmente, la firma no sería válida y el software no se ejecutaría. Este software del que hablamos, puede ser de fiar ya que, si su firma no fuera válida, no habría sido cargado. El valor de la fiabilidad de cada estrato está garantizado por el anterior, hasta llegar al ancla de confianza.

Sería posible obtener una comprobación hardware de la firma para cada parte del software. Aun así, esto no mantendría la flexibilidad que una "cadena" proporciona. En una cadena, cualquier enlace dado puede ser reemplazado por una versión diferente para proporcionar propiedades diferentes, sin tener que hacer todo el recorrido hasta el ancla de confianza. Este uso de múltiples estratos es una aplicación de una técnica general para mejorar la escalabilidad. Esto es análogo al uso de múltiples certificados en una cadena de certificado.

 Seguridad informática
En seguridad informática, los certificados digitales están verificados utilizando una cadena de confianza. El ancla de confianza para el certificado digital es la autoridad de certificación (CA) raíz.

La jerarquía de certificación es una estructura de certificados que permite a un particular verificar la validez del emisor de un certificado. Los certificados son emitidos y firmados por certificados de lo más alto de la jerarquía, de este modo la validez y la fiabilidad de un certificado dado está determinado por la validez correspondiente del certificado que lo firmó.

La cadena de la confianza de una cadena de certificados es una lista ordenada de certificados, que contienen un certificado de un usuario final y certificados intermedios (que representan la CA intermedia), que habilita el receptor para verificar que el emisor y todo los certificados intermedios son fidedignos.

Véase también
 El proceso de la cadena de certificados está mejor descrito en la página *autoridad de certificado Intermedio.*

 X.509 cadenas de certificado: Descripción de conceptos de la cadena de certificados en un estándar ampliamente utilizado para certificados digitales.

 Referencias
