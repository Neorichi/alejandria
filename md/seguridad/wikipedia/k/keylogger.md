---
type: Artículo de enciclopedia
title: Keylogger
description: "Un keylogger (derivado del inglés: key ('tecla') y logger ('registrador'); 'registrador de teclas') es un tipo de software o un dispositivo hardware específico que se encarga de registrar las pulsaciones que se realizan …"
resource: https://es.wikipedia.org/wiki/Keylogger
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Keylogger"}
license: CC BY-SA 4.0
id: eswiki-Keylogger
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Keylogger

Un ***keylogger*** (derivado del inglés: *key* ('tecla') y *logger* ('registrador'); 'registrador de teclas') es un tipo de *software* o un dispositivo *hardware* específico que se encarga de registrar las pulsaciones que se realizan en el teclado, para posteriormente memorizarlas en un fichero o enviarlas a través de internet.

Suele usarse como *malware* del tipo  daemon, permitiendo que otros usuarios tengan acceso a contraseñas importantes, como los números de una tarjeta de crédito, u otro tipo de información privada que se quiera obtener.

El registro de pulsaciones de teclas también puede utilizarse para supervisar las actividades de los niños en escuelas o en el hogar, por parte de empleadores para monitorear a los empleados, así como por las fuerzas del orden para investigar un uso malicioso.

El registro de lo que se teclea puede hacerse tanto con medios de hardware como de software. Los sistemas comerciales disponibles incluyen dispositivos que pueden conectarse al cable del teclado (lo que los hace inmediatamente disponibles pero visibles si un usuario revisa el teclado) y al teclado mismo (que no se ven pero que se necesita algún conocimiento de como soldarlos para instalarlos en el teclado). Escribir aplicaciones para realizar *keylogging* es trivial y, como cualquier programa computacional, puede ser distribuido a través de un troyano o como parte de un virus informático o gusano informático. Incluso puede alterar las búsquedas en Google, creando búsquedas inexistentes y otras páginas adicionales. Se suele descargar comprimido para eludir antivirus. Se dice que se puede utilizar un teclado virtual para evitar esto, ya que sólo requiere clics del ratón. Sin embargo, las aplicaciones más nuevas también registran *screenshots* al realizarse un clic, que anulan la seguridad de esta medida.

 Funcionamiento
El registro de las pulsaciones del teclado se puede alcanzar por medio de *hardware* y de *software* usando las teclas para teclear en el teclado:

 Keylogger con hardware

Son dispositivos disponibles en el mercado que vienen en dos tipos:
 **Adaptadores** en línea que se intercalan en la conexión del teclado, tienen la ventaja de poder ser instalados inmediatamente. Sin embargo, mientras que pueden ser a veces inadvertidos se detectan fácilmente con una revisión visual detallada.
 **Dispositivos** que se pueden instalar dentro de los teclados estándares, requiere de habilidad para soldar y de tener acceso al teclado que se modificará. No son detectables a menos que se abra el cuerpo del teclado.

 Keylogger con software
Contrariamente a las creencias populares, el código de un *keylogger* por software es simple de escribir, con un conocimiento básico de la API proporcionada por el sistema operativo objetivo. Los *keyloggers* de software se dividen en:
 **Basado en núcleo**: este método es el más difícil de escribir, y también de combatir. Tales keyloggers residen en el nivel del núcleo y son así prácticamente invisibles. Derriban el núcleo del sistema operativo y tienen casi siempre el acceso autorizado al hardware que los hace de gran alcance. Un *keylogger* que usa este método puede actuar como *driver* del teclado por ejemplo, y accede así a cualquier información registrada en el teclado mientras que va al sistema operativo. En 2017, los investigadores de seguridad encontraron un keylogger en el driver de algunos portátiles HP.
 **Enganchados**: estos keyloggers registran las pulsaciones de las teclas del teclado con las funciones proporcionadas por el sistema operativo. El sistema operativo activa el *keylogger* en cualquier momento en que se presione una tecla, y realiza el registro.
 **Métodos creativos**: aquí el programador utiliza funciones como GetAsyncKeyState, GetForegroundWindow, etc. Estos son los más fáciles de escribir, pero como requieren la revisión del estado de cada tecla varias veces por segundo, pueden causar un aumento sensible en uso de la CPU y pueden ocasionalmente dejar escapar algunas pulsaciones del teclado.

 Protección

En algunas computadoras podemos darnos cuenta si están infectadas por un keylogger (dependiendo de la velocidad y uso de CPU de nuestro procesador) por el hecho de que el programa registrará cada una de nuestras teclas de la siguiente manera: FicheroLog = FicheroLog + UltimaTecla, este evento será ejecutado por el keylogger cada vez que el usuario presione una tecla. Si bien este evento no será una carga relevante para nuestro procesador si se ejecuta a una velocidad normal, pero si mantienes unas 10 teclas presionadas por unos 30 segundos con la palma de tu mano y tu sistema se congela o su funcionamiento es demasiado lento podríamos sospechar que un keylogger se ejecuta sobre nuestro computador.

Otro signo de que un keylogger se está ejecutando en nuestro computador es el problema de la tilde doble (´´) al presionar la tecla para acentuar vocales, salen dos tildes seguidas y la vocal sin acentuar. Esto ocurre en keyloggers configurados para otros idiomas.

 *Anti-spyware*
Los programas *Anti-spyware* pueden detectar diversos keyloggers y limpiarlos. Vendedores responsables de supervisar la detección del *software* apoyan la detección de keyloggers, así previniendo el abuso del *software*.

 *Firewall*
Habilitar un cortafuegos o *firewall* puede salvar el sistema del usuario no solo del ataque de keyloggers, sino que también puede prevenir la descarga de archivos sospechosos, troyanos, virus, y otros tipos de *malware*.

 Monitores de red
Los monitores de red (llamados también cortafuegos inversos) se pueden utilizar para alertar al usuario cuando el keylogger use una conexión de red. Esto da al usuario la posibilidad de evitar que el keylogger envíe la información obtenida a terceros.

 Software *anti-keylogging*
El software para la detección de *keyloggers* está también disponible. Este tipo de software graba una lista de todos los keyloggers conocidos. Los usuarios legítimos del PC pueden entonces hacer, periódicamente, una exploración de esta lista, y el *software* busca los artículos de la lista en el disco duro. Una desventaja de este procedimiento es que protege solamente contra los keyloggers listados, siendo vulnerable a los keyloggers desconocidos o relativamente nuevos.
Incluso Microsoft ha admitido públicamente que el sistema operativo Windows 10 tiene un keylogger integrada en su versión final "para mejorar los servicios de entrada y de la escritura". En el caso de Windows 10 y keylogging, basta con cambiar algunos parámetros de privacidad en su ordenador.

 Contraseña de un solo uso
Otra forma común de proteger los códigos de acceso para que no sean robados por los registradores de pulsaciones de teclas es pedir a los usuarios que proporcionen algunos caracteres seleccionados al azar de su código de autenticación. Por ejemplo, es posible que se les solicite que ingresen los caracteres segundo, quinto y octavo. Incluso si alguien está observando al usuario o usando un registrador de pulsaciones de teclas, solo obtendrá unos pocos caracteres del código sin conocer sus posiciones.

Referencias

 Enlaces externos
