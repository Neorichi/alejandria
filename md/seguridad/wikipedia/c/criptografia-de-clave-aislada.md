---
type: Artículo de enciclopedia
title: Criptografía de clave aislada
description: La criptografía de clave aislada (en inglés Key-Insulated cryptography) fue introducida en 2002 por Y.
resource: https://es.wikipedia.org/wiki/Criptografía_de_clave_aislada
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_de_clave_aislada"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_de_clave_aislada
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía de clave aislada

La **criptografía de clave aislada** (en inglés *Key-Insulated cryptography*) fue introducida en 2002 por Y. Dodis, J. Katz, S. Xu, M. Yung y mejorado posteriormente por Hanaoka y otros. El objetivo de estos sistemas es minimizar el daño causado tras un ataque que comprometa la clave privada de un sistema criptográfico. Para ello siguen un esquema similar al siguiente:
 Se divide el tiempo en N periodos
 La(s) clave(s) secretas se almacenan de forma posiblemente insegura (la seguridad está expuesta), pero estas claves son actualizadas en cada período.
 Para actualizar las claves se realiza una interacción con un dispositivo físicamente protegido (*secure helper*), el cual mantiene una clave secreta maestra que mantiene fija entre periodos.
 Todos los cálculos son hechos en el sistema inseguro.
 La clave pública se mantiene fija para todos los periodos.
De esta forma, incluso aunque las clave están expuesta, la seguridad del sistema permanece garantizada si la clave actual no ha sido violada. Cuanto más frecuentemente se cambie la clave más expuesto queda el sistema 'seguro'.

Este tipo de criptografía ha sido usado con criptografía de clave pública para realizar funcionalidades de cifrado, a lo que se conoce por las siglas **KIE** o **KIPE** del inglés *key-insulated public key encryption*), y de firma

 Referencias
