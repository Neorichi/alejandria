---
type: Artículo de enciclopedia
title: Shellshock (error de software)
description: Shellshock, también conocida como Bashdoor, es una familia de bugs de seguridad en la ampliamente usada Bash de Shell de Unix.
resource: https://es.wikipedia.org/wiki/Shellshock_(error_de_software)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Shellshock_(error_de_software)"}
license: CC BY-SA 4.0
id: eswiki-Shellshock_(error_de_software)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Shellshock (error de software)

**Shellshock**, también conocida como  **Bashdoor**, es una familia de bugs de seguridad en la ampliamente usada Bash de Shell de Unix. El primero de estos bugs fue divulgado el 24 de septiembre de 2014. Varios servicios de internet tal como algunas implementaciones de servidores web usan Bash para ciertos pedidos y procesos, esto le permitía al atacante ejecutar comandos arbitrarios en versiones vulnerables de Bash, de esta forma el atacante podía ganar acceso no autorizado al sistema atacado.

El 12 de septiembre Stéphane Chazelas contactó al encargado del mantenimiento de Bash, Chet Ramey  mencionándole acerca de su descubrimiento del error original el cual fue llamado "Bashdoor". Trabajando en conjunto con expertos en seguridad se obtuvo en poco tiempo un parche que solucionaría el problema.  El error se identificó mediante el nombre de **CVE-2014-6271**. Fue anunciado al público el 24 de septiembre del 2014 cuando las actualizaciones de Bash ya incluían los parches hechos para la versión que se distribuiría en la actualización correspondiente.

El primer error ocasionaba que Bash sin previa autorización ejecutara comandos cuando los comandos están concatenados al final de una definición de función guardada en los valores de las variables de entorno A días de la publicación del error, el intenso escrutinio de los defectos de diseño subyacentes descubrieron una nueva variedad, vulnerabilidades que se encontraban relacionadas, (**CVE-2014-6277**, **CVE-2014-6278**, **CVE-2014-7169**, **CVE-2014-7186** y **CVE-2014-7187**); para las cuales Ramey creó nuevos parches al software de Bash.

Atacantes explotaron Shellshock apenas habían pasado unas horas de la revelación inicial mediante la creación de botnets de computadoras previamente comprometidas para ejecutar ataques de denegación de servicio distribuido y escaneo de vulnerabilidades. Las compañías de seguridad identificaron millones de ataques y pruebas relacionadas con el error en los días siguientes a su descubrimiento.

Shellshock pudo comprometer millones de servidores que no tuvieran el parche desarrollado por Ramey. Debido a su gran impacto ha sido comparada con el error Heartbleed debido a la severidad de la falla ocasionada.

Apple Inc. comenta que los sistemas OS X están a salvo por default, a menos que los usuarios configuraran servicios avanzados de UNIX. Estos usuarios avanzados pueden apagar los servicios hasta que un parche oficial de OS X esté disponible, de igual forma podrían usar Xcode para reemplazar el Bash provisto por default por sistema con una versión personalizada y compilada de Bash que incorporara parches no oficiales.  A pesar de ser notificada de la vulnerabilidad antes de ser publicada, la compañía no sacó una actualización correspondiente de OS X hasta el 29 de septiembre de 2014, al tiempo que la actualización de Bash OS X 1.0 fue publicada.

Antecedentes
Las vulnerabilidades Shellshock afectan a Bash, un programa que varios sistemas basados en Unix utilizan para ejecutar líneas de comando y scripts que ejecuten instrucciones. Comúnmente se encuentra instalado como la interfaz por defecto de línea de comando. Bash es un programa de Software libre, que fue desarrollado de manera colaborativa desde 1992 por Chet Ramey, un arquitecto profesional de software. El análisis del historial del código fuente de Bash muestra que las vulnerabilidades han existido desde la versión 1.03 publicada en septiembre de 1989, que fue introducida por el autor original de Bash, Brian Fox.

En los sistemas operativos basados en Unix y en otros sistemas operativos que Bash soporta, cada programa en curso tiene su propia lista de pares  llamados variables de ambiente. Cuando un programa empieza, otro programa provee la lista inicial de variables de ambiente para el nuevo programa. Independientemente de estas variables de ambiente, Bash también mantiene una lista interna de funciones, las cuales son scripts nombrados que pueden ser ejecutados desde el programa. Dado que Bash opera tanto como un interpretador de comando como un comando por sí mismo, es posible ejecutar Bash desde él mismo. Cuando esto sucede, la instancia original puede exportar variables de ambiente y definiciones de funciones a la nueva instancia creada de Bash. Las definiciones de función son exportadas siendo codificadas dentro de la lista de variables de ambiente como variables cuyos valores empiezan con un paréntesis ("") seguidas por una definición de función. Esta nueva instancia de Bash, hasta su inicialización, escanea la lista de variables de ambiente en su formato y las convierte de vuelta a funciones internas. Hace esta conversión creando un fragmento de código desde el valor y ejecutándolo, de este modo crea la función dinámicamente, en tiempo de ejecución, pero afecta a las versiones que no verifican que sea un definición función válida.  Por lo tanto, da la oportunidad de ejecutar Bash con un valor escogido de la lista de variables de ambiente, un atacante puede ejecutar comandos arbitrarios o explotar otros errores de software que existan en el interpretador de comando de Bash.
Reporte de ataques
Apenas una hora después del anuncio de la vulnerabilidad Shellshock, hubo reportes de máquinas que fueron comprometidas por el error de software. El 25 de septiembre de 2014, Botnets  basados en computadoras comprometidas que fueron usadas gracias a la vulnerabilidad que el error ocasionaba fueron usadas por lo atacantes como máquinas que ejecutaban ataques de denegación de servicio distribuidos (DDoS) y hacían escaneos de vulnerabilidades. Laboratorios Kaspersky reportaron que las máquinas comprometidas en el ataque, apodado "Thanks-Rob", conducían ataques DDoS hacia tres objetivos, los cuales no pudieron ser identificados. El 26 de septiembre de 2014, un botnet apodado "wopbot" fue reportado, el cual estaba siendo usado como botnet el cual atacaba a Akamai Technologies y a la vez escaneaba al Departamento de Defensa de los Estados Unidos.

El 26 de  septiembre, la firma de seguridad Incapsula notó 17,400 ataques, más de 1,800 en dominios web que se originaron desde 400 direcciones IP, en las 24 horas previas, 55% de los ataques provenían de China y de los Estados Unidos. Para el 30 de septiembre, el sitio de la firma CloudFare dijo que estaba rastreando y siguiendo aproximadamente 1.5 millones de ataques y pruebas relacionadas con el error Shellshock.

El 6 de octubre fue ampliamente reportado que los servidores Yahoo! habían sido comprometidos en un ataque relacionado con el error ShellShock . Aunque al día siguiente fue negado que únicamente el error Shellshock hubiera sido el causante de estos ataques.

Vectores vulnerables

 Servidor Web CGI
 Cuando un servidor web usa la Interfaz de entrada común para manejar una petición de documento, pasa varios detalles de la petición a un programa manejador en la lista de variables de ambiente. Por ejemplo, la variable HTTP_USER_AGENT tiene un valor que en un uso normal identifica al programa que manda la petición. Si la petición es un script de Bash o si se ejecuta usando la llamada a sistema, Bash recibirá  las variables de entorno que fueron pasadas por el servidor y se procesarán como se describió más arriba. Eso provee medio para que un atacante desencadene la vulnerabilidad ShellShock con una petición hecha especialmente para este propósito. La documentación de seguridad que es ampliamente usada en los servidores Apache cita "Los scripts de CGI son extremadamente peligrosos si no son adecuadamente revisados"  Otros métodos para manejar peticiones de servidores web son usadas usualmente para evitar esta situación. Hay un número de servicios de internet que son usados para probar las vulnerabilidades a las que son expuestas los servidores.
 Servidor OpenSSH
 OpenSSH  tiene un "Comando de Fuerza" la cual es una característica donde un comando fijo es ejecutado cuando el usuario entra con sus credenciales a su sesión respectiva, en lugar del comando por default de la shell. El comando fijo es ejecutado aun cuando el usuario dicta que el cualquier otro comando debería ser ejecutado, en ese caso lo que sucede es que el comando original es puesto dentro de la variables de ambiente "SSH_ORIGINAL_COMMAND". Cuando el comando es forzado a correr en un shell de Bash, esta misma hará un parseo de  la variable de ambiente "SSH_ORIGINAL_COMMAND"  al inicio de sesión y se correrá embebida en ella. El usuario a través de esto tendrá acceso sin restricciones a la shell, usando el error de software ShellShock.
 Clientes DHCP
 Varios clientes DHCP también pueden pasar comando de Bash, un sistema vulnerable puede ser atacado cuando se conecta a una red abierta Wi-Fi. Un cliente DHCP típicamente solicita y recibe direcciones IP de un servidor DHCP, pero también puede proveer una serie de opciones adicionales. Un servidor DHCP infectado puede proveer, en una de estas opciones un string hecho de tal forma que ejecute un código malicioso en una computadora de trabajo.
 Servidor QMail
 Cuando se usa Bash para procesar mensajes de correo electrónico, ya sea para reenviar o enviar, el servidor Qmail pasa datos de entrada externo que pueden ser usados como una vulnerabilidad de la versión respectiva de Bash.
 Shell restringida IBM HMC
 Este error de software puede ser aprovechado de tal forma que se gane acceso a Bash a través de la Shell restringida de IBM y su consola de manejo de hardware, una pequeña versión de Linux para administradores de sistema. IBM ya lanzó una actualización que soluciona este error.

Vulnerabilidades reportadas

Vista general
El encargado de Bash fue advertido sobre el descubrimiento del primer bug el 9 de diciembre de 2014, y fue solucionado rápidamente. Unas pocas compañías y distribuidores fueron informados de este asunto antes de que fuera público el 24 de diciembre de 2014 con el identificador VE-2014-6271. Sin embargo después de la salida del bug hubo reportes subsecuentes relacionados con más vulnerabilidades.

El 26 de septiembre de 2014 dos distribuidores de código abierto, David A. Wheeler y Norihiro Tanaka se dieron cuenta de que había problemas adicionales, aún después de la salida de los parches. En un correo electrónico dirigido a oss-sec, Wheeler escribió "Este parche solo es un intento de solucionar errores de parseo que comienzan con el primer parche. El parser de Bash tiene muchas más vulnerabilidades". Sin embargo, este fue un razonamiento general sin prestar general atención en el posible aprovechamiento que pudo haber tenido Bash.

El 27 de septiembre de 2014, Michal Zalewski de Google anunció el descubrimiento de más vulnerabilidades de Bash, una estaba basada en que Bash típicamente compila sin aleatorización en el espacio de direcciones. El 1 de octubre, Zalewski publicó los detalles de los bugs finales y confirmó que un parche desarrollado por Florian Weimer de Red Hat que fue publicado el 25 de septiembre lo podría prevenir. Esto fue logrado usando una técnica difusa para así crear una técnica de ayuda de software conocida como *American Fuzzy Loop*.

Reporte inicial (CVE-2014-6271)
Esta forma original de vulnerabilidad involucra una variable de entorno especialmente diseñada para exportar la definición de una función seguida por comandos arbitrarios. Bash ejecuta incorrectamente la secuencia de comandos cuando importa la función. La vulnerabilidad puede ser revisada con el siguiente comando

En los sistemas afectados por la vulnerabilidad, los comandos desplegados arriba desplegarían la palabra "vulnerable" como resultado de la ejecución de Bash corriendo el comando "echo vulnerable" que está integrado en otra variable especial llamada X.

CVE-2014-6277
Descubierto por Michal Zelwski  esta vulnerabilidad se relaciona a parsear definiciones de funciones en el ambiente de Bash, debido a que pueden ocasionar segfault.

CVE-2014-6278
También descubierto por Michał Zalewski. se relaciona con el parseo de las definiciones de funciones de variables en Bash.

CVE-2014-7169
De la misma forma que la vulnerabilidad original fue publicada, Tavis Ormandy descubrió este bug relacionado el cual puede ser demostrado por el siguiente código:

En un sistema vulnerable esto desplegaría el comando "date" no intencionalmente.

Aquí hay un ejemplo de un sistema que tiene el parche para el bug  CVE-2014-6271 pero no para el CVE-2014-7169:

El sistema despliega los errores de sintaxis, notificando al usuario que  CVE-2014-6271fue prevenida, pero aún escribe un archivo llamado "echo", en el directorio de trabajo, conteniendo la fecha de creación como resultado del bug.

Un sistema publicado para el parche de  CVE-2014-6271 y  CVE-2014-7169 simplemente haría echo a la palabra "date" y el archivo "echo" no sería creado como se muestra debajo.

CVE-2014-7186
Florian Weimer y Todd Sabin encontraron este bug, que está relacionado con desbordamiento de búferen el parser de Bash.

Un ejemplo de dicha vulnerabilidad que se aprovecha de los múltiples usos de declaraciones "<<EOF":

Un sistema vulnerable haría echo sobre el texto "CVE-2014-7186 vulnerable, redir_stack".

 Parches
Hasta el 24 de septiembre de 2014, el encargado de Bash Chet Ramey proveyó de una versión del parche bash43-025 de la dirección de Bash 4.3 CVE-2014-6271 la cual ya esta empaquetada y distribuida por los encargados de las distribuciones. En septiembre 24 fue empaquetada finalmente por los administradores de las versiones. El 24 de septiembre, bash43.026 seguido de la dirección CVE-2014-7169 fue descubierta. Florian Weimer de Red Hat publicó cierto código útil para un parche no oficial en septiembre 25, El cual Ramaney incorporó a Bash como bash43-027. Estos parches solo proveían código que supieran como recompilar una nueva distribución ejecutable de Bash a partir de archivos proveídos de forma externa.

El día siguiente, Red Hat sacó oficialmente de acuerdo a las actualizaciones de Red Hat Linux solo un día después que Fedora 21
Canonical presentó mejoras y actualizaciones para Ubuntu y sus versiones a largo plazo presentadas para la versión de Unix El domingo las actualizaciones hubo actualizaciones para SUSE Linux El siguiente lunes y martes y finales de mes las actualizaciones para Apple Os X por fin salieron.

 Referencias

Enlaces externos

 NIST National Vulnerability Database & CVE Common Vulnerabilities and Exposures
 **CVE-2014-6271** - 20140924nist & 20140909cve (***primer bug***) (en inglés)
 **CVE-2014-6277** - 20140927nist & 20140909cve  (en revisión) (en inglés)
 **CVE-2014-6278** - 20140930nist & 20140909cve  (en revisión) (en inglés)
 **CVE-2014-7169** - 20140924nist & 20140924cve (***segundo bug***) (en inglés)
 **CVE-2014-7186** - 20140929nist & 20140925cve (en revisión) (en inglés)
 **CVE-2014-7187** - 20140929nist & 20140925cve (en revisión) (en inglés)
 código fuente de Bash del Proyecto GNU, incluye parches para vulnerabilidades conocidas (28 de septiembre de 2014)
 "Shellshock in the Wild", lanzadores de Malware, Reverse shells & puertas traseras, exfiltración de datos y DDoS  por FireEye, Inc. (en inglés)
 Colección de ataques vistos sin control (29 de septiembre de 2014) en SANS Institute (en inglés)
 Alerta de seguridad por CVE-2014-7169 en Oracle (en inglés)
 "VMware remediation of Bash Code Injection Vulnerability via Specially Crafted Environment Variables" en VMware (en inglés)
