---
type: Artículo de enciclopedia
title: Envenenamiento de DNS
description: "El envenenamiento de caché DNS o envenenamiento de DNS (DNS cache poisoning o DNS poisoning) es una situación creada de manera maliciosa o no deseada que provee datos de un servidor de nombres de dominio (DNS) que no se …"
resource: https://es.wikipedia.org/wiki/Envenenamiento_de_DNS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Envenenamiento_de_DNS"}
license: CC BY-SA 4.0
id: eswiki-Envenenamiento_de_DNS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Envenenamiento de DNS

El **envenenamiento de caché DNS** o **envenenamiento de DNS** (*DNS cache poisoning* o *DNS poisoning*) es una situación creada de manera maliciosa o no deseada que provee datos de un servidor de nombres de dominio (DNS) que no se origina de fuentes autoritativas DNS. Esto puede pasar debido a diseños inapropiados de *software*, falta de configuración de nombres de servidores y escenarios maliciosamente diseñados que explotan la arquitectura tradicionalmente abierta de un sistema DNS. Una vez que un servidor DNS  ha recibido aquellos datos no autentificados y los almacena temporalmente para futuros incrementos de desempeño, es considerado envenenado, extendiendo el efecto de la situación a los clientes del servidor.

 Ataques de Envenenamiento de Caché
Normalmente, una computadora conectada a Internet utiliza un servidor DNS proporcionado por el proveedor de servicios de Internet (ISP). Este DNS generalmente atiende solamente a los propios clientes del ISP y contiene una pequeña cantidad de información sobre DNS almacenada temporalmente por usuarios previos del servidor. Un ataque de envenenamiento (*poisoning attack*) de un solo servidor DNS de un ISP puede afectar a los usuarios atendidos directamente por el servidor comprometido o indirectamente por los servidores dependientes del servidor.

Para realizar un ataque de envenenamiento de caché, el atacante explota una vulnerabilidad en el software de DNS que puede hacer que este acepte información incorrecta. Si el servidor no valida correctamente las respuestas DNS para asegurarse de que ellas provienen de una fuente autoritativa, el servidor puede terminar almacenando localmente información incorrecta y enviándola a los usuarios para que hagan la misma petición.

Esta técnica puede ser usada para reemplazar arbitrariamente contenido de una serie de víctimas con contenido elegido por un atacante. Por ejemplo, un atacante envenena las entradas DNS de direcciones IP para un sitio web objetivo, reemplazándolas con la dirección IP de un servidor que él controla. Luego, el atacante crea entradas falsas para archivos en el servidor que él controla con nombres que coinciden con los archivos del servidor objetivo. Estos archivos pueden contener contenido malicioso, como un virus o un gusano. Un usuario cuya computadora ha referenciado al servidor DNS envenenado puede ser engañado al creer que el contenido proviene del servidor objetivo y sin saberlo descarga contenido malicioso.

Como parte del proyecto Golden Shield, China, de forma regular hace uso de envenenamiento de DNS para redes o sitios específicos que violan las políticas bajo las cuales el proyecto opera.

 Variantes
En las siguientes variantes, las entradas del servidor ns.wikipedia.org pueden ser envenenadas y redirigidas al servidor de nombres del atacante en la dirección w.x.y.z. Estos ataques asumen que el servidor para wikipedia.org es ns.wikipedia.org.

Para conseguir éxito en el ataque, el atacante debe forzar que el servidor DNS objetivo haga una petición hacia un dominio controlado por uno de los servidores de nombres del atacante.

 Redirección al servidor de nombres del dominio objetivo

La primera variante del envenenamiento de caché de DNS involucra redirigir el nombre del servidor del atacante del dominio hacia el servidor de nombres del dominio objetivo, luego se asigna a dicho servidor de nombres una dirección IP especificada por el atacante.

Petición del servidor DNS: cuáles son los registros de direcciones para subdominio.ejemplo.com?

 subdominio.ejemplo.com. IN A

Respuesta del atacante:

 Answer:
 (no response)

 Authority section:
 example.com. 3600 IN NS ns.wikipedia.org

 Additional section:
 ns.wikipedia.org. IN A w.x.y.z

Un servidor vulnerable puede almacenar en caché el registro A adicional (la dirección IP) para ns.wikipedia.org, permitiendo al atacante resolver consultas para todo el dominio wikipedia.org.

 Redirigir el registro DNS a otro dominio objetivo

La segunda variante de envenenamiento de caché DNS involucra redirigir el servidor de nombres de otro dominio hacia otro dominio no relacionado con la petición original de una dirección IP especificada por el atacante.

Petición del servidor DNS: cuáles son los registros de dirección para subdominio.ejemplo.com?

 subdominio.ejemplo.com. IN A

Respuesta del atacante:

 Answer:
 (no response)

 Authority section:
 wikipedia.org. 3600 IN NS ns.ejemplo.com.

 Additional section:
 ns.ejemplo.com. IN A w.x.y.z

Un servidor vulnerable puede almacenar la información de autoridad no relacionada de los registros de servidor de nombres de wikipedia.org, permitiendo al atacante resolver consultas para todo el dominio wikipedia.org.

 Responder antes del servidor de nombres real
La tercera variante de envenenamiento de caché de DNS, que es denominada falsificación de DNS (*DNS Forgery*) involucra hacer demorar la respuesta real hacia una consulta recursiva DNS hacia el servidor DNS. Las consultas DNS contienen un número identificador (*nonce*) de 16 bits, utilizado para identificar las respuestas asociadas a una respuesta dada. Si el atacante puede predecir exitosamente el valor de dicho número identificador y devolver la respuesta primero, el servidor aceptará la respuesta del atacante como válida. Si el servidor elige aleatoriamente el puerto origen de respuesta, el ataque se volverá más dificultoso, dado que la respuesta falsa debe ser enviada por el mismo puerto desde donde la consulta se originó.

Enviando un número de peticiones simultáneas de DNS al servidor para forzarlo a enviar más consultas recursivas, la probabilidad de predecir exitosamente uno de los números identificadores se incrementa. Esta modificación es una forma de ataque de cumpleaños (*birthday attack*).

 Prevención y mitigación
Muchos ataques de envenenamiento de caché contra servidores DNS pueden evitarse al desconfiar de la información que otros servidores DNS les pasan e ignorar cualquier registro DNS pasado que no sea directamente relevante para la consulta. Por ejemplo, las versiones de BIND 9.5.0-P1 [2] y superiores realizan estas comprobaciones. [3] La aleatorización del puerto de origen para solicitudes DNS, combinada con el uso de números aleatorios criptográficamente seguros para seleccionar tanto el puerto de origen como el nonce criptográfico de 16 bits , puede reducir en gran medida la probabilidad de ataques exitosos de DNS.

Una versión segura de DNS, DNSSEC, utiliza firmas criptográficas electrónicas validadas con un certificado digital confiable para determinar la autenticidad de los datos. DNSSEC puede bloquear ataques de envenenamiento de caché.

Este tipo de ataque puede ser mitigado también por las capas de transporte o aplicación para conseguir validación extremo a extremo (end-to-end validation) una vez que una conexión es establecida en extremo. Un ejemplo común de esto es el uso de Seguridad de Capa de Transporte y firmas digitales. Por ejemplo, usando la versión segura de HTTP, HTTPS, los usuarios pueden verificar si el certificado digital es válido y pertenece al dueño esperado de un sitio web. De manera similar, el programa de inicio de sesión remoto SSH verifica certificados digitales en los extremos (si los conoce) antes de proseguir con una sesión. Para aplicaciones que descargan actualizaciones automáticamente, la aplicación puede alojar una copia local del certificado digital de los datos y validar el certificado almacenado en la actualización de software contra el certificado alojado.

En abril del 2016, Google lanzó el servicio de DNS-sobre-HTTPS (*DNS-over-HTTPS*). Este esquema puede esquivar las limitaciones del protocolo DNS. Hace una revisión remota DNSSEC y transfiere los resultados usando un túnel seguro HTTPS.

 Véase también
 Domain Name System
 Servidor Raíz
 Pharming
 Spoofing

 Referencias

 Enlaces externos
 BIND 9 DNS Cache Poisoning - Discovered by Amit Klein (Trusteer)
 Predictable transaction IDs in Microsoft DNS server allow cache poisoning
 Microsoft Knowledge Base: How to prevent DNS cache pollution
 SANS DNS cache poisoning update
 DNS Threats & Weaknesses: research and presentations
 Blocking Unwanted Domain Names
 DNS Poisoning - a practical example
 Notes on the Domain Name System about Poisoning
 Nueva técnica de fraude informático: el pharming
 Pharming: ¿Es su sitio Web de confianza ... o una buena falsificación?
AyCarrumba - ARP and DNS spoofing tool
