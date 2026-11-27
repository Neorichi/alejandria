---
type: Artículo de enciclopedia
title: Content Scrambling System
description: CSS, del inglés Content Scrambling System, es un código de cifrado utilizado en los DVD (Digital Versatile Disc) comerciales, con el fin de cifrar la información multimedia, codificada en formato MPEG-2.
resource: https://es.wikipedia.org/wiki/Content_Scrambling_System
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Content_Scrambling_System"}
license: CC BY-SA 4.0
id: eswiki-Content_Scrambling_System
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Content Scrambling System

**CSS**, del inglés *Content Scrambling System*, es un código de cifrado utilizado en los DVD (Digital Versatile Disc) comerciales, con el fin de cifrar la información multimedia, codificada en formato MPEG-2. Fue creado con el fin de salvaguardar la duplicación ilegal de discos mediante el cifrado de archivos y la introducción de las claves de cifrado en el reproductor hardware.

 Descripción
El Content Scrambling System (CSS) se usa en DVD para cifrar los datos, de manera que solamente los reproductores con licencias de DVD pueden descodificar. El descifrado se realiza de diferentes formas, desarrollando un protocolo de petición-respuesta entre el software reproductor de DVD y la unidad lectora de DVD (ATAPI, SCSI o SATA).

 Proceso de descifrado
 La **autentificación** es un proceso por el cual la unidad lectora y el módulo de descifrado de CSS se reconocen (o autentifican) mutuamente. Este paso es necesario antes de poder leer datos del disco, para llevarlo a cabo se emplean "*las claves de autentificación*".
 Para el cifrado y descifrado de "títulos", se requieren las **claves de título**. Un título puede ser una película al completo, un tráiler, contenido extra, etc. empaquetado en un archivo contenedor.
 El descifrado de una clave de título se lleva a cabo mediante las **claves de disco**.
 Una clave de disco a su vez está cifrada mediante una **clave de reproducción**. Cada reproductor de DVD contiene un cierto número de claves que previamente han sido incorporadas por el fabricante, el cual posee alrededor de 400.

 Modos de cifrado en CSS
Un sector en un DVD contiene 2048 bytes (igual que el sector de un CD-ROM). Cada sector tiene una cabecera con un paquete MPEG-2 que son precedidas por sus correspondientes cadenas de datos (MPEG-2, AC-3, etc.) u otro tipo de información (PCI y DSI).

Un sector contiene los datos del paquete. Inmediatamente después de su cabecera, comienza la cabecera del PACK, que contiene 2 bits que determinarán el tipo de cifrado.

Estos bits se codifican de la siguiente manera, si el PACK es un paquete de datos:
 ***00***: no cifrado.
 ***01***: cifrado CSS.
 ***10***: desconocido / reservado.
 ***11***: cifrado CPRM.

Una vez obtenido un sector que necesite ser descifrado usando CSS, y la clave secreta correcta, éste es descifrado y está listo para ser reproducido en un PC o en un lector DVD.

 Debilidad del cifrado
El CSS se basa en un esquema simple de cifrado basado en cambios XORs y tablas de búsquedas. La longitud de la clave es de 40 bits, por lo tanto, para romper la llave mediante un ataque mediante fuerza bruta se precisan 2^25 combinaciones, y para un ataque de texto plano solamente 2^18 combinaciones.

La debilidad del CSS es precisamente la longitud extremadamente corta de la clave secreta y errores de cifrado que hacen que el algoritmo sea vulnerable a un ataque, pudiéndose analizar en un tiempo razonable.

 Autentificación del DVD
Cuando se inserta un nuevo DVD en una unidad DVD, éste debe ser autentificado antes de poder ser usado. La autenticación de disco es ligeramente más complicada. Usa CSS en modo 3.

La autenticación requiere de los siguientes pasos, que deben de realizarse en el orden correcto:
 Obtener un AGID de la unidad DVD.
 Realizar una llamada a la unidad y recibir su respuesta.
 Calcular los cambios sufridos por la unidad.
 Obtener las llamadas desde la unidad y calcular la respuesta.
 Enviar la respuesta a la unidad DVD.
 Leer la clave de disco recibida del disco.

Una vez se den estos pasos, toda la superficie del DVD será legible por la unidad de DVD.

 Ruptura del Algoritmo CSS
En 1999, el algoritmo CSS fue descubierto y publicado en Internet, por un adolescente noruego de 15 años, junto con un grupo de hackers.

Fue el noruego Jon Lech Johansen quien creó el DeCSS junto al grupo MoRE (Masters of Reverse Engeneering) para poder ver las películas adquiridas legalmente en Linux. El DeCSS (Decoder Content Scramblins System) siempre ha estado rodeado de un halo de prohibición, polémica y muchos problemas para su libre distribución, puesto que existen muchos intereses creados en el negocio de los DVD.

 Aspectos Jurídicos del escándalo DeCSS
La industria discográfica llevó a juicio al único miembro del grupo con identidad conocida: el joven noruego Jon Johansen, acusado de robo de datos. La justicia noruega absolvió a Jon de todos los cargos. Según el veredicto, usar DeCSS para leer DVD obtenidos legalmente no es ilegal, y no hay ninguna prueba de que Jon quisiera facilitar la copia ilegal.

Si Noruega hubiera tenido una legislación similar a la directiva sobre copyright de la UE, probablemente Jon hubiera sido declarado culpable de quebrantar el artículo 6 (violar una protección de copyright).

 Véase también
 ARccOS
 DVD Decrypter
 CPRM
 Jon Lech Johansen
 Criptografía
 Codificación
 Audio

 Referencias
 Content Scramble System (CSS) official website
 IEEE - Copy Protection for DVD Video (PDF)
 Cryptanalysis of Contents Scrambling System by Frank A. Stevenson
 The Content Scrambling System
