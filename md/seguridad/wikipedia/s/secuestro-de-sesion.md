---
type: Artículo de enciclopedia
title: Secuestro de sesión
description: "En informática, el secuestro de sesión, a veces también conocido como secuestro de cookie, es la explotación de una sesión informática válida —a veces también denominada clave de sesión— para obtener acceso no …"
resource: https://es.wikipedia.org/wiki/Secuestro_de_sesión
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Secuestro_de_sesión"}
license: CC BY-SA 4.0
id: eswiki-Secuestro_de_sesión
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Secuestro de sesión

En informática, el **secuestro de sesión**, a veces también conocido como **secuestro de cookie**, es la explotación de una sesión informática válida —a veces también denominada clave de sesión— para obtener acceso no autorizado a información o servicios en un sistema informático. En particular, suele referirse al robo de una cookie mágica utilizada para autenticar a un usuario a un servidor remoto. Es particularmente relevante para los desarrolladores web, ya que las cookies de HTTP utilizadas para mantener una sesión en muchos sitios web pueden ser fácilmente robadas por un atacante utilizando un ordenador de intermediario o al acceder a cookies guardadas en el ordenador de la víctima (véase Robo de cookies).

Un método popular utiliza paquetes IP encaminados por origen. Esto permite a un atacante en un punto B de la red que participe en una conversación entre *A* y *C* al favorecer que los paquetes IP pasen a través de la máquina *B*.

Si el encaminamiento basado en origen no es factible, el atacante puede recurrir al secuestro "ciego", por el cual adivina las respuestas de las dos máquinas. Así, el atacante puede enviar una orden, pero nunca puede ver la respuesta. Aun así, una orden común sería poner una contraseña que permita el acceso desde algún lugar más en la red.

Un atacante también puede estar entre *A* y *C* utilizando un programa de captura para mirar la conversación. Esto es conocido como ataque de intermediario.

 Historia de HTTP
Las versiones 0.8 y 0.9 del protocolo HTTP no tenían cookies y otras características necesarias para secuestros de sesión. La versión 0.9beta de Mosaic Netscape, liberada el 13 de octubre de 1994, permitía cookies.

Las versiones tempranas de HTTP 1.0 tenían algunas debilidades de seguridad relacionandas a secuestros de sesión, pero  eran difíciles de explotar debido a las ambigüedades de los servidores y navegadores HTTP 1.0 iniciales. Debido a que HTTP 1.0 ha sido designado como opción retrocompatible para HTTP 1.1 desde principios de los 2000 —y ya que los servidores HTTP 1.0 son todos esencialmente servidores HTTP 1.1 el problema de secuestro de sesión ha evolucionado a un riesgo de seguridad casi permanente.

La introducción de supercookies y otras características con el HTTP 1.1 modernizado ha permitido que el problema del secuestro se transforme en un problema de seguridad actual. La estandarización de estados de máquina de servidores web y navegadores ha contribuido a este problema de seguridad actual.

 Métodos
Hay cuatro métodos principales utilizados para perpetrar un secuestro de sesión. Estos son:
 **Fijación de sesión**, donde el atacante fija la identidad de sesión de un usuario a una conocida por él, por ejemplo enviando al usuario un correo electrónico con un enlace que contiene una identidad particular de sesión. El atacante ahora sólo tiene que esperar hasta que el usuario ingrese.
 **Secuestro del lado de la sesión**, , donde el atacante emplea un analizador de paquetes para rastrear el tráfico de red entre dos partes y así robar la cookie de sesión. Muchos sitios de web utilizan cifrado SSL en páginas de login para impedir a los atacantes ver la contraseña, pero no utiliza cifrado para el resto del sitio una vez el usuario se ha autenticado. Esto deja al atacante la posibilidad de leer el tráfico de red para interceptar todos los datos que se entregan al servidor, así como las páginas web visitadas por el cliente. Dado que estos datos incluyen la cookie de sesión, el atacante puede hacerse pasar por la víctima, incluso si su contraseña no está comprometida. Los Wi-Fi hotspots son particularmente vulnerables, ya que cualquiera que comparta la red generalmente será capaz de leer la mayoría del tráfico de web entre otros nodos y el punto de acceso.
 **Cross-site scripting**, donde el atacante engaña al ordenador del usuario para ejecutar código que es interpretado como confiable ya que parece pertenecer al servidor, permitiéndole obtener una copia de la cookie o llevar a cabo otras operaciones.
 El **malware** y los programas indeseados pueden utilizar un secuestro de navegador  para robar los archivos con los cookies de un navegador sin el conocimiento del usuario, y entonces realizar acciones (como instalar aplicaciones de Android) de forma silenciosa. Un atacante con el acceso físico sencillamente puede intentar robar la cookie de sesión, por ejemplo, obteniendo el archivo o los contenidos de la memoria del ordenador del usuario o del servidor.

 Ataques

 Firesheep
En octubre de 2010, una extensión de Mozilla Firefox llamada Firesheep fue liberada lo que hizo fácil a secuestradores de sesión que atacaran usuarios de Wi-Fi públicos sin encriptar. Muchos sitios web como Facebook, Twitter, y cualquiera que el usuario añadiera a sus preferencias permitían al usuario de Firesheep a acceder información privada de cookies fácilmente y amenazar la propiedad personal del usuario del Wi-Fi público. Unos meses más tarde, Facebook y Twitter respondieron ofreciendo (y más tarde exigiendo) HTTP Seguro en todos los accesos.

 Sniffer de WhatsApp
Una aplicación llamada "WhatsApp Sniffer" apareció en Google Play en mayo de 2012, y era capaz de mostrar mensajes de otros usuarios de WhatsApp conectados a la misma red que el usuario de la aplicación. En ese tiempo WhatsApp utilizaba infraestructura XMPP con encriptado, no comunicación de texto plano.

 DroidSheep
DroidSheep es una herramienta sencilla de Android para secuestro de sesión de web (*sidejacking*). Escucha  paquetes de HTTP enviados vía una conexión de red inalámbrica (802.11) y extrae la id de sesión de estos paquetes para reutilizarla. DroidSheep puede capturar las sesiones utilizando la librería libpcap y permite: redes abiertas (sin encriptar), redes encriptadas con WEP, y redes encriptadas con WPA/WPA2 (solo PSK). Este software utiliza libpcap y arpspoof. El apk fue liberado en Google Play pero fue retirada de ahí por Google.

 CookieCadger
Cookie Cadger es una herramienta de penetración de seguridad gráfica de código abierto hecha para interceptar y repetir peticiones concretas HTTP GET inseguras a un navegador. Cookie Cadger es una utilidad multiplataforma de código abierto basada en la herramienta Wireshark que se puede utilizar para monitorear redes Ethernet cableadas, Wi-Fi inseguro, o cargar un archivo de información de captura de paquetes para análisis off-line. Cookie Cadger ha sido usado para destacar las debilidades de sitios donde la juventud comparte información como Shutterfly (utilizados por la liga AYSO de fútbol) y TeamSnap.

 Prevención
Los métodos para impedir secuestro de sesión incluyen:
 Cifrar el tráfico de datos entre las partes utilizando SSL/TLS; en particular la clave de sesión (aun así idealmente todo tráfico para la sesión completa). Los sitios de banca y comercio electrónico confían ampliamente en esta técnica, porque impide completamente los ataques de tipo sniffer. Aun así, todavía es posible ejecutar otros tipos de secuestro de sesión. En respuesta, científicos de la Universidad Radboud de Nimega propusieron en 2013 una manera de impedir el secuestro de sesión correlacionando la sesión de aplicación con las credenciales SSL/TLS.
 Recurrir a una clave de sesión aleatoria y larga. Esto reduce el riesgo que un atacante sencillamente pueda adivinar una clave de sesión válida a través del ensayo y error o de ataques de fuerza bruta.
 Regenerar la ID de sesión después de un inicio de sesión exitoso. Esto impide la fijación de sesión porque el atacante no sabe la id de sesión del usuario después de que él/ella se ha registrado.
 Algunos servicios hacen controles secundarios de identidad del usuario. Para ejemplo, un servidor web podría comprobar que la dirección IP de cada petición que hizo el usuario coincida con la última utilizada durante la misma sesión. Esto, sin embargo, no evita ataques por parte de alguien que comparta la misma dirección IP, y podría frustrar a usuarios cuya dirección IP tienda a cambiar durante una sesión de navegación.
 Alternativamente, algunos servicios cambiarán el valor de la cookie con cada petición. Esto reduce dramáticamente la ventana en la cual un atacante puede operar y hace fácil identificar si ha tenido lugar un ataque, pero puede causar otros problemas técnicos (por ejemplo, dos peticiones legítimas, con muy poca diferencia de tiempo del mismo cliente pueden conducir a un error de control de token en el servidor).
 Los usuarios también pueden querer cerrar la sesión de los sitios web cada vez que terminan de usarlos. Aun así esto no protegerá contra ataques como Firesheep.

 Véase también
 Cross-site request forgery
 Cookie
 Ataque de predicción de secuencia TCP

 Referencias

 Enlaces externos
 Web oficial de ArpON
