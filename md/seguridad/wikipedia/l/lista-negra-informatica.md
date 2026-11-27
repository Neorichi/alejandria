---
type: Artículo de enciclopedia
title: Lista negra (informática)
description: "En informática, una lista negra, lista de bloqueados, lista de denegación o lista de elementos bloqueados es un mecanismo de control de acceso básico que permite acceder y utilizar elementos como direcciones de correo …"
resource: https://es.wikipedia.org/wiki/Lista_negra_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Lista_negra_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Lista_negra_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Lista negra (informática)

En informática, una **lista negra**, **lista de bloqueados**,  **lista de denegación** o **lista de elementos bloqueados** es un mecanismo de control de acceso básico que permite acceder y utilizar elementos como direcciones de correo electrónico, usuarios, contraseñas, URLs, direcciones IP, nombres de dominio, *hashes* de archivos, etc menos los indicados explícitamente en la lista. Los elementos indicados en la lista tendrán el acceso denegado. Lo contrario es una lista blanca e indica que solo los elementos indicados en la lista están autorizados para acceder a ellos y utilizarlos independientemente de su ubicación. Una lista gris contiene elementos bloqueados temporalmente (o temporalmente permitidos) a la espera de algún paso adicional.

Las listas negras pueden utilizarse en varios puntos de una arquitectura de seguridad, como en los *hosts*, servidores web proxy, servidores DNS, servidores de correo electrónico, cortafuegos, servicios de directorio o a sistemas de autenticación de aplicaciones. El tipo de elemento bloqueado está influenciado por la ubicación del control de acceso. Por ej., los servidores DNS son muy efectivos para bloquear nombres de dominio, pero no para bloquear URLs. Un cortafuegos es muy efectivo para bloquear direcciones IP, pero no tanto para bloquear archivos maliciosos o contraseñas.

Hay varios ejemplos de aplicación de listas negras, como una compañía que no desea utilizar ciertas aplicaciones en su red o impedir el uso de contraseñas débiles, o un colegio que necesita impedir el acceso desde sus ordenadores a una lista de ciertos sitios web.

 Tendencia de la industria a alejarse del término 'lista negra'
La industria de la informática se está alejando del uso de este término, proponiendo alternativas como *lista de denegación* y *lista autorizada* o *lista de bloqueados* y *lista de permitidos*.

En junio y julio de 2020:

 GitHub publicó que cambiaría muchos "términos que pueden ser ofensivos para la comunidad de color".
 Apple Inc. publicó en su conferencia de desarrolladores que adoptarían un lenguaje técnico más inclusivo y cambiarían el término *lista negra* por *lista de denegación* y el término *lista blanca* por *lista de permitidos*.
 La fundación Linux indicó que utilizarán lenguaje neutro en el código del kernel y la documentación, y evitaría términos como *lista negra* y *esclavo*.
 El equipo de Ingeniería de Twitter declaró su intención de alejarse de algunos términos incluyendo 'lista negra' y 'lista blanca'.
 Red Hat publicó su intención de fomentar código abierto más inclusivo y evitar esos y otros términos.
 ZDNet informó de una lista de compañías que ha tomado este tipo de decisiones incluyendo a: Twitter, GitHub, Microsoft, LinkedIn, Ansible, Red Hat, Splunk, Android, Go, MySQL, PHPUnit, Curl, OpenZFS, Rust, JP Morgan y otras más.

 Ejemplos de sistemas a proteger
Las listas negras se utilizan para proteger sistemas informáticos y es probable que su contenido esté orientado al tipo de sistema a proteger.

 Sistemas de información
Un sistema de información incluye computadoras de usuarios y servidores. Una lista negra en ese contexto puede incluir cierto tipo de software no permitido en el entorno de la compañía, como por ejemplo aplicaciones P2P. Además de aplicaciones, en una lista negra pueden agregarse personas, dispositivos y sitios web.

 Correo electrónico
La mayoría de los proveedores de correo electrónico tiene la opción de poner en listas negras ciertas direcciones de correos electrónicos indeseadas. Por ejemplo, un usuario molesto de recibir muchos correos electrónicos desde la misma dirección de correo electrónico puede agregar esa dirección a la lista negra y la aplicación cliente de correo electrónico enviará directamente esos mensajes a la carpeta de correo no deseado o incluso puede eliminarlos sin notificar al usuario.

Un filtro de correo no deseado puede utilizar una lista negra de direcciones de correos electrónicos para evitar la entrega a su destino. También puede utilizar direcciones IP o nombres de dominio, desde donde se envían los correo electrónicos no deseados, para implementar un bloqueo más general.

Además de las listas negras privadas de correo electrónico, hay listas para uso público, incluyendo los de:

 La Alianza *antispam* China
 Fabel Spamsources
 Spam and Oper Relay Blocking System
 El proyecto DrMX

 Navegación web
El objetivo de las listas negras en un navegador web es evitar que el usuario acceda a páginas web maliciosas o engañosas, filtrándolas localmente. Una lista negra muy popular utilizada es Google Safe Browsing, utilizada por defecto por Firefox, Safari y Chrome.

 Nombres de usuario y contraseñas
La listas negras también pueden listar credenciales de usuarios. Es común en sistemas o sitios web que no se permita el uso ciertos nombres de usuario reservados. Esos nombres de usuario reservados son comúnmente asociados con funciones de administración del sistema.

Las listas negras de contraseñas son muy similares a las listas negras de nombres de usuario pero típicamente contienen más entradas que las listas negras de nombres de usuario. Las listas negras de contraseñas sirven para evitar que los usuarios utilicen contraseñas fáciles de conocer que podrían llevar al acceso no autorizado por parte de usuarios maliciosos. Las listas negras de contraseñas se utilizan como una capa de seguridad extra, normalmente junto con políticas de contraseñas que establecen requisitos de la longitud de la misma y/o la complejidad de los caracteres utilizados. Esto es así porque un gran número de combinaciones de contraseñas son fáciles de adivinar, como por ejemplo: "Password123" o "Qwerty123".

 Métodos de distribución
Las listas negras se distribuyen de varias maneras. Algunas son simplemente listas de correo. El método DNSBL suele utilizarlo los servicios DNS. Algunas listas utilizan rsync cuando tienen que transmitir un gran volumen de datos. Pueden utilizarse funciones de servicios Web como simples solicitudes GET o interfaces más complejos como una API RESTful.

 Ejemplos

 En Comparison of DNS blacklists tienes una lista de algunas listas negras de tipo DNS.
 Empresas como Google, Symantec y Sucuri mantienen listas negras internas de sitios webs que son conocidos por tener malware y muestran una alerta antes de dejar que el usuario ingrese al sitio.
 El software de control de contenido como DansGuardian y SquidGuard pueden funcionar como una lista negra con el fin de bloquear URLs de sitios indicados como inapropiados para un entorno laboral o educativo. Estas listas negras pueden ser obtenidas sin cargo o de proveedores comerciales.
 También existen listas negras gratuitas para el proxy Squid, tales como Blackweb
 Un firewall o un sistema de detección de intrusos (IDS por sus siglas en inglés) también pueden usar listas negras para bloquear direcciones y/o redes IP hostiles conocidas. Un ejemplo de esto puede ser el proyecto OpenBL
 Muchos esquemas de protección de copias incluyen listas negras de software.
 La empresa PasswordRBL ofrece una lista negra de contraseñas distribuidas vía RESTful API para Active Directory de Microsoft, sitios web y aplicaciones.
 Los miembros de sitios de subastas electrónicas pueden agregar a otros miembros a su lista negra personal. Esto significa que el resto de miembros no pueden realizar ofertas o realizar preguntas en sus subastas ni pueden utilizar la función "comprar ahora" en sus elementos.
 Otra forma de lista es la lista amarilla; consiste en una lista de direcciones IP de servidores de correo electrónico que normalmente envían correo electrónico de forma lícita pero algunas veces envían correo no deseado. Algunos de estos servidores son Yahoo, Hotmail y Gmail. Un servidor incluido en una lista amarilla no debería figurar en una lista negra, de forma que primero se consultaría la lista amarilla y si el servidor se encuentra en ella, no es necesario consultar listas negras.
 El programa modprobe de Linux tiene un elemento denominado blacklist modulename para ignorar módulos no deseados. Hay ocasiones donde dos o más módulos entran en conflicto con la gestión de un dispositivo o un módulo quiere gestionarlo de una forma no válida.
 Muchos navegadores web pueden consultar listas negras con sitios de suplantación para advertir a los usuarios que, sin saberlo, intentan visitar un sitio web fraudulento.
 Muchos programas de compartición de ficheros P2P utilizan listas negras para bloquear el acceso a sitios gestionados por compañías que hacen cumplir los derechos de autor. Un ejemplo es la lista negra Bluetack.

 Consideraciones de uso

Como se indicó en una conferencia reciente sobre listas negras de nombres de dominio y direcciones IP utilizadas para proteger Internet: "estas listas generalmente no se cruzan. Por lo tanto, parece que estas listas no convergen en un conjunto de indicadores maliciosos". Esta preocupación combinada con un modelo económico significa que las listas negras son una parte importante de la protección de la red, pero para que sean realmente efectivas tienen que complementarse con listas blancas y grises.

Un ejemplo puede ser la lista de bloqueados de Adblock Plus que incluye listas blancas dentro de listas negras agregando un prefijo de dos arrobas y dos tuberías a un nombre de dominio.

 Referencias
