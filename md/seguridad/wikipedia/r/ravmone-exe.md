---
type: Artículo de enciclopedia
title: RavMonE.exe
description: "RavMonE, conocido más correctamente como \"RJump\", es un troyano informático que abre una puerta trasera en los equipos que ejecutan Microsoft Windows."
resource: https://es.wikipedia.org/wiki/RavMonE.exe
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/RavMonE.exe"}
license: CC BY-SA 4.0
id: eswiki-RavMonE.exe
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# RavMonE.exe

**RavMonE**, conocido más correctamente como "**RJump**", es un troyano informático que abre una puerta trasera en los equipos que ejecutan Microsoft Windows. Una vez que el ordenador está infectado, el virus permite a los usuarios no autorizados de acceder a los contenidos de la computadora. Esto plantea un riesgo de seguridad para el usuario de la máquina infectada, ya que el atacante puede robar información personal y utilizar la computadora como un punto de acceso en una red interna.

RavMonE se hizo famoso el 12 de septiembre de 2006, cuando una serie de vídeos del iPod se enviaba con el virus ya instalado. Debido a que el virus sólo infecta ordenadores con Windows, se puede inferir que el fabricante contratado de Apple no hizo uso de computadoras Macintosh. Apple llegó objeto de algunas críticas públicas por la liberación de los virus con su producto.

 Descripción

RavMonE es un gusano informático escrito en el lenguaje de script Python y se convierte en un archivo ejecutable de Windows con la herramienta Py2Exe. Intenta propagarse copiándose a unidades de almacenamiento mapeadas y extraíbles. Se puede transmitir por abrir archivos adjuntos de correo electrónico infectados y descarga de archivos infectados de Internet. También se puede propagar a través de los medios extraíbles, como CD-ROM, memoria flash, cámaras digitales y reproductores multimedia.

La mayoría de los programas antivirus identifican RavMonE.exe como malware, por ejemplo Kapersky lo identifica como un Worm.Win32.RJump.a,  y TrendMicro lo identifica como un WORM_RJUMP.A.

 Acción

Una vez que el virus se ejecuta, realiza las siguientes tareas:

 Se copia a sí mismo en %WINDIR% como RavMon.exe o, RavMonE.exe o, AdobeR.exe,
 Se agrega el valor "RavAV" = "%WINDIR%\RavMonE.exe" en el registro de Windows como HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run,
 Abre un puerto aleatorio y acepta comandos de direcciones remotas,
 Se crea un archivo de registro RavMonLog para almacenar el número de puerto,
 Publica una solicitud HTTP para asesorar al atacante sobre la dirección IP del equipo infectado y el número del puerto abierto.

Cuando un dispositivo de almacenamiento extraíble está conectado al ordenador infectado copia los siguientes archivos en el dispositivo:

 autorun.inf: una secuencia de comandos para ejecutar el gusano la próxima vez que el dispositivo está conectado a un ordenador,
 msvcr71.dll: un módulo Microsoft C Runtime Library que contiene las funciones estándar tales como copiar en la memoria e imprimir en su consola,
 ravmon.exe: una copia del gusano.

 Alias de los diferentes antivirus

 Backdoor.Rajump (Symantec)
 W32/Jisx.A.worm (Panda Security)
 W32/RJump-C (Sophos)
 W32/RJump.A!worm (Fortinet)
 Win32/RJump.A (ESET NOD32 Antivirus y ESET Smart Security)
 Win32/RJump.A!Worm (CA)
 Worm.RJump.A (BitDefender)
 Worm.Win32.RJump.a (Kaspersky Lab)
 Worm/Rjump.E (Avira)
 WORM_SIWEOL.B (TrendMicro)
 Worm/Generic.AMR (AVG)
 INF:RJump[Trj](Avast!)

 Referencias

 Enlaces externos
 RJump.A: *Vs Antivirus*. Propagación y métodos de limpieza.
