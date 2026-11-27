---
type: Artículo de enciclopedia
title: Modelo Bell-LaPadula
description: En seguridad informática, el modelo de seguridad Bell-Lapadula, llamado así por sus creadores David Elliott Bell y Leonard J.
resource: https://es.wikipedia.org/wiki/Modelo_Bell-LaPadula
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelo_Bell-LaPadula"}
license: CC BY-SA 4.0
id: eswiki-Modelo_Bell-LaPadula
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelo Bell-LaPadula

En **seguridad informática**, el modelo de seguridad **Bell-Lapadula**, llamado así por sus creadores David Elliott Bell y Leonard J. LaPadula, consiste en dividir el permiso de acceso de los usuarios a la información en función de etiquetas de seguridad. Por ejemplo, en sistemas militares norteamericanos, categorizándola en 4 niveles: no clasificado, confidencial, secreto y ultrasecreto.

 Características
Este modelo se centra en la confidencialidad y no en la integridad. Se distinguen 2 tipos de entidades, sujetos y objetos. Se define estados seguros y se prueba que cualquier transición se hace de un estado seguro a otro.
Un estado se define como estado seguro si el único modo de acceso permitido de un sujeto a un objeto está en concordancia con la política de seguridad. Para determinar si un modo de acceso específico está permitido, se compara la acreditación de un sujeto con la clasificación del objeto (más precisamente, la combinación de la clasificación y el conjunto de compartimientos) para determinar si el sujeto está autorizado para el modo de acceso especificado. El esquema de clasificación/acreditación se expresa en términos de un retículo. El modelo define 2 reglas de control de acceso mandatorio (MAC) y una regla de control de acceso discrecional (DAC) con 3 propiedades:
 Propiedad de seguridad simple: Un sujeto de un determinado nivel de seguridad no puede leer un objeto perteneciente a un nivel de seguridad más alto.
 Propiedad (Propiedad estrella): Un sujeto de un determinado nivel de seguridad no puede escribir un objeto perteneciente a un nivel de seguridad más bajo. (También llamada propiedad de confinamiento).
 Propiedad de seguridad discrecional: Se utiliza una matriz de acceso para especificar el control de acceso discrecional.

Con Bell-La Padula, los usuarios pueden crear contenido sólo en su nivel de seguridad o por encima (i.e, investigadores en el nivel secreto pueden crear archivos secretos o super secretos pero no archivos públicos). Inversamente, los usuarios pueden ver solamente contenido de su propio nivel o inferior.

 Principio de tranquilidad

El principio de tranquilidad del modelo de Bell-La Padula establece que la clasificación de un sujeto u objeto no cambia mientras está siendo referenciada.
Hay 2 formas para el principio de tranquilidad: el *principio de tranquilidad fuerte* establece que los niveles de seguridad no cambian durante la operación normal del sistema y el *principio de tranquilidad débil* establece que los niveles de seguridad no cambian de una manera que violen las reglas de una dada política de seguridad.

 Véase también

 Modelo Biba
 Modelo Clark-Wilson
 Modelo de la matriz de acceso
 Modelo HRU
 Modelo Take-Grant
 Modelo Alan-Turing

 Referencias
