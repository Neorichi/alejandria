---
type: Artículo de enciclopedia
title: Tails (sistema operativo)
description: The Amnesic Incognito Live System o Tails es una distribución Linux diseñada para preservar la privacidad y el anonimato.
resource: https://es.wikipedia.org/wiki/Tails_(sistema_operativo)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Tails_(sistema_operativo)"}
license: CC BY-SA 4.0
id: eswiki-Tails_(sistema_operativo)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Tails (sistema operativo)

- **Nombre:** The Amnesic Incognito Live System
- **Familia:** GNU/Linux
- **Autor:** The Amnesic Incognito Live System
- **Desarrollador:** The Tor Project
- **Modelo desarrollo:** Software libre
- **Última versión:** 7.16
- **Lenguaje programación:** C, C++, Python, Vala, JavaScript
- **Núcleo:** Linux
- **Núcleo tipo:** Monolítico
- **Ui:** GNOME

**The Amnesic Incognito Live System** o **Tails** es una distribución Linux diseñada para preservar la privacidad y el anonimato. Es la siguiente iteración de desarrollo de la distribución Incognito Live System. Está basada en Debian GNU/Linux, con todas las conexiones salientes forzadas a salir a través de Tor. El sistema está diseñado para ser arrancado como un Live CD o USB sin dejar ningún rastro en el almacenamiento local (por lo general, disco duro) a menos que se indique explícitamente.

 Historia

Tails fue lanzado el 23 de junio de 2009. Surgió como la nueva versión de  Incognito Live System, una distribución de Linux basada en Gentoo. Tor Project subvencionó el desarrollo de Tails además de recibir apoyo también de Debian Project, Fundación Mozilla, y de Freedom of the Press Foundation.

Laura Poitras, Glenn Greenwald, y Barton Gellman dijeron de Tails que era una herramienta indispensable en su trabajo con Edward Snowden.

El 3 de julio de 2014, el canal de la televisión pública alemana *Das Erste* reportó que el sistema de vigilancia de la NSA, XKeyscore, contenía información acerca de personas que o bien indagaron en buscadores web convencionales sobre Tails, o bien accedieron directamente a la web oficial de Tails. Un comentario en el código de XKeyscore llamaba a Tails *"Un mecanismo de COMSEC recomendado en foros extremistas"*.

El 28 de diciembre de 2014, *Der Spiegel* publicó diapositivas de una presentación secreta del NSA que databan de junio de 2012 en los cuales la NSA consideraba a Tails como *la gran amenaza* para su misión, y que cuando es usada en unión con otras herramientas como OTR, CSpace, RedPhone, y TrueCrypt era catalogado como *catastrófico,* seguido de *cerca de la pérdida total del objetivo de las comunicaciones*.

Componentes
 Redes
 Tor con: aislamiento del flujo, regular, obfs2, obfs3, obfs4, y soporte para ScrambleSuit bridges, el frontend gráfico de Vidalia.
 NetworkManager para una configuración sencilla de la red.
 Tor, un navegador web basado en Mozilla Firefox y modificado para mantener el anonimato con: Torbutton para anonimato y protección contra JavaScript, todas las cookies son tratadas como cookies de sesión por defecto; HTTPS Everywhere habilita de manera transparente las conexiones encriptadas a la SSL a un mayor número de webs, NoScript para tener aún más control sobre Javascript y AdBlock Plus para eliminar anuncios.
 Pidgin preconfigurado con OTR para Off-the-Record Messaging.
 Claws Mail un cliente de correo electrónico, con soporte de GnuPG.
 El cliente correo electrónico Icedove (Thunderbird) con Enigmail con soporte para OpenPGP.
 Liferea feed aggregator.
 Gobby para escritura colaborativa de textos.
 Aircrack-ng para redes Wi-Fi de Auditoría de seguridad de sistemas de información.
 I2P, una conexión anónima.
 Electrum, un cliente de uso fácil de bitcoin.

Cifrado y privacidad
 LUKS y GNOME Disks para instalar y usar dispositivos de almacenado encriptados, p. ej. para memoria USB.
 GnuPG, la implementación GNU de OpenPGP para correo electrónico, datos encriptados y loging anónimo.
 Monkeysign, una herramienta para OpenPGP de administración de contraseñas.
 PWGen, un potente generador aleatorio de contraseñas.
 Esquema de Shamir usando gfshare y ssss.
 Teclado virtual Florence como un countermeasure contra hardware keylogger.
 MAT para anonimizar los metadatos de los ficheros.
 KeePassX, gestor de contraseñas.
 GtkHash para calcular checksums.
 Keyringer, una herramienta de línea de comando para encriptar de manera compartida a través de Git.
 Paperkey, una herramienta de línea de comando para recuperar las claves secretas de OpenPGP en texto plano.

Véase también
 Tor
 Dark web
 Internet profunda
 Parrot Security OS
 GNU Privacy Guard
 Whonix

 Referencias

 Bibliografía

 Enlaces externos

  (en inglés)
 Tails en DistroWatch
