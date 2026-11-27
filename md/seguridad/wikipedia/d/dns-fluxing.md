---
type: Artículo de enciclopedia
title: DNS Fluxing
description: "Se llama DNS Fluxing a una serie de actividades destinadas a ocultar la ubicación real de determinados recursos dentro de una red. Consiste en cambiar registros DNS con una frecuencia extrema y reducir mucho el tiempo …"
resource: https://es.wikipedia.org/wiki/DNS_Fluxing
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/DNS_Fluxing"}
license: CC BY-SA 4.0
id: eswiki-DNS_Fluxing
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# DNS Fluxing

Se llama **DNS Fluxing** a una serie de actividades destinadas a ocultar la ubicación real de determinados recursos dentro de una red. Consiste en cambiar registros DNS con una frecuencia extrema y reducir mucho el tiempo TTL del dominio para asegurarse que los otros servidores DNS no lleguen a cachear el dominio, obligando siempre a consultar el DNS raíz del dominio.

Es usado habitualmente en ciberataques para mejorar la disponibilidad y la resistencia a fallos. En estos casos el recurso oculto es un servidor que entrega malware, un sitio web de phishing o un servidor de comando y control de una botnet.

Hay dos posibles formas de hacer DNS Fluxing: **Fast Flux**, también llamado **IP Flux**, y **Domain Flux**.

 Fast Flux

**Fast Flux** o **IP Flux** consiste en el constante cambio de dirección IP asociada a un nombres de dominio con el fin de dificultar la localización del ataque. Las Botnet abusan de esta capacidad de cambiar la dirección IP asociada a un dominio vinculando varias direcciones IP y cambiando rápidamente las direcciones vinculadas.

Habitualmente Fast Flux se combina con técnicas de Blind Proxy Redirection, de forma que las direcciones IP pertenecen a hosts comprometidos (bots), que se conocen como **agentes fast-flux**, que actúan como proxies inversos formando un servicio de red Fast-Flux (**FFSN**, del inglés *Fast-Flux Service Network*) que reenvían solicitudes del cliente al servidor C&C y reenvían las respuestas del servidor C&C al cliente. También se pueden usar varios niveles de indirección. La red Fast-Flux garantiza que un cliente víctima solo se conectará a agentes de flujo rápido, pero nunca al servidor real de C&C. De esta forma se evade la detección de servidores C&C y las listas negras basadas en IP.

Hay tres tipos de **Fast Flux**:
 **Single-flux**. Se caracteriza por tener varias (cientos o incluso miles) direcciones IP asociadas a un nombre de dominio. Estas direcciones IP son registradas y desregistradas rápidamente - usando una combinación de planificación Round-robin y valores de tiempo de vida (Time-to-live, TTL) muy cortos - contra un registro de DNS particular. Los cambios aplican a registros A y AAAA. El  servidor de DNS del dominio está alojado en un servidor fijo.
 **Name Server Flux**, o simplemente **NS flux**, consiste en cambiar frecuentemente la dirección IP de registros de pegamento del DNS (registros A o AAAA que definen IPs donde se hacen las búsquedas de dominio apuntados por registro NS). Es decir, se cambian frecuente las direcciones IP de los servidores de nombre DNS.
 **Double-flux**. Consiste en hacer a la vez **Single-flux** y **NS fluxing**. En este caso tanto las direcciones asociadas al nombre de dominio como el servidor de DNS del dominio son agentes fast-flux.

 Domain Flux
Es el inverso del IP flux y consiste en el constante cambio y la asignación de múltiples dominios a una sola dirección IP. Para usar esta técnica es frecuente el uso de:
Dominios con wildcards. Por ejemplo, se puede hacer que todos los dominios de la forma *.dominio.com apunten a la misma dirección IP. Esto se puede aprovechar para que el contenido aleatorio que aparece en el símbolo comodín (por ejemplo, 'asdkjlkwer.dominio.com') sirva para identificar de manera única a una víctima y así poder identificarla.
algoritmos de generación de dominio o (DGA). Son algoritmos que generan aleatoriamente nombres de dominio seudoaleatorios a partir de una semilla. Es habitual el uso de estos algoritmos en malware que se conectan a servidor C&C. El atacante selecciona una semilla e instala un malware con la misma. Como el atacante conoce la semilla, es capaz de predecir los dominios que se generarán, por lo que se anticipa y genera de forma aleatoria alguno de ellos, lo activa, espera a conectar con algunos nodos y los desactiva (des-registra) y vuelta a empezar. Esto dificulta la labor de administradores e investigadores de seguridad de bloquear accesos al servidor C&C para anular una botnet. Por ejemplo, los sistemas de detección basados en listas negras, listas de reputación y filtros web pueden ser evadidos sin problemas ya que, pasado un tiempo, el servidor C&C tendrá otro dominio y otra IP, y por tanto se permitirá el acceso. Por eso cuando se encuentra una muestra es muy importante aplicar ingeniería inversa y encontrar la semilla. Esta forma de elusión fue popularizado por los malware Conficker y es utilizado por el malware Kraken, Locky, Murofet, CryptoLocker y Torpig. Cada día es una técnica más habitual

 Referencias
