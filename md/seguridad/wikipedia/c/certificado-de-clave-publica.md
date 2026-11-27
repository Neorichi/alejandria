---
type: Artículo de enciclopedia
title: Certificado de clave pública
description: "Un certificado de clave pública es un tipo de documento digital firmado por una entidad llamada Autoridad de certificación (tipo de certificado digital) que asocia una clave pública a unos datos que representan la …"
resource: https://es.wikipedia.org/wiki/Certificado_de_clave_pública
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Certificado_de_clave_pública"}
license: CC BY-SA 4.0
id: eswiki-Certificado_de_clave_pública
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Certificado de clave pública

Un **certificado de clave pública** es un tipo de documento digital firmado por una entidad llamada Autoridad de certificación (tipo de certificado digital) que asocia una clave pública a unos datos que representan la identidad de una entidad (por ejemplo una persona física, organismo o empresa) que posee la clave privada asociada a dicha clave pública. De esta forma, cuando se usa la clave privada asociada a dicha clave pública se puede asegurar, atendiendo a la autoridad de la Autoridad de certificación, que ha sido usada por la entidad asociada.

Además de la clave pública y de indicaciones de la identidad, se pueden incluir otras informaciones relevantes como el periodo de validez, identificador de los algoritmos para los cuales se puede usar la clave pública o políticas o restricciones de uso de dicho certificado.

 Origen
El avance de las tecnologías y de información hace que tanto empresas como Administraciones se están decidiendo por Internet como vía de comunicación ya que permiten distribuir productos y servicios de una forma rápida y económica. Por ello se crea este certificado, para poder asegurar la identidad y confidencialidad de las comunicaciones entre ciudadanos, empresas u otras instituciones y administraciones públicas a través de Internet.

 Criptografía
Para asegurar la confidencialidad del mensaje se utilizan técnicas y sistemas criptográficos.
El cifrado digital consiste en aplicar un algoritmo para cifrar un mensaje reconocible y que este solo pueda ser descifrado con este mismo algoritmo y su correspondiente clave.
Hay dos opciones básicas en el cifrado digital:

Criptografía de clave simétrica: se utiliza una sola clave para cifrar y descifrar el mensaje. Este método es bueno para grandes cantidades de datos gracias a su velocidad pero el tener que distribuir la clave hace que si alguien la consigue junto con el mensaje podrá descifrarlo.
Criptografía de clave asimétrica: cada usuario tendrá una pareja de claves, una privada que solo la conocerá el propietario y otra pública conocida por todos los usuarios. Ambas complementarias. Esto hace que no sea necesario el envío de la clave pero hace el proceso más lento.

Para resolver el problema de lentitud se utiliza un algoritmo de clave pública con uno de clave simétrica.
La firma digital permite saber el origen de la información y asegurar que ésta no ha sido modificada.

 Tipos según su propósito
Se pueden clasificar los certificados según el propósito para el que se han sido creados. Veamos algunos ejemplos:
**Certificado de servidor TLS**
En TLS es necesario que el servidor presente un certificado como parte de la fase inicial de configuración. El cliente cuando se conecta verifica que el certificado del servidor es válido para la URL desde la que se presta el servicio.
**Certificado de cliente TLS**
En TLS el servidor puede requerir que el cliente se autentique mediante un certificado de cliente válido.
**Certificado de firma de código**
Un certificado válido puede ser usado para permitir la validación de firmas de programas con el fin de validar que no ha sido modificado.
**Certificado raíz**
Son certificados autofirmado, que son proporcionados por autoridades confiables, y que son usados para firmar otros certificados.
**Certificado para S/MIME**
Son certificados que permiten el uso del protocolo S/MIME para enviar correo electrónico cifrado y/o firmado.
**Certificado anónimo rastreable**

El RFC 5636 propone la generación de certificados anónimos rastreable a partir de un protocolo que separa la autoridad de certificación en dos entidades: La Autoridad de registro y la Autoridad de certificación propiamente dicha. El certificado generado asocia una clave pública a un seudónimo. La Autoridad de registro que mantiene en una base de datos la identidad real de las entidades (típicamente usuarios), y la Autoridad de certificación que tiene conocimiento de los certificados a seudónimos pero no tienen conocimiento de la identidad real del mismo. Sin la colaboración de ambas autoridades es imposible saber que entidad es el poseedor de un certificado. Por eso a estos certificado se les llama Certificados anónimos rastreables.

 Campos comunes
Los certificados de clave pública contienen una serie de campos. Los más habituales son:
**Serial Number**.- Es el número de serie e identifica de forma única el certificado de la CA. Esta clave es la que se usa si es necesario revocarlo.
**Subject**.- Indica la entidad que se certifica (por ejemplo una máquina, una persona o una organización)
**Issuer**.- La entidad que verificó la información y firmó el certificado (la Autoridad de certificación)
**Not Before**.- El momento a partir del cual el certificado es válido.
**Not After**.- El momento pasado el cual el certificado no es válido.
**Key Usage**.- Los usos criptográficos válidos para los que se puede usar el certificado (Ej firma de certificados, cifrado  de claves, cifrado de datos, o validación de firmas digitales).
**Extended Key usage**.- Aplicaciones en las cuales puede usar el certificado (por ejemplo autenticiación de servidores TLS, protección de correo electrónico o firma de código)
**Public Key**.- La clave pública firmada en el certificado.
**Signature Algorithm**.- Algoritmo usado para firmar el certificado de clave pública.
**Signature**.- La firma del cuerpo del certificado por la Autoridad de certificación.

 Utilización
Gracias a este certificado se podrán realizar trámites de manera rápida y segura con la Administración pública vía Internet. Existe un gran abanico de servicios que los Organismos y Empresas ofrecen al ciudadano.

 España

Según la Sede Electrónica del Instituto Nacional de Estadística (España), un certificado electrónico sirve para:

 Autenticar la identidad del usuario, de forma electrónica, ante terceros.
 Firmar electrónicamente de forma que se garantice la integridad de los datos trasmitidos y su procedencia. Un documento firmado no puede ser manipulado, ya que la firma está asociada matemáticamente tanto al documento como al firmante.
 Cifrar datos para que sólo el destinatario del documento pueda acceder a su contenido.

En España, actualmente los certificados electrónicos emitidos por entidades públicas son el DNI electrónico (DNIe) y el de la Fábrica Nacional de Moneda y Timbre - Real Casa de la Moneda (FNMT-RCM).
El DNIe español, al ser de uso obligado, comprende a más de 57 millones de usuarios. Por otro lado, aún no se ha puesto en marcha el NIE-electrónico, que facilitaría un uso más amplio de este sistema, y permitiría la reducción de costes burocráticos para las Administraciones Públicas y los usuarios.

Para el certificado digital de la FNMT, es necesario contar con DNI o NIE.

 Certificación de la FNMT-RCM
El certificado se descarga en el navegador del equipo donde lo han solicitado. No es necesario que se guarde en el disco duro, pudiendo exportarse directamente a un dispositivo extraíble (como una memoria USB).

1. Para tramitarlo, el usuario ha de dirigirse a la página de la FNMT, e instalar el CONFIGURADOR FNMT-RCM, tras lo cual se han de seguir las instrucciones del asistente y después reiniciar el equipo.

2. Una vez reiniciado el equipo, se ha de acceder a un enlace. Se introduce luego el DNI/NIE del solicitante, y se selecciona la longitud de clave-contraseña (pestaña debajo del campo para el DNI/NIE). Importante, si seleccionamos grado *alto*, debemos crear una contraseña personal que estará asociada al certificado —y esta contraseña no ha de olvidarse—; en caso de que seleccionemos grado *medio*, no creará ninguna contraseña (esta opción sólo aparece al usar el navegador Internet Explorer). Se ha de enviar petición y el sistema nos creará un código de 9 dígitos que debemos apuntar, o preferentemente imprimir.

3. Acreditación de la identidad: con el código de solicitud del paso anterior, deberá personarse en una oficina de registro (Agencia Tributaria o Seguridad Social) aportando el código y su DNI/NIE.

4. Descarga del Certificado de la FNMT: después de haber acreditado la identidad en una oficina de registro y haciendo uso del código obtenido en paso 2, se puede descargar el certificado en un determinado enlace.

Importante: No se ha de formatear el ordenador. Se debe realizar todo el proceso desde el mismo equipo, con el mismo usuario, y el mismo navegador.

Por otro lado, la validez del certificado se puede comprobar en VALIDe. o usando la aplicación FNM-RCM.

 Tarjeta CERES con certificado digital
Para las tarjetas CERES, en Mozilla hay que dar de alta el dispositivo de tarjeta criptográfica para que haga uso de ella. Para ello, hay que ir a Opciones->Avanzado->Dispositivo de seguridad. Hay que cargar el módulo criptográfico FNMT PKCS11.

 Véase también

 Referencias

 Enlaces externos
 Preguntas frecuentes de Certificados SSL
 Ley 19.799 actualizada - Ley chilena de sobre documentos electrónicos, firma electrónica y servicios de certificación de dicha firma.
Ley 527 de 1999 - Ley colombiana por medio de la cual se define y reglamenta el acceso y uso de los mensajes de datos, del comercio electrónico y de las firmas digitales, y se establecen las entidades de certificación y se dictan otras disposiciones.
 SeSeLe, Asistente para certificados SSL y CA autofirmados.

 España
 Ley 59/2003 - Ley española sobre firma electrónica.
 Ayuda de la Agencia Tributaria sobre Certificado digital.
