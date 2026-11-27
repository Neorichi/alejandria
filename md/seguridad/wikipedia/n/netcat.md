---
type: Artículo de enciclopedia
title: Netcat
description: "Netcat es una herramienta de red que permite a través de intérprete de comandos y con una sintaxis sencilla abrir puertos TCP/UDP en un HOST (quedando netcat a la escucha), asociar una shell a un puerto en concreto …"
resource: https://es.wikipedia.org/wiki/Netcat
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Netcat"}
license: CC BY-SA 4.0
id: eswiki-Netcat
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Netcat

- **Nombre:** netcat
- **Última versión:** 0.7.1
- **Fecha última versión:** 10 de enero de 2004
- **Sistema operativo:** GNU/Linux Unix Windows
- **Género:** Utilidad de red
- **Licencia:** GNU GPL

**Netcat** es una herramienta de red que permite a través de intérprete de comandos y con una sintaxis sencilla abrir puertos TCP/UDP en un HOST (quedando netcat a la escucha), asociar una shell a un puerto en concreto (para conectarse por ejemplo a MS-DOS o al intérprete bash de Linux remotamente) y forzar conexiones UDP/TCP (útil por ejemplo para realizar rastreos de puertos o realizar transferencias de archivos bit a bit entre dos equipos). Fue originalmente desarrollada por Hobbit en 1996 y liberada bajo una licencia de software libre permisiva (no copyleft, similar a BSD, MIT) para UNIX. Posteriormente fue portada a Windows y Mac OS X entre otras plataformas. Existen muchos forks de esta herramienta que añaden características nuevas como GNU Netcat o Cryptcat.

Entre sus múltiples aplicaciones, es frecuente la depuración de aplicaciones de red. También es utilizada a menudo para abrir puertas traseras en un sistema.

 Funcionamiento básico
La forma más básica de operar de netcat consiste en:
 Crear un socket para conectarse a un servidor (o bien para hacer de servidor)
 Enviar todo lo que entre por la entrada estándar por el socket
 Sacar por la salida estándar todo lo recibido por el socket

 Parámetros
A continuación se listan algunos de los parámetros más usados con Netcat:
 -l: Indica que Netcat abre el puerto para Escucha (Listen): Acepta una **única** conexión de un Cliente y se cierra.
 -p: Especifica el puerto.
 -k: Fuerza a que el puerto permanezca abierto tras haber recibido una Conexión. Se usa con el parámetro -l y permite infinitas Conexiones.
 -u: El puerto abierto se abre como UDP, en vez de TCP que es la opción por defecto.
 -v: Muestra información de la conexión.
 -t: Las respuestas son compatibles para sesiones de Telnet.
 -q *segundos*: Tras haber recibido el EOF de la Entrada de datos, espera los segundos indicados para enviarla.
 -i *segundos*: Especifica un delay (retraso) de tiempo para el envío o recepción de las líneas de texto.

 Ejemplos
Abrir nueva conexión al puerto 25 (como telnet):

nc mail.server.net 25.

Abrir una conexión para enviar un Archivo de manera RAW (Binario) a un Cliente:

cat ARCHIVO | nc -l PUERTO

Abrir una conexión y volcar la Información recibida en ARCHIVO (Cliente del Ejemplo anterior):

nc HOST PUERTO > ARCHIVO

Simular una Respuesta HTTP (austera) a un Cliente que se conecta con un navegador web (https://web.archive.org/web/19961229112017/http://localhost/):

echo -en "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n\Hola Mundo" | nc -l -p 80

 Véase también
 Cmd

 Enlaces externos
 netcat en SourceForge
 Sitio web oficial de GNU Netcat
 Netcat, la navaja suiza de TCP/IP
 Netcat para Windows Espejo
