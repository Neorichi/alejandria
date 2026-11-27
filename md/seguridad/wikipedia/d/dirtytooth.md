---
type: Artículo de enciclopedia
title: DirtyTooth
description: DirtyTooth es el término genérico asignado a una característica en los perfiles BlueTooth de los dispositivos iPhone que podría ser explotada si se utiliza iOS con una versión inferior a la 11.2.
resource: https://es.wikipedia.org/wiki/DirtyTooth
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/DirtyTooth"}
license: CC BY-SA 4.0
id: eswiki-DirtyTooth
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# DirtyTooth

DirtyTooth es el término genérico asignado a una característica en los perfiles BlueTooth de los dispositivos iPhone que podría ser explotada si se utiliza iOS con una versión inferior a la 11.2. Los dispositivos con el sistema operativo Android no están afectados.

 Historia

El primer *hack* fue reportado el 5 de marzo de 2017 por Chema Alonso y fue oficialmente presentado al público durante la conferencia de seguridad RootedCon celebrada ese mismo mes en Madrid (España) y más tarde en la Toorcon en  San Diego (EE. UU.) junto a Kevin Mitnick. Un documento tipo whitepaper fue presentado en 2017 en el cual detalla una posible implementación utilizando altavoces bluetooth reales. En la conferencia de seguridad BlackHat Europe de 2017 se realizó otra demostración, esta vez utilizando una Raspberry Pi. A principios de 2018, durante el MWC 2018 en Barcelona, se realizó otra demostración en el stand de la GSMA utilizando un altavoz Bluetooth real.

 Funcionamiento
DirtyTooth se basa en la forma la cual el protocolo Bluetooth notifica al usuario cuando se realiza un cambio de perfil. Algunos sistemas operativos preguntan a dicho usuario si acepta o no el cambio de perfil, pero hay otros como iOS que no realizan esta comprobación cambiando directamente a otro. Dependiendo del perfil Bluetooth, este puede ofrecer diferentes niveles de acceso a los servicios y a la información ubicada en el dispositivo. La implementación de DirtyTooth funciona suplantando el perfil A2DP al que el usuario pretende conectar utilizando un dispositivo con iOS, cambiando a otro PBAP después de realizar una conexión, la cual se puede completar sin petición de PIN si la versión de Bluetooth es 2.1 o superior.

 Hardware afectado
Cualquier modelo de iPhone, desde el iPhone 3G hasta el iPhone X si este tiene una versión iOS por debajo de la 11.2.

 Impacto
Los datos obtenidos, si se explota este hack DirtyTooth, podrían incluir información personal y técnica sobre el usuario así como del dispositivo afectado.

 Mitigación
Actualizar el dispositivo iPhone a una versión iOS 11.2. o superior evita la explotación de este hack.

 Referencias

 Enlaces externos
 Official webpage
 Exploit Database
 DirtyTooth for Raspberry Pi
 DirtyTooth en el Mobile World Congress 2018
