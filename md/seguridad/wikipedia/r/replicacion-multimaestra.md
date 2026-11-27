---
type: Artículo de enciclopedia
title: Replicación multimaestra
description: La replicación multimaestra es un método de replicación de base de datos donde se habilitan los datos para ser distribuidos en un grupo de computadoras, y actualizado por cualquier miembro del grupo.
resource: https://es.wikipedia.org/wiki/Replicación_multimaestra
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Replicación_multimaestra"}
license: CC BY-SA 4.0
id: eswiki-Replicación_multimaestra
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Replicación multimaestra

La **replicación multimaestra**  es un método de replicación de base de datos donde se habilitan los datos para ser distribuidos en un grupo de computadoras, y actualizado por cualquier miembro del grupo. El sistema de replicación multimaestra es responsable de propagar la modificación de los datos a los diferentes miembros, estos datos pueden ser contrastados con una replicación maestra-esclava, en donde un miembro del grupo está asignado como el "maestro" para tomar las piezas de datos y es el único del nodo habilitado a modificarlos. Otros miembros solo pueden modificar los datos comunicándose con el maestro del nodo. Habilitando solo un maestro se facilita la consistencia en los miembros del grupo, pero es de reducida flexibilidad frente a la replicación multimaestra.

 Ventajas
 Si un maestro falla, otros maestros continuaran actualizando la base de datos
 Los maestros pueden estar en diferentes lugares físicos. Ej: a través de una red distribuida

 Desventajas
 Muchos sistemas de replicación multimaestra son pobremente consistentes. Ej: retardo y asincronía, violación de propiedades ACID
 Varios de los sistemas de replicación son muy complejos y producen latencia en la comunicación
 Problemas como resolución de conflictos puede volverse difícil en tanto incrementa el número de nodos lo cual aumenta las latencias

 Métodos

 Basado en Log
Un log de transacción de base de datos esta referenciada a capturar cambios hechos en las bases de datos. Para la captura de transacciones basadas en log, los cambios de las bases de datos solo pueden ser distribuidas asíncronamente.

 Basado en Trigger
Los Triggers en el suscriptor capturan cambios hechos para a la base de datos y los envían al publicador. Con captura de transacción basada en trigger, la base de datos puede ser distribuida tanto síncronamente como asíncronamente.

 Implementaciones
La mayoría de los servidores de directorio basados en LDAP implementan replicación multimaestra.

 OpenLDAP
El más usado servidor de código abierto de LDAP implementa replicación multimaestra desde la versión 2.4 (October 2007)

 MySQL

MariaDB y MySQL tienen soporte de replicación y posibilita el esquema de replicación multimaestra desde la versión 3.23. El MySQL Cluster soporta detección y resolución de conflictos entre múltiples maestros desde la versión 6.3.

 PostgreSQL

PostgreSQL, desde la versión 9.0, incluye replicación binaria interna (built-in binary replication), basada en intercambio de cambios a todos los bloques de bases de datos para otros sistemas asíncronos después del commit. PostgreSQL también habilitara ejecuciones de queries de solo lectura para las réplicas esclavas. esto permitirá dividir el tráfico de lectura sobre múltiples nodos eficientemente.

PostgreSQL ofrecerá múltiples soluciones para replicación multi-maestra, incluyendo soluciones basadas en commit de dos faces. Las herramientas Bucardo, rubyrep, PgPool y PgPool-II, PgCluster y Sequoia como algunas otras soluciones propietarias. Otra promesa es la esperada implementación replicación sincrónica con Postgres-R y Postgres-XC que están en desarrollo.

 Ingres

Con el Ingres Replicator, los objetos que se actualizan en un servidor Ingres pueden ser replicador en otros servidores locales o remotos a través de replicación multi-maestra. Si uno de los servidores falla, la conexión del cliente puede ser redirigida a otro servidor. Esto no es requerido por todos los servidores Ingres en un ambiente de replicación en cada uno de los otros porque esta nube causa excesivo tráfico de red en las implementaciones. Por el contrario, Ingres Replicator provee de un elegante y sofisticado diseño que permite que intercambiar los datos entre servidores indicados ordenadamente reduciendo así el tráfico de red. Esto permite que alguno funcione como servidor contra fallas mientras los demás obtienen los nuevos datos, que es reforzado con un protocolo de commit en dos faces asegurando así la correcta transacción durante al replicación. Ingres Replicator además es capaz de operar con soluciones RDBMSs de diferentes proveedores.

 Véase también
 Transferencia de zona DNS
 Optimización de Replicación
 Operación Maestra Simple Flexible
 Active Directory
 Sistema de Administración Distribuido de Bases de datos

 Referencias
 Challenges Involved in Multimaster Replication
 Active Directory Replication Model
 Terms and Definitions for Database Replication
 SymmetricDS is web-enabled, database independent, data synchronization/replication software. It uses web and database technologies to replicate tables between relational databases in near real time. The software was designed to scale for a large number of databases, work across low-bandwidth connections, and withstand periods of network outage. By using database triggers, SymmetricDS guarantees that data changes are captured and atomicity is preserved. Support for database vendors is provided through a Database Dialect layer, with implementations for MySQL, Oracle, SQL Server, PostgreSQL, DB2, Firebird, HSQLDB, H2, and Apache Derby included. Licensed under LGPL open source license.
 Daffodil Replicator is a Java tool for data synchronization, data migration, and data backup between various database servers. Daffodil Replicator works over standard JDBC driver and supports replication across heterogeneous databases. At present, it supports following databases: Microsoft SQL Server, Oracle, Daffodil database, DB2, Apache Derby, MySQL, and PostgreSQL. Daffodil Replicator is available in both enterprise (commercial) and open source (GPL-licensed) versions.
 DBReplicator Project Page
 DMOZ Open Directory Project - Database Replication Page
