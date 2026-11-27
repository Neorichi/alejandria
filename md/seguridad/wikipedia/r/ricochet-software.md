---
type: Artículo de enciclopedia
title: Ricochet (software)
description: "Ricochet o Ricochet IM es un proyecto de software libre, multiplataforma y mensajería instantánea desarrollado inicialmente por John Brooks y posteriormente adoptado como el proyecto oficial del cliente de mensajería …"
resource: https://es.wikipedia.org/wiki/Ricochet_(software)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ricochet_(software)"}
license: CC BY-SA 4.0
id: eswiki-Ricochet_(software)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ricochet (software)

- **Nombre:** Ricochet
- **Desarrollador:** Invisible.im
- **Licencia:** BSD
- **Última versión:** LSR
- **Lenguaje programación:** C++
- **Sistema operativo:** Windows, OS X, Linux, FreeBSD

**Ricochet** o **Ricochet** **IM** es un proyecto de software libre, multiplataforma y mensajería instantánea desarrollado inicialmente por John Brooks y posteriormente adoptado como el proyecto oficial del cliente de mensajería instantánea del grupo Invisible.im. El objetivo del grupo Invisible.im es para ayudar a las personas a mantener la privacidad mediante el desarrollo de un cliente de mensajería instantánea "libre de metadatos".

 Historia
Originalmente llamado Torsión IM, Ricochet fue renombrado en junio de 2014. Ricochet es una alternativa moderna a TorChat, que no ha sido actualizado en varios años, y a Tor Messenger, el cual está descontinuado. El 17 de septiembre de 2014, se anunció que el grupo Invisible.im trabajaría con Brooks en el desarrollo de Ricochet en un artículo de Kim Zetter en *Wired*. Zetter también escribió que los planes futuros de Ricochet incluían un rediseño de protocolo y capacidades de transferencia de archivos. El rediseño del protocolo se llevó a cabo en abril de 2015.

En febrero de 2016, los desarrolladores de Ricochet hicieron pública una auditoría de seguridad que había sido patrocinada por Open Technology Fund y realizada por NCC Group en noviembre de 2015. Los resultados de la auditoría fueron "razonablemente positivos". La auditoría identificó "múltiples áreas de mejora" y una vulnerabilidad que podría utilizarse para desanonimizar a los usuarios. Según Brooks, la vulnerabilidad ha sido corregida en la última versión.

 Tecnología
Ricochet es un servicio de mensajería instantánea descentralizada, lo que significa que no hay un servidor al que conectarse y con el que compartir metadatos. Además, usando Tor, Ricochet inicia un servicio oculto de Tor localmente en el ordenador de una persona y puede comunicarse sólo con otros usuarios de Ricochet que también están ejecutando sus propios servicios ocultos de Tor creados por Ricochet. De esta manera, la comunicación de Ricochet nunca deja la red Tor. Un nombre de usuario (ejemplo: ricochet:hslmfsg47dmcqctb) se genera automáticamente al iniciar por primera vez Ricochet; la primera mitad del nombre de usuario es la palabra "ricochet", y la segunda mitad es la dirección del servicio oculto Tor. Antes de que dos usuarios de Ricochet puedan hablar, al menos uno de ellos debe compartir en privado o públicamente su nombre de usuario único de alguna manera.

 Beneficios de privacidad

 Ricochet no revela las direcciones IP de los usuarios ni sus ubicaciones físicas porque usa Tor.
 El contenido de los mensajes está autenticado criptográficamente y es privado.
 No es necesario registrarse en ningún sitio para usar Ricochet, especialmente con un servidor fijo.
 La información de la lista de contactos se almacena localmente, y sería muy difícil para las técnicas de vigilancia pasiva determinar con quién está chateando el usuario.
 Ricochet no guarda el historial de chat. Cuando el usuario cierra una conversación, el registro de chat no es recuperable.
 El uso de los servicios ocultos de Tor impide que el tráfico de la red salga alguna vez de la red Tor, con lo que se preserva el anonimato y se complica la vigilancia pasiva de la red.
 Ricochet es una aplicación portátil, los usuarios no necesitan instalar ningún software para usar Ricochet. Ricochet se conecta a la red Tor automáticamente.

 Avisos de seguridad

 Un sistema informático ya comprometido normalmente derrotará las protecciones de privacidad que ofrece Ricochet, como un malware de registro de pulsaciones de teclas.
 Aunque Ricochet usa Tor, otras aplicaciones no usarán Tor a menos que el usuario haya configurado independientemente servicios adicionales de Tor en su ordenador.
 Las técnicas de vigilancia activa y pasiva todavía pueden determinar si el usuario está utilizando la Internet y cuándo, pero no necesariamente lo que está haciendo en la Internet.
 Dado que un usuario de Ricochet no se registra ni inicia sesión en ningún sitio para utilizar Ricochet, ni siquiera con una contraseña, es importante implementar una seguridad física por capas, incluyendo la encriptación del disco, para proteger a Ricochet. No hay encriptación presente en los restos de datos.
 Los usuarios de Linux Tails, y otros usuarios de sistemas operativos live, puede opcionalmente hacer una copia de seguridad Ricochet en servicios de nube de conocimiento cero como SpiderOak, o en una unidad USB de propiedad personal (idealmente encriptada).

 Véase también

 Ring (software)
 Tox (Protocolo)

 Referencias

 Enlaces externos
