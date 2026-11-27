---
type: Artículo de enciclopedia
title: Virus CIH
description: El virus CIH, también conocido como virus Chernobyl, es un virus informático que ataca los sistemas Windows 9x, surgido en 1998.
resource: https://es.wikipedia.org/wiki/Virus_CIH
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Virus_CIH"}
license: CC BY-SA 4.0
id: eswiki-Virus_CIH
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Virus CIH

- **Nombre:** Virus CIHChernobyl
- **Desarrollador:** Cheng-Ing Hau
- **Género:** Virus informático
- **Estado:** Inactivo
- **Idiomas:** Inglés y taiwanés
- **Lanzamiento:** 1998
- **Sistema operativo:** Windows 9x

El **virus CIH**, también conocido como **virus Chernobyl**, es un virus informático que ataca los sistemas Windows 9x, surgido en 1998.

El nombre original del virus (**CIH**) es un acrónimo con las iniciales de su creador, Chen Ing Hau (陳盈豪, pinyin: *Chén Yíngháo*), a la razón estudiante en la Universidad Tatung de Taipéi (Taiwán). El sobrenombre posterior de **"virus Chernobyl"** se debió a que la fecha de activación del virus (26 de abril) coincidía casualmente con el aniversario del accidente de Chernóbil, ocurrido en la URSS el 26 de abril de 1986. En realidad, la fecha elegida se debía al cumpleaños del autor del virus.

En su momento fue considerado uno de los virus más peligrosos y destructivos, capaz de eliminar información crítica del usuario e incluso sobrescribir el sistema BIOS, impidiendo el arranque del equipo. Se calcula que el virus logró infectar unos 60 millones de ordenadores en todo el mundo, ocasionando pérdidas por valor de 1000 millones de dólares, aunque otras fuentes rebajan dicha cuantía a una cuarta parte.

Chen dijo que su objetivo de crear el virus era básicamente dejar en ridículo a ciertas compañías de software que presumían de la eficacia de sus programas antivirus. El joven programador declaró en su descargo que, cuando algunos de sus compañeros propagaron el virus fuera de su Universidad, él mismo publicó un antivirus disponible gratuitamente, desarrollado con la ayuda de otro estudiante, Weng Shi-hao (翁世豪). Por aquel entonces, los fiscales taiwaneses no pudieron imputar a Chen ningún delito, debido a que las víctimas no presentaron cargos contra él. Estos hechos propiciaron que más adelante se aprobase una nueva legislación sobre delitos informáticos en Taiwán. Por su parte, Chen trabajó para la compañía taiwanesa Gigabyte como programador sénior hasta que fundó su propia empresa, llamada CIH.

Historia
En septiembre de 1998, Yamaha lanzó una actualización de firmware para sus dispositivos CD-R400 que se hallaba infectada por el virus. Un mes más tarde, una versión demo del juego SiN de Activision, extendió el contagio a causa de una copia infectada. En 1999, varios miles de equipos a la venta de IBM salieron al mercado portando el virus CIH, justo un mes antes de que este se activase.

Al activarse, el virus CIH actuaba rellenando los primeros 1024 KB del dispositivo de arranque con una secuencia de ceros, y a continuación atacaba la BIOS. En la práctica estas acciones dejaban el computador inutilizable y para la mayoría de los usuarios no avanzados el virus "destruía" el PC. Técnicamente, sin embargo, bastaba con reemplazar el chip del BIOS; posteriormente, también se idearon algunos métodos para recuperar los datos del disco duro.

Aún hoy, CIH puede encontrarse de manera residual en algunos equipos antiguos con Windows 95/98/ME instalado.

Este virus tuvo una breve reaparición en 2001, cuando una variante del virus *ILoveYou*, que portaba un fichero VBS con una rutina del CIH, estuvo circulando por Internet bajo el reclamo de un desnudo de Jennifer Lopez. Por último, en diciembre de 2002 se detectó una versión modificada del virus llamada CIH.1106, considerada mucho menos dañina que la original.

Detalles
Método de propagación
CIH tenía su caldo de cultivo en sistemas Windows 95, 98 y ME sistemas basados en MS-DOS. Propagándose a través de ficheros ejecutables de formato PE (*Portable Executable*). A partir de la siguiente generación de sistemas Windows, basados en arquitectura NT, el virus dejó de propagarse, y a día de hoy se considera prácticamente erradicado.

CIH no empleaba ninguna técnica concreta para difundirse, aprovechando los cauces habituales usados por otros virus de la época: mensajes de correo electrónico, transferencias de ficheros por FTP, CD-ROM, disquetes, etc. Después, había que esperar a que el archivo infectado se ejecutase en el sistema, tras lo cual el virus quedaba residente en memoria, permaneciendo allí a la espera de infectar más programas y archivos. Asimismo, CIH ponía en práctica técnicas avanzadas para elevar sus privilegios de ejecución, saltando desde el nivel destinado a las aplicaciones de usuario (*anillo* 3) hasta el nivel asignado al núcleo del sistema operativo (*anillo* 0). Esto le permitía interceptar las llamadas al sistema y burlar la detección del software antivirus.

Método de infección
El virus CIH infectaba archivos ejecutables de Windows con formato PE (*.EXE). Cuando se abría cualquier archivo de extensión EXE, el virus instalado en memoria comprobaba si este disponía de huecos suficientes; en caso afirmativo lo infectaba, e inmediatamente verificaba la fecha del día para decidir si era tiempo de activarse.

Tras la infección, los archivos presentaban el mismo tamaño que al principio, debido al sofisticado método de infección puesto en práctica. El virus lograba "inyectar" código malicioso en el ejecutable, sin aumentar su tamaño (lo que dificultaba la detección), aprovechando los huecos internos de la estructura del archivo. CIH troceaba su propio código (apenas 1KB) para ajustarse a los huecos disponibles. De esta forma lograba inocularse en nuevos archivos ejecutables. Por esta peculiaridad, recibió el apelativo de ***«spacefiller»*** ("tapahuecos") en la jerga técnica.

Efectos
El 26 de abril, fecha de activación en casi todas las variantes del virus CIH, este iniciaba el ataque usando dos tácticas diferentes.

La primera consistía en sobrescribir la tabla de particiones del disco duro (MBR) con datos aleatorios, comenzando por el sector 0, hasta provocar el colapso del sistema. Esta sobrescritura impedía que el ordenador pudiese arrancar y hacía casi imposible recuperar los datos. Tras esto, cuando el usuario trataba de reiniciar el equipo, nada se mostraba en la pantalla excepto el mensaje de error: "DISK BOOT FAILURE", lo que indicaba que el virus había formateado el disco.

La segunda ocasionaba graves daños en computadoras con microprocesador Pentium y placa compatible con el chipset . Este ataque consistía en grabar información basura en la memoria flash del sistema BIOS, dejándolo inservible.Lo que causa que el hardware quede inservible.

Todas las variantes del virus CIH presentan un *modus operandi* similar: borran los primeros 2048 sectores del disco duro (alrededor de 1MB) y además, si el sistema no está protegido, intentan sobrescribir la memoria del BIOS, dejando inutilizable el computador hasta el recambio del chip del BIOS o de la placa base en su totalidad.

Variantes del virus
CIH v1.2/CIH.1103
Esta versión es la más común. Se activaba el 26 de abril.
Contiene la frase: CIH v1.2 TTIT
CIH v1.3/CIH.1010A y CIH1010.B
Esta versión también se activaba el 26 de abril.
Contiene la frase: CIH v1.3 TTIT
CIH v1.4/CIH.1019
Esta versión se activaba el día 26 de cualquier mes. Aún puede encontrarse en ciertos sistemas antiguos, aunque es poco frecuente.
Contiene la frase: CIH v1.4 TATUNG.
CIH.1049
Esta versión se activaba el 2 de agosto, en lugar del 26 de abril.
CIH.1106
Esta versión se activaba el día 2 de cualquier mes.

Referencias

Enlaces externos
 CIH Official Site (en inglés)
 CIH at linkedin (en inglés)
 F-Secure CIH Technical Page (en inglés)
 Symantec CIH Technical Page (en inglés)
 News article about the Jennifer Lopez e-mail (en inglés)
 FIX-CIH - Site by Steve Gibson on how to repair most of the damage from CIH (en inglés)
