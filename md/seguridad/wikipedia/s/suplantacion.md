---
type: Artículo de enciclopedia
title: Suplantación
description: "La suplantación de identidad o spoofing (no confundir con sniffing) en términos de seguridad de redes, hace referencia al uso de técnicas a través de las cuales un atacante, generalmente con usos maliciosos o de …"
resource: https://es.wikipedia.org/wiki/Suplantación
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Suplantación"}
license: CC BY-SA 4.0
id: eswiki-Suplantación
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Suplantación

La **suplantación de identidad** o *spoofing* (no confundir con sniffing) en términos de seguridad de redes, hace referencia al uso de técnicas a través de las cuales un atacante, generalmente con usos maliciosos o de investigación, se hace pasar por una entidad distinta a través de la falsificación de los datos en una comunicación.

 Tipos de suplantaciones

 Suplantación de IP
Consiste básicamente en sustituir la dirección IP origen de un paquete TCP/IP por otra dirección IP a la cual se desea suplantar. Esto se consigue generalmente gracias a programas destinados a ello y puede ser usado para cualquier protocolo dentro de TCP/IP como ICMP, UDP o TCP. Hay que tener en cuenta que las respuestas del host que reciba los paquetes alterados irán dirigidas a la IP original. Por ejemplo si se envía un *ping* (paquete icmp *echo request*) suplantado, la respuesta será recibida por el host al que pertenece la IP legalmente. Este tipo de *spoofing* unido al uso de peticiones de difusión a diferentes redes es usado en un tipo de ataque de inundación conocido como ataque *smurf*. Para poder realizar la suplantación de IP en sesiones TCP, se debe tener en cuenta el comportamiento de dicho protocolo con el envío de paquetes SYN y ACK con su SYN específico y teniendo en cuenta que el propietario real de la IP podría (si no se le impide de alguna manera) cortar la conexión en cualquier momento al recibir paquetes sin haberlos solicitado. También hay que tener en cuenta que los enrutadores actuales no admiten el envío de paquetes con IP origen no perteneciente a una de las redes que administra (los paquetes suplantados no sobrepasarán el enrutador).

 Suplantación de ARP

La suplantación de identidad por falsificación de tabla ARP se trata de la construcción de tramas de solicitud y respuesta ARP modificadas con el objetivo de falsear la tabla ARP (relación IP-MAC) de una víctima y forzarla a que envíe los paquetes a un host atacante en lugar de hacerlo a su destino legítimo.

El protocolo Ethernet trabaja mediante direcciones MAC, no mediante direcciones IP. ARP es el protocolo encargado de traducir direcciones IP a direcciones MAC para que la comunicación pueda establecerse; para ello cuando un host quiere comunicarse con una IP emite una trama ARP-Request a la dirección de difusión pidiendo la MAC del anfitrión poseedor de la IP con la que desea comunicarse. El ordenador con la IP solicitada responde con un ARP-Reply indicando su MAC. Los enrutadores y los *hosts* guardan una tabla local con la relación IP-MAC llamada tabla ARP. Dicha tabla ARP puede ser falseada por un ordenador atacante que imita tramas ARP-Reply indicando su MAC como destino válido para una IP específica, como por ejemplo la de un enrutador, de esta manera la información dirigida al enrutador pasaría por el ordenador atacante quien podrá escanear dicha información y redirigirla si así lo desea. El protocolo ARP trabaja a nivel de enlace de datos de OSI, por lo que esta técnica sólo puede ser utilizada en redes LAN o en cualquier caso en la parte de la red que queda antes del primer enrutador. Una manera de protegerse de esta técnica es mediante tablas ARP estáticas (siempre que las IP de red sean fijas), lo cual puede ser difícil en redes grandes.

Otras formas de protegerse incluyen el uso de programas de detección de cambios de las tablas ARP (como *Arpwatch*) y el uso de la seguridad de puerto de los conmutadores para evitar cambios en las direcciones MAC.

 Suplantación de DNS
Suplantación de identidad por nombre de dominio. Se trata del falseamiento de una relación entre nombre de dominio y una IP ante una consulta de resolución de nombre, es decir, resolver con una dirección IP falsa un cierto nombre DNS o viceversa. Esto se consigue falseando las entradas de la relación nombre de dominio e IP de un servidor DNS, mediante alguna vulnerabilidad del servidor en concreto o por su confianza hacia servidores poco fiables (DNS Rogue). Las entradas falseadas de un servidor DNS son susceptibles de infectar (envenenar) la caché DNS de otro servidor diferente (envenenamiento de DNS).

 Suplantación de web

Suplantación de una página web real (no confundir con *phishing*). Enruta la conexión de una víctima a través de una página falsa hacia otras páginas web con el objetivo de obtener información de dicha víctima (páginas web vistas, información de formularios, contraseñas etc.). La página web falsa actúa a modo de *proxy*, solicitando la información requerida por la víctima a cada servidor original y saltándose incluso la protección SSL. El atacante puede modificar cualquier información desde y hacia cualquier servidor que la víctima visite. La víctima puede abrir la página web falsa mediante cualquier tipo de engaño, incluso abriendo un simple enlace. La suplantación de web es difícilmente detectable; quizá la mejor medida es algún complemento del navegador que muestre en todo momento la IP del servidor visitado: si la IP nunca cambia al visitar diferentes páginas web significará que probablemente se esté sufriendo este tipo de ataque. Este ataque se realiza mediante una implantación de código el cual robará la información. Usualmente se realizan páginas fantasmas en las cuales se inyectan estos códigos para poder sacar información de las víctimas.

 Suplantación de correo electrónico

Suplantación de la dirección de correo electrónico de otras personas o entidades. Esta técnica es usada con asiduidad para enviar bulos por correo electrónico como complemento perfecto para la suplantación de identidad y para enviar mensajes basura, ya que es sencilla y solo requiere utilizar un servidor SMTP configurado para tal fin. Para protegerse se debería comprobar la IP del remitente (para averiguar si realmente esa ip pertenece a la entidad que indica en el mensaje) y la dirección del servidor SMTP utilizado.
Las medidas recomendadas para prevenir estos ataques son crear registros SPF y firmas digitales DKIM.

 Suplantación de GPS
Un ataque de suplantación de GPS intenta engañar a un receptor de GPS transmitiendo una señal ligeramente más poderosa que la recibida desde los satélites del sistema GPS, estructurada para parecerse a un conjunto normal de señales GPS. Sin embargo estas señales están modificadas de tal forma de que causarán que el receptor determine una posición diferente a la real, específicamente algún lugar determinado por la señal atacante. Debido a que el sistema GPS trabaja midiendo el tiempo que le toma a una señal el viajar entre el satélite y el receptor, una suplantación exitosa requiere que el atacante conozca con precisión donde se encuentra el blanco de tal forma que la señal falsa pueda ser estructurada con el retraso apropiado.

Un ataque de suplantación de GPS comienza con la transmisión de una señal ligeramente más poderosa que la que entrega la posición correcta, y luego se comienza a desviar lentamente hacia la posición deseada por el atacante, ya que si esto se hace demasiado rápido el receptor atacado perderá la fijación en la señal, en cuyo momento el ataque de suplantación solo funcionaría como un ataque de perturbación. Se ha sugerido que la captura de un Lockheed RQ-170 en el noreste de Irán en diciembre de 2011, fue el resultado de un ataque de este tipo. Previamente los ataques de suplantación de GPS habían sido predichos y discutidos en la comunidad GPS, pero aún no han sido confirmado un ejemplo conocido de un ataque de suplantación malicioso.

Una prueba de concepto de este ataque se realizó con éxito en junio de 2013, cuando el yate de lujo White Rose fue mal dirigido con señales GPS falsificadas desde Mónaco a la isla de Rodas por un grupo de estudiantes de ingeniería aeroespacial de la Escuela de Ingeniería Cockrell de la Universidad de Texas en Austin. Los estudiantes estaban a bordo del yate, lo que permitió a su equipo de suplantación dominar progresivamente la intensidad de señal de los satélites GPS reales, alterando el curso de la embarcación. Previamente, en el año 2012, este mismo grupo de estudiantes fue capaz de cambiar el curso de vuelo de un vehículo aéreo no tripulado mediante el uso de la misma técnica de suplantación de GPS.

 Suplantación de facial recognition
La tecnología de reconocimiento facial se utiliza ampliamente en diversas áreas, como controles de inmigración y seguridad de teléfonos, así como en plataformas populares como Airbnb y Uber para validar la identidad de las personas. Sin embargo, este aumento en el uso ha vuelto al sistema más vulnerable a ataques, ya que los sistemas de reconocimiento facial se han vuelto más comunes en la sociedad. Algunas fuentes en línea y tutoriales explican cómo las personas pueden engañar a los sistemas de reconocimiento facial utilizando imágenes, máscaras o modelos impresos en 3D en lo que se conoce como suplantación facial o ataques de presentación. Estas tácticas pueden llevar a peligros en términos de obtener acceso no autorizado. Por lo tanto, medidas como comprobaciones de vitalidad que verifican el parpadeo, el aprendizaje profundo y cámaras especiales como cámaras 3D para capturar imágenes con profundidad pueden ayudar a prevenir la suplantación de reconocimiento facial. Es importante utilizar medidas de seguridad integrales como estas para protegerse contra intentos de suplantación facial y mantener la seguridad y la integridad general de los sistemas que requieren autenticación mediante reconocimiento facial.

 Véase también
Sniffing
MAC
 ARP
 Router
 TCP
 UDP
 IP
 SSL
 Plugin
 Hoax
 SMTP
 Hijacking
 Phishing
 Smishing
 Falsificación de documentos de identidad

 Referencias

 Enlaces externos
 ¿Cómo detectar spoofing?
