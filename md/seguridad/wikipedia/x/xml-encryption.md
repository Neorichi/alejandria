---
type: Artículo de enciclopedia
title: XML Encryption
description: A medida que la tecnología XML se extiende, cada vez más información se distribuye en este formato.
resource: https://es.wikipedia.org/wiki/XML_Encryption
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/XML_Encryption"}
license: CC BY-SA 4.0
id: eswiki-XML_Encryption
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# XML Encryption

A medida que la tecnología XML se extiende, cada vez más información se distribuye en este formato. Pero XML nació como formato de documentos y en sí mismo no contiene elementos relacionados con la seguridad. Esto hace necesario realizar un esfuerzo concreto en esta materia, en una búsqueda para encontrar un método para proteger esa información compartida.

XML Encryption es una Recomendación del Consorcio Web (W3C) que especifica un proceso para cifrar datos (no únicamente documentos XML) y representar esa información cifrada a su vez en XML para que viaje por los medios de transmisión. Este artículo pretende describir y ejemplificar someramente su funcionamiento, para información detallada acudir a la Especificación del Consorcio Web.

Se han publicado las graves deficiencias de seguridad de esta especificación.

 Aspectos generales

XML Encryption establece que para cifrar un elemento (o un contenido textual de un elemento), este va a ser sustituido por otro elemento establecido por la especificación que contendrá el dato cifrado y la información necesaria para el procesamiento, como puede ser la identificación del algoritmo utilizado o datos sobre la clave empleada. Este elemento es , de tal modo que podría aparecer como raíz del nuevo documento generado tras el proceso, o como hijo de otros elementos ya existentes previamente.

Por otro lado, la especificación establece XML Schema como esquema de modelo de datos. Dicho Schema puede ser consultado en la especificación de XML Encryption y es necesario para conocer la sintaxis a emplear.

La versión actual de XML Encryption utiliza el siguiente espacio de nombres:

xmlns:xenc='http://www.w3.org/2001/04/xmlenc#'

 Granularidad del cifrado de documentos XML

XML Encryption establece que es posible cifrar datos a distintos niveles de granularidad, desde elementos simples hasta documentos enteros. Puede verse fácilmente con un ejemplo bastante intuitivo, obtenido directamente del Consorcio Web (W3C). Supongamos que disponemos del siguiente documento XML:

    John Smith

      4019 2445 0277 5567
      Example Bank
      04/02

Se trata de una información de pago que contiene datos sobre una tarjeta de crédito: un cliente llamado John Smith dispone de una tarjeta de crédito, cuyo número es 4019 2445 0277 5567, con un límite de 5000 USD y con fecha de expiración. Esta información es delicada y debería ser protegida.

Veamos unos ejemplos de diferentes niveles de cifrado para ese documento…

 Cifrando un elemento

Podemos cifrar únicamente el elemento  y dejar el nombre del cliente intacto, obteniendo lo siguiente:

    John Smith

        A23B45C56

Al cifrar totalmente el elemento , incluyendo sus etiquetas, la identidad del elemento permanece oculta. Esto ofrece una interesante posibilidad para la seguridad ya que en principio no se sabrá cuál es el medio de pago hasta que no se descifre el dato.

 Cifrando elementos hijos

Podemos optar por no cifrar todo el elemento  sino algunos datos en concreto: el número, el banco y la fecha de expiración.

    John Smith

          A23B45C56

Ahora vemos que el elemento  permanece visible pero no los datos que queríamos ocultar.

 Cifrando contenido textual

Si queremos proteger únicamente el número de tarjeta de crédito (es decir, el contenido textual del elemento ) obtendríamos lo siguiente:

    John Smith

            A23B45C56

      Example Bank
      04/02

Vemos que toda la información permanece intacta excepto el contenido textual del elemento  que contenía el dato a proteger.

 Cifrando documentos enteros

Si se necesita que toda la información sea protegida es posible cifrar todo un documento XML. Si lo hacemos con el documento de nuestro ejemplo se obtiene lo siguiente:

      A23B45C56

Ahora, toda la información ha sido cifrada.

 Super-cifrado (cifrando datos previamente cifrados)

Dado que es posible cifrar cualquier tipo de información, nada nos impide cifrar datos que ya estaban cifrados. Esto se conoce como Super-cifrado y puede ser utilizado siempre que se respete la siguiente limitación: se debe cifrar el elemento  al completo.

Cifrar el contenido textual o elementos hijos del mismo tendría como resultado un documento XML inválido frente al Schema que define XML Encryption, ya que según este esquema un elemento  no puede ser padre o hijo de otro elemento . Será necesario pues tener en cuenta esa limitación a la hora de utilizar esta posibilidad de doble cifrado.

 Sintaxis de XML Encryption

Normalmente el aspecto de un documento XML cifrado será bastante más complejo que el que hemos visto en los ejemplos anteriores. El Schema que modeliza toda esa sintaxis es relativamente extenso y da cobertura a multitud de aspectos relacionados con la criptografía, empleando para ello un conjunto de elementos y atributos especiales.

Por ejemplo para conocer el método de cifrado empleado se utiliza el elemento . Si este elemento no existe el destinatario del mensaje cifrado debe saber de antemano cuál fue el algoritmo utilizado.

Los datos cifrados propiamente dichos se engloban en elementos , representando el contenido en Base 64.

El manejo de las claves también tiene su propia estructura, pero también se emplean partes propias de XML Signature (otro trabajo del W3C). Por ejemplo se puede asociar una cadena de caracteres visible a una clave secreta que sólo conozcan el emisor y el receptor de antemano. Esta cadena se incrusta en el elemento  y así el receptor sabrá que clave utilizar para descifrar la información (una interesante forma de evitar enviar las claves secretas por medios de comunicación inseguros).

Por otro lado, si optamos por enviar la clave junto con el documento, será recomendable que la cifremos a su vez; se utiliza para ello el elemento  para transportarla en el documento. Esto nos servirá para poder enviar la clave propiamente dicha junto con el documento de un modo seguro.

Existen más elementos y atributos específicos que aportan más información para el procesamiento de XML Encryption. Hay que tener en cuenta que, como se ha comentado antes, muchas de esos métodos pertenecen no a XML Encryption propiamente dicho sino a XML Signature.

 Algoritmos reconocidos

Dado que XML Encryption involucra muchos aspectos sobre criptografía y seguridad en general, se ha hecho una clasificación de los algoritmos reconocidos y de cuál es su misión en el procesamiento.

Para el cifrado de los datos se admiten diversos algoritmos de criptografía entre los cuales figuran TripleDES, AES y RSA. Cada uno debe ser referido en el documento cifrado mediante un identificador destinado a ello y que está definido en la especificación.

El transporte de las claves (Key Transport) queda a cargo de los algoritmos RSA-v1.5 y RSA-OAEP obligatoriamente. Su función es un cifrado asimétrico (clave pública) diseñado específicamente para cifrar y descifrar claves.

Para la autenticación de los mensajes (Message Authentication) el grupo de trabajo recomienda utilizar XML Signature, otro trabajo del Consorcio Web.

Los cánones del documento XML se describen en el *Canonical XML*, un trabajo del consorcio Web (W3C). Este proceso consiste en serializar un documento XML en un flujo de octetos, paso necesario para el cifrado.

Por último se establece que la codificación de los datos se haga obligatoriamente en Base64.

Existen más algoritmos y métodos reconocidos por XML Encryption que los aquí comentados… para conocerlos en detalle debemos acudir a la especificación.

 Implementaciones

Existen diversas implementaciones que se acogen a la actual especificación de XML Encryption:
 XML Security Library, de Aleksey Sanin, distribuido bajo MIT License (http://www.aleksey.com/xmlsec/).
 KeyTools XML, de Baltimore (https://web.archive.org/web/20031204164338/http://www.baltimore.com/keytools/xml/).
 Phaos XML (https://web.archive.org/web/20060907073156/http://www.phaos.com/products/category/xml.html).

 Referencias

 An Introduction to XML Encryption and XML Signatura, Murdoch Mactaggart
 1.0, W3C
 XML Encryption, W3C
 XML Key Management, W3C
 XML Schema, W3C
 XML Signature, W3C

*Este artículo incorpora material de http://www.planetasilius.tk, que mediante una  permitió agregar contenido publicarlos bajo licencia GFDL.*
