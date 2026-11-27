---
type: Artículo de enciclopedia
title: Red de mezcla
description: "Las redes de mezcla son protocolos de enrutamiento que crean comunicaciones difíciles de rastrear usando una cadena de servidores proxy conocidos como mezclas, los cuáles reciben mensajes de múltiples emisores, los …"
resource: https://es.wikipedia.org/wiki/Red_de_mezcla
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Red_de_mezcla"}
license: CC BY-SA 4.0
id: eswiki-Red_de_mezcla
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Red de mezcla

Las **redes de mezcla** son protocolos de enrutamiento que crean comunicaciones difíciles de rastrear usando una cadena de servidores proxy conocidos como *mezclas*, los cuáles reciben mensajes de múltiples emisores, los reordenan y los devuelven en orden aleatorio al próximo destino (posiblemente otro nodo de mezcla). Esto rompe el enlace entre la fuente de la petición y el destino, haciendo más difícil la tarea de alguien que pretende escuchar las comunicaciones de extremo a extremo. Además, las mezclas solo conocen el nodo inmediatamente precedente del cual recibieron cada mensaje y el destino inmediato siguiente al cuál enviar los mensajes fuera de orden, lo que hace que la red sea resistente a nodos de mezcla maliciosos.Cada mensaje viaja cifrado a cada proxy utilizando criptografía asimétrica; el cifrado resultante se forma de a capas como una muñeca rusa (con la diferencia de que cada "muñeca" es de la misma medida) con el mensaje como el innermost capa.  Cada proxy descifra el mensaje cifrado de su propia capa para revelar dónde enviar el mensaje luego.  Si todos menos uno de los servidores proxy son comprometidos por el adversario, todavía se puede lograr cierta imposibilidad de rastreao contra adversarios más débiles.

El concepto de redes de mezcla fue descrito por primera vez por David Chaum en 1981. Las aplicaciones basadas en este concepto incluyen remailers anónimos (como Mixmaster) y el encaminamiento cebolla (con proyectos como Tor o Nym).

 Historia
David Chaum publicó el concepto de Redes de Mezcla en 1981 en su ensayo: "Untraceable electronic mail, return addresses, and digital pseudonyms". El ensayo era para su trabajo de tesis de maestría, poco después de que sea introducido al campo de la criptografía a través de los trabajos sobre criptografía asimétrica de Martin Hellman, Whitfield Diffie y Ralph Merkle. Si bien la criptografía asimétrica garantizaba la seguridad de la información, Chaum creía que existían vulnerabilidades a la privacidad personal en el los metadatos encontrados en las comunicaciones. Algunas vulnerabilidades que permitían comprometer la privacidad personal incluían la hora de los mensajes enviados y recibidos, el tamaño de los mismos y la dirección del emisor original. Cita el ensayo de Martin Hellman y Whitfield "Direcciones Nuevas en Criptografía" (1976) en su trabajo.
 Referencias
