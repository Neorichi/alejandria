---
type: Artículo de enciclopedia
title: Canal binario simétrico
description: Un canal binario simétrico (en inglés Binary Symmetric Channel, BSC en adelante) es un canal típico de comunicaciones usado habitualmente en la teoría de códigos y teoría de la información.
resource: https://es.wikipedia.org/wiki/Canal_binario_simétrico
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Canal_binario_simétrico"}
license: CC BY-SA 4.0
id: eswiki-Canal_binario_simétrico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Canal binario simétrico

Un **canal binario simétrico** (en inglés *Binary Symmetric Channel*, **BSC** en adelante) es un canal típico de comunicaciones usado habitualmente en la teoría de códigos y teoría de la información. En este modelo, el transmisor envía un bit (que puede tomar valor cero o uno), y el receptor lo recibe. Este bit se recibirá correctamente en la mayoría de los casos, pero existe una probabilidad (probabilidad de error) de que se transmita incorrectamente. La importancia de este canal reside en ser uno de los más simples de analizar, es por ello por lo que es utilizado frecuentemente en la teoría de la información.

 Descripción

El BSC es un *canal binario* que puede transmitir uno de dos símbolos posibles (denominados 0 y 1). La transmisión no es perfecta, y ocasionalmente el receptor recibe el bit equivocado. Nótese que un canal no binario sería capaz de transmistir más de dos símbolos, habiendo múltiples posibilidades.

Este canal se suele usar con bastante frecuencia por ser uno de los más simples para analizar. Es por ello por lo que muchos problemas de la teoría de la comunicación se simplifican mediante un modelo BSC. Un BSC puede ser una solución aproximada aceptable para un canal de mayor complejidad.

 Definición
Un **canal binario simétrico con probabilidad *p* de fallo** es un canal con una entrada binaria y una salida (también binaria), definida con una probabilidad de error *p*. Esto viene a significar, que si una variable aleatoria *X* se transmite, y se recibe la variable aleatoria *Y*, entonces el canal viene determinado por las siguientes probabilidad condicionada
 Pr( *Y* = 0 | *X* = 0) = 1-*p*
 Pr( *Y* = 0 | *X* = 1) = *p*
 Pr( *Y* = 1 | *X* = 0 ) = *p*
 Pr( *Y* = 1 | *X* = 1 ) = 1-*p*

Donde 0 ≤ *p* ≤ 1/2. Si *p*>1/2 entonces el receptor obtendría los bits contrarios (interpretar un 1 cuando se recibe un 0, y viceversa), obteniéndose un canal equivalente con probabilidad de fallo 1-*p* ≤ 1/2.

 Capacidad de un BSC
La capacidad de canal es 1- H(*p*), donde H(*p*) es la función de entropía.

 Referencias
 David J. C. MacKay. *Information Theory, Inference, and Learning Algorithms* Cambridge: Cambridge University Press, 2003. ISBN 0-521-64298-1
 Thomas M. Cover, Joy A. Thomas. *Elements of information theory*, 1st Edition. New York: Wiley-Interscience, 1991. ISBN 0-471-06259-6.
