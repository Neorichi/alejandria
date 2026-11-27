---
type: Artículo de enciclopedia
title: Pegasus (spyware)
description: Pegasus es un spyware instalado en dispositivos que ejecutan ciertas versiones de iOS (el sistema operativo móvil de Apple) y Android, desarrollado por la firma cibernética israelí, NSO.
resource: https://es.wikipedia.org/wiki/Pegasus_(spyware)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Pegasus_(spyware)"}
license: CC BY-SA 4.0
id: eswiki-Pegasus_(spyware)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Pegasus (spyware)

- **Nombre:** Pegasus
- **Desarrollador:** Grupo NSO
- **Licencia:** Software propietario
- **Lanzamiento:** 2011
- **Descubrimiento:** 2016
- **Género:** spyware

**Pegasus** es un spyware instalado en dispositivos que ejecutan ciertas versiones de iOS (el sistema operativo móvil de Apple) y Android, desarrollado por la firma cibernética israelí, NSO. Descubierta en agosto de 2016 después de un intento fallido de instalarlo en un iPhone perteneciente a un activista de derechos humanos, una investigación reveló detalles sobre el software espía, sus capacidades y las vulnerabilidades de seguridad que explotó. Pegasus es capaz de leer mensajes de texto, rastrear llamadas, recopilar contraseñas, rastrear la ubicación del teléfono y recopilar información de las aplicaciones. Apple lanzó la versión 9.3.5 de su software iOS para corregir las vulnerabilidades. Las noticias del spyware atrajeron una gran atención de los medios. Fue llamado "el ataque de teléfono inteligente más sofisticado de la historia", y se convirtió en la primera vez en la historia del iPhone en que se detectó un ataque remoto de jailbreak. La compañía que creó el spyware, NSO, declaró que brindan a "los gobiernos autorizados tecnología que los ayuda a combatir el terrorismo y el crimen".

 Detalles del spyware
No es necesario que el usuario haga clic en ningún enlace, Pegasus habilita secretamente un jailbreak explotando vulnerabilidades en el dispositivo y puede leer mensajes de texto, rastrear llamadas, recopilar contraseñas, rastrear la ubicación del teléfono, así como recopilar información de aplicaciones que incluyen (entre otras) iMessage, Gmail, Viber, Facebook, WhatsApp, Telegram y Skype.

 Parche
Apple lanzó la versión 9.3.5 de iOS para su línea de productos para teléfonos inteligentes iPhone en agosto de 2016. Los detalles de la actualización fueron correcciones para las tres vulnerabilidades de seguridad críticas que explotó Pegasus.

 Descubrimiento del spyware
Las vulnerabilidades se encontraron diez días antes de que se lanzara la actualización iOS 9.3.5. El defensor árabe de los derechos humanos Ahmed Mansoor recibió un mensaje de texto que prometía "secretos" sobre la tortura que ocurría en las prisiones de los Emiratos Árabes Unidos", junto con un enlace. Mansoor envió el enlace a Citizen Lab. Se realizó una investigación con la colaboración de la compañía de seguridad Lookout que reveló que si Mansoor hubiera seguido el enlace, habría hecho *jailbreak* a su teléfono en el lugar e implantado el spyware en él. Citizen Lab vinculó el ataque a una compañía privada de software espía israelí conocida como NSO, que vende Pegasus a los gobiernos por "intercepción legal", pero existen sospechas de que se aplica para otros propósitos. A mes de mayo de 2022, NSO era propiedad de una firma europea de capital privado, Novalpina Capital.

En cuanto a la extensión del problema, Lookout explicó en una publicación del blog: "Creemos que este software espía ha estado en libertad por una cantidad significativa de tiempo basado en algunos de los indicadores dentro del código" y señaló que el código muestra signos de una "tabla de mapeo de kernel que tiene valores desde iOS 7". El New York Times y The Times of Israel informaron que parece que los Emiratos Árabes Unidos estaban utilizando este software espía en 2013. Un par de demandas legales afirman que NSO ayudó a los clientes a operar el software y, por lo tanto, participó en numerosas violaciones de los derechos humanos iniciadas por sus clientes.

 Vulnerabilidades
Lookout proporcionó detalles de las tres vulnerabilidades:

 CVE-2016-4655: Fuga de información en el kernel: una vulnerabilidad de mapeo de la base del kernel que filtra información al atacante y le permite calcular la ubicación del kernel en la memoria.
 CVE-2016-4656: La corrupción de la memoria del núcleo lleva a Jailbreak: vulnerabilidades a nivel de kernel de iOS de 32 y 64 bits que permiten al atacante liberar en secreto el dispositivo e instalar un software de vigilancia.
 CVE-2016-4657: Corrupción de la memoria en Webkit: una vulnerabilidad en Safari WebKit que permite al atacante poner en peligro el dispositivo cuando el usuario hace clic en un enlace.

 Reacciones
 Noticias
La noticia del spyware recibió una importante atención de los medios, particularmente por ser llamado "el ataque de teléfono inteligente más sofisticado", y, por ser la primera vez en la historia del iPhone cuando se detecta un ataque remoto de jailbreak.

 Comentario de NSO
Dan Tynant, de The Guardian, escribió un artículo que incluía comentarios de NSO, donde afirmaron que brindan a los "gobiernos autorizados una tecnología que los ayuda a combatir el terrorismo y el crimen", aunque el Grupo le dijo que no tenía conocimiento de ningún incidente.

 Escepticismo del programa Bug-Bounty
Tras la noticia, los críticos afirmaron que el programa de recompensas de errores de Apple, que recompensa a las personas por encontrar fallas en su software, podría no haber ofrecido recompensas suficientes para evitar que se vendieran exploits en el mercado negro, en lugar de que se informara a Apple. Russell Brandom, de The Verge, comentó que el programa de recompensas por errores de Apple, que recompensa a las personas que logran encontrar fallas en su software, tiene un máximo de pagos de $ 200 000, "solo una fracción de los millones que se gastan regularmente en ataques iOS en el mercado negro.". Continúa preguntando por qué Apple no "se libra de las vulnerabilidades de seguridad?", Pero también escribe que "tan pronto como se notificaron las vulnerabilidades [de Pegasus], Apple las arregló, pero quedan muchos otros errores. Mientras que las compañías de software espía ven una compra de exploits como un pago único por años de acceso, la recompensa de Apple tiene que pagarse cada vez que aparece una nueva vulnerabilidad ". Brandom también escribió; "Los mismos investigadores que participan en la recompensa de errores de Apple podrían ganar más dinero vendiendo los mismos hallazgos a un agente explotador". Concluyó el artículo por escrito; "Es difícil decir cuánto daño podría haber sido causado si Mansoor hubiera hecho clic en el enlace del software espía... La esperanza es que, cuando el próximo investigador encuentre el próximo error, el pensamiento importe más que el dinero".

 Críticas por su uso

 El Salvador
En noviembre de 2021, periodistas de El Salvador denunciaron haber recibido un correo electrónico proveniente de Apple, en el que se leía

Luego de un peritaje realizado por Citizen Lab y Access Now, se concluyó que los celulares de los periodistas estuvieron infectados entre julio de 2020 y noviembre de 2021. El Gobierno de Nayib Bukele, hasta 2023, jamás se pronunció sobre las acusaciones.

La Comisión Interamericana de Derechos Humanos ordenó la investigación de estos delitos a la Fiscalía General de la República (El Salvador), quienes poco han hecho para averiguar quién estuvo detrás de estos ataques que vulneran la libertad de prensa.

 México
El spyware ha sido utilizado contra periodistas activistas de derechos humanos y políticos en México. Según un reportaje publicado por el New York Times, el gobierno mexicano fue el primer cliente del malware, empezando con la administración de Felipe Calderón Hinojosa y usado exponencialmente en el sexenio de Peña Nieto. En 2021 la Red en Defensa de los Derechos Digitales (R3D) denunció que el software se utilizó para espiar al periodista Ricardo Raphael, al activista de derechos humanos Raymundo Ramos Vázquez, así como a un periodista de Animal Político, cuyo nombre no fue publicado. En 2023 R3D dio a conocer que dos personas pertenecientes a la asociación civil Centro Prodh habían sido víctimas de espionaje.

 República Dominicana
Amnistía Internacional denunció que el dispositivo móvil de la periodista Nuria Piera había sido marcado e infectado por el software Pegasus en tres ocasiones entre los años 2020 y 2021. Se detectó que la primera infección de Pegasus al dispositivo de Piera fue el 20 de julio de 2020.

 Perú
Durante el gobierno de Pedro Castillo, el presidente le solicitó al ciudadano español Jorge Hernández, alias "El Español", la creación de un equipo especial de inteligencia clandestino para chuponear y atentar contra sus opositores. De esta forma, se dispuso la adquisición del software Pegasus para tales fines. Como parte de dicha operación, Castillo dio autorización a "El Español" y a Henry Shimabukuro para que se encarguen de la adquisición del equipo. Con ello en mente, ambos personajes se contactaron con Carlos Barba Daza, empresario de seguridad y asesor del entonces congresista fujimorista Luis Cordero Jon Tay, al que se le ofreció ser el nuevo jefe de la Dirección Nacional de Inteligencia (DINI), que no aceptó. Luego, le encargaron a Barba que realizara la búsqueda del software Pegasus en Panamá.  Ya en dicho país, Barba se puso en contacto con Cordero Jon Tay, realizando una visita en una feria tecnológica. Aunque se pusieron en contacto con la empresa de Pegasus, la empresa se negó a seguir negociando argumentando que querían hablar con alguien "debidamente acreditado por el gobierno". Finalmente, no se compró.

 Colombia
Durante la administración de Iván Duque se hizo compra del software Pegasus, siendo adquirido con recursos lícitos de Estados Unidos y usado para la lucha contra el narcotráfico aunque el presidente Gustavo Petro ha asegurado que dicho software ha sido usado para espiar a los militantes y afines a la coalición Pacto Histórico.

 Véase también
 iOS 9
 Espionaje con Pegasus al Gobierno de España

 Referencias
