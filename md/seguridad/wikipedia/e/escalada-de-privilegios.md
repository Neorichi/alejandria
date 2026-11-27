---
type: Artículo de enciclopedia
title: Escalada de privilegios
description: "La escalada de privilegios es el acto de explotar un error, un fallo de diseño o una supervisión de la configuración en un sistema operativo o una aplicación de software para obtener un acceso elevado a los recursos que …"
resource: https://es.wikipedia.org/wiki/Escalada_de_privilegios
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Escalada_de_privilegios"}
license: CC BY-SA 4.0
id: eswiki-Escalada_de_privilegios
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Escalada de privilegios

La **escalada de privilegios** es el acto de explotar un error, un fallo de diseño o una supervisión de la configuración en un sistema operativo o una aplicación de software para obtener un acceso elevado a los recursos que normalmente están protegidos de una aplicación o un usuario. El resultado es que una aplicación con más privilegios de los previstos por el desarrollador de la aplicación o el administrador del sistema puede realizar acciones no autorizadas. Consiste en aprovechar vulnerabilidades del sistema como archivos o servicios mal configurados para poder ejecutar scripts o exploits con privilegios de superusuario.

 Antecedentes
La mayoría de los sistemas informáticos están diseñados para ser utilizados con múltiples cuentas de usuario, cada una de las cuales tiene habilidades conocidas como privilegios. Los privilegios comunes incluyen la visualización y edición de archivos, o la modificación de los archivos del sistema.

La escalada de privilegios significa que un usuario recibe privilegios a los que no tiene derecho. Estos privilegios pueden utilizarse para eliminar archivos, ver información privada o instalar programas no deseados, como virus. Suele ocurrir cuando un sistema tiene un fallo que permite eludir la seguridad o, alternativamente, tiene suposiciones de diseño erróneas sobre cómo se utilizará. La escalada de privilegios se produce de dos formas:

 **Escalada vertical de privilegios**, también conocida como *elevación de privilegios*, en la que un usuario o aplicación con menos privilegios accede a funciones o contenidos reservados para usuarios o aplicaciones con más privilegios (por ejemplo, los usuarios de la banca por Internet pueden acceder a funciones administrativas del sitio o se puede eludir la contraseña de un teléfono inteligente).
 **Escalada horizontal de privilegios**, en la que un usuario normal accede a funciones o contenidos reservados para otros usuarios normales (por ejemplo, el usuario A de la banca por Internet accede a la cuenta bancaria por Internet del usuario B)

 Vertical

Este tipo de escalada de privilegios se produce cuando el usuario o el proceso puede obtener un nivel de acceso más alto del que pretendía un administrador o un desarrollador de sistemas, posiblemente mediante la realización de operaciones a nivel del núcleo.

 Ejemplos

 Mediante un usuario de la empresa, el atacante hurgará hasta encontrar una vulnerabilidad del usuario administrador que pueda explotar para poder conseguir privilegios de administrador.
 Algunos servicios de Windows están configurados para funcionar con la cuenta de usuario del Sistema Local. Una vulnerabilidad como el desbordamiento de búfer puede utilizarse para ejecutar código arbitrario con privilegios elevados al Sistema Local. Alternativamente, un servicio del sistema que se hace pasar por un usuario menor puede elevar los privilegios de ese usuario si los errores no se manejan correctamente mientras el usuario se hace pasar por él (por ejemplo, si el usuario ha introducido un manejador de errores malintencionado).
 En algunas versiones anteriores del sistema operativo Microsoft Windows, el salvapantallas de *Todos los Usuarios* se ejecuta en la cuenta del Sistema Local, por lo que cualquier cuenta que pueda sustituir al binario actual del salvapantallas en el sistema de archivos o el Registro puede, por lo tanto, elevar los privilegios.
 En ciertas versiones del núcleo Linux era posible escribir un programa que estableciera su directorio actual en /etc/cron.d, solicitar que se realizara un volcado de memoria en caso de que éste fallara y luego se ejecutara el comando kill por otro proceso. El archivo de volcado del núcleo se habría colocado en el directorio actual del programa, es decir, /etc/cron.d, y cron lo habría tratado como un archivo de texto instruyéndolo para ejecutar los programas según lo previsto. Debido a que el contenido del archivo estaría bajo el control del atacante, éste podría ejecutar cualquier programa con privilegios de superusuario.
 Cross-zone scripting es un tipo de ataque de escalada de privilegios en el que un sitio web subvierte el modelo de seguridad de los navegadores web, permitiéndole así ejecutar código malicioso en los ordenadores clientes.
 También hay situaciones en las que una aplicación puede utilizar otros servicios de alto privilegio y tiene suposiciones incorrectas acerca de cómo un cliente podría manipular su uso de estos servicios. Una aplicación que puede ejecutar comandos de línea de comandos o comandos de shell podría tener una vulnerabilidad de *Inyección de Shell* si utiliza una entrada no validada como parte de un comando ejecutado. Un atacante podría entonces ejecutar comandos de sistema usando los privilegios de la aplicación.
 Las calculadores de Texas Instruments (en particular la TI-85 y la TI-82) fueron diseñadas originalmente para usar solo programas interpretados escritos en dialectos de TI-BASIC; sin embargo, después de que los usuarios descubrieron errores que podían ser explotados para permitir que el código nativo Z-80 se ejecutara en el hardware de la calculadora, TI liberó datos de programación para apoyar el desarrollo de terceros. (Esto no continuó con el TI-Nspire basado en ARM, para el cual se han encontrado *jailbreaks* usando Ndless pero que aún son combatidas activamente por Texas Instruments).
 Algunas versiones del iPhone permiten a un usuario no autorizado acceder al teléfono mientras está bloqueado.

 Jailbreaking
*Artículo principal: Jailbreak IOS*

El **jailbreak** es el acto o la herramienta que se utiliza para realizar el acto de escapar de una chroot o de un *jail* en sistemas operativos de tipo UNIX-like o para eludir la gestión de derechos digitales (DRM). En el primer caso, permite al usuario ver archivos fuera del sistema de archivos que el administrador pretende poner a disposición de la aplicación o el usuario en cuestión. En el contexto de la DRM, esto permite al usuario ejecutar código definido arbitrariamente en dispositivos con DRM, así como romper las restricciones de tipo chroot. El término se originó en la comunidad de delincuentes de iPhone/iOS y también se ha utilizado como término para el pirateo de PlayStation Portable; estos dispositivos han sido objeto repetidamente de *jail*, lo que ha permitido la ejecución de código arbitrario, y a veces han sido desactivados por las actualizaciones de los proveedores.

Los sistemas iOS, incluidos el iPhone, el iPad y el iPod touch, han sido objeto de los esfuerzos de iOS jailbreaking desde su lanzamiento, y continúan con cada actualización de firmware. Las herramientas de iOS jailbreaking incluyen la opción de instalar Cydia o Sileo, alternativas de terceros a la App Store, como una forma de encontrar e instalar ajustes y binarios del sistema. Para evitar que iOS se rompa mediante un jailbreak, Apple ha hecho que la ROM de arranque del dispositivo ejecute comprobaciones de los *blobs SHSH* con el fin de no permitir la subida de kernels personalizados y evitar que el software se reduzca a un firmware anterior que se pueda romper el *jail*. En un *jailbreak* "sin ataduras", el entorno de iBoot se cambia para ejecutar un *exploit* de la ROM de arranque y permitir el envío de un cargador de arranque de bajo nivel parcheado o hackear el kernel para enviar el kernel fugado después de la comprobación SHSH.

Existe un método similar de evasión de jailbreak para los teléfonos inteligentes de la plataforma S60, donde utilidades como HelloOX permiten la ejecución de código no firmado y el acceso total a los archivos del sistema. o el firmware editado (similar al firmware pirateado M33 utilizado para la PlayStation Portable) para eludir las restricciones del código no firmado. Desde entonces, Nokia ha emitido actualizaciones para frenar el jailbreak, de manera similar a Apple.

En el caso de las consolas de juego, el jailbreak se utiliza a menudo para ejecutar juegos caseros. En 2011, Sony, con la ayuda del bufete de abogados Kilpatrick Stockton, demandó a George Hotz, de 21 años de edad, y a los asociados del grupo fail0verflow por haber violado el jailbreak de la PlayStation 3 (véase Sony Computer Entertainment America contra George Hotz y PlayStation Jailbreak).

 Android
*Artículo principal: Android rooting*

Los teléfonos Android pueden *rootearse* oficialmente ya sea pasando por un proceso controlado por los fabricantes, usando un *exploit* para *rootearse* o flasheando la recuperación personalizada. Los fabricantes permiten el *rooting* a través de un proceso que ellos controlan, mientras que algunos permiten el *rooting* del teléfono simplemente pulsando combinaciones de teclas específicas en el momento del arranque, o por otros métodos autoadministrados. El uso de un método de los fabricantes casi siempre anula la garantía de forma permanente, incluso si el dispositivo se desinstala y se vuelve a encender. Los *exploits* de software suelen tener como objetivo un proceso a nivel de raíz accesible para el usuario, utilizando un *exploit* específico del núcleo del teléfono, o utilizando un *exploit* de Android conocido que ha sido parcheado en versiones más recientes; no actualizando el teléfono, o degradando intencionadamente la versión.

 Estrategias de mitigación

 Prevención de ejecución de datos
 Aleatoriedad en la disposición del espacio de direcciones (para hacer más difícil que los desbordamientos de búferes ejecuten instrucciones privilegiadas en direcciones conocidas en la memoria)
 Ejecutar las aplicaciones con menos privilegios (por ejemplo, ejecutando Internet Explorer con el SID del administrador desactivado en el token del proceso) a fin de reducir la posibilidad de que los *exploits* de desbordamiento de búfer abusen de los privilegios de un usuario elevado.
 Requerir que el código del modo del núcleo esté firmado digitalmente.
 Parchear
 Uso de compiladores que atrapan los desbordamientos del buffer.
 Cifrado de los componentes de software o firmware.
 Uso de un sistema operativo con Controles de Acceso Obligatorio (MAC) como SELinux.
Investigaciones recientes han demostrado qué puede proporcionar protección eficaz contraataques de escalada de privilegios. Entre ellas se incluye la propuesta del observador de kernel adicional (AKO), que previene específicamente ataques centrados en vulnerabilidades del sistema operativo. Las investigaciones muestran que AKO es, de hecho, eficaz contra los ataques de escalada de privilegios.

 Horizontal
La escalada horizontal de privilegios se produce cuando una aplicación permite al atacante acceder a recursos que normalmente estarían protegidos de una aplicación o un usuario. El resultado es que la aplicación realiza acciones con el mismo usuario pero en un contexto de seguridad diferente al previsto por el desarrollador de la aplicación o el administrador del sistema; se trata efectivamente de una forma limitada de escalada de privilegios (concretamente, la asunción no autorizada de la capacidad de hacerse pasar por otros usuarios).

 Ejemplos
Este problema se produce a menudo en las aplicaciones web.

 El atacante suplanta a un usuario de su mismo nivel para obtener acceso a archivos privados de este. En ataques a aplicaciones web, por ejemplo, a la web de un banco donde, el atacante utiliza los mensajes HTML del servidor para comprender la estructura con la que se ha creado la base de datos y a raíz de eso utilizar por ejemplo una inyección SQL para autenticarse como otro usuario y robar sus datos.

Esta actividad maliciosa puede ser posible debido a las debilidades o vulnerabilidades comunes de las aplicaciones web.

Entre las posibles vulnerabilidades o situaciones de la aplicación web que pueden dar lugar a esta condición se incluyen:

 Los identificadores de sesión predecibles en la cookie HTTP del usuario
 Fijación de sesión
 Cross-site scripting
 Contraseñas fáciles de adivinar
 Robo o secuestro de cookies de sesión
 Keyloggers

 Véase también

 Programación defensiva
 Número ilegal
 Principio de mínimo privilegio
 Separación de privilegios
 Android rooting
 Privacidad

 Referencias
