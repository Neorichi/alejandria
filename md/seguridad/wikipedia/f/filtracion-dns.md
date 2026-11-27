---
type: Artículo de enciclopedia
title: Filtración DNS
description: Una filtración DNS se refiere a un defecto de seguridad que permite que las solicitudes DNS sean reveladas a los servidores DNS de los ISP, a pesar del uso de un servicio de VPN para intentar para encubrirlos.
resource: https://es.wikipedia.org/wiki/Filtración_DNS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Filtración_DNS"}
license: CC BY-SA 4.0
id: eswiki-Filtración_DNS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Filtración DNS

Una **filtración DNS** se refiere a un defecto de seguridad que permite que las solicitudes DNS sean reveladas a los servidores DNS de los ISP, a pesar del uso de un servicio de VPN para intentar para encubrirlos.
A pesar de que es una preocupación principalmente para usuarios de VPN, también es posible prevenirlo para usuarios de proxy y de internet directo.

 Proceso
La vulnerabilidad permite que un ISP, así como cualquiera que esté monitoreando la comunicación en el camino, pueda ver los sitios web que un usuario puede estar visitando. Esto es posible porque las solicitudes DNS del navegador son enviadas al servidor DNS del ISP directamente, y no enviado a través del VPN.

Esto sólo ocurre con algunos tipos de VPNs, p. ej. VPNs de "túnel-partido", donde el tráfico todavía puede ser enviado sobre la interfaz de red local incluso cuándo la VPN está activa.

Empezando con Windows 8, Microsoft introdujo la "Resolución de Nombres Multi-Homed Inteligente". Esto alteró la forma en que Windows 8 manejaba  las peticiones DNS, al asegurar que una petición DNS podría recorrer todas interfaces de red disponibles en el ordenador. Aunque hay consenso general que este método nuevo de resolución de nombres de dominio aceleró el tiempo requerido completar una búsqueda DNS, también expuso a los usuarios VPN a filtraciones DNS cuando estén conectados a una VPN, porque el ordenador ya no utilizaría sólo los servidores DNS asignados por el servicio VPN. En cambio la petición DNS sería enviada a través de todas las interfaces  disponibles, por ello el tráfico DNS viajaría fuera del túnel VPN y expondría los servidores DNS por defecto del usuario.

 Prevención
Existen sitios web que permiten hacer pruebas para determinar si ocurre una filtración DNS. Las filtraciones DNS pueden ser atacadas en un número de maneras:

 Encriptando las solicitudes DNS con DNS mediante HTTPS o DNS sobre TLS, el cual impide que las peticiones sean vistas por potenciales observadores.
 Utilizando un cliente VPN qué envíe las peticiones DNS sobre la VPN. No todas las aplicaciones  VPN logran bloquear exitosamente las filtraciones DNS, lo cual fue encontrado en un estudio por la Organización de la Commonwealth para Búsqueda Científica e Industrial en 2016 cuándo llevaron a cabo un estudio en profundidad llamado "Un Análisis de la Privacidad y los Riesgos de Seguridad de las aplicaciones de VPN de Android con permisos habilitados" y encontraron que el 84% de las 283 aplicaciones VPN en la Tienda de Juego del Google que probaron tenían filtraciones DNS.
 Cambiando los servidores DNS en el ordenador local para adaptar la red entera, o apuntándolos a unos diferentes. Existen aplicaciones de terceros  disponibles para esto, como NirSoft quicksetdns.
 Utilizando un Firewall para inutilizar el DNS en todo el dispositivo (normalmente conexiones UDP salientes y a veces TCP puerto 53), o poniendo servidores DNS a direcciones que no existen, como unos como locales 127.0.0.1 o 0.0.0.0 (vía línea de comando o aplicaciones de tercerossi no posible vía os interfaz GUI). Esto requiere formas alternativas de resolver dominios como el que mencionamos más arriba, o utilizando  aplicaciones con proxy configurado, o utilizando aplicaciones de proxy helper como Proxifier o ProxyCap, el cual deja resolver ámbitos sobre proxy. Muchas aplicaciones permiten ingresar proxy manuales o utilizar proxy ya utilizados por sistema.
 Utilizando  navegadores web completamente anónimos como Tor Navegador qué no sólo hace el usuario anónimo, sino que también requiere que cualquier dns sea instalado en el sistema operativo.

 Lista de los sitios web que ofrecen DNS pruebas de filtración
Ya que algunos sitios web pueden informar resultados de prueba positivos falsamente,  es aconsejable siempre comprobar cada resultado manualmente. Asegurando anotar que el país, proveedor, y la ip no es del ISP doméstico sino de algo diferente o extranjero.

 Conclusión
Puede que no siempre sea tan fácil saber si el está utilizando DNS prefijados, y si  hay cualquier filtraciones DNS.
La manera más segura es verificar usando más de unas  pruebas de filtración en línea .
A veces el ISP puede ya estar utilizando servidores DNS públicos por default, dondel el público no se da cuenta de la diferencia porque los servidores son mismos, pero el ISP puede recoger datos también. En tal caso,  lo más seguro es cambiar a DNS diferentes que no tengan filtraciones DNS. Por ejemplo si el ISP utilizaba Google público dns y  nosotros estamos utilizando el mismo,  puede ser sensato probar cloudflare DNS, y luego ver si  hay cualesquier filtraciones a Google DNS.

 Referencias
