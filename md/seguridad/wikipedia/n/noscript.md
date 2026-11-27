---
type: Artículo de enciclopedia
title: NoScript
description: NoScript (o NoScript Security Suite) es una extensión libre y de código abierto para Mozilla Firefox, SeaMonkey, Flock y navegadores web basados en Mozilla Firefox y Google Chrome.
resource: https://es.wikipedia.org/wiki/NoScript
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/NoScript"}
license: CC BY-SA 4.0
id: eswiki-NoScript
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# NoScript

- **Nombre:** NoScript
- **Desarrollador:** Giorgio Maone
- **Última versión:** 13.6.23
- **Lenguaje programación:** CSS, JavaScript y XUL
- **Sistema operativo:** Multiplataforma
- **Género:** Extensiones de Mozilla
- **Licencia:** GPLv3+
- **Idiomas:** Multilingüe

**NoScript** (o **NoScript Security Suite**) es una extensión libre y de código abierto para Mozilla Firefox, SeaMonkey, Flock y navegadores web basados en Mozilla Firefox y Google Chrome. NoScript bloquea la ejecución de JavaScript, Java, Flash, Silverlight, y otros complementos y contenidos de scripts. NoScript tiene una lista blanca para permitir la ejecución de guiones informáticos de ciertos sitios. También ofrece contramedidas específicas contra los ataques de seguridad.

 Características
 Seguridad y uso
Después de la instalación en Firefox, es bloqueado por defecto el contenido ejecutable JavaScript, Java, Flash, Silverlight, y otros contenidos "activos", bajo la asunción que los sitios web maliciosos pueden usar estas tecnologías en formas maliciosas. El usuario puede permitir que el contenido activo pueda ser ejecutado en sitios web de confianza, dando un permiso explícito.

NoScript toma la forma de un icono en la barra de herramientas o en la barra de estado del Firefox. Muestra cada sitio cuyo contenido está siendo bloqueado o permitido para la página actual que se está viendo, con opciones para permitir el contenido actualmente bloqueado o para prohibir el contenido actualmente permitido.

NoScript también provee defensas adicionales contra ataques en Internet tales como XSS, CSRF, Clickjacking, ataque Man-in-the-middle y DNS rebinding, con contramedidas específicas que trabajan independientemente del bloqueo de script.

 Emparejado de sitios y lista blanca
Los scripts (y otros elementos bloqueables) son permitidos o bloqueados basado en la fuente de donde el script es leído - que con frecuencia no es idéntica a la URL mostrada en el campo de la dirección de la página web. Esto es porque muchas páginas web leen elementos tales como iframes, hojas de estilo (stylesheets), scripts y reproductores embebidos desde sitios remotos. Cuando una página web incluye scripts y otros elementos bloqueables de muchas fuentes, el usuario puede especificar una política de bloqueo tanto para la dirección principal y como para cada una de las fuentes separadamente.

Una vez que cualquier fuente es marcada como confiable, NoScript la tratará como confiable incluso si es cargada indirectamente por páginas web o scripts originados desde otros dominios.

Para cada fuente, la dirección, el dominio, o el dominio padre exactos pueden ser especificados. Permitiendo un dominio (ej. mozilla.org), hace que todos sus subdominios sean permitidos implícitamente (ej. www.mozilla.org, addons.mozilla.org y así sucesivamente) con cada posible protocolo (ej. HTTP y HTTPS). Permitiendo una dirección (protocolo://host ej. https://www.mozilla.org), hace que sus subdirectorios sean permitidos (ej. https://www.mozilla.org/firefox y https://www.mozilla.org/thunderbird), pero no los parientes del dominio ni sus hermanos. Por lo tanto, mozilla.org y addons.mozilla.org no serán permitidos automáticamente.

 Lista negra de no confianza
Los sitios también se pueden poner en la lista negra de NoScript (la lista negra contiene los sitios en que no se confía y en donde se bloqueará automáticamente el contenido de scripts, etc).

 Protección Anti-XSS
El 11 de abril de 2007 fue lanzado al público el NoScript en su versión 1.1.4.7, introduciendo una protección del lado del cliente contra el cross-site scripting (XSS) de tipo 0 y de tipo 1. Cuando un sitio web intenta inyectar código HTML o Javascript dentro de un sitio diferente, NoScript filtra la solicitud maliciosa, neutralizando su carga peligrosa.

 Premio
NoScript fue nombrado por PC World como uno de los 100 mejores productos de 2006, estando en el puesto #52.

 Referencias

 Enlaces externos

 Repositorio oficial en GitHub
 NoScript en addons.mozilla.org
