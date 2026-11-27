---
type: Artículo de enciclopedia
title: Control de acceso a red
description: "Control de acceso a red (del inglés Network Access Control, NAC) es un enfoque de la seguridad en redes de computadoras que intenta unificar la tecnología de seguridad en los equipos finales (tales como antivirus, …"
resource: https://es.wikipedia.org/wiki/Control_de_acceso_a_red
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Control_de_acceso_a_red"}
license: CC BY-SA 4.0
id: eswiki-Control_de_acceso_a_red
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Control de acceso a red

**Control de acceso a red** (del inglés ***Network Access Control***, NAC) es un enfoque de la seguridad en redes de computadoras que intenta unificar la tecnología de seguridad en los equipos finales (tales como antivirus, prevención de intrusión en hosts, informes de vulnerabilidades), usuario o sistema de autenticación y reforzar la seguridad de acceso a la red (red de acceso).

 Escenario
El control de acceso a red es un concepto de ordenador en red y conjunto de protocolos usados para definir como asegurar los nodos de la red antes de que estos accedan a la red. NAC puede integrar el proceso de remedio automático (corrigiendo nodos que no cumplen las normativas antes de permitirles acceso) en el sistema de red, permitiendo a la infraestructura de red como routers, switches y firewalls trabajar en conjunto con el back office y el equipamiento informático del usuario final para asegurar que el sistema de información está operando de manera segura antes de permitir el acceso a la red.

El objetivo del **control de acceso a red** es realizar exactamente lo que su nombre implica: control de acceso a la red con políticas, incluyendo pre-admisión, chequeo de políticas de seguridad en el usuario final y controles post-admisión sobre los recursos a los que pueden acceder en la red los usuarios y dispositivos, y que pueden hacer en ella.

 Objetivos del control de acceso a red
El control de acceso a red (NAC) representa una categoría emergente en productos de seguridad, su definición es controvertida y está en constante evolución. Los objetivos principales de este concepto se pueden resumir en:

**Mitigar** ataques de día cero

El propósito clave de una solución NAC es la habilidad de prevenir en los equipos finales la falta de antivirus, parches, o software de prevención de intrusión de hosts y acceder así a la red poniendo en riesgo a otros equipos de contaminación y expansión de gusanos informáticos.

**Refuerzo de políticas**
Las soluciones NAC permiten a los operadores de red definir políticas, tales como tipos de ordenadores o roles de usuarios con acceso permitido a ciertas áreas de la red, y forzarlos en switches y routers.

**Administración de acceso e identidad**
Donde las redes IPs convencionales refuerzan las políticas de acceso con base en direcciones IP, los dispositivos NAC lo realizan basándose en identidades de usuarios autenticados, al menos para usuarios finales de equipos portátiles y sobremesa.

 funciones

**Pre-admisión y Post-admisión**
Existen dos filosofías de diseño predominantes en NAC, basadas en políticas de refuerzo antes de ganar acceso a la red o después de hacerlo. En el primer caso denominado NAC de pre-admisión, las estaciones finales son inspeccionadas antes de permitirles el acceso a la red. Un caso típico de NAC pre-admisión sería el prevenir que equipos con antivirus no actualizados pudieran conectarse a servidores sensibles. Alternativamente, el NAC post-admisión crea decisiones de refuerzo basadas en acciones de usuario después de que a estos usuarios se les haya proporcionado el acceso a la red.

**Con agente vs sin agente**
La idea fundamental de la tecnología NAC es permitir a la red tomar decisiones de control de acceso basadas en inteligencia sobre los sistemas finales, por lo que la manera en que la red es informada sobre los sistemas finales es una decisión de diseño clave. Una diferencia clave entre sistemas NAC es si requieren agentes software para informar de las características de los equipos finales, o si por el contrario utilizan técnicas de escaneo e inventariado para discernir esas características remotamente.

**Solución, cuarentena y portal cautivo**
Los administradores de sistemas y redes despliegan productos NAC con la prevención de que a algunos clientes legítimos se les denegará el acceso a la red (si los usuarios nunca tuvieron antivirus desactualizados y sus sistemas están siempre actualizados, NAC no sería necesario). Por ello las soluciones NAC requieren de un mecanismo para remediar el problema del usuario final que le ha sido denegado el acceso a la red.

Las dos estrategias comunes para este remedio son redes de cuarentena y portales cautivos.

 Referencias

 Enlaces externos
Recursos NAC
