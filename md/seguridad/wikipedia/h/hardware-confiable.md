---
type: Artículo de enciclopedia
title: Hardware confiable
description: Se conoce como hardware confiable a todo dispositivo diseñado para ofrecer una serie de facilidades que permiten manejar de manera segura información crítica.
resource: https://es.wikipedia.org/wiki/Hardware_confiable
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Hardware_confiable"}
license: CC BY-SA 4.0
id: eswiki-Hardware_confiable
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Hardware confiable

Se conoce como **hardware confiable** a todo dispositivo diseñado para ofrecer una serie de facilidades que permiten manejar de manera segura información crítica.

Limitaciones
Lo único que aporta el hardware confiable son facilidades que mejoran la seguridad y dificultan los ataques. Los tipos de ataques al hardware son muchos y a día de hoy no se puede asegurar infalibilidad. Los dispositivos se pueden atacar de dos formas:
**Directamente**. Por ejemplo atacando los componentes internos del dispositivo, observar y manipular el dispositivo (en inglés *micro probing*), ingeniería inversa, congelamiento en nitrógeno líquido para aumentar el tiempo en que la RAM retiene datos y lectura posterior, acceso con rayos UV o X etc.
**Indirectamente**. Por ejemplo usando canales encubiertos

Por otra parte hay que resaltar que gran parte de los ataques que se producen tienen como objetivo el software que a su vez hace uso del hardware confiable. Por tanto es muy importante diseñar el software de tal forma que use el hardware confiable de forma adecuada.

Estrategias
Veamos algunas de las estrategias más usadas para mejorar la seguridad de los dispositivos.
Resistencia a ser modificados
Una estrategia habitual para tener un hardware más seguro es que oponga algún tipo de resistencia a ser modificado. Se dice que está **a prueba de modificaciones** (en inglés *tamper proof*)
Existen distintas formas de protegerse:
Con **evidencias de modificación** (en inglés *tamper evidence*). Consiste en que el dispositivo posee mecanismos que provocan que el ataque físico deje huella y por tanto pueda ser detectado.
Con **resistencia a la modificación** (en inglés *tamper resistance*). Consiste en que el dispositivo posee características que hacen difícil atacarlo físicamente.
Con **detección a las modificaciones** (en inglés *tamper resistance*). Consiste en que el dispositivo posee características que permiten detectar cuándo se están realizando un ataque (ejemplo con el uso de sensores)
Con **mecanismos de respuesta a modificaciones** (en inglés *tamper response*). Consiste en que el dispositivo posee mecanismos que destruyen la información cuando se produce un ataque, lo cual evita el acceso a la misma.

Centralizar las funcionalidades críticas

La estrategia consiste en centralizar las funcionalidades críticas en un procesador criptográfico que estará muy protegido y que nos permitirá relajar las medidas de seguridad en el resto del sistema.

Computación confiable

El Trusted Computing Group es un conjunto de empresas que definen especificaciones de hardware con el objetivo de tener plataformas más seguras que permiten una computación más confiable. A a las plataformas que cumplen sus especificaciones las llaman **Plataformas confiables** las cuales dicen que aportan un entorno seguro para la ejecución de software dando lugar a lo que llaman **Computación confiable**.

Referencias
