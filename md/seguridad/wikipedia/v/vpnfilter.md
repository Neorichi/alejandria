---
type: Artículo de enciclopedia
title: VPNFilter
description: VPNFilter es un malware diseñado para infectar diferentes routers.
resource: https://es.wikipedia.org/wiki/VPNFilter
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/VPNFilter"}
license: CC BY-SA 4.0
id: eswiki-VPNFilter
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# VPNFilter

**VPNFilter** es un malware diseñado para infectar diferentes routers. Hasta el 28 de mayo de 2018, se estima que pudo haber afectado aproximadamente entre 500,000 y 1,000,000 de routers en todo el mundo. Este malware puede robar datos personales y, además, implementa un "kill switch", un sistema diseñado para destruir remotamente el router y puede resistir un proceso de reinicio del dispositivo. Según el FBI, este malware pudo ser creado por el grupo de hackers ruso Fancy Bear.

 Modo de operación del malware

VPNFilter está programado para atacar diferentes routers, y se considera que está específicamente diseñado para infectar dispositivos de redes que usan el protocolo Modbus tanto en las comunicaciones como para control industrial de hardware - utilizado en las fábricas y almacenes.

Este malware usa las credenciales por defecto de los routers para conectar e infectar los dispositivos, sin embargo, la infección puede ser evitada usando medidas de seguridad estándar, como por ejemplo, cambiar las claves de acceso por defecto.

El proceso de infección del dispositivo ocurre en múltiples etapas:
 El malware crea un virus en el dispositivo y añade al *crontab* una lista de tareas que se ejecutarán a intervalos regulares por el planificador de tareas del cron de Linux. De este modo, el malware obtiene acceso al dispositivo y puede reiniciar la infección aunque se corrijan las etapas siguientes.
 Esta etapa representa el cuerpo de la infección, y consiste en la ejecución del código asociado a las instrucciones del crontab.
 El malware ejecuta unas instrucciones de tipo "especial", implementadas en diferentes módulos con funciones específicas, como espiar el control industrial de los dispositivos (Modbus SCADA) o utilizar la red anónima Tor para comunicarse con el servidor.

 Efectos del malware
VPNFilter espía los datos enviados a través de una red donde al menos uno de los dispositivos está infectado, almacenando información de carácter sensible, como contraseñas y nombres de usuario, e incluso datos de control que pueden ser utilizados para futuros ataques a la red.

 Mitigar los efectos del malware

Tanto Cisco como Symantec sugieren restaurar a los valores de fábrica del dispositivo si existen indicaciones de que este puede haber sido infectado. Normalmente, este proceso se consigue utilizando un objeto pequeño y puntiagudo para pulsar un botón de reinicio durante unos 10 a 30 segundos (dependiendo del modelo). Una vez reiniciado a sus valores de fábrica, las claves del dispositivo volverán a su configuración por defecto, por lo que deben ser actualizados inmediatamente para evitar nuevas infecciones.

 Dispositivos afectados

El virus inicial que instala el malware VPNFilter ataca únicamente a dispositivos que ejecutan un firmware basado en Busybox en Linux compilado para procesadores específicos, no incluyendo los ordenadores de sobremesa linux.

Los siguientes routers han sido reconocidos como potencialmente sensibles al ataque hasta la fecha:

Dispositivos Asus:
 RT-AC66U
 RT-N10
 RT-N10E
 RT-N10U
 RT-N56U
 RT-N66U

Dispositivos D-Link:
 DES-1210-08P
 DIR-300
 DIR-300A
 DSR-250N
 DSR-500N
 DSR-1000
 DSR-1000N

Dispositivos Huawei:
 HG8245

DIspositivos Linksys:
 E1200
 E2500
 E3000
 E3200
 E4200
 RV082
 WRVS4400N

Dispositivos Mikrotik:
 CCR1009
 CCR1016
 CCR1036
 CCR1072
 CRS109
 CRS112
 CRS125
 RB411
 RB450
 RB750
 RB911
 RB921
 RB941
 RB951
 RB952
 RB960
 RB962
 RB1100
 RB1200
 RB2011
 RB3011
 RB Groove
 RB Omnitik
 STX5
 Routers Mikrotiken sus versiones hasta 6.38.5

Dispositivos Netgear:
 DG834
 DGN1000
 DGN2200
 DGN3500
 FVS318N
 MBRN3000
 R6400
 R7000
 R8000
 WNR1000
 WNR2000
 WNR2200
 WNR4000
 WNDR3700
 WNDR4000
 WNDR4300
 WNDR4300-TN
 UTM50

Dispositivos QNAP:
 TS251
 TS439 Pro
 Otros dispositivos QNAP NAS que utilicen el software QTS

Dispositivos TP-Link:
 R600VPN
 TL-WR741ND
 TL-WR841N

Dispositivos Ubiquiti:
 NSM2
 PBE M5

Dispositivos Upvel:
 Desconocido

Dispositivos ZTE:
 ZXHN H108N

 Epidemiología
Según Cisco Talos, el malware VPNFilter podría haber infectado hasta 500,000 dispositivos en el mundo, en 54 países diferentes, aunque se estima que la mayoría de ataques se habrían concentrado en Ucrania.

 Investigación del FBI
El FBI destinó múltiples recursos a una investigación que culminó con el cierre del dominio *toknowall.com*, el cual se considera que podía haber sido utilizado para redirigir distintas peticiones de la etapa 1 del malware, permitiendo al virus recuperar el código necesario para proceder a las etapas 2 y 3.

 Alentar a la reinfección
El 25 de mayo de 2018, el FBI sugirió que bastaría con que los usuarios reiniciaran el dispositivo, de manera que las etapas 2 y 3 se eliminarían del dispositivo, aunque dejando la etapa 1 activa. De este modo, los dispositivos infectados necesitarían conectar al dominio requisado para infectar de nuevo al dispositivo, lo que ayudaría al FBI a descubrir los dispositivos infectados.

 Referencias

 Referencias
