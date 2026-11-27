---
type: Artículo de enciclopedia
title: BlackEnergy
description: BlackEnergy es un malware de propósito múltiple que ha sido utilizado desde 2007 en ataques de tipo denegación de servicio y amenaza persistente avanzada.
resource: https://es.wikipedia.org/wiki/BlackEnergy
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/BlackEnergy"}
license: CC BY-SA 4.0
id: eswiki-BlackEnergy
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# BlackEnergy

**BlackEnergy** es un *malware* de propósito múltiple que ha sido utilizado desde 2007 en ataques de tipo denegación de servicio y amenaza persistente avanzada. Se ha detectado que este software tiene capacidad de extensión para incluir ataques a plataformas ARM y MIPS, dispositivos de redes Cisco, robo de certificados, puertas de entrada SSH, el componente KillDisk para destrucción de archivos, escritorio remoto, etc. Se ha comprobado también el uso de BlackEnergy como *ransomware* en incidentes de secuestro de datos.

Durante 2015, BlackEnergy junto con KillDisk fueron utilizados en Ucrania contra medios de comunicación durante las elecciones locales y contra empresas de sector eléctrico a finales de año. Una vez instalado, el *malware* verifica que el equipo afectado realmente pertenezca al objetivo al que se quiere atacar e instala una puerta trasera SSH de manera que el atacante pueda tomar control efectivo del equipo afectado. El comportamiento de BlackEnergy en un ataque particular se configura mediante un archivo XML incluido dentro del ejecutable del software.
Apagón del 23 de diciembre de 2015 en Ucrania
Una investigación sobre el apagón del 23 de diciembre de 2015 en Ucrania muestra que el uso de BlackEnergy fue elemento crucial en el sabotaje coordinado a diferentes empresas de servicio eléctrico de Ucrania al dar acceso a los atacantes. Una vez adquirido el acceso, los atacantes procedieron a cortar la electricidad, lanzaron un ataque de denegación de servicio para impedir que llegaran los reportes de los usuarios e intentaron dañar la configuración de los sistemas SCADA de manera de entorpecer la reactivación del sistema eléctrico. Este apagón es el primero en el mundo que ha sido documentado como producido con el uso de un *malware*.

KillDisk
Desde 2014, se ha detectado el uso del componente KillDisk para destrucción de archivos cambiando su contenido por datos aleatorios e intentando dejar el equipo en un estado en el que no pueda reiniciarse. En los ataques documentados, se ha encontrado una lista de tipos de archivo a destruir específica a cada sector de actividad.
Puerta trasera SSH
Una de las extensiones de BlackEnergy usadas en el ataque a las empresas del sector eléctrico fue un servidor SSH, preparado para autentificar usuarios y claves específicas predefinidas, y configurado para atender conexiones en un puerto inusual, el cual permite a los atacantes conectarse libremente al equipo afectado.

Referencias
