---
type: Artículo de enciclopedia
title: GNU Privacy Guard
description: "GNU Privacy Guard (GnuPG o GPG) es una herramienta de cifrado y firmas digitales desarrollado por Werner Koch, que viene a ser un reemplazo del PGP (Pretty Good Privacy) pero con la principal diferencia que es software …"
resource: https://es.wikipedia.org/wiki/GNU_Privacy_Guard
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/GNU_Privacy_Guard"}
license: CC BY-SA 4.0
id: eswiki-GNU_Privacy_Guard
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# GNU Privacy Guard

- **Nombre:** GNU Privacy Guard (GPG)
- **Desarrollador:** GNU Project
- **Última versión:** 2.5.24
- **Sistema operativo:** Multiplataforma
- **Género:** Pretty Good Privacy
- **Licencia:** GNU General Public License

**GNU Privacy Guard** (**GnuPG** o **GPG**) es una herramienta de cifrado y firmas digitales desarrollado por Werner Koch, que viene a ser un reemplazo del PGP (*Pretty Good Privacy*) pero con la principal diferencia que es software libre licenciado bajo la GPL. GPG cumple el estándar RFC 4880 del IETF denominado OpenPGP.

GnuPG es parte del Proyecto GNU y recibió fondos del Gobierno alemán en 1999.

 Usos
GPG es estable, calificado como un software para el uso en producción y es comúnmente incluido en los sistemas operativos como FreeBSD, OpenBSD, NetBSD y GNU/Linux.

Aunque básicamente el programa tiene una interfaz textual, actualmente hay varias aplicaciones gráficas que utilizan recursos de GPG. Por ejemplo, ha sido integrado dentro de Kmail y Evolution, también hay un plugin llamado Enigmail que se integra con Firefox y Thunderbird que trabajan en Windows, GNU/Linux y otros sistemas operativos.

GPG también puede ser compilado en otras plataformas como Mac OS X y Windows. En Mac OS X hay portada una aplicación libre llamada MacGPG, que ha sido adaptada para usar el ambiente del usuario y sus definiciones de clases nativas.

 Funcionamiento
GPG cifra los mensajes usando pares de claves individuales asimétricas generadas por los usuarios. Las claves públicas pueden ser compartidas con otros usuarios de muchas maneras, un ejemplo de ello es depositándolas en los servidores de claves. Siempre deben ser compartidas cuidadosamente para prevenir falsas identidades por la corrupción de las claves públicas. También es posible añadir una firma digital criptográfica a un mensaje, de esta manera la totalidad del mensaje y el remitente pueden ser verificados en caso de que se desconfíe de una correspondencia en particular.

GnuPG también soporta algoritmos de cifrado simétricos, por ejemplo CASTS.

GPG no usa algoritmos de software que están restringidos por patentes. En su lugar, usa una serie de algoritmos no patentados como ElGamal, CAST5, Triple DES (3DES), AES y Blowfish.

GPG es un software de cifrado híbrido que usa una combinación convencional de criptografía de claves simétricas para la rapidez y criptografía de claves públicas para el fácil compartimiento de claves seguras, típicamente usando recipientes de claves públicas para cifrar una clave de sesión que es usada una vez. Este modo de operación es parte del estándar OpenPGP y ha sido parte del PGP desde su primera versión.

 Problemas
El estándar OpenPGP especifica varios métodos de mensajes con firmas digitales. Debido a un error al intentar mejorar la eficiencia de uno de los métodos, se introdujo una vulnerabilidad de seguridad (Nguyen 2004) que afectó a un único método de mensajes firmado digitalmente utilizado en algunas versiones de GPG (desde la 1.0.2 hasta la 1.2.3, con menos de 1000 claves listadas en los servidores de claves). Dicha vulnerabilidad ha sido corregida a partir de la versión 1.2.4 de GPG. El episodio ilustra la dificultad de realizar implementaciones correctas de algoritmos criptográficos, protocolos e incluso criptosistemas.

GPG es un sistema en línea de comandos. Diferentes implementaciones gráficas están disponibles, pero solo algunas tienen implementadas todas sus características (por ejemplo: borrado de ID, usuarios o firmas). Debido a que todas las instrucciones deben ser pasadas a la línea de comandos, rápidamente llegan a dificultar el uso correcto de aspectos no triviales del programa. El trabajo sobre una versión de  biblioteca está en progreso.

 Véase también

 Gpg4win

 Referencias

 Enlaces externos
 Sitio web oficial de GNU Privacy Guard
 Gpg4win. GnuPG para Windows
 FireGPG. Extensión para Firefox con soporte para Gmail
