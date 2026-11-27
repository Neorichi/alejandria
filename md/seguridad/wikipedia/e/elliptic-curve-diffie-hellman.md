---
type: Artículo de enciclopedia
title: Elliptic-curve Diffie-Hellman
description: "El protocolo Elliptic-curve Diffie–Hellman (ECDH) es un protocolo de establecimiento de claves anónimo que permite a dos partes, cada una de las cuales tiene un par de claves pública-privada de curvas elípticas, …"
resource: https://es.wikipedia.org/wiki/Elliptic-curve_Diffie-Hellman
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Elliptic-curve_Diffie-Hellman"}
license: CC BY-SA 4.0
id: eswiki-Elliptic-curve_Diffie-Hellman
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Elliptic-curve Diffie-Hellman

El protocolo **Elliptic-curve Diffie–Hellman** (**ECDH**) es un protocolo de establecimiento de claves anónimo que permite a dos partes, cada una de las cuales tiene un par de claves pública-privada de curvas elípticas, establecer un secreto compartido en un canal inseguro. Este secreto compartido puede usarse directamente como clave o para derivar otra clave. La clave, o la clave derivada, pueden usarse entonces para cifrar sucesivas comunicaciones usando un cifrado de clave simétrica. Es una variante del protocolo Diffie-Hellman usando criptografía de curva elíptica.

 Protocolo de establecimiento de clave
El siguiente ejemplo ilustra cómo se establece una clave. Supóngase que Alice quiere establecer una clave compartida con Bob, pero el único canal disponible para ellos puede ser espiado por una tercera parte. Los parámetros de dominio (esto es,  en el caso binario) se deben acordar previamente. Además, cada parte debe tener un par de claves adecuado para criptografía de curva elíptica, consistente en una clave privada  (un entero aleatoriamente elegido en el intervalo ) y una clave pública representada por un punto  (donde , esto es, el resultado de sumar consigo mismo veces). Sea el par de claves de Alice y . Cada parte debe conocer la clave pública de la otra parte antes de ejecutar el protocolo.

Alice computa el punto . Bob computa el punto . El secreto compartido es  (la coordenada *x* del punto). La mayoría de protocolos estandarizados basados en ECDH derivan una clave simétrica de usando alguna función de derivación de clave basada en *hash*.

El secreto compartido calculado por ambas partes coincide, ya que .

La única información sobre su clave privada que Alice expone inicialmente es su clave pública. Así, ninguna otra parte además de Alice puede determinar su clave privada, a menos que esa parte pueda resolver el problema del logaritmo discreto sobre la curva elíptica. La clave privada de Bob es segura de la misma forma. Ninguna otra parte además de Alice o Bob puede computar el secreto compartido, a menos que pueda resolver el problema de Diffie-Hellman sobre la curva elíptica.

Las claves públicas son o bien estáticas (y confiables, por ejemplo a través de un certificado) o efímeras (también conocidas como ECDHE, donde la «E» final viene del inglés «ephemeral»). Las claves efímeras son temporales y no necesariamente autenticadas, de forma que si se desea autenticación, se deben obtener los seguros de autenticidad por otros medios. La autenticación es necesaria para evitar ataques de intermediario. Si la clave de Alice o de Bob es estática se impide este tipo de ataques. Las claves públicas estáticas no proveen ni *forward secrecy* ni resistencia a la suplantación de clave, entre otras propiedades de seguridad avanzadas. Los usuarios de claves privadas estáticas deben validar la otra clave pública, y deben aplicar una función de derivación de clave segura al secreto compartido bruto de Diffie-Hellman para evitar filtrar información sobre la clave privada estática. Un esquema que ofrece otras propiedades de seguridad es MQV.

Aunque el secreto compartido se puede usar directamente como clave, en ocasiones es deseable aplicar una función *hash* al secreto para eliminar bits débiles debido al intercambio de Diffie-Hellman.

 Programas

 Curve25519 es el conjunto de parámetros de curva elíptica y la implementación de referencia de Daniel J. Bernstein en C. También están disponibles *bindings* e implementaciones alternativas.
 La aplicación de mensajería instantánea Line ha usado el protocolo ECDH para su cifrado de extremo a extremo de «sellado de cartas» en todos los mensajes enviados a través de la misma desde octubre de 2015.

 Véase también

 Diffie-Hellman

 Referencias
