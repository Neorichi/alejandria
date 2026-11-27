---
type: Artículo de enciclopedia
title: Inyección XPath
description: De manera similar a las inyecciones de SQL, ataques de inyección XPath se producen cuando un sitio web utiliza la información suministrada por el usuario para construir una consulta XPath para datos XML.
resource: https://es.wikipedia.org/wiki/Inyección_XPath
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Inyección_XPath"}
license: CC BY-SA 4.0
id: eswiki-Inyección_XPath
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Inyección XPath

De manera similar a las inyecciones de SQL, **ataques de inyección XPath** se producen cuando un sitio web utiliza la información suministrada por el usuario para construir una consulta XPath para datos XML. Mediante el envío de sentencias intencionalmente mal formadas, un atacante puede descubrir cómo se estructuran los datos XML, incluso acceder a todos sus datos. El atacante incluso puede ser capaz de elevar sus privilegios en el sitio web si los datos XML se utilizan para la autentificación (como un archivo de usuario basado en XML).

La consulta XML se realiza con XPath, un tipo de declaración descriptiva simple que permite la consulta XML para localizar información. Al igual que SQL, puede especificar ciertos atributos para encontrar y patrones para que coincidan. Cuando se hace uso de XML en un sitio web es común aceptar algún tipo de entrada en la cadena de consulta para identificar el contenido a localizar y mostrar en la página. Esta entrada debe ser desinfectada para verificar que no se mete hasta la consulta XPath y devuelva datos incorrectos o indeseados.

XPath es un lenguaje estándar, y su notación / sintaxis es siempre independiente de la implementación, lo que significa que el ataque puede ser automatizado. No hay dialectos diferentes, ya que se lleva a cabo en las solicitudes de las bases de datos SQL.
Debido a que no existe un control de acceso de nivel, es posible obtener el documento completo. No vamos a encontrar ningún tipo de limitaciones como podemos encontrar en los ataques de inyección SQL.

 Ejemplo de la vulnerabilidad

Usaremos este fragmento de código XML para los ejemplos.

Supongamos que tenemos un sistema de autenticación de usuario en una página web que utiliza un archivo de datos de este tipo para acceder a los usuarios. Una vez que un nombre de usuario y la contraseña han sido suministradas el software puede utilizar XPath para buscar el usuario:

Con un nombre de usuario y contraseña normales este XPath iba a funcionar, pero un atacante podría enviar un mal nombre de usuario y contraseña y obtener un nodo XML seleccionado sin conocer el nombre de usuario o contraseña, de esta manera:

En este caso, sólo la primera parte de la consulta XPath tiene que ser verdad. La sección de acceso se convierte en irrelevante, y la parte de Nombre de usuario coincidirá con TODOS los empleados debido a la parte "1 = 1".

 Defensa contra inyecciones XPath

Al igual que las técnicas para evitar la inyección SQL, es necesario utilizar una interfaz de XPath parametrizada, si está disponible, o escapar (filtrar) la entrada introducida por el usuario para que sea seguro incluirla en una consulta creada dinámicamente. Si estás usando comillas para terminar la entrada en la consulta dinámica del constructor XPath, entonces necesitas filtrar esa comilla en la entrada que no es de confianza para asegurar que los datos que no son de confianza no puedan tratar de salir de ese contexto citado. En el siguiente ejemplo, las comillas simples (') se utilizan para terminar los parámetros de usuario y contraseña. Por lo tanto, tenemos que sustituir ese carácter de la entrada con la versión XML codificada de ese carácter, que es "&apos;".

Otra mejor opción de defensa consiste en utilizar una consulta XPath precompilada. Las consultas XPath precompiladas ya están predefinidos antes de que el programa se ejecuta, en lugar de crear sobre la marcha la entrada del usuario y añadirla a la cadena de la consulta. Esta es una opción mejor, porque usted no tiene que preocuparse por perder un carácter que debería haberse escapado (filtrado).

 Véase también
 SQL
 Base de datos
 Modelo de base de datos
 Inyección SQL

 Enlaces externos
XPath Injection por owasp (en inglés)
