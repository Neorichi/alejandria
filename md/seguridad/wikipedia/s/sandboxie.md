---
type: Artículo de enciclopedia
title: Sandboxie
description: "Sandboxie es un software de tipo sandbox (textualmente caja de arena) para Microsoft Windows, parecido a un sistema de virtualización por «aislamiento»."
resource: https://es.wikipedia.org/wiki/Sandboxie
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sandboxie"}
license: CC BY-SA 4.0
id: eswiki-Sandboxie
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sandboxie

- **Nombre:** Sandboxie
- **Desarrollador:** Ronen Tzur EE. UU.
- **Última versión:** 5.33.1
- **Sistema operativo:** Microsoft Windows
- **Género:** Virtualización por «aislamiento»
- **Licencia:** Freeware (End-user Licence Agreement)

**Sandboxie** es un software de tipo *sandbox* (textualmente *caja de arena*) para Microsoft Windows, parecido a un sistema de virtualización por «aislamiento». Este freeware crea un «contenedor» dentro del cual los programas de aplicación se ejecutan de forma segura.

 Descripción
Sandboxie actúa de forma previa a las infecciones en las computadoras equipadas con Windows. Este software aísla dentro de su contenedor los archivos de navegación y los de funcionamiento de las aplicaciones que controla.

Los programas (navegadores y otros) ejecutados por medio de Sandboxie y los archivos descargados están encerrados en unas réplicas de los directorios normalmente utilizados. Además, Sandboxie hace una copia de una parte del registro de Windows para proteger el original contra las inserciones malévolas de claves y valores.

Así, cuando un programa se está ejecutando dentro de Sandboxie, las modificaciones efectuadas no son efectivas en los archivos auténticos, y los parásitos y los bugs encerrados en el interior del contenedor no alteran el sistema operativo. De la misma manera, los malwares de toda clase quedan acantonados dentro de la *bandeja de arena*. Las novedades o los cambios de interés se deberán registrar fuera del sandbox después de un control de validez.

Además, Sandboxie evita desde la zona que controla toda inyección en el kernel de Windows (driver, DLL). Así, actúa de cierta manera (pero a un nivel distinto) como el sistema PatchGuard de Windows Vista 64 bits impidiendo el funcionamiento de todo software en modo supervisor, sea malicioso o no.

Bastará con vaciar el contenido del sandbox antes de acabar una sesión de utilización del ordenador para que todos los rastros inútiles o peligrosos aislados en él sean definitivamente borrados del disco: malwares, histórica y contenido del caché de navegación, etc.

 Enlaces externos
 (en inglés) Sitio web oficial
 (en francés) Sandboxie - descriptivo, uso, pruebas por "Txon".
 Funcionamiento de Sandboxie (ingeniería inversa)
 Sandboxie, evita que el navegador afecte al resto del sistema por Sacha Fuentes
 (en italiano) Navigare su Internet in tutta sicurezza con Sandboxie por Gianni Amato
