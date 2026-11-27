---
type: Artículo de enciclopedia
title: Whonix
description: Whonix es una distribución basada en Debian GNU/Linux enfocada a la seguridad.
resource: https://es.wikipedia.org/wiki/Whonix
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Whonix"}
license: CC BY-SA 4.0
id: eswiki-Whonix
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Whonix

- **Family:** Unix-like
- **Desarrollador:** Comunidad de desarrolladores de Whonix
- **Modelo desarrollo:** Código abierto
- **Última versión:** 17.0.4.5
- **Núcleo:** Kernel
- **Núcleo tipo:** Monolítico
- **Licencia:** Principalmente la GNU GPL
- **Español:** Sí / No

**Whonix** es una distribución basada en Debian GNU/Linux enfocada a la seguridad. Busca proporcionar intimidad, seguridad y anonimato en Internet. El sistema operativo consta de dos máquinas virtuales, una estación de trabajo y una pasarela a la red Tor, ejecutando Debian GNU/Linux. Todas las comunicaciones están forzadas a pasar bajo la red Tor.

 Diseño
Whonix está distribuido como dos imágenes de máquinas virtuales: una pasarela y una estación de trabajo. Estas imágenes están instaladas en el sistema operativo anfitrión. Cada imagen virtual contiene un GNU/Linux modificado basado en Debian. Las actualizaciones están distribuidas vía Tor utilizando el sistema de paquetería apt-get de Debian.

Los motores de virtualización soportados son VirtualBox, Qubes-OS y Linux KVM.

En el inicio cada máquina virtual comprueba que todo el software está al día, y que la fecha y hora esté correctamente configurada.

La máquina virtual que funciona como pasarela es la responsable de ejecutar Tor, y tiene dos interfaces virtuales de red. Una de ellas está conectada a internet via NAT en la VM, y es usada para comunicarse con la red Tor. La otra está conectada en una LAN virtual que corre solamente bajo el anfitrión.

La estación de trabajo ejecuta las aplicaciones del usuario. Está conectada solo a la LAN virtual, y solo puede conectarse directamente con la pasarela, la cual obliga a todo el tráfico proveniente de la estación de trabajo a pasar bajo la red Tor. La estación de trabajo puede "ver" solo direcciones de IP  en la LAN interna, los cuales son las mismas en cada instalación de Whonix.

Las aplicaciones del usuario no tienen conocimiento de la "IP real" del usuario. No tienen acceso a ninguna información del hardware físico. Para conseguir esa información, una aplicación podría encontrar una forma de "salir" de Virtualbox, o corromper la pasarela (probablemente por un error en Tor o en el núcleo Linux de la pasarela).

El navegador preinstalado en la estación de trabajo es la versión modificada de Mozilla Firefox proporcionada por el proyecto Tor como parte del paquete del navegador Tor. Este navegador ha sido modificado para reducir la cantidad de información del sistema que podría filtrarse a los servidores web.

Es diferente a Tails. Whonix no es "amnésico". Tanto la pasarela como la estación de trabajo conservan su información en cada reinicio. El no ser amnésico mejora la seguridad en la pasarela, al permitir al sistema de "entrada" de Tor elegir los puntos de entrada más antiguos en la red Tor, reduciendo la capacidad de adversarios para atrapar a usuarios utilizando nodos maliciosos.

Por otro lado, una estación de trabajo no amnésica podría permitir a los atacantes, especialmente a los operadores de servicios web, inyectar datos y asociar sesiones de usuario con otra, a pesar de las medidas de seguridad del navegador. Es posible que los usuarios obliguen a la estación de trabajo a ser parcial o totalmente amnésica, restableciéndola manualmente a estados anteriores, aunque el desarrollador no sugiera eso. Es posible ejecutar más de una estación de trabajo con una sola pasarela.

Una configuración avanzada usa dos computadoras físicas separadas, con la pasarela funcionando en el hardware físico de una de las computadoras, y la estación de trabajo en una máquina virtual alojada en la segunda computadora. Esto protege de ataques en Virtualbox.

 Referencias
