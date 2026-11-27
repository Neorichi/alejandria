---
type: Artículo de enciclopedia
title: Algoritmo de generación de dominio
description: Un algoritmo de generación de dominios o DGA (del inglés Domain Generation Algorithm) es un algoritmo que genera pseudoaleatoriamente nombres de dominio a partir de una semilla.
resource: https://es.wikipedia.org/wiki/Algoritmo_de_generación_de_dominio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Algoritmo_de_generación_de_dominio"}
license: CC BY-SA 4.0
id: eswiki-Algoritmo_de_generación_de_dominio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Algoritmo de generación de dominio

Un **algoritmo de generación de dominios** o **DGA** (del inglés *Domain Generation Algorithm*) es un algoritmo que genera pseudoaleatoriamente nombres de dominio a partir de una semilla.

Es frecuente el uso de la fecha del sistema como semilla para generar los nombres de dominios. Por ejemplo, el malware Murofet usa la fecha para inicializar su algoritmo y genera al día 800 dominios diferentes. Otras veces se usan datos de sitios de legítimos. Por ejemplo Torpig usan los trending topics de Twitter.

 Uso con malware
Es habitual el uso de estos algoritmos en ciberataques. Su uso, junto con técnicas de Domain Fluxing, permiten eludir el bloqueo de conexión al servidores C&C o al servidor donde descargar software.

El atacante selecciona una semilla e instala un malware con la misma. Como el atacante conoce la semilla, es capaz de predecir los dominios que se generarán, por lo que se anticipa y genera de forma aleatoria alguno de ellos, lo activa, espera a conectar con algunos nodos y los desactiva (des-registra) y vuelta a empezar. Esto dificulta la labor de administradores e investigadores de seguridad de bloquear accesos al servidor C&C para anular una botnet. Por ejemplo, los sistemas de detección basados en listas negras, listas de reputación y filtros web pueden ser evadidos sin problemas ya que, pasado un tiempo, el servidor C&C tendrá otro dominio y otra IP, y por tanto se permitirá el acceso. Por eso cuando se encuentra una muestra es muy importante aplicar ingeniería inversa y encontrar la semilla. Esta forma de elusión fue popularizado por los malware Conficker y es utilizado por el malware Kraken, Locky, Murofet, Zeus, CryptoLocker y Torpig. Cada día es una técnica más habitual

 Referencias
