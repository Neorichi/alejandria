---
type: Artículo de enciclopedia
title: Bitfrost
description: Bitfrost es la plataforma de seguridad de la OLPC XO-1, una laptop de bajo costo destinada a niños de países en desarrollo, y desarrollada por el proyecto One Laptop Per Child (OLPC) project.
resource: https://es.wikipedia.org/wiki/Bitfrost
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Bitfrost"}
license: CC BY-SA 4.0
id: eswiki-Bitfrost
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Bitfrost

- **Nombre:** Bitfrost
- **Desarrollador:** Ivan Krstić
- **Sistema operativo:** Linux
- **Género:** Privacidad, Antivirus
- **Licencia:** GNU General Public License

**Bitfrost** es la plataforma de seguridad de la OLPC XO-1, una laptop de bajo costo destinada a niños de países en desarrollo, y desarrollada por el proyecto One Laptop Per Child (OLPC) project. El principal arquitecto de Bitfrost es Ivan Krstić. La primera especificación pública fue publicada en febrero de 2007.

 Arquitectura de Bitfrost
 Contraseñas
No se requiere ninguna contraseña para acceder a la computadora.

 Sistema de derechos
Cualquier programa, al momento de ser instalado, requiere ciertos conjuntos de derechos, por ejemplo "acceder a la cámara", o "acceder a internet". El sistema realiza un seguimiento de estos derechos, y el programa es luego ejecutado en un ambiente en el cual sólo los recursos requeridos están disponibles. Esto está implementado mediante una máquina virtual contenedora completamente desarrollada.

Por defecto, el sistema no permite ciertas combinaciones de derechos; por ejemplo, un programa no tendría permisos para acceder a la cámara y acceder a internet a la vez. Cualquiera puede escribir y distribuir programas que requieran combinaciones de derechos permitidas. Los programas que requieran combinaciones de derechos no aprobadas necesitan una firma criptográfica de alguna autoridad. El usuario de la laptop puede utilizar el panel de seguridad incluido para otorgar derechos adicionales a cualquier aplicación.

 Modificando el sistema
Los usuarios pueden realizar modificaciones al sistema operativo de la laptop, una versión especial de Red Hat Linux corriendo la nueva interfaz gráfica Sugar, y operando sobre LinuxBIOS y Open Firmware. El sistema original permanece disponible en segundo plano y puede ser restaurado.

Adquiriendo una clave de desarrollador de una ubicación central, un usuario puede incluso modificar la copia de resguardo del sistema y varios aspectos de la BIOS. Dicha clave de desarrollador es entregada sólo después de un período de espera (para que el robo de la máquina pueda ser reportado a tiempo) y es válida para una sola máquina en particular.

 Contratos antirrobo
Las laptops solicitan un nuevo "contrato" a un servidor de la red central una vez al día. Estos contratos llegan con una fecha de vencimiento (normalmente un mes), y la laptop deja de funcionar si todos sus contratos han expirado. Los contratos también pueden ser otorgados por un servidor en la escuela, o mediante un dispositivo USB. Aquellas laptops que hayan sido reportadas como robadas no pueden obtener un nuevo contrato.

El país que adquiere la laptop puede determinar si se utiliza este sistema de contratos, y seleccionar el tiempo de vencimiento de los mismos.

 Micrófono y cámara
El micrófono y la cámara incluidos en la laptop se encuentran conectados directamente a un LED, así el usuario puede saber en todo momento si están encendidos. Esto no puede ser deshabilitado por software.

 Trivia
 La especificación misma menciona que el nombre "Bitfrost" es un juego de palabras con Bitfrost, el concepto de la Mitología nórdica que describe un puente entre el mundo de los mortales y el reino de los dioses. De acuerdo con la Edda prosaica, el puente fue construido para ser fuerte, pero que finalmente sería roto; el puente es un reconocimiento a la idea de que no existe cosa tal como el sistema de seguridad perfecto.

 Referencias

 Enlaces externos
 (en) OLPC Wiki: Bitfrost
 (en) Especificación de Bitfrost, versión Draft-19 - publicación 1, 7 de febrero de 2007
 (en) High Security for $100 Laptop, Wired News, 7 de febrero de 2007
 (en) Making antivirus software obsolete - Technology Review magazine recognized Ivan Krstić, Bitfrost's main architect, as one of the world's top innovators under the age of 35 (Krstić was 21 at the time of publication) for his work on the system.
