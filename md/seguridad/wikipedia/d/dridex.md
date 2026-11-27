---
type: Artículo de enciclopedia
title: Dridex
description: Dridex es un malware especializado en el robo de credenciales bancarias que utiliza un botnet ya establecido para expandirse ejecutando ataques de tipo mando y control (C2).
resource: https://es.wikipedia.org/wiki/Dridex
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Dridex"}
license: CC BY-SA 4.0
id: eswiki-Dridex
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Dridex

**Dridex** es un *malware* especializado en el robo de credenciales bancarias que utiliza un botnet ya establecido para expandirse ejecutando ataques de tipo mando y control (C2).

Los blancos del ataque son usuarios de Windows que reciben un correo con un documento en Word o Excel con macros camufladas. Si el receptor del correo abre el documento anexo, se ejecutan macros que descargan silenciosamente el malware Dridex e infectan la computadora.

El objetivo primordial de este malware es robar información bancaria de los usuarios de máquinas infectadas para inmediatamente lanzar transacciones fraudulentas. Para obtener la información bancaria el *malware* instala un escucha de teclado y realiza ataques de tipo inyección web. Durante 2015, las pérdidas por causadas por este malware fueron estimadas en 20 millones de libras en el Reino Unido y en 10 millones de dólares en Estados Unidos. Hasta 2015 Se había detectado ataques de Dridex en más de 20 países que no incluyen a España ni a Hispanoamérica.

Ejemplo de mensaje
Los mensajes de correo utilizados invitan al usuario a abrir un documento anexo. Por ejemplo:

El documento anexo con un nombre parecido a *BACS33434.doc* supuestamente contendría los detalles de la transacción.

Arquitectura
El malware Dridex tiene cuatro componentes principales:
Loader - Encargado de descargar e instalar Dridex e iniciar la conexión a una red P2P.
Core - Realiza las funciones principales del malware: Robo de credenciales, ataque de tipo inyección web y descarga de módulos VNC y Backconnect.
VNC - Permite al atacante ver y controlar remotamente el equipo infectado.
Backconnect - Utiliza el equipo comprometido como túnel de datos hacia otras computadoras.

Esfuerzos para combatirlo
En 2015, en un esfuerzo conjunto de diferentes entes en Estados Unidos y el Reino Unido se logró penetrar la red de servidores P2P de Dridex y redirigirla hacia un sitio sumidero. Las investigaciones condujeron hacia un ciudadano moldavo sospechoso de manejar el *malware*. Sin embargo, este esfuerzo tuvo un corto efecto dado que la red de distribución se reorganizó rápidamente.
Distribución de un antivirus
A principios de 2016 se confirmó que sorpresivamente, Dridex está distribuyendo e instalando el antivirus gratuito de la empresa Avira, capaz de detectar y erradicar a Dridex. Un representante de la empresa indicó que ellos no están involucrados en esto. Se sospecha que un hacker de sombrero negro habría discretamente penetrado la red de distribución de Dridex y cambiado su configuración para distribuir el antivirus. Otra hipótesis es que los manejadores del virus quisieron limpiar las máquinas infectadas de otros virus (como ya se ha hecho en otros ataques) pero que algo salió mal.

Referencias
