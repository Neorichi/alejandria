---
type: Artículo de enciclopedia
title: Open relay
description: "Se entiende como open relay (‘relé abierto’ en inglés) un servidor SMTP configurado de tal manera que permite que cualquier usuario de Internet lo use para enviar correo electrónico a través de él, no solamente el …"
resource: https://es.wikipedia.org/wiki/Open_relay
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Open_relay"}
license: CC BY-SA 4.0
id: eswiki-Open_relay
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Open relay

Se entiende como ***open relay*** (‘relé abierto’ en inglés) un servidor SMTP configurado de tal manera que permite que cualquier usuario de Internet lo use para enviar correo electrónico a través de él, no solamente el correo destinado a, o procedente de usuarios conocidos. Esta solía ser la configuración por defecto en muchos servidores de correo; de hecho, era la forma en que Internet fue creada inicialmente, pero las retransmisiones de correo abiertas se han convertido en impopulares debido a su explotación por parte de los spammers y gusanos. Muchos relays se cerraron o fueron puestos en listas negras por otros servidores.

 Historia y tecnología
Hasta la década de 1990, los servidores de correo se configuraban comúnmente intencionalmente como relays abiertos; esta configuración también era con frecuencia la configuración por defecto de instalación en sistemas UNIX. El método tradicional de store-and-forward de transmitir un mensaje de correo electrónico a su destino requería que fuera pasando de un ordenador a otro (a través y más allá de Internet) a través de módems telefónicos. Para muchas de esas redes iniciales, como UUCPNET, FidoNet y Bitnet, listas de máquinas que eran retransmisores abiertos eran una parte fundamental de esas redes. El filtrado de un mensaje de correo electrónico y la velocidad de entrega de correo electrónico no eran prioridades en ese momento y en cualquier caso, el gobierno y los servidores educacionales que iniciaron la Internet estaban cubiertas por un decreto federal que prohíbe la transferencia de mensajes comerciales. RFC

 El abuso por spammers
A mediados de la década de 1990, con el auge del spam, los spammers recurrieron a enviar su correo electrónico a través de servidores de terceros para evitar la detección y de explotar los recursos adicionales de estos servidores abiertos. Los spammers enviarían un correo electrónico a la retransmisión abierta y (efectivamente) incluir una lista con copia oculta grande, entonces el open relay transmitiría el spam a la lista entera. Si bien esto reducía en gran medida las necesidades de ancho de banda para los spammers en un momento en el que las conexiones a Internet eran limitadas, obligó que cada spam fuera una copia exacta y por lo tanto más fácil de detectar. Después de que el abuso por parte de los spammers se generalizó, el funcionamiento de un relay abierto llegó a ser mal visto entre la mayoría de los administradores de servidores de Internet y otros usuarios importantes. El RFC 2505 y RFC 5321 (que define SMTP) recomiendan que no haya retransmisiones abiertas. La naturaleza de copia exacta de spam utilizando relés abiertos hacía que fuera fácil crear sistemas de detección de correo electrónico a granel, como Vipul's Razor y el Distributed Checksum Clearinghouse. Para contrarrestar esto, los spammers se vieron obligados a empezar a utilizar engañadores de hash para hacerlos menos eficaces y la ventaja de utilizar relés abiertos se perdió, ya que cada copia del spam era "único" y tenía que ser enviado de forma individual.

Ya que los retransmisores de correo abiertos no hacen ningún esfuerzo por autenticar el remitente de un correo electrónico, éstos son vulnerables a la suplantación de dirección.

 Esfuerzos *antispam*
Muchos proveedores de servicios de Internet utilizan DNSBLs (Listas de Bloqueo basado en DNS) para rechazar el correo de retransmisiones abiertas. Una vez que se detecta o se informó que un servidor de correo permite a terceras partes enviar correo a través de este, se añadirán a una o más de dichas listas, y otros servidores de correo electrónico que utilizan esas listas rechazarán cualquier mensaje que provenga de esos sitios. El relé no necesita realmente ser utilizado para enviar spam a la lista negra: en vez de eso, puede ser incluido en la lista negra después de una prueba simple que solo confirma el acceso abierto.

Esta tendencia reduce el porcentaje de los remitentes de correo que eran retransmisiones abiertas desde el 90% hasta menos del 1% a lo largo de varios años. Esto llevó a los spammers a adoptar otras técnicas, como el uso de botnets de ordenadores zombis para enviar spam.

Una de las consecuencias de la nueva inaceptabilidad de retransmisores abiertos era un inconveniente para algunos usuarios finales y algunos proveedores de servicios de Internet. Para permitir a los clientes utilizar sus direcciones de correo electrónico en sitios de Internet distintos de sistemas de la compañía (por ejemplo, en la escuela o en el trabajo), muchos sitios de correo permiten explícitamente la retransmisión abierta para que los clientes puedan enviar correo electrónico a través del ISP desde cualquier lugar. Cuando el uso de retransmisores abiertos se convirtió en inaceptable debido al abuso ( e inutilizable debido a bloqueo de retransmisiones abiertas), los proveedores de Internet y otros sitios tuvieron que adoptar nuevos protocolos para permitir que los usuarios remotos para enviar correo. Estos incluyen hosts inteligentes, SMTP-AUTH, POP antes de SMTP, y el uso de redes privadas virtuales (VPN). El IETF ha escrito unas mejores prácticas actuales que cubren Operaciones de envío de correo electrónico en el RFC 5068.

Tenga en cuenta que lo anterior solo se convierte en un problema si el usuario desea ( o tiene que) continuar enviando el correo electrónico de forma remota, utilizando el mismo servidor SMTP que estuvieran accediendo previamente a nivel local. Si tienen acceso válido a otro servidor SMTP de su nueva ubicación remota, a continuación, por lo general será capaz de utilizar ese nuevo servidor para enviar mensajes de correo electrónico como si fuera de su antigua dirección, incluso cuando este servidor se encuentra asegurado. (Aunque esto puede implicar alguna reconfiguración del cliente de correo electrónico del usuario que puede no ser del todo sencilla).

La Ley de Can Spam de 2003 establece que es ilegal para enviar spam a través de una retransmisión abierta en los Estados Unidos, pero no contiene ninguna disposición en relación con el envío de correo electrónico personal a través de ellos, o en cuanto a su operación, aunque la eficacia del acto ha sido cuestionada.

 Proponentes modernos
El más famoso open relay que opera hoy en día es probablemente el de John Gilmore, quien sostiene que mantener una retransmisión abierta es un asunto de libertad de expresión. Su servidor está incluido en muchas listas negras de retransmisión abierta (muchos de los cuales son generados por la "detección automática", es decir, por listas negras *antispam* que envían un correo electrónico de prueba a otros servidores para ver si van a ser transmitidos). Estas medidas hacen que gran parte de su correo electrónico saliente sea bloqueado. Junto con su configuración deliberada de este servidor, la retransmisión abierta permite a las personas enviar mensajes de correo electrónico sin que su dirección IP esté visible directamente para el destinatario y por lo tanto enviar un correo electrónico de forma anónima. En 2002, su open relay, junto con otros 24, fue utilizado por un gusano informático para propagarse.

John Gilmore y otros defensores de retransmisión abierta declaran que no apoyan el correo no deseado, pero ven una amenaza más grande en los intentos de limitar las capacidades de la Web que puedan bloquear la evolución de las nuevas tecnologías de próxima generación. Comparan las restricciones de comunicación en red con las restricciones que algunas empresas de telefonía trataron de colocar en sus líneas en el pasado, que impedían la transferencia de datos en lugar de la solo voz.

 Véase también
 SMTP
 Inseguridad informática
 Spam
 Email spoofing
 Correo electrónico

 Referencias

 Enlaces externos
 Herramienta para probar si un MTA es Open relay
