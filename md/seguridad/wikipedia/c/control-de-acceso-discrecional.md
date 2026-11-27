---
type: Artículo de enciclopedia
title: Control de acceso discrecional
description: "En seguridad informática, control de acceso discrecional (DAC) es una especie de control de acceso definidos por los Criterios de Trusted Computer System Evaluation (TCSEC) \"como una forma de restringir el acceso a …"
resource: https://es.wikipedia.org/wiki/Control_de_acceso_discrecional
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Control_de_acceso_discrecional"}
license: CC BY-SA 4.0
id: eswiki-Control_de_acceso_discrecional
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Control de acceso discrecional

En seguridad informática, **control de acceso discrecional** (**DAC**) es una especie de control de acceso definidos por los Criterios de Trusted Computer System Evaluation (TCSEC) "como una forma de restringir el acceso a objetos basados en la identidad de los sujetos y / o grupos a los que pertenecen. Los controles son discrecionales en el sentido de que un sujeto con un permiso de acceso seguro es capaz de pasar a ese permiso (quizás indirectamente) a cualquier otro sujeto (a menos restringido por el control de acceso obligatorio)".

El control de acceso discrecional se define generalmente en oposición al control de acceso obligatorio (MAC) (algunas veces llamado *control de acceso no-discrecional*). A veces, un sistema en su conjunto dice tener control de acceso *discrecional* o *puramente discrecional* como una forma de indicar que carece de control mandatorio. Por otro lado, sistemas que indican implementaciones de MAC o DAC en forma simultánea, tienen DAC como una categoría de control de acceso donde los usuarios pueden pasar de uno a otro y MAC como una segunda categoría de control de acceso que impone restricciones a la primera.

 Implementaciones
En la práctica, el significado del término no se limita a la definición del estándar TCSEC ya que éste no impone un concepto de implementación. Por esto, existen al menos dos implementaciones: con dueño (*owner*) como implementación general y con capacidades, cómo evolución.

 Implementación con dueño
El término DAC suele ser utilizado en contextos donde cada objeto tiene un *dueño* que controla los permisos para acceder al objeto, probablemente porque la mayoría de los sistemas que implementan DAC usan el concepto de dueño. Pero la definición del TCSEC no habla nada sobre dueños, por lo que técnicamente en sistemas de control de acceso no es necesario tener el concepto de dueño para ajustarse a la definición de DAC del TCSEC.

Los usuarios (dueños) tienen en la implementación DAC la potestad de determinar las políticas y/o asignar los atributos de seguridad. Un ejemplo de esto es el sistema de permisos del Unix File System y su sistema de usuarios y grupos con permisos de lectura - escritura - ejecución para los objetos (archivos y directorios).

 Implementación con capacidades
Los sistemas que implementan seguridad por capacidades se describen como que proveen control de acceso discrecional porque permiten a los usuarios transferir sus accesos a otros usuarios, aunque el sistema de control de capacidades no está fundamentado en una restricción del acceso "basado en la identidad de los sujetos" (los sistemas por capacidades no permiten, en general, que los permisos sean pasados a otro usuario; el sujeto que espera recibir sus permisos primero tiene que tener acceso a recibir las capacidades de otro sujeto. Los sujetos no pueden pasar al acceso de cualquier sujeto en el sistema).

 Véase también
 Control de Acceso
 Control de Acceso Obligatorio (MAC)
 Control de Acceso basado en roles (RBAC)
 Seguridad por capacidades
 XACML eXtensible Access Control Markup Language

 Referencias

 Enlaces externos
 . *The Inevitability of Failure: The Flawed Assumption of Security in Modern Computing Environments*. In Proceedings of the 21st National Information Systems Security Conference, pp. 303–14, oct. 1998. PDF versión
