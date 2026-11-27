---
type: Artículo de enciclopedia
title: Nessus
description: Nessus es un programa de escaneo de vulnerabilidades en diversos sistemas operativos.
resource: https://es.wikipedia.org/wiki/Nessus
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nessus"}
license: CC BY-SA 4.0
id: eswiki-Nessus
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nessus

**Nessus** es un programa de escaneo de vulnerabilidades en diversos sistemas operativos. Consiste en un demonio o diablo, *nessusd*, que realiza el escaneo en el sistema objetivo, y *nessus*, el cliente (basado en consola o gráfico) que muestra el avance e informa sobre el estado de los escaneos. Desde consola *nessus* puede ser programado para hacer escaneos programados con cron.

En operación normal, *nessus* comienza escaneando los puertos con nmap o con su propio escáner de puertos para buscar puertos abiertos y después intentar varios exploits para atacarlo. Las pruebas de vulnerabilidad, disponibles como una larga lista de plugins, son escritos en **NASL** (*Nessus Attack Scripting Language*, Lenguaje de Scripting de Ataque Nessus por sus siglas en inglés), un lenguaje scripting optimizado para interacciones personalizadas en redes.

Opcionalmente, los resultados del escaneo pueden ser exportados como informes en varios formatos, como texto plano, XML, HTML, y LaTeX. Los resultados también pueden ser guardados en una base de conocimiento para referencia en futuros escaneos de vulnerabilidades.

Algunas de las pruebas de vulnerabilidades de Nessus pueden causar que los servicios o sistemas operativos se corrompan y caigan. El usuario puede evitar esto desactivando "unsafe test" (pruebas no seguras) antes de escanear.

Actualmente existen dos versiones: "Home" y "Work" Esta última de pago y sin restricciones.

 Historia
El proyecto Nessus comenzó en 1998, cuando Renaud Deraison quiso que la comunidad de Internet tuviese un escáner remoto de seguridad que fuese libre, aunque a día de hoy su licencia ha cambiado (se ha convertido en software privativo).

 Enlaces externos

 Página oficial de Nessus
 Comentarios relativos a los cambios en el programa Nessus
