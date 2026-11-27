---
type: Artículo de enciclopedia
title: Motaba
description: El Motaba es un gusano informático, fue liberado en la red a mediados de julio del año 2006.
resource: https://es.wikipedia.org/wiki/Motaba
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Motaba"}
license: CC BY-SA 4.0
id: eswiki-Motaba
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Motaba

El **Motaba** es un gusano informático, fue liberado en la red a mediados de julio del año 2006. También fue el nombre del virus causante de la enfermedad protagonista de la película "Epidemia".

Fue programado en Visual Basic, y se propaga a través del cliente de mensajería instantánea MSN Messenger, enviando una dirección a los contactos conectados antepuesta por una frase que dice "jaja mira esta foto" y al hacer click se cierra la ventana automáticamente y se produce la infección.

 Datos
Nombre: W32/Motaba.A
Tipo: Gusano informático
Alias: Motaba
Plataforma: Windows 32-bit
Tamaño: 81 kb.

 Infección

Crea tres archivos en la carpeta System32, ambos con el mismo peso, ya que es una copia del mismo virus:
motaba.exe
spof.exe
motaba.hta

EL virus reconoce el sistema operativo Windows en donde se trabaja, reconociendo las diferencias en el árbol de archivos, como por ejemplo "*winnt*" es el nombre de la carpeta que contiene a "*system32*" en Windows NT, mientras que esta está contenida en la carpeta "windows" en otras versiones del sistema operativo. El gusano las detecta y se copia en la correspondiente a cada sistema.

El gusano crea las siguientes entradas en el registro para autoejecutarse en cada reinicio del sistema:

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run [variable] = [archivo del sistema] [archivo malicioso]

Donde [variable] puede tener cualquier nombre, y [archivo del sistema] es un archivo legítimo de Windows que ejecuta al [archivo malicioso], que es el archivo del gusano. Luego envía mensajes infectados a los contactos del MSN, para continuar con su propagación.
