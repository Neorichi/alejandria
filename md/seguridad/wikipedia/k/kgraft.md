---
type: Artículo de enciclopedia
title: KGraft
description: kGraft es una característica del núcleo Linux que implementa la aplicación de parches en vivo de un kernel en ejecución, lo que permite que se apliquen parches del kernel mientras el kernel aún se está ejecutando.
resource: https://es.wikipedia.org/wiki/KGraft
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/KGraft"}
license: CC BY-SA 4.0
id: eswiki-KGraft
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# KGraft

**kGraft** es una característica del núcleo Linux que implementa la aplicación de parches en vivo de un kernel en ejecución, lo que permite que se apliquen parches del kernel mientras el kernel aún se está ejecutando. Al evitar la necesidad de reiniciar el sistema con un nuevo núcleo que contiene los parches deseados, kGraft apunta a maximizar el tiempo de actividad y disponibilidad del sistema. Al mismo tiempo, kGraft permite que las actualizaciones de seguridad relacionadas con el kernel se apliquen sin diferirlas a los tiempos de inactividad programados. Internamente, kGraft permite que se reemplacen funciones completas en un kernel en ejecución con sus versiones parcheadas, haciendo esto de forma segura mediante el uso selectivo de las versiones originales de las funciones para asegurar la consistencia del proceso mientras se realiza la aplicación de parches en vivo.

kGraft es desarrollado por SUSE, con su código fuente bajo los términos de las versiones dos y tres de la Licencia Pública General de GNU (GPL). En abril de 2014, se envió kGraft para su inclusión en la línea principal del núcleo Linux, y los fundamentos minimalistas para la aplicación de parches en vivo se fusionaron en la línea principal del núcleo Linux en la versión 4.0 del kernel, que se publicó el 12 de abril de 2015, en conjunto con kpatch.

 Internos
Internamente, kGraft consta de dos partes.  el módulo núcleo del kernel ejecuta el mecanismo de parcheo en vivo al alterar el funcionamiento interno del kernel, mientras que las utilidades del espacio de usuario preparan módulos individuales de kernel de parches en vivo desde las fuentes. El parche en vivo del kernel se realiza en el nivel de la función, lo que significa que kGraft puede reemplazar funciones completas en el kernel en ejecución con sus versiones parcheadas, mientras que depende de los mecanismos y la infraestructura establecidos por ftrace para "enrutar" las versiones antiguas de las funciones. No es posible realizar cambios en las estructuras de datos internas del kernel; sin embargo, los parches de seguridad, que son uno de los candidatos naturales para ser utilizados con kGraft, rara vez contienen cambios en las estructuras de datos del kernel.

Al aplicar parches activos, kGraft no requiere que se detenga un kernel en ejecución para que se introduzcan en él versiones parcheadas de funciones. En lugar de reemplazar las funciones de forma atómica, kGraft proporciona "vistas del mundo" (o "universos") consistentes a los procesos del espacio de usuario, a los hilos del núcleo y a los controladores de interrupciones, que se monitorean durante su ejecución para que se puedan seguir utilizando las versiones originales de las funciones del núcleo parcheadas. Para lograrlo, kGraft mantiene las versiones originales de las funciones parcheadas en forma de lectura-copia-actualización (RCU), y selecciona dinámicamente entre las versiones original y parcheada según el proceso, el hilo del kernel o el controlador de interrupciones que las ejecuta. Más específicamente, las versiones originales de funciones se siguen utilizando en el momento cuando se aplica un parche en vivo para los procesos ejecutando actualmente en el espacio del núcleo, para los hilos del núcleo hasta que alcanzan el punto de terminación, y para que se ejecuta actualmente interrupción manipuladores

Debido a su diseño, kGraft no introduce latencia adicional al aplicar parches en vivo. Como inconveniente, las versiones originales de las funciones del kernel parcheadas pueden ser mantenidas durante largos períodos de tiempo en caso de que haya procesos que permanezcan demasiado tiempo dentro del espacio del kernel; por ejemplo, un proceso puede esperar la E/S en un socket de red. Además, como las versiones originales y parcheadas de las funciones pueden ejecutarse en paralelo, pueden surgir problemas si utilizan las estructuras de datos internas del kernel de diferentes maneras.

 Historia
SUSE anunció kGraft en enero de 2014 y lo lanzó públicamente en marzo de 2014 bajo los términos de la versión de Licencia Pública General de GNU   2 (GPLv2) para la parte del kernel, y bajo los términos de la versión 3 (GPLv3 ) para la parte del espacio de usuario. Se lanzó poco después de que Red Hat lanzó su propia implementación de parches en vivo del kernel llamada kpatch. kGraft pretende fusionarse en la línea principal del núcleo Linux, y se presentó para su inclusión en abril de 2014.

kGraft se puso a disposición de SUSE Linux Enterprise Server 12 el 18 de noviembre de 2014, como una característica adicional llamada *SUSE Linux Enterprise Live Patching*.

Fundamentos minimalistas para la aplicación del parche en vivo del kernel se fusionaron en la línea principal del núcleo Linux en la versión del kernel 4.0, que se lanzó el 12 de abril de 2015. Esos fundamentos, basados principalmente en la funcionalidad ftrace del kernel, forman un núcleo común capaz de soportar parches en vivo tanto por kGraft como por kpatch, al proporcionar una interfaz de programación de aplicaciones (API) para los módulos del kernel que contienen parches y una interfaz binaria de aplicaciones (ABI) para las utilidades de gestión del espacio de usuario. Sin embargo, el núcleo común incluido en el núcleo Linux 4.0 solo es compatible con la arquitectura x86 y no proporciona ningún mecanismo para garantizar la coherencia a nivel de la función mientras se aplican los parches activos.

Desde abril de 2015, se está trabajando en la migración de kGraft a línea principal del núcleo Linux. Sin embargo, la implementación de los mecanismos de coherencia de nivel de función requeridos se ha retrasado porque las pilas de llamadas proporcionadas por el núcleo Linux pueden ser poco confiables en situaciones que involucran código de ensamblaje sin marcos de pila adecuados; como resultado, el trabajo de portabilidad continúa en curso a. En un intento por mejorar la confiabilidad de las pilas de llamadas del kernel, una verificación de la sanidad especializada. En un intento por mejorar la confiabilidad de las pilas de llamadas del kernel, una verificación de sanidad especializada llamada stacktool también ha sido desarrollada.

 Véase también

 Actualización dinámica de software, un campo de investigación centrado en actualizar programas mientras se ejecutan
 kexec, un método para cargar un núcleo Linux completamente nuevo desde un sistema en ejecución
 Ksplice y KernelCare, otras tecnologías de parches en vivo del núcleo Linux desarrolladas por Ksplice, Inc. (más tarde adquiridas por Oracle) y CloudLinux, respectivamente

 Referencias

 Enlaces externos
