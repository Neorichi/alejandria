---
type: Artículo de enciclopedia
title: RkUnhooker
description: Rootkit Unhooker también conocido como RkU y RkUnhooker.
resource: https://es.wikipedia.org/wiki/RkUnhooker
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/RkUnhooker"}
license: CC BY-SA 4.0
id: eswiki-RkUnhooker
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# RkUnhooker

- **Nombre:** Rootkit Unhooker
- **Autor:** UG North
- **Género:** Anti-rootkit

**Rootkit Unhooker** también conocido como **RkU** y **RkUnhooker**. Es un anti-rootkit (ARK), un software utilitario de uso individual para la detección de las intrusiones dentro del sistema operativo Microsoft Windows, un HIDS (Host Intrusion Detection System). Esta es una herramienta freeware puesta a disposición “tal cual es”, “tal cual está disponible” y por la cuenta y riesgo de sus usuarios. Lo esencial de su desarrollo se hizo a lo largo del segundo semestre 2006.

 Descripción

Según el *manual de usuario* traducido por "Mixel Adm", la ventana principal del programa contiene seis páginas:

 1. Detector/reparador de ganchos
 2. Detector de procesos ocultos
 3. Detector de drivers ocultos
 4. Detector de archivos ocultos
 5. Detector de ganchos de código
 6. Reporte

 Detector/reparador de Ganchos en la SSDT

La SSDT (System Service Descriptor Table) es el lugar en el que el sistema almacena punteros a las funciones principales del sistema. Algunos rootkits de modo núcleo usualmente utilizan la siguiente técnica – remplazan la dirección actual de la función en la tabla de direcciones (SSDT) con una función-manejadora propia. Algunos programas comerciales también utilizan esta técnica, por ejemplo Panda Antivirus interviene la función NtTerminateProcess para prevenir que los programas del antivirus sean terminados.

El firewall Agnitum Outpost hace lo mismo, además interviniendo NtWriteVirtualMemory, para proteger a los usuarios de técnicas de Malware conocidas como inyección de código. Programas de emulación de CD como Alcohol y Daemon Tools intervienen funciones relacionadas con el registro para engañar a los DRMs (Digital Right Managers o Administrador de Derechos Digitales).

RKU puede mostrar el estado de la SSDT, mostrando que funciones (también llamadas servicios en terminología de MS) están redireccionandas y además da la posibilidad restaurar su dirección original.

 Detector de procesos ocultos

El propósito general de un rootkit es ocultar su presencia del usuario, algunos rootkits sus ejecutable de la API, haciendo que las herramientas para el monitoreo de procesos como el administrador de tareas, process explorer, etc. No puedan ver dichos procesos. RKU está provisto de una forma avanzada de detección de procesos que permite la visualización de todos los procesos ejecutándose en el sistema.

 Detector de drivers ocultos

Los rootkits también ocultan sus propios drivers, para evitar que el usuario pueda eliminarlos del sistema. RKU está provisto de una parte principal que puede detectar drivers ocultos.

 Detector de archivos ocultos

Esconden sus archivos binarios (ejecutables), registros de texto de la API estándar de Microsoft Windows. Está provisto de código especial que puede detectar archivos ocultos, así como copiarlos/borrarlos.

 Detector de ganchos de código

Otra táctica usada por malware rootkits para esconder su presencia es ganchar las funciones de gestión del sistema de la API de Windows. RkU puede detectar este modo de ocultación, comparando la imagen actual y la integridad del código del sistema operativo dado. Adicionalmente checa los componentes principales del SO (como drivers de discos/red) Además RkU puede restaurar el código original, sobrescribiendo el código existente en memoria. En algunos casos esto puede llevar a un BSOD y resetear la PC.

 Tipos de ganchos detectados

 **Inline** – presentes en modo kernel y usuario. La aplicación o driver intruso, escribe su propio código en el cuerpo de la función, redirigiendo a su manejador. Este tipo de ganchos cambien puede ser aplicado a drivers que no exportan funcione, esto es llamado ganchado IRP inline.
 Dificultad de Detección - variada, desde media a muy difícil.
 **IAT** - presentes en modo kernel y usuario. La aplicación o driver incluso reemplaza la dirección de la función con una propia, parchando la tabla de importación (Import Table). Este tipo de ganchos son usados en su mayoría en modo usuario.
 Dificultad de detección - variada, desde muy fácil a fácil
 **Syscall** - la System Call (también llamada call gate) es una instrucción especial (o interrupción) usada por el sistema operativo para transferir llamadas del modo usuario al modo kernel. El intrus reemplaza la dirección actual del manejador, con una propia. Puede estar combinada con ganchos del tipo inline.
 Dificultad de Detección - variada, desde muy fácil a media.
