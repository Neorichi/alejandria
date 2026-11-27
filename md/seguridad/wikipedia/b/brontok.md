---
type: Artículo de enciclopedia
title: Brontok
description: "El gusano Brontok es un virus informático con características de ataque, gusano y troyano que afecta ordenadores con Windows y puede ser considerado como una amenaza informática grave si no se dispone de protección …"
resource: https://es.wikipedia.org/wiki/Brontok
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Brontok"}
license: CC BY-SA 4.0
id: eswiki-Brontok
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Brontok

El **gusano Brontok** es un virus informático con características de ataque, gusano y troyano que afecta ordenadores con Windows y puede ser considerado como una amenaza informática grave si no se dispone de protección antivirus.

Este virus informático dispone de una gran variedad de alias:
Brontok.CV, BackDoor.Generic.1138, Email-Worm.Win32.Brontok.q, Generic.Brontok.26CDB61D, I-Worm.Brontok.c, I-Worm/VB.IM, W32.Brontok.Q, W32/Brontok.C@mm, W32/Brontok.CM@mm, W32/Brontok.H.worm, W32/Rontokbro.gen@MM, W32/Rontokbro@MM, W32/Suspicious_M.gen, Win32/Brontok.AS@mm, Win32/Brontok.CV, Win32/Robknot!generic, Win32/Robknot.Variant!Worm, Win32:Brontok-I, Worm.Brontok.c, Worm.Brontok.E, Worm/Brontok.C

El malware disponía de una imagen que cada vez que el sistema arrancaba se mostraba. La imagen tiene el mismo texto sin sentido que el que  se incluía en el correo.
El virus fue creado en Indonesia en 2005 y se cree que el impacto no fue muy grave.

Brontok puede eliminarse con el último software antivirus actualizado, aunque hay varias formas independientes disponibles por los proveedores de antivirus.

El virus fue creado por JowoBot y afecta principalmente a Windows XP

 Efectos
 Cuando el virus Brontok se ejecuta por primera vez, se copia a sí mismo en la carpeta de Datos de Programa de los usuarios. Luego se programa a sí mismo en el arranque de Windows, creando una entrada de registro en la clave: HKLM\Software\Microsoft\Windows\CurrentVersion\Run.
 Se extiende enviándose a sí mismo a direcciones de correo obtenidas del ordenador afectado.
 El virus desactiva:
el editor del registro (regedit.exe).
el Administrador de Tareas.  +  +
el Firewall de Windows.
 Modifica la configuración del explorador de archivos, ocultando el menú *Herramientas / Opciones de carpeta* de modo que los archivos 'ocultos' y 'de sistema' no sean accesibles por el usuario.
 Las direcciones tecleadas en el explorador de Windows son borradas antes de completarse.
 Usando su propio motor de correo se envía a sí mismo hacia las direcciones que encuentra en la computadora infectada, falsificando a veces la misma dirección de correo del usuario como remitente.
 En muchas variantes del virus, la computadora **reinicia cuando**:
se intenta abrir una ventana de Línea de Comandos.
se trata de acceder a recursos de habituales de administradores de sistema o de programadores.
una ventana contiene en su título ciertas cadenas de caracteres: 'Resource hacker', 'Datos de programa', 'Symantec', 'Norton', 'Panda', 'Microsoft', etc.
 Impide al usuario descargar archivos.
 Abre ventanas en el navegador predeterminado y carga páginas Web localizadas en la carpeta "Mis Documentos" y/o sub-carpetas.
 Crea archivos .exe en carpetas y unidades llamados como la misma carpeta y usando un icono característico del explorador de carpetas de Windows.
 Lleva a cabo un ataque ping flood a dos sitios web, del gobierno de Israel y de la revista Playboy.
