---
type: Artículo de enciclopedia
title: Subdesbordamiento de búfer
description: "En informática un subdesbordamiento de búfer (Buffer underflow/underrun) es un problema aritmético, el cual sucede cuando un búfer carga su información (flujo de datos) a una velocidad más baja que el procesamiento de …"
resource: https://es.wikipedia.org/wiki/Subdesbordamiento_de_búfer
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Subdesbordamiento_de_búfer"}
license: CC BY-SA 4.0
id: eswiki-Subdesbordamiento_de_búfer
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Subdesbordamiento de búfer

En **informática** un **subdesbordamiento de búfer** (Buffer underflow/underrun) es un problema aritmético, el cual sucede cuando un búfer carga su información (flujo de datos) a una velocidad más baja que el procesamiento de la misma, lo que hace que el programa o dispositivo que procesa dicha información se detenga momentánea y seguidamente por el hecho de que si continúa, estaría haciendo una solicitud a un espacio de memoria nula. Un subdesbordamiento de búfer puede efectuarse en cualquier software o dispositivo que dependa del flujo de datos o carga de un búfer: Grabadores, exploradores de internet, etcétera.

 Ejemplo gráfico

La combinación del color verde claro y el color verde oscuro representan el avance del proceso de la información, el color verde claro representa el progreso de carga del búfer, el verde oscuro representa el progreso del proceso fuera del búfer (Subdesbordamiento), y el color gris representa la memoria nula reservada para la carga del búfer:

 Ejemplo en un pseudocódigo

Un pseudocódigo de una carga de un búfer a una velocidad inferior a su procesamiento dentro del programa o dispositivo que lo solicita:

 búfer.cargar.velocidad 2
 programa.procesar.info.velocidad 3

En este caso el búfer carga información a una velocidad de valor "2" y es procesado por el programa o dispositivo a una velocidad de valor "3" (1 de offset),

 Ejemplo matemático

En este ejemplo "X" representa la velocidad de procesamiento de la información del búfer, "Y" representa los espacios nulos en la memoria (subdesbordamiento) de la carga del mismo:

 X(-Y)

De esta manera "X" está procesando información nula, aquí es donde ocurre el subdesbordamiento de búfer.

 Underflow/run vs Overflow/run

Un *subdesbordamiento de búfer* (buffer Underflow/run) es el opuesto de *desbordamiento de búfer* (buffer Overflow/run), por el hecho de que este último se produce mediante la aparición de una sobrecarga en el búfer y la incapacidad de procesar la información almacenada en él y un *subdesbordamiento de búfer* se produce por la falta de información en un búfer y el exceso de capacidad de procesar la información almacenada en él.

 Acceso no autorizado a la memoria

El espacio del progreso del proceso fuera de la carga del buffer de datos (Subdesbordamiento), permite que un atacante puede obtener un acceso no autorizado a la memoria para obtener un funcionamiento no esperado del programa vulnerable (desde el cierre del mismo hasta lograr ejecutar código arbitrario).

 Durante la grabación

Un **subdesbordamiento de búfer** durante la grabación de un CD o de un DVD es generado por falta de flujo de datos en el búfer de la grabadora, esto hace que el láser de la misma no pueda detenerse y comience a escribir el disco con información invalida, esto hace del disco un disco inservible e irreutilizable.
A mediados del año 2000, apareció de la mano de Sanyo el CD-RW que incorporaba la tecnología BURN-Proof (Buffer UndeRuN-Proof technology), esta tecnología le ordenaba al láser que hiciera una pequeña marca en el disco llamada GAP cuando detectaba que el búfer de la grabación también conocido como caché estaba vacío y que cuando volviese a cargar información, la grabación pueda reanudarse.

Ejemplo, BURN-Proof:

 SI Disco AVISA a Software_Grabador = ("Estoy enviando datos")
  Software_Grabador AVISA a Disco = ("Los recibo correctamente")
 SI Disco AVISA a Software_Grabador = ("No puedo enviar datos")
  Software_Grabador AVISA a Disco = ("No hay problema, me detengo")
 SI Disco AVISA a Software_Grabador = ("Ya me recupere")
  Software_Grabador AVISA a Disco = ("Continúo la grabación")

Otro método para protegerse de un subdesbordamiento de búfer durante la grabación es valerse de una memoria caché (búfer) alta, de esta manera la posibilidad de aparición de un subdesbordamiento de búfer se reduce notablemente, pero no proporciona una seguridad total, una combinación de una memoria caché alta y una protección contra un subdesbordamiento de búfer tal como lo es el BURN-Proof garantizan una gran protección contra un subdesbordamiento de búfer, por otro lado, la compañía Plextor usa la tecnología de Sanyo en combinación con su propia metodología PoweRec (Plextor Optimised Writing Error Reduction Control). Con esta, la grabación es periódicamente pausada usando la tecnología BURN-Proof, permitiendo que la calidad de grabado sea revisada y de una manera u otra esto permita aumentar la velocidad de grabación en algunos incrementos.

Otros fabricantes de unidades han licenciado tecnologías similares o han desarrollado sus propias versiones. Mitsumi usa la tecnología de OAK el sistema ExacLink, LG Electronics utiliza su tecnología SuperLink, Yamaha utiliza los mismos métodos pero sobre una marca llamada SafeBurn, Lite-On la llama Smart Burn, Acer Communications se refiere a su tecnología como Seamless Link y Ricoh a la suya como "JustLink". Aunque se conocen con distintos nombres, el resultado es el mismo.

Los formatos más nuevos como DVD+R, DVD+RW y Blu-Ray son inmunes a este problema porque debido a su diseño permiten pausar y reanudar la grabación a voluntad sin incidentes. Por lo que muchas aplicaciones desactivan automáticamente la protección al grabar en estos formatos.

 Referencias

 Véase también

 Búfer
 Caché
 Desbordamiento de búfer
 Error de software
 Inseguridad informática
 Null
 Offset
 Problemas aritméticos
 Seguridad informática

 Enlaces externos

 Características y trucos para evitar un buffer underrun
 Habilitar la protección contra buffer underrun en las nuevas grabadoras
