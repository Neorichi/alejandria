---
type: Artículo de enciclopedia
title: USB Thief
description: USB Thief es un malware de tipo troyano diseñado para robar información de equipos bajo Microsoft Windows aislados de Internet.
resource: https://es.wikipedia.org/wiki/USB_Thief
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/USB_Thief"}
license: CC BY-SA 4.0
id: eswiki-USB_Thief
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# USB Thief

**USB Thief** es un malware de tipo troyano diseñado para robar información de equipos bajo Microsoft Windows aislados de Internet. Fue descubierto en marzo de 2016 por la empresa de seguridad ESET. Utiliza dispositivos de memoria USB para propagarse y no deja trazas en los equipos de donde roba información. Además cuenta con un mecanismo que impide copiar o ejecutar el malware usando herramientas estándar, de manera de dificultar su descubrimiento y estudio.

Normalmente se considera que al aislar una computadora de Internet, esta se mantiene segura. Sin embargo, al conectar una memoria USB a estos equipos, el malware se ejecuta automáticamente usando el modo Auto-run que por defecto se le asigna a los dispositivos USB en los sistemas Windows. Su objetivo es copiar en el dispositivo USB información extraída del equipo al cual se conecta sin dejar trazas de su ejecución en el propio equipo. Un examen posterior al equipo comprometido no muestra signos de la ejecución del malware.

A diferencia de otros programas de tipo malware, USB Thief no intenta reproducirse sino más bien se mantiene discretamente en el dispositivo esperando a que el atacante lo recupere y extraiga la información robada. En el reporte de seguridad no se mencionan mecanismos por los que este malware se comunique con otros equipos para transmitir la información robada. Para esparcir el malware el atacante puede dejar caído el dispositivo a la vista de una persona que al insertarlo en un equipo para ver su contenido expondrá el equipo al ataque del malware. Otras formas de consisten en regalar el dispositivo contaminado como elemento promocional en tiendas o ferias de tecnología.

Precedentes
Anteriormente se ha utilizado las memorias USB para atacar computadoras aisladas de internet. Fue el caso del gusano Stuxnet que supuestamente fue utilizado para atacar equipos aislados de internet en instalaciones nucleares iraníes. Ese gusano se autoreplicaba y era fácil de encontrar y estudiar. El malware Gauss superaba a Stuxnet al no replicarse y estar encriptado. Su código no ha sido desencriptado, de manera que no se conoce el tipo de ataque que ese malware portaba.

Medidas de protección
Como medida de protección contra este tipo de ataque se recomienda no utilizar memorias USB que no provengan de una fuente segura y utilizar algún antivirus actualizado que examine y desinfecte las memorias USB antes de usarlas.
Referencias
