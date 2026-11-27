---
type: Artículo de enciclopedia
title: Inseguridad informática
description: "La inseguridad informática es la falta o poca presencia de seguridad informática en un sistema operativo, aplicación, red o dispositivo, esto permite su demostración por hackers éticos (sombreros blancos) o su …"
resource: https://es.wikipedia.org/wiki/Inseguridad_informática
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Inseguridad_informática"}
license: CC BY-SA 4.0
id: eswiki-Inseguridad_informática
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Inseguridad informática

La **inseguridad informática** es la falta o poca presencia de seguridad informática en un sistema operativo, aplicación, red o dispositivo, esto permite su demostración por hackers éticos (sombreros blancos) o su explotación por hackers mal intencionados (sombreros negros).

 Vulnerabilidades
Según el tipo de vulnerabilidades informáticas, estas se pueden agrupar en función a su causa principal:
 Diseño:
 Debilidad en el diseño de protocolos empleados en las redes.
 Políticas de seguridad deficientes e inexistentes.
 Implementación:
 Errores de programación.
 Presencia de puertas traseras (backdoors) en software y hardware.
 Errores de código por descuido de fabricantes y desarrolladores.
 Uso:
 Configuración inadecuada de los sistemas informáticos.
 Falta de conocimientos de los usuarios y de los responsables de IT.
 Existencia de herramientas que faciliten los ataques.
 Limitación gubernamental de tecnología de seguridad.
 Vulnerabilidades de día cero: Es aquella vulnerabilidad que se sabe cómo explotar, pero no cómo solucionar y que mientras no se corrija, pondrá en riesgo los sistemas informáticos. Son la causa de los conocidos como ataques de día cero.

Aparte de esta agrupación, las vulnerabilidades informáticas también se pueden clasificar en cuatro tipos, según la gravedad del incidente:

 **Crítica:**  Las vulnerabilidades informáticas críticas son aquellas que permiten que las amenazas informáticas se produzcan y propaguen sin la intervención del usuario, es decir, pueden ejecutarse sin que el usuario tenga que hacer nada para ello.  Por ejemplo, la presencia de una puerta trasera en un software puede aprovecharse por un atacante que conozca su existencia y la use para llevar a cabo su ciberataque sin que el usuario sea consciente de ello.
 **Importante:**  Las vulnerabilidades informáticas importantes son aquellas que ponen en riesgo la confidencialidad, integridad y/o disponibilidad de los sistemas de información, incluidos también los recursos de procesamiento de los usuarios. Es decir, comprometen no solo los datos e información de los sistemas informáticos, también los recursos que emplean para funcionar adecuadamente. Que tu equipo acabe siendo parte de una botnet puede ser el resultado de este tipo de vulnerabilidad.
 **Moderada:**  Las vulnerabilidades moderadas son aquellas que presentan un menor riesgo para la información y los recursos de los sistemas informáticos, que tienen menos potencial para afectar a grandes cantidades de usuarios y que pueden mitigarse con la implantación de medidas de seguridad, como por ejemplo un sistema de seguridad perimetral informática.
 **Baja:**  Finalmente, las vulnerabilidades informáticas clasificadas como bajas son aquellas que apenas entrañan riesgos reales para los usuarios y que no suponen ninguna ventaja o punto de entrada aprovechable por el atacante.

 Vulnerabilidades comunes

 Abusos CGI
Son vulnerabilidades que pueden ser explotadas de forma remota mediante la ejecución de un script desde el navegador (generalmente por http) del atacante sobre el cgi-bin del servidor, esto permite el acceso y manejo de información restringida.

 Inyección de código

 Inyección SQL
Una inyección SQL es un ataque que permite ejecutar código arbitrario en una base de datos relacional. Mucho hackers aprovechan esto para poder ejecutar instrucciones GET en la base de datos, lo que permite obtener nombres de usuarios, contraseñas, etc.

 XSS (Cross Site Scripting)
Un **XSS** (Cross Site Scripting) es una vulnerabilidad provocada por la falta o error de validación en el código html, esto permite la inclusión de cualquier tipo de sintaxis html y logra comprometer la seguridad de la persona que accede a un exploit de XSS desde su navegador cuando este incluye algún scripts (VBS, JS) malicioso que pretende infectar su sistema operativo o secuestrar contraseñas, cookies, etc. Es también conocido como "Inyección HTML".

 Hacking

El **hacking** es el arte de la intrusión directa a un sistema informático ayudándose de alguna vulnerabilidad, sus intenciones varían desde demostrar dicha vulnerabilidad en un sistema operativo, aplicación, red o dispositivo para luego crear un parche que logre remendar esa situación, hasta explotar esa vulnerabilidad para fines perjudiciales para la víctima o beneficiosos para los intrusos.

 Hijacking

El *hijacking* (del inglés "secuestrar") consiste en ocupar una identidad obteniendo acceso no autorizado a un sistema, módem, cuenta (correo electrónico, banco, etc.) para poder falsificar la identidad de esta persona (autentificación).

 DoS y DDoS

Los ataques del tipo DoS (Denial of Service) y los ataques DDoS (Distributed Denial of Service) son utilizados generalmente para hacer flood en un servidor y algunas veces hasta logran efectuar un kernel panic en el sistema operativo del servidor.

 Spoofing

El **Spoofing** es una técnica del hacking que consiste en falsificar los paquetes enviados, para obtener acceso a un servidor, módem, o cualquier otro dispositivo.
En términos de seguridad de redes hace referencia al uso de técnicas de suplantación de identidad generalmente con usos maliciosos o de investigación.

**IP SPOOFING**
Suplantación de IP. Consiste básicamente en sustituir la dirección IP de origen de un paquete TCP/IP por otra dirección IP a la cual se desea suplantar. Esto se consigue generalmente gracias a programas destinados a ello y puede ser usado para cualquier protocolo dentro de TCP/IP como ICMP, UDP o TCP. Hay que tener en cuenta que las respuestas del host que reciba los paquetes irán dirigidas a la IP falsificada. Por ejemplo si enviamos un ping (paquete icmp "echo request") spoofeado, la respuesta será recibida por el host al que pertenece la IP legalmente. Hay que tener en cuenta que los routers actuales no admiten el envío de paquetes con IP origen no perteneciente a una de las redes que administra (los paquetes spoofeados no sobrepasarán el router).

 Ingeniería social

La **ingeniería social** consiste en la utilización de técnicas de índole psicológica, para lograr obtener información confidencial.

 Cracking

El **cracking** es un paradigma del hacking que consiste en saltar barreras impuestas por los sistemas de seguridad informática (criptografía, autentificación, validación). El cracking también consiste en la modificación de software compilado, agregándole funciones o eliminar las trabas como tiempo de uso (software trial).

 Ataque de fuerza bruta

 En criptografía

El **ataque de fuerza bruta** en criptografía consiste en descubrir la clave de un cifrado basándose en su algoritmo y en una clave similar: La fuerza bruta no puede romper claves modernas como RSA y AES entre otras.

 En autentificaciones

Un **ataque de fuerza bruta** en una autentificación consiste en realizar una gran cantidad de intentos de acceso, cuya contraseña es variada cada vez que es ingresada, siguiendo una lógica en particular, hasta agotar las opciones.

Véase también
Persistencia de datos
Malware
Seguridad informática
Exploit

 Referencias
