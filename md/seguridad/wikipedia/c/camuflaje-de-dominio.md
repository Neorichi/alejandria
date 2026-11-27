---
type: Artículo de enciclopedia
title: Camuflaje de dominio
description: El Camuflaje de Dominio o Domain shadowing consiste en tomar el control de un dominio registrado consiguiendo las credenciales de administración para crear registros DNS de multitud de subdominios.
resource: https://es.wikipedia.org/wiki/Camuflaje_de_dominio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Camuflaje_de_dominio"}
license: CC BY-SA 4.0
id: eswiki-Camuflaje_de_dominio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Camuflaje de dominio

El **Camuflaje de Dominio** o ***Domain shadowing*** consiste en tomar el control de un dominio registrado consiguiendo las credenciales de administración para crear registros DNS de multitud de subdominios. Estos subdominios creados redirigen su resolución a direcciones IP en poder del atacante.  Esos subdominios pueden apuntar bien a una única IP, o a un conjunto de ellas según las necesidades y circunstancias.

La forma habitual de funcionamiento es organizar los subdominios en niveles. Para el primer nivel el atacante generará un número aleatorio de subdominios con nomenclatura inteligible basadas en palabras comunes. En este nivel inicial se alojan páginas de entrada que redirigen rápidamente al usuario a otros subdominios (de redirección) con una nomenclatura aleatoria, o incluso de otro dominio diferente que esté bajo control y hacer uso incluso de un cuarto nivel de dominio dificultar aún más la trazabilidad en el flujo de las comunicaciones. Rápidas rotaciones de distintos subdominios aleatorios harán llegar finalmente a la víctima a un subdominio que aloja un exploit para infectar al usuario (nivel de explotación). Esta serie de redirecciones y organización en subdominios proporciona un mecanismo de gran eficacia para evitar detecciones y bloqueos. Las direcciones IP de los subdominios suelen rotarse con frecuencia para hacer más efectiva la estrategia de evasión.

Este comportamiento ha demostrado ser altamente efectivo para evitar técnicas de bloqueo típicas como el uso de listas negras y/o sumidores de DNS de sitios o direcciones IP.

Usado desde 2011, esta técnica está disponible en algunos kits de exploits web como Angler. En 2016 Cisco descubrió que más de 15.000 sitios únicos que redirigían a web con Angler,  de los cuales el 99,8% se usaba menos de 10 veces. Estos sitios intermedios no alojaban ninguna de las actividades maliciosas de Angler. Servían como conductos

 Referencias
