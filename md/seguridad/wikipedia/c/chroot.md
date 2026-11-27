---
type: Artículo de enciclopedia
title: Chroot
description: chroot en los sistemas operativos derivados de Unix, es una operación que invoca un proceso, cambiando para este y sus hijos el directorio raíz del sistema.
resource: https://es.wikipedia.org/wiki/Chroot
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Chroot"}
license: CC BY-SA 4.0
id: eswiki-Chroot
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Chroot

**chroot** en los sistemas operativos derivados de Unix, es una operación que invoca un proceso, cambiando para este y sus hijos el directorio raíz del sistema. "chroot" puede referirse a la llamada de sistema chroot(2) o al programa ejecutable chroot(8). Comúnmente, el entorno virtual creado por chroot a partir de la nueva raíz del sistema se conoce como "jaula chroot".

El sistema chroot fue introducido por Bill Joy el 18 de marzo de 1982 (17 meses antes de que BSD 4.2 fuera publicado) para probar su sistema de instalación y construcción.

Al usar "chroot" para invocar un proceso, se impedirá al mismo y a sus procesos hijos acceder por su nombre a ningún fichero que esté por encima del nuevo directorio raíz. Esto es entendido a menudo como un dispositivo de seguridad, ya que en teoría crea una zona segura para ejecutar un programa que provoca desconfianza, no está probado, o de alguna forma puede presentar un comportamiento peligroso para la integridad del sistema. Sin embargo, cabe señalar que las jaulas chroot no son tan seguras como otro tipo de jaulas o la virtualización.

Debido a que los programas esperan encontrar en lugares determinados su espacio de almacenamiento, los archivos de configuración o sus bibliotecas de enlace dinámico, entre otros, preparar una jaula chroot implica también incluir dichos recursos dentro de ella.

Los programas tienen permitido llevarse descriptores de archivos abiertos (sean archivos físicos, tuberías, o conexiones de red) dentro de la jaula, lo cual puede simplificar el diseño haciendo innecesario dejar archivos funcionales dentro del directorio chroot. Esto también funciona como un sistema de capacidades simple, en el cual, al programa se le otorga acceso explícito a los recursos externos del chroot basado en los descriptores que puede llevar a su interior.
 Usos
Las jaulas chroot se usan para crear y mantener una copia virtual separada del sistema operativo en un directorio del mismo. Esto puede ser útil para:
 **Pruebas y desarrollo:** Se puede crear un área de prueba para un programa cuando es arriesgado usar un sistema en producción directamente.
 **Control de dependencia:** Los programas pueden ser desarrollados, construidos y puestos a prueba solo con las dependencias esperadas. Esto puede prevenir algunas formas de ligado corrupto que surgen cuando los desarrolladores construyen proyectos con diferentes bibliotecas instaladas.
 **Compatibilidad:** El software heredado o que usa una diferente interfaz binaria de aplicación, algunas veces debe de ejecutarse por separado, ya que las bibliotecas que lo soportan o los archivos de datos podrían, de otra forma, entrar en conflicto de nombres o enlaces con los del sistema contenedor de la jaula.
 Referencias
McGrath, Roland. «Páginas 2 y 8 del manual de sistema de chroot».

 Enlaces externos
