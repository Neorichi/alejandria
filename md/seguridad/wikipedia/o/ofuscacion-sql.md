---
type: Artículo de enciclopedia
title: Ofuscación SQL
description: La Ofuscación SQL es uno de los principales métodos utilizado por los hackers para acceder a bases de datos.
resource: https://es.wikipedia.org/wiki/Ofuscación_SQL
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ofuscación_SQL"}
license: CC BY-SA 4.0
id: eswiki-Ofuscación_SQL
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ofuscación SQL

La **Ofuscación SQL** es uno de los principales métodos utilizado por los hackers para acceder a bases de datos.

Al estar al tanto de los controles de seguridad que protegen los activos digitales, los atacantes en muchos casos usan técnicas de evasión para pasar desapercibidos y montar su ataque sin ser detectados y bloqueados por mecanismos de seguridad. Una de las técnicas de evasión más populares, aplicable sobre todo contra los mecanismos de seguridad basados en patrones es la ofuscación, generando una instancia del ataque que hace esencialmente lo que el ataque está destinado a hacer, pero está diseñado intencionalmente para verse muy diferente del patrón del control de seguridad busca.

Por ejemplo, la ofuscación de sentencias de SQL (nos referimos a esto más tarde como ofuscación de SQL) es muy común como un medio para eludir los firewalls de aplicaciones web (WAF) y ejecutar ataques de inyección SQL, y confundir las soluciones de monitoreo de actividad de base de datos, (DAM) que analizan el tráfico de la base de datos SQL Esta técnica es común entre atacantes, herramientas de automatización y pen testers para ejecutar implícitamente comandos SQL contra bases de datos.

Uno de los métodos más comunes para sustentar un ataque de inyección SQL es el uso de codificación SQL HEX, donde las transacciones de SQL "legibles" de texto plano se convierten en caracteres HEX o hexadecimales (0-9, AF), lo que hace que sean ilegibles y más difíciles de monitorear por DAM y soluciones de firewall de base de datos (DBF). Por lo tanto, una "selección * de contraseñas" en una solución DAM se vería así: "73656C656374202A2066726F6D2070617373776F726473".

 Patrones de ataques SQL codificados en HEX
Basándose en análisis de datos, detectamos varios patrones de ataques SQL codificados en HEX. Sorprendentemente, una de cada cinco consultas de ataque en SQL Server aprovechó las técnicas de codificación HEX. Este tipo de ataque es menos común para las bases de datos MySQL.

 Ejemplo en Microsoft SQL Server
El siguiente es el patrón más común de un ataque SQL codificados en HEX contra SQL Server:en el ejemplo anterior, los comandos de ataque se colocan en la variable ***a***, cuando están codificados como una cadena HEX. A continuación, los comandos ofuscados se ejecutan mediante la instrucción ***exec(@a)***. Detrás de las consultas con codificación HEX encontramos varios tipos de ataques.

Este es otro ejemplo de una consulta HEX que observamos en Microsoft SQL Server:El Transact-SQL anterior (T-SQL) entrega una carga maliciosa a un sistema objetivo. Crea y escribe un archivo (generalmente un archivo ejecutable o DLL) en una ubicación específica en un sistema de destino. El ataque se realizó utilizando el objeto ADODB.Stream (que tiene un identificador de clase de ***'00000566-0000-0010-8000-00AA006D2EA4'***) y procedimientos almacenados de automatización OLE (***sp_OA***). Los procedimientos OLE le permiten trabajar con objetos COM desde T-SQL. Puede usar estos procedimientos para crear objetos COM y usar los métodos y propiedades de ese objeto. Por ejemplo, use el objeto Sistema de archivos para abrir, leer y escribir archivos directamente dentro de T-SQL.

 Ejemplo en MySQL
En base al análisis de ataques a MySQL, detectamos tres patrones de consultas con codificación HEX. Estos patrones intentan entregar una carga útil a un sistema objetivo a través de comandos SQL.La colección de comandos en ***Pattern*** 1 y 2 carga un ejecutable portátil (PE) con codificación HEX en una tabla y luego lo extrae en un archivo en un sistema de destino.La colección de comandos en ***Pattern*** 3, decodifica y carga un archivo DLL en un archivo en un sistema de destino. Luego, crea una nueva función SQL que reside en la DLL entregada y ejecuta la función utilizando el comando SELECT. Esta función descarga y guarda otro ejecutable en una ubicación específica, cambia sus permisos a '777' (todos pueden leer escribir y ejecutar) y finalmente lo ejecuta.

 Consultas ofuscadas
Las consultas con codificación HEX se usan a menudo contra MySQL y MS SQL Server como métodos avanzados de conversión de binario a hexadecimal para entregar una carga a un sistema de destino a través de comandos SQL. Una vez que la carga útil está en el sistema de destino, convierte de formato hexadecimal a un ejecutable binario y luego se ejecuta.

Las consultas con codificación HEX también se utilizan para modificar las configuraciones de seguridad de la base de datos para aumentar una superficie de ataque. Por lo general, se manifiestan en servicios y características habilitantes. Las siguientes consultas habilitan opciones avanzadas y desactivan el rastreo predeterminado. El seguimiento predeterminado proporciona un registro de actividad rico y persistente y cambios relacionados principalmente con las opciones de configuración. Luego recuperan información sobre todos los rastros existentes usando el procedimiento ***fn_trace_getinfo*** y luego los detienen.Además, los ataques en MS SQL que tenían el propósito de controlar los servicios de Microsoft-Windows-SharedAccess y SQL Server Agent a través de la llamada del procedimiento ***xp_servicecontrol***.

Los ataques detienen el servicio Microsoft-Windows-SharedAccess, que es responsable del uso compartido de la conexión a Internet. Esta acción en realidad detiene el Firewall de Windows.Además, los atacantes usan el procedimiento ***xp_servicecontrol*** para iniciar un servicio del Agente SQL Server que ejecuta trabajos SQL que contienen más comandos de ataque.

 Referencias
