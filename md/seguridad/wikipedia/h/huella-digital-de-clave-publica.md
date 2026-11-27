---
type: Artículo de enciclopedia
title: Huella digital de clave pública
description: En la criptografía de clave pública, una huella digital de clave pública es una secuencia corta de bytes utilizada para identificar una clave pública más larga.
resource: https://es.wikipedia.org/wiki/Huella_digital_de_clave_pública
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Huella_digital_de_clave_pública"}
license: CC BY-SA 4.0
id: eswiki-Huella_digital_de_clave_pública
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Huella digital de clave pública

En la criptografía de clave pública, una **huella digital de clave pública** es una secuencia corta de bytes utilizada para identificar una clave pública más larga. Las huellas digitales se crean al aplicar una función de cifrado hash a una clave pública. Como las huellas digitales son más cortas que las claves a las que se refieren, se pueden usar para simplificar ciertas tareas de administración de claves. En el software de Microsoft, se usa "impresión del pulgar" en lugar de "huella digital".

 Creando huellas digitales de clave pública
Una huella digital de clave pública se suele crear a través de los siguientes pasos:

 Una clave pública (y opcionalmente algunos datos adicionales) está codificada en una secuencia de bytes. Para garantizar que la misma huella digital pueda recrearse más tarde, la codificación debe ser determinista, y cualquier información adicional debe intercambiarse y almacenarse junto con la clave pública. Los datos adicionales suelen ser información que cualquier persona que use la clave pública debe tener en cuenta. Los ejemplos de datos adicionales incluyen: con qué versiones de protocolo debe usarse la clave (en el caso de las huellas digitales de PGP); y el nombre del titular de la clave (en el caso de las huellas digitales del anclaje X.509 Trust, donde los datos adicionales constan de un certificado autofirmado X.509).
 Los datos producidos en el paso anterior se someten a hash con una función hash criptográfica como SHA-1 o SHA-2.
 Si lo desea, la salida de la función hash se puede truncar para proporcionar una huella digital más corta y más conveniente.

Este proceso produce una huella digital corta que puede usarse para autenticar una clave pública mucho más grande. Por ejemplo, mientras que una clave pública típica de RSA tendrá una longitud de 1024 bits o más, las huellas digitales típicas MD5 o SHA-1 tienen solo 128 o 160 bits de longitud.

Cuando se muestran para inspección humana, las huellas digitales suelen codificarse en cadenas hexadecimales. Estas cadenas se formatean en grupos de caracteres para facilitar su lectura. Por ejemplo, una huella digital MD5 de 128 bits para SSH se mostraría de la siguiente manera:

 43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8

 Uso de huellas digitales de clave pública para autenticación de claves

Cuando se recibe una clave pública en un canal que no es de confianza, como Internet, el destinatario a menudo desea autenticar la clave pública. Las huellas digitales pueden ayudar a lograr esto, ya que su pequeño tamaño les permite pasar por canales confiables donde las claves públicas no se ajustan fácilmente.

Por ejemplo, si Alicia desea autenticar una clave pública como perteneciente a Bob, puede ponerse en contacto con Bob por teléfono o en persona y pedirle que le lea su huella digital o darle un trozo de papel con la huella digital anotada. Alicia puede verificar que esta huella digital de confianza coincida con la huella digital de la clave pública. Intercambiar y comparar valores como este es mucho más fácil si los valores son huellas  digitales cortas en lugar de claves públicas largas.

Las huellas digitales también pueden ser útiles al automatizar el intercambio o el almacenamiento de datos clave de autenticación. Por ejemplo, si los datos clave de autenticación necesitan ser transmitidos a través de un protocolo o almacenados en una base de datos donde el tamaño de una clave pública completa es un problema, entonces el intercambio o almacenamiento de huellas digitales puede ser una solución más viable.

Además, las huellas las digital se pueden consultar con los motores de búsqueda para garantizar que los motores de búsqueda de terceros puedan ver la clave pública que un usuario acaba de descargar. Si el motor de búsqueda devuelve hits haciendo referencia a la huella  digital vinculada a los sitios adecuados, uno puede sentirse más seguro de que un atacante no está inyectando la clave, como un ataque Man-in-the-middle.

PGP desarrolló la lista de palabras de PGP para facilitar el intercambio de huellas digitales de clave pública a través de canales de voz.

 Huellas digitales de clave pública en la práctica

En sistemas como SSH, los usuarios pueden intercambiar y verificar huellas digitales manualmente para realizar autenticación de clave. Una vez que un usuario ha aceptado la huella digital de otro usuario, esa huella digital (o la clave a la que hace referencia) se almacenará localmente junto con un registro del nombre o dirección del otro usuario, para que las comunicaciones futuras con ese usuario puedan autenticarse automáticamente.

En sistemas como la PKI basada en X.509, las huellas digitales se utilizan principalmente para autenticar claves de raíz. Estas claves raíz emiten certificados que se pueden usar para autenticar claves de usuario. Este uso de certificados elimina la necesidad de verificación manual de huellas digitales entre los usuarios.

En sistemas como PGP o Groove, las huellas digitales se pueden utilizar para cualquiera de los enfoques anteriores: se pueden usar para autenticar claves que pertenecen a otros usuarios o claves que pertenecen a las autoridades emisoras de certificados. En PGP, los usuarios normales pueden emitir certificados entre sí, formando una red de confianza, y las huellas digitales se utilizan a menudo para ayudar en este proceso (por ejemplo, en las fiestas de firmado de claves).

En sistemas como CGA o SFS y la mayoría de las redes criptográficas punto a punto, las huellas digitales están integradas en formatos de nombres y direcciones preexistentes (como direcciones IPv6, nombres de archivos u otras cadenas de identificación). Si las direcciones y los nombres ya se están intercambiando a través de canales confiables, este enfoque permite que las huellas digitales se adhieran a ellos.

En PGP, la mayoría de las claves se crean de tal manera que lo que se denomina "ID de clave" es igual a los 32 o 64 bits inferiores, respectivamente, de una huella digitales de clave. PGP usa ID de clave para referirse a claves públicas para una variedad de propósitos. Estas no son, propiamente hablando, huellas digitales, ya que su corta duración les impide autenticar de forma segura una clave pública. Los identificadores de 32 bits no se deben utilizar ya que el hardware actual puede generar una identificación de 32 bits en tan solo 4 segundos.

 Seguridad de huellas digitales de clave pública

La principal amenaza para la seguridad de una huella digital es un ataque de preimagen, donde un atacante construye un par de claves cuya clave pública se mezcla con una huella digitales que coincide con la huella digital de la víctima. El atacante podría presentar su clave pública en lugar de la clave pública de la víctima para enmascararse como la víctima.

Una amenaza secundaria para algunos sistemas es un ataque de colisión, en el que un atacante construye múltiples pares de claves que se fusionan con su propia huella digital. Esto puede permitirle a un atacante repudiar las firmas que ha creado o causar otra confusión.

Para evitar los ataques de preimagen, la función de cifrado hash utilizada para una huella digital debe poseer la propiedad de la segunda resistencia de preimagen. Si los ataques de colisión son una amenaza, la función hash también debe poseer la propiedad de resistencia a la colisión. Si bien es aceptable truncar la salida de función hash por el bien de huellas digitales más cortas y utilizables, las huellas digitales truncadas deben ser lo suficientemente largas como para conservar las propiedades relevantes de la función hash contra ataques de búsqueda de fuerza bruta.

En la práctica, la mayoría de las huellas digitales que se usan comúnmente en la actualidad se basan en hashes MD5 o SHA-1 no truncados. A partir de 2017, se pueden encontrar colisiones pero no preimágenes en MD5 y SHA-1. Por lo tanto, es probable que en el futuro aumente el uso de nuevas funciones hash como SHA-256. Sin embargo, las huellas digitales basadas en SHA-256 y otras funciones hash con longitudes de salida largas tienen más probabilidades de ser truncadas que (relativamente cortas) huellas digitales MD5 o SHA-1.

En situaciones en las que la longitud de la huella digital debe minimizarse a toda costa, la seguridad de la huella digital puede aumentarse aumentando el costo de cálculo de la huella digital. Por ejemplo, en el contexto de Direcciones generadas criptográficamente, esto se denomina "Extensión Hash" y requiere que cualquier persona que calcule una huella digital busque un hashsum que comience con un número fijo de ceros, lo que se supone que es una operación costosa.

 Véase también
 Huella digital
 Criptografía asimétrica
 Fiesta de firmado de claves
 X.509

 Referencias
