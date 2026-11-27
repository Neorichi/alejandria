---
type: Artículo de enciclopedia
title: Inyección SQL
description: "Inyección SQL es un método de infiltración de código intruso que se vale de una vulnerabilidad informática presente en una aplicación en el nivel de validación de las entradas para realizar operaciones sobre una base de …"
resource: https://es.wikipedia.org/wiki/Inyección_SQL
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Inyección_SQL"}
license: CC BY-SA 4.0
id: eswiki-Inyección_SQL
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Inyección SQL

**Inyección SQL** es un método de infiltración de código intruso que se vale de una vulnerabilidad informática presente en una aplicación en el nivel de validación de las entradas para realizar operaciones sobre una base de datos.

El origen de la vulnerabilidad radica en la incorrecta comprobación o filtrado de las variables utilizadas en un programa que contiene, o bien genera, código SQL. Es, de hecho, un error de una clase más general de vulnerabilidades que puede ocurrir en cualquier lenguaje de programación o  script que esté incrustado en otro.

Se conoce como Inyección SQL, indistintamente, al tipo de vulnerabilidad, al método de infiltración, al hecho de incrustar código SQL intruso y a la porción de código incrustado.

 Descripción

Se dice que existe o se produjo una *inyección SQL* cuando, de alguna manera, se inserta o "inyecta" código SQL invasor dentro del código SQL programado, a fin de alterar el funcionamiento normal del programa y lograr así que se ejecute la porción de código "invasor" incrustado, en la base de datos.

Este tipo de intrusión normalmente es de carácter malicioso, dañino o espía, por tanto es un problema de seguridad informática, y debe ser tomado en cuenta por el programador de la aplicación para poder prevenirlo. Un programa elaborado con descuido, displicencia o con ignorancia del problema, podrá resultar ser vulnerable, y la seguridad del sistema (base de datos) podrá quedar finalmente comprometida.

La intrusión ocurre durante la ejecución del programa vulnerable, ya sea, en computadores de escritorio o bien en sitios Web, en este último caso obviamente ejecutándose en el servidor que los aloja.

La vulnerabilidad se puede producir automáticamente cuando un programa "arma descuidadamente" una sentencia SQL en tiempo de ejecución, o bien durante la fase de desarrollo, cuando el programador explicita la sentencia SQL a ejecutar en forma desprotegida. En cualquier caso, siempre que el programador necesite y haga uso de parámetros a ingresar por parte del usuario, a efectos de consultar una base de datos; ya que, justamente, dentro de los parámetros es donde se puede incorporar el código SQL intruso.

Al ejecutarse la consulta en la base de datos, el código SQL inyectado también se ejecutará y podría hacer un sinnúmero de cosas, como insertar registros, modificar o eliminar datos, autorizar accesos e, incluso, ejecutar otro tipo de código malicioso en el computador.

Por ejemplo, asumiendo que el siguiente código reside en una aplicación web y que existe un parámetro "nombreUsuario" que contiene el nombre de usuario a consultar, una inyección SQL se podría provocar de la siguiente forma:

El código SQL original y *vulnerable* es:

consulta := "SELECT * FROM usuarios WHERE nombre = '" + nombreUsuario + "';"

Si el operador escribe un nombre, por ejemplo "Pepe", nada anormal sucederá, la aplicación generaría una sentencia SQL similar a la siguiente, que es perfectamente correcta, en donde se seleccionarían todos los registros con el nombre "Pepe" en la base de datos:

SELECT * FROM usuarios WHERE nombre = 'Pepe';

Pero si un operador malintencionado escribe como nombre de usuario a consultar:

Alicia'; DROP TABLE usuarios; SELECT * FROM datos WHERE nombre LIKE '%

, se generaría la siguiente consulta SQL, (el color verde es lo que pretende el programador, el azul es el dato, y el rojo, el código SQL inyectado):

 SELECT * FROM usuarios WHERE nombre = 'Alicia';
 DROP TABLE usuarios;
 SELECT * FROM datos WHERE nombre LIKE '%';

En la base de datos se ejecutaría la consulta en el orden dado, se seleccionarían todos los registros con el nombre 'Alicia', se borraría la tabla 'usuarios' y finalmente se seleccionaría toda la tabla "datos", que no debería estar disponible para los usuarios web comunes.

En resumen, cualquier dato de la base de datos puede quedar disponible para ser leído o modificado por un usuario malintencionado.

Nótese por qué se llama "**Inyección**" SQL. Si se observa el código malicioso, de color rojo, se notará que está insertado en el medio del código bueno, el verde. Así, el código rojo ha sido "**inyectado**" dentro del verde.

La inyección SQL es fácil de evitar, por parte del programador, en la mayoría de los lenguajes de programación que permiten desarrollar aplicaciones web. En la siguiente sección se trata brevemente ese tema.

 Blind SQL injection

'*Ataque a ciegas por **inyección SQL****, en inglés, **Blind SQL injection*', es una función y una técnica de ataque que utiliza la inyección SQL. Se evidencia cuando en una página web, por un fallo de seguridad, no se muestran mensajes de error al no producirse resultados correctos ante una consulta a la base de datos, mostrándose siempre el mismo contenido (es decir, solo hay respuesta si el resultado es correcto).

Sentencias condicionales con el tipo "Or 1=1" o "having 1=1" ofrecen respuestas *siempre correctas* (true o verdadero) por lo cual suelen ser usadas por los programadores como formas de comprobación. El problema para la seguridad de la página radica en que esta técnica es utilizada en combinación con diccionarios o fuerza bruta para la búsqueda, carácter por carácter, de una contraseña, un nombre de usuario, un número de teléfono o cualquier otra información que albergue la base de datos atacada; para ello se utiliza código SQL específico que "va probando" cada carácter consiguiendo un resultado positivo acumulable cuando hay una coincidencia. De esta manera se puede saber, por ejemplo, que una contraseña comienza por "F...", luego continúa con ".i...", y luego "..r...", etc (acumula *Fir...*), hasta dar con la palabra completa.

Existen programas que automatizan este proceso de "tanteos" letra por letra en el resultado de la consulta SQL, que un intruso podría enviar inyectado.

 Algunas formas de evitar la *Inyección SQL*

 Ruby on Rails
En el framework Ruby on Rails (RoR), las consultas son verificadas automáticamente por cualquiera de los métodos de búsqueda incluidos. Por ejemplo:

La única forma de que un usuario mal intencionado pueda usar una inyección de SQL en RoR es que mediante código se transforme la variable a tipo string y se utilice como argumento de la búsqueda directamente. Por ejemplo:

 Perl
En lenguaje Perl DBI, el método DBI::quote filtra los caracteres especiales (asumiendo que la variable $sql contiene una referencia a un objeto DBI):

O también se puede usar la característica *placeholder* (con comillado automático) como sigue:

 PHP
En el lenguaje PHP, hay diferentes funciones que pueden servir de ayuda para usar con distintos sistemas de gestión de bases de datos.

Si se usa MySQL, la función a usar es mysql_real_escape_string:

No obstante es más recomendado usar alternativas que ofrecen consultas preparadas como la clase **PDO**.

Y si se utiliza MySQLi...

 Java
En lenguaje Java, se puede usar la interfaz PreparedStatement

En lugar de:

se puede usar parametrización o escape de variables, como se indica en los siguientes apartados.

 Parametrización de sentencias SQL

 Escape de las variables a insertar en la sentencia SQL

Escapar el texto contenido en la variable remplazando los caracteres especiales en SQL por su equivalente textual, de tal forma que SQL interprete todo el contenido de la variable como si fuera texto.

También se puede utilizar el método escapeSQL de la clase  procedente de la librería de Apache Commons Lang

 En C#
En lenguaje C#, de la plataforma .NET (o su alternativa libre Mono), se tiene ADO.NET SqlCommand (para Microsoft SQL Server) u OracleCommand (para servidores de bases de datos Oracle). El ejemplo siguiente muestra cómo prevenir los ataques de inyección de código usando el objeto SqlCommand. El código para ADO.NET se programa de forma similar, aunque puede variar levemente según la implementación específica de cada proveedor.

En vez de:

se podría usar lo siguiente:

 Véase también
 SQL
 Base de datos
 Modelo de base de datos
 Base de datos relacional
 Inseguridad informática

 Referencias

 Enlaces externos
Inyección SQL (SQL Injection) por Giancarlo Sanchez
 OWASP SQL Injection Cheat Sheets, by OWASP
 Técnicas de ataque en servidores web con scripts vía inyección SQL
 Artículo "Ataques a servidores SQL: Hacking, Cracking, y Técnicas de protección" escrito por Seth Fogie y Cyrus Peikari
 Artículo "Inyección SQL y Oracle, Parte uno"escrito por Pete Finnigan
 Artículo "Ataques de inyección SQL - ¿Estás a salvo?" escrito por Mitchell Harper
 Artículo "Protegiéndose frente a la inyección SQL" escrito por Umachandar Jayachandran
 Artículo "Detén los ataques de Inyección SQL antes de que ellos te detengan a ti" escrito por Paul Litwin
 "Protección contra los ataques de inyección"
 "Tutorial básico de la inyección SQL"
 "SQLrand: Previniendo los ataques de Inyección SQL" escrito por Stephen W. Boyd y Angelos D. Keromytis
 "¿Qué es la Inyección SQL?" escrito por CGISecurity.com
 "Inyección de código SQL: Excelente artículo resumido y completo " escrito por Juan Martínez Llinás (en español)
 Artículo "Inyección de código SQL en MS SQL Server 2005" "Pdf" Ejemplo y pasos a seguir para explotar un SQL SERVER 2005
 Artículo "Automatización de inyección SQL con PANGOLIN" Uso de herramientas gráficas para realizar tareas.
 Artículo "Automatización de inyección SQL con SQLiHelper " Uso de herramientas gráficas para realizar tareas.
bsqlbf.pl : programa escrito por un español en lenguaje Perl.
 Video de demostración de ataque BLIND SQL INJECTION mediante bsqlbf.pl
Video-Enumerando DB con una Blind Sql Injection
