---
type: Artículo de enciclopedia
title: Exec Shield
description: Exec Shield es un proyecto realizado por Red Hat, Inc. en 2002 con el objetivo de reducir el riesgo producto de agujeros de seguridad en Linux.
resource: https://es.wikipedia.org/wiki/Exec_Shield
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Exec_Shield"}
license: CC BY-SA 4.0
id: eswiki-Exec_Shield
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Exec Shield

- **Género:** componente del núcleo Linux

***Exec Shield*** es un proyecto realizado por Red Hat, Inc. en 2002 con el objetivo de reducir el riesgo producto de agujeros de seguridad en Linux. El primer resultado del proyecto fue un parche de seguridad para el núcleo Linux que emula el bit NX en máquinas x86, las cuales no disponen de una implementación nativa de NX en su hardware. Aunque el proyecto Exec Shield tiene muchos otros componentes, algunas personas se refieren al primera parche como Exec Shield.

El primer parche de Exec Shield añadía una opción a la zona de memoria de datos como no ejecutable y a la zona de memoria del programa como no escribible. Esto elimina muchos de los exploits potenciales, así como también aquellos provenientes de desbordamiento de búfer y otras técnicas eficaces en la sobrescritura de datos y la inserción de código en dichas estructuras. Exec Shield también proporciona aleatorización del espacio de direcciones para mmap y la base del *heap*.

Además, este parche incrementa la dificultad de insertar y ejecutar shellcodes, haciendo que la mayoría de exploits no sean efectivos. Ninguna recompilación de las aplicaciones es necesaria para poder usar completamente Exec Shield, aunque algunas aplicaciones (Mono, Wine, XEmacs) no son del todo compatibles.

Otras características que están fuera del proyecto Exec Shield son los Ejecutables con Posición Independiente (PIE), el parche de aleatorización del espacio de direcciones para los núcleos Linux, un amplio conjunto de comprobaciones internas de seguridad para glibc que hacen que los exploits del montículo y de formato de cadenas sean casi imposibles, la característica GCC Fortify Source, y la adaptación y unión de GCC *stack-protector*.

 Implementación
Exec Shield funciona en todas las máquinas x86 que usan límites del segmento de código. Gracias a la manera en que Exec Shield funciona, es muy ligero; sin embargo, no protegerá totalmente distribuciones arbitrarias de la memoria virtual. Si el límite del segmento de código (CS) es superado, por ejemplo llamando a mprotect para aumentar la memoria ejecutable, entonces las protecciones se pierden por debajo de ese límite. Ingo Molnar advirtió de esto en una conversación de corre electrónico. Afortunadamente, la mayoría de las aplicaciones son seguras ya que la pila (que es la parte más importante) no se convierte en ejecutable a menos que la aplicación realice algunas llamadas explícitas.

Por agosto de 2004, nada del proyecto Exec Shield trataba de forzar protecciones de la memoria restringiendo mprotect en cualquier arquitectura; aunque la memoria no se debería iniciar siendo ejecutable, podía ser ejecutable más tarde, de modo que el núcleo permitirá a una aplicación marcar las páginas de la memoria como escribibles y ejecutables a la vez. Sin embargo, en cooperación con el proyecto SELinux (Security Enhanced Linux), la política estándar de la distribución Fedora Core prohíbe este comportamiento para la mayoría de los ejecutables, con algunas excepciones por razones de compatibilidad.

 Historia

Exec Shield fue desarrollado por varias personas de Red Hat; el primer parche fue realizado por Ingo Molnar de Red Hat y la primera versión apareció en mayo de 2003. Forma parte de Fedora Core desde la versión 1 a la 6 y de Red Hat Enterprise Linux desde la versión 3 (Update 3) hasta la 4. Otros desarrolladores involucrados en el proyecto son Jakub Jelínek, Ulrich Drepper, Richard Henderson, Arjan van de Ven.

 Véase también

Bit NX
Openwall
PaX
StackGuard
W^X

 Referencias

 Enlaces externos
Página web del parche de Exec Shield de Ingo Molnar , incluye documentación en el archivo ANNOUNCE-exec-shield
Artículo del proyecto en Newsforge
Artículo del proyecto en Red Hat Magazine
Puntos de seguridad negativos con Exec Shield
