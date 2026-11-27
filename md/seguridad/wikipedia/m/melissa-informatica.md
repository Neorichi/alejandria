---
type: Artículo de enciclopedia
title: Melissa (informática)
description: Melissa es un de Microsoft Office lanzado en 1999.
resource: https://es.wikipedia.org/wiki/Melissa_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Melissa_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Melissa_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Melissa (informática)

- **Titulo:** Melissa
- **Tipocabecera:** informática
- **Etiqueta1:** Nombre Tecnico
- **Datos1:** WM97.Melissa
- **Etiqueta2:** Fecha de descubrimiento
- **Datos2:** 1999
- **Etiqueta3:** Sistema Operativo Afectado
- **Datos3:** Microsoft Windows
- **Etiqueta4:** Tipo
- **Datos4:** Macrovirus

**Melissa** es un  de Microsoft Office lanzado en 1999. También es conocido como **W97M**, Simpsons (en referencia a los dibujos animados estadounidenses), Kwyjibo o Kwejeebo (en referencia a la palabra imaginaria que Bart Simpson intenta usar en el Scrabble y que aparece en el código del virus: «written by Kwyjibo»).

 Historia
El 26 de marzo de 1999 y en apenas unos días, protagonizó uno de los casos de infección masiva más importantes de la historia de los virus informáticos. De hecho, compañías como Microsoft, Intel o Lucent Technologies tuvieron que bloquear sus conexiones a Internet debido a la acción de Melissa.

Melissa se distribuyó por primera vez en la discusión del grupo de noticias Usenet:alt.sex. El virus estaba dentro de un archivo llamado "List.doc", que decía contener una lista de contraseñas con las que se permitía el acceso a 80 sitios web pornográficos. La forma original del virus fue enviada por e-mail a muchas personas.

 Autor
Melissa fue creado por David L. Smith de Aberdeen, Nueva Jersey. Él reconoció en su declaración de culpabilidad que el virus Melissa causó más de 80 millones de dólares en daños a las empresas norteamericanas.

El virus lo creó en memoria de una bailarina topless de Florida de la cual se había enamorado. Por ello fue condenado a 10 años de prisión y multado con 5000 dólares.

Smith posteriormente colaboraría para ayudar al FBI en la búsqueda de Jan de Wit, el creador holandés del virus informático Anna Kournikova.

 Especificaciones del virus
Melissa se puede propagar en los procesadores de textos Microsoft Word 97 y Word 2000 y Microsoft Excel 97, 2000 y 2003. Se puede autoenviar por correo electrónico desde Microsoft Outlook 97 o 98, enviándolo a los primeros 50 contactos de la libreta de direcciones en un email con el asunto "*Important message from...*" y en el cuerpo del mensaje "*Here is that document you asked for… don’t show anyone else;-)*". Al abrirse, el virus modificaba el archivo de plantilla por defecto en Word "normal.dot", cambiaba el registro de Windows y se replicaba por correo electrónico.

 Versión del virus
 Melissa A
De: *(nombre del usuario infectado)*

Asunto: *Mensaje Importante de "Nombre del remitente*

Para: (*50 nombres de la agenda*)

Texto del Mensaje: *Aquí está ese documento que usted me solicitó... no se lo muestre a nadie;-)*

Archivo adjunto: *LIST.DOC*

Es un documento de Word que contiene el virus que, si se descarga y se abre, ejecuta la macro del documento y se inician los intentos de envíos masivos de sí mismo a las 50 personas de la libreta de direcciones del correo electrónico, multiplicándose con ello, y al ser infectado escribe en los documentos que se tengan abiertos:

“Veintidós puntos, más triple puntuación de palabras, más cincuenta puntos por usar todas mis letras. El juego termina. Me voy de aquí”

Cuando se abre el archivo de Word, se infecta la plantilla de documentos normal.dot, propagando la infección a a todos los documentos de Word.

Esto ocurre cuando el minutero del reloj coincide con el día del mes.

 Melissa AD WM97
Este es un virus de macros y Gusano de Internet.

Se envía por correo a las primeras 150 direcciones de e-mail, de la agenda del Outlook.

Crea tres archivos en el directorio raíz, el *CMOS.COM, FAT32.COM y DRIVES.BAT*.

El archivo *DRIVES.BAT* se ejecuta al reinicio del equipo al correr el *AUTOEXEC.BAT*, el cual es modificado para ello, e intenta borrar todos los datos en los discos y los otros existentes.

El virus cambia la fecha de la computadora.

 Melissa AM
Si se tienen más de 10 nombres en su libreta de direcciones en el Outlook, el virus se reenviará a sí mismo vía e-mail a un total de 30 o 60% de estos contactos. Estos mensajes serán enviados aleatoriamente con los atributos de prioridades Baja, Normal o Alta.

Asunto: Se genera al azar construyéndose una frase con una serie de palabras como: *Hello!, Hi!, Here, I think this,Gee... Guess this, is, used to be, are, that, the, your, file, document,.doc, you requested, they asked.*

Esto puede generar:

Asuntos como:
*¡Hola! Creo que esto solía ser el documento que ha solicitado.*

*¡Hola! Vaya... Supongo que esto es el archivo que pidió".*

Adjunto al mensaje se incluye un documento Word infectado.

WM97/Melissa AM también envía información del sistema infectado, incluyendo datos como nombre de usuario, zona horaria, nombre del usuario registrado, etc., a ciertas direcciones de correo electrónico. Se supone que la idea del autor es recabar con esto una base de datos de los usuarios infectados.

 Melissa AO
En equipos que cuentan con Outlook, enviar e-mail con:

Asunto: *Muy URGENTE: a todos los usuarios de correo electrónico.*

Mensaje: *Este anuncio es para todos los usuario de correo electrónico. Por favor, tenga en cuenta que nuestro servidor de correo electrónico se cayó y se recomienda que lea el documento que se adjunta con este e-mail.*

 Melissa B
Es una variante que solo tiene activa su parte de gusano. En su código, en el campo de comentario del autor del documento, se lee: No queremos infectar su PC; solo avisarle

Asunto: *No confíes en nadie*.

Mensaje: Ten cuidado con lo que abres, podría ser un virus.

Archivo adjunto: Cuando el documento es abierto, el gusano comprueba el registro del sistema buscando rastros del "Melissa.a", y si no está presente, envía un mensaje con una copia del documento infectado, Con el texto:
Esto podría haber tenido resultados desastrosos. Ten más cuidado la próxima
vez que se abre un e-mail. Protéjase a usted mismo! Descubra cómo en estos sitios web: Y anexa algunas ligas a sitios Web.

 Melissa I
Esta versión del virus, sortea aleatoriamente el asunto y el mensaje de entre estas ocho posibilidades en Inglés

1. Asunto: *80mb gratis de espacio Web! *
Mensaje: *Echa un vistazo al documento adjunto para más detalles sobre cómo obtener el espacio libre. Está bien, ahora tengo un montón de espacio.*

2. Asunto: ¡*Mira esto!*
Mensaje: *Esto es un poco de material malvado!*

3. Asunto: *Sitios Chulos.*
Mensaje: *Echa un vistazo al documento adjunto para obtener una lista de algunos de los mejores sitios en la Web.*

4. Asunto: *Descargas Gratis.*
Mensaje: *Aquí está una lista de sitios, donde se puede obtener descargas gratuitas. (El asterisco se sustituye con un carácter aleatorio).*

5. Asunto: *Hardware barato*.
Mensaje: *He adjuntado una lista de sitios web donde se puede obtener Hardware barato.*

6. Asunto: *Música gratis*.
Mensaje: A*quí está una lista de lugares donde se puede obtener música gratis.*

7. Asunto: *Pregunta para usted...*
Mensaje: *Es bastante complicado así que lo he conectado.*

8. Asunto: *Software barato*.
Mensaje: El documento adjunto contiene una lista de sitios web donde se puede obtener software barato.

Archivo adjunto: El virus Melissa I, utiliza una clave de registro llamada "empírica", para comprobar que se ha hecho el envío de correo masivo.

Si el número de minutos es igual al número de horas, (ejemplos 8:08 A.M., 10:10 A.M.) El virus inserta el texto, en el documento activo:

*Todos los imperios caen, sólo tienes que saber dónde presionar*.

 Melissa O, W97M.Melissa AA, W97M.Duhalde, W97M.Melissa Variant.
Variante modificada que emplean capacidades heurísticas, para evitar que los antivirus lo detecten.

Este virus contiene referencias a la elección presidencial del 9 de abril de 2000, en Perú.

Se trata de un virus de MACRO que es capaz de transmitirse por correo electrónico automáticamente de un usuario a otro y que podría transmitir información confidencial desde la computadora infectada sin que se de cuenta el usuario.

Contiene 2 rutinas maliciosas (payloads), dependiendo de si se usa Office 97 o 2000, con lo que desactivará la opción de Seguridad en Macros del menú Herramientas.

Modifica el registro de Windows, de este modo para saber que ya se ha enviado y así no volver a hacerlo en ese equipo. Dicha marca es la entrada:

HKEY_CURRENT_USER\Software\Microsoft\Office\ x?" con valor "y". Elecciones2000 = Pacocha:-P

También modifica la plantilla Normal.DOT, con lo que se infecta a partir de que se guarde el documento en Word.

El correo electrónico tiene el siguiente aspecto:

Asunto: *Presidente Duhalde*

Mensaje: *Programa de Gobierno 1999 - 2004.*

Archivo adjunto: *AVISEN A LOS QUE PUEDAN*

*Me acaban de avisar que ha aparecido un virus que se envía por correo bajo el título de ELECCIONES 2000 ÚLTIMAS ENCUESTAS DE APOYO. Cuando lo abren se borra el disco duro. Por favor reenvíen este correo a sus amigos para alertarles al respecto. Dígales que los borren sin abrirlos.*

Si se tiene abierto un documento y los minutos del reloj más uno coinciden con el día, se inserta un espacio en blanco en el texto en donde esta el cursor.

 Melissa Papa

El "Papa" está basado en el mismo código del "Melissa", infecta únicamente archivos de Excel 97. Utiliza también el Microsoft Outlook para sus envíos.

Sin embargo, por su método de infección, puede considerarse un gusano.

El código de este gusano (worm) contiene un procedimiento que abre e infecta cualquier libro de trabajo de Excel. Utiliza lenguaje Visual Basic, envía sus propias copias vía e-mail,  del Outlook, a cada una de las primeras 60 direcciones de la libreta de direcciones:

Asunto: *Fwd: Libro de trabajo de todos. Net y Fred Cohen*

Texto:*Contiene información urgente. No le preste atención a advertencias de macros.*

Al mensaje se adjunta un archivo de Excel infectado.

Aleatoriamente en su número de envíos, el gusano inunda con mensajes el sitio Web de "Fred Cohen & Associates" ó una IP específica.

 Melissa U (gen1)
Actúa en las versiones Word 97 o Word 2000.

El archivo adjunto: Se descarga como un archivo corrupto o defectuoso por lo que los antivirus lo ignoran y al momento de ser ejecutado lo reacomoda haciéndolo válido.

Al ser abierto, el virus se activa y empieza a borrar archivos importantes de sistema como son: •	 c: \ command.com •	 c: \ IO.SYS •	 c: \ Ntdetect.com •	 c: \ Suhdlog.dat •	 d: \ command.com •	 d: \ IO.SYS •	 D: \ Suhdlog.dat

Posteriormente envía automáticamente los correos electrónicos, a través de las listas de direcciones del correo electrónico, de los que reciben el correo infectado.

 Melissa V
Esta variante es similar a Melissa.U. Se envía a 40 direcciones de e-mail.

Mensaje: Tema: Mis imágenes (nombre de usuario)

El mensaje está vacío, y (nombre de usuario) se sustituye con el nombre del usuario registrado en Word.

Se eliminarán todos los archivos de la raíz de las diferentes unidades del equipo, Después de que Melissa.V se ha enviado por correo.

 Melissa W

Se activa la carga útil a las 10 horas del día 10 de cada mes, cuando el virus inserta el siguiente texto en el documento abierto:

*worm!  Vamos que nos gusta.*

 Véase también
 Antivirus
 Malware
 Virus informático

 Referencias
