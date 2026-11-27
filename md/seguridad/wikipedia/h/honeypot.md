---
type: Artículo de enciclopedia
title: Honeypot
description: "Un honeypot, o sistema trampa o señuelo, es una herramienta de la seguridad informática dispuesto en una red o sistema informático para ser el objetivo de un posible ataque informático, y así poder detectarlo y obtener …"
resource: https://es.wikipedia.org/wiki/Honeypot
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Honeypot"}
license: CC BY-SA 4.0
id: eswiki-Honeypot
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Honeypot

Un ***honeypot***, o sistema **trampa** o **señuelo**, es una herramienta de la seguridad informática dispuesto en una red o sistema informático para ser el objetivo de un posible ataque informático, y así poder detectarlo y obtener información del mismo y del atacante.

La característica principal de este tipo de programas es que están diseñados no solo para protegerse de un posible ataque, sino para servir de señuelo invisible al atacante, con objeto de detectar el ataque antes de que afecte a otros sistemas críticos. El *honeypot*, sin embargo, puede estar diseñado con múltiples objetivos, desde simplemente alertar de la existencia del ataque u obtener información sin interferir en el mismo, hasta tratar de ralentizar el ataque —*sticky honeypots*— y proteger así el resto del sistema.De esta forma se tienen *honeypots* de baja interacción, usados fundamentalmente como medida de seguridad, y *honeypots* de alta interacción, capaces de reunir mucha más información y con fines como la investigación.

Si el sistema dispuesto para ser atacado forma toda una red de herramientas y computadoras dedicadas en exclusiva a esta tarea se le denomina *honeynet*.

*Honeypot* es la terminología con la que se describe el recurso informático monitorizado usado para probar, que sea atacado o que se vea comprometido por ataques informáticos.

El uso principal que se le otorga a este señuelo de *network* es el de distraer a posibles atacantes de información y máquinas más importantes de la network real, aprender sobre las formas de ataques que pueden sufrir y examinar dichos ataques durante y después de la explotación de un *honeypot*.

Dado el incremento de ataques, es relevante tener una forma para poder prevenir y ver vulnerabilidades de un sistema concreto de *network*. Es decir, se usa un señuelo para poder proteger una *network* de presentes o futuros ataques.

 Tipos de *honeypots*
Encontramos dos tipos principales de *honeypot*, estos son los físicos y los virtuales:

 Físico: se trata de una máquina real con su propia dirección IP, esta máquina simula comportamientos modelados por el sistema. Muchas veces no se utiliza tanto esta modalidad de *honeypot* debido al precio elevado de adquirir nuevas máquinas, su mantenimiento y a la complicación añadida de configurar hardwares especializados.
 Virtual: el uso de este tipo de *honeypot* permite instalar y simular huéspedes en la network procedentes de distintos sistemas operativos, para hacer esto se debe simular el TCP/IP del sistema operativo objetivo. Esta modalidad es más frecuente.

Además, también se pueden distinguir los *honeypot* basándose en si su finalidad es la de investigación o la de producción:

 La técnica de investigación se dirige en juntar toda la información posible de los *blackhat* *hackers* a partir de darles el acceso a sus sistemas de seguridad para que inflitren.
 La técnica de producción, en cambio, va dirigida a proteger las compañías que preparen las *honeypot*, mejorando sus sistemas de seguridad.

Según los criterios de diseño, los *honeypots* se pueden clasificar en:

 *Honeypots* puros: sistemas de producción completos. Las actividades del atacante se controlan mediante el uso de un *bug tap* que se ha instalado en el enlace del *honeypot* a la red. No es necesario instalar ningún otro *software*. Aunque un *honeypot* puro es útil, el sigilo de los mecanismos de defensa puede garantizarse mediante un mecanismo más controlado.
 *Honeypots* de alta interacción: imitan las actividades de los sistemas de producción que alojan una variedad de servicios y, por lo tanto, un atacante puede tener muchos servicios para perder el tiempo. Al emplear máquinas virtuales, se pueden alojar múltiples *honeypots* en una sola máquina física. Por lo tanto, incluso si el *honeypot* se ve comprometido, se puede restaurar más rápidamente. En general, los *honeypots* de alta interacción brindan más seguridad al ser difíciles de detectar, pero su mantenimiento es costoso. Si las máquinas virtuales no están disponibles, se debe mantener una computadora física para cada *honeypot*, lo que puede ser exorbitantemente costoso. Ejemplo: *Honeynet*.
 *Honeypots* de baja interacción: simulan solo los servicios solicitados con frecuencia por los atacantes. Dado que consumen relativamente pocos recursos, varias máquinas virtuales se pueden alojar fácilmente en un sistema físico, los sistemas virtuales tienen un tiempo de respuesta corto y se requiere menos código, lo que reduce la complejidad de la seguridad del sistema virtual. Ejemplo: *Honey*.

La ***sugarcane*** (caña de azúcar) es un tipo de *honeypot* que se hace pasar por un *proxy* abierto. A menudo puede adoptar la forma de un servidor diseñado para parecerse a un proxy HTTP mal configurado. Probablemente el *proxy* abierto más famoso fue la configuración predeterminada de *sendmail* (antes de la versión 8.9.0 en 1998) que reenviaba correos electrónicos hacia y desde cualquier destino.

 Definición del término

El término *honeypot* significa en inglés, literalmente, «tarro de miel». Sin embargo, los angloparlantes han usado el término para referirse a otras cosas, relacionando siempre de manera eufemística o sarcástica esas otras cosas con un tarro de miel.

Así, han usado el término *honeypot* para referirse a algo tentador que resulta ser una trampa, como en castellano lo es en la fábula de Félix María Samaniego, *Las moscas* (fragmento):

 *Spam honeypots*

Los *spammers* abusan de recursos como los servidores de correo abiertos y los proxies abiertos. Algunos administradores de sistemas han creado *honeypots* que imitan este tipo de recursos para identificar a los presuntos *spammers*.

Algunos honeypots de este estilo incluyen Jackpot, escrito en Java por Jack Cleaver; smtpot.py, escrito en Python por Karl Krueger y spamhole escrito en C.

 *Honeypots* de seguridad

Programas como *Deception Toolkit* de Fred Cohen se disfrazan de servicios de red vulnerables. Cuando un atacante se conecta al servicio y trata de penetrar en él, el programa simula el agujero de seguridad pero realmente no permite ganar el control del sistema. Registrando la actividad del atacante, este sistema recoge información sobre el tipo de ataque utilizado, así como la dirección IP del atacante, entre otras cosas.

 Honeynet Project es un proyecto de investigación que despliega redes de sistemas *honeypot* (*HoneyNets*) para recoger información sobre las herramientas, tácticas y motivos de los criminales informáticos.
 PenTBox Security Suite es un proyecto que desarrolla una Suite de Seguridad Informática. Dentro de los programas que la engloban está disponible un Honeypot configurable de baja interacción. El proyecto es multiplataforma, programado en Ruby y está licenciado bajo GNU/GPL.

 Tecnología del engaño
Recientemente, ha surgido un nuevo segmento de mercado llamado tecnología engañosa que utiliza tecnología trampa básica con la adición de automatización avanzada para escalar. La tecnología de engaño aborda la implementación automatizada de recursos trampa en una gran empresa comercial o institución gubernamental.

 Malware *honeypots*
Los *honeypots* de *malware* se utilizan para detectar *malware* mediante la explotación de los vectores de replicación y ataque conocidos de *malware*. Los vectores de replicación, como las unidades flash USB, se pueden verificar fácilmente en busca de evidencia de modificaciones, ya sea a través de medios manuales o utilizando *honeypots* especiales que emulan las unidades.

 Detección de los *honeypot*
Así como los *honeypots* son armas contra los *spammers*, los sistemas de detección de *honeypots* son armas contra las que emplean los *spammers*. Dado que los sistemas de detección probablemente usarían características únicas de trampas trampa específicas para identificarlas, como los pares propiedad-valor de la configuración predeterminada de *honeypot*, muchos *honeypot* en uso utilizan un conjunto de características únicas más grandes y más abrumadoras para aquellos que buscan detectar y así identificarlos. Esta es una circunstancia inusual en el *software*; una situación en la que la "versionitis" (un gran número de versiones del mismo software, todas ligeramente diferentes entre sí) puede ser beneficiosa. También hay una ventaja en tener algunos *honeypots* fáciles de detectar desplegados. Fred Cohen, el inventor de Deception Toolkit, argumenta que cada sistema que ejecuta su *honeypot* debe tener un puerto de engaño que los adversarios puedan usar para detectar el *honeypot*. Cohen cree que esto podría disuadir a los adversarios.

 *Honey nets*
Dos o más *honeypots* en una red forman una *honey net* (red trampa). Por lo general, una red trampa se usa para monitorear una red más grande y/o más diversa en la que un señuelo puede no ser suficiente. Las *Honey Nets* y los *Honeypots* se implementan generalmente como parte de sistemas de detección de intrusos de red más grandes. Una granja de miel es una colección centralizada de honeypots y herramientas de análisis.

El concepto de la red de miel comenzó en 1999 cuando Lance Spitzner, fundador del Proyecto Honeynet, publicó el artículo *"To build a Honeypot"*.

 Investigación periodística

En 2006, la BBC realizó una investigación para determinar la incidencia de ataques que podría sufrir un ordenador típico. En una primera fase, consistente en simplemente registrar el número y tipo de ataques, los resultados fueron que cada 15 minutos, de media, el ordenador recibía spam «molesta», típicamente ofertas fraudulentas para mejorar la seguridad del ordenador. Sin embargo, cada hora, de media, el ordenador recibía ataques más serios, de gusanos informáticos tipo SQL Slammer y MS.Blaster.

La segunda fase de la investigación consistía en dejar entrar el *adware* y *spyware* para ver sus eventuales efectos en el ordenador. El resultado fue que, de tratarse de un ordenador cualquiera en un hogar normal, hubiera quedado totalmente insegura e inservible.

 Véase también

 Honeynet
 Cracker
 Hacker
 Spam
 Botnet

 Referencias

 Enlaces externos

 (EN) 'Conoce a tu Enemigo': Todo lo que necesitas saber sobre honeypots*Un honeypot es un sistema de información cuyo valor recae en el uso ilícito de este sistema*. ISBN 0-321-16646-9
