---
type: Artículo de enciclopedia
title: Lista de revocación de certificados
description: "La lista de revocación de certificados, conocida por sus sigla en inglés CRL (Certificate Revocation List) es un registro utilizado en la operación de algunos sistemas criptográficos, usualmente los de infraestructura …"
resource: https://es.wikipedia.org/wiki/Lista_de_revocación_de_certificados
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Lista_de_revocación_de_certificados"}
license: CC BY-SA 4.0
id: eswiki-Lista_de_revocación_de_certificados
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Lista de revocación de certificados

La **lista de revocación de certificados**, conocida por sus sigla en inglés **CRL** (***C*ertificate *R*evocation *L*ist**) es un registro utilizado en la operación de algunos sistemas criptográficos, usualmente los de infraestructura de clave pública (PKI), para mantener un listado de aquellos certificados (más concretamente sus números de serie) que han sido revocados y, por tanto, ya no son válidos y en los que no se debería confiar.

 Utilidad
Cuando una autoridad de certificación emite un certificado digital, lo hace con un periodo
máximo de validez, que suele estar comprendido entre dos y cuatro años. En España por ejemplo, la perdurabilidad máxima para fines legales esta tipificada por la Ley 59/2003 sobre la firma electrónica, Artículo 8. que establece la duración para los certificados reconocidos de un máximo de cinco años. El objetivo de este periodo de caducidad es
obligar a la renovación del certificado para adaptarlo a los cambios tecnológicos. Así se disminuye
el riesgo de que el certificado quede comprometido por un avance tecnológico.
La fecha de caducidad viene indicada en el propio certificado digital.

Sin embargo, existen otras situaciones que pueden invalidar el certificado digital aun cuando no ha caducado, de manera inesperada:
 El usuario del certificado cree que su clave privada ha sido robada.
 Desaparece la condición por la que el certificado fue expedido. Por ejemplo, el cambio de apoderado de una entidad jurídica.
 El certificado contiene información errónea o información que ha cambiado. Por ejemplo, una errata en los apellidos.
 Una orden judicial.
 Etc.

Por tanto, debe existir algún mecanismo para comprobar la validez de un certificado *antes*
de su caducidad. Las CRL son uno de estos mecanismos.

 Funcionamiento

Una CRL es una lista de números de serie de certificados digitales revocados por una autoridad
de certificación concreta. Dicha lista está firmada digitalmente por la propia autoridad de certificación.

Cuando un tercero desea comprobar la validez de un certificado debe descargar una CRL actualizada
desde los servidores de la misma autoridad de certificación que emitió el certificado en cuestión.
A continuación comprueba la autenticidad de la lista gracias a la firma digital de la autoridad de certificación. Después debe comprobar que el número de serie del certificado cuestionado está en la lista. En caso afirmativo, no se debe aceptar el certificado como válido.

Estrictamente hablando, no es necesario descargar una CRL cada vez que se verifica un certificado.
Solamente es necesario cuando no se dispone de la CRL de una entidad de certificación concreta, y cuando dicha lista tiene una cierta antigüedad que aconseja su renovación.

Una forma de averiguar si un certificado fue revocado es utilizando el protocolo OCSP (Online Certificate Status Protocol, RFC 2560). Mediante este último se pueden realizar consultas sobre certificados específicos sin la necesidad de descargar una CRL.

 Ventajas e inconvenientes

La única ventaja de las CRL es que se pueden consultar sin necesidad de una conexión de datos permanente con cada autoridad de certificación. Basta establecer dicha conexión con cierta periodicidad para descargar las CRL actualizadas.

Sin embargo, las desventajas de las CRL son varias:
 Existe el peligro de que un certificado haya sido revocado, pero no aparezca en la CRL del tercero que comprueba su validez. Esto se debe a que la CRL utilizada podría no estar actualizada.
 Si existe responsabilidad legal por el uso de un certificado revocado, no hay forma de demostrar quién es el culpable: el tercero por no comprobar la validez, o la autoridad de certificación por no incluirlo en la CRL a tiempo.
 Las CRL solamente crecen en tamaño, resultando ineficientes para su tratamiento directo.

 Alternativas

La única alternativa a las CRL es utilizar un protocolo de consulta en línea que aporte información al momento sobre cada certificado en concreto. Este protocolo se denomina OCSP.

 Enlaces relacionados

 Protocolo OCSP
 Infraestructura de clave pública
