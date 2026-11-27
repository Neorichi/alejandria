---
type: Artículo de enciclopedia
title: Bomba fork
description: "Una bomba de tenedor es una forma de ataque del tipo denegación de servicio sobre un computador implementando una operación tenedor o alguna otra funcionalidad equivalente mediante la cual un proceso es capaz de …"
resource: https://es.wikipedia.org/wiki/Bomba_fork
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Bomba_fork"}
license: CC BY-SA 4.0
id: eswiki-Bomba_fork
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Bomba fork

Una **bomba de tenedor** es una forma de ataque del tipo denegación de servicio sobre un computador implementando una operación tenedor o alguna otra funcionalidad equivalente mediante la cual un proceso es capaz de autorreplicarse. La bomba de tenedor es considerado un wabbit ya que no se autorreplica de la misma forma que los gusanos o los virus. Su efecto se basa en la suposición de que el número de programas y procesos que se ejecutan simultáneamente en un ordenador tiene un límite.

Una bomba de tenedor funciona creando una gran cantidad de procesos muy rápidamente con el objetivo de saturar el espacio disponible en la lista de procesos mantenida por el sistema operativo del computador. Si la tabla de procesos se llega a saturar, entonces no se pueden iniciar nuevos programas hasta que no se cierre alguno. En el caso de que esto suceda, es muy poco probable que se pueda iniciar un programa útil ya que los procesos de la bomba estarán esperando para poder crear nuevos procesos a la primera oportunidad que se les conceda.

Las bombas tenedor no sólo ocupan espacio dentro de la lista de procesos, también consumen tiempo de proceso y memoria de la máquina donde se ejecutan. Como resultado de esto, los ordenadores se vuelven lentos e incluso se pueden volver inutilizables dada la falta de memoria y la imposibilidad de aprovechar el procesador.

 Dificultad de solución

Una vez una bomba de tenedor ha sido activada de forma "satisfactoria" en un sistema, puede que no sea posible ejecutar ninguna tarea sin un reinicio del sistema, ya que la única solución es detener todos los procesos iniciados por ella. Normalmente se requiere cargar un programa adicional para "matar" procesos, lo que puede no ser posible si no hay posiciones vacías dentro de la tabla de procesos o espacio dentro de las estructuras de memoria.

 Prevención
Una forma de prevenir el ataque de una bomba de tenedor es limitar el número de procesos que un usuario puede ejecutar. Cuando un proceso intenta crear otro proceso y el propietario de dicho proceso ya posee la cantidad máxima de procesos que se le ha asignado, el intento de creación del nuevo proceso falla. El máximo número de procesos asignado a cada usuario debe ser lo suficientemente bajo para poder resistir la ejecución simultánea de una bomba de tenedor por cada usuario y dejar libres los suficientes recursos como para poder restaurar el sistema.

Téngase en cuenta que la ejecución accidental de una bomba de tenedor es altamente improbable en más de un usuario a la vez.

Los sistemas de tipo Unix típicamente tienen establecido este límite, controlado con el comando *ulimit* del shell. En los kernel Linux existe una variable llamada **RLIMIT_NPROC**, que indica la cantidad máxima de procesos que se puede ejecutar. Si un proceso intenta llamar a la función tenedor y el usuario propietario del proceso ya tiene igual o más procesos que los indicados en **RLIMIT_NPROC** la llamada a la función fallará.

Otra solución implica la detección de bombas tenedor antes de su ejecución por parte del sistema operativo, aunque eso supone más gasto de recursos por parte del sistema. Existe un módulo para el Kernel de Linux.

 Ejemplo de una bomba de tenedor
Código fuente de una bomba de tenedor programada en Batch funcional en cualquier versión de Microsoft Windows:

O bien, una reacción más rápida:

Código fuente de una bomba de tenedor programada en UNIX C o C++:

Bomba de tenedor para bash de linux

O de forma larga

En Perl:

En Python:

En Ruby:

 Véase también
 Fork
 Malware

 Referencias
