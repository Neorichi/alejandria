---
type: Artículo de enciclopedia
title: HijackThis
description: HijackThis (abreviado como HJT) es una herramienta gratuita, creada por Merijn Bellekom y posteriormente vendida a Trend Micro, que ayuda al usuario a detectar software malicioso para los sistemas Microsoft Windows.
resource: https://es.wikipedia.org/wiki/HijackThis
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/HijackThis"}
license: CC BY-SA 4.0
id: eswiki-HijackThis
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# HijackThis

- **Nombre:** HijackThis
- **Desarrollador:** Trend Micro
- **Última versión:** 2.0.4
- **Fecha última versión:** 25 de marzo de 2010
- **Última versión prueba:** 2.0.5 beta
- **Fecha última versión prueba:** 11 de febrero de 2011
- **Sistema operativo:** Microsoft Windows
- **Género:** Antispyware
- **Licencia:** GNU General Public License
- **Idiomas:** Inglés

**HijackThis (abreviado como HJT)** es una herramienta gratuita, creada por Merijn Bellekom y posteriormente vendida a Trend Micro, que ayuda al usuario a detectar software malicioso para los sistemas Microsoft Windows.

El 28 de diciembre de 2011, cambió su licencia de Freeware a GNU General Public License liberando el código a la comunidad. Trend Micro ya no mantiene esta herramienta.

 Funcionamiento
Su potencial principal está en la capacidad de detectar rápidamente los métodos de *Browser Hijacking* que suelen utilizar software de tipo malware, en lugar de recurrir a una base de datos actualizada de virus y spyware como la mayoría de antivirus y software destinado a la eliminación de estos.

Hijackthis no autodetecta ni elimina spyware como popularmente se cree, sino que puede ayudar al usuario experto a detectarlo, siendo no recomendable el uso por usuarios inexpertos debido al riesgo de borrar software vital del sistema. El uso más común de ésta herramienta suele ser exportar una lista en texto plano de los resultados de análisis y escribirla en un foro de internet donde otros usuarios expertos darán su opinión.

Las más recientes versiones de HijackThis incluyen herramientas adicionales como un administrador de tareas, un editor del archivo hosts, y escáner de Alternate Data Streams.

 Áreas de búsqueda
HijackThis explora rápidamente el computador y crea una lista de diferencias con respecto a un ambiente libre de spyware. Esta lista incluye entre otras entradas:

 Hooks de búsqueda de URL
 Página de inicio del navegador y buscador usado
 Redirecciones en el archivo hosts
 Browser Helper Objects (BHO)
 Barra de herramientas del navegador
 Programas que arrancan al inicio
 Ajustes del panel de control
 Ajustes administrativos
 Ajustes del registro de Windows
 Elementos de menúes contextuales
 Botones de barra de herramientas
 Secuestradores del Winsock
 Opciones Avanzadas del Internet Explorer
 Plugins del Internet Explorer
 Secuestros de DefaultPrefix
 Secuestros de "Resetear Configuración web"
 Ajustes de la "Zona de confianza" y "Protocolo por defecto" del Internet Explorer
 Módulos ActiveX
 Hacks del DNS
 Protocolos adicionales y secuestradores de protocolos
 Secuestro de la hoja de estilo del usuario
 Subclaves de AppInit_DLL/Winlogon Notify
 Clave del registro de ShellServiceObjectDelayLoad
 Valor del registro del SharedTaskScheduler
 Servicios del NT, 2000, XP y 2003
 *Layered Service Providers*
 Servidor proxy

 Archivo log y resolución de problemas
HijackThis puede generar un archivo log de texto sencillo que detalla todas las entradas que encuentra.
La mayoría de estas entradas pueden ser desactivadas o eliminadas por HijackThis. Debe tenerse precaución cuando se usa la última opción, ya que, a excepción de una pequeña lista de entradas legítimas permitidas, HijackThis no discrimina entre los elementos legítimos y los no deseados, permitiendo así que un usuario inhabilite inintencionalmente programas importantes, causando posiblemente que el sistema o los periféricos dejen de funcionar correctamente. Sin embargo, HijackThis intentará crear respaldos de los archivos y de las entradas del registro que elimina, que se pueden usar para restaurar el sistema en el caso de un error.

Una forma común es postear el archivo log en un foro donde usuarios más experimentados ayudarán a descifrar las entradas que deberían ser eliminadas. También existen herramientas automáticas que analizan logs guardados y procuran proporcionar recomendaciones al usuario, o limpiar entradas automáticamente. Sin embargo, el uso de tales herramientas generalmente no es recomendado por los que se especializan en tratar manualmente de los logs de HijackThis, ellos consideran que las herramientas son potencialmente peligrosas para los usuarios sin experiencia, y que no son lo suficiente precisas y confiables para sustituir la consulta de un analista humano entrenado.

 Analizando los resultados del log
Cada línea o ítem comienza con una letra o un número, con las siguientes referencias:

 R0, R1, R2, R3: URL de páginas de inicio/búsqueda en el navegador IE (Internet Explorer).
 F0, F1, F2, F3: programas cargados a partir de ficheros *.ini (system.ini, win.ini...). Son maliciosos.
 N1, N2, N3, N4: URL de páginas de inicio/búsqueda en Netscape/Mozilla.
 O1: redirecciones mediante modificación del fichero HOSTS.
 O2: BHO (Browser Helper Object), o sea plugins para aumentar las funcionalidades del IE (Internet Explorer), pero también pueden ser spywares secuestradores.
 O3: *toolbars* (barras de herramientas) para IE.
 O4: aplicaciones que se cargan automáticamente en el inicio de Windows, desde claves en el registro o por estar en la carpeta de Inicio.
 O5: opciones de IE que no son visibles desde panel de control.
 O6: acceso restringido (por el administrador) a las opciones de IE.
 O7: acceso restringido (por el administrador) al Regedit.
 O8: ítems extra encontrados en el menú contextual de IE.
 O9: botones extra en la barra de herramientas de IE, así como ítems extra en el apartado Herramientas de IE (no incluidas en la instalación por defecto).
 O10: Winsock hijackers. MALICIOSO
 O11: adición de un grupo extra en las Opciones Avanzadas de IE (no por defecto).
 O12: plugins para IE.
 O13: hijack del prefijo por defecto en IE.
 O14: hijack de la configuración por defecto de IE.
 O15: sitios indeseados en la zona segura de IE. llamados también *trusted zone*. Malicioso
 O16: objetos ActiveX
 O17: hijack de dominio / Lop.com
 O18: protocolos extra / hijack de protocolos
 O19: hijack de la hoja de estilo del usuario.
 O20: valores de registro autoejecutables AppInit_DLLs. Los *notify* son maliciosos.
 O21: claves de registro autoejecutables ShellServiceObjectDelayLoad
 O22: claves de registro autoejecutables SharedTaskScheduler
 O23: servicios

Todos los *no file* o *file missing* indicados por el log pueden ser archivos corruptos, inutilizables, etc, y se pueden eliminar sin peligro aparente.

 Referencias

 Enlaces externos
 Foro de ayuda oficial de HijackThis en español
