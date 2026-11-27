---
type: Artículo de enciclopedia
title: Criptografía con umbral
description: "La criptografía con umbral (en inglés threshold cryptography) tiene como objetivo distribuir alguna funcionalidad criptográfica entre muchos usuarios de tal forma que: Cualquier conjunto con usuarios pueda …"
resource: https://es.wikipedia.org/wiki/Criptografía_con_umbral
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_con_umbral"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_con_umbral
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía con umbral

La **criptografía con umbral** (en inglés *threshold cryptography*) tiene como objetivo distribuir alguna funcionalidad criptográfica entre muchos usuarios de tal forma que:
 Cualquier conjunto con  usuarios pueda colectivamente calcular la funcionalidad
 Ningún conjunto con solo  usuarios pueda realizar la funcionalidad.
Cuando se describe un sistema criptográfico con umbral se suele usar la notación 't-umbral' (en inglés *t-threshold*) para indicar cual es el valor umbral del sistema

El objetivo de distribuir la funcionalidad haciendo que cooperen distintas entidades se suele deber a las siguientes motivaciones:
**Tolerancia a fallos**
Por un lado es necesario comprometer la seguridad de varias entidades para romper la seguridad del sistema. Por otro lado, estableciendo un umbral menor que el número de participantes se permite que alguna de las entidades pueda dejar de funcionar aumentando así la disponibilidad de la funcionalidad.
**Distribución de responsabilidades**
Por ejemplo en un sistema de cifrado con umbral para obtener el contenido en claro es necesario que varios servidores cooperen para realizar la acción. En un sistema de firma con umbral es necesario que las dos entidades, que pueden tener visiones distintas del problema, estén de acuerdo en realizar la firma.

 Este enfoque fue iniciado por Yvo Desmedt y actualmente hay muchas propuestas principalmente para firma digital y para cifrado con clave pública.

 Cifrado de clave pública
Aplicando el concepto al cifrado, decimos que un cifrado es 'con umbral' si para descifrar un mensaje se requiere que cooperen un número de entidades superior al umbral requerido. Este tipo de sistemas solo es posible con clave pública. En estos sistemas el mensaje se cifra usando una clave pública y la clave privada es compartida de tal forma que permite la funcionalidad descrita.

Por ejemplo esto se usa en sistemas de voto electrónico donde se genera una clave pública, con la que el votante cifra sus votos, y para reconstruir la clave privada, usada para descifrar, es necesario que colaboren varias entidades. De esta forma se disminuye la confianza que se tendría que dar a una sola entidad.

Se han propuesto muchos esquemas.Por ejemplo se han propuesto sistemas de cifrado con umbral para RSA o para El-Gamal.

 Firma digital
 En los sistemas de firma digital con umbral solo  o más miembros del grupo pueden generar firmas del grupo con  miembros. Por otro lado  o menos miembros no pueden hacerlo. Por otro lado cualquiera puede usar la clave pública para verificar la firma.

El primer esquema de firma digital con umbral fue publicado por Yvo Desmedt y Yair Frankel Luego ha habido otras propuestas por ejemplo basadas en RSA.

Aplicaciones
Esta clase de esquemas de firma tiene mucho potencial para aplicaciones como toma de decisiones, voto electrónico, etc.

Por ejemplo en el RFC 5636 se usa para la generación de certificados con pseudónimos (Certificados anónimos rastreables) en el que hay una firma digital con 2 entidades firmantes y es necesario que firmen las dos. Por un lado se tiene la Autoridad de registro y por otro la de  Autoridad de certificación. Ambas entidades son independientes y operan en conjunto generando un certificado digital firmado parcialmente primero por la Autoridad de registro y después por la Autoridad de Certificación.

Tipos
De acuerdo a si un verificador puede rastrear los signatarios podemos distinguir dos tipos de firmas con umbral:
 Con firmantes anónimos, es decir, nadie puede revelar la identidad de los signatarios. Han sido propuestos distintos sistemas de este tipo
 Con firmantes rastreables

Generación de claves
En este tipo de esquemas un punto muy importante de la seguridad es como las distintas entidades pasan a poseer en exclusiva su clave secreta. Los dos enfoques principales son:
Confiar en una entidad confiable que obtenga las distintas claves y se encargue de distribuirlas.
Usar un protocolo de generación de claves distribuidas. En este tipo de protocolos múltiples entidades contribuyen al cálculo de la clave pública y de su propia clave privada. De esta forma en ningún momento ninguna entidad tiene posesión de información secreta que no debería tener.
 Referencias
