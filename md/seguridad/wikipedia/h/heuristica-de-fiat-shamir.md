---
type: Artículo de enciclopedia
title: Heurística de Fiat-Shamir
description: La heurística de Fiat-Shamir es una técnica criptográfica para a partir de una prueba de conocimiento cero interactiva obtener una prueba de conocimiento cero no interactiva.
resource: https://es.wikipedia.org/wiki/Heurística_de_Fiat-Shamir
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Heurística_de_Fiat-Shamir"}
license: CC BY-SA 4.0
id: eswiki-Heurística_de_Fiat-Shamir
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Heurística de Fiat-Shamir

La **heurística de Fiat-Shamir** es una técnica criptográfica para a partir de una prueba de conocimiento cero interactiva obtener una prueba de conocimiento cero no interactiva. Si la prueba interactiva es un protocolo de identificación, entonces la versión no-interactiva puede ser usada directamente como una firma digital. Esta técnica fue aportada por Amos Fiat y Adi Shamir en 1986.

Mecanismo
La heurística sigue los siguientes pasos:
El probador genera un mensaje de compromiso indicando que conoce el secreto.
El probador toma el compromiso y otra información como entradas y devuelve el desafío aplicando alguna función hash criptográfica
El probador calcula la respuesta y envía la transcripción que incluye el compromiso, el desafío y la respuesta al verificador.

Seguridad
La heurística fue presentada originalmente sin una prueba de seguridad; más tarde David Pointcheval y Jacques Stern  probaron su seguridad contra un ataque de mensaje escogido en el modelo de oráculo aleatorio, esto es bajo la suposición de que el oráculo aleatorio existe (no se pueden predecir los resultados de una función hash). En caso de no existir el oráculo aleatorio se ha probado que es inseguro.

Ejemplo
Veamos un ejemplo con la prueba interactiva sobre el conocimiento del logaritmo discreto.

Alicia quiere probar a Bob que conoce  el cual es el logaritmo discreto de  para la base .
Alicia coge un número aleatorio , calcula  y envía a Bob .
Bob coge un número aleatorio  y se lo envía a Alicia.
Alicia calcula  y devuelve  a Bob.
Bob comprueba que  (lo cual sucede solo si ).

La heurística de Fiat-Shamir lo convierte en:

Alicia quiere probar a Bob que conoce  el cual es el logaritmo discreto de  para la base .
Alicia coge un número aleatorio  y calcula .
Alicia calcula , donde  es una función hash criptográfica.
Alicia calcula . El resultado de la prueba es el par .
Cualquiera puede comprobar que  ya que .

Se ha demostrado que si el valor hash usado no depende del valor (público) de y, la seguridad del esquema es débil ya que un probador malicioso puede entonces seleccionar cierto x tal que el producto de cx es conocido.

Referencias
