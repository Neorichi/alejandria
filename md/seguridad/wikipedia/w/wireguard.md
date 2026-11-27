---
type: Artículo de enciclopedia
title: WireGuard
description: "WireGuard es una aplicación de software libre y de código abierto y un protocolo de comunicación que implementa técnicas de red privada virtual (VPN) para crear conexiones seguras punto a punto en configuraciones …"
resource: https://es.wikipedia.org/wiki/WireGuard
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/WireGuard"}
license: CC BY-SA 4.0
id: eswiki-WireGuard
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# WireGuard

- **Nombre:** WireGuard
- **Desarrollador:** Jason A. Donenfeld
- **Autor:** Jason A. Donenfeld
- **Última versión:** 1.0.20220627
- **Fecha última versión:** 27 de junio de 2022
- **Género:** Red privada virtual
- **Lenguaje programación:** C (módulo de kernel de Linux), Go (implementación del espacio de usuario)
- **Licencia:** GPLv2

**WireGuard** es una aplicación de software libre y de código abierto y un protocolo de comunicación que implementa técnicas de red privada virtual (VPN) para crear conexiones seguras punto a punto en configuraciones enrutadas o puenteadas. Se ejecuta como un módulo dentro del núcleo Linux y tiene como objetivo un mejor rendimiento que los protocolos de tunelización IPsec y OpenVPN. Fue escrito por Jason A. Donenfeld y se publica bajo la segunda versión de la GNU General Public License (GPL). El sitio web oficial describe el protocolo como un trabajo en progreso.

 Características
WireGuard tiene como objetivo proporcionar una VPN que sea simple y altamente efectiva. Una revisión realizada por *ArsTechnica* observó que tecnologías VPN populares como OpenVPN e IPsec son a menudo complejas de configurar, desconectan fácilmente (en ausencia de configuración adicional), toman un tiempo considerable negociando reconexiones, pueden usar cifrados obsoletos y tienen un código relativamente masivo (de 400,000 a 600,000 líneas de código para los dos ejemplos dados) lo que hace que sea más difícil encontrar bugs.

El diseño de WireGuard busca reducir estos problemas, haciendo el túnel más seguro y fácil de administrar por defecto. Mediante el uso de versionado de paquetes de criptografía, se centra en cifradores que se consideran entre los métodos de encriptación actuales más seguros, y también tiene una base de código de alrededor de 4000 líneas, aproximadamente el 1% de OpenVPN o IPsec, lo que facilita las auditorías de seguridad. *Ars Technica* informó que en sus pruebas, los túneles estables fueron fáciles de crear con WireGuard, en comparación con las alternativas, y comentó que sería "difícil regresar" a largos retrasos de reconexión, en comparación con las reconexiones instantáneas y "sin disparates" de WireGuard.

 Protocolo
WireGuard utiliza Curve25519 para el intercambio de claves, ChaCha20 para la encriptación, Poly1305 para la autenticación de datos, SipHash para claves de hashtables y BLAKE2s para el hashing. Soporta la capa 3 para IPv4 e IPv6 y puede encapsular v4 en v6 y viceversa.

En mayo de 2019, investigadores del INRIA publicaron una prueba del protocolo verificada por una máquina, producida utilizando el asistente de pruebas de CryptoVerif.

 Disponibilidad
 Implementaciones
Las implementaciones del protocolo WireGuard son las siguientes:

 La implementación inicial de Donenfeld, escrita en C y Go.
 BoringTun de Cloudflare, una implementación de espacio de usuario escrita en Rust .
 La implementación de Matt Dunwoodie para OpenBSD, escrita en C.
 La implementación wg(4) de Ryota Ozaki para NetBSD, escrita en C.
 La implementación de FreeBSD está escrita en C y comparte la mayor parte de la ruta de datos con la implementación de OpenBSD.
 Existe una implementación nativa del *kernel* de Windows denominada "wireguard-nt", disponible desde agosto de 2021.
 Los módems-enrutadores AVM Fritz!Box que admiten Fritz!OS en su versión 7.39 y posteriores permiten conexiones WireGuard de sitio a sitio a partir de la versión 7.50.
 Hay una implementación en espacio de usuario del procesamiento de paquetes vectoriales escrita en C.

 Historia
Las primeras snapshots de la base de código existen desde el 30 de junio de 2016. Cuatro de los primeros usuarios de WireGuard fueron los proveedores de servicios de VPN Mullvad, AzireVPN, IVPN y cryptostorm. WireGuard ha recibido donaciones de Mullvad, Private Internet Access, IVPN y la NLnet Foundation.

A fecha de junio de 2018, los desarrolladores de WireGuard recomiendan tratar el código y el protocolo como experimentales, y advierten que aún no han logrado una versión estable compatible con el seguimiento de CVE de cualquier vulnerabilidad de seguridad que pueda descubrirse.

El 9 de diciembre de 2019, David Miller, responsable principal de la pila de red de Linux, aceptó los parches de WireGuard en el árbol de mantenimiento "net-next", para su inclusión en un kernel próximo. El 28 de enero de 2020, Linus Torvalds fusionó el árbol net-next de David Miller, y WireGuard ingresa al árbol principal del núcleo Linux.

 Recepción
El senador de Oregón, Ron Wyden, recomendó al National Institute of Standards and Technology (NIST) que evalúen WireGuard como reemplazo de tecnologías existentes como IPsec y OpenVPN.

Este sistema ha sido recibido muy favorablemente por toda la comunidad, ganando mención en docenas de canales de tecnología, debido a su gran velocidad comparado con sistemas como OpenVPN y un proceso de instalación muy sencillo

 Implementaciones
Entre las implementaciones del protocolo WireGuard se incluyen:
 La implementación inicial de Donenfeld, escrita en C y Go.
 BoringTun de Cloudflare, una implementación del espacio de usuario escrita en Rust.

 Programas de espacio de usuario que soportan WireGuard
Entre los programas de espacio de usuario que soportan WireGuard se incluyen:
 NetworkManager desde la versión 1.16
 systemd desde la versión 237
 Intel's ConnMan desde la versión 1.38
 La red privada de Firefox de Mozilla

 Véase también
 Secure Shell (SSH), un protocolo de red criptográfico utilizado para proteger los servicios a través de una red no segura.
 OpenVPN, un VPN de que ha ganado amplia fama por su gran uso en la industria

 Referencias

 Otras lecturas
 Whitepaper técnico de WireGuard

 Enlaces externos
