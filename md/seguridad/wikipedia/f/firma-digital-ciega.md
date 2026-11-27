---
type: Artículo de enciclopedia
title: Firma digital ciega
description: "La firma digital ciega es un protocolo de firma digital que permite a una persona obtener un mensaje con una firma o sello otorgados por otra entidad para que pueda ser presentada ante terceros, sin necesidad de …"
resource: https://es.wikipedia.org/wiki/Firma_digital_ciega
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Firma_digital_ciega"}
license: CC BY-SA 4.0
id: eswiki-Firma_digital_ciega
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Firma digital ciega

La **firma digital ciega** es un protocolo de firma digital que permite a una persona obtener un mensaje con una firma o sello otorgados por otra entidad para que pueda ser presentada ante terceros, sin necesidad de revelarle a esta información del contenido específico del mensaje.

La principal motivación que tuvo su creador David Chaum fue que cada vez que se llama por teléfono, se compra un producto usando una tarjeta de crédito, se suscribe a una revista o paga algún impuesto, esa información va a parar a una base de datos en algún lugar, lo que trasgrede nuestro derecho a privacidad.

 Analogía intuitiva
Para tener una idea intuitiva del concepto de firma ciega podemos establecer una analogía con la firma manual que realizamos en sobres de carta que tienen papel de calco. En estos sobres cuando firmamos en el papel de calco la propia firma pasa al documento que hay en el interior del sobre. De esta forma realizamos una firma de un documento sin saber el contenido de dicho documento. Este tipo de firma permite comprobar que el documento firmado es el mismo que estaba en el sobre que se entregó.

Por ejemplo con este tipo de firmas manuales podríamos establecer el siguiente esquema de votación sin usar medios electrónicos:
 El votante toma su papeleta de votación y la envuelve en papel calco, para luego enviarlo en un sobre con su remitente al comisario.
 El comisario abre el sobre, para firmar sobre el papel calco (sin ver que hay en el interior), y devuelve el paquete en otro sobre. Esta acción permitirá asegurar que el votante se encuentra autorizado para votar asegurando además el secreto del voto.
 Para el día de las elecciones, cada votante manda su papeleta con su voto marcado al comisario en un sobre sin remitente.
Posteriormente estos sobres pueden ser abiertos y contados públicamente. Si cada votante recuerda algún elemento característico de su papeleta, como el patrón en las fibras del papel, podrá reconocer su voto en el conteo.

 Definición
Un esquema de firma ciega es un protocolo criptográfico entre un usuario V y un firmante U de tal forma que U firma digitalmente una serie de datos enviados por V sin conocer el contenido  de los mismos. El propósito de este tipo de protocolos es la obtención de una serie de datos firmados cuyo contenido solo es conocido por el usuario.

Para implementar el protocolo de firma digital ciega se requiere lo siguiente:
Un protocolo de firma digital que sea desarrollado por el prestador del servicio o firmante U. Vamos a denotar por  a la firma digital del mensaje .
Dos funciones,  y , conocidas solo por el usuario V, de tal forma que:  tal que  no debe dar pista de
A la función  la llamamos **función de cegado, de ocultación o de opacidad**, y a la función  se le llama **función de descegado o de recuperación**.

El proceso sería de la siguiente forma. Supongamos que A tiene un mensaje que quiere que B firme sin saber lo que es. Se tendrían los siguientes pasos:
A crea un hash de su mensaje
A ciega dicho hash (usando la **función de cegado**) y se lo envía a B
B realiza la firma (usando protocolo de **firma digital**) y la envía a A
A desciega la firma (usando la **función de descegado**)
Podría pensarse por qué se ciega el hash si lo que se firma es un valor hash (no reversible) y no el contenido en claro. Esto se hace así para separar la operación de firmado de la operación de verificación de la firma. De esta forma C, otra entidad externa, puede verificar la firma sin que haya la posibilidad de que, al ponerse en contacto con B, B pueda identificar a A (observar que antes de prestar un servicio de firma ciega el servidor B es habitual que requiera una autenticación de A).

Ejemplo
Basándonos en el sistema criptográfico de clave pública RSA se puede desarrollar un esquema de firma ciega definiendo funciones de ocultación  y recuperación . Dado un k entero aleatorio tal que  definimos:

 Aplicaciones
La firma ciega ha sido utilizada para esquemas dinero electrónico (por ejemplo ecash) y esquemas de voto electrónico.

 Referencias
