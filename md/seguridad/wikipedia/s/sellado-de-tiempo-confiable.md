---
type: Artículo de enciclopedia
title: Sellado de tiempo confiable
description: El sellado de tiempo confiable es el proceso de llevar, de manera segura, la cuenta del tiempo tanto de la creación como de la modificación de un documento electrónico.
resource: https://es.wikipedia.org/wiki/Sellado_de_tiempo_confiable
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sellado_de_tiempo_confiable"}
license: CC BY-SA 4.0
id: eswiki-Sellado_de_tiempo_confiable
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sellado de tiempo confiable

El **sellado de tiempo confiable** es el proceso de llevar, de manera segura, la cuenta del tiempo tanto de la creación como de la modificación de un documento electrónico. La seguridad aquí significa que nadie —ni siquiera el dueño del documento— podría ser capaz de cambiarlo una vez que ha sido guardado debido a que la integridad de aquel que realizó el sellado de tiempo nunca debe ser comprometida.

La parte administrativa involucra poner en marcha una infraestructura de sellado de tiempo confiable disponible públicamente para obtener, procesar y renovar sellados de tiempo.

 Historia
La idea detrás de realizar sellado de tiempo de la información tiene siglos de antigüedad. Por ejemplo, cuando Robert Hooke descubrió Ley de Hooke en 1660, él no quería publicarlo, pero quería ser capaz de reclamar su autoría. Para ello publicó el anagrama *ceiiinosssttuv* y luego publicó la traducción *ut tensio sic vis* (latín para *como la extensión, así la fuerza*). De similar manera, Galileo publicó primero su descubrimiento de las fases de Venus en la forma de un anagrama.

Un ejemplo moderno es el caso de una organización de investigación industrial que más tarde debería probar, para obtener una patente, que realizaron un descubrimiento en particular en una fecha en particular; como los medios magnéticos pueden ser alterados fácilmente, esto puede ser un problema no trivial.

Una posible solución es que el investigador compute y grabe una copia física en un cuaderno del laboratorio del *hash o* resumen criptográfico de la información del archivo en cuestión En el futuro, si llegase a existir la necesidad de probar que una versión de este archivo obtenida de un medio de respaldo, no fue alterada, la función de *hash* podría ser recomputada y comparada con el valor de *hash* que estaba escrito en el cuaderno.

 Sellado de tiempo (digital) confiable

De acuerdo al estándar RFC 3161, un sellado de tiempo confiable es un Sellado de tiempo emitido por un Tercero Confiable (TTP por sus siglas en inglés) que actúa como una autoridad de sellado de tiempo (AST). Es usado para demostrar la existencia de alguna información antes de cierta fecha (ej. contratos, información de investigación, registros médicos, etc.) sin la posibilidad de que el dueño pueda cambiar el sellado de tiempo. Múltiples ASTs pueden ser usadas para aumentar la confiabilidad y reducir la vulnerabilidad del sistema.

El nuevo estándar ANSI ASC X9.95 para Sellado de tiempo mejora el estándar RFC 3161 con nuevos requerimientos asociados a la seguridad de la información para asegurar la integridad de los datos contra una fuente confiable de tiempo comprobable ante terceros. Este estándar ha sido aplicado para autentificar información firmada digitalmente para conformidad reguladora, transacciones financieras, y evidencia legal.

 Creando el sellado de tiempo

La idea se basa en la firma digital y las funciones de *hash* o resumen. En primer lugar se calcula un *hash* de la información original. Un resumen es una especie de huella dactilar digital de la información original: una cadena de bits completamente diferentes para cada conjunto de información que se le entrega como parámetro de entrada. Si la información original se modifica aunque sea lo más mínimo, entonces dará como resultado un *hash* completamente diferente.

Este resumen es enviado a la AST, la cual concatena el sellado de tiempo al *hash* y calcula el nuevo resumen de esta concatenación. Este *hash* es firmado digitalmente con la llave privada de la AST. Finalmente, el resumen firmado junto con el sellado de tiempo son enviados de vuelta al solicitante del sellado de tiempo quien lo almacena junto a la información original (ver diagrama).

Como la información original no se puede calcular a partir del *hash* —pues la función resumen es una función unidireccional—, la AST nunca podrá obtener estos datos, lo que permite que este método se pueda utilizar para sellar información confidencial.

 Verificando el sellado de tiempo

Cualquiera que confíe en el emisor del sellado de tiempo puede entonces verificar que el documento no fue creado después de la fecha que indica el sellado. Además ya no puede ser repudiado que el solicitante del sellado de tiempo estaba en posesión de la información original al momento indicado por el sellado de tiempo. Para probar esto (ver diagrama) se calcula el *hash* de la información original, se adjunta a esto el sellado de tiempo otorgado por la AST y luego se calcula nuevamente un *hash* de la información anterior. A este resumen se le llamará A.

Entonces la firma digital de la AST necesita ser validada. Esto puede hacerse verificando que el resumen firmado proveniente de la AST fue efectivamente firmado con su llave privada mediante verificación de firma digital. El *hash* A es comparado con el *hash* B dentro del mensaje firmado por la AST para confirmar que son iguales, probando que el sellado de tiempo y el mensaje no fueron alterados y que este fue realmente publicado por la AST. Si esto no ocurre, entonces el sellado de tiempo fue alterado o bien el sellado de tiempo no fue emitido por la AST.

Sellado de tiempo descentralizado en la cadena de bloques

Con la llegada de las criptomonedas como el bitcoin, se ha vuelto posible obtener cierto nivel de precisión en el sellado de tiempo de manera descentralizada y a prueba de manipulaciones. Los datos digitales pueden ser codificados mediante hash y el hash puede ser incorporado en una transacción almacenada en la cadena de bloques, lo cual sirve como evidencia del momento en que esos datos existieron. Para las cadenas de bloques basadas en el Sistema de Prueba de Trabajo (Proof of Work), la seguridad se deriva de la enorme cantidad de esfuerzo computacional realizado después de que el hash se ha enviado a la cadena de bloques. Manipular el sellado de tiempo requeriría más recursos computacionales que los combinados del resto de la red y no podría hacerse sin ser detectado en una cadena de bloques activamente defendida.

Sin embargo, el diseño y la implementación de Bitcoin en particular hacen que sus sellados de tiempo sean susceptibles a cierto grado de manipulación. Permite sellados de tiempo hasta dos horas en el futuro y acepta nuevos bloques con sellados de tiempo anteriores al bloque anterior.

El enfoque de sellado de tiempo descentralizado utilizando la cadena de bloques también ha encontrado aplicaciones en otras áreas, como en las cámaras de tablero (dashboard cameras), para asegurar la integridad de los archivos de video en el momento de su grabación, o para demostrar la prioridad de contenido creativo e ideas compartidas en plataformas de redes sociales.

 Véase también
 Criptografía
 Digitalizador de firmas
 Seguridad informática
 Sellado de tiempo
 X.509

 Referencias

 Enlaces externos
 RFC 3161 Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)
 ANSI ASC X9.95 Standard for Trusted Time Stamps
 Free timestamp service (Jersey based)
 Free timestamp service + URL timestamps
 écrive.net - timestamping service
 RSA Laboratories - What is digital timestamping?
  (1991) Stuart Haber, W. Scott Stornetta, Lecture Notes in Computer Science
 The Trouble with Timestamps
 Free TSA.
