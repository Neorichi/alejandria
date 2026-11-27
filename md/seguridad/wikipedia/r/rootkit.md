---
type: Artículo de enciclopedia
title: Rootkit
description: "Un rootkit o encubridor es un conjunto de software que permite al usuario un acceso de \"privilegio\" a un ordenador, pero mantiene su presencia inicialmente oculta al control de los administradores al descomponer el …"
resource: https://es.wikipedia.org/wiki/Rootkit
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Rootkit"}
license: CC BY-SA 4.0
id: eswiki-Rootkit
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Rootkit

Un ***rootkit*** o **encubridor** es un conjunto de *software* que permite al usuario un acceso de "privilegio" a un ordenador, pero mantiene su presencia inicialmente oculta al control de los administradores al descomponer el funcionamiento normal del sistema operativo. Este término proviene de una concatenación de la palabra inglesa *root*, que significa 'raíz' (nombre tradicional de la cuenta privilegiada en los sistemas operativos Unix) y de la palabra inglesa *kit*, que significa 'conjunto de herramientas' (en referencia a los componentes de software que implementan este programa).

El término *rootkit* tiene connotaciones peyorativas ya que se lo asocia a programas maliciosos al esconderse a sí mismo y a otros programas, procesos, archivos, directorios, claves de registro y puertos. Esto permite al intruso mantener el acceso a una amplia variedad de sistemas operativos como pueden ser GNU/Linux, Solaris o Microsoft Windows para remotamente enviar acciones o extraer información sensible.

Usualmente, un atacante instala un encubridor en una computadora después de primero haber obtenido derechos de escritura en cualquier parte de la jerarquía del sistema de ficheros, pudiendo ser por haberse aprovechado de una vulnerabilidad conocida o por haber obtenido una contraseña (ya sea por descifrado de contraseñas o por ingeniería social). Una vez que el *rootkit* ha sido instalado, permite que el atacante disfrace la siguiente intrusión y mantenga el acceso privilegiado a la computadora por medio de rodeos a los mecanismos normales de autenticación y autorización. Pese a que los *rootkits* pueden servir con muchos fines, han ganado notoriedad fundamentalmente como *malware*, escondiendo programas que se apropian de los recursos de las computadoras o que roban contraseñas sin el conocimiento de los administradores y de los usuarios de los sistemas afectados. Los encubridores pueden estar dirigidos al *firmware*, al hipervisor, al núcleo, o, más comúnmente, a los programas del usuario.

La detección del encubridor es complicada pues es capaz de corromper al programa que debería detectarlo. Los métodos de detección incluyen utilizar un sistema operativo alternativo confiable; métodos de base conductual; controles de firma, controles de diferencias y análisis de volcado de memoria. La eliminación del encubridor puede ser muy difícil o prácticamente imposible, especialmente en los casos en que el *rootkit* reside en el núcleo; siendo a veces la reinstalación del sistema operativo el único método posible que hay para solucionar el problema.

 Uso de los rootkits
Un *rootkit* se usa habitualmente para esconder algunas aplicaciones que podrían actuar en el sistema atacado. Suelen incluir puertas traseras para ayudar al intruso a acceder fácilmente al sistema una vez que se ha conseguido entrar por primera vez. Por ejemplo, el rootkit puede esconder una aplicación que lance una consola cada vez que el atacante se conecte al sistema a través de un determinado puerto. Los *rootkits* del núcleo pueden contener funcionalidades similares. Una puerta trasera puede permitir también que los procesos lanzados por un usuario sin privilegios de administrador ejecuten algunas funcionalidades reservadas únicamente al superusuario. Todo tipo de herramientas útiles para obtener información de forma ilícita pueden ser ocultadas mediante *rootkits*.

Los encubridores se utilizan también para usar el sistema atacado como «base de operaciones», es decir, usarlo a su vez para lanzar ataques contra otros equipos. De este modo puede parecer que es el sistema infiltrado el que lanza los ataques y no el intruso externo. Este tipo de ataques podrían ser de denegación de servicio (DoS), ataques mediante IRC o mediante correo electrónico en forma de correo basura.

 Funcionamiento de los *rootkits*
El funcionamiento de los encubridores se puede generalizar de la siguiente manera:

 Infección del sistema: en primer lugar, el *rootkit* se instala en el dispositivo e infecta el sistema.
 El modo encubierto: una vez que el *rootkit* se haya instalado, pasa al modo encubierto. En otras palabras, el rootkit se oculta en el sistema y empieza a manipular los procesos de intercambio de datos que utilizan los programas y las funciones para mandar falsa información a los programas de seguridad como, por ejemplo, los programas antivirus.
 Crear una puerta trasera: el último paso consiste en crear una puerta trasera para permitir el acceso remoto al dispositivo. La tarea del encubridor consiste en ocultar los inicios de sesión remotos y cualquier actividad que se pueda clasificar como sospechosa para poder manipular el dispositivo sin dejar ningún rastro.

 Tipos de rootkits
 Tipos básicos
Los *rootkits* se pueden clasificar en dos grupos: los que van integrados en el núcleo y los que funcionan a nivel de aplicación. Los que actúan desde el núcleo añaden o modifican una parte del código de dicho núcleo para ocultar el *backdoor*. Normalmente este procedimiento se complementa añadiendo nuevo código al núcleo, ya sea mediante un controlador o un módulo, como los módulos del núcleo de Linux o los dispositivos del sistema de Windows. Estos rootkits suelen parchear las llamadas al sistema con versiones que esconden información sobre el intruso. Son los más peligrosos, ya que su detección puede ser muy complicada.

Los encubridores que actúan como aplicaciones pueden reemplazar los archivos ejecutables originales con versiones descifradas que contengan algún troyano, o también pueden modificar el comportamiento de las aplicaciones existentes usando hacks, parches, código inyectado, etc.

 Ejemplos
Algunos troyanos han utilizado estos *rootkits* no persistentes que cargan en la memoria una vez que ellos se encuentran instalados:
 SuckIT
 Adore
 T0rn
 Ambient's Rootkit (ARK)
 Hacker Defender
 First 4 Internet XCP (Extended Copy Protection) DRM
 RkU Test Rootkit & Unreal
 Rootkit de núcleo: UACd (agrega un controlador de muy bajo nivel llamado UACd.sys)
 Rootkits de Macintosh

 Detección de *rootkits*
Hay limitaciones inherentes a cualquier programa que intente detectar *rootkits* mientras se estén ejecutando en el sistema sospechoso. Los *rootkits* son aplicaciones que modifican muchas de las herramientas y librerías de las cuales depende el sistema. Algunos *rootkits* modifican el propio núcleo (a través de módulos y otros métodos como se indica más arriba). El principal problema de la detección de *rootkits* consiste en que el sistema operativo en ejecución no es fiable globalmente. En otras palabras, algunas acciones como pedir la lista de los procesos en ejecución o listar los ficheros de un directorio no son fiables al no comportarse como deberían.

El mejor método para detectar un *rootkit* es apagar el sistema que se considere infectado y revisar o salvar los datos arrancando desde un medio alternativo, como un disco de rescate (como un CD-ROM) o una memoria USB. Un *rootkit* inactivo no puede ocultar su presencia. Los programas antivirus mejor preparados suelen identificar a los *rootkits* que funcionan mediante llamadas al sistema y peticiones de bajo nivel, las cuales deben quedar intactas. Si hay alguna diferencia entre ellas, se puede afirmar la presencia de un *rootkit*. Los *rootkits* intentan protegerse a sí mismos monitorizando los procesos activos y suspendiendo su actividad hasta que el escaneo ha finalizado, de modo que el *rootkit* no pueda ser identificado por un detector.

Los fabricantes de aplicaciones de seguridad han ido integrando los detectores de *rootkits* en los productos tradicionales de detección de antivirus. Si un *rootkit* consigue esconderse durante el proceso de detección, será identificado por el detector de *rootkits*, que busca movimientos sospechosos. Si el encubridor «decide» detenerse momentáneamente, será identificado como un virus. Esta técnica combinada de detección puede obligar a los atacantes a implementar mecanismos de contraataque (también llamados retrorrutinas) en el código del *rootkit*, con el objetivo de eliminar los procesos creados por el software de seguridad, eliminando así al programa antivirus de la memoria. Al igual que con los virus convencionales, la detección y eliminación de los rootkits será una batalla permanente entre los creadores del rootkit y de los programas de seguridad.

Hay varios programas disponibles para detectar *rootkits*. En los sistemas basados en Unix, dos de las aplicaciones más populares son chkrootkit y rkhunter. Para Windows está disponible un detector llamado Blacklight (gratuito para uso personal) en la web de F-Secure. Blacklight presenta problemas de incompatibilidad en Windows 7. Otra aplicación de detección para Windows es Rootkit Revealer de Sysinternals. Detecta todos los *rootkits* actuales comparando las funcionalidades del sistema operativo original con las que se han detectado. Sin embargo, algunos *rootkits* han empezado a añadir este programa a la lista de los cuales no deben esconderse. En esencia, eliminan las diferencias entre los dos listados, de modo que el detector no los encuentra. Pero algo tan simple como renombrar el fichero 'rootkitrevealer.exe' hace que el *rootkit* ya no sepa que se está enfrentando a un detector. Como se decía antes, será una continua batalla entre los *rootkits* y los antivirus.

 Véase también
 Cracker
 Hacker
 Malware
 Seguridad informática
 Seguridad de la información
 Virus informático

 Referencias

 Enlaces externos
 Rootkits en el núcleo Linux
 Análisis del rootkit T0rn
 Rootkits para Windows y Linux y software de detección(En alemán)
 Anti-trojan.org: Información sobre troyanos en rootkits y software de detección
 Strider GhostBuster Rootkit Detection
 Unix Rootkits en packet storm security
  Six Rootkit Detectors Protect Your System (Serdar Yegulalp - InformationWeek)
 web de F-Secure
 Sysinternals
