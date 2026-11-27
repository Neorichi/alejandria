---
type: Artículo de enciclopedia
title: Vulnerabilidad del metarchivo de Windows
description: "La vulnerabilidad del metarchivo de Windows, también llamada ejecución de código de imagen del metarchivo y abreviada M CE, es una vulnerabilidad de seguridad en la forma en que algunas versiones del sistema operativo …"
resource: https://es.wikipedia.org/wiki/Vulnerabilidad_del_metarchivo_de_Windows
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Vulnerabilidad_del_metarchivo_de_Windows"}
license: CC BY-SA 4.0
id: eswiki-Vulnerabilidad_del_metarchivo_de_Windows
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Vulnerabilidad del metarchivo de Windows

La **vulnerabilidad del metarchivo de Windows**, también llamada ejecución de código de imagen del metarchivo y abreviada M
CE, es una vulnerabilidad de seguridad en la forma en que algunas versiones del sistema operativo Microsoft Windows manejan imágenes en el formato de metarchivo de Windows. Permite que se ejecute código arbitrario en las computadoras afectadas sin el permiso de sus usuarios. Fue descubierto el 27 de diciembre de 2005 y los primeros informes de las computadoras afectadas se anunciaron en 24 horas. Microsoft lanzó una actualización de alta prioridad para eliminar esta vulnerabilidad a través de Windows Update el 5 de enero de 2006. Los ataques que usan esta vulnerabilidad se conocen como vulnerabilidades de WMF.

La vulnerabilidad se encontraba en gdi32.dll y existía en todas las versiones de Microsoft Windows desde Windows 3.0 a Windows Server 2003 R2. Sin embargo, los vectores de ataque solo existen en versiones basadas en NT de Windows (Windows NT, Windows 2000, Windows XP y Windows Server 2003). Los exploits que aprovechan la vulnerabilidad en los sistemas basados en Windows NT facilitaron la propagación de varios tipos de malware, generalmente a través de descargas directas.

Debido al impacto extremo, este error ganó el Premio Pwnie 2007 por "Mass 0wnage" y "Breaking the Internet".

 Sistemas Afectados
Todas las versiones del sistema operativo Microsoft Windows admiten el estándar de gráficos de metarchivo de Windows. Todas las versiones de Windows 3.0 a Windows Server 2003 R2 contienen este defecto de seguridad. Sin embargo, Windows NT 4.0 y Windows XP, a menos que estén parchados, son más vulnerables que las versiones anteriores porque su instalación predeterminada permite la ejecución del código de metarchivo de Windows, la fuente de la vulnerabilidad. Las versiones posteriores de Windows no tienen esta vulnerabilidad.

Según el experto en seguridad del ordenador, Steve Gibson, Windows NT 4 es vulnerable y está disponible en la imagen está habilitado. Sistemas operativos de Windows que no tiene un preestreno de imagen habilitado o que tiene hardware - Prevención de Ejecución de Datos Basados (DEP).

Según el experto en seguridad del ordenador, Steve Gibson, Windows NT 4 es vulnerable y está disponible en la imagen está habilitado. Los sistemas operativos que no sean Windows (por ejemplo, macOS, Unix, Linux, etc.) no se ven afectados directamente. Sin embargo, un sistema que no sea Windows podría volverse vulnerable si ejecuta un software para ver archivos WMF de Windows. Esto podría incluir software que incorpore o clone la biblioteca de enlace dinámico (DLL) de Interfaz de Dispositivo de Gráficos (GDI) nativa de Windows o que ejecute programas de Windows o Windows a través de un emulador o capa de compatibilidad. Un sistema similar a Unix que usa Wine para emular a Windows, por ejemplo, podría ser explotado. Gibson escribió el programa MouseTrap, que su compañía distribuye como software gratuito, para detectar la vulnerabilidad del Meta archivo de Windows en los sistemas que ejecutan emuladores de Windows y Windows. Todas las aplicaciones no tendrán que ser susceptibles a esta proeza.

 La vulnerabilidad
Según valoraciones por F-Seguros, la vulnerabilidad es un defecto inherente  en el diseño de WMF archivos, porque la arquitectura subyacente de tales archivos es de una era anterior, e incluye características que dejan código real para ser ejecutado siempre que un WMF abre el archivo. El propósito original de este era principalmente para manejar la anulación de trabajos de impresión durante spooling.

Según Secunia, "La vulnerabilidad se debe a un error en el manejo de los archivos de metarchivo de Windows ('.wmf') que contiene registros de 'Escape' de SETABORTPROC especialmente diseñados. Dichos registros permiten que se ejecute una función arbitraria definida por el usuario cuando se procesa un archivo WMF falla ". De acuerdo con la documentación del SDK de Windows 3.1, el escape de SETABORTPROC fue obsoleto y reemplazado por la función del mismo nombre en Windows 3.1, mucho antes de que se descubriera la vulnerabilidad de WMF. Sin embargo, el código de escape obsoleto se conservó por compatibilidad con programas de 16 bits escritos para (o al menos compatibles con Windows 3.0). Este cambio ocurrió aproximadamente al mismo tiempo que Microsoft estaba creando la reimplementación de GDI para Windows NT de 32 bits, y es probable que la vulnerabilidad haya ocurrido durante este esfuerzo.

El mecanismo de 'Escape' en cuestión permite que las aplicaciones (no los metarchivos) accedan a las funciones del dispositivo de salida que GDI aún no ha resumido, como las curvas de Bézier aceleradas por hardware, el soporte de postscript encapsulado, etc. a algunos datos de la llamada, que generalmente solo se la pasan al conductor. Debido a que la mayoría de las llamadas de Escape producen gráficos reales, se permite el mecanismo de escape general en los metarchivos, aunque se pensó poco en la posibilidad de usarlo para SETABORTPROC, los intérpretes de metarchivos no vulnerables modernos ahora verifican el código de operación contra una lista negra o lista blanca, mientras el conjunto completo de códigos de operación disponibles para el código regular que llama directamente a las funciones de escape de GDI (debido a que dicho código ya se está ejecutando de la misma manera que el código que podría hacer la llamada de GDI, no hay riesgo de seguridad en ese caso).

Vale la pena señalar que Windows de 16 bits (excepto el modo Real de Windows 3.0 que se usa con poca frecuencia) fue inmune a la vulnerabilidad porque el puntero especificado en el metarchivo solo puede apuntar a datos dentro del metarchivo, y Windows de 16 bits siempre tuvo ana completa aplicación sin datos de ejecución ordenada por la arquitectura segmentada del modo protegido de 16 bits. Windows NT para arquitecturas de CPU distintas de 32 bits x86 (como MIPS, PowerPC, Alpha, Itanium y x86_64) requirió una programación orientada al retorno para explotarlas porque esas arquitecturas carecían de la funcionalidad de no ejecución de los procesadores x86 más antiguos

La vulnerabilidad es CVE-2005-4560 en Las Vulnerabilidades Comunes y base de datos de Exposiciones, EE.UU.-CERT referencia VU # 181038 y Artículo de Base de Conocimiento de Microsoft 912840. Encendido el 28 de diciembre de 2005 y publicado públicamente por presidente Alex de la compañía Eckelberry.

 Propagación e infección
Las computadoras pueden verse afectadas a través de la propagación de correos electrónicos infectados que llevan el archivo WMF pirateado como un archivo adjunto. La infección también puede resultar de:

 Ver un sitio web en un navegador que abre automáticamente archivos WMF, en cuyo caso, cualquier código malicioso potencial puede descargarse y abrirse automáticamente. Internet Explorer, el navegador web predeterminado para todas las versiones de Microsoft Windows desde 1996 hasta Windows 10, hace esto.
 Vista previa de un archivo infectado en el Explorador de Windows.
 Ver un archivo de imagen infectado utilizando algunos programas vulnerables de visualización de imágenes.
 Vista previa o abriendo correos electrónicos infectados en versiones más viejas de Microsoft Outlook y Outlook Express.
 Indexando un disco duro que contiene un archivo infectado con Google Desktop.
 Al hacer clic en un enlace a través de un programa de mensajería instantánea como Windows Live Messenger, AOL Instant Messenger (AIM) o Yahoo! Mensajero.

También se pueden usar otros métodos para propagar la infección. Debido a que el problema está dentro del sistema operativo, el uso de navegadores que no sean de Microsoft, como Firefox u Opera, no proporciona una protección completa. Por lo general, se solicita a los usuarios que descarguen y vean un archivo malicioso que infecte la computadora. Los archivos infectados se pueden descargar automáticamente, lo que abre la posibilidad de infección por la indexación del disco o la vista previa accidental.

Según las evaluaciones de la compañía de antivirus McAfee, la vulnerabilidad se ha utilizado para propagar el troyano de puerta trasera Bifrost. Otras formas de malware también han explotado la vulnerabilidad para entregar varias cargas útiles maliciosas.

McAfee afirma que la primera generación de tales explotaciones había sido encontrada por más del 6% de su base de clientes hasta el 31 de diciembre de 2005.

 Remiendo oficial
Microsoft lanzó un parche oficial para solucionar el problema el 5 de enero de 2006. Este parche puede aplicarse en lugar de otras medidas correctivas.

El parche oficial está disponible para Windows 2000, Windows XP y Microsoft Windows Server 2003. Windows NT 4 y otros sistemas operativos más antiguos no recibieron un parche, ya que para entonces ya no eran compatibles con Microsoft. Steve Gibson declaró en su Security Now! podcast # 20, que su compañía Gibson Research Corporation haría un parche disponible para los sistemas Windows 9x si Microsoft no lo hiciera. Después de una investigación adicional, Steve Gibson declaró, en una versión posterior de Security Now! podcast # 23, que Windows 9x y ME no son vulnerables y no necesitan parches. Los usuarios de Windows 9x / ME pueden ejecutar su utilidad Mouse Trap para ver esto por sí mismos.

Paolo Monti de Future Time, el distribuidor italiano del sistema antivirus NOD32 de Eset, ha proporcionado un parche gratuito para descargar de Windows NT. El parche funciona en sistemas operativos más antiguos, pero se suministra sin garantía.

Ha habido informes de que el parche oficial se instala automáticamente, incluso cuando la Actualización automática de Windows está configurada para preguntar antes de instalar las actualizaciones descargadas automáticamente. Esto provoca un reinicio automático, que puede causar la pérdida de datos si el usuario tiene un programa abierto con cambios no guardados.

 Otras medidas correctivas
Estas medidas son de interés histórico solo en los sistemas actualizados a partir del 5 de enero de 2006.

 Solución
Como una solución temporal antes de que estuviera disponible un parche, el 28 de diciembre de 2005, Microsoft recomendó a los usuarios de Windows que no volvieran a registrar el archivo de biblioteca de enlace dinámico shimgvw.dll (lo que se puede hacer ejecutando el comando regsvr32.exe / u shimgvw.dll desde el menú Ejecutar o el símbolo del sistema) que invoca la vista previa de archivos de imagen y es explotado por la mayoría de estos ataques. La DLL se puede volver a registrar después de aplicar parches ejecutando regsvr32.exe shimgvw.dll. Esta solución bloquea un vector de ataque común pero no elimina la vulnerabilidad.

 Parche de terceros
Ilfak Guilfanov lanzó un parche de terceros el 31 de diciembre de 2005 para desactivar temporalmente la llamada a la función vulnerable en gdi32.dll. Este parche no oficial recibió mucha publicidad debido a la falta de disponibilidad de uno oficial de Microsoft, que recibió la recomendación de SANS Institute Internet Storm Center y F-Secure. Debido a la gran cantidad de publicidad, incluido el hecho de estar indirectamente recortado, el sitio web de Guilfanov recibió más visitantes de los que podía afrontar y se suspendió el 3 de enero de 2006; El parche todavía estaba disponible para descargar desde una serie de réplicas, incluido el sitio web Internet Storm Center.

El sitio web de Guilfanov volvió a estar en línea el 4 de enero en un estado muy reducido. Ya que no proporcionaba el parche en el sitio debido a problemas de ancho de banda, la página de inicio proporcionaba una lista de réplicas donde un usuario podía descargar el parche y el verificador de vulnerabilidades asociado, y la suma de comprobación MD5 para el archivo, de modo que pudiera verificarse que El archivo descargado fue probablemente genuino.

Después de que Microsoft lanzó su parche, Guilfanov retiró el suyo.

 Técnicas de reducción del riesgo
Microsoft dice que su parche elimina la funcionalidad defectuosa en GDI32 que permitió la vulnerabilidad de WMF. Para las computadoras que ejecutan una versión sin parchar de Windows, se recomienda un enfoque de defensa en profundidad, para mitigar el riesgo de infección. Varias fuentes han recomendado esfuerzos de mitigación que incluyen:

 Hacer que el uso de la prevención de ejecución de datos forzada por hardware sea efectivo para todas las aplicaciones.
 Configure la aplicación WMF predeterminada para que no sea susceptible de infección, como el Bloc de notas.
 No utilice Internet Explorer, o al menos desactive las descargas al establecer la configuración de seguridad predeterminada en alta.
 Mantenga todo el software antivirus actualizado. Considere actualizaciones manuales frecuentes.
 Bloquee todos los archivos WMF en el perímetro de la red mediante el filtrado del encabezado de archivo.
 Hacer uso de las cuentas de los usuarios que se configuran con los derechos de usuario que se requieren.
 Desactive la carga de imágenes en Internet Explorer y en todos los demás navegadores.
 Deshabilita la carga de imágenes en Outlook Express.
 Deshabilita hipervínculos MSN Messenger.
 Deshabilite el servicio de indexación en Windows 2000, Windows XP y Windows Server 2003.
 Desactive las aplicaciones de Búsqueda de escritorio, como Google Desktop o Búsqueda de escritorio de Windows, hasta que se corrija el problema.

De acuerdo con este artículo del SANS Institute Internet Storm Center, el uso de un navegador web que no sea Internet Explorer puede ofrecer una protección adicional contra esta vulnerabilidad. Dependiendo de la configuración, estos navegadores pueden preguntarle al usuario antes de abrir una imagen con la extensión .wmf, pero esto solo reduce la posibilidad de abrir el Metarchivo de Windows creado con fines malintencionados, y no protege contra la vulnerabilidad que se explota, ya que estos navegadores aún abren el metarchivo. Si se está haciendo pasar por otro formato. Es mejor desactivar por completo la carga de imágenes en cualquier navegador utilizado.

 Acusaciones
En 2006, Steve Gibson sugirió que la naturaleza peculiar del 'error' era una indicación de que la vulnerabilidad era en realidad una puerta trasera diseñada intencionalmente en el sistema. La acusación se convirtió en una afirmación y se extendió por Internet como un rumor después de que el sitio web de noticias de tecnología Slashdot recogió la especulación de Gibson. El rumor fue ampliamente desacreditado y Thomas Greene, al escribir en The Register, atribuyó el error de Gibson a "su falta de experiencia en seguridad" y lo llamó un "experto en popinjay".

 Notas

 ^  Security Watch: Iniquitous Images Imperil the Internet!, Larry Seltzer, PC Magazine.
 ^A Description of the Image Preview Feature in Windows Millennium Edition, Microsoft.
 sunbeltblog.blogspot.com Microsoft clarifies DEP issue
 ^ Library for non-Windows operating systems to run WMF files.
 ^ Linux/BSD still exposed to WMF exploit through WINE, ZDNet.
 ^ It's not a bug, it's a feature, F-Secure.
 ^  Proeza-WMF , por McAfee
 ^ Microsoft Security Advisory (912840) - Vulnerability in Graphics Rendering Engine Could Allow Remote Code Execution, Microsoft Official Advisory on the vulnerability.
 ^ http://www.hexblog.com/2005/12/wmf_vuln.html, unofficial patch by Ilfak Guilfanov.
 ^ Trustworthy Computing, SANS Institute Internet Storm Center.
 ^ Ilfak to the rescue!, F-Secure.
 ^ Trustworthy Computing, Slashdot. Linking to SANS Institute Internet Storm Center's article titled Trustworthy Computing (see above).
 ^ .MSI Archivo de instalador para WMF el defecto disponible, SANS Centro de Tormenta de Internet de Instituto.
 ^ How to Configure Memory Protection in Windows XP SP2, software-enforced Data Execution Prevention (DEP) feature in Microsoft Windows XP SP 2.
 ^ How to improve browsing performance in Internet Explorer (KB153790), Microsoft.
 ^ Images are blocked when you open an e-mail message in Outlook Express on a Windows XP Service Pack 2-based computer (KB843018), Microsoft.
 ^ http://www.nod32.ch/en/download/tools.php Unofficial WMF patch by Paolo Monti distributed by ESET.
 ^ http://blogs.securiteam.com/index.php/archives/210 Unofficial Windows 98SE patch by Tom Walsh.

 Referencias

 Enlaces externos

 GRC  M.I.C.E. Metafile Ejecución de Código de la imagen
 Boletín de Seguridad del Microsoft para Usuarios de Casa del novato
 SEÑORA de Boletín de Seguridad de Microsoft08-021
 SEÑORA de Boletín de Seguridad de Microsoft06-001
 WMF FAQ - SANS Centro de Tormenta de Internet de instituto
 Defecto de Seguridad del Windows Es  esevere' - Correo de Washington
 Windows de Microsoft WMF "SETABORTPROC" Ejecución de Código Arbitrario - Secunia aconsejable
 Resumen de estado cuando de 1 enero
 Mirando en el WMF asunto, cómo   consiga allí? - Centro de Respuesta de Seguridad de Microsoft Blog
 La proeza nueva liberada para el WMF vulnerabilidad - SANS Centro de Tormenta de Internet de Instituto
 Ser prudente con WMF archivos - F-Seguros
 Lotus Nota Vulnerable a WMF Proeza de 0 Días - SANS Centro de Tormenta de Internet de Instituto
 Vulnerabilidad Checker - Ilfak Guilfanov
 Proeza de ejemplo - Metasploit Proyecto
 Páginas de Red de Desarrollador de Microsoft para Escapada y SetAbortProc
 Mark Russinovich  Comentario Técnico en el Backdoor Controversia
