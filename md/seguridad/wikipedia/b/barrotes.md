---
type: Artículo de enciclopedia
title: Barrotes
description: Barrotes es un virus informático, considerado como el primero de origen español, apareció en diciembre de 1992, programado en lenguaje ensamblador para sistemas basados en DOS.
resource: https://es.wikipedia.org/wiki/Barrotes
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Barrotes"}
license: CC BY-SA 4.0
id: eswiki-Barrotes
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Barrotes

- **Nombre:** Barrotes
- **Género:** Virus informático
- **Desarrollador:** OSoft (Pseudónimo)
- **Lanzamiento:** 1992
- **Descubrimiento:** Diciembre de 1992
- **Estado:** Discontinuado, obsoleto
- **Lenguaje programación:** Lenguaje ensamblador
- **Plataforma:** DOS

**Barrotes** es un virus informático, considerado como el primero de origen español, apareció en diciembre de 1992, programado en lenguaje ensamblador para sistemas basados en DOS. Inicialmente, aunque en menor medida, también fue denominado **Toledo** por la prensa, debido a la localización en la ciudad homónima de su primer descubrimiento, y registrado como **Virus:DOS/Barrotes** por Microsoft.

Como muchos virus de la época, se queda latente en la máquina afectada, en espera de detectar una fecha concreta para ejecutar su código malicioso, también llamado payload, siendo el 5 de enero la fecha escogida por su desarrollador, una fecha muy señalada en España, ya que es la noche de reyes, pasando a mostrar el mensaje *«Virus BARROTES por OSoft»* y los gráficos en pantalla de los característicos barrotes que le dan nombre y que hacen parecer que el sistema se encuentra en la celda de una prisión.

 Características
El virus ocupa un total de 1310 bytes de tamaño e infecta archivos ejecutables COM y EXE.Cuando se ejecuta un fichero infectado en el sistema, el código malicioso del virus es lo primero en ejecutarse, pasando a comprobar si ya se encuentra residente en memoria, detectando así si ya se ha ejecutado con anterioridad, obviando el proceso de infección del archivo ejecutado, en caso contrario procede a instalarse en memoria registrando el vector de interrupción correspondiente a los servicios de DOS (int 21) en la cabecera del virus, gracias a lo cual el virus irá infectando archivos en el sistema conforme el usuario los vaya ejecutando.

Posteriormente, comprobará si la fecha es 5 de enero, para mostrar el mensaje del autor y los barrotes, en caso contrario, ejecuta el sistema con normalidad, pasando desapercibido.

 Método de propagación

Barrotes no posee ningún método automático de propagación, más allá de infectar archivos locales en la máquina afectada por el virus. Su método de difusión mayoritaria, dado el contexto de su época de actuación —los años 90— era el intercambio de archivos infectados a través de medios de almacenamiento físicos, como el disquete.

 Variantes
Posteriormente, aparecieron nuevas versiones y variantes del virus con efectos maliciosos más pronunciados, como la variante **Barrotes 1303** en 1996**,** que destruía el sector de arranque del disco duro, impidiendo arrancar el sistema y acceder a la información almacenada en él, cambiando la fecha de activación por el 23 de septiembre.Muchos sistemas informáticos se vieron expuestos a estos efectos.

 Véase también

 (c)Brain
 Stoned (virus informático)
 Michelangelo (virus informático)

 Referencias

 Bibliografía
 «Pc Manía», *HOBBY PRESS, S.A.*, número 28, 1995 Internet Archive
 «OK PC», *Editorial Nueva Prensa, S.A.*, número 17, 1993 Internet Archive
 «Virus Bulletin - The International Publication On Computer Virus Prevention, Recognition And Removal», *Network Security Management, UK* (en inglés), ISSN 0956-9979, 1994 Internet Archive

 Enlaces externos
 Virus.DOS.Barrotes (*YouTube*)
