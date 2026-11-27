---
type: Artículo de enciclopedia
title: Cryptocat
description: Cryptocat fue una aplicación web libre destinado a permitir conversar en línea de forma cifrada y segura.
resource: https://es.wikipedia.org/wiki/Cryptocat
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cryptocat"}
license: CC BY-SA 4.0
id: eswiki-Cryptocat
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cryptocat

- **Desarrollador:** Nadim Kobeissi
- **Última versión:** 2.0.37
- **Género:** Comunicación Segura
- **Lenguaje programación:** JavaScript
- **Sistema operativo:** Multiplataforma
- **Licencia:** GNU General Public License
- **Idiomas:** Multilenguaje

**Cryptocat** fue una aplicación web libre destinado a permitir conversar en línea de forma cifrada y segura. Cryptocat cifra las conversaciones (chats) en el lado del cliente (usuario), confiando solo en el servidor con datos ya cifrados. Cryptocat se ofrece como una aplicación para  GNU/Linux y MacOS, como una extensión para los navegadores Mozilla Firefox, Google Chrome, y Apple Safari.

Cryptocat proporciona un medio para comunicaciones cifrado interrumpido, proporcionando mayor privacidad que servicios como Google Talk, al mismo tiempo que mantiene un nivel más de accesibilidad que otras plataformas de cifrado de alto nivel, y además permite múltiples usuarios en una sala de chat.

 Historia
Fue lanzado como una aplicación web en mayo de 2011. Al siguiente año, en junio, el desarrollador y creador fue detenido en la frontera de Estados Unidos y fue cuestionado sobre su aplicación. En junio de 2013 el investigador Steve Thomas descubrió un *bug* de seguridad que se podía usar para desencriptar mensajes de grupos enviados entre septiembre de 2012 y abril de 2013. Sin embargo, los mensajes privados entre individuales no se veían afectados y el problema fue resuelto en un mes con una actualización de seguridad e informando a los usuarios sobre las conversaciones que se vieron comprometidas.

En febrero de 2014 una auditoría de seguridad de la firma *iSec Partners* criticó el modelo de autenticación de *Cryptocat* como insuficiente, los desarrolladores respondieron con una mejora en la autenticación de los usuarios y una mejora en la detección de ataques *man-in-the-middle*. En el año 2016 el proyecto entró en suspensión, para ser relanzado meses después con el código fuente completamente reescrito y una nueva aplicación para escritorio.

 Cómo funciona
Cryptocat usa el protocolo Off-the-Record Messaging (OTR) para cifrar mensajes privados. A partir de que Cryptocat genera pares de llaves para cada conversación (chat), implementa un formulario confidencialidad directa perfecta (perfect forward secrecy ). Cryptocat también puede ser utilizado de manera conjunta con Tor a fin de mantener anónima los detalles de conexión de cliente del servidor. El proyecto también planea crear una versión embebida o integrada para dispositivos Raspberry Pi.

 Arquitectura
Usa un algoritmo *Double Ratchet Algorithm* y se establece una sesión segura con un *handshake* usando criptografía de curvas elípticas, una manera similar de garantizar la seguridad como la usada por la aplicación *Signal*. El objetivo de *Cryptocat* es que sus mensajes obtengan confidencialidad, integridad, autenticidad de la fuente, seguridad e indistinguibilidad incluso a través de una red controlada por un atacante activo.

Cryptocat utiliza el estándar de encriptación avanzada *Galois/Counter* para cifrado autenticado, *Curve25519*, Diffie-Hellman de curva elíptica, *HMAC-SHA256* para derivación de clave y Ed25519 para firmar los mensajes. Para limitar el efecto de una clave comprometida, las claves a largo plazo se usan exclusivamente una vez para el intercambio de clave autenticado inicial, y una vez para firmar una preclave firmada de plazo intermedio generada recientemente.

 Problemas de seguridad
Versiones anteriores de Cryptocat fueron cuestionadas por no utilizar fuentes de entropía apropiadas. De todas maneras, versiones más recientes se basan en la generación de números aleatorios incluida en los navegadores web.

El desarrollador de Cryptocat Nadim Kobeissi fue arrestado e interrogado en la frontera de Estados Unidos por el Departamento de Seguridad Nacional de los Estados Unidos en junio de 2012 sobre la resistencia a la censura. Y difundió el incidente en Twitter; lo que provocó cobertura de los medios y un incremento en la popularidad de Cryptocat.

El 2013, la red de Cryptocat migró a Bahnhof, el proveedor de alojamiento web sueco conocido por estar construido en el interior de un refugio antinuclear de la Guerra Fría.

 Véase también
 Tor
 Privacidad en Internet
 Libertad de información
 Criptoanarquismo
 Hacktivismo

 Referencias

 Enlaces externos
