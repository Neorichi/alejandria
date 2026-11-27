---
type: Artículo de enciclopedia
title: Mimikatz
description: Mimikatz es, al mismo tiempo, un programa que lleva a cabo una vulnerabilidad en Microsoft Windows y una debilidad de este sistema operativo que permite extraer contraseñas guardadas en la memoria del ordenador.
resource: https://es.wikipedia.org/wiki/Mimikatz
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Mimikatz"}
license: CC BY-SA 4.0
id: eswiki-Mimikatz
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Mimikatz

**Mimikatz** es, al mismo tiempo, un programa que lleva a cabo una vulnerabilidad en Microsoft Windows y una debilidad de este sistema operativo que permite extraer contraseñas guardadas en la memoria del ordenador. Es una expresión coloquial en francés que quiere decir "gatos lindos", y fue creada por el programador de nacionalidad francesa Benjamin Delpy.

 Historia
Benjamin Delpy encontró una vulnerabilidad en Microsoft Windows que guarda al mismo tiempo, en la memoria, una réplica cifrada de una contraseña junto con la clave para descifrarla. En 2011, se comunicó con Microsoft para reportar la vulnerabilidad; sin embargo, Microsoft contestó que el equipo tenía que estar comprometido previamente. Delpy se dio cuenta de que la vulnerabilidad podía emplearse para acceder a dispositivos no comprometidos de una red desde uno que sí lo estaba.

Lanzó la primera versión del software en mayo de 2011 como software de código cerrado .

En septiembre de 2011, la vulnerabilidad se utilizó en el ataque a DigiNotar .

 Conferencia rusa
En una conferencia en 2012, Delpy se refirió al software. Una vez, durante la conferencia, volvió a su habitación y vio que un extraño estaba sentado frente a su portátil. El extraño se disculpó, alegando que había confundido la habitación y se fue. Durante la conferencia, otro hombre se le acercó y le pidió que le diera en una memoria USB copias de su presentación y del software. Las copias fueron entregadas por Delpy.

Delpy quedó impresionado por sus experiencias y, antes de irse de Rusia, subió el código fuente a GitHub. Creía que los que se defendían de los ciberataques tenían que aprender sobre el código para poderse proteger contra estos.

 Actualizaciones de Windows
En el año 2013, Microsoft incorporó a Windows 8.1 una opción que habilitaba la desactivación de la función susceptible de ser aprovechada.   Esta función, en Windows 10, está desactivada de manera predeterminada. Sin embargo, Jake Williams, de Rendition Infosec, sostiene que sigue siendo efectiva debido a dos razones: porque el sistema tiene una versión anterior de Windows o porque es capaz de utilizar la elevación de privilegios para adquirir el control necesario sobre el objetivo y activar la función vulnerable.

Benjamin Delpy ha actualizado el software para abordar vulnerabilidades más allá de las que tenía el original..

 Uso en malware
El ataque Carbanak y el ciberataque al Bundestag utilizaron esta vulnerabilidad. El malware NotPetya y BadRabbit utilizaron versiones de este ataque combinadas con las vulnerabilidades EternalBlue y EternalRomance.

 En la cultura popular
En el episodio 9 de la segunda temporada de **Mr. Robot**, Angela Moss utiliza Mimikatz para obtener la contraseña del dominio de Windows de su jefe.

 Referencias

 Enlaces externos

 Implementación por Benjamin Delpy en github
 Implementación del exploit en GitHub
