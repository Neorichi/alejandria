---
type: Artículo de enciclopedia
title: EternalBlue
description: EternalBlue es un exploit desarrollado por la NSA.
resource: https://es.wikipedia.org/wiki/EternalBlue
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/EternalBlue"}
license: CC BY-SA 4.0
id: eswiki-EternalBlue
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# EternalBlue

- **Nombre:** EternalBlue
- **Desarrollador:** Equation Group
- **Software afectado:** Microsoft Windows

**EternalBlue** es un exploit desarrollado por la NSA. Fue filtrado por el grupo de hackers The Shadow Brokers el 14 de abril de 2017, y fue utilizado en el ataque mundial de ransomware con WannaCry del 12 de mayo de 2017.

Detalles
EternalBlue aprovecha una vulnerabilidad en la implementación del protocolo Server Message Block (SMB) de Microsoft. Esta vulnerabilidad, denotada como CVE-2017-0144 en el catálogo Common Vulnerabilities and Exposures (CVE), se debe a que la versión 1 del servidor SMB (SMBv1) acepta en varias versiones de Microsoft Windows paquetes específicos de atacantes remotos, permitiéndoles ejecutar código en el ordenador en cuestión.

La actualización de seguridad de Windows del 14 de marzo de 2017 resolvió el problema a través del parche de seguridad MS17-010, para todas las versiones de Windows que en ese momento eran mantenidas por la compañía: Windows Vista, Windows 7, Windows 8.1, Windows 10, Windows Server 2008, Windows Server 2012, y Windows Server 2016. Las versiones antiguas, como Windows XP, Windows 8, o Windows Server 2003, no han recibido dicho parche. (La extensión del periodo de mantenimiento para Windows XP había acabado hacía tres años, el 8 de abril de 2014, y el de Windows Server el 14 de julio de 2015). Microsoft recientemente liberó el parche para Windows XP y Server 2003.

Por diversos motivos, muchos usuarios de Windows no habían instalado MS17-010 cuando, dos meses más tarde, el 12 de mayo de 2017, se produjo el ataque WannaCry que empleaba la vulnerabilidad **EternalBlue**. El 13 de mayo de 2017, un día después del ataque, Microsoft aportó la actualización de seguridad para Windows XP, Windows 8, y Windows Server 2003, disponible para descarga en el Microsoft Update Catalog.

 Responsabilidad
Según Microsoft, fue la NSA de los Estados Unidos la responsable debido a su controvertida estrategia de no revelar sino de almacenar las vulnerabilidades. La estrategia impidió que Microsoft conociera (y posteriormente parcheara) este fallo, y presumiblemente otros fallos ocultos.

 Eternalrocks
EternalRocks o MicroBotMassiveNet es un gusano de computadora que infecta a Microsoft Windows. Utiliza siete exploits desarrollados por la NSA. Comparativamente, el programa de rescate WannaCry que infectó 230.000 ordenadores en mayo de 2017 solo utiliza dos exploits de la NSA, haciendo que los investigadores crean que EternalRocks es significativamente más peligroso. El gusano fue descubierto a través de un honeypot.

EternalBlue fue una de las varias hazañas utilizadas, junto con la herramienta de implante de puerta trasera DoublePulsar.

 Infección
EternalRocks instala primero Tor, una red privada que oculta la actividad de Internet, para acceder a sus servidores ocultos. Después de un breve "período de incubación" de 24 horas, el servidor responde a la solicitud de malware descargándolo y auto-replicándose en la máquina "host".

El malware incluso se denomina a sí mismo WannaCry para evitar ser detectado por los investigadores de seguridad. A diferencia de WannaCry, EternalRocks no posee un interruptor de apagado y no es un software de rescate.

Referencias
