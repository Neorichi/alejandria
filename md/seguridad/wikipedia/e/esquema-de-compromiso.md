---
type: Artículo de enciclopedia
title: Esquema de compromiso
description: En criptografía, un esquema de compromiso permite comprometerse a un valor que permanecerá oculto, con la capacidad de revelar este valor luego.
resource: https://es.wikipedia.org/wiki/Esquema_de_compromiso
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Esquema_de_compromiso"}
license: CC BY-SA 4.0
id: eswiki-Esquema_de_compromiso
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Esquema de compromiso

En criptografía, un **esquema de compromiso** permite comprometerse a un valor que permanecerá oculto, con la capacidad de revelar este valor luego.

El concepto de esquemas de compromiso fue formalizado en 1988 por Gilles Brassard, David Chaum, y Claude Crépeau en 1988, pero el concepto fue utilizado informalmente antes de ese año. La idea de los compromisos apareció anteriormente en las obras de Manuel Blum, Shimon Even, y Shamir *et al*.  La terminología parece haber sido creada por Blum.

 Aplicaciones
 Pruebas de conocimiento cero
Los esquemas de compromiso son utilizados en pruebas de conocimiento cero para que el verificador especifique sus propias selecciones de antemano. Esto permite que las pruebas de conocimiento cero se creen en paralelo pero sin revelar información adicional. Esto también permite especificar toda la información con antelación en un compromiso, pero revelando únicamente el resultado de una prueba que se realizará en el futuro.

 Esquema de firmas
El Esquema de firma Lamport es un sistema de firmas digital que depende de la creación de dos paquetes de datos secretos, se publican entonces hashes verificables de los paquetes de datos y luego se revelan selectivamente paquetes parciales de los datos secretos de manera que se ajusten específicamente a los datos que se deben firmar. De esta forma, el esquema de compromiso previo con los valores secretos se convierte en una parte crítica del funcionamiento del sistema.

 Definiendo la seguridad

 Imposibilidad de  esquemas de compromiso universalmente generables
Es imposible de resolver los esquemas de compromiso en el marco de la generación universal. La razón es que el compromiso de generación universal tiene que ser *extraíble*.

 Generación

 Compromiso en bits a partir de un generador pseudoaleatorio

En 1991, Moni Naor[13] demostró cómo crear un esquema de compromiso en bits a partir de una generador pseudoaleatorio de números criptográficamente seguro.

 Compromiso en bits cuánticos

En 1996, Dominic Mayers demostró que es imposible generar protocolos de compromiso incondicionalmente seguros mediante criptografía cuántica, lo que teóricamente vincularía y ocultaría la información aun cuando no haya restricciones a nivel de recursos computacionales.

Una suposición sutil de la prueba de Mayers es que la fase de compromiso tiene que terminarse en algún momento. Esto permite que los protocolos que requieran un continuo flujo de información se cancele, en cuyo caso ya no estarían vinculados.

 Véase también
 Transferencia inconsciente
 Fiesta de firmado de claves
 Red de confianza
 Zerocoin

 Referencias

 Enlaces externos
 Compromiso cuántico de bits en arxiv.org
