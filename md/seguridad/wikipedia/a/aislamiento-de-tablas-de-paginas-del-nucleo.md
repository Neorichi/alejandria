---
type: Artículo de enciclopedia
title: Aislamiento de tablas de páginas del núcleo
description: "El aislamiento de tablas de páginas del núcleo (KPTI, por sus siglas en inglés, antes conocido como KAISER) es una característica del núcleo Linux que mitiga la vulnerabilidad Meltdown (que afecta principalmente a las …"
resource: https://es.wikipedia.org/wiki/Aislamiento_de_tablas_de_páginas_del_núcleo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Aislamiento_de_tablas_de_páginas_del_núcleo"}
license: CC BY-SA 4.0
id: eswiki-Aislamiento_de_tablas_de_páginas_del_núcleo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Aislamiento de tablas de páginas del núcleo

El **aislamiento de tablas de páginas del núcleo** (**KPTI**, por sus siglas en inglés, antes conocido como **KAISER**) es una característica del núcleo Linux que mitiga la vulnerabilidad Meltdown (que afecta principalmente a las CPUs x86 de Intel) y mejora la resistencia del núcleo ante intentos de eludir la aleatorización de la disposición del espacio de direcciones del núcleo (KASLR). Funciona aislando mejor las memorias del espacio de usuario y del espacio del kernel. KPTI se integró en la versión 4.15 del núcleo Linux, y también se incorporó como backport a los núcleos Linux 4.4.11 y 4.9.75. Windows y macOS también han recibido actualizaciones similares. KPTI no soluciona la vulnerabilidad Spectre.

 Antecedentes de KAISER

Los parches de KPTI se basaron en KAISER (*Kernel Address Isolation to have Side-channels Efficiently Removed*; en español, "Aislamiento de Direcciones del Núcleo para Eliminar Eficientemente los Canales Laterales"), publicado en junio de 2017, antes de que se conociera Meltdown. KAISER mejoraba KASLR, una mitigación de 2014 para un problema mucho menos grave.

En 2014, el núcleo Linux adoptó la aleatorización de la disposición del espacio de direcciones del núcleo (KASLR), que dificulta la explotación de otras vulnerabilidades del *kernel* y que depende de que las direcciones de memoria del núcleo permanezcan ocultas al espacio de usuario. Sin embargo, a pesar de que esto prohíbe el acceso a estas direcciones de memoria del núcleo, existen varios ataques de canal lateral viables en los procesadores actuales que pueden revelar la ubicación de esta memoria, permitiendo eludir la protección de KASLR.

Mientras que KASLR simplemente impide la fuga de datos referentes a la ubicación de las direcciones de memoria, KAISER además impide la fuga de información contenida en esa memoria, cubriendo, por lo tanto, el caso de Meltdown.

En 2017, KAISER solucionó estos problemas de KASLR eliminando el origen de la fuga de direcciones.

 KPTI y la Vulnerabilidad Meltdown

KPTI está basado en KAISER. Sin KPTI, cuando se ejecuta código en el espacio de usuario (es decir, aplicaciones), Linux mantiene toda la memoria del *kernel* en las tablas de páginas, aunque protegida. La ventaja es que cuando la aplicación realiza una llamada al sistema o se recibe una interrupción, las tablas de páginas del núcleo siempre están presentes, evitando la sobrecarga asociada con la mayoría de los cambios de contexto (limpieza del TLB, intercambio de tablas de páginas, etc.).

En enero de 2018, se hizo pública la vulnerabilidad Meltdown, que afecta a las CPUs Intel x86 y ARM Cortex-A75. Esta vulnerabilidad era mucho más grave que la elusión de KASLR que KAISER pretendía originalmente solucionar: se descubrió que el propio *contenido* de la memoria del *kernel* podía quedar expuesto, no solo la ubicación de las direcciones de memoria. Los parches de KAISER se adaptaron para corregir el problema de Meltdown y se renombraron como KPTI.

KPTI (basado en KAISER) previene Meltdown al impedir que las ubicaciones protegidas se mapeen al espacio de usuario.

Actualmente no hay constancia de que los procesadores AMD x86 se vean afectados por Meltdown, por lo que no necesitan KPTI para mitigar el problema. Sin embargo, los procesadores AMD sí son susceptibles a la elusión de KASLR cuando KPTI está desactivado.

 Implementación

KPTI corrige estas fugas de información separando completamente las tablas de páginas del espacio de usuario de las del espacio del núcleo. En los procesadores que soportan los identificadores de contexto de proceso (PCID), se puede evitar la limpieza del TLB, pero incluso entonces, esto supone una pérdida significativa de rendimiento, particularmente en tareas con muchas llamadas al sistema o interrupciones.

La sobrecarga de trabajo se estableció en un 0.28% según los autores originales de KAISER; un desarrollador de Linux la estimó en aproximadamente un 5% para la mayoría de las tareas típicas, y hasta un 30% en ciertos casos, incluso con la optimización de PCID; en el caso de la base de datos PostgreSQL, el impacto en pruebas de solo lectura en un procesador Intel Skylake fue del 7 al 17% (o del 16 al 23% sin PCID), mientras que una evaluación completa de pruebas de referencia arrojó una caída de rendimiento de entre el 13 y el 19% (Coffee Lake frente a Broadwell-E). Phoronix ha realizado muchas pruebas de referencia en las que Redis perdía un 6-7% de rendimiento mientras que la compilación del núcleo Linux se ralentizaba en un 5% en Haswell.

KPTI puede desactivarse parcialmente con la opción "nopti" de arranque del núcleo. También se han añadido medios para desactivar KPTI en caso de que futuros procesadores corrijan las fugas de información descritas.

 Referencias

 Enlaces externos
 Documentación de los parches KPTI (en inglés)
