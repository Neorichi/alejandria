---
type: Artículo de enciclopedia
title: Directory traversal
description: "Un directory traversal (o salto de directorio o cruce de directorio o path traversal) consiste en explotar una vulnerabilidad informática que ocurre cuando no existe suficiente seguridad en cuanto a la validación de un …"
resource: https://es.wikipedia.org/wiki/Directory_traversal
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Directory_traversal"}
license: CC BY-SA 4.0
id: eswiki-Directory_traversal
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Directory traversal

Un **directory traversal** (o **salto de directorio** o **cruce de directorio** o  **path traversal**) consiste en explotar una vulnerabilidad informática que ocurre cuando no existe suficiente seguridad en cuanto a la validación de un usuario, permitiéndole acceder a cualquier tipo de directorio superior (padre) sin ningún control.

La finalidad de este ataque es ordenar a la aplicación a acceder a un archivo al que no debería poder acceder o no debería ser accesible. Este ataque se basa en la falta de seguridad en el código. El software está actuando exactamente como debe actuar y en este caso el atacante no está aprovechando un bug en el código.

**Directory traversal** también es conocido como el ../ ataque punto punto barra, escalado de directorios y backtracking.

 Ejemplo
Un ejemplo típico de una aplicación vulnerable es:

Un ataque contra este sistema podría ser mandar la siguiente petición de HTTP:

GET /vulnerable.php HTTP/1.0
Cookie: TEMPLATE=../../../../../../../../../etc/shadow

Generando el servidor una respuesta como:

HTTP/1.0 200 OK
Content-Type: text/html
Server: Apache

root:fi3sED95ibqR6:0:1:System Operator:/:/bin/ksh
daemon:*:1:1::/tmp:
phpguru:f8fk3j1OIf31.:182:100:Developer:/home/users/phpguru/:/bin/csh

La repetición de los caracteres ../ después de /home/users/phpguru/templates/ ha causado que el código include penetre hasta el directorio raíz y entonces fuese al directorio de contraseñas de UNIX "/etc/shadow".

El archivo de contraseñas de UNIX es un archivo que se utiliza comúnmente para realizar el **directory traversal**, y es utilizado frecuentemente para crackear las contraseñas.

 Variaciones de directory traversal
Directory traversal es más complicado de prevenir de lo que puede parecer. Una estrategia de filtrar los caracteres que puedan suponer una amenaza es probable que falle.

Hay muchos más factores implicados que pueden determinar el funcionamiento de un ataque directory traversal. Sin embargo, si la aplicación no valida la legitimidad de los parámetros, es bastante probable que los atacantes tengan muchas probabilidades de explotar esta funcionalidad para propósitos maliciosos.

A continuación se listan algunas de las cadenas de ataques directory traversal conocidas:

 Directory traversal en UNIX
En los sistemas Unix o similares se utiliza los caracteres ../, para realizar el directory traversal.

 Directory traversal en Microsoft Windows
En Microsoft Windows o DOS el directory traversal se realiza mediante ..\.

Actualmente, muchos programas para Windows o APIs aceptan además los caracteres utilizados para directory traversal en sistemas Unix o similares.

Cada partición tiene un directorio raíz (nombrado C:\  para una partición particular C) y no existen un directorio común raíz por encima de este. Esto quiere decir que las vulnerabilidades de directorio en Windows están limitadas a una única partición.

 URI codificado directory traversal
Algunas aplicaciones realizan escaneos sobre las cadenas introducidas buscando caracteres peligrosos como:
 ..
 ..\
 ../
para prevenir el directory traversal. Sin embargo, la cadena es usualmente decodificada en URI antes de ser utilizada. Es por ello que estas aplicaciones son vulnerables a percent encoded directory traversal como puede ser:
 %2e%2e%2f que se traduce a ../
 %2e%2e/ que se traduce a ../
 ..%2f que se traduce a ../
 %2e%2e%5c que se traduce a ..\
etc.

 Unicode / UTF-8 codificado directory traversal

UTF-8 ha sido marcada como fuente de vulnerabilidades y ataques vectoriales en Cryptogram Newsletter July 2000 por Bruce Schneier y Jeffrey Streifling.

Cuando Microsoft añadió soporte unicode a su servidor Web, una nueva forma de codificar los caracteres ../ fue introducida en su código, causando vulnerabilidades de codificación en cuanto a directory traversal.

La codificación de porcentajes múltiples, como por ejemplo:
 %c1%1c
 %c0%9v
 %c0%af
se traducen a los caracteres / o \.

Esto se debe a que las cadenas cifradas con porcentajes se decodifican en caracteres de 8-bit (por parte de un Microsoft webserver). Este comportamiento ha sido históricamente correcto por parte de Windows y DOS que tradicionalmente han utilizado 8-bit basados en el canon de ASCII.

Sin embargo, el UTF-8 original no seguía ningún canon, y muchas cadenas cifradas que podían ser traducidas a una misma cadena. Microsoft desarrolló un sistema anti-traversal para UTF-8, no dándose cuenta de que C0AF y 2F en (HEX) eran los mismos caracteres cuando se realizaban comparaciones de cadenas.

 Posibles métodos para prevenir Directory Traversal

Un posible algoritmo para prevenir el directory traversal podría ser:

 Procesar las peticiones de URI para que no resulten en una petición de un fichero.
 Cuando se realiza una petición URI por un fichero/directorio, se debe construir el path completo del fichero/directorio (sólo si este existe), y normalizar todos los caracteres (ej, 20% convertido a espacios).
 Se asume que un documento raíz está normalizado, su directorio es conocido y tiene un tamaño N. Además ningún fichero de este directorio puede ser servido.
 Asegurarse de que los primeros N caracteres de un directorio correcto es exactamente el mismo que el del documento raíz.
 Si sucede esto, permitir al fichero ser devuelto.
 Si no, devolver un error, la petición está claramente fuera de los límites de lo que el web-server debería permitir entregar.

 Enlaces externos

(en inglés) Conviction for using directory traversal.
(en inglés) Bugtraq: IIS %c1%1c remote command execution
(en inglés) Cryptogram Newsletter July 2000 .
