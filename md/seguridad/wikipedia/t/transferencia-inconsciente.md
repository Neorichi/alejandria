---
type: Artículo de enciclopedia
title: Transferencia inconsciente
description: "En seguridad informática, el protocolo de transferencia inconsciente (oblivious transfer) es un método utilizado para transferir un secreto de un usuario a un usuario y que A no sepa si B pudo conocer el secreto (la …"
resource: https://es.wikipedia.org/wiki/Transferencia_inconsciente
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Transferencia_inconsciente"}
license: CC BY-SA 4.0
id: eswiki-Transferencia_inconsciente
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Transferencia inconsciente

En seguridad informática, el protocolo de **transferencia inconsciente** (*oblivious transfer*) es un método utilizado para transferir un secreto de un usuario  a un usuario  y que A no sepa si B pudo conocer el secreto (la probabilidad de que esto suceda es de ), de ahí el término "inconsciente". Este protocolo da lugar a la eclosión de otros protocolos como compromiso de bits y demostración de conocimiento nulo.

 Definición formal

Aquí definiremos lo que se conoce como protocolo de Rabin, la siguiente definición ilustrará con precisión un protocolo de transferencia inconsciente de una clave secreta de un criptosistema de Rabin:

 El usuario  elige 2 grandes números primos  y , luego calcula  y le envía  a .
  elige una , donde  y  (que  y  sean coprimos) y le envía  a .
  calcula las 4 raíces de  que son , elige una aleatoriamente y se la envía a
 Si  recibe  o , entonces  puede calcular  y  mediante el algoritmo euclídeo haciendo  lo que concluirá en  o , si  recibe  o , entonces  no puede calcular  y .

Aquí queda plasmado como la probabilidad de que B conozca p y q es 1/2, ya que el espacio muestral contiene 4 resultados (x, n-x, y, n-y) y todos equiprobables (consistente en la definición de la probabilidad de Laplace) lo que cada resultado tiene probabilidad de 1/4 y como el suceso "B puede conocer p y q" contiene 2 de esos resultados (y, n-y), se ve que la probabilidad es de 1/2 y en aras de la generalización, si cada bit de un secreto codificado se transmite mediante transferencia inconsciente, entonces la probabilidad de que B pueda conocer el secreto con precisión es de 2^-n, donde n es la longitud de bits del secreto codificado.
