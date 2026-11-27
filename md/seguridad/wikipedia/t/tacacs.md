---
type: Artículo de enciclopedia
title: TACACS
description: "TACACS (acrónimo de Terminal Access Controller Access Control System, en inglés ‘sistema de control de acceso mediante control del acceso desde terminales’)."
resource: https://es.wikipedia.org/wiki/TACACS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/TACACS"}
license: CC BY-SA 4.0
id: eswiki-TACACS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# TACACS

**TACACS** (acrónimo de* **T**erminal **A**ccess **C**ontroller **A**ccess **C**ontrol **S**ystem*, en inglés ‘sistema de control de acceso mediante control del acceso desde terminales’). Es un protocolo de autenticación remota privativo de Cisco, comúnmente usado en redes Unix, que se usa para comunicarse con un servidor de autenticación. TACACS permite a un servidor de acceso remoto comunicarse con un servidor de autenticación para determinar si el usuario tiene acceso a la red. TACACS está documentado en el RFC 1492.

Se trata de un servicio ocupado para la autenticación a un dispositivo, o también negarlo en caso de que las credenciales no sean verídicas. El protocolo que maneja es TCP y su puerto 49.

En un servidor con TACACS, la comunicación siempre va a ser directa, entre el cliente y servidor. El router actúa como un intermediador. Se realiza la conexión con el router que va a conectar con el servidor TACACS. Este servidor TACACS realiza la conexión con el router para saber cual es el usuario al router y el router lo pregunta al host. El host se la da al router y se la manda al servidor TACACS. Se repite dicha conexión para que el servidor TACACS pida la contraseña al router y del router al host. El host se la otorga al router y se la ofrece al servidor TACACS. De tal modo, el servidor TACACS decide si acepta o deniega la acción para que se pueda acceder al router.

 Configuración de TACACS en Cisco IOS
Para configurar un servidor TACACS+ en un dispositivo Cisco IOS, se utilizan los comandos proporcionados, de los cuales permitirán conectarse a un router de acuerdo a los usuarios y contraseñas ingresados en el servidor TACACS.

 Se crea un usuario local llamado con su contraseña. Este usuario se usará como respaldo por si los métodos de autenticación remota como TACACS+ o RADIUS fallan. Rx(config)#username  password
 Se activa el modelo AAA (Autenticación, Autorización y Contabilidad) en el dispositivo (en este caso Router), lo que permite la configuración de los métodos de autenticación y autorización que jugarán un papel importante en el servidor TACACS. Rx(config)#aaa new-model
 Se configura el método de autenticación para las sesiones de inicio de sesión. Primero se indica que se quiere autenticar a los usuarios por medio del servicio TACACS y si llega a fallar se utilizarán las credenciales locales. Rx(config)#aaa authentication login default group tacacs+ local
 Se entra en la configuración de líneas virtuales (VTY) para permitir conexiones remotas al dispositivo. Rx(config)#line vty 0 15
 Se especifica que se debe utilizar la autenticación local para las sesiones de líneas virtuales si no se puede autenticar a través de TACACS. Rx(config-line)#login local
 Se permiten el acceso por todos los tipos de transporte (como SSH y Telnet) en las líneas VTY. Rx(config-line)#transport input all
 Se procede a salir del modo de configuración de línea. Rx(config-line)#exit
 Se debe especificar la dirección IP del servidor TACACS que se conectará al dispositivo para autenticación. Rx(config)#tacacs-server host
 Se define la llave utilizada para la comunicación segura con el servidor TACACS. Esta clave debe coincidir con la configurada en el mismo servidor TACACS.Rx(config)#tacacs-server key De igual manera, se debe configurar el servidor en donde se manejara la autenticación por TACACS+ por medio del servicio AAA en el que se debe ingresar la configuración de la red del dispositivo al que se quiere autenticar, indicando el nombre del dispositivo, su IP de ese dispositivo (pueden ser de una a todas las IP's que maneje en sus interfaces), el tipo de servidor de autenticación (en este caso, TACACS) y la llave que debe coincidir con la que se dio en el comando.

Una vez agregados estos comandos, esta configuración permite que el dispositivo Cisco utilice TACACS+ para gestionar la autenticación, lo que ayuda en la seguridad y flexibilidad al acceder a la red. Aquí, si se accede por Telnet al router, pedirá un usuario y contraseña. Si otorgo el usuario y contraseña local, no me va a dejar, pero si le otorgo el usuario y contraseña que le otorgue al servidor TACACS, este sí me va a permitir acceder, dado que se tiene la prioridad de entrar por la autenticación TACACS que de manera local. Para entrar por manera local, se debe desconectar el servidor TACACS de la red para que se pueda acceder por el usuario y contraseña dados de manera local.

 Referencias
