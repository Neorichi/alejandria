---
type: Artículo de enciclopedia
title: Infraestructura de clave pública
description: "La infraestructura de clave pública (, PKI) es un conjunto de roles, políticas, hardware, software y procedimientos necesarios para crear, administrar, distribuir, usar, almacenar y revocar certificados digitales y …"
resource: https://es.wikipedia.org/wiki/Infraestructura_de_clave_pública
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Infraestructura_de_clave_pública"}
license: CC BY-SA 4.0
id: eswiki-Infraestructura_de_clave_pública
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Infraestructura de clave pública

La **infraestructura de clave pública** (, PKI) es un conjunto de roles, políticas, hardware, software y procedimientos necesarios para crear, administrar, distribuir, usar, almacenar y revocar certificados digitales y administrar el cifrado de clave pública. El propósito de una PKI es facilitar la transferencia electrónica segura de información para diversas actividades de la red, como comercio electrónico, banca por Internet y correo electrónico confidencial. Se utiliza en actividades en las que las contraseñas simples son un método de autenticación inadecuado y se requieren pruebas más rigurosas para confirmar la identidad de las partes involucradas en la comunicación, así como para validar la información que se transfiere.

 Propósito y funcionalidad
La tecnología PKI permite a los usuarios autenticarse frente a otros usuarios y usar la información de los certificados de identidad (por ejemplo, las claves públicas de otros usuarios) para cifrar y descifrar mensajes, firmar digitalmente información y garantizar el no repudio de un envío, entre otros usos.

En una operación criptográfica que use PKI intervienen conceptualmente como mínimo las siguientes partes:
 Un usuario iniciador de la operación.
 Unos sistemas servidores que dan fe de la ocurrencia de la operación y garantizan la validez de los certificados implicados en la operación (autoridad de certificación, Autoridad de registro y sistema de sellado de tiempo).
 Un destinatario de los datos cifrados/firmados/enviados garantizados por parte del usuario iniciador de la operación (puede ser él mismo).

Las operaciones criptográficas de clave pública son procesos en los que se utilizan unos algoritmos de cifrado conocidos y accesibles para todos. Por este motivo la seguridad que puede aportar la tecnología PKI está fuertemente ligada a la privacidad de la llamada clave privada y los procedimientos operacionales o políticas de seguridad aplicados.

Es de destacar la importancia de las políticas de seguridad en esta tecnología, puesto que ni los dispositivos más seguros ni los algoritmos de cifrado más fuerte sirven de nada si, por ejemplo, una copia de la clave privada protegida por una tarjeta criptográfica —del inglés — se guarda en un disco duro convencional de un PC conectado a Internet.

 Tipos de certificados

Existen diferentes tipos de certificado digital, en función de la información que contiene cada uno y a nombre de quién se emite el certificado:

 **Certificado personal**, que acredita la identidad del titular.
 **Certificado de pertenencia a empresa**, que además de la identidad del titular acredita su vinculación con la entidad para la que trabaja.
 **Certificado de representante**, que además de la pertenencia a empresa acredita también los poderes de representación que el titular tiene sobre la misma.
 **Certificado de persona jurídica**, que identifica una empresa o sociedad como tal a la hora de realizar trámites ante las administraciones o instituciones.
 **Certificado de atributo**, el cual permite identificar una cualidad, estado o situación. Este tipo de certificado va asociado al certificado personal. (p.ej. Médico, Director, Casado, Apoderado de..., etc.).

Además, existen otros tipos de certificado digital utilizados en entornos más técnicos:

 **Certificado de servidor seguro**, utilizado en los servidores web que quieren proteger ante terceros el intercambio de información con los usuarios.
 **Certificado de firma de código**, para garantizar la autoría y la no modificación del código de aplicaciones informáticas.

 Componentes
Los componentes más habituales de una infraestructura de clave pública son:

 La autoridad de certificación (o, en inglés, CA, ***C**ertificate **A**uthority*): es la encargada de emitir y revocar certificados. Es la entidad de confianza que da legitimidad a la relación de una clave pública con la identidad de un usuario o servicio.
 La autoridad de registro (o, en inglés, RA, ***R**egistration **A**uthority*): es la responsable de verificar el enlace entre los certificados (concretamente, entre la clave pública del certificado) y la identidad de sus titulares.
 Los repositorios: son las estructuras encargadas de almacenar la información relativa a la PKI. Los dos repositorios más importantes son el repositorio de certificados y el repositorio de listas de revocación de certificados. En una lista de revocación de certificados (o, en inglés, CRL, ***C**ertificate **R**evocation **L**ist*) se incluyen todos aquellos certificados que por algún motivo han dejado de ser válidos antes de la fecha establecida dentro del mismo certificado.
 La autoridad de validación (o, en inglés, VA, ***V**alidation **A**uthority*): es la encargada de comprobar la validez de los certificados digitales.
 La autoridad de sellado de tiempo (o, en inglés, TSA, ***T**ime**S**tamp **A**uthority*): es la encargada de firmar documentos con la finalidad de probar que existían antes de un determinado instante de tiempo.
 Los usuarios y entidades finales son aquellos que poseen un par de claves (pública y privada) y un certificado asociado a su clave pública. Utilizan un conjunto de aplicaciones que hacen uso de la tecnología PKI (para validar firmas digitales, cifrar documentos para otros usuarios, etc.)

 Consideraciones sobre PKI

 Todo **certificado válido** ha de ser emitido por una autoridad de certificación reconocida, que garantiza la validez de la asociación entre el poseedor del certificado y el certificado en sí.
 El poseedor de un certificado es responsable de la conservación y custodia de la clave privada asociada al certificado para evitar el conocimiento de la misma por terceros.
 Las entidades de registro se encargan de la verificación de la validez y veracidad de los datos del que pide un certificado, y gestionan el ciclo de vida de las peticiones hacia las autoridades de certificación.
 El poseedor de un certificado *válido* puede usar dicho certificado para los usos para los que ha sido creado según las políticas de seguridad.
 Toda operación que realice el poseedor de un certificado ha de realizarse de forma presencial por parte del poseedor del certificado y dentro del hardware de cliente (ya sea la tarjeta criptográfica o PKCS#11 u otro dispositivo seguro, como el fichero seguro o PKCS#12, etc).
 Las comunicaciones con seguridad PKI no requieren del intercambio de ningún tipo de clave secreta para su establecimiento, por lo que se consideran muy seguras si se siguen las políticas de seguridad pertinentes.

 Seguridad de los certificados
La seguridad en la infraestructura PKI depende en parte de cómo se guarden las claves privadas. Existen dispositivos especiales denominados tokens de seguridad  para facilitar la seguridad de la clave privada, así como evitar que ésta pueda ser exportada. Estos dispositivos pueden incorporar medidas biométricas, como la verificación de huella dactilar, que permiten aumentar la confiabilidad, dentro de las limitaciones tecnológicas, en que sólo la persona dueña del certificado pueda utilizarlo.

 Ejemplos de uso
Los sistemas de PKI, de distintos tipos y proveedores, tienen muchos usos, incluyendo la asociación de una llave pública con una identidad para:
 Cifrado y/o autenticación de mensajes de correo electrónico (ej., utilizando OpenPGP o S/MIME).
 Cifrado y/o autenticación de documentos (ej., la firma XML o el cifrado XML si los documentos son codificados como XML).
 Autenticación de usuarios o aplicaciones (ej., logon por tarjeta inteligente, autenticación de cliente por SSL).
 Bootstrapping de protocolos seguros de comunicación, como IKE y SSL.
 Garantía de no repudio (negar que cierta transacción tuvo lugar)

 Véase también
 Autoridad de certificación
 Sellado de tiempo (timestamping)
 Seguridad por niveles
 Cifrado autenticado sin certificado
 PKCS

 Referencias

 Enlaces externos
 Decisión del Banco Central Europeo, de 11 de enero de 2013, por la que se establece el marco de una infraestructura de clave pública para el Sistema Europeo de Bancos Centrales (BCE/2013/1 Artículo 1), sitio digital 'Agencia Estatal Boletín Oficial del Estado (BOE), España.
