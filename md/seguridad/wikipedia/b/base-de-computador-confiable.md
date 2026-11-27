---
type: Artículo de enciclopedia
title: Base de computador confiable
description: "Una Base de computador confiable, también conocido por las siglas TCB (del inglés Trusted Computer Base), es un conjunto de elementos hardware, firmware y software que permiten a un sistema informático implementar los …"
resource: https://es.wikipedia.org/wiki/Base_de_computador_confiable
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Base_de_computador_confiable"}
license: CC BY-SA 4.0
id: eswiki-Base_de_computador_confiable
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Base de computador confiable

Una **Base de computador confiable**, también conocido por las siglas TCB (del inglés *Trusted Computer Base*), es un conjunto de elementos hardware, firmware y software que permiten a un sistema informático implementar los requisitos de seguridad establecidos. Cualquier cosa fuera del TCB puede ser malicioso.

En ordenadores de propósito general la TCB suele estar formada por la mayoría de los elementos hardware del sistema (excepto los dispositivos de E/S) y una parte del núcleo del sistema operativo. Entre las funciones del sistema operativo que se deben incluir dentro de la TCB se encuentran las relativas a creación de procesos, cambio de contexto, gestión de memoria y parte de la gestión de la E/S y del sistema de archivos.

Siempre se quiere que la TCB sea lo más pequeña posible de forma que nos podamos centrar en asegurar la seguridad de esa pequeña parte y que la seguridad del resto del sistema se apoye en ella.

Modelo de seguridad

La política de seguridad establecida como requisito del sistema no se suele implementar directamente en la TCB. En su lugar se recurre a lo que se llama **modelo de seguridad** que es una especificación formal de las funciones que la TCB llevará a cabo y gracias a las cuales se pueden probar la política de seguridad requerida. Es decir es el conjunto de reglas y prácticas que regulan cómo un sistema maneja, protege y distribuye la información.

Referencias
