---
type: Artículo de enciclopedia
title: Efecto avalancha
description: "En criptografía, el efecto avalancha es la propiedad deseable de los algoritmos criptográficos, generalmente cifrados de bloque y funciones de cifrado criptográfico, en donde si una entrada cambia ligeramente (por …"
resource: https://es.wikipedia.org/wiki/Efecto_avalancha
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Efecto_avalancha"}
license: CC BY-SA 4.0
id: eswiki-Efecto_avalancha
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Efecto avalancha

En criptografía, el **efecto avalancha** es la propiedad deseable de los algoritmos criptográficos, generalmente cifrados de bloque y funciones de cifrado criptográfico, en donde si una entrada cambia ligeramente (por ejemplo, permutando un solo bit), la salida cambia significativamente (por ejemplo, la mitad de los bits de salida). En el caso de los cifrados de bloque de alta calidad, un cambio tan pequeño en la clave o en el texto plano debería provocar un cambio drástico en el texto cifrado. El término real fue utilizado por primera vez por Horst Feistel, aunque el concepto se remonta a al menos la *difusión de* Shannon.

Si un cifrado de bloque o función de hash criptográfica no exhibe el efecto de avalancha en un grado significativo, entonces tiene una asignación aleatoria deficiente y, por lo tanto, un criptoanalista puede hacer predicciones sobre la entrada, teniendo como dato solo la salida. Esto puede ser suficiente para romper parcial o completamente el algoritmo. Por lo tanto, el efecto de avalancha es una condición deseable desde el punto de vista del diseñador del algoritmo o dispositivo criptográfico. Si no se incorpora esta característica, la función hash queda expuesta a ataques que incluyen ataques de colisión, ataques de extensión de longitud y ataques de preimagen.

La construcción de un cifrado o hash que exhiba un efecto de avalancha sustancial es uno de los principales objetivos de diseño, y matemáticamente la construcción aprovecha el efecto mariposa. Esta es la razón por la que la mayoría de los cifrados de bloque son cifrados de producto. También es la razón por la que las funciones hash tienen grandes bloques de datos. Ambas características permiten que los pequeños cambios se propaguen rápidamente a través de las iteraciones del algoritmo, de modo que cada bit de la salida debería depender de cada bit de la entrada antes de que finalice el algoritmo.

 Criterio de avalancha estricto
El **estricto de avalancha estricto** (***SAC***, por sus siglas en inglés) es una formalización del efecto de avalancha. Se satisface si, cada vez que se complementa un solo bit de entrada, cada uno de los bits de salida cambia con un 50% de probabilidad. El SAC se basa en los conceptos de integridad y avalancha. Fue introducido por Webster y Tavares en 1985.

Las generalizaciones de orden superior de SAC implican múltiples bits de entrada. Las funciones booleanas que satisfacen el orden más alto de SAC son siempre funciones dobladas, también llamadas *funciones máximamente no lineales* o *funciones no lineales perfectas*.

 Criterio de independencia de bit
El **criterio de independencia de bit** (***BIC***, por sus siglas en inglés) establece que los bits de salida *j* y *k* deben cambiar independientemente cuando se invierte un solo bit de entrada *i*, para todos *i*, *j* y *k* .

 Véase también

 Efecto mariposa
 Confusión y difusión

 Referencias
