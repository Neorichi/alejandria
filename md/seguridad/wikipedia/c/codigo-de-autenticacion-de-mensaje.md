---
type: Artículo de enciclopedia
title: Código de autenticación de mensaje
description: En criptografía, un código de autenticación de mensaje o Message Authentication Code en inglés, a menudo llamado por su sigla MAC, es una porción de información utilizada para autenticar un mensaje.
resource: https://es.wikipedia.org/wiki/Código_de_autenticación_de_mensaje
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Código_de_autenticación_de_mensaje"}
license: CC BY-SA 4.0
id: eswiki-Código_de_autenticación_de_mensaje
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Código de autenticación de mensaje

En criptografía, un **código de autenticación de mensaje** o ***Message Authentication Code*** en inglés, a menudo llamado por su sigla **MAC**, es una porción de información utilizada para autenticar un mensaje.

Los valores MAC se calculan mediante la aplicación de una función hash criptográfica con clave secreta *K*, que solo conocen el remitente y destinatario, pero no los atacantes. Se dice que la función hash tiene que ser criptográfica porque tiene que cumplir ciertas propiedades de seguridad que las hacen resistentes frente a ataques de adversarios. Matemáticamente la función hash criptográfica toma dos argumentos: una clave *K* de tamaño fijo y un mensaje *M* de longitud arbitraria. El resultado es un código MAC de longitud fija:

*MAC* = *C*K(*M*)

donde:
 *M* es un mensaje de longitud arbitraria
 *C*K es la función que transforma el mensaje en un valor *MAC* y que utiliza una clave secreta *K* como parámetro
 *MAC* es el valor MAC calculado de longitud fija

Si el valor MAC enviado coincide con el valor que el destinatario calcula, este puede garantizar que:
 El mensaje no fue alterado
 El mensaje proviene del remitente indicado en el mensaje
 Si el mensaje incluye un número de secuencia, que el mensaje sigue la secuencia correcta

 Seguridad
 Función MAC ideal
Se define la función MAC ideal como un mapeo aleatorio de todos los posibles valores del mensaje de entrada *M* en salidas de tamaño de *n* bits.

 Propiedad de seguridad
 Para que una función MAC pueda ser usada es necesario que sea resistente a la computación de nuevos valores hash.

 Tipos de funciones MAC
Actualmente, existen 3 grandes grupos de funciones MAC:

 **CBC-MAC**: La idea detrás de este algoritmo es la de convertir un algoritmo de cifrado simétrico en una función MAC. El funcionamiento básico consiste en cifrar el mensaje usando un algoritmo en modo CBC y tirar todo el resultado de texto cifrado a excepción del último bloque.
 **HMAC**: Dado que una función MAC es un mapeo aleatorio, y que las funciones hash se comportan como tales, podemos explotar la idea de utilizar una función hash para implementar una función MAC. La opción más popular hoy en día es la de usar HMAC-SHA-256.
 **UMAC**: Las funciones UMAC parten de la premisa de que el atacante necesita interactuar con el sistema para comprobar si el resultado MAC que ha generado es válido o no. Es decir, no existe nada parecido a un ataque exhaustivo off-line contra las funciones MAC. Así, argumentan que se puede reducir el resultado a tan solo 64 bits. Sin embargo, no existe un estándar bien definido de funciones MAC como ocurre con las funciones hash, lo que tiene efectos contraproducentes a largo plazo desde el punto de vista de la implementación.

 Debilidad. Aplicación del principio de Horton
El uso de valores MAC para autenticar provee cierta seguridad pero no es la panacea. Por ejemplo, podría haber un ataque que consistiera en interceptar el mensaje y el valor MAC para poder reutilizarlo para autenticarse.

En general el principio de Horton establece que se debe autenticar el significado del mensaje, y no el código del mensaje. Aplicando el principio a autenticación de mensaje con MAC, deberíamos autenticar no solo el valor MAC, sino también cierta información que sea usada para formar un valor MAC que no sea ambiguo. Por ejemplo, puede ser buena idea incorporar algún tipo de sello de tiempo cuando calculó el valor MAC (por ejemplo concatenándolo al mensaje). Este sello de tiempo se enviaría al verificador. Si el verificador recibe un sello de tiempo antiguo entonces decide que es falso (ha caducado). Si el adversario decide actualizar el sello de tiempo entonces el valor MAC interceptado ya no sería válido para mandárselo al verificador.

Otro sistemas proponen concatenar al mensaje (para calcular el valor MAC) cierto datos relativos al contexto en el que se está (número de mensaje, tamaños de campos negociados, número de versión del protocolo...). Estos datos no habría que enviárselos al verificador porque ya están en el contexto y los conoce.

 Aplicaciones
Las MAC se suelen usar para autenticación (de ahí su nombre). El que se quiere autenticar y el verificador comparten la clave de la función MAC y la mantienen en secreto. De esta forma cuando el verificador recibe el valor MAC puede verificar si ese valor MAC se corresponde con el que se tiene que generar a partir de un mensaje dado.

Hay dos formas principales de funcionar, según donde se genere el mensaje:
 El mensaje es generado por el que se quiere autenticar y después este manda al verificador el mensaje y el valor MAC asociado. En el paso siguiente el verificador verifica la validez del valor MAC y a la vez se asegura de la integridad del mensaje recibido.
 El mensaje es generado por el verificador y se le manda al que se quiere autenticar para que este genere el valor MAC y lo mande al verificador. Este tipo de protocolo se encuadraría en los llamada protocolos desafío-respuesta

 Véase también
 Función hash criptográfica
 Data Authentication Code, un algoritmo de cálculo de valores MAC de ANSI basado en el cifrador simétrico DES
 UMAC
 HMAC
 CMAC
 Poly1305-AES
 Poly1305-AED
 Hash

 Referencias
