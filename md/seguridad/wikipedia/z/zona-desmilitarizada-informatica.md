---
type: Artículo de enciclopedia
title: Zona desmilitarizada (informática)
description: "En seguridad informática, una zona desmilitarizada (conocida también como DMZ, sigla en inglés de demilitarized zone) o red perimetral es una red local que se ubica entre la red interna de una organización y una red …"
resource: https://es.wikipedia.org/wiki/Zona_desmilitarizada_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Zona_desmilitarizada_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Zona_desmilitarizada_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Zona desmilitarizada (informática)

En seguridad informática, una **zona desmilitarizada** (conocida también como **DMZ**, sigla en inglés de *demilitarized zone*) o **red perimetral** es una red local que se ubica entre la red interna de una organización y una red externa, generalmente en Internet. El objetivo de una DMZ es que se permitan las conexiones desde la red externa a la DMZ, pero que *en general* no se permitan las conexiones desde la *DMZ* a la red interna (los equipos de la DMZ no deben conectarse directamente con la red interna). Esto permite que los equipos de la DMZ puedan dar servicios a la red externa, a la vez que protegen la red interna en el caso de que unos intrusos comprometan la seguridad de los equipos situados en la zona desmilitarizada. Para cualquiera de la red externa que quiera conectarse ilegalmente a la red interna, la zona desmilitarizada se convierte en un callejón sin salida.

La *DMZ* se usa habitualmente para ubicar servidores que es necesario que sean accedidos desde fuera, como servidores de correo electrónico, web y DNS. Y son precisamente estos servicios alojados en estos servidores los únicos que pueden establecer tráfico de datos entre la DMZ y la red interna, como una conexión de datos entre un servidor web y una base de datos protegida situada en la red interna.

Las conexiones que se realizan desde la red externa hacia la DMZ se controlan generalmente utilizando *port address translation* (PAT).

Una DMZ se crea a menudo a través de las opciones de configuración del cortafuegos, donde cada red se conecta a un puerto distinto de este. Esta configuración se llama cortafuegos en trípode (three-legged firewall).

Obsérvese que los enrutadores domésticos son llamados *DMZ host*, aunque esa no es una definición correcta de zona desmilitarizada.

 Origen del término
El término *zona desmilitarizada*, aplicado a la seguridad informática procede probablemente de la franja de terreno neutral que separa a los países inmersos en un conflicto bélico. Es una reminiscencia de la guerra de Corea, aún vigente y en tregua desde 1953. Paradójicamente, a pesar de que esta zona desmilitarizada es terreno neutral, es una de las más peligrosas del planeta, pues la franja no pertenece formalmente a ningún país, y cualquier inmersión en ella causará fuego de ambos bandos.

 DMZ perimetral

En el caso de un enrutador de uso doméstico, el DMZ perimetral se refiere a la dirección IP que tiene una computadora para la que un enrutador deje todos los puertos abiertos, excepto aquellos que estén explícitamente definidos en la sección NAT del enrutador. Es configurable en varios enrutadores y se puede habilitar y deshabilitar.

Con ello se persigue conseguir superar limitaciones para conectarse con cierto tipo de programas, aunque es un riesgo muy grande de seguridad que conviene tener solventado instalando un cortafuegos por software en el ordenador que tiene dicha IP en modo DMZ.

Para evitar riesgos es mejor no habilitar esta opción y usar las tablas NAT del enrutador y abrir únicamente los puertos que son necesarios.

 *Dual firewall*
Un planteamiento más seguro es usar dos cortafuegos, esta configuración ayuda a prevenir el acceso desde la red externa a la interna. Este tipo de configuración también es llamado cortafuegos de subred monitorizada (*screened-subnet firewall*).
Se usan dos cortafuegos para crear la DMZ. El primero (llamado *"front-end"*) debe permitir el tráfico únicamente del exterior a la DMZ. El segundo (llamado *"back-end"*) permite el tráfico únicamente desde la red interna a la DMZ.

 Véase también
 *Bastion host*

 Referencias
