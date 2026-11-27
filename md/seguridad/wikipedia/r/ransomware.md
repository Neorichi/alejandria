---
type: Artículo de enciclopedia
title: Ransomware
description: "Un ransomware (del inglés ransom, 'rescate', y ware, acortamiento de software) o 'secuestro de datos' en español, es un tipo de programa dañino que restringe el acceso a determinadas partes o archivos del sistema …"
resource: https://es.wikipedia.org/wiki/Ransomware
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ransomware"}
license: CC BY-SA 4.0
id: eswiki-Ransomware
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ransomware

Un ***ransomware*** (del inglés *ransom*, 'rescate', y *ware*, acortamiento de *software*) o 'secuestro de datos' en español, es un tipo de programa dañino que restringe el acceso a determinadas partes o archivos del sistema operativo infectado y pide un rescate a cambio de quitar esta restricción. Algunos tipos de *ransomware* cifran los archivos del sistema operativo inutilizando el dispositivo y coaccionando al usuario a pagar el rescate. Se han propuesto algunas alternativas en español al término en inglés, como 'programa de secuestro', 'secuestrador', 'programa de chantaje' o 'chantajista'. En los primeros tiempos el pago se hacía a través de cuentas bancarias de países opacos, pero como el rastreo al delincuente era posible, se pasó al uso de monedas virtuales no rastreables.

Aunque los ataques se han hecho populares desde mediados de la década del 2010, el primer ataque conocido fue realizado a finales de la década de los 80, por el Dr. Joseph Popp. Su uso creció internacionalmente en junio del 2013. La empresa McAfee señaló en 2013 que solamente en el primer trimestre, había detectado más de 250 000 tipos de *ransomware* únicos.

 Tipos
Hay tres tipos de *ransomware*:
**Bloqueadores**. Su objetivo es bloquear o simular el bloqueo del sistema informático al completo y muestra un mensaje de alerta para pedir el rescate. Se han dado casos en los que el mensaje parece que pertenece a alguna autoridad gubernamental y se indica que se ha detectado contenido ilegal y pide dinero para pagar una multa y evitar entrar en prisión. En este tipo se incluye *ransomware* que coloca un banner pornográfico en el escritorio y alegaba que la víctima ha visto contenido prohibido para pedir el rescate.
**Cifradores** o **filecoders**. El *ransomware* realiza cifrado del nombre y/o el contenido de ficheros. Inicialmente usaban criptografía simétrica. Actualmente suelen usar criptografía asimétrica. Ejemplos de este tipo de *ransomware* son el AIDS (el primer *ransomware* que usaba criptografía simétrica para cifrar el nombre de los archivos) y PGPCoder (usaba criptografía asimétrica).
**Híbridos**. Combina características de bloqueador y de cifrador. Ejemplo de este tipo de *ransomware* es CryptoLocker.

 Métodos de propagación
Normalmente un *ransomware* se transmite como un troyano o como un gusano, infectando el sistema operativo, por ejemplo, con un archivo descargado o explotando una vulnerabilidad de *software*. En este punto, el *ransomware* se iniciará, cifrará los archivos del usuario con una determinada clave, que solo el creador del *ransomware* conoce, y provocará al usuario que la reclame a cambio de un pago.

 *Modus operandi*
El atacante camufla el código malicioso dentro de otro archivo o programa apetecible para que el usuario esté llamado a hacer clic*.* Algunos ejemplos de estos camuflajes serían:
 Archivos adjuntos en correos electrónicos.
 Vídeos de páginas de dudoso origen.
 Actualizaciones de sistemas.
 Programas, en principio, fiables, como Windows o Adobe Flash.

Luego, una vez que ha penetrado en el ordenador, el *ransomware* se activa y provoca el bloqueo de todo el sistema operativo, lanza el mensaje de advertencia con la amenaza y el importe del rescate que se ha de pagar para recuperar toda la información. Además, en ocasiones incluyen en la amenaza la dirección IP, la compañía proveedora de Internet y hasta una fotografía captada desde la cámara web.

 Ataques *ransomware* más conocidos

 Petya

Creado y descubierto en 2016

En 2017 comenzó un ciberataque mundial (Las compañías ucranianas fueron los primeros en decir que estaban siendo atacadas), utilizando una nueva variante de Petya. En ese día Kaspersky Lab informó de las infecciones en Francia, Alemania, Italia, Polonia, Reino Unido y Estados Unidos, pero que la mayoría de las infecciones se dirigieron a Rusia y Ucrania, donde más de 80 empresas fueron atacadas, incluyendo el Banco Nacional de Ucrania.

 Reveton

En 2012 se comenzó a distribuir un *ransomware* llamado Reveton. Estaba basado en el troyano Citadel, el cual estaba a su vez basado en el troyano Zeus. Su funcionamiento se basa en desplegar un mensaje perteneciente a una agencia de la ley, preferentemente correspondiente al país donde reside la víctima. Por este funcionamiento se lo comenzó a nombrar como *trojan cop*, o «policía troyano», debido a que alegaba que el computador había sido utilizado para actividades ilícitas, tales como descargar *software* pirata o pornografía infantil. El troyano muestra una advertencia informando que el sistema fue bloqueado por infringir la ley y de ese modo deberá pagar una fianza para poder liberarlo, mediante el pago a una cuenta anónima como puede ser Ukash o Paysafecard.

Para hacer creer a la víctima que su computador está siendo rastreado por la ley, se muestra la dirección IP del computador en pantalla, además se puede mostrar material de archivo y simular que la cámara web está filmando a la víctima.

A principios del año 2012 comenzó su expansión por varios países de Europa; según el país, podría variar el logo referente a las Fuerzas de la Ley correspondientes. Por ejemplo, en el Reino Unido, contenía el logo del Servicio de Policía Metropolitana. Debido a estos sucesos, la Policía Metropolitana envió un comunicado informando que bajo ningún concepto ellos bloquearían un computador ni siquiera como parte de una investigación.

En mayo de 2012, Trend Micro descubrió las variaciones de este *malware* para los Estados Unidos y Canadá, sospechando que los autores planeaban expandirlo a América del Norte. En agosto de 2012, se comenzó a utilizar el logo del FBI para reclamar una fianza de 200 dólares a los propietarios de computadores infectados, a pagar mediante una tarjeta de aMoneyPak. En febrero de 2013, un ciudadano ruso fue arrestado en Dubái por autoridades españolas debido a su conexión con la red criminal que había estado usando Reveton, al cual se sumaron otras diez personas con cargos por lavado de dinero.

En agosto de 2014, Avast reportó nuevas variantes de Reveton, donde se distribuía *software* malicioso con el fin de robar contraseñas.

 CryptoLocker

En septiembre de 2013 En septiembre de 2013 apareció el ransomware CryptoLocker el *ransomware* basado en el cifrado de archivos también conocido como CryptoLocker, el cual genera un par de claves de 2048-bit del tipo RSA con las que se controla el servidor y se cifran archivos de un tipo de extensión específica. la clave privada permanece en poder del atacante, quien la entrega si el pago se realiza dentro del plazo de un bitcoin o un bono prepago en efectivo dentro de los tres días tras la infección. Debido al largo de la clave utilizada, se considera que es extremadamente difícil reparar la infección de un sistema.

En caso de que el pago se retrase más allá de los tres días, el precio se incrementa a 10 *bitcoins*, lo que equivalía, aproximadamente, a 2300 dólares, en noviembre de 2013.

CryptoLocker fue aislado gracias a que incautaron la red GameoverZeuS, tal como fue anunciado oficialmente por el Departamento de Justicia de los Estados Unidos el 2 de junio de 2014.

El Departamento de Justicia emitió una acusación en contra del ciberdelincuente ruso Evgeniy Bogachev (Евгений Богачев) alegando su participación en la red GameoverZeuS. Se estima que consiguió al menos tres millones de dólares hasta que el *malware* fue desactivado.

 CryptoLocker.F y TorrentLocker
En septiembre de 2014, una ola de *ransomware* llegó a sus primeros objetivos en Australia, denominados CryptoWall y CryptoLocker. Las infecciones se propagaban a través de una cuenta de correo australiana falsa, la cual enviaba un correo electrónico notificando entregas fallidas de paquetes. De este modo evitaba los filtros *antispam* y conseguía llegar a los destinatarios. Esta variante requería que los usuarios ingresaran en una página web y, previa comprobación mediante un código CAPTCHA, accedieran a la misma, antes de que el *malware* fuese descargado, de esta manera se evitó que procesos automáticos puedan escanear el *malware* en el correo o en los enlaces insertados.

Symantec determinó la aparición de nuevas variantes conocidas como CryptoLocker.F, el cual no tenía ninguna relación al original debido a sus diferencias en el funcionamiento.

TorrentLocker es otro tipo de infección con un defecto, ya que usaba el mismo flujo de claves para cada uno de los computadores que infectaba, el cifrado pasó a ser trivial pero antes de descubrirse ya habían sido 9000 los infectados en Australia y 11 700 en Turquía.

 CryptoWall

CryptoWall es una variedad de *ransomware* que surgió a principios de 2014 bajo el nombre de CryptoDefense dirigida a los sistemas operativos Microsoft Windows. Se propaga a través del correo electrónico con suplantación de identidad, en el cual se utiliza *software* de explotación como Fiesta o Magnitud para tomar el control del sistema, cifrar archivos y así pedir el pago del rescate del computador. El rango de precios se encuentra entre los 500 y 1000 dólares.

En marzo de 2014, José Vildoza, un programador argentino, desarrolló una herramienta para recuperar los archivos de las víctimas de manera gratuita. La recuperación de archivos fue posible gracias a una vulnerabilidad en el ransomware por el cual las claves de cifrado quedaban guardadas en el equipo afectado.

Cuando los autores se percataron del error, actualizaron el criptovirus nombrándolo CryptoWall, pasando luego por distintas actualizaciones hasta llegar a la versión 3.0.

CryptoWall 3.0 ha sido reportado desde enero de 2015 como una infección que surge donde hackers rusos se encuentran detrás de esta extorsión.

 TeslaCrypt
TeslaCrypt es uno de los *ransomware* considerados como eliminados ya que la clave maestra para el descifrado de los ficheros atacados es pública. Existe una herramienta gratuita de la empresa ESET que permite realizar este trabajo.

 Mamba
Un grupo de investigadores de seguridad de Brasil, llamado Morphus Labs, acaba de descubrir un nuevo *ransomware* de cifrado de disco completo (FDE - *Full Disk Encryption*) llamado Mamba. Mamba, como lo llamaron, utiliza una estrategia de cifrado a nivel de disco en lugar de uno basado en archivos convencionales. Para obtener la clave de descifrado, es necesario ponerse en contacto con alguien a través de la dirección de correo electrónico proporcionada. Sin eso, el sistema no arranca.

El *ransomware* Mamba se ha identificado el 7 de septiembre de 2017 durante un procedimiento de respuesta a incidentes por parte de Renato Marinho, un experto en seguridad de Morphus laboratorios. Esta amenaza de malware utiliza el cifrado a nivel de disco que causa mucho más daño que los ataques basados en archivos individuales. Los desarrolladores criminales han utilizado el *DiskCryptor* para cifrar la información., una herramienta de código abierto.

Se hizo una comparación con el virus Petya que también utiliza disco cifrado. Sin embargo, Petya cifra solamente la tabla maestra de archivos (MFT) con lo que no afectan a los datos en sí.

Tras la exitosa infiltración, Mamba crea su carpeta titulada DC22 en la unidad C del equipo donde coloca sus archivos binarios. Un servicio del sistema se crea y alberga el proceso del ransomware. Un nuevo usuario llamado MythBusters se crea asociado con la contraseña 123456.

También sobrescribe el registro de inicio maestro (MBR) del disco del sistema que contiene el gestor de arranque para el sistema operativo. Esto prohíbe efectivamente al usuario de incluso cargar el sistema operativo sin ingresar el código de descifrado.

 WannaCry

WanaCrypt0r o también conocido como WannaCry es un *ransomware* activo que apareció el 12 de mayo de 2017 con origen en el arsenal estadounidense de malware Vault 7 revelado por Wikileaks pocas semanas antes, el código malicioso ataca una vulnerabilidad descrita en el boletín MS17-010 en sistemas Windows que no estén actualizados de una manera adecuada. Provocó el cifrado de datos en más de 200.000 ordenadores en más de 150 países por todo el mundo afectando, entre otros, a:
 Rusia: red semafórica, metro e incluso el Ministerio del Interior;
 Reino Unido: gran parte de los centros hospitalarios;
 Estados Unidos;
 España: empresas tales como Telefónica, Gas Natural e Iberdrola.

El *ransomware* cifra los datos que, para poder recuperarse, pide que se pague una cantidad determinada, en un tiempo determinado. Si el pago no se hace en el tiempo determinado, el usuario no podrá tener acceso a los datos cifrados por la infección. WannaCry se ha ido expandiendo por Estados Unidos, China, Rusia, Italia, Taiwán, Reino Unido y España, al igual de que se señala que los sistemas operativos más vulnerables ante el *ransomware* son Windows Vista, Windows 7, Windows Server 2012, Windows 10 y Windows Server 2016.

Un ordenador infectado que se conecte a una red puede contagiar el *ransomware* a otros dispositivos conectados a la misma, pudiendo infectar a dispositivos móviles. A su inicio, WanaCrypt0r comienza a cifrar los archivos de la víctima de una manera muy rápida.

Afortunadamente en la actualidad se pudo detener su expansión gracias a un programador de Reino Unido, autor del blog MalwareTechBlog.

 Ryuk

Ryuk es un ransomware que apareció primera vez en agosto de 2018 pero que se ha empezado a conocer a partir de mediados del 2019 debido al gran número de ataques instituciones públicas (ej. SEPE, Ministerio de trabajo de España, hospitales de Alabama, Ayuntamiento de Jerez, Ayuntamiento de Bilbao) y grandes empresas (ej. Tribune Publishing, Tampa Bay Times). El mensaje que Ryuk muestra en pantalla cuando se activa en el ordenador objetivo muestra una dirección de cartera de Bitcoin para realizar el pago y dos direcciones de correo electrónico para que la víctima contacte directamente con los atacantes, además de una clave de referencia. Este malware ha ido evolucionando desde su aparición.
El software usa una clave distinta a cada objetivo (organización) lo que complica el caso ya que si una organización afectada consigue la clave o como descifrar los datos no servirá para el resto de organizaciones. Se han observado versiones con gran capacidad de propagación, a modo de gusano, aprovechándose de protocolos Wake on LAN (para arrancar equipos apagados), SMB y RPC. Implementa controles para no afectar a usuarios localizados en Rusia, Ucrania o Bielorrusia.

Durante la pandemia de COVID-19 de 2020 se produjo un aumento significativo de los ataques de ransomware. La evidencia ha demostrado que las instituciones objetivo de estos ataques incluían el gobierno, las finanzas y la atención médica. Los investigadores han sostenido que varios factores diferentes pueden explicar el aumento de ataques durante este tiempo. Sin embargo, un factor importante es que el trabajo remoto, que se convirtió en la norma para muchas industrias en 2020, provocó un aumento de los ataques debido a la falta de seguridad en comparación con los entornos de trabajo tradicionales.

 Mitigación

Al igual que ocurre con otras formas de *malware*, los programas de seguridad puede que no detecten la carga útil (*payload*) de un programa *ransomware* hasta que el cifrado de archivos está en proceso o ha concluido, especialmente si se distribuye una nueva versión desconocida para el antivirus. Si un ataque se detecta de manera temprana, se puede eliminar de manera sencilla sin darle tiempo de comenzar el proceso de cifrado.

Expertos en seguridad informática han sugerido medidas preventivas para hacer frente al *ransomware*. Usar *software* o políticas de seguridad para bloquear cargas útiles conocidas ayudará a prevenir las infecciones, pero no protegerá contra cualquier ataque. Mantener copias de seguridad *offline* en lugares inaccesibles para el ordenador infectado (discos duros externos, DVD, USB, almacenamiento en la nube,...), evita que el *ransomware* acceda a ellas, lo que ayuda a restaurar los datos en caso de infección. Sin embargo, la prevención puede requerir altos recursos financieros y humanos a nivel empresarial.

Expertos en seguridad también han señalado que las pobres prácticas de administración de información es una causa importante del grave impacto de *ransomware,* y recomiendan entre otras medidas disminuir el uso de software pirata o no legal, empleando, a cambio, software libre.

 Ransomware como servicio

El Ransomware ha tenido mucho éxito. Los ciberdelincuentes han dado un paso más ofreciendo **Ransomware como servicio** o **RaaS** (del inglés *Ransomware as a Services* ). En esta forma de explotación los cibercriminales crean un kit malicioso compacto capaz de lanzar un ataque de ransomware. Este kit lo venden/alquilan a los interesado bajo un programa de afiliación a otros cibercriminales que tienen la intención de lanzar un ataque. Además del software les proporcionan: conocimientos técnicos e información paso a paso sobre cómo lanzar un ataque de ransomware utilizando el servicio, una plataforma que incluso puede mostrar el estado del ataque utilizando un panel de control en tiempo real. A veces, cuando el ataque tiene éxito, el dinero del rescate se divide entre el proveedor de servicios, el codificador y el atacante. Por ejemplo el creador del kit puede recolectar el rescate, proporcionar la herramienta de descifrado a las víctimas que pagan y paga el 70% de los ingresos a través de Bitcoin al operador.

Ejemplos:
 Stampado. Creado en el verano de 2016
 Philadelphia. Creado a finales de 2016.
 Frozr Locker.
 Satán.
 RaasBerry. Detectado en verano de 2017. Los clientes pueden elegir entre distintos periodos de suscripción que empiezan a partir del mes.
 Cerber.
 Atom.
 Hostman.
 Shark.
 GrandCrab. Aparece en 2017
 Ako. Detectado en 2019
 LockBit. Detectado en 2019 y desmantelado en 2024

 Véase también
 CryptoLocker
 Exploit
 *Malware*
 Petya
 Privacidad digital
 WannaCry
 Ataques ransomware WannaCry

 Referencias

 Enlaces externos
 Néstor Parrondo, «La estafa del correo electrónico de Correos: si picas, tu ordenador quedará inutilizado», sitio digital 'Yahoo', 30 de marzo de 2015.
 *Asociación Nacional Afectados Internet y Nuevas Tecnologías*, Ayudan a recuperar tu dinero estafado.
 «Mamba Ransomware Discovered»
 *Servicio público y gratuito antiransomware de INCIBE*, Ayudan a descifrar la información e informan sobre medidas de prevención para no verse afectado.
