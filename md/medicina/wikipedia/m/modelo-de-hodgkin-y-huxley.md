---
type: Artículo de enciclopedia
title: Modelo de Hodgkin y Huxley
description: El modelo de Hodgkin y Huxley describe cómo se inician y transmiten los potenciales de acción en las neuronas.
resource: https://es.wikipedia.org/wiki/Modelo_de_Hodgkin_y_Huxley
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelo_de_Hodgkin_y_Huxley"}
license: CC BY-SA 4.0
id: eswiki-Modelo_de_Hodgkin_y_Huxley
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelo de Hodgkin y Huxley

El **modelo de Hodgkin y Huxley** describe cómo se inician y transmiten los potenciales de acción en las neuronas.

Consiste en un conjunto de cuatro ecuaciones diferenciales ordinarias no lineales, que aproximan las características eléctricas de células excitables como las neuronas o los miocitos cardíacos.

Alan Lloyd Hodgkin y Andrew Huxley propusieron el modelo en 1952 para explicar los mecanismos iónicos que subyacían a la iniciación y propagación de los potenciales de acción del axón gigante de calamar. En 1963 recibieron el  por este trabajo.

 Componentes básicos

La membrana lipídica acumula potencial eléctrico al impedir que los iones pasen del interior al exterior de la célula, y viceversa. Por lo tanto está representada por un capacitor (Cm).
 Los canales iónicos permiten el tránsito regulado de las cargas a través de ciertos segmentos de la membrana. Por lo que están representados por resistores no lineales (gn, donde n es un canal iónico específico), lo que significa que la conductancia de los resistores varía en función del tiempo y del voltaje.
 Las puertas de los canales iónicos están representadas por conductancias lineales (gL).
 Los gradientes electroquímicos que producen el flujo de iones están representados por baterías (En y EL), cuyos valores están determinados por el potencial de Nernst de la especie iónica de interés.
 Las bombas iónicas utilizan energía de la célula para restablecer el gradiente electroquímico en estado de reposo. Están representadas por fuentes de corriente (Ip).

La derivada en el tiempo del potencial a lo largo de la membrana  es proporcional a la suma de las corrientes en el circuito:

Donde Ii denota las corrientes iónicas individuales del modelo.

 Modelos relacionados
El modelo de FitzHugh-Nagumo es una simplificación del modelo de Hodgkin y Huxley.
