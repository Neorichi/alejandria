---
type: Artículo de enciclopedia
title: ILoveYou
description: ILoveYou (o VBS/LoveLetter/TheLoveBug) es un gusano escrito en VBScript.
resource: https://es.wikipedia.org/wiki/ILoveYou
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/ILoveYou"}
license: CC BY-SA 4.0
id: eswiki-ILoveYou
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# ILoveYou

- **Nombre:** ILoveYou
- **Desarrollador:** Onel de Guzman
- **Lanzamiento:** 2000
- **Descubrimiento:** 4 de mayo de 2000
- **Género:** Gusano informático
- **Plataforma:** Microsoft Windows

***ILoveYou*** (o ***VBS/LoveLetter/TheLoveBug***) es un gusano escrito en VBScript. En mayo de 2000, infectó aproximadamente a cincuenta millones de computadores, provocando pérdidas de más de diez mil millones de dólares.

 Arquitectura del gusano

El gusano sobrescribe con su código los archivos con extensiones .VBS y .VBE. Elimina los archivos con extensiones .JS, .JSE, .CSS, .WSH, .SCT y .HTA, y crea otros con el mismo nombre y extensión.VBS en el que introduce su código. También localiza los archivos con extensión .JPG, .JPEG, .MP3 y .MP2, los elimina, y crea otros donde el nuevo nombre está formado por el nombre y la extensión anterior más VBS como nueva extensión real.

VBS/LoveLetter llega al usuario en un mensaje de correo electrónico que tiene por Asunto: 'ILOVEYOU' e incluye un fichero llamado 'LOVE-LETTER-FOR-YOU. TXT.vbs'. Cuando este virus se ejecuta, crea varias copias de sí mismo en el disco duro con los siguientes nombres:

Tras esto, el virus crea varias entradas en el registro de configuración de Windows.

VBS/LovelLetter comprueba, en el directorio SYSTEM de Windows, la existencia del fichero WinFAT32.exe. Si lo encuentra genera un número aleatorio entre 1 y 5, y dependiendo del número que resulte, crea la entrada de registro 'HKCU\Software\Microsoft\InternetExplorer\Main\Start, a la que le asigna un valor para bajarse el fichero WIN-BUGSFIX. EXE.

Tras realizar esta operación, el virus genera, en el directorio SYSTEM de Windows, el fichero LOVE-LETTER-FOR-YOU.HTM, que será el que posteriormente envíe por IRC. Después, el gusano se envía a todas las direcciones que encuentra en el libro de direcciones de Microsoft Outlook.

Cuando ya se ha enviado por correo, VBS/LoveLetter realiza su efecto destructivo. En concreto, busca en el *path* del disco duro y en el de todas las unidades de red archivos con extensión vbs, vbe, js, jse, css, wsh, sct y hta. Cuando los encuentra, los sobreescribe con su código, modifica su tamaño y les cambia la extensión a VBS, lo que conlleva la pérdida de toda la información contenida en los archivos. Si los archivos que encuentra poseen extensión jpg o jpeg también los sobreescribe, cambia su tamaño y les añade al final la extensión VBS (quedando como jpg.vbs o jpeg.vbs).

Si *VBS/LoveLetter* encuentra un fichero con extensión *.mp3* o *.mp2,* genera una copia de sí mismo con el nombre del archivo encontrado y añade la extensión VBS ocultando los ficheros originales. El virus también comprueba si en el directorio en el que se está realizando la búsqueda se encuentra alguno de los siguientes ficheros: mirc32.exe, mlinnk32.exe, mirc.ini, scrip.ini o mirc.hlp. Si los encuentra crea el fichero 'script.ini', que será el encargado de mandar por IRC el fichero LOVE-LETTER-FOR-YOU.HTM a todo aquel que se conecte al mismo canal que él.

 Persecución de los autores
 *ILoveYou* apareció en internet el 4 de mayo de 2000. El virus se presentó en un principio en forma de mensaje de correo con el asunto "ILOVEYOU" y un archivo adjunto con el nombre "LOVE-LETTER-FOR-YOU.TXT.vbs", que al ser abierto, infectaba el ordenador y se autoenviaba a las direcciones de correo que el usuario tuviera en su agenda de direcciones. Comenzó en Filipinas y le bastó un solo día para propagarse por todo el mundo, infectando ordenadores en Hong Kong, Europa y luego en los Estados Unidos.

Cinco días más tarde, se reconocían 18 mutaciones del virus. Al multiplicarse explosivamente, este gusano condujo a Internet al colapso.

El 8 de mayo, Reonel Ramones, un empleado bancario de 27 años, fue detenido en Manila por la Oficina Nacional de Investigaciones (NBI) de la policía de Filipinas y acusado preliminarmente de vulnerar la Ley Normativa sobre Instrumentos de Acceso, cuyo principal objetivo es proteger las contraseñas para las tarjetas de crédito. Sin embargo, fue liberado al día siguiente por orden de la justicia filipina, al carecer de pruebas suficientes para mantenerlo bajo custodia. La acusación se había fundamentado en una queja de un proveedor de servicios de Internet de que el virus se había originado en el departamento en que Ramones vivía con su compañera, Irene de Guzmán, y el hermano de esta, Onel de Guzmán. Todos ellos habían estudiado en el Colegio de Computación AMA de Manila (AMACC).

Tres días más tarde, el 11 de mayo, el virus estaba muy expandido por todos los PC y la situación se estaba saliendo de control. Onel de Guzmán se presentó con su abogado en conferencia de prensa para reconocer que pudo haber trasmitido el virus "accidentalmente". Tomando como base los programas encontrados en el departamento de Guzmán y Ramones por la policía, se dijo en un primer momento que el virus había sido elaborado por un grupo de estudiantes del Colegio de Computación AMA denominado "GRAMMERSoft", grupo al cual pertenecía Guzmán. Sin embargo, este luego confesaría que había creado el virus por sí solo, y que correspondía a la aplicación de sus tesis: una guía sobre cómo robar códigos secretos a través de Internet o cómo introducirse en un ordenador ajeno y tomar su control.

Pese a que en un principio la Oficina Nacional de Investigaciones (NBI) imputó cargos a Guzmán tomando como base la Ley Normativa sobre Instrumentos de Acceso, el 21 de julio la justicia de Filipinas los desestimó todos, puesto que esta Ley no se aplicaba a la intrusión en las computadoras. De hecho, en ese momento Filipinas carecía de leyes sobre delitos informáticos, y por lo mismo, a Guzmán se le retiraron todos los cargos.

 Efectos y daños causados
El virus se propagó rápidamente por todo el mundo. El 13 de mayo de 2000 se habían reportado 50 millones de infecciones alrededor del globo, cifra que representaba al 10% del total de computadores con conexión a Internet en esa época. El virus atacó a El Pentágono, la CIA, el Parlamento Británico y las grandes empresas. En España, por ejemplo, el 80% de las empresas sufrieron los ataques del virus. Se estimó que el monto de los daños causados fue entre 5.5 a 8.7 miles de millones de dólares, derivados principalmente del trabajo de eliminación de los gusanos de los sistemas infectados.

Por otra parte, este hecho dejó en manifiesto en Filipinas la necesidad de contar con una legislación reguladora de la actividad en Internet. Por lo mismo, el 14 de junio de 2000, se dictó la Ley N.º8.792, que actualmente, en su Sección 33 sanciona la inducción de virus computacionales y otros con el objetivo de dañar mensajes de datos y documentos electrónicos. Con todo, no pudo ser aplicada en contra de Onel de Guzmán, puesto que el hecho tipificado (la liberación del virus) había sido ejecutado antes de la entrada en vigencia de esta ley penal.

 Véase también
 Virus informático
 Gusano informático
 Polimorfismo
 Seguridad informática

 Referencias
