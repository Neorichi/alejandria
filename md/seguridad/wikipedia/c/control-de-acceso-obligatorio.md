---
type: Artículo de enciclopedia
title: Control de acceso obligatorio
description: "El control de acceso obligatorio, también conocido por las siglas MAC (del inglés Mandatory access control), es un modelo de control del acceso de usuarios a recursos (objetos, archivos, sistemas informáticos,...) que …"
resource: https://es.wikipedia.org/wiki/Control_de_acceso_obligatorio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Control_de_acceso_obligatorio"}
license: CC BY-SA 4.0
id: eswiki-Control_de_acceso_obligatorio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Control de acceso obligatorio

El **control de acceso obligatorio**, también conocido por las siglas **MAC** (del inglés *Mandatory access control*), es un modelo de control del acceso de usuarios a recursos (objetos, archivos, sistemas informáticos,...) que se basa en los derechos de accesos establecidos por una autoridad central. La filosofía subyacente es que la información pertenece a la organización (en lugar de los miembros individuales de ella), y es la organización la que controla la política de seguridad.

Se establecen reglas de cumplimiento obligatorio que protegen el acceso a los recursos (lectura, cambios...) por parte de usuarios no autorizados. Cada usuario puede acceder solamente a los recursos a los que está autorizado Cuando un usuario intenta acceder a los datos, el sistema evalúa la solicitud y la acepta o la deniega.

 Ejemplos

Ejemplos del uso de políticas de acceso obligatorio son:

 **Sistemas de seguridad multinivel** o **MLS** (del inglés *Multiple Level of Security*). Son el tipo más simple de MAC. A cada recurso se le asigna un nivel de seguridad en función del grado de daño que podría sufrir el sistema si el recurso es indebidamente accedido, estableciendo una jerarquía de más a menos nivel de seguridad. A cada usuario se le asigna un nivel de confianza que le autoriza el acceso a recursos clasificados de hasta cierto nivel de seguridad. Por ejemplo, podríamos tener la típica clasificación de seguridad "No_clasificado < Confidencial < Secreto < Alto_secreto", clasificar los recursos en esos niveles y determinar para cada usuario hasta que nivel pueden tener acceso. Ejemplos de este tipo de política de acceso son el **modelo Bell-LaPadula** (establece los niveles de seguridad basándose en criterios de confidencialidad) y el **modelo Biba** (establece los niveles de seguridad basándose en criterios de integridad) .
 **Sistema de seguridad multicategoría** o **MCS** (del inglés *Multi-Category Security*). Es un subconjunto de la seguridad multinivel (MLS). Los usuarios se clasifican en categorías que indican que es lo que tienen que conocer. El administrador decide en qué categorías se sitúan los usuarios. Los usuarios pueden controlar los recursos de su propiedad, añadiéndolos o quitándolos de cualquier categoría de las que están ellos. Para acceder a un recurso, las categorías en las que se encuentra el usuario deben ser las mismas o un superconjunto de las categorías del recurso.
 **Sistemas de seguridad multilaterales** también conocidos como **Sistemas de seguridad de compartimentación**. Se usa cuando dentro del mismo nivel de seguridad no se quiere que los recursos sean accesibles a todos los usuarios con permiso en ese nivel de acceso. El acceso se organiza en segmentos o compartimentos, y dentro de esos puede hay niveles de protección de tipo multinivel. Esta forma es como funcionan los departamentos de una empresa. Por ejemplo, en una compañía consultora una persona que es consultor en el Banco1 no debería tener acceso a los datos del Banco2. Otro ejemplo serían las agencias de espionaje: Los nombres de los agentes que trabajan en un país A debería ser secreto para los usuarios del departamento responsable del espionaje del país B. Ejemplos de este tipo de política de acceso son el **Modelo Brewer-Nash** y el **Modelo de la British Medical Association** (**modelo MBA**).
**Modelo Clark-Wilson**. Enfocado en mantener la integridad en base permitir solo transacciones adecuadas las cuales están divididas en subpartes que tienen que estar realizadas por entidades independientes (sin colusión entre agentes que trabajan en diferentes subpartes). Esta política está inspirada en como empresas como los bancos aseguran la integridad del saldo de sus clientes.

 Referencias
