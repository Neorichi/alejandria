---
type: Artículo de enciclopedia
title: Troyano (informática)
description: "En informática, se denomina caballo de Troya, o troyano, a un malware que se presenta al usuario como un programa aparentemente legítimo e inofensivo, pero que, al ejecutarlo, le brinda a un atacante acceso remoto al …"
resource: https://es.wikipedia.org/wiki/Troyano_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Troyano_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Troyano_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Troyano (informática)

En informática, se denomina **caballo de Troya**, o **troyano**, a un *malware* que se presenta al usuario como un programa aparentemente legítimo e inofensivo, pero que, al ejecutarlo, le brinda a un atacante acceso remoto al equipo infectado. El término troyano proviene de la historia del caballo de Troya del ciclo épico griego, narrado principalmente en la Eneida de Virgilio y mencionado en la Odisea de Homero..

Los troyanos pueden realizar diferentes tareas, pero, en la mayoría de los casos, crean una puerta trasera que permite la administración remota a un usuario no autorizado.

Un troyano es un tipo de *malware*. Para que un *malware* sea un troyano solo tiene que acceder y controlar la máquina anfitriona sin ser advertido, bajo una apariencia inocua.

Hay ciertas fuentes que lo descatalogan como malware debido a que aparentemente no causa daños en los sistemas, pero causan también otra clase de perjuicios, como el robo de datos personales.

 Evolución histórica

Los troyanos se concibieron como una herramienta para causar el mayor daño posible en el equipo infectado. En los últimos años y gracias al mayor uso de Internet, esta tendencia ha cambiado hacia el robo de datos bancarios o información personal.

Desde sus orígenes, los troyanos han sido utilizados como arma de sabotaje por los servicios de inteligencia como la CIA, cuyo caso más emblemático fue el sabotaje al gasoducto siberiano en 1982. La CIA instaló un troyano en el software que se ocuparía de manejar el funcionamiento del gasoducto, antes de que la URSS comprara ese software en Canadá.

De acuerdo con un estudio de la empresa responsable del software de seguridad BitDefender desde enero hasta junio de 2009, «El número de troyanos está creciendo, representan el 83 % del malware detectado».

 Propósitos de los troyanos

Los troyanos están diseñados para permitir a un individuo el acceso remoto a un sistema. Una vez en ejecución, el atacante puede acceder al sistema de forma remota y realizar diferentes acciones sin necesitar permiso. Las acciones que el atacante puede realizar en el equipo remoto dependen de los privilegios que tenga el usuario atacado en ese equipo y de las características del troyano.

Algunas de las operaciones más comunes son:
 Utilización la máquina como parte de una *botnet* (por ejemplo, para realizar ataques de denegación de servicio o envío de *spam*).
 Instalación de otros programas (incluyendo aplicaciones maliciosas).
 Robo de información personal: información bancaria, contraseñas, códigos de seguridad, robo de archivos varios, etcétera.
 Borrado, modificación o transferencia de archivos (descarga o subida).
 Borrado completo del disco.
 Ejecución o finalización de procesos.
 Apagado o reiniciado del equipo.
 Captura de las pulsaciones del teclado.
 Capturas de pantalla.
 Llenado del disco duro con archivos inútiles.
 Monitorización del sistema y seguimiento de las acciones del usuario.
 Captura de imágenes o vídeos a través de la webcam, si tiene.
 Acciones inocuas desde el punto de vista de la seguridad, destinadas a sorprender al usuario, tales como expulsar la unidad de CD, cambiar la apariencia del sistema, etc.

Actualmente, y dada la popularidad de los dispositivos móviles y tabletas, son estas plataformas (especialmente aquellas con menor control en su mercado de aplicaciones) las que suscitan un creciente interés entre los desarrolladores de este tipo de malware. Dado el uso personal de estos dispositivos, las acciones que un atacante puede realizar en estos dispositivos comprende las ya descritas, más otras específicas derivadas de la naturaleza privada de la información que se almacena en estas plataformas. Algunos ejemplos son:

 Captura de los mensajes entrantes y salientes de aplicaciones de mensajería.
 Captura del registro de llamadas.
 Acceso y modificación de contactos en la agenda.
 Habilidad para efectuar llamadas y enviar mensajes de texto.
 Conocimiento de la posición geográfica del dispositivo mediante GPS.

 Características de los troyanos

Generalmente, los caballos de troya son utilizados para robar información, en casos extremos, obtener el control remoto de la computadora, de forma que el atacante consiga acceso de lectura y escritura a los archivos y datos privados almacenados, visualizaciones de las pantallas abiertas, activación y desactivación de procesos, control de los dispositivos y la conexión a determinados sitios de Internet desde la computadora afectada como las páginas pornográficas.
Los troyanos están compuestos principalmente por dos programas: un programa de administración, que envía las órdenes que se deben ejecutar en la computadora infectada y el programa residente situado en la computadora infectada, que recibe las órdenes del administrador, las ejecuta y le devuelve un resultado. Generalmente también se cuenta con un editor del programa residente, el cual sirve para modificarlo, protegerlo mediante contraseñas, unirlo a otros programas para disfrazarlo, configurar en que puerto deseamos instalar el servidor, etc.
Atendiendo a la forma en la que se realiza la conexión entre el programa de administración y el residente se pueden clasificar en:
 Conexión directa
 El atacante se conecta directamente al PC infectado mediante su dirección IP. En este caso, el equipo atacante es el cliente y la víctima es el servidor.
 Conexión indirecta (o inversa)
 El equipo *host* o víctima se conecta al atacante mediante un proceso automático en el *malware* instalado en su equipo, por lo que no es necesario para el atacante disponer de la dirección IP de la víctima. Para que la conexión este asegurada, el atacante puede utilizar una IP fija o un nombre de dominio. La mayoría de los troyanos modernos utilizan este sistema de conexión, donde el atacante es el servidor a la espera de la conexión y el equipo *host* es el cliente que envía peticiones de conexión para recibir órdenes de ejecución remotas bajo su propia demanda.

Los troyanos y otros tipos de *malware*, así como muchas utilidades software han evolucionado hacia el modelo de conexión inversa debido a la extensión de routers que aplican en su mayoría por defecto una capa de seguridad en la red inicial (como el propio NAT) actuando como firewall que impide bajo condiciones, conexiones entrantes hacia los clientes de la red salvo que este mecanismo se deshabilite o configure expresamente. De esta manera, es más sencillo crear herramientas que se salten esta protección ocasionando que sean los clientes los que soliciten sus órdenes remotas en lugar de permitir recibirlas.

A pesar de que los troyanos de conexión directa han caído en desuso casi totalmente frente a los de conexión inversa, dentro de los círculos de piratas informáticos se sigue utilizando la denominación de **cliente** para el equipo atacante y **servidor** para el equipo víctima, lo cual es incorrecto desde un punto de vista estricto.

La conexión inversa tiene claras ventajas sobre la conexión directa. Ésta traspasa algunos *firewalls* (la mayoría de los *firewall* no analizan los paquetes que salen de la computadora, pero que sí analizan los que entran), pueden ser usados en redes situadas detrás de un rúter sin problemas (no es necesario redirigir los puertos) y no es necesario conocer la dirección IP del servidor.

Cabe destacar que existen otro tipo de conexiones, que no son de equipo víctima a equipo atacante, sino que utilizan un servidor intermedio, normalmente ajeno a ambos, para realizar el proceso de control. Se suelen utilizar para este propósito los protocolos IRC y el FTP, HTTP, aunque también pueden usarse otros.

 Formas de infectarse con troyanos

La mayoría de infecciones con troyanos ocurren cuando se ejecuta un programa infectado con un troyano. Estos programas pueden ser de cualquier tipo, desde instaladores hasta presentaciones de fotos. Al ejecutar el programa, este se muestra y realiza las tareas de forma normal, pero en un segundo plano y al mismo tiempo se instala el troyano. El proceso de infección no es visible para el usuario ya que no se muestran ventanas ni alertas de ningún tipo, por lo que evitar la infección de un troyano es difícil. Algunas de las formas más comunes de infección son:
 Descarga de programas de redes P2P.
 Páginas web que contienen contenido ejecutable (por ejemplo controles ActiveX o aplicaciones Java).
 Exploits para aplicaciones no actualizadas (navegadores, reproductores multimedia, clientes de mensajería instantánea).
 Ingeniería social (por ejemplo un cracker manda directamente el troyano a la víctima a través de la mensajería instantánea).
 Archivos adjuntos en correos electrónicos y archivos enviados por mensajería instantánea.
 Conectar a su equipo un dispositivo externo infectado.

Debido a que cualquier programa puede realizar acciones maliciosas en un ordenador, hay que ser cuidadoso a la hora de ejecutarlos. Estos pueden ser algunos buenos consejos para evitar infecciones:
 Disponer de un programa antivirus actualizado regularmente para estar protegido contra las últimas amenazas.
 Disponer de un firewall correctamente configurado. Algunos antivirus lo traen integrado.
 Tener instalados los últimos parches y actualizaciones de seguridad del sistema operativo.
 Descargar los programas siempre de las páginas web oficiales o de páginas web de confianza.
 No abrir los datos adjuntos de un correo electrónico si no conoces al remitente.
 Evitar la descarga de software de redes p2p.
 Actualizar el software del equipo.
Investigaciones recientes han revelado que el método del caballo de Troya se ha utilizado como ataque a los sistemas de computación en la nube. Un ataque troyano a sistemas en la nube intenta insertar una aplicación o servicio en el sistema que puede afectar los servicios en la nube al cambiar o detener las funcionalidades. Cuando el sistema en la nube identifica los ataques como legítimos, se realiza el servicio o aplicación que puede dañar e infectar el sistema en la nube.

 Algunas señales de que nuestra computadora está infectada por un troyano
 Pantalla o ventanas con mensajes poco usuales.
 Sin justificación aparecen, desaparecen y se modifican archivos.
 Comportamientos poco habituales en el funcionamiento de la computadora, como: modificaciones en el escritorio, refrescadores de pantalla, la unidad de CD-DVD, intercambio de las funciones de los botones del ratón, alteración del volumen del reproductor de sonido.
 Se activan o desactivan ventanas en la pantalla.
 Presencia de ficheros .TXT o sin extensión en el disco duro, preferiblemente en C:\.
 Eliminación repentina de los archivos de la papelera.
 Cambios en las propiedades de archivos que se encuentran o estuvieron en la papelera (Alteración en "fecha de creación", "fecha de eliminación" y "tipo de archivo").
 Lentitud en el Sistema Operativo, bloqueos continuos o se reinicia el sistema sin que se conozcan las causas, programas que inesperadamente comienzan su ejecución o la concluyen.
 El navegador de Internet accede por sí solo a determinados sitios.
 El navegador de Internet o el cliente de correo no reconoce nombre y contraseña o indica que ya está siendo utilizado.
 En la carpeta de enviados del cliente de correo electrónico se muestran mensajes no conocidos.

 Eliminación de troyanos

Una de las principales características de los troyanos es que no son visibles para el usuario. Un troyano puede estar ejecutándose en un ordenador durante meses sin que el usuario lo perciba. Esto hace muy difícil su detección y eliminación de forma manual. Algunos patrones para identificarlos son: un programa desconocido se ejecuta al iniciar el ordenador, se crean o borran archivos de forma automática, el ordenador funciona más lento de lo normal, errores en el sistema operativo.

Por otro lado, los programas antivirus están diseñados para eliminar todo tipo de software malicioso; además de eliminarlos, también previenen de nuevas infecciones actuando antes de que el sistema resulte infectado. Es muy recomendable tener siempre un antivirus instalado en el equipo y a ser posible también un firewall.

Herramientas relacionadas

Generador de troyanos

Un **Generador de troyanos** o **TDK** (del inglés *Trojan Development Kit*), es una herramienta que permite crear fácilmente troyanos personalizados que suelen incluir ciertas técnicas de ocultación.

Ejemplos de generadores de troyanos son:
 Senna Spy Generator. Posee opciones para transferencia de ficheros, ejecución de comandos DOS, control del teclado, y listado y control de procesos.
 Trojan Construction Kit. Está basado en línea de comandos.
 Trojan Horse Construction Kit.
 Progenic Mail Trojan (PMT).
 Pandora's box.
 Stealth Tool. Programa orientado a alterar el fichero de un troyano para mejorar su capacidad de ocultación.

Trojan Development Kit App

Se llama **Trojan Development Kit App** a aplicaciones móviles que permiten crear rápidamente aplicaciones móviles que son troyanos personalizados, generalmente ransomware, para ser usados en dispositivos móviles, habitualmente Android. Por ejemplo en 2017 se descubrió una app, en formato APK, descargable previo pago, que se anunciaba en sitios de hackers y redes sociales chinas y que permitía generar un ransomware personalizable de tipo Lockdroid. La aplicación permitía personalizar el mensaje que se presenta al usuario, el código de desbloqueo, el icono de la aplicación, operaciones para ofuscar el código y animaciones a mostrar en la pantalla del dispositivo bloqueado. . Al concluir esta configuración básica, la aplicación genera un archivo infectado con el ransomware. A partir de ese punto corresponde al usuario encontrar la forma de infectar los aparatos de sus potenciales víctimas. Este tipo de aplicaciones son especialmente interesantes para el mercado chino debido a que Play Store de Google está bloqueada en ese país, lo que obliga a los usuarios a descargar apps desde sitios y foros diversos.

Wrapper

Un **Wrapper** es un programa usado para combinar dos o más ejecutables en un solo programa. Suele ser usado para adjuntar un ejecutable inofensivo, por ejemplo un juego, a la carga útil de un troyano con la intención de que el ejecutable resultante parezca un fichero inofensivo. Cuando el usuario ejecuta el fichero ejecutable resultante, primero ejecuta el programa inofensivo y después instala, en segundo plano y de forma oculta, el troyano.

Ejemplos de este tipo de software son:
 ELiteWrap. Es de los más antiguos y funciona en Windows y permite configurar la extracción de ficheros a directorios especificados y programar su ejecución.
 Silk Rope 2000. Posee una interfaz gráfica fácil y permite ocultar Back Orifice en el programa inofensivo que elijamos, pudiendo seleccionar el icono del programa ejecutable resultante.
 PE Bundle.
 Teflon Oil Patch (TOVB4).
 AFX File Lace.
 Exe2vbs.
 Saran Wrap. Diseñado específicamente para trabajar con Back Orifice.
 Trojan Man.
 Restorator.
 FireKiller 2000.

Herramientas para aprovechar canales encubiertos

Son herramientas diseñadas para explotar canales encubiertos para permitir mantener ocultas ciertas comunicaciones.

 Tipos de troyanos

 Backdoors
 Un troyano de estas características, le permite al atacante conectarse remotamente al equipo infectado. Las conexiones remotas son comúnmente utilizadas en informática y la única diferencia entre estas y un *backdoor* es que en el segundo caso, la herramienta es instalada sin el consentimiento del usuario. La tecnología aplicada para acceder remotamente al equipo no posee ninguna innovación en particular ni diferente a los usos inofensivos con que son utilizadas estas mismas aplicaciones. Una vez que el atacante accede al ordenador del usuario, los usos que puede hacer del mismo son variados, según las herramientas que utilice: enviar correos masivos, eliminar o modificar archivos, ejecución de archivos, reiniciar el equipo o usos más complejos como instalar aplicaciones para uso malicioso (por ejemplo: alojamiento de sitios web de violencia o pedofilia).
 Keyloggers
 Los keyloggers (del inglés Key = Tecla y Log = Registro) son uno de los tipos más utilizados para obtener información sensible de los usuarios. Los troyanos de este tipo, instalan una herramienta para detectar y registrar las pulsaciones del teclado en un sistema. Pueden capturar información como contraseñas de correos, cuentas bancarias o sitios web, entre otras, y por lo tanto atentar contra información sensible del usuario. La información capturada es enviada al atacante generalmente, en archivos de texto con la información, cifrada o sin cifrar. Estos troyanos no son una amenaza para el sistema sino para el usuario y su privacidad. Los datos recolectados pueden ser utilizados para realizar todo tipo de ataques, con fines económicos o simplemente malignos, como modificar las contraseñas de las cuentas de acceso a algún servicio.
 Banker
 Los troyanos bancarios tienen como principal objetivo robar datos privados de las cuentas bancarias de los usuarios. Utilizan diferentes técnicas para obtener los datos de acceso a todo tipo de entidades financieras, algunas de ellas son: reemplazar parcial o totalmente el sitio web de la entidad, enviar capturas de pantalla de la página bancaria (útiles cuando el usuario utiliza teclados virtuales) o incluso la grabación en formato de video de las acciones del usuario mientras accede al sitio web. Los datos son enviados al atacante, por lo general, por correo electrónico o alojándolos en sitios FTP.
 Downloader
 Este tipo de troyanos tiene como principal función la de descargar otros archivos maliciosos. Esta clase de amenazas no hace algún daño en sí, sino que descarga otros archivos maliciosos para el ordenador. El troyano se encarga, no solo de descargar el/los archivos, sino también de ejecutarlos o preparar la máquina para su ejecución automática al inicio.
 Botnets
 Los troyanos botnets, son utilizados para crear redes de equipos zombis (botnets). El atacante utiliza el troyano (generalmente combinado con herramientas de backdoors) para controlar una cantidad importante de ordenadores y así poder utilizarlos para cualquier fin maligno. Pueden ser utilizados para enviar spam o para realizar ataques de denegación de servicio (DoS); estos consisten en saturar un sitio web generando más accesos y requerimientos de los que puede soportar y provocando la baja del servicio.
 Proxy
 Este tipo de troyanos instalan herramientas en el ordenador que le permiten al atacante utilizar la PC infectada como un servidor proxy. Un proxy es un servidor que da acceso a otros ordenadores a Internet a través de él. En este caso, el atacante utiliza el ordenador infectado para acceder a la web a través de él, enmascarando su identidad.
 Password Stealer
 Los passwords Stealer se encargan de robar información introducida en los formularios en las páginas web. Pueden robar información de todo tipo, como direcciones de correo electrónico, logins, passwords, PIN, números de cuentas bancarias y de tarjetas de crédito. Estos datos pueden ser enviados por correo electrónico o almacenados en un servidor al que el delincuente accede para recoger la información robada. En la mayoría de sus versiones, utilizan técnicas keyloggers para su ejecución y son similares a estos.
 Dialer
 Los troyanos “Dialer” crean conexiones telefónicas en el ordenador del usuario, utilizando las funcionalidades del módem. Estas conexiones son creadas y ejecutadas de forma transparente a la víctima. Generalmente, se trata de llamados de alto costo a sitios relacionados con contenido adulto en Internet. Este tipo de troyanos crean un daño económico al usuario, el ordenador no se ve afectado por hacer una llamada telefónica.
 Cemetery
 El troyano “Cemetery” es una novedad en este tipo de malware, apareciendo por primera vez en 2018. Su principal propósito es el robo de información multimedia y documentos. Trabaja exclusivamente en la papelera de reciclaje, ya que es el área más vulnerable de cualquier ordenador. Su *modus operandi* es el siguiente: cambia las propiedades de los archivos infectados, alterando su fecha de creación, tipo de archivo o fecha de eliminación del mismo, comúnmente con fechas recientes o incluso semanas próximas, provocando que un antivirus no pueda detectarlo ya que el archivo todavía "no fue creado".

 Troyanos más famosos

 NetBus (1998)
 Software malicioso para el control de una forma remota de sistemas informáticos Microsoft Windows a través de una red. Fue creado en 1998 y ha sido muy controvertido por su potencial de ser utilizado como una puerta trasera.
 Historia
 NetBus se escribió en Delphi por Carl-Fredrik Neikter, un programador sueco en marzo de 1998. Entró en circulación antes que Back Orifice, fue liberado en agosto de 1998. El autor afirmó que el programa estaba destinado a ser usado para bromas, no para irrumpir ilegalmente en los sistemas informáticos. Traducido del sueco, el nombre significa "NetPrank". Sin embargo, el uso de NetBus ha tenido graves consecuencias. En 1999, NetBus se utilizó para introducir pornografía infantil en el equipo de trabajo de Magnus Eriksson, un erudito en Derecho Universidad de Lund. Las 3500 imágenes fueron descubiertas por los administradores del sistema, y Eriksson se supone que lo había descargado a sabiendas.
 Características
 Existen dos componentes para la arquitectura cliente-servidor. El servidor debe ser instalado y ejecutado en el equipo que quiere ser controlado a distancia, el tamaño de archivo es de casi 500 KB. El nombre y el icono han variado mucho de versión a versión. Nombres comunes eran "Patch.exe" y "SysEdit.exe". Cuando se inicia por primera vez, el servidor se instala en el ordenador host, incluyendo la modificación de Windows del Registro para que se inicie automáticamente en cada inicio del sistema.
 Back Orifice
 Es un programa de control remoto de ordenadores que funciona bajo un servidor y un cliente. Si colocamos el servidor a otro ordenador remoto, es posible desde el cliente, gobernar cualquier función del ordenador remoto, entre los que destaca abrir y cerrar programas, controlar el CD-ROM, leer y modificar ficheros o borrar parte del disco duro.
 Para ello el servidor se autoejecuta y se borra cada vez que el ordenador ajeno se enciende, nuestro cliente escanea el puerto elegido y cuando este está abierto actúa a través de él, desde un menú repleto de pestañas y opciones de control remoto. El sistema es bueno para controlar un ordenador u ordenadores dentro de nuestra red LAN, aunque dejar este puerta abierta para Windows es toda una amenaza.
 Sub7(1999)
 Sub7, o SubSeven, es un software de administración remota para sistemas Microsoft Windows a través del Internet, es también categorizado como troyano o Puerta trasera por ciertas características similares a las de un virus informático. Es usado para acceder y controlar de forma remota una computadora sin el consentimiento del usuario, en donde es el usuario que mantiene en su poder al Cliente del software por medio del Servidor que permite que el sistema comprometido sea controlado de forma remota.
 Memz(2000)
 Es un troyano que infecta a las computadoras cambiando el MBR o el motor de arranque por un dibujo del nyan cat que primero empieza con playloads de abrir el Internet Explorer sin su consentimiento del usuario, que después sigue abriendo los comandos y aplicaciones del sistema como el cmd, bloc de notas, etc. Y por último se toma capturas de pantallas, hasta que la computadora colapse.
 Bifrost(2004)
 Es una variante de virus informático, el cual es usado para acceder remotamente a otra pc, sin consentimiento.

 Véase también

 Referencias

 Enlaces externos
