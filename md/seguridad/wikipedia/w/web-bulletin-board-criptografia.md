---
type: Artículo de enciclopedia
title: Web Bulletin Board (criptografía)
description: "Un Web Bulletin Board (siglas WBB), Public Bulletin Board (siglas PBB) o simplemente Bulletin Board (siglas BB), es un sistema informático que permite a un tipo de entidades (escritores) publicar información que es …"
resource: https://es.wikipedia.org/wiki/Web_Bulletin_Board_(criptografía)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Web_Bulletin_Board_(criptografía)"}
license: CC BY-SA 4.0
id: eswiki-Web_Bulletin_Board_(criptografía)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Web Bulletin Board (criptografía)

Un **Web Bulletin Board** (siglas WBB), **Public Bulletin Board** (siglas PBB) o simplemente **Bulletin Board** (siglas BB), es un sistema informático que permite a un tipo de entidades (escritores) publicar información que es accesible a otro tipo de entidades (lectores). La publicación de la información de dicho sistema se realiza de forma que cualquier mensaje publicado no puede ser borrado ni alterado. Además cuando se publica un mensaje nuevo se localiza al final de la secuencia ordenada de mensajes que es el WBB.

Es habitual que la información sea pública (de ahí lo de llamarlo PBB) y así todo el mundo puede ser un lector. Este hecho ha provocado que el tablón de anuncios se diga que es *web* para así sugerir que la lectura es realizada sobre HTTP, accesible a todo el mundo, aunque usar este protocolo no es obligatorio. Es bastante posible que, por razones de eficiencia, los lectores puede que vean solo cierta parte del contenido del WBB y no todo al completo.

Cuando un escritor escribe algo en el WBB, provee una firma digital para permitir que pueda ser verificado el origen del mensaje. Por otro lado el sistema del WBB es responsable de asegurar que todo el contenido es correcto y no ha sido cambiado después de la publicación. Por tanto:
Toda la información que se publica en el WBB tiene que ser firmada por el mismo.
Tiene que ser tolerantes de fallos para garantizar que no se pierda la información.
Deben tratar adecuadamente la situación de que dos o más escritores intenten escribir a la vez en el WBB.

Para resolver estos requisitos es habitual que el escritor espere una confirmación de escritura para cada petición de escritura que haya tenido éxito. Además el sistema suele establecer un tiempo mínimo desde que el WBB publicó un mensaje hasta que se publica el siguiente mensaje al que se le llama . Por tanto si un escritor no recibe confirmación de que la escritura ha sido correcta en ese tiempo es necesario que el escritor vuelva a empezar el proceso de escritura.

Diseños
Ha habido distintas propuestas para diseñar sistemas WBB. Las dos principales tendencias son las basadas en sistemas criptográficos específicamente diseñados para el problema o, por otro lado, usar la tecnología de cadena de bloques.
Propuesta de James Heather y David Lundin
James Heather y David Lundin han propuesto el siguiente esquema de criptografía para proveer la funcionalidad:
Un WBB es una secuencia  donde n comienza desde 1 y cada  contiene un mensaje junto con una serie de metadatos sobre el mensaje formando la siguiente estructura:
 donde
 es el mensaje
 es una marca temporal que indica el momento en el que se escribió el mensaje
 es el nombre del escritor
 es un valor hash que identifica el mensaje en el punto de la secuencia
 es la firma realizada por  del mensaje
 es la firma realizada por el WBB aceptando el mensaje para su publicación.
Para asegurar que dicha secuencia es consistente se tiene que cumplir
 con  indica el estado hash en el momento.
. Dado un momento, si se quiere meter un mensaje, es necesario conocer el valor actual de
 con  la marca temporal del momento de firmado
 con  el tiempo mínimo desde que el WBB publicó un mensaje hasta que se publica el siguiente mensaje.

Lectura
Cuando un lector lee el WBB recupera además del contenido una copia firmada y con marca de tiempo del hash del estado actual. Esto hace imposible, ya que se podría demostrar el fraude, que el WBB cambie posteriormente lo que anteriormente había en el WBB. Podemos formalizar lo que lee con:
, , donde  representa el momento actual.
Podemos decir que se trata de una lectura certificada donde la firma de la respuesta es un compromiso por parte del WBB de su contenido en el momento

Escritura
La escritura se realice en tres etapas:
El escritor obtiene el estado actual del WBB (obtiene un valor hash). Obtiene . El escritor rechazará el mensaje si este tiene un  donde T es el momento actual.
El escritor envía al WBB  donde . El WBB rechaza el mensaje si
El escritor recibe un recibo indicando como ha ido la escritura . El WBB rechaza el mensaje si
Podemos decir que se trata de una publicación certificada donde la firma del paso final no es solo un recibo de la publicación del mensaje sino también un compromiso del estado actual del WBB

Aplicaciones
Ejemplos de aplicaciones de un WBB:
En el voto electrónico es frecuente usar un WBB donde publicar ciertas informaciones con el fin de que distintas entidades puedan verificar cierta información y así permitir una verificabilidad del proceso
En el contexto de las subastas  los postores realizan ofertas en un determinado momento y quieren tener una prueba de que realizar esa oferta en ese determinado momento. Por otro lado el subastado quiere protección contra alegaciones y conductas indebidas. Por tanto ambos necesitan tener pruebas de que la secuencia de ofertas no ha sido manipulada.
En foros de discusión puede ser deseable tener un sistema que provea una historia auditable de la discusión.
En algunos contextos, puede ser útil tener un log verificable de las actividades de uno o varios sistemas.
Es posible incrementar la confianza de los sistemas de incidencias/peticiones de forma que las peticiones queden registradas de forma segura.

Referencias
