---
type: Artículo de enciclopedia
title: Botnet
description: Botnet es un término que hace referencia a un conjunto o red de robots informáticos o bots, que se ejecutan de manera autónoma y automática.
resource: https://es.wikipedia.org/wiki/Botnet
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Botnet"}
license: CC BY-SA 4.0
id: eswiki-Botnet
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Botnet

**Botnet** es un término que hace referencia a un conjunto o red de robots informáticos o bots, que se ejecutan de manera autónoma y automática. El artífice de la botnet puede controlar todos los ordenadores/servidores infectados de forma remota.

 Formación de una Botnet
En los sistemas Windows y macOS la forma más habitual de expansión de los "bots" suele ser en la distribución de software ilícito, pese a que se puede expandir mediante cualquier software sospechoso. Este tipo de software suele contener malware el cual, una vez el programa se ejecuta, puede escanear su red de área local, disco duro, puede intentar propagarse usando vulnerabilidades conocidas de Windows, etc.

En otros entornos como UNIX, GNU/Linux o BSD la forma más clásica de ataque a servidores para construir y expandir una Botnet es por telnet o SSH por medio del sistema prueba-error: probando usuarios comunes y contraseñas al azar contra todas las IPs que se pueda de forma sistemática o bien mediante ataques a bugs muy conocidos, que los administradores pueden haber dejado sin enmendar.

Las Botnets normalmente usan servicios gratuitos de DNS para IPs dinámicas como DynDns.org, No-IP.com, & Afraid.org para apuntar a un subdominio al cual el creador puede conectarse en caso de que le cierren el servidor de IRC. En muchas ocasiones basta con avisar a estos proveedores para que cancelen su cuenta y de esta manera desarticular la Botnet completa.

Afortunadamente la estructura de servidores de la botnet tiene vulnerabilidades inherentes a su arquitectura. Por ejemplo, si se encuentra el servidor de IRC y el canal, se tiene acceso a la botnet completa, con lo cual al servidor de IRC le basta con cerrar el canal o poner una g-line o k-line a las ips que intenten entrar a dicho canal.

No obstante existen construcciones más refinadas de estas botnets que tienen una lista de servidores alternativos en caso de que pase esto. Otras veces, en cambio, los bots están configurados con un dominio, el cual puede cambiar fácilmente de destinación (IP) para guiar al botnet al server preferido en ese momento, sin depender de configuraciones anteriores.

El control de la botnet se hacía normalmente a través del IRC, pero nuevas versiones de estas botnets han evolucionado hacia control mediante HTTP, con lo que la detección de estas redes es más compleja. Esto hace que las redes de empresas sean más vulnerables también, ya que el tráfico de IRC queda bloqueado.

Adicionalmente algunos spammers tienen su propio servidor de IRC donde son los dueños y, posiblemente, haga falta ser operador de la red para ver los canales, hacer whois, o ver alguna información útil. Cabe decir que en muchos casos estos servidores suelen funcionar en el equipo de una de las víctimas pero teniendo el control total el atacante.

Además, comparar diferentes formas de detectar botnets es realmente útil para los investigadores. Les ayuda a ver qué tan bien funciona cada método en comparación con otros. Este tipo de comparación es buena porque permite a los investigadores evaluar los métodos de manera justa y encontrar formas de mejorarlos.

 Botnets p2p
Otros tipos de botnet poco comunes crean una red p2p descentralizada entre las víctimas, las cuales normalmente utilizan una comunicación cifrada y de esta manera posibilita al dueño la capacidad de controlarlas libremente. Al no tener un servidor central la eliminación de esta se vuelve mucho más difícil de controlar.

 Usos habituales de las botnets
Estas redes son usadas en general para generar dinero a través de usos que generan dinero a sus controladores. Entre los usos más comunes están:

 **Ataques de denegación de servicio distribuidos (DDoS)**:  Este tipo de ataques consiste en enviar al equipo de la víctima una gran cantidad de solicitudes de servicio hasta que dicho equipo sea incapaz de procesarlas y quede incomunicado. Es un ataque usado por los dueños de los botnet para hacer chantaje o extorsión y pedir dinero a cambio de liberar el equipo. Si se recibe un ataque de tipo DDoS desde una Botnet, dada la dispersión geográfica de los ordenadores que la componen, es casi imposible encontrar un patrón de las máquinas que están atacando y dado el alto número de ellas que lo estarán haciendo al mismo tiempo, no se puede contemplar el filtrado de paquetes como una solución real que funcione. No obstante, puede ayudar a mitigar el problema hacer un escaneo pasivo de los paquetes para reconfigurar y adaptar el firewall.

 **Envío de Spam**: Lo más frecuente es que una botnet se utilice para enviar spam a direcciones de correo electrónico. Normalmente los creadores de estas Botnets venden sus servicios a los spammers. Por lo menos en un caso una investigación (la red Rustock) consiguió averiguar que un solo hacker había conseguido el control de un millón de ordenadores, utilizándolos como plataforma para sus ataques, con los que era capaz de enviar 30 billones de spam por día.

 **Minería de Bitcoins**: Con la aparición de criptomonedas, ya en 2011 había reportes de un nuevo uso para las botnets: usar el procesamiento de los computadores para generar bitcoins. De esta forma los criminales pueden obtener recursos sin gastar en hardware ni en consumo de energía. Se espera que este uso siga aumentando en el futuro. Un ejemplo de estas redes es ZeroAccess botnet.
 **Robo de Bitcoins**: Una variante adicional es el robo de bitcoins usando botnets. Es el caso de la red Pony, que robaba información de los equipos infectados. Se estima que con esta red se obtuvieron credenciales (usuario/password) de al menos 2 millones de equipos.
 **Fraudes publicitarios**. Normalmente, los servicios de anuncios en Internet pagan a los administradores de las webs donde figuran en función de varios factores, entre los que se incluye la visualización del anuncio y el hacer clic en el mismo. Los ciberdelincuentes ordenan a los bots que visiten sus propios sitios web y hagan clic en los anuncios para generar beneficios económicos de manera fraudulenta.
 **Ataque de fuerza bruta:** Consiste en usar una lista configurada de nombres de usuario y contraseñas para intentar adivinar las credenciales de inicio de sesión. Los sitios web pueden limitar estos ataques limitando los intentos de inicio de sesión de cada IP. Los ordenadores bots reciben una lista de webs o IP junto con estos posibles nombres de usuario y contraseña para cada una de las webs.

 Véase también
 Blaster
 Buffer overflow
 DDoS
 Malware
 Privacidad
 Script kiddie
 Spammer
 Troyano (informática)
 Zombi

 Referencias

 Enlaces externos
 NetFilter Página de iptables. Firewall de GNU/Linux
 German honeynet research paper
 Introducción a lo que son las botnets por el centro de respuesta a incidentes de Seguridad del Gobierno de España (INTECO-CERT)
