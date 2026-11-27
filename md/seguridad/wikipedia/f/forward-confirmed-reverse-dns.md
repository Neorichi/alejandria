---
type: Artículo de enciclopedia
title: Forward confirmed reverse DNS
description: "Forward confirmed reverse DNS (FCrDNS), también conocido como inversa DNS de círculo completo, DNS inverso doble o iprev, es un parámetro de configuración de red en la que una determinada dirección IP tiene tanto …"
resource: https://es.wikipedia.org/wiki/Forward_confirmed_reverse_DNS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Forward_confirmed_reverse_DNS"}
license: CC BY-SA 4.0
id: eswiki-Forward_confirmed_reverse_DNS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Forward confirmed reverse DNS

**Forward confirmed reverse DNS** (FCrDNS), también conocido como inversa DNS de círculo completo, DNS inverso doble o iprev, es un parámetro de **configuración de red** en la que una determinada dirección IP tiene tanto entradas DNS directas (nombre-a-dirección) como inversas (dirección-a-nombre) que coinciden entre sí. Esta es la configuración estándar esperada por los estándares de Internet que apoyan muchos protocolos dependientes de DNS. Las  y  (Informativo) lo recomiendan como una buena práctica, pero no es un requisito de la RFC que definen estándares que rigen el funcionamiento del DNS.

Una verificación FCrDNS puede crear una forma débil de autenticación de que existe una relación válida entre el titular de un nombre de dominio y el propietario de la red que se ha dado una dirección IP. Aunque débil, esta autenticación es lo suficientemente fuerte para que pueda ser usada para fines de poner en listas blancas, ya que los spammers y phishers no pueden por lo general sobrepasar esta verificación cuando utilizan *ordenadores zombi* para la suplantación de identidad en el correo. Es decir, el DNS inverso podría verificar, pero por lo general será parte de otro dominio que el nombre de dominio pretendido.

Usar el servidor de correo del ISP como relé puede resolver el problema de DNS reverso, ya que el requisito es que la búsqueda directa y la búsqueda inversa para el relé que envía tienen que coincidir, no tiene por qué estar relacionado con el campo "De:" o el dominio de envío de mensajes que reenvía.

Otros métodos para establecer una relación entre una dirección IP y un dominio de correo electrónico son el Sender Policy Framework (SPF) y el registro MX. Sin embargo, SPF se basa en DNS reversa.

Los ISPs que no quieren o no pueden configurar el DNS inverso generarán problemas para hosts en sus redes, ya que no serán capaces de soportar aplicaciones o protocolos que requieren que los DNS reverso estén de acuerdo con el registro A correspondiente. Los ISPs que no pueden o no proporcionarán DNS inversa en última instancia limitarán la capacidad de su base de clientes para utilizar los servicios de Internet que proporcionan de una manera efectiva y segura.

 Aplicaciones
 La mayoría de los agentes de transferencia de correo electrónico (software de servidor) utilizan una verificación FCrDNS y si hay un nombre de dominio válido, lo ponen en el  campo de encabezado para rastreo "Recibido:".
 Algunos agentes de transferencia de correo electrónico realizarán la verificación FCrDNS sobre el nombre de dominio que figura en los comandos de SMTP HELO y EHLO. Esto puede violar el RFC 2821 y así el correo electrónico por lo general no es rechazado de forma predeterminada.
 El sistema antifalsificación de remitentes Sender Policy Framework utiliza una revisión FCrDNS en su mecanismo "ptr:".
 Algunos filtros de spam de correo electrónico utilizan revisiones FCrDNS como un método de autenticación para los nombres de dominio o con fines de listas blancas, de acuerdo con RFC 7001, por ejemplo.
 SpamCop utiliza las revisiones FCrDNS, lo que a veces causa problemas a los usuarios de SpamCop que también son clientes de proveedores de servicios de Internet que no proporcionan registros DNS y rDNS adecuadamente emparejados para servidores de correo.
 Algunos servidores de FTP, Telnet y TCP Wrapper realizan revisiones FCrDNS.
 Algunos servidores IRC realizan controles FCrDNS para prevenir el abuso.

 Referencias

 Enlaces externos
 Consideraciones para el uso de DNS Reverse Mapping
 Herramienta para probar Forward Confirmed RDNS
