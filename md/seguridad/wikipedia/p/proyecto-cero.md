---
type: Artículo de enciclopedia
title: Proyecto Cero
description: Proyecto Cero es el nombre de un equipo de analistas de seguridad empleados por Google encargado de encontrar ataques de día cero.
resource: https://es.wikipedia.org/wiki/Proyecto_Cero
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Proyecto_Cero"}
license: CC BY-SA 4.0
id: eswiki-Proyecto_Cero
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Proyecto Cero

**Proyecto Cero** es el nombre de un equipo de analistas de seguridad empleados por Google encargado de encontrar ataques de día cero. Su presentación tuvo lugar el 15 de julio de 2014.

 Historia
Después de encontrar una serie de fallos en el *software* utilizado por muchos usuarios finales mientras investigaban otros problemas, como la vulnerabilidad crítica Heartbleed, Google decidió formar un equipo dedicado a tiempo completo a encontrar dichas vulnerabilidades, no solo en el *software* de Google, sino también en cualquier *software* utilizado por sus usuarios.

El nuevo grupo de Google se anunció el 15 de julio de 2014 en el blog de seguridad de Google. Si bien la idea del Proyecto Cero se remonta a 2010, su creación se motiva por la tendencia más amplia de las iniciativas de contravigilancia de Google tras los resultados de las revelaciones sobre la red de vigilancia mundial hechas por Edward Snowden. El equipo estaba anteriormente encabezado por Chris Evans, anteriormente director del equipo de seguridad del navegador Chrome, que posteriormente se unió a Tesla Motors. Otros miembros notables incluyen investigadores de seguridad como Ben Hawkes, Ian Beer y Tavis Ormandy.

 Búsqueda y reporte de errores
Los errores encontrados por el equipo del Proyecto Cero son reportados al fabricante y sólo se hacen públicamente visibles una vez que un parche ha sido liberado. O si han pasado 90 días sin que un parche haya sido liberado.  La fecha límite de 90 días es la forma en que Google implementa la revelación responsable, dando a las empresas de software 90 días para solucionar un problema antes de informar al público para que los propios usuarios puedan tomar las medidas necesarias para evitar ataques.

 Miembros notables
 Ben Hawkes
 Tavis Ormandy
 Ian Beer
 Jann Horn

 Miembros anteriores
 George Hotz
 Chris Evans
 Mate Tait
 Steven Vittitoe

 Descubrimientos notables
El 30 de septiembre de 2014 Google detectó un fallo de seguridad en el sistema de Windows 8.1 llamado *NtApphelpCacheControl*, que permite a un usuario normal obtener acceso de administrador. Microsoft fue notificada del problema inmediatamente, pero no lo solucionó en un plazo de 90 días, lo que implicó que la información sobre el fallo se pusiera a disposición del público el 29 de diciembre de 2014. La liberación del fallo al público provocó la respuesta de Microsoft asegurando que ya estaban trabajando en el problema.

El 19 de febrero de 2017 Google descubrió una falla dentro de los *proxies* inversos de Cloudflare, lo que provocó que los servidores en la frontera de su red —los que enlazan con internet— ejecutaran código más allá del final de un búfer y devolvieran contenido de memoria con información privada como *cookies* HTTP, tókenes de autenticación, cuerpos POST de HTTP y otros datos sensibles. Algunos de estos datos fueron almacenados en caché por los motores de búsqueda. Un miembro del equipo de Proyecto Cero se refirió a esta falla como Cloudbleed.

El 27 de marzo de 2017 Tavis Ormandy del Proyecto Cero descubrió una vulnerabilidad en el popular gestor de contraseñas LastPass. El 31 de marzo de 2017, LastPass anunció que habían solucionado el problema.

El Proyecto Cero estuvo involucrado en el descubrimiento de las vulnerabilidades Meltdown y Spectre que afectan a la inmensa mayoría de las CPU modernas, las cuales fueron descubiertas a mediados de 2017 de manera confidencial, y hechas públicas a principios de enero de 2018. Fueron descubiertas por Jann Horn, de Proyecto Cero, de manera independiente a los otros investigadores que informaron sobre estas fallas de seguridad. Estaba previsto inicialmente que se hicieran públicas el 9 de enero de 2018 distribuyendo en ese momento los parches de seguridad, pero tuvieron que adelantar el anuncio debido a las crecientes especulaciones e hipótesis sobre su alcance y severidad.

 Referencias

 Enlaces externos
 Blog oficial
 Base de datos de detectó vulnerabilidades
 Lista de las vulnerabilidades encontradas por Google antes de empezar el "Proyecto Cero"
