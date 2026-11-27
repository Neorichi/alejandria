---
type: Artículo de enciclopedia
title: Self-XSS
description: Self-XSS es un ataque de ingeniería social usado para perder control de las cuentas web de las víctimas.
resource: https://es.wikipedia.org/wiki/Self-XSS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Self-XSS"}
license: CC BY-SA 4.0
id: eswiki-Self-XSS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Self-XSS

**Self-XSS** es un ataque de ingeniería social usado para perder control de las cuentas web de las víctimas. En un ataque self-XSS, la víctima del ataque ejecuta accidentalmente código malicioso en su propio navegador web, exponiéndose así al atacante.

 Descripción general
Self-XSS opera engañando a los usuarios para que copien y peguen contenido malicioso en la consola de desarrolladores web de sus navegadores Por lo general, el atacante publica un mensaje que dice copiando y ejecutando cierto código, el usuario será capaz de hackear la cuenta de otro usuario. De hecho, el código permite al atacante secuestrar la cuenta de la víctima.

 Historia y mitigación

En el pasado, varios atacantes engañaron a varios usuarios, los cuales pegaron códigos de JavaScript maliciosos en sus barras de direcciones. Cuando los desarrolladores de navegadores detuvieron esto al impedir que se ejecute fácilmente JavaScript desde la barra de direcciones, los atacantes comenzaron a usar Self-XSS en su forma actual, tratando de engañar al usuario convenciendolo de mejoras en sus cuentas de correo o redes sociales. Algunos proveedores de navegadores web y sitios web han tomado medidas para mitigar este ataque, entre estos están Mozilla Firefox y Google Chrome, los cuales han comenzado a implementar mensajes de advertencia para advertir a los usuarios sobre los ataques Self-XSS. Facebook actualmente muestra un mensaje de advertencia cuando los usuarios abren la consola de desarrolladores web y enlazan con páginas que explican el ataque en detalle.

 Etimología
La palabra "self" proviene del hecho de que el usuario se está atacando a sí mismo. La palabra "XSS" del nombre proviene de la abreviatura de secuencias de comandos de sitios cruzados, ya que ambos ataques producen código malicioso que se ejecuta en un sitio legítimo. Sin embargo,  los ataques no tienen mucho más en común, porque XSS es un ataque contra el propio sitio web, mientras que el "self-XSS" es un ataque de ingeniería social contra el usuario.

 Referencias

 Lectura adicional
