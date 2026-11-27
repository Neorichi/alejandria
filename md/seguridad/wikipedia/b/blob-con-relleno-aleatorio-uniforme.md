---
type: Artículo de enciclopedia
title: Blob con relleno aleatorio uniforme
description: "En criptografía, un blob con relleno aleatorio uniforme (del inglés padded uniform random blob o PURB) es una disciplina para formatos de datos encriptados diseñada para minimizar filtraciones de información no …"
resource: https://es.wikipedia.org/wiki/Blob_con_relleno_aleatorio_uniforme
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Blob_con_relleno_aleatorio_uniforme"}
license: CC BY-SA 4.0
id: eswiki-Blob_con_relleno_aleatorio_uniforme
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Blob con relleno aleatorio uniforme

En criptografía, un **blob con relleno aleatorio uniforme** (del inglés **padded uniform random blob** o PURB) es una disciplina para formatos de datos encriptados diseñada para minimizar filtraciones de información no intencionada tanto del formato de su metadata de encriptación o de su largo total.

Propiedades de los PURBs

Cuando se crean apropiadamente, el contenido de un PURB es indistinguible de un string de bits aleatorio uniforme para cualquier observador que no tenga una llave de desencripción relevante. Por lo tanto, un PURB *no* filtra información desde encabezados u otra metadata en texto plano asociadas con el texto encriptado. Esta "higiene" de minimización de filtraciones contrasta con formatos de datos encriptados tradicionales como Pretty Good Privacy, el cual incluye información de codificación de los metadatos tales como la aplicación que creó la data, la versión del formato de datos, la cantidad de recipientes para quienes se destina la información, las llaves públicas de los receptores y las cifras que se usaron para encriptar los datos. Aun cuando esa metada de encriptación era considerada no relevante cuando se diseñaron estos formatos de encriptación, técnicas modernas de ataques han encontrado numerosas formas de usar dichos metadatos filtrados incidentalmente para facilitar ataques, tal como identificar datos encriptados con cifrados débiles o algoritmos obsoletos, identificar aplicaciones para rastrear usuarios o identificar versiones de software con vulnerabilidades conocidas, o técnicas de análisis de tráfico tales como identificar todos los usuarios, grupos y llaves públicas involucradas en una conversación desde un mensaje encriptado observado desde dos de ellos.

Además, un PURB está relleno hasta un grupo acotado de longitudes posibles, para minimizar la cantidad de información que los datos podrían filtrar potencialmente a observadores debido a su longitud total. Sin el relleno, los objetos encriptados como archivos o cadenas de bits hasta  bits de longitud pueden filtrar hasta  bits de información para un observador - la cantidad de bits necesaria para representar la longitud exactamente. Un PURB está relleno hasta una longitud representable en un número de punto  flotante cuya mantisa no es más larga que (o sea, no contiene más bits significativos que) los de su exponente. Esta restricción limita la cantidad máxima de información que el largo total de un PURB puede filtrar a un máximo de  bits, una reducción asintótica significativa y la mejor alcanzable en general para formatos de encriptación de largo variable cuyos encabezados se limita a un factor constante de la carga sin rellenar. Esta filtración asintótica es la misma que uno obtendría al rellenar objetos encriptados a la potencia de alguna base, tal como la potencia de dos.

Evidencia experimental indica que en grupos de datos que incluyen objetos como archivos, paquetes de software y videos en línea, dejar objetos sin rellenar o rellenarlos hasta un bloque constante los deja frecuentemente identificables simplemente por la longitud.  En cambio, rellenar objetos a la potencia de dos o a un largo PURB, asegura que la mayoría de os objetos son indistinguibles de al menos otros objetos y por lo tanto de un *grupo anónimo* no trivial.

 Codificando y decodificando PURBs

Debido a que PURB es una disciplina para diseñar formatos encriptados y no un formato encriptado particular, no hay un solo método para codificar y decodificar PURBs. Las aplicaciones pueden utilizar cualquier esquema de codificación provisto que produzca una cadena de bits que parezca uniformemente aleatoria para un observador sin la llave apropiada, asumiendo que los supuestos de dificultad computacional se satisfacen y que el PRUB está relleno hasta una de las longitudes permitidas. Por lo tanto, los PURBs correctamente codificados *no identifican la aplicación que los creó* en su texto cifrado. Una aplicación de desencriptación, por lo tanto, no puede antes de la decodificación saber si un PURB fue encriptado para esa aplicación o ese usuario, antes de tratar de desencriptarlo con todas las posibles llaves de desencriptación.

Codificar y decodificar PURBs presentan desafíos técnicos, debido a que las técnicas tradicionales de análisis sintáctico por definición no son aplicables ya que no tiene *marcadores* de metada que puedan usar para discernir la estructura antes de desencriptarla. En cambio, un PURB debe ser *desencriptado primero* y luego analizado cuando el decodificador ha usado la clave de encriptación adecuada para el PURB.

Codificar y decodificar PURBs para que puedan ser descifrados por varios receptores, claves públicas y/o cifrados presentan el desafío técnico adicional que cada receptor debe encontrar un punto de entrada diferente en el PURB al de otros receptores, pero el PURB no presenta metada con texto claro que indique las posiciones de esos puntos de entrada, ni siquiera la cantidad de ellos. El documento que proponía los PURBs también incluía algoritmos para encriptar objetos para múltiples destinatarios usando suites de cifrado múltiples. Con estos algoritmos, los receptores pueden encontrar sus puntos de entrada respectivos al PURB solamente con una cantidad de *desencripciones de prueba* logaritmicas usando Criptografía simétrica y solo una operación cara de Criptografía de clave pública por cada suite de cifrado.

Un tercer desafío técnico es representar la clave pública misma que necesita ser codificada en cada punto de entrada del PURB, como la clave pública efímera Diffie-Hellman que un receptor necesita para derivar el secreto compartido, en una codificación indistinguible de bits uniformemente aleatorios. Debido a la codificación estándar de puntos de curva elíptica que los hacen distinguibles de bits aleatorios, se deben utilizar algoritmos de codificación *indistinguibles*, tales como Elligator y sus sucesores.

Problemas y limitaciones

La ventaja principal de la privacidad es que los PURBs ofrecen una garantía fuerte que los datos correctamente codificados no filtrarán nada incidental por metadatos internos que algún observador pueda usar fácilmente para identificar debilidades en el software usado o en los datos que lo produjeron, o para identificar la aplicación o el usuario que creó el PURB. La ventaja de privacidad puede traducirse en un beneficio de seguridad para los datos encriptados con cifrados obsoletos o débiles, o por software que tenga vulnerabilidades conocidas y que un atacante pueda explotar basándose en información trivial de metadata del texto plano.

Una desventaja importante de la disciplina de encriptación de PURBs es la complejidad para su codificación y decodificación, debido a que el decodificador no puede confiar en las técnicas de análisis sintáctico tradicionales antes de la desencriptación. Una desventaja adicional es que el sobrecosto computacional del padding, aun cuando el esquema propuesto para los PURBs incurre en solo un bajo porcentaje de sobrecoste adicional para objetos de tamaño significativo.

El acolchado (*padding*) Padme propuesto en el documento PURB solamente crea archivos de tamaños específicos de tamaños muy distintos. Por lo tanto, un archivo encriptado podría ser identificado como encriptado con PURB con alta confianza, ya que la probabilidad de que cualquier otro archivo tenga un tamaño acolchado exacto es muy baja. Otro problema del padding ocurre con mensajes muy cortos, donde el acolchado no esconde correctamente el tamaño del contenido.

Una crítica de incurrir en la complejidad y sobrecosto de la encriptación PURB es que el *contexto* en el cual un PURB se almacena o se transmite puede filtrar metadatos sobre el contenido encriptado, y que por lo tanto esa metada está fuera del control del formato de encriptación y por lo tanto no puede ser gestionado por el formato de encriptación solamente.
Por ejemplo, la elección de un usuario del nombre de archivo o del directorio en el cual guardar un PURB en el disco podría permitir a un observador inferir la aplicación que probablemente lo creó y para qué propósito, aunque el contenido mismo del PURB no lo haga. Similarmente, encriptar el cuerpo de un correo electrónico como un PURB en vez del tradicional formato PGP o S/MIME puede eliminar el filtrado de metadatos, pero no puede prevenir la filtración de información de los encabezados desencriptados del correo, o desde el dispositivo de origen hasta el servidor de correo. Aun así, otras disciplinas separadas pero complementarias están típicamente disponibles para limitar esa filtración contextual de los metadatos, como el uso de convenciones apropiadas para nombres de archivos, o el uso de direcciones de correo con pseudónimos para comunicaciones sensibles.

 Referencias

 Enlaces externos
