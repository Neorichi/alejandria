---
type: Artículo de enciclopedia
title: Evasión (seguridad de redes)
description: En seguridad de redes, la evasión consiste en eludir una defensa de seguridad de la información con el fin de enviar un exploit, ataque u otra forma de malware a una red o sistema objetivo, sin ser detectado.
resource: https://es.wikipedia.org/wiki/Evasión_(seguridad_de_redes)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Evasión_(seguridad_de_redes)"}
license: CC BY-SA 4.0
id: eswiki-Evasión_(seguridad_de_redes)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Evasión (seguridad de redes)

En seguridad de redes, la **evasión** consiste en eludir una defensa de seguridad de la información con el fin de enviar un *exploit*, ataque u otra forma de *malware* a una red o sistema objetivo, sin ser detectado. Las evasiones suelen utilizarse para contrarrestar los sistemas de detección y prevención de intrusiones basados en la red (IPS, IDS), pero también pueden utilizarse para eludir los cortafuegos y el análisis de malware. Otro objetivo de las evasiones puede ser colapsar una defensa de seguridad de red, haciéndola ineficaz ante posteriores ataques dirigidos.

 Descripción
Las evasiones pueden ser particularmente desagradables porque una evasión bien planificada e implementada puede permitir que se lleven a cabo sesiones completas en paquetes que evaden un IDS. Los ataques llevados a cabo en tales sesiones se producirán delante de las narices de los administradores de red y de servicios.

Los sistemas de seguridad se vuelven ineficaces frente a técnicas de evasión bien diseñadas, del mismo modo que un caza furtivo puede atacar sin ser detectado por el radar y otros sistemas defensivos.

Una buena analogía de las evasiones es un sistema diseñado para reconocer palabras clave en patrones de habla en un sistema telefónico, como "entrar en el sistema X". Una evasión sencilla consistiría en utilizar un idioma distinto del inglés, pero que ambas partes puedan entender, y lo idea es que sea un idioma que hable el menor número posible de personas.

 Ataques de evasión

Desde mediados de los años noventa se conocen varios ataques de evasión avanzados y selectivos:

 En 1997 apareció un texto fundamental en el que se describían los ataques contra los sistemas IDS.
 Una de las primeras descripciones exhaustivas de los ataques la realizaron Ptacek y Newsham en un informe técnico en 1998.
 En 1998, también un artículo de la revista *Phrack Magazine* describe formas de eludir la detección de intrusiones en la red.

 Informes
El artículo de 1997 trata sobre todo de varios trucos basados en *shell-scripting (script de shell)* y caracteres para engañar a un IDS. El artículo de Phrack Magazine y el informe técnico de Ptacek et al. tratan sobre *exploits* de protocolos TCP/IP, evasiones y otros. Discusiones más recientes sobre evasiones incluyen el informe de Kevin Timm.

 Protección contra las evasiones
El reto en la protección de servidores contra evasiones es modelar la operación del *host* final en el dispositivo de seguridad de la red, es decir, el dispositivo debe ser capaz de saber cómo el host objetivo interpretaría el tráfico, y si sería dañino, o no. Una solución clave en la protección contra las evasiones es la normalización del tráfico en el dispositivo IDS/IPS. La otra forma de separar el acceso a Internet puede implementarse basándose en cómo el usuario final puede estar seguro accediendo al segmento de Internet.

Últimamente se ha hablado de dedicar más esfuerzos a la investigación de técnicas de evasión. En una presentación en *Hack.lu* se habló de algunas técnicas de evasión potencialmente nuevas y de cómo aplicar múltiples técnicas de evasión para eludir los dispositivos de seguridad de la red.

 Véase también

 Proyecto Metasploit

 Referencias
