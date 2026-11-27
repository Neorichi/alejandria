---
type: Artículo de enciclopedia
title: Aislamiento de procesos
description: "En seguridad informática, el aislamiento de procesos, espacio o entorno aislado (en inglés \"Sandboxing\") es un mecanismo de seguridad que aísla un programa en ejecución, simulando un entorno virtual, para evitar que …"
resource: https://es.wikipedia.org/wiki/Aislamiento_de_procesos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Aislamiento_de_procesos"}
license: CC BY-SA 4.0
id: eswiki-Aislamiento_de_procesos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Aislamiento de procesos

En seguridad informática, el **aislamiento de procesos**, **espacio** o **entorno aislado** (en inglés "*Sandboxing*") es un mecanismo de seguridad que aísla un programa en ejecución, simulando un entorno virtual, para evitar que pueda afectar a una máquina real.

A menudo se utiliza para ejecutar programas o códigos no probados o no confiables, generalmente ofrecidos por terceros, para comprobar si contienen un virus u otro código malicioso, sin arriesgarse a dañar la máquina anfitriona o el sistema operativo.

Una forma de conseguir el aislamiento es mediante la **emulación**. Componentes como la CPU, la memoria o los dispositivos de red y de entrada/salida son simulados dentro del entorno aislado. El anfitrión (la máquina física) le ofrece al huésped (el proceso aislado) un conjunto reducido y estrechamente controlado de recursos, con el objetivo de hacerle creer que está siendo ejecutado sobre una máquina real, pero sin darle acceso directo a estos componentes. De esta forma, el entorno aislado puede monitorear la actividad del proceso para, por ejemplo, determinar si tiene un comportamiento malicioso.

Al proporcionar un entorno altamente controlado, los entornos aislados pueden considerarse un ejemplo específico de virtualización.

Algunos ejemplos de aislamiento son:

 Los applets son programas que se ejecutan en contención dentro de una máquina virtual o un intérprete de *scripts* que haga el aislamiento. En esquemas de uso de aplicaciones de retransmisión, el *applet* es descargado en el cliente remoto y puede comenzar a ejecutarse antes de que llegue en su totalidad. Los applets son comunes en los navegadores web, los cuales usan ese mecanismo para ejecutar de manera segura código no confiable contenido en páginas web. Las tres implementaciones de applet más conocidas —Adobe Flash, Java y Silverlight— permiten al menos una ventana rectangular con la que es posible la interactividad con el usuario y brinda algo de espacio persistente —todo con el permiso del usuario—.
 Android fue uno de los primeros sistemas operativos convencionales en implementar el aislamiento completo de aplicaciones, mediante la asignación de un id de usuario linux propio a cada aplicación. GrapheneOS refuerza el aislamiento de aplicaciones para lograr una capa adicional de seguridad y evitar aplicaciones potencialmente maliciosas y, a diferencia del Android estándar, permite el aislamiento de todas las aplicaciones del sistema operativo.
 Una celda es un conjunto de límites en los recursos impuesto a los programas por el núcleo de un sistema operativo. Puede incluir cuotas máximas de entrada/salida, cuotas de espacio en disco, restricciones al acceso a redes y al sistema de archivos. Las celdas son usadas comúnmente en servidores virtualizados.
 Las máquinas virtuales emulan un ordenador en su totalidad, en el cual un sistema operativo convencional puede arrancar y funcionar como si estuviera sobre *hardware* real. El sistema operativo cliente está aislado en el sentido de que no corre nativamente en la máquina anfitriona y puede acceder únicamente a los recursos —muchas veces virtuales— que le proporciona el emulador.
 Aislamiento en máquinas nativas: Los investigadores de seguridad utilizan frecuentemente tecnologías de aislamiento para analizar el comportamiento de *software* malicioso. Al crear un ambiente que simula o replica los sistemas de escritorio objetivo, se puede evaluar cómo el software malicioso infecta y compromete el equipo.

 Véase también
 Sandboxie
 Sandboxed (biblioteca de programación C++ basada en Chrome Sandbox)

 Referencias
