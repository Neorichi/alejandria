---
type: Artículo de enciclopedia
title: Programación orientada al retorno
description: "Programación orientada al retorno (ROP del inglés Return-oriented programming) es una técnica de explotación de seguridad informática que permite a un atacante ejecutar código ante la presencia de defensas de seguridad …"
resource: https://es.wikipedia.org/wiki/Programación_orientada_al_retorno
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Programación_orientada_al_retorno"}
license: CC BY-SA 4.0
id: eswiki-Programación_orientada_al_retorno
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Programación orientada al retorno

**Programación orientada al retorno** (**ROP** del inglés ***Return-oriented programming***) es una técnica de explotación de seguridad informática que permite a un atacante ejecutar código ante la presencia de defensas de seguridad como protección de espacio ejecutable y código firmado.

En esta técnica, un atacante gana control de la pila de llamadas para secuestrar el flujo de control del programa y entonces ejecuta secuencias de instrucciones de máquina elegidas cuidadosamente entre las que ya están presentes en la memoria del computador, las cuales se denominan "gadgets". Cada gadget típicamente termina con una instrucción de retorno y está localizado en una subrutina dentro del programa existente y/o en el código de alguna biblioteca compartida. Estos gadgets encadenados le permiten a un atacante realizar operaciones arbitrarias en un computador que emplee defensas contra ataques más simples.

 Referencias
