---
type: Artículo de enciclopedia
title: Eliminación de datos
description: "Un algoritmo de eliminación de datos (en inglés disk wiping), en informática, es el usado para el borrado del contenido de dispositivos de almacenamiento, tales como discos duros, memorias flash, memorias USB etc., de …"
resource: https://es.wikipedia.org/wiki/Eliminación_de_datos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Eliminación_de_datos"}
license: CC BY-SA 4.0
id: eswiki-Eliminación_de_datos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Eliminación de datos

Un algoritmo de **eliminación de datos** (en inglés *disk wiping*), en informática, es el usado para el borrado del contenido de dispositivos de almacenamiento, tales como discos duros, memorias flash, memorias USB etc., de forma segura. El algoritmo ejecuta la sobrescritura de los datos almacenados en el dispositivo varias veces y de un modo aleatorio.

El más común y aprobado por la NSA consiste en 3iteraciones. En la primera escriben unos (1), en la segunda ceros (0) y en la tercera el código designado por el gobierno 246. Hay diferentes versiones comerciales del algoritmo, diferenciándose entre ellas el número de iteraciones y los datos escritos. A mayor número de rondas, en una implementación correcta, debería lograrse.

 Porqué es necesario
La eliminación permanente de datos va más allá de los comandos básicos de eliminación de archivos, que solo eliminan punteros directos a los sectores del disco de datos dejando abierta la posibilidad de recuperación de datos con herramientas de software comunes o especializadas. La desmagnetización y la destrucción física hacen que los medios de almacenamiento sean inutilizables de allí en más.

Un algoritmo de eliminación de datos permite a la vez, eliminar toda la información mientras se deja el disco operativo. Las nuevas implementaciones de medios basados en memoria flash, como las unidades de estado sólido o las unidades flash USB, pueden hacer que las técnicas de borrado de datos fallen, permitiendo que los datos remanentes sean recuperables. Consiste en una aplicación de software que escribe de manera forzosa una secuencia de ceros, unos o datos pseudoaleatorios sin sentido en todos los sectores de una unidad de disco duro, asegurando el cumplimiento normativo de estándares de seguridad informática. Muchos programas de erradicación de datos también proporcionan sobrescrituras múltiples para que sean compatibles con los estándares reconocidos del gobierno y de la industria, aunque una sobrescritura de una sola pasada se considera suficiente para las unidades de disco duro modernas. Un buen software debe proporcionar la verificación de la eliminación de datos, verificación que es necesaria para cumplir con ciertos estándares.

Para proteger los datos en medios perdidos o robados, algunas aplicaciones de borrado de datos destruyen los datos de forma remota si la contraseña se ingresa incorrectamente. Las herramientas de borrado de datos también pueden apuntar a datos específicos en un disco para el borrado de rutina, proporcionando un método de protección contra piratería que consume menos tiempo que el cifrado de software. El cifrado de hardware / firmware integrado en el propio disco o en los controladores integrados es una solución popular sin ninguna degradación en el rendimiento.

 Estándares de seguridad
Existen normas estrictas de la industria y regulaciones gubernamentales que obligan a las organizaciones a mitigar el riesgo de exposición no autorizada de datos corporativos y gubernamentales confidenciales. Las regulaciones en los Estados Unidos incluyen HIPAA (Ley de Responsabilidad y Portabilidad del Seguro de Salud); FACTA (Ley de transacciones de crédito justas y precisas de 2003); GLB (Gramm-Leach Bliley); Ley Sarbanes-Oxley (SOx); Normas de seguridad de datos de la industria de tarjetas de pago (PCI DSS) y la ley de protección de datos en el Reino Unido.

El incumplimiento puede dar lugar a multas y daños a la reputación de la empresa, así como a la responsabilidad civil y penal.

 Véase también
Eliminadores de metadatos

 Enlaces externos
 NSA
