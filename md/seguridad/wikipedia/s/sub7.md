---
type: Artículo de enciclopedia
title: Sub7
description: "Sub7, o SubSeven, es el nombre de un software de administración remota para sistemas Microsoft Windows a través del Internet, es también categorizado como troyano o Puerta trasera por ciertas características similares a …"
resource: https://es.wikipedia.org/wiki/Sub7
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sub7"}
license: CC BY-SA 4.0
id: eswiki-Sub7
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sub7

- **Nombre:** Sub7
- **Desarrollador:** MobMan
- **Autor:** MobMan
- **Lanzamiento:** 1999
- **Última versión:** 2.1.5
- **Última versión prueba:** 2.2.0
- **Género:** Administración remota
- **Lenguaje programación:** Borland Delphi
- **Sistema operativo:** Microsoft Windows
- **Plataforma:** 95/98/ME/NT/XP/2000

**Sub7**, o **SubSeven**, es el nombre de un software de administración remota para sistemas Microsoft Windows a través del Internet, es también categorizado como troyano o Puerta trasera por ciertas características similares a las de un Virus informático. Es usado para acceder y controlar de forma remota una computadora sin el consentimiento del usuario, en donde es el usuario que mantiene en su poder al Cliente del software por medio del Servidor que permite que el sistema comprometido sea controlado de forma remota. También puede ser usado para actividades de espionaje, Hacking, y a veces hasta criminales o robo de información sensible. El nombre del software deriva de otro software de la misma categoría llamado **NetBus** cuya escritura a la inversa es ***suBteN*** en la que sustituyendo la sílaba ***ten*** por ***seven*** que formaría la palabra ***SubSeven***.

 Características y funcionamiento

El Subseven se divide en 3 partes:

 **El Cliente**: Es el software que envía los comandos de control interpretados por el servidor como instrucciones de control y es usado por el usuario que tiene por objetivo obtener información y control sobre el sistema remoto, siendo así el usuario tendría las habilidades de control remoto tales como la posibilidad de editar el archivo registro del servidor windows, girar la pantalla, modificar los colores de los escritorios, obtener información, realizar grabaciones de vídeo o de sonido, apagar y reiniciar el sistema, visualizar cámara y pantalla del computador remotamente e incluso obtener teclas presionadas.

 **El Editor del Servidor**: Es usado para editar y configurar la forma en que se instala el servidor en la computadora remota y especificar el Puerto de red en la cual se establecerá la conexión remota , también se puede configurar notificaciones de instalación exitosa, auto-copiado del servidor a una carpeta diferente a donde fue ejecutado como método para evitar la eliminación del archivo por parte del usuario controlado, cambiar icono del servidor "camuflaje", inyectar procesos, proteger el servidor por contraseña evitando la manipulación del sistema remoto por otro usuario que posea el cliente del SubSeven y otras funciones que permiten la instalación del servidor de forma invisible para el sistema que va a ser controlado por el cliente.

 **El Servidor**: Es el programa que residirá en el sistema que será controlado, no posee interfaz gráfica ya que sus funciones están orientadas a recibir y ejecutar instrucciones enviadas desde el cliente del SubSeven, siendo invisible para el sistema y controlado de forma furtiva, normalmente el tamaño del servidor está entre los 25Kb a 120Kb dependiendo de la capacidad de funciones que se incluyan en dicho software, normalmente se usan plugins o complementos para usar más funciones no incluidas en el servidor, que son instaladas desde el cliente como archivos de extensión Dll, obteniendo más control sobre el sistema sin necesidad de aumentar el tamaño del servidor.

*Véase también:* Propósito de los troyanos

Sus funciones básicas son:

 Captura del teclado: obtiene las pulsaciones del teclado.
 Chat: Le da la posibilidad de chatear al usuario remoto o de otros clientes que ya están conectados a la misma computadora.
 Chat Matrix: Le permite chatear con el usuario remoto al estilo "matrix", al usuario remoto se le abrirá una ventana totalmente negra con letras verdes fosforescentes y cubre toda la pantalla del computador, obligándolo a solo chatear con el usuario que usa el cliente de SubSeven,.
 MSG Manager (Administrador de mensajes de alertas): Esta opción sirve para configurar y enviar una notificación de alerta de Microsoft Windows con un mensaje personalizable por parte del Cliente.
 Instant Messenger Spy (Espía de Mensajería Instantánea): Característica que posibilita ver en tiempo real conversaciones del usuario remoto en las diferentes aplicaciones de Mensajería instantánea como lo son: Windows Live Msn, ICQ, AIM , etc.
 FileManager (Administrador de Archivos): Esta característica permite explorar en disco duro remoto por medio del sistema de ficheros del windows, usted puede cargar / descargar / modificar / eliminar cualquier archivo que desee. Básicamente, es como el Explorador de Windows pero en forma remota.
 Windows Manager (Administrador de Ventanas): Aquí usted puede controlar cualquier ventana abierta en el computador remotamente, por ejemplo, bloquear, cerrar, minimizar y maximizar una de sus ventanas de su explorador web, Bloc de notas, o algún otro programa abierto.
 Process Manager (Administrador de tareas): Con esta opción, podrá ver los procesos en ejecución, y detalles de esos archivos, como su peso , consumo de memoria de la Unidad central de procesamiento, etc.
 Clipboard Manager (Administrador del Porta papeles): Captura cualquier texto grabado en el portapapeles del computador.

 SubSeven 2.1.5 Legends
Esta edición fue lanzado en el mes de febrero del 2003, considerado por el autor como "Edición de aniversario" , ya que su primera versión fue desarrollado en el mismo mes pero en el año 1999. Es la versión más estable y confiable de todas las versiones existentes, a diferencia de sus versiones anteriores, este soporta plataformas de Microsoft Windows NT/2K/XP, pero quedando en la categoría de troyanos de conexión directa (Conexión de Cliente a Servidor) en la cual el computador remoto abre un puerto de red ***(en la versión 2.1.5 por defecto es: 27374)*** , y luego el Cliente se conecta a ese puerto estableciendo una conexión entre dos computadoras de forma remota a través de la red , pero este queda obsoleto a cortafuegos actuales que bloquean cualquier conexión remota.

*Véase también:* Características de los troyanos

 SubSeven 2.2
Esta versión es según el autor, de tipo **Beta** o versión de prueba, es la única versión modular de sub7, ya que permite de forma personalizada editar y crear funciones, algunas inestables, pero agrega tres nuevas formas para autocargarse en Windows, ejecutándose en cada reinicio del sistema, de esa manera siempre estará disponible al conectarse el sistema remoto a Internet:

 Usando la opción de Componentes Instalados del registro
 Creando una carpeta de inicio personalizada
 Creando un archivo EXPLORER. EXE en el directorio raíz
A diferencia de versiones anteriores, la 2.2 agrega la posibilidad de enviar comandos en línea y utiliza plugins (actualizaciones) vía Internet, como lo hace el BO2K (Back Oriffice 2000)

Estos plugins se descargan de cualquier sitio Web o Alojamiento web en la que este alojado el archivo DLL, y se instalan en la computadora remota descargándose de dicho servidor web. Los mismos llevan la extensión Dll con nombres aleatorios, y son guardados en la carpeta C:\WINDOWS\SYSTEM.

 SubSeven 2.3

Esta versión fue lanzado el 28 de febrero de 2010, formará parte de la nueva generación de troyanos de conexión inversa, en la cual consiste en que el servidor se conectara al cliente quien tendrá el puerto de red abierto para establecer una conexión entre las dos computadoras, de esta forma configurando el servidor , especificara su IP o Dominio de red para que el servidor de SubSeven se conecte a su computador o sistema al puerto de red especificado.

Incluye nuevas funciones:

 Desinstalacion silenciosa de programas.
 Obtener contraseña de red Wifi.
 Control completo del sistema remoto / y visualizador de pantalla remota como Teamviewer.
 Recupera contraseñas de VNC.
 Obtiene contraseñas guardadas por el explorador Google chrome, Internet Explorer.
 Obtiene contraseña guardadas de redes compartidas (Incluye contraseñas de Windows Live Messenger).
 Obtiene contraseñas de sistemas Microsoft office / Windows / Microsoft SQL Server.
 Sistema de Scanner bluetooth (32-bit) esto hace un escaneo durante 30 segundos para encontrar alguna información sobre los dispositivos bluetooth conectados al sistema como teléfonos etc., para así descargar datos obtenidos del dispositivo en cuestión.
 Recopila información acerca de dispositivos USB conectados.
 Obtiene cuentas y contraseñas de Microsoft Outlook 2000 (solo cuentas POP3 y SMTP), Microsoft Outlook 2002/2003/2007 (cuentas de POP3, IMAP, HTTP y SMTP)y Windows Mail.
 Obtiene cuentas y contraseñas de Windows Live Mail, IncrediMail y Eudora.
 Netscape 6.x/7.x (si la contraseña no está cifrada con la contraseña maestra)
 Mozilla Thunderbird (si la contraseña no está cifrada con la contraseña maestra)
 Group Mail Free
 Correos Yahoo!- Si la contraseña está guardado en el Yahoo! Messenger.
 Hotmail/MSN mail - Si la contraseña está guardado en el MSN/Windows/Live Messenger.
 Gmail - Si la contraseña está guardada en el Gmail Notifier, Google Desktop, o por el Google Talk.
 ICQ Lite 4.x/5.x/2003
 AOL Instant Messenger v4.6 o versiones anteriores, AIM 6.x, y AIM Pro.
 Trillian
 Trillian Astra* Miranda
 GAIM/Pidgin* MySpace IM
 PaltalkScene
 Digsby

 Historia final del SubSeven

El 1 de abril del año 2010, 5 días después de que el sitio web ***www.subseven.org*** fuese hackeado por un pirata informático que se hacía llamar *-Punk-*, el equipo del portal de Sub7 anunció en su sitio web que el proyecto había llegado a su fin debido a dicho ataque. El equipo de Sub7 anunció que el hacker había robado el código fuente y la base de datos del sitio eliminando todos los proyectos. Al principio se creía que era una broma de *April Fools*, pero al día siguiente apareció un hilo en un foro donde el intruso publicaba información de su hazaña.

*Contexto del sitio:*

Aunque se cancelase el proyecto el 1/4/2010, la página www.subseven.org anuncia desde el 1/11/2010 que volverán con la versión 2.3.1.

 Referencias

 Véase también
 Back Orifice
 Ingeniería social (seguridad informática)
 Malware
 Phishing
 Seguridad informática
