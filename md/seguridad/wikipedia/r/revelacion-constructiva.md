---
type: Artículo de enciclopedia
title: Revelación constructiva
description: La revelación constructiva (en inglés constructive vulnerability) es una política de revelación parcial de vulnerabilidades propuesta por el University of Oulu Secure Programming Group (OUSPG)
resource: https://es.wikipedia.org/wiki/Revelación_constructiva
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Revelación_constructiva"}
license: CC BY-SA 4.0
id: eswiki-Revelación_constructiva
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Revelación constructiva

La **revelación constructiva** (en inglés *constructive vulnerability*) es una política de revelación parcial de vulnerabilidades propuesta por el University of Oulu Secure Programming Group (OUSPG)

 Descripción
El objetivo principal es producir una política de revelación que permita conseguir una herramienta de prueba de caja negra de vulnerabilidades que permita evaluar si los productos tienen esas vulnerabilidades. Esta herramienta permitiría detectar y por tanto eliminar la mayoría de las vulnerabilidades más triviales, evaluar la calidad de los productos y concienciar a los proveedores sobre la necesidad de no tener en sus productos ciertas vulnerabilidades.

Para ello se basa en la construcción y liberación de un conjunto de pruebas que detectan vulnerabilidades. Al aplicar este conjunto de pruebas tanto los proveedores como los clientes pueden evaluar en cierto grado la vulnerabilidad de los sistemas y poder hacer comparaciones entre distintos productos competidores. El conjunto de pruebas debería ser liberado bajo la licencia pública como GPL, sin coste. De esta forma cualquiera podría utilizarlas.

Esos test podrían ser reaprovechados usándolos en pruebas de regresión de los futuros productos evitando la reaparición de vulnerabilidades.

 Fases
Fases implicadas en el modelo:
 Fase de **creación**.- En esta fase se selecciona el área o áreas donde se va a poner el interés (sólo se evaluará la seguridad sobre estas áreas), se crea el material de test y se empaqueta. A continuación se prueban los distintos productos que implementan la funcionalidad que estamos tratando mediante el conjunto de prueba generado.
 Fase de **pre-release**.- Se notifica a los respectivos proveedores de las vulnerabilidades descubiertas y se les distribuye los test de prueba para que puedan arreglar la funcionalidad requerida. Se establece un proceso de comunicación y coordinación de consultoría y construcción del arreglo (parche). Si es necesario se construyen exploits para motivar al proveedor y se le entregan de forma privada. A los proveedores afectados no se les revela información sobre lo que afecta a otros competidores. Se establece un periodo de gracia hasta pasar a la siguiente fase para dar tiempo a los proveedores para corregir sus vulnerabilidades.
 Fase de **release**.- Se hace públic el conjunto de pruebas. Los detalles sobre cada proveedor se mantieneb en secreto y no se liberan exploits (no hay revelación completa). Sólo se libera el material que permite indicar las vulnerabilidades potenciales.

 Referencias
