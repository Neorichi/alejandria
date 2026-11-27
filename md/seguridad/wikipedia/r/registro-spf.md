---
type: Artículo de enciclopedia
title: Registro SPF
description: "El Sender Policy Framework (SPF) es un protocolo de autenticación de correo electrónico que permite a los propietarios de dominios especificar qué servidores de correo están autorizados a enviar mensajes en nombre de su …"
resource: https://es.wikipedia.org/wiki/Registro_SPF
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Registro_SPF"}
license: CC BY-SA 4.0
id: eswiki-Registro_SPF
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Registro SPF

El **Sender Policy Framework** (**SPF**) es un protocolo de autenticación de correo electrónico que permite a los propietarios de dominios especificar qué servidores de correo están autorizados a enviar mensajes en nombre de su dominio. Los servidores receptores pueden verificar esta información para detectar y filtrar mensajes que suplanten la identidad del dominio emisor (spoofing).

SPF forma parte de un conjunto de tecnologías de autenticación del correo junto con DKIM y DMARC.

 Funcionamiento
SPF utiliza el DNS para publicar la política de envío de un dominio. El proceso es el siguiente:

 El propietario del dominio publica un registro TXT en el DNS de su dominio con la lista de servidores autorizados.
 Cuando un servidor receptor recibe un mensaje, consulta el DNS del dominio indicado en el sobre del correo (dirección MAIL FROM).
 El servidor verifica si la IP del servidor remitente está incluida en el registro SPF.
 Según el resultado, puede aceptar, marcar o rechazar el mensaje conforme a la política definida.

 Formato del registro
El registro SPF se publica como un registro TXT en el DNS. Ejemplo:

v=spf1 include:_spf.google.com mx a ip4:203.0.113.10 ~all

Los principales mecanismos son:
 v=spf1: versión del protocolo (obligatorio).
 include:: incluye los rangos IP de un tercero (proveedor de correo).
 mx: autoriza los servidores MX del dominio.
 a: autoriza la IP del registro A del dominio.
 ip4: / ip6:: autoriza una IP o rango específico.
 all: política para el resto de remitentes, con los calificadores ~all (softfail) o -all (fail).

 Calificadores
Cada mecanismo puede tener un calificador que define la acción:
 + (pass): el remitente está autorizado (valor por defecto).
 - (fail): el remitente no está autorizado; el mensaje debe rechazarse.
 ~ (softfail): el remitente probablemente no está autorizado; el mensaje puede marcarse pero no rechazarse.
 ? (neutral): no se da ninguna indicación sobre la autorización.

 Limitaciones
 SPF solo verifica la dirección del sobre (MAIL FROM), no la cabecera From: visible para el destinatario.
 Un dominio solo puede tener un registro SPF; múltiples registros SPF generan errores de validación.
 SPF se rompe con el reenvío de correo tradicional, ya que el servidor reenviador no suele estar en la lista SPF del dominio original.
 El protocolo no protege contra el spoofing de la cabecera From: por sí solo; se requiere DMARC para ello.

 Historia
SPF fue propuesto por Meng Weng Wong en 2003 y estandarizado por la IETF en el RFC 7208 (2014), que obsoletó el RFC 4408 (2006). Es uno de los mecanismos de autenticación de correo más ampliamente adoptados.

 Véase también
 DKIM
 DMARC
 Email spoofing
 Correo electrónico

 Referencias

 Enlaces externos
 RFC 7208 — Sender Policy Framework (IETF)
