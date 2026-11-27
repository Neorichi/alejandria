---
type: Artículo de enciclopedia
title: Ophcrack
description: Ophcrack es una herramienta para crackear las contraseñas de Windows basada en las tablas Rainbow.
resource: https://es.wikipedia.org/wiki/Ophcrack
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ophcrack"}
license: CC BY-SA 4.0
id: eswiki-Ophcrack
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ophcrack

- **Nombre:** Ophcrack
- **Desarrollador:** Cedric TissieresPhilippe OechslinObjectif Sécurité
- **Ultima version:** 3.6.0
- **Lenguaje programación:** C++, C
- **Sistema operativo:** Microsoft Windows, Linux, Mac OS X
- **Idiomas:** inglés, español, francés, portugués, alemán y otros
- **Género:** Password cracking
- **Licencia:** GNU General Public License

**Ophcrack** es una herramienta para crackear las contraseñas de Windows basada en las tablas Rainbow. Es una implementación muy eficiente de las tablas Rainbow hecha por los inventores de este método. Viene con una Interfaz Gráfica de Usuario GTK+ y corre bajo Windows, Mac OS X (CPU Intel) y también en Linux.

 Opciones de ejecución
Permite la instalación en el mismo sistema operativo del cual se quiere averiguar la contraseña, pero su mayor potencial e interesante ejecutarlo desde otro sistema operativo instalado en otra partición, disco duro, o desde del Ophcrack LiveCD, se basa en una distribución Linux, que incluye además de las herramientas, un juego de tablas Rainbow.

El índice de éxito de acceso a claves de Ophcrack es del 99,9%, para claves que contengan números y letras, sean todas mayúsculas o minúsculas.

 Versiones

 Ophcrack 3.6.0

4 de junio de 2013

Ophcrack LiveCD 3.6.0 y la correspondiente incluyendo las nuevas tablas probabilísticas han sido puestos en libertad. Ophcrack precarga ha sido reescrito para arreglar los problemas encontrados en la versión 3.5.0. Apoyo de las tablas de probabilidad se mejoró también.

 Ophcrack 3.5.0

2 de mayo de 2013

Ophcrack versión 3.5.0 está lista para descargar. Esta versión incluye el soporte de las nuevas tablas probabilísticas. Estas tablas estarán disponibles en breve y mezclar patrones y Markov para acabar con las contraseñas más probables.

 Ophcrack 3.4.1

7 de marzo de 2013

Lanzamos la versión 3.4.1 de Ophcrack hoy. Se añade el apoyo de los cuadros Vista especiales XL y corrige algunos errores con Vista ocho mesas XL en Windows.

 Ophcrack 3.4.0

5 de mayo de 2012

Este nuevo LiveCD incluye la última versión de Ophcrack 3.4.0.
Está construido sobre SliTaz 4.0, la última versión de este gran LiveCD. Christophe Lincoln de SliTaz nos ayudó a realzar los guiones de particiones y detección de tablas. Una nueva interfaz ncurses también está disponible para ayudar a los usuarios buscar las tablas en otras unidades o interactúan con Ophcrack.
Por último, un LiveCD sin tablas ha sido puesto en libertad, así como para los usuarios que ya ha descargado o comprado tablas. El directorio que contiene los archivos de la tabla se deben colocar dentro de otro directorio llamado mesas para que Ophcrack para encontrar de forma automática.

27 de abril de 2012

Después de casi tres años sin noticias, aquí viene la versión 3.4.0 de Ophcrack.
Esta será probablemente la versión final en la rama 3.x.
Se añade el apoyo de la XP Flash próximo lanzamiento de Vista y ocho mesas XL. En Windows también añade el soporte de dumping los hashes través samdump2 en directo con NTFS bajo nivel de acceso a los archivos bloqueados.

 Ophcrack 3.3.1
 Soporte para Vista y siete
 Bkhive 1.1.0.
 Samdump2 1.1.0.
 Soporte para crackear hashes LM con caracteres alemanes.
 Facilidad de cambiar las tablas en el LiveCD.

 Características
 Se ejecuta en Windows / Unix, Linux, Mac OS X.
 Rompe hashes LM y NTLM.
 Tablas libres disponibles para Windows XP, vista y siete
 Módulo de fuerza bruta para contraseñas simples.
 Auditoría y el modo de exportación a CSV.
 Gráficos en tiempo real para analizar las contraseñas.
 Carga hashes desde SAM cifradas recuperadas desde una partición Windows, incluyendo Vista.
 Software libre y de código abierto (GPL).

 Ophcrack LiveCD

 Versión 1.1.4.

 Corre bajo Windows, Linux y Mac OS X (intel).
 Rompe hashes LM y NTLM.
 Tablas libres disponibles para hashes LM alfanuméricos.
 Carga hashes desde SAM local y SAM remota.
 Carga hashes desde SAM cifradas recuperadas desde una partición Windows, incluyendo Vista.

 Versión 2.3.1.
Posee las mismas características que el Ophcrack 3.3.1., ya que es su LiveCD.

 Se ejecuta en Windows / Unix, Linux, Mac OS X.
 Rompe hashes LM y NTLM.
 Tablas libres disponibles para Windows XP y Vista.
 Módulo de fuerza bruta para contraseñas simples.
 Auditoría y el modo de exportación a CSV.
 Gráficos en tiempo real para analizar las contraseñas.
 Carga hashes desde SAM cifradas recuperadas desde una partición Windows, incluyendo Vista.
 Software libre y de código abierto (GPL).

 Referencias

 Enlaces externos
 Ophcrack 3 (LiveCD 2) home page
 Alternative Ophcrack 3 (LiveCD 2) home page
 Ophcrack Online Demo - form to submit hashes and instantly crack passwords
 Ophcrack LiveCD 2 Tutorial
 Ophcrack home page at École polytechnique fédérale de Lausanne
  - Crackear contraseñas en plataformas Windows con Ophcrack
