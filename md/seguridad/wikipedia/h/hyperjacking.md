---
type: Artículo de enciclopedia
title: Hyperjacking
description: Hyperjacking es un tipo de ataque de escape de máquina virtual en el que un pirata informático toma control malicioso sobre el hipervisor que crea el entorno virtual dentro de un host de máquina virtual (VM).
resource: https://es.wikipedia.org/wiki/Hyperjacking
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Hyperjacking"}
license: CC BY-SA 4.0
id: eswiki-Hyperjacking
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Hyperjacking

***Hyperjacking*** es un tipo de ataque de **escape de máquina virtual** en el que un pirata informático toma control malicioso sobre el hipervisor que crea el entorno virtual dentro de un host de máquina virtual (VM). El objetivo del ataque es apuntar al sistema operativo anfitrión que está por debajo de las máquinas virtuales, para que el programa del atacante pueda ejecutarse y las aplicaciones en las máquinas virtuales por encima de él sean completamente ajenas a su presencia.

 Visión general

*Hyperjacking* consiste en instalar un hipervisor falso y malicioso que puede administrar todo el sistema del servidor. Las medidas de seguridad regulares no son efectivas porque el sistema operativo no será consciente de que la máquina ha sido comprometida. En el *hyperjacking*, el hipervisor opera específicamente en modo oculto y se ejecuta debajo de la máquina anfitrión, hace que sea más difícil de detectar y es más probable que obtenga acceso a los servidores informáticos donde puede afectar el funcionamiento de toda la organización. Si el hacker obtiene acceso al hipervisor, todo lo que está conectado a ese servidor puede ser manipulado. El hipervisor representa un único punto de falla cuando se trata de la seguridad y protección de la información confidencial.

Para que un ataque de *hyperjacking* tenga éxito, un atacante tendría que tomar el control del hipervisor mediante los siguientes métodos:

 Inyectar un hipervisor malicioso debajo del hipervisor original.
 Obtención directa del control del hipervisor original.
 Ejecutar un hipervisor malicioso sobre un hipervisor existente

 Técnicas de mitigación
Algunas características de diseño básicas en un entorno virtual pueden ayudar a mitigar los riesgos de *hyperjacking*:

 La administración de seguridad del hipervisor debe mantenerse separada del tráfico regular. Esta es una medida más relacionada con la red que el propio hipervisor.
 Los sistemas operativos invitados nunca deben tener acceso al hipervisor. Las herramientas de administración no deben instalarse ni utilizarse desde el SO invitado.
 Actualizar el hipervisor regularmente.

 Ataques conocidos
A principios de 2015, no había habido ningún informe de una demostración real de un secuestro exitoso además de las pruebas de "prueba de concepto". La vulnerabilidad de VENOM (CVE-2015-3456) se reveló en mayo de 2015 y tenía el potencial de afectar a muchos centros de datos. Los ataques son raros debido a la dificultad de acceder directamente a los hipervisores; sin embargo, el hyperjacking es considerado una amenaza del mundo real.

 Referencias
