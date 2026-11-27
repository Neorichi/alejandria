---
type: Artículo de enciclopedia
title: Condición de carrera
description: Condición de carrera o condición de secuencia (del inglés race condition) es una expresión usada en electrónica y en programación.
resource: https://es.wikipedia.org/wiki/Condición_de_carrera
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Condición_de_carrera"}
license: CC BY-SA 4.0
id: eswiki-Condición_de_carrera
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Condición de carrera

**Condición de carrera o condición de secuencia** (del inglés *race condition*) es una expresión usada en electrónica y en programación.
Cuando la salida o estado de un proceso es dependiente de una secuencia de eventos que se ejecutan en orden arbitrario y van a trabajar sobre un mismo recurso compartido, se puede producir un error cuando dichos eventos no *llegan* (se ejecutan) en el orden que el programador esperaba. El término se origina por la similitud de dos procesos *compitiendo*  en carrera por llegar antes que el otro, de manera que el estado y la salida del sistema dependerán de cuál *llegó* antes, pudiendo provocarse inconsistencias y comportamientos impredecibles y no compatibles con un sistema determinista.
En determinados escenarios, la gran velocidad de ejecución de un hilo no es suficiente para garantizar que operaciones concurrentes den resultados esperados. Se pueden dar condiciones de carrera a nivel de proceso o incluso a nivel de sistema cuando éste está distribuido.

A modo de ejemplos de alto nivel: un sistema mal diseñado de reserva de entradas podría ocasionar que dos usuarios accediendo desde la web a la vez, reserven legítimamente la misma butaca. O un sistema de conteo automático de plazas libres de una plaza de estacionamiento en sus barreras de entrada y salida de vehículos podría indicar que está totalmente vacío cuando realmente está lleno (o viceversa). De igual forma, dos personas ingresando y retirando efectivo a la vez de una misma cuenta bancaria podrían ver su saldo incrementado o por el contrario su ingreso realizado pero no materializado en saldo disponible.
Si bien son situaciones que pudieran ser improbables, son posibles y pueden ser y han de ser evitadas en el desarrollo de software.

Si los procesos que están en condición de carrera son correctamente sincronizados, todo debería funcionar correctamente, por lo que el resultado será el esperado. Múltiples procesos se encuentran en condición de carrera si el resultado de los mismos depende del orden de su llegada, y si no son correctamente sincronizados puede producirse una corrupción de datos que puede derivar incluso en un problema de seguridad del sistema capaz de ser explotado de forma malintencionada. Análogamente, en circuitos electrónicos se da una condición de carrera cuando la salida de un sistema o subsistema depende del orden en que se hayan mandado las solicitudes de activación o desactivación de sus componentes.

La naturaleza imprevisible de las condiciones de carrera da lugar en muchas ocasiones a la aparición de bugs de manera repentina que normalmente no ocurren durante el testeo de un software. Además, pueden ser difícilmente trazables, difícilmente replicables de manera controlada o visibles incluso con herramientas de depuración de programas.

 Véase también
 Control de concurrencia
 Bloqueo mutuo
 Sincronización
 Riesgo (electrónica)

 Enlaces externos
 Starvation and Critical Race Analyzers for Ada
 VHDL example
 Paper "Algorithms for the Optimal State Assignment of Asynchronous State Machines" by Robert M. Fuhrer, Bill Lin and Steven M. Nowick
 Paper "A Novel Framework for Solving the State Assignment Problem for Event-Based Specifications" by Luciano Lavagno, Cho W. Moon, Robert K. Brayton and Alberto Sangiovanni-Vincentelli
 Article "Secure programmer: Prevent race conditions—Resource contention can be used against you" by David A. Wheeler
 Chapter "Avoid Race Conditions" (Secure Programming for Linux and Unix HOWTO)
 Race conditions, security, and immutability in Java, with sample source code and comparison to C code, by Chiral Software
 Interview with Dmitriy Vyukov - the author of Relacy Race Detector (RRD)
