---
type: Artículo de enciclopedia
title: Ataques ransomware WannaCry
description: "Los ataques ransomware de la variedad WannaCry (en inglés WannaCry ransomware attack o WannaCry DoublePulsar Attack), fueron ataques informáticos que usaron el criptogusano conocido como WannaCry (también denominado …"
resource: https://es.wikipedia.org/wiki/Ataques_ransomware_WannaCry
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataques_ransomware_WannaCry"}
license: CC BY-SA 4.0
id: eswiki-Ataques_ransomware_WannaCry
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataques ransomware WannaCry

- **Título:** Ataques ransomware WannaCry
- **Lugar:** 150 países.
- **Fecha:** Desde el 12 de mayo de 2017
- **Tipo:** Ciberataque
- **Perpetrador:** Hipotéticos: NSA o Park Jin Hyok
- **Motivo:** Desconocido (probablemente una muestra de poder).

Los **ataques ransomware** de la variedad **WannaCry** (en inglés **WannaCry ransomware attack** o **WannaCry DoublePulsar Attack**), fueron ataques informáticos que usaron el criptogusano conocido como WannaCry (también denominado WannaCrypt, WanaCrypt0r 2.0, Wanna Decryptor) dirigidos al sistema operativo Windows de Microsoft. Durante el ataque, los datos de las víctimas fueron cifrados, en donde se les solicitó un rescate económico que debía ser pagado con la criptomoneda Bitcoin, para permitir de nuevo el acceso a los datos.

El ataque comenzó el viernes, 12 de mayo de 2017 y ha sido descrito como sin precedentes en tamaño, infectando más de 230.000 computadoras en más de 150 países. Los países más afectados fueron Rusia, Ucrania, India y Taiwán, así como partes del servicio nacional de salud de Gran Bretaña (NHS), Telefónica de España, FedEx, Deutsche Bahn, y las aerolíneas LATAM; junto con muchos otros blancos a nivel mundial.

Los ataques ransomware normalmente infectan una computadora cuándo un usuario abre un correo electrónico phishing y, a pesar de que presuntamente correos electrónicos de esta clase serían los causantes de la infección WannaCry, este método de ataque no ha sido confirmado. Una vez instalado, WannaCry utiliza el exploit conocido como EternalBlue, desarrollado por la Agencia de Seguridad Nacional de los Estados Unidos (NSA), para extenderse a través de redes locales y anfitriones remotos que no hayan recibido la actualización de seguridad más reciente, y de esta manera infecta directamente cualquier sistema expuesto. Un “parche” crítico habría sido emitido por Microsoft el 14 de marzo de 2017 para eliminar la vulnerabilidad subyacente para sistemas soportados por Microsoft en la actualidad, lo cual se dio casi dos meses antes del ataque, sin embargo, muchas organizaciones no llegaron a aplicarlas.

Aquellas máquinas usando sistemas más antiguos, para los que Microsoft no publica actualizaciones, como Windows XP y Windows Server 2003, se encontraban en una situación de riesgo, sin embargo Microsoft ha tomado la decisión inusual de publicar actualizaciones para estos sistemas operativos para todos los clientes.

Poco después del comienzo del ataque, un investigador de seguridad web llamado Marcus Hutchins, conocido en la blogosfera como “MalwareTech” accionó sin advertirlo un “botón de apagado” propio del gusano, al registrar un nombre de dominio hallado en el código del ransomware. Esto retrasó la difusión de la infección, pero se han detectado nuevas versiones que carecen de este “botón de apagado”.

 Wanna Cry
**WannaCrypt0r 2.0**, también conocido como **WannaCry**, es un *programa dañino* de tipo *ransomware*. En septiembre de 2018, el Departamento de Justicia de los Estados Unidos inculpó al norcoreano Park Jin Hyok de ser el creador de WannaCry y haber cometido el ataque informático de alcance mundial en 2017.

 Antecedentes
El supuesto vector de infección, EternalBlue, fue publicado por el grupo cracker *The Shadow Brokers* el 14 de abril de 2017, junto con otras herramientas aparentemente filtradas del colectivo *Equation Group*, de quienes se presume un vínculo con la Agencia de Seguridad Nacional de Estados Unidos.

EternalBlue aprovecha la vulnerabilidad CVE-2017-01447 usada en la implementación ideada por Microsoft para el protocolo Server Message Block (SMB). Esta vulnerabilidad de Windows no es un defecto que permita un ataque de día cero, sino uno para el que Microsoft ya había publicado herramientas, junto con un parche de seguridad para reparar dicha vulnerabilidad dos meses antes, el 14 de marzo de 2017. El parche se aplicaba al protocolo SMB utilizado por Windows, y cubría varios clientes del sistema operativo Windows de Microsoft, incluyendo Windows Vista en adelante (con la excepción de Windows 8), así como versiones incrustadas y de servidor, como Windows Server 2008 en adelante y Windows Embedded POSReady 2009, sin embargo, el parche no cubría el más antiguo Windows XP. Según Dona Sarkar, directora del programa Windows Insider, Windows 10 no fue afectado.

Desde el 21 de abril de 2017, investigadores de seguridad informaron que la cantidad de ordenadores con la puerta trasera DoublePulsar instalada ascendía a las decenas de miles. Desde el 25 de abril, distintos reportes estimaban que el número de computadores infectados con DoublePulsar llegaba a varios cientos de miles, y que este número aumentaba exponencialmente con el paso de los días. Aparentemente, DoublePulsar era también instalado durante el ataque.

 El ataque cibernético

El 12 de mayo de 2017, WannaCry empezó afectar ordenadores en todo el mundo. La infección inicial podría haber empezado a través del uso de una vulnerabilidad en las defensas de red o un ataque de phishing bien ejecutado sobre una primera víctima. Cuando es ejecutado, el malware primero verifica el "botón de apagado" el cual corresponde a un nombre de dominio específico. Si este no es encontrado, entonces el ransomware cifra los datos del ordenador, y procede a tratar de usar el exploit SMB para extenderse a ordenadores aleatorios en el Internet, y "lateralmente" a ordenadores en la misma red. Como otras variaciones de ransomware, la "carga útil" encuentra y ubica una variedad de archivos, para luego notificar al usuario que los archivos han sido cifrados, reclamando un pago de alrededor de $300 en bitcoin en un plazo de tres días o $600 siete días tras la notificación.

Varias organizaciones que no habían instalado la actualización de seguridad de Microsoft estuvieron afectadas por el ataque. Aquellos que aún usaban Windows XP se encontraban en un riesgo comparativamente más alto  ya que no se habían publicado parches de seguridad para este sistema operativo desde abril de 2014 (con la excepción de una actualización de emergencia publicado en mayo de 2014). Aun así, el día después del brote epidémico, Microsoft publicó un parche de seguridad de emergencia para Windows XP.

Según *Wired*, los sistemas afectados también tendrían instalada la puerta trasera conocida como DoublePulsar, la cual debe ser removida al descifrar el sistema..

Tres direcciones bitcoin hard-coded, o "carteras", fueron usadas para recibir los pagos de las víctimas. De la misma manera que sucede con esta clase de cartera, sus transacciones y balances son accesibles al público, pero los dueños de cartera permanecen en el anonimato. Al 19 de mayo de 2017, 2:33 UTC, un total de 238 pagos, que acumulaban $72,144.76 habían sido transferidos.

 Impacto
Este episodio en la historia de los ataques computacionales no tiene precedente según Europol. Esta agencia estima que alrededor de 200,000 ordenadores fueron infectados en 150 países. Según Kaspersky Lab, los cuatro países más afectados fueron Rusia, Ucrania, India y Taiwán.

El ataque afectó muchos hospitales del Servicio Nacional de Salud (NHS) en Inglaterra y Escocia, y hasta 70,000 dispositivos pudieron haber sido afectados, incluyendo ordenadores, escáneres de IRM, refrigeradores para el almacenamiento de sangre y equipamiento de quirófano. El 12 de mayo, algunos servicios del NHS tuvieron que ignorar emergencias no críticas, y algunas ambulancias fueron desviadas. En 2016, se reportó que miles de ordenadores en 42 locaciones distintas del NHS a lo largo de Inglaterra todavía usaban Windows XP como sistema operativo. Los hospitales del NHS en Gales e Irlanda del Norte no fueron afectados por el ataque.

La instalación industrial de Nissan Motor Manufacturing, ubicada en Tyne y Wear, detuvo la producción después de que el ransomware infectó algunos de sus sistemas. Renault también detuvo la producción en varios sitios en un intento de parar la propagación del software malicioso.

El ataque habría podido ser mucho peor de no ser por el investigador independiente que halló el "botón de apagado" que los creadores del software habían incluido en el mismo, o si el ataque hubiera sido dirigido a infraestructura crítica, como plantas de energía nuclear, represas o sistemas de ferrocarril.

 Ciberataque global
El 12 de mayo de 2017 entre las 8 y las 17:08 horas UTC se registró un ataque a escala mundial que afectó a las empresas Telefónica, Iberdrola y Gas Natural, entre otras compañías en España, así como al servicio de salud británico, como confirmó el Centro Nacional de Inteligencia. La prensa digital informaba aquel día que al menos 141 000 computadores habían sido atacados en todo el mundo.

Los expertos sostienen que WannaCry usó la vulnerabilidad EternalBlue, desarrollada por la Agencia de Seguridad Nacional estadounidense y filtrada por el grupo The Shadow Brokers, que permite atacar computadores con el sistema operativo Microsoft Windows no actualizados debidamente. La compañía Microsoft había comenzado a distribuir actualizaciones de seguridad al día siguiente de conocerse esta vulnerabilidad, el 10 de marzo de 2017, a través de Windows Update, pero solamente para las versiones de Windows posteriores a Windows Vista. El 13 de mayo de 2017, ante la supuesta gravedad del ataque, publicó un parche separado para Windows 8, Server 2003 y XP. Muchos computadores que no tenían aplicadas las actualizaciones de seguridad MS17-010 de marzo de 2017 quedaron gravemente afectados, con sus archivos cifrados y mostrando un mensaje en pantalla que exigía un rescate de 300 dólares en bitcoins a cambio de descifrar los archivos.

Marcus Hutchins, un experto en ciberseguridad de Reino Unido evitó en gran medida la expansión del ciberataque global. El autor del blog MalwareTech estaba estudiando el programa dañino cuando se dio cuenta de que el mismo intentaba conectarse a un dominio no registrado: si no lo lograba, cifraba el equipo; si lo lograba, se detenía. Una vez que este experto en seguridad registró el dominio, a las 17:08 UTC del 12 de mayo, cesó el ataque. Todas las medidas urgentes que se tomaron a partir de esa hora fueron prácticamente innecesarias.

 Respuesta defensiva
Varias horas después de la liberación inicial del ransomware, el 12 de mayo de 2017, mientras intentaba establecer la escala del ataque, Marcus Hutchins, un investigador quien bloguea bajo el seudónimo @MalwareTech, accidentalmente descubrió lo que en la práctica resulta ser un "botón de apagado" del malware, incluido como hard code en el código del mismo. Registrando un nombre de dominio correspondiente a un sinkhole DNS, logró detener la propagación del gusano, porque el ransomware solamente cifraba los archivos del ordenador si era incapaz de conectarse a dicho dominio. Mientras esto no ayudó a los sistemas que ya habían sido infectados, retrasó severamente la propagación de la infección inicial y dio tiempo para que se desplegaran medidas defensivas en todo el mundo, particularmente en América del Norte y Asia, en donde el ataque no había alcanzado la misma extensión que en otras zonas. Se ha sugerido que el propósito de este "botón de apagado" incluía hacer el programa más difícil de analizar.  Algunas configuraciones de red pueden impedir la efectividad de este método.

Microsoft publicó una declaración recomendando a los usuarios que instalaran la actualización MS17-010 para protegerse del ataque. La compañía publicó varios parches de seguridad, para las versiones de Windows que ya no eran soportadas, incluyendo Windows XP, Windows 8 y Servidor de Windows 2003.

El 16 de mayo de 2017, los investigadores del University College de Londres informaron que su sistema, nombrado *PayBreak*, era capaz de derrotar a WannaCry y a otras familias de ransomware.

 Reacciones
Varios expertos destacaron la decisión de la NSA de no revelar la vulnerabilidad, y su pérdida de control sobre la herramienta EternalBlue, usada en el ataque. Edward Snowden dijo que si la NSA hubiera "revelado privadamente" el defecto utilizado para atacar hospitales cuando fue encontrado, y no cuando fue filtrado, [el ataque] podría no haber ocurrido". El experto británico en ciberseguridad Graham Cluley también encuentra "algo de culpabilidad de parte de los servicios de inteligencia de los EE. UU.". Según él y otros "(las agencias) podrían haber hecho algo hace mucho tiempo para arreglar este problema, y no lo hicieron". También dijo que a pesar de los usos obvios de tales herramientas para espiar personas de interés, las agencias tienen el deber de proteger a los ciudadanos de su país. El presidente ruso Vladímir Putin colocó la responsabilidad del ataque sobre los servicios de inteligencia de los EE. UU., por haber creado EternalBlue.

Otros comentaron que este ataque muestra cómo la práctica de las agencias de inteligencia de acumular exploits para propósitos ofensivos en vez de revelarlas para propósitos defensivos, puede ser problemática. El presidente y principal asesor jurídico de Microsoft, Brad Smith, escribió "Repetidamente, los exploits en las manos de los gobiernos se han filtrado al dominio público y han causado daños extensos. Un escenario equivalente con armas convencionales sería que al ejército de EE.UU le robaran algunos de sus misiles Tomahawk."

Adam Segal, director del programa de políticas digitales y del ciberespacio en el consejo de relaciones exteriores de los Estados Unidos, declaró que "la aplicación de parches y actualizaciones a los sistemas tienen graves defectos, en el sector privado y en agencias de gobierno". Además, Segal dijo que la incapacidad aparente de los gobiernos para asegurar las vulnerabilidades informáticas "abre muchas preguntas acerca de las backdoors y el acceso a los métodos de cifrado que el gobierno dice necesitar del sector privado para su seguridad".

Algunos expertos utilizaron la visibilidad generada por el ataque como una posibilidad para reiterar el valor e importancia de realizar copias de seguridad con regularidad y mantener las mismas en un medio seguro, tener buena seguridad informática incluyendo el aislamiento de los sistemas críticos, utilizar software apropiado, y tener instalados los parches de seguridad más recientes.

En el Reino Unido el impacto en el NHS se politizó rápidamente, a partir de las declaraciones que aseguraban que los efectos fueron exacerbados por la financiación precaria del NHS por parte del Partido Conservador, en una situación facilitada por las medidas de austeridad del gobierno, en particular la negativa a pagar un cargo adicional para mantener protegidos los computadores que usaban el sistema desactualizado Windows XP de tales ataques. La secretaría del interior, Amber Rudd se rehusó a confirmar si los datos de los pacientes habían sido respaldados, y el secretario de salud del gabinete en la sombra Jon Ashworth acusó al secretario de salud Jeremy Hunt de negarse a actuar oportunamente ante una notificación crítica de Microsoft, el Centro Nacional de Ciberseguridad (NCSC) y la Agencia Nacional del Delito, que fue entregada dos meses antes del ataque.

Arne Schönbohm, presidente de la oficina Federal de Alemania para la Seguridad de la Información (BSI), declaró que "los ataques recientes muestran cuán vulnerable es nuestra sociedad digital. Es una llamada de alerta para que las compañías finalmente se tomen la seguridad informática [seriamente]".

 Lista de organizaciones afectadas

 Atribución
A pesar de que las compañías de ciberseguridad Kaspersky Lab y Symantec dijeron que el código tiene algunas semejanzas con aquel anteriormente utilizado por el Lazarus Group, (al cual se atribuye el ciberataque a Sony Pictures de 2014 y a un banco de Bangladés, habiendo sido este grupo vinculado con Corea del Norte), esto puede ser cualquier sencillo re-uso del código por otro grupo, o un intento atribuirles el ataque en una operación de bandera falsa. EE UU acusa al hacker norcoreano detrás del ciberataque ‘WannaCry’ y el de Sony.

 Véase también
 Ciberataques al Comité Nacional Demócrata
 Ciberataque a Sony Pictures de 2014
 Ciberapagón en Corea del Norte de 2014
 Ciberataque a Dyn de octubre de 2016
 Conficker
 SQL Slammer
 Vault 7
 RedEye

 Referencias
