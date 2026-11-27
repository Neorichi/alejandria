---
type: Artículo de enciclopedia
title: Tráfico de relleno
description: "El tráfico de relleno (traducción directa del término inglés traffic padding), también llamado tráfico dummy (del inglés dummy traffic), es un tipo de esquema de relleno para tráfico de red cuya estrategia consiste en …"
resource: https://es.wikipedia.org/wiki/Tráfico_de_relleno
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Tráfico_de_relleno"}
license: CC BY-SA 4.0
id: eswiki-Tráfico_de_relleno
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Tráfico de relleno

El **tráfico de relleno** (traducción directa del término inglés *traffic padding*), también llamado **tráfico dummy** (del inglés *dummy traffic*), es un tipo de esquema de relleno para tráfico de red cuya estrategia consiste en generar tráfico artificial de información, con contenido irrelevante, que se intercambian las distintas entidades.

Como contrapartida evidentemente el uso de tráfico dummy tenemos que provoca un gasto adicional de ancho de banda que no es aprovechado para la transmisión de información.

Aplicaciones
Dificultar el análisis del tráfico
Si un atacante que escucha el tráfico que se intercambian las entidades tendrá dificultades para distinguir entre la información real y la de relleno. Será difícil detectar quién se está comunicando con quién y cual es el contenido de dicha comunicación.

Observar que la utilidad de tráfico dummy no se circunscribe a redes en las que las entidades se comunican directamente, sino que también es muy útil para redes en las que se usan entidades intermedias en la comunicación a modo de proxy. En este último tipo de redes se ha demostrado que si no hay tráfico dummy normalmente se puede establecer quien se está comunicando con quien realizando un estudio de la tasas de entrada y de salida de mensajes de los nodos.

El tráfico dummy es una buena herramienta para redes en las que se busca el anonimato (darknets).

El uso de tráfico dummy no es la solución a todos los problemas. Hay atáques de análisis de tráfico que obtienen las tasas de tráfico incluso si usamos tráfico dummy.

Confidencialidad
Se ha propuesto el uso de tráfico de relleno para conseguir la confidencialidad sin utilizar cifrado (protocolos de rellenado con paja y aventado). De esta forma se puede conseguir mantener el secreto de la comunicación sin usar claves de cifrado que pueden estar sujetas a leyes restrictivas.

 Estratategias
Hay distintas estrategias para diseñar el tráfico de relleno de forma que sea lo más efectiva posible en sus objetivos. Veamos algunos ejemplos.
 Control del tráfico
Normalmente en las redes que usa tráfico dummy hay entidades que funcionan a modo de intermediario para ocultar quien se comunica con quien. Es tipo de redes podemos clasificar en función de quien controla el tráfico dummy el tráfico dummy:
 **Extremo a extremo** (en inglés *end-to-end*).- Son el emisor y el receptor quien lo controla
 **Enlaces con relleno** (en inglés *link padding*).- Son las entidades intermedias quien lo controla.

 Cantidad de tráfico
Hay dos estrategias principales para calibrar que cantidad de mensajes de tráfico dummy son necesarias:
 **Con intervalo de tiempo constante** o CIT (del inglés *Constant Interval Time*).- El tráfico es modificado para tener tasas constantes de tráficos usando temporizadores periódicos.
 **Con intervalo de tiempo variable** o VIT (del inglés *Variable Interval Time*).- El tráfico es modificado para tener tasas una tasa variable usando temporizadores no periódicos.

 Referencias
