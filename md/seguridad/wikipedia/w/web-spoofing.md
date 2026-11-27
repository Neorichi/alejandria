---
type: Artículo de enciclopedia
title: Web spoofing
description: El Web Spoofing consiste en la suplantación de una página web real por otra falsa con el fin de realizar una acción fraudulenta, no confundir con phishing.
resource: https://es.wikipedia.org/wiki/Web_spoofing
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Web_spoofing"}
license: CC BY-SA 4.0
id: eswiki-Web_spoofing
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Web spoofing

El **Web Spoofing** consiste en la suplantación de una página web real por otra falsa con el fin de realizar una acción fraudulenta, no confundir con phishing. La web falsa adopta el diseño de la web que se pretende suplantar e incluso una URL similar. Un tipo de ataque más sofisticado consiste en crear una “copia  sombra” de toda la World Wide Web para conseguir que el tráfico de la víctima pase por el atacante, de esta manera se obtiene toda la información sensible de la víctima.

Este tipo de ataque consigue redirigir la conexión de una víctima a través de una página falsa hacia otras páginas web con el objetivo de realizar alguna acción fraudulenta asociada con el phishing para obtener información, como usuarios y contraseñas, del tráfico de dicha víctima. Además, es posible que el atacante envíe datos a los servidores de páginas reales en nombre de la víctima o desde cualquier servidor web a la víctima.
 Funcionamiento
Para llevar a cabo este tipo de ataques se pueden usar distintas técnicas para conseguir atraer la atención del usuario a la web falsa:
 El atacante puede poner un enlace a la web falsa en un web conocida.
 Si conoce el correo electrónico del usuario es posible enviar un correo que incluya el enlace a la web falsa.
 Otro tipo de técnicas más sofisticadas, incluyen la ejecución de código javascript o la instalación de plug-ins.
Cuando el usuario ha accedido a la web falsa a través de alguna de las opciones anteriores, aparece una ventana del navegador web en la pantalla que simula a alguno de los navegadores conocidos. Después, todo el tráfico de las páginas visitadas que tenga lugar en la ventana infectada se envía a través de un servidor malicioso permitiendo a éste interceptar la información enviada. La página web falsa actúa a modo de proxy solicitando la información requerida por la víctima a cada servidor original. Es posible, entonces, conseguir contraseñas, nombres de usuarios o cualquier otro tipo de datos sensibles. Mientras el usuario siga usando dicho navegador falso, toda la información pasará a través del servidor malicioso sin que el usuario atacado sea capaz de identificar que está siendo atacado. Este tipo de ataque funciona incluso cuando el usuario solicita una conexión segura mediante protocolos SSL/TLS ya que se salta dicha protección. La víctima habrá establecido una conexión segura con el servidor del atacante en vez de con la web deseada, incluso el navegador verificará que dicha conexión es segura (aparecerá el icono del candado).

 Tipos de ataque
El atacante puede realizar distintos tipos de ataque que pueden ser clasificados en dos:
 Ataque pasivo: El atacante observa pasivamente el tráfico del usuario atacado, recabando información sobre las páginas visitadas. La información que el usuario introduce en los distintos formularios, que será enviada a los servidores web, es adquirida por el atacante. De esta manera, es posible obtener información delicada como nombres de usuario y contraseñas, así como información bancaria.

 Ataque activo: El atacante puede modificar cualquier información que viaje entre la máquina atacada y los distintos servidores web. Por ejemplo, una vez que el usuario envía algún formulario para realizar una transacción, el atacante puede modificar tanto el destinatario como la cantidad. Así mismo, el atacante también puede modificar la información enviada desde el servidor web al usuario.
 Prevención, identificación y actuación
El web spoofing es difícilmente detectable; quizá la mejor medida es algún plugin del navegador que muestre en todo momento la IP del servidor visitado: si la IP nunca cambia al visitar diferentes páginas web significará que probablemente estemos sufriendo este tipo de ataque.

Otra manera de prevenir este tipo de spoofing es evitar usar hipervínculos. Por ejemplo, en vez de usar un enlace de un correo electrónico, escribir la url de la web por uno mismo. Además, es aconsejable evitar usar la misma contraseña en todos los sitios web ya que en caso de haber sido víctimas de este ataque el daño será menor.

En caso de usar hipervínculos, es recomendable comprobar la url del enlace situando el ratón sobre ella, si observamos que dicha url ha podido ser adulterada o no se corresponde con la que se conoce, no debemos hacer clic sobre dicho ella. El atacante puede llegar incluso a modificar el contenido de la url que aparece mediante la ejecución de código javascript asociado al evento de situar el ratón sobre el enlace, para hacer que aparezca la url que se espera. Para evitar que esto suceda es posible deshabilitar la ejecución de código javascript en el navegador.

Además, es recomendable extremar la precaución cuando se accede a páginas de comercio electrónico ya que estas son el principal objetivo de los atacantes. Cualquier web que sea usada para realizar transacciones bancarias, comprar o vender artículos tiene mayor probabilidad de estar sujeta a web spoofing.

La mitigación de los riesgos de web spoofing puede llevarse a cabo por parte de las empresas. Si es posible, ciertos empleados deben ser asignados para monitorizar el sitio web y asegurarse de que ningún sitio fraudulento ha sido creado. Un gran incremento en llamadas de los consumidores en relación con la web algunas veces será signo de que la web habrá sido suplantada.

Si los correos electrónicos enviados por los usuarios a los correos de contacto que aparecen en la web son devueltos a servidores de correo, puede que sea un sitio fraudulento.

Si ha sido determinado de que la web ha sido objetivo de suplantación, será necesario recabar información sobre ella. Esta información ayudará a identificar la web fraudulenta, determinar si la información del cliente ha sido robada y conocer la identidad del atacante. Será adecuado acudir a la justicia para denunciar el robo de información y el uso incorrecto de marcas comerciales, así como comunicar rápidamente con el Servidor de Servicio de Internet (ISP) responsable de alojar a la web fraudulenta para que sea retirada. Contactar con los registradores del servidor de nombre para que lleven a cabo la misma función.

 Véase también
 Spoofing
 Hoax
 Proxy
 Phising
 SSL
 URL
 Plug-in

Referencias
