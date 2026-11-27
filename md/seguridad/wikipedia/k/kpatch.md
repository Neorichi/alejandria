---
type: Artículo de enciclopedia
title: Kpatch
description: kpatch es una característica del núcleo Linux que implementa la aplicación de parches en vivo de un kernel en ejecución, lo que permite que los parches del kernel se apliquen mientras el kernel aún se está ejecutando.
resource: https://es.wikipedia.org/wiki/Kpatch
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Kpatch"}
license: CC BY-SA 4.0
id: eswiki-Kpatch
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Kpatch

**kpatch** es una característica del núcleo Linux que implementa la aplicación de parches en vivo de un kernel en ejecución, lo que permite que los parches del kernel se apliquen mientras el kernel aún se está ejecutando. Al evitar la necesidad de reiniciar el sistema con un nuevo kernel que contiene los parches deseados, kpatch apunta a maximizar el tiempo de actividad y disponibilidad del sistema. Al mismo tiempo, kpatch permite que las actualizaciones de seguridad relacionadas con el kernel se apliquen sin diferirlas a los tiempos de inactividad programados. Internamente, kpatch permite que se reemplacen funciones completas en un kernel en ejecución con sus versiones parcheadas, haciendo esto de forma segura al detener todos los procesos en ejecución mientras se realiza la aplicación de parches en vivo.

kpatch es desarrollado por Red Hat, con su código fuente bajo los términos de la Licencia Pública General de GNU versión 2 (GPLv2). En mayo de 2014, se envió kpatch para su inclusión en la línea principal del núcleo Linux, y los fundamentos minimalistas para la aplicación de parches en vivo se fusionaron en la línea principal del núcleo Linux en la versión 4.0 del kernel, que se publicó el 12 de abril de 2015.

 Internos

Internamente, kpatch consta de dos partes: el módulo ejecuta el mecanismo de parcheo en vivo al alterar el funcionamiento interno del kernel, mientras que un conjunto de utilidades de espacio de usuario prepara módulos individuales de kernel desde fuentes diferentes y administra su aplicación. El parcheo en vivo del kernel se realiza a nivel de función, lo que significa que kpatch puede reemplazar funciones enteras en el kernel en ejecución con sus versiones parcheadas utilizando la infraestructura proporcionada por  para "enrutar" versiones antiguas de funciones. De esta manera, los parches también se pueden deshacer fácilmente. No es posible realizar cambios en las estructuras de datos internas del kernel; sin embargo, los parches de seguridad, que son uno de los candidatos naturales para ser utilizados con kpatch, rara vez contienen cambios en las estructuras de datos del kernel.

kpatch garantiza que los parches activos se apliquen de forma atómica y segura deteniendo todos los procesos en ejecución mientras se aplica el parche activo, y asegurando que ninguno de los procesos detenidos se ejecute dentro de las funciones que se van a parchear. Este enfoque simplifica todo el mecanismo de parcheo en vivo y previene ciertos problemas asociados con la forma en que las versiones originales y parcheadas de las funciones utilizan las estructuras de datos. Como inconveniente, este enfoque también deja la posibilidad de que falle un parche activo, e introduce una pequeña cantidad de latencia necesaria para detener todos los procesos en ejecución.

 Historia
Red Hat anunció y lanzó públicamente kpatch en febrero de 2014 bajo los términos de la versión de Licencia Pública General de GNU versión 2 (GPLv2), poco antes de que SUSE lanzara su propia implementación de parches en vivo del kernel llamada kGraft. kpatch se fusionó con la línea principal del núcleo Linux y se presentó para su inclusión en mayo de 2014.

kpatch ha sido incluido en Red Hat Enterprise Linux 7.0, lanzado el 10 de junio de 2014, como una vista previa de la tecnología.

Fundamentos minimalistas para la aplicación del parche en vivo del kernel se fusionaron en la línea principal del núcleo Linux en la versión del kernel 4.0, que se lanzó el 12 de abril de 2015. Esos fundamentos, basados principalmente en la funcionalidad ftrace del kernel, forman un núcleo común capaz de soportar parches en vivo tanto por kpatch como por kGraft, al proporcionar una interfaz de programación de aplicaciones (API) para módulos de kernel que contienen parches y una interfaz binaria de aplicaciones (ABI). para las utilidades de gestión del espacio de usuario. Sin embargo, el núcleo común incluido en el núcleo Linux 4.0 solo es compatible con la arquitectura x86 y no proporciona ningún mecanismo para garantizar la coherencia a nivel de la función mientras se aplican los parches activos.

Desde abril de 2015, hay trabajos en portar kpatch al núcleo común de parches en vivo proporcionada por la línea principal del núcleo Linux. Sin embargo, la implementación de los mecanismos de coherencia de nivel de función requeridos se ha retrasado porque las pilas de llamadas proporcionadas por el núcleo Linux pueden ser poco confiables en situaciones que involucran código de ensamblaje sin marcos de pila adecuados; como resultado, el trabajo de portabilidad continúa en curso a septiembre de 2015. En un intento por mejorar la confiabilidad de las pilas de llamadas del kernel, una verificación de sanidad especializada llamada stacktool también ha sido desarrollada.

 Véase también

kexec, un método para cargar un núcleo Linux completamente nuevo desde un sistema en ejecución
 Ksplice y KernelCare, otras tecnologías de parches en vivo del núcleo Linux desarrolladas por Ksplice, Inc. (más tarde adquiridas por Oracle) y CloudLinux, respectivamente

 Referencias

 Enlaces externos

 Código fuente de kpatch en GitHub
