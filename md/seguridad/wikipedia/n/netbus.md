---
type: Artículo de enciclopedia
title: NetBus
description: "NetBus es un programa utilizado para el control de una forma remota de sistemas informáticos Microsoft Windows a través de una red. Fue creado en 1998 y ha sido muy controvertido por su potencial de ser utilizado como …"
resource: https://es.wikipedia.org/wiki/NetBus
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/NetBus"}
license: CC BY-SA 4.0
id: eswiki-NetBus
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# NetBus

- **Nombre:** NetBus
- **Desarrollador:** Carl-Fredrik Neikter
- **Lanzamiento:** Marzo de 1998
- **Última versión:** 2.01 Pro
- **Sistema operativo:** Windows
- **Licencia:** Shareware

**NetBus** es un programa utilizado para el control de una forma remota de sistemas informáticos Microsoft Windows a través de una red. Fue creado en 1998 y ha sido muy controvertido por su potencial de ser utilizado como una puerta trasera.

 Historia
NetBus se escribió en Delphi por Carl-Fredrik Neikter, un programador sueco, en marzo de 1998. Entró en circulación antes que Back Orifice, fuese liberado en agosto de 1998. El autor afirmó que el programa estaba destinado a ser usado para bromas, no para irrumpir ilegalmente en los sistemas informáticos. Traducido del sueco, el nombre significa "NetPrank". (broma en red)

 Características
Existen dos componentes para la arquitectura cliente-servidor. El servidor debe ser instalado y ejecutado en el equipo que quiere ser controlado a distancia, el tamaño de archivo es de casi 500 KB. El nombre y el icono han variado mucho de versión a versión. Nombres comunes eran "Patch.exe" y "SysEdit.exe". Cuando se inicia por primera vez, el servidor se instala en el ordenador host, incluyendo la modificación de Windows del Registro para que se inicie automáticamente en cada inicio del sistema.

El servidor atiende las conexiones en el puerto 12345 (en algunas versiones, el puerto es configurable), el puerto 12346 se utiliza para ciertas tareas, así como el puerto 20034.

El cliente es un programa separado de la presentación con una interfaz gráfica que permite al usuario realizar una serie de actividades en el equipo remoto, como pueden ser:
 Registro de las pulsaciones del teclado (Keylogging)
 Inyección de teclas de manera remota
 Captura de pantalla, permitiendo descargarla al cliente
 Ejecución remota de aplicaciones
 Navegación por los archivos y carpetas del servidor
 Apagado del sistema
 Abrir / cerrar la bandeja del CD
 Tunneling

NetBus hace conexiones a través de un sinnúmero de sistemas; el cliente de NetBus fue diseñado para las siguientes versiones de Windows:
 Windows 95
 Windows ME
 Windows NT 4.0
 Windows 2000 y Windows XP (Netbus client v1.70)

La mayor parte del protocolo utilizado entre el cliente y el servidor es textual. Por lo tanto, el servidor puede ser controlado por comandos, permitiendo administrar equipos con NetBus desde sistemas operativos distintos a Windows.

**Características**

(tales como la captura de pantalla)

Requieren una aplicación con capacidad de aceptar datos binarios, tales como netcat. La mayoría de los protocolos más comunes (como el Internet Relay Chat protocolo POP3, SMTP,HTTP) también se puede utilizar con conexiones de una manera similar.

NetBus Pro 2.0 fue liberado en febrero de 1999. Se comercializa como una poderosa herramienta de administración remota, pero existen versiones especiales hacker que permiten utilizarlo con fines ilegales.

Todas las versiones del programa han sido ampliamente utilizados por los "script Kiddies" y fue popularizado por el lanzamiento de **Back Orifice**. Debido a su pequeño tamaño, Back Orifice se puede utilizar para obtener acceso y control a una máquina remota. El atacante puede utilizar Back Orifice NetBus para instalar el servidor en el equipo de destino. La mayoría de antivirus detecta y elimina estos programas NetBus.

También existe una herramienta llamada **NetBuster**. Lo que Pretende es ejecutar en un servidor, NetBuster podría ser utilizado para mando a distancia.

 Enlaces externos
 Information about Back Orifice and NetBus — Information from anti-virus vendor Symantec
