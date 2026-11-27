---
type: Artículo de enciclopedia
title: Ataque de predicción de secuencia TCP
description: Un ataque de predicción de secuencia TCP es un intento de predecir el número secuencial usado para identificar los paquetes en una conexión TCP, puede ser usado para falsificar paquetes.
resource: https://es.wikipedia.org/wiki/Ataque_de_predicción_de_secuencia_TCP
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_de_predicción_de_secuencia_TCP"}
license: CC BY-SA 4.0
id: eswiki-Ataque_de_predicción_de_secuencia_TCP
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque de predicción de secuencia TCP

Un **ataque de predicción de secuencia TCP** es un intento de predecir el número secuencial usado para identificar los paquetes en una conexión TCP, puede ser usado para falsificar paquetes.

El atacante espera adivinar correctamente el número secuencial que será utilizado por el host que envía el paquete. Si el atacante logra adivinar este número, podrá enviar paquetes falsificados al host de destino que parecerán originados por el host que envía el paquete, a pesar de que los paquetes falsos pueden ser originados por un tercero que controla el ataque.  Una manera de que esto ocurra es que el atacante escuche la conversación que ocurre entre diversos host de confianza y, posteriormente, enviar paquetes utilizando la misma dirección IP de origen. Al monitorear el tráfico antes de que el ataque sea montado, el atacante puede descubrir el número secuencial. Después de saber el número secuencial y la dirección IP, se convierte en una carrera entre el host de confianza y el atacante por ver quién envía el paquete correcto primero. Una forma común que utiliza el atacante para enviar el paquete primero es atacar el host de confianza a través de, por ejemplo, un ataque de denegación de servicios. Una vez que el atacante tiene control sobre la conexión, es capaz de mandar paquetes falsos sin necesidad de recibir respuesta.

Si un atacante logra que se reciban estos paquetes falsos, puede causar varias acciones maliciosas, incluyendo inyección a la conexión TCP de datos de preferencia del atacante y el cierre prematuro de una conexión existente TCP a través de la inyección de paquetes RST.

Teóricamente, información como diferencias de tiempo o información de capas bajas de protocolos, pueden permitir al host de destino distinguir paquetes auténticos de TCP del host de confianza y paquetes falsos, esto,  con el número secuencial correcto enviado por el atacante. Si esa información está disponible para el host de destino, si el atacante no es capaz de falsificar esa información y el host de destino junta y usa esa información correctamente, entonces el host de destino puede ser “inmune” a ataques de secuencia tipo TCP. Usualmente, este no es caso, así que el número secuencial es el primer medio de protección de tráfico TCP contra este tipo de ataque.

Otra solución a este ataque es configurar un router o un firewall para no permitir que entren paquetes de una fuente externa, pero con una dirección IP interna. Aunque esto no soluciona el ataque, va a prevenir que los potenciales ataques no lleguen a su destino.

Véase también
Aircrack-ng
AirSnort
BackTrack
Ataque de denegación de servicio
Nmap
Analizador de paquetes
Snort
SYN flood
Wireshark
Pouned*

Referencias

Enlaces externos
 RFC 1948, Defending Against Sequence Number Attacks, May 1996, obsoleted by RFC 6528 Steven M. Bellovin.
 RFC 6528, Defending against Sequence Number Attacks, February 2012 Standard Track Steven M. Bellovin
 A Weakness in the 4.2BSD Unix TCP/IP Software
