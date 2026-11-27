---
type: Artículo de enciclopedia
title: Heurística en antivirus
description: "En el campo de los antivirus, se conoce como heurística al conjunto de técnicas que se emplean para reconocer códigos maliciosos (virus, gusanos, troyanos, etcétera) que no se encuentren en su base de datos (ya sea …"
resource: https://es.wikipedia.org/wiki/Heurística_en_antivirus
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Heurística_en_antivirus"}
license: CC BY-SA 4.0
id: eswiki-Heurística_en_antivirus
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Heurística en antivirus

En el campo de los antivirus, se conoce como **heurística** al conjunto de técnicas que se emplean para reconocer códigos maliciosos (virus, gusanos, troyanos, etcétera) que no se encuentren en su base de datos (ya sea porque son nuevos, o por no ser muy divulgados). El término general implica funcionalidades como detección a través de firmas genéricas, reconocimiento del código compilado, desensamblado, desempaquetamiento, entre otros.

Su importancia radica en el hecho de ser la única defensa automática posible frente a la aparición de nuevos códigos maliciosos de los que no se posea firmas.

 Lógica proposicional
 Firmas genéricas
Hay muchos códigos maliciosos que son modificados por sus autores para crear nuevas versiones. Usualmente, estas variantes contienen similitudes con los originales, por lo que se catalogan como una familia de virus. Gracias a las similitudes dentro del código del virus, los antivirus pueden llegar a reconocer a todos los miembros de la misma familia a través de una única firma o vacuna genérica. Esto permite que al momento de aparecer una nueva versión de un virus ya conocido, aquellos antivirus que implementan esta técnica puedan detectarlo sin la necesidad de una actualización.
Las implementaciones de heurística de algunos antivirus utilizan técnicas para reconocer instrucciones comúnmente aplicadas por los códigos maliciosos y así poder identificar si un archivo puede suponer una amenaza.

 Desensamblado
Todo archivo ejecutable puede ser desensamblado con el objetivo de obtener el código fuente del programa en lenguaje ensamblador. La heurística de algunos antivirus es capaz de analizar el código fuente de los programas sospechosos. De esta forma puede reconocer un posible código malicioso si encuentra técnicas de desarrollo que suelen usarse para programar virus, sin la necesidad de una actualización.

 Desempaquetamiento
Los programadores de códigos maliciosos suelen usar empaquetadores de archivos ejecutables como UPX con el fin de modificar la "apariencia" del virus a los ojos del análisis antivirus. Para evitar ser engañados por un código malicioso antiguo y luego reempaquetado, los antivirus incluyen en sus técnicas heurísticas métodos de desempaquetamiento. De esta forma pueden analizar el código real del programa, y no el empaquetado..

 Evaluaciones retrospectivas
La heurística es un aspecto muy difícil de probar en los antivirus, dado que se requiere realizar las denominadas evaluaciones retrospectivas.

 ¿Qué son las evaluaciones retrospectivas?

Para poder analizar correctamente el funcionamiento de las capacidades heurísticas o *proactivas* de un antivirus, lo que se hace es detener la actualización de firmas del producto durante un período **X**. En ese lapso, se acumulan muestras de códigos maliciosos nuevos, para que una vez recolectada una cantidad suficiente, se analice si los antivirus las reconocen o no. Al no haber sido actualizados para detectar esas muestras, el antivirus solo podrá reconocer si están infectadas o no a través de sus capacidades heurísticas.

Gracias a estas evaluaciones se puede conocer en detalle el rendimiento de los productos antivirus frente a virus nuevos o desconocidos..

 Ejemplos

Existen varios organismos independientes que realizan evaluaciones retrospectivas, como por ejemplo:

 InfoSpyware.com (en castellano)
 AV-Comparatives (en inglés)
 Hispasec (en castellano)
 MalwareBytes (en castellano)
