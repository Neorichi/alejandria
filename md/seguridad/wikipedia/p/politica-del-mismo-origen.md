---
type: Artículo de enciclopedia
title: Política del mismo origen
description: En informática, la política del mismo origen (en inglés Same-origin policy o abreviado SOP) es una medida importante de seguridad para scripts en la parte cliente (casi siempre JavaScript).
resource: https://es.wikipedia.org/wiki/Política_del_mismo_origen
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Política_del_mismo_origen"}
license: CC BY-SA 4.0
id: eswiki-Política_del_mismo_origen
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Política del mismo origen

En informática, la **política del mismo origen** (en inglés *Same-origin policy* o abreviado **SOP**) es una medida importante de seguridad para scripts en la parte cliente (casi siempre JavaScript). Esta política viene del navegador web Netscape Navigator 2.0, y previene que un documento o script cargado en un "origen" pueda cargarse o modificar propiedades del documento desde un "origen" diferente. Se trata de uno de los conceptos de seguridad más importantes de los navegadores modernos.

En su aplicación más estricta, la política del mismo origen se extiende a todos los recursos de la página web, incluyendo hojas de estilo, imágenes y demás.

 Restricción de acceso
La filosofía de la política del mismo origen es sencilla: el navegador no debería confiar en contenido cargado desde sitios web arbitrarios. Las páginas web que se ejecutan en un sandbox no pueden conectar a recursos de otros orígenes. Sin esta protección, una página web maliciosa podría comprometer la confidencialidad y la integridad de otra página web.

En cuanto a recursos no programados del lado del cliente, sin su restricción el origen malicioso puede perfectamente rastrear al visitante mediante la huella digital de su navegador.

 Cómo superar la restricción de acceso
Es posible "superar" esta restricción firmando el script. Sin embargo, en la práctica, las firmas de scripts son muy poco usadas. Principalmente esto se debe a que el antiguo Internet Explorer no soportaba los scripts firmados, y no todo el mundo puede disponer de una firma digital ampliamente reconocida, especialmente los desarrolladores web.

Esto tampoco sería aplicable si se aplica un SOP estricto, con independencia del qué o el cómo de los recursos a cargar en la visita.

 Adopción por parte de los proveedores
Esta política es usada en los navegadores web modernos que soportan scripts en la parte cliente. El antiguo Internet explorer utilizaba un enfoque alternativo de zonas de seguridad además de la política del mismo origen ("o del mismo sitio"). Por defecto en Internet Explorer, los sitios web estaban restringidos a sus sitios de origen, pero el usuario puede elegir el permitir a sitios de intranet locales (o sitios que él ha confiado explícitamente) acceder a datos a través de otros dominios.

 Véase también
 Política de Seguridad de Contenidos (**Content Security Policy**, recomendación del W3C para las publicaciones web)

 Enlaces externos
 Comprobador en línea del CSP, al que se puede aplicar un SOP estricto para alcanzar la máxima puntuación.
 Política del mismo origen para JavaScript
 JavaScript Security: Same Origin (Mozilla)
 JavaScript Security in Communicator 4.x (PDF)
 Violating Same Origin Policy with XMLHttp: Cross-Browser Differences (SourceForge Wiki)
 Second page of an article on JavaScript Security (focuses on Same Origin issues)
