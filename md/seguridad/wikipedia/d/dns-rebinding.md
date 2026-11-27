---
type: Artículo de enciclopedia
title: DNS rebinding
description: "La revinculación de DNS o DNS rebinding es un ataque informático basado en DNS donde el atacante aprovecha una vulnerabilidad para transformar el equipo en un proxy de red. Para esto utiliza código embebido en páginas …"
resource: https://es.wikipedia.org/wiki/DNS_rebinding
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/DNS_rebinding"}
license: CC BY-SA 4.0
id: eswiki-DNS_rebinding
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# DNS rebinding

La **revinculación de DNS** o ***DNS rebinding*** es un ataque informático basado en DNS donde el atacante aprovecha una vulnerabilidad para transformar el equipo en un *proxy* de red. Para esto utiliza código embebido en páginas web aprovechándose de la política del mismo origen de los navegadores.

 Uso
Normalmente las peticiones del código incorporado en las páginas web (Javascript, Java, Flash..) están limitadas al sitio web desde el que se han originado, lo que se conoce como *política del mismo origen*. La *DNS rebinding* puede mejorar la habilidad de un *malware* basado en JavaScript para penetrar en redes privadas transtornando la política del mismo origen.
Usando DNS rebinding un atacante puede sortear cortafuegos, navegar en intranets corporativas, mostrar documentos sensibles y comprometer máquinas internas que no estén parcheadas.

 Cómo funciona la *DNS rebinding*
El atacante registra un dominio el cual delega a un servidor DNS que él controla. El servidor está configurado para responder con un parámetro TTL muy corto, que previene que la respuesta sea cacheada.

La primera respuesta contiene la dirección IP del servidor con el código malicioso. Las consiguientes respuestas contienen direcciones IP de redes privadas falsas (RFC 1918) presumiblemente detrás de un cortafuegos que es la meta del atacante.

Dado que las dos son respuestas DNS completamente válidas, autorizan al script el acceso a hosts dentro de la red privada. Devolviendo múltiples direcciones IP, el servidor DNS habilita al script para escanear la red local o realizar actividades maliciosas.

 Protección
Las siguientes técnicas pueden ser utilizadas para prevenir ataques de DNS rebinding:
 *DNS pinning*: fijando una dirección IP al valor recibido en la primera respuesta DNS. Esta técnica puede bloquear algunos usos legítimos de DNS dinámico.
 Bloqueando la resolución de nombres externos en direcciones internas en los servidores de nombres locales de la organización.
 Los servidores pueden rechazar peticiones HTTP con una cabecera de Host irreconocible.

Con el tiempo, los fabricantes han tomado medidas para proteger del problema.
 *Flash Player* desde la versión 9,0,115,0.
 Firefox. Protección adicional con el complemento NoScript, desde la versión 2.0rc5.

 Referencias

 Enlaces externos
 Cómo se hizo
