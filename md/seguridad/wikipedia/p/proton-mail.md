---
type: Artículo de enciclopedia
title: Proton Mail
description: "Proton Mail es un servicio de correo electrónico cifrado, creado en 2013 por los científicos e ingenieros del CERN Jason Stockman, Andy Yen, y Wei Sun a raíz de las revelaciones del extrabajador de la NSA, Edward …"
resource: https://es.wikipedia.org/wiki/Proton_Mail
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Proton_Mail"}
license: CC BY-SA 4.0
id: eswiki-Proton_Mail
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Proton Mail

- **Eslogan:** Un servicio de correo electrónico seguro que protege tu privacidad
- **Creador:** Andy Yen, Jason Stockman, Wei Sun
- **Estado actual:** activo
- **Idioma:** alemán, español, francés, inglés, italiano, ruso y turco
- **Usuarios:** 25 millones (2020)
- **Nombre:** Proton Mail

**Proton Mail** es un servicio de correo electrónico cifrado, creado en 2013 por los científicos e ingenieros del CERN Jason Stockman, Andy Yen, y Wei Sun a raíz de las revelaciones del extrabajador de la NSA, Edward Snowden, sobre las prácticas de vigilancia masiva de las agencias de seguridad estadounidenses. Se debe mencionar que los fundadores se conocieron mientras trabajaban en el CERN, pero este no tiene relación alguna con Proton Mail ni fue parte de su creación, financiamiento o distribución. El servicio está diseñado como una prueba de conocimiento cero, mediante el cifrado del lado del cliente para proteger los correos electrónicos y los datos del usuario antes de ser enviados a los propios servidores de Proton Mail, a diferencia de otros servicios de correo web común, como Gmail y Outlook. Proton Mail es muy similar a Tuta Mail, ya que ambos utilizan cifrado de extremo a extremo.

Proton Mail está a cargo de la empresa Proton AG, con sede en Ginebra y sus servidores se encuentran en Suiza, fuera de la jurisdicción de los Estados Unidos y de la Unión Europea, donde cualquier gobierno solo puede solicitarle datos mediante una orden judicial del Tribunal Supremo suizo. El servicio se financió inicialmente a través de una campaña de financiación colectiva, y se mantendrá a largo plazo mediante la fijación de precios a varios niveles, aunque se puede crear una cuenta gratuita con 500 MB de almacenamiento y la posibilidad de enviar hasta 150 correos electrónicos diarios, cuenta que además proporciona mayor capacidad en el buzón, posibilidad de enviar más correos diarios, dominio de correo personalizado y otras funciones adicionales como el servicio Proton VPN.

En diciembre de 2017 Proton Mail contaba con más de 2 000 000 de usuarios registrados y para finales de 2018 ya eran 10 000 000 sus usuarios. En la primavera de 2020, se indica que hay más de 25 millones de usuarios.

 Características
Las cuentas Proton Mail pueden utilizar hasta tres niveles de seguridad. Dos contraseñas de usuario y autentificación de dos factores mediante aplicación. La primera, «*la contraseña de inicio de sesión* (*login password*)», autentifica al usuario en el sistema Proton Mail. La segunda, «*la contraseña de acceso al buzón* (*mailbox password*)» que se utiliza para descifrar el buzón de correo electrónico del usuario. Este descifrado se realiza del lado del cliente en el navegador web. La segunda contraseña es conocida solo por el usuario. Así pues, como los servidores de Proton Mail solo guardan los datos del usuario de forma cifrada, la recuperación de dicha contraseña resulta imposible, por lo que Proton Mail no podría descifrar los mensajes de los usuarios aunque fuera solicitada por una orden judicial.

La tercera es mediante una aplicación móvil que puede ser elegida por el usuario como Google Authentificator o Authy 2 la cual debe escanear un código QR que el sistema proporciona la cual da la llave que generara cada 30 segundos un código de autentificación diferente.

Tanto la verificación por aplicación y la contraseña de buzón pueden ser desactivados a voluntad del usuario o solo activar una de dos. El único método de acceso obligatorio es la contraseña.

Asimismo el usuario puede elegir desactivar la opción que se encuentra en cualquier otro servicio de correo electrónico el cual es la recuperación de la cuenta mediante un correo alternativo. Si esta opción es activada y el usuario llegará a olvidar o perder el método o los métodos de acceso perderá por completo la posibilidad de acceder a la cuenta para siempre.

Al igual que el servicio de mensajería Telegram y ciertas redes sociales Proton Mail también proporciona la posibilidad de poner fecha de caducidad a los mensajes de forma opcional, con lo que desaparecerán del sistema Proton Mail después de un período de tiempo.

 Seguridad
Proton Mail utiliza una combinación de protocolos de criptografía y cifrado asimétrico de clave pública para ofrecer un cifrado de extremo a extremo. Cuando un usuario crea una cuenta en Proton Mail, su navegador genera un par de claves RSA: una pública y otra privada. La clave pública se utiliza para cifrar los mensajes de correo electrónico del usuario y otros datos de usuario; mientras que La clave privada, que es capaz de descifrar los datos del usuario, está simétricamente cifrada con la contraseña del buzón del usuario en el navegador web del usuario utilizando el protocolo AES-256. Ambas claves cifradas se almacenan entonces en sus servidores.

A finales de 2016, se introdujo un modo de una sola contraseña.

Los mensajes enviados desde una cuenta a otra cuenta Proton Mail se cifran con la clave pública del buzón del destinatario. Cuando el destinatario inicia su sesión, su contraseña del buzón de usuario descifra su clave privada, revelando el contenido de su bandeja de entrada. Los mensajes enviados desde Proton Mail a direcciones de correo electrónico que no son de Proton Mail pueden enviarse con o sin cifrado, a elección del remitente. Sin cifrado, los correos electrónicos se enviarán normalmente. Con el cifrado, el mensaje se cifrará con el protocolo AES con una contraseña compartida, previamente convenida entre ambas partes. El destinatario del correo recibe un enlace que le redirige a la página web Proton Mail. Una vez que se suministra la clave compartida, el correo electrónico se descifra en el navegador web. Los correos electrónicos de una dirección no Proton Mail a otra de Proton Mail se envían como cualquier otro correo electrónico normal.

 Ataques
Un video que mostraba un ataque de cross-site scripting apareció en julio de 2014. Los desarrolladores de Proton Mail revisaron el video y confirmaron que el problema solo afectó a una versión inicial de desarrollo de Proton Mail, que fue lanzada en mayo de 2014 y que el ataque no afectaba a la versión actual. Andy Yen manifestó que en julio de 2018 Proton Mail sufrió de nuevo varios ataques DDoS. En septiembre de 2018 las fuerzas de seguridad británicas arrestaron a un sospechoso en relación con estos y otros ataques a escuelas y líneas aéreas.

 La arquitectura del servidor

Los administradores de Proton Mail son propietarios del hardware y de la red del servidor y los mantienen ellos mismos para evitar confiar en un tercero. En respuesta a una saturación de sus servidores, a mediados de 2014 los fundadores de Proton Mail comenzaron a desarrollar y aumentar la arquitectura de dichos servidores. Actualmente el servicio está a cargo de dos centros de datos redundantes en el centro y en el oeste de Suiza. Cada centro de datos utiliza la misma carga a través de web, mismo correo y servidores SQL, fuentes de alimentación redundantes, unidades de disco duro con cifrado de disco completo y el uso exclusivo de Linux y otros software de código abierto. Proton Mail también se unió al RIPE NCC en un esfuerzo por tener un mayor control sobre la infraestructura de internet circundante.

El protocolo Transport Layer Security (TLS) se utiliza para proteger y cifrar todo el tráfico de internet entre los usuarios y los servidores de Proton Mail. Un informe técnico y de código fuente serán publicados en breve, según los desarrolladores. Proton Mail.ch tiene una nota de «A» de los Qualys SSL Labs.

 Interfaz
Proton Mail utiliza una interfaz basada en la web, similar a la de Gmail. Los usuarios también tienen la capacidad de fijar las fechas de caducidad de mensajes de correo electrónico y contraseñas de cifrado para mensajes de correo electrónico salientes a los usuarios que no son de Proton Mail.

 Historia
Proton Mail fue creado en respuesta al escándalo sobre la vigilancia y la interceptación de correo electrónico mundial por parte de la NSA en 2013, y está inspirado en Gmail, Lavabit y Snapchat.

 Financiación
El 17 de junio de 2014, Proton Mail comenzó una campaña de financiación colectiva en Indiegogo con el objetivo de recaudar  dólares. El 30 de junio, la cuenta PayPal de Proton Mail fue bloqueada, impidiendo la retirada de  dólares de donaciones de la cuenta. Un representante de la compañía declaró que dicha congelación fue originada por las dudas acerca de la legalidad del cifrado, sospechas que demostraron ser totalmente infundadas. Las restricciones fueron levantadas al día siguiente. La campaña finalizó el 31 de julio de 2014, con un total de  dólares recaudados de  donantes.

El 18 de marzo de 2015, Proton Mail recibió 2 millones de dólares de Charles River Ventures, y de la Fondation Genevoise pour l'Innovation Technologique (Fongit). Los desarrolladores de Proton Mail planean utilizar dichos fondos para ampliar su infraestructura, hacer crecer su equipo y abrir nuevas oficinas.

 Asunto de Google 2016
En 2016, Proton Mail fue suprimido en los resultados de búsqueda de Google, lo que resultó en que Proton Mail terminó ganando menos usuarios nuevos de lo planeado para ese año.

 Software libre
Desde abril de 2020, el código fuente de todos los programas con los que puede acceder a sus correos de Proton (Android, iOS, Bridge y el programa de red) está disponible gratuitamente en GitHub, bajo licencias GPL 3.0 y MIT.

 Véase también
 Proton AG
 Tuta - correo electrónico cifrado

 Referencias

 Enlaces externos

 Sitio web oficial
 Blog oficial
