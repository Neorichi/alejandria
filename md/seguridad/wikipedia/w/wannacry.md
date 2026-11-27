---
type: Artículo de enciclopedia
title: WannaCry
description: "WannaCry —también denominado WannaCrypt, WanaCrypt0r 2.0, Wanna Decryptor o WCry— es una familia de ransomware para Microsoft Windows con capacidad de propagación automática, por lo que suele describirse como un …"
resource: https://es.wikipedia.org/wiki/WannaCry
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/WannaCry"}
license: CC BY-SA 4.0
id: eswiki-WannaCry
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# WannaCry

- **Nombre:** WannaCry
- **Autor:** Desconocido; atribuido al Grupo Lazarus por los gobiernos de Estados Unidos y el Reino Unido
- **Descubrimiento:** 12 de mayo de 2017

**WannaCry** —también denominado **WannaCrypt**, **WanaCrypt0r 2.0**, **Wanna Decryptor** o **WCry**— es una familia de ransomware para Microsoft Windows con capacidad de propagación automática, por lo que suele describirse como un criptogusano. El nombre se emplea asimismo para designar el ciberataque mundial que comenzó el 12 de mayo de 2017. El programa cifraba numerosos tipos de archivos de los equipos comprometidos y exigía un rescate pagadero en Bitcoin para intentar recuperarlos.

La expansión masiva se produjo mediante vulnerabilidades del protocolo SMBv1 corregidas por Microsoft en el boletín de seguridad **MS17-010**. WannaCry incorporó el *exploit* **EternalBlue**, desarrollado originalmente por la Agencia de Seguridad Nacional de Estados Unidos (NSA) y publicado por el grupo The Shadow Brokers en abril de 2017. Esta combinación permitió que el malware se propagara por redes locales y a través de Internet sin que cada nueva víctima tuviera que abrir un archivo o enlace malicioso.

Las estimaciones publicadas durante y después del incidente difieren según la fecha y el método de medición, pero coinciden en que afectó a cientos de miles de sistemas en más de 150 países. Entre las organizaciones perjudicadas figuraron el Servicio Nacional de Salud británico (NHS), Telefónica, Renault, Nissan, Deutsche Bahn, FedEx y organismos públicos de varios países.

El investigador británico Marcus Hutchins, conocido entonces por el seudónimo *MalwareTech*, redujo de forma drástica la primera oleada al registrar un dominio incorporado en el código que actuaba como mecanismo de desactivación. El registro no reparó los equipos ya cifrados ni eliminó la necesidad de instalar parches, y posteriormente se localizaron variantes con otros dominios de desactivación.

La autoría material no ha sido establecida mediante una sentencia específica sobre el ataque. No obstante, varias empresas de seguridad identificaron vínculos técnicos con el Grupo Lazarus, asociado a Corea del Norte, y los gobiernos del Reino Unido y Estados Unidos atribuyeron públicamente la operación a actores norcoreanos. En septiembre de 2018, el Departamento de Justicia de los Estados Unidos acusó al programador norcoreano Park Jin Hyok de participar, entre otras actividades, en la creación y difusión de WannaCry 2.0.

 Denominación y clasificación

Las muestras y notas de rescate utilizaron distintas grafías, entre ellas *WannaCry*, *WannaCrypt*, *WanaCrypt0r*, *Wana Decrypt0r* y *WCry*. En la documentación técnica de Microsoft apareció con identificadores como *Ransom:Win32/WannaCrypt*, mientras que otros proveedores emplearon nombres propios para variantes o componentes concretos.

Se clasifica como *ransomware* porque impide el acceso a datos mediante cifrado y reclama un pago, y como gusano porque intenta comprometer automáticamente otros sistemas vulnerables. Esta segunda capacidad distinguió el brote de muchas campañas de ransomware contemporáneas, que dependían principalmente de archivos adjuntos, descargas o enlaces de phishing.

 Antecedentes

 Vulnerabilidades de SMB y MS17-010

El 14 de marzo de 2017, Microsoft publicó el boletín **MS17-010**, que corregía varias vulnerabilidades críticas en la implementación de SMBv1. Un atacante remoto podía enviar paquetes especialmente diseñados a un servidor SMB y ejecutar código en el sistema vulnerable. Las actualizaciones estaban disponibles para las versiones de Windows que se encontraban dentro del ciclo ordinario de soporte.

El 14 de abril de 2017, The Shadow Brokers difundió un conjunto de herramientas atribuidas a la NSA. Entre ellas figuraba EternalBlue, capaz de explotar vulnerabilidades cubiertas por MS17-010. El material filtrado también incluía herramientas relacionadas con la puerta trasera DoublePulsar, aunque los análisis no siempre coinciden en el papel que esta desempeñó en cada infección de WannaCry.

EternalBlue suele vincularse en la bibliografía a **CVE-2017-0144**. Algunas fichas de detección de Microsoft relativas a WannaCry también remiten a **CVE-2017-0145**, otra de las vulnerabilidades de SMBv1 comprendidas en MS17-010. Por ello, numerosos análisis describen de forma conjunta la explotación de las vulnerabilidades SMB corregidas por aquel boletín, en lugar de atribuir toda la cadena a un único identificador CVE.

 Variantes anteriores al brote mundial

Symantec documentó muestras semejantes a WannaCry empleadas en ataques limitados durante febrero, marzo y abril de 2017. Estas variantes tempranas no incorporaban todavía la propagación masiva mediante EternalBlue y, según su análisis, se apoyaban en credenciales comprometidas y otras herramientas para desplazarse dentro de las redes atacadas. También presentaban semejanzas de código y de infraestructura con programas asociados previamente al Grupo Lazarus.

 Funcionamiento

 Componentes y persistencia

Los análisis forenses describen una arquitectura compuesta por una parte de carga y propagación y otra dedicada al cifrado y a la interacción con la víctima. Entre los archivos observados se encontraban `mssecsvc.exe`, asociado al cargador y al gusano; `tasksche.exe`, otro cargador; y `@WanaDecryptor@.exe`, que mostraba la interfaz de rescate. La infección creaba el servicio `mssecsvc2.0`, podía añadir valores de ejecución automática al Registro de Windows y desplegaba archivos auxiliares con extensiones `.wnry`, junto con componentes de Tor.

El malware eliminaba o dificultaba el uso de determinados mecanismos locales de recuperación. Entre otras acciones observadas, ejecutaba comandos para borrar copias de instantáneas de volumen y modificar opciones de arranque, con el objetivo de reducir las posibilidades de restaurar los archivos sin pagar.

 Propagación

Al ejecutarse, el componente de gusano examinaba equipos accesibles por el puerto TCP 445 y trataba de explotar SMBv1 mediante EternalBlue. La propagación se producía tanto lateralmente dentro de la red local como hacia direcciones de Internet generadas por el programa. Los sistemas sin la actualización MS17-010 y con SMB expuesto eran especialmente vulnerables.

Durante las primeras horas se especuló con que una campaña de correos de phishing hubiera iniciado el brote. Sin embargo, los análisis posteriores no confirmaron una campaña de correo como mecanismo dominante de la expansión mundial. La propagación masiva sí está documentada mediante la explotación automática de SMB; el modo exacto en que se introdujo la primera muestra en la primera red comprometida no quedó establecido de manera concluyente.

Aunque los equipos con sistemas operativos sin soporte constituían un riesgo evidente, el incidente no se limitó a Windows XP. El informe posterior del National Audit Office británico señaló, por ejemplo, que muchos de los dispositivos infectados en el NHS utilizaban Windows 7 sin los parches correspondientes.

 Cifrado y petición de rescate

WannaCry buscaba numerosas extensiones de documentos, imágenes, bases de datos, archivos comprimidos y otros datos de usuario. Para cada archivo generaba una clave de AES-128 en modo CBC; esa clave se protegía posteriormente mediante criptografía RSA. Los archivos resultantes incorporaban una cabecera identificada por la cadena `WANACRY!` y, según la muestra, recibían extensiones como `.WNCRY` o `.WCRY`.

La nota de rescate estaba traducida a numerosos idiomas, incluido el español. Exigía generalmente el equivalente a 300 dólares en bitcoin y anunciaba que el importe se duplicaría después de tres días; también advertía de la supuesta pérdida definitiva de los archivos tras siete días. El programa cambiaba el fondo de escritorio, mostraba una cuenta atrás y proporcionaba instrucciones para adquirir y enviar la criptomoneda.

El malware incluía tres direcciones de Bitcoin codificadas directamente. Symantec atribuyó esta decisión a un error de concurrencia que impidió generar de forma fiable una cartera distinta para cada víctima. Al no existir una identificación automática clara entre cada pago y cada equipo, el proceso de entrega de claves resultaba difícil de administrar incluso para los atacantes.

 Dominios de desactivación

Antes de iniciar determinadas acciones, la variante responsable de la primera gran oleada comprobaba si podía contactar con un dominio largo y aparentemente aleatorio incluido en su código. Si la conexión tenía éxito, el proceso se detenía. Este comportamiento pudo concebirse como una forma de detectar entornos automatizados de análisis —algunos de los cuales responden positivamente a cualquier dominio—, aunque su propósito original no se conoce con certeza.

Marcus Hutchins registró el dominio y redirigió su tráfico a un servidor de observación o *sinkhole*. La medida provocó que una gran cantidad de nuevas ejecuciones se desactivaran y frenó de forma notable la propagación de aquella variante. No descifró archivos existentes, no eliminó infecciones ya instaladas y podía resultar ineficaz en redes que bloquearan la consulta o la respuesta del dominio. En días posteriores se encontraron muestras que utilizaban otros dominios, uno de los cuales fue registrado y hundido por investigadores de Check Point.

 Ataque mundial de mayo de 2017

 Cronología

El viernes 12 de mayo de 2017 comenzaron a notificarse infecciones simultáneas en organizaciones de numerosos países. La combinación de cifrado y propagación automática provocó que el incidente creciera con rapidez, especialmente en redes extensas que contenían equipos sin MS17-010 o en las que SMBv1 podía utilizarse lateralmente.

Durante la mañana europea, la red interna de Telefónica y distintos centros del NHS hicieron públicos problemas relacionados con ransomware. En las horas siguientes aparecieron incidentes en empresas de transporte, fabricación, telecomunicaciones, logística, energía y organismos públicos. El registro del dominio de desactivación a última hora del 12 de mayo redujo la velocidad de la primera oleada, aunque las labores de aislamiento, parcheo y restauración continuaron durante días.

Ese mismo fin de semana, Microsoft publicó orientaciones de emergencia y tomó la decisión excepcional de ofrecer actualizaciones para sistemas fuera de soporte general, entre ellos Windows XP, Windows 8 y Windows Server 2003. La empresa insistió en aplicar MS17-010, deshabilitar SMBv1 cuando fuera posible, aislar sistemas comprometidos y mantener actualizado el software antimalware.

 Alcance

Las cifras publicadas fueron aumentando a medida que se reunían datos. ENISA calculó el 15 de mayo aproximadamente 190 000 equipos afectados en más de 150 países, mientras que Europol y distintos medios difundieron estimaciones cercanas o superiores a 200 000. Otras autoridades y empresas contabilizaron más conexiones, direcciones vulnerables o detecciones y ofrecieron cifras mayores. La disparidad se debe, entre otros factores, a que unas mediciones contaban dispositivos cifrados, otras direcciones IP, intentos de infección o conexiones al dominio hundido.

El Departamento de Seguridad Nacional de España informó el 17 de mayo de más de 360 000 equipos afectados en 180 países, y situó a España en el decimoctavo puesto por número de infecciones confirmadas, con más de 1200. Estas cifras deben entenderse como una fotografía de aquel momento y no como un censo definitivo de víctimas.

 Impacto

 Servicio Nacional de Salud del Reino Unido

El NHS de Inglaterra fue uno de los casos más visibles. El National Audit Office concluyó que al menos 81 de los 236 *trusts* hospitalarios resultaron afectados directamente o desconectaron sistemas como medida de precaución. También se vieron afectados 603 organismos de atención primaria y otras entidades del NHS, entre ellos 595 consultorios de medicina general.

El ataque obligó a cancelar citas, desviar ambulancias, volver temporalmente a procedimientos en papel y posponer determinadas pruebas y tratamientos. El NAO identificó directamente 6912 citas canceladas y estimó que el total real pudo superar las 19 000. Las evaluaciones posteriores no encontraron indicios de robo o compromiso de datos de pacientes ni atribuyeron daños clínicos directos al incidente.

Una actualización gubernamental estimó en alrededor de 92 millones de libras el coste para el NHS, al combinar la pérdida de actividad durante el brote y las labores posteriores de restauración y mejora tecnológica. Aunque el uso de Windows XP recibió gran atención pública, el Gobierno británico calculó que aproximadamente el 4,7 % de los dispositivos del NHS utilizaban ese sistema cuando ocurrió el ataque, y el NAO señaló que la mayor parte de los equipos infectados identificados ejecutaban Windows 7 sin parchear.

 España
En España, el caso más conocido fue el de Telefónica. INCIBE-CERT recogió el 12 de mayo que el *ransomware* había afectado a su red interna y que la empresa pidió a parte de la plantilla apagar los ordenadores como medida preventiva. La repercusión pública convirtió a la operadora en una de las primeras referencias internacionales del brote.

Según el expediente abierto posteriormente por la Agencia Española de Protección de Datos (AEPD), la incidencia afectó a ordenadores personales de empleados y no a servidores que alojaran datos de clientes o de terceros. Telefónica comunicó que sus servicios continuaron funcionando con normalidad y que no se había comprometido la confidencialidad de datos personales. La empresa activó su plan de gestión de crisis y anunció medidas como la reducción de los ciclos de parcheo y la aceleración de inversiones en seguridad.

La respuesta española fue coordinada por organismos como CCN-CERT, INCIBE-CERT y el entonces Centro Nacional para la Protección de las Infraestructuras Críticas. El CCN-CERT difundió alertas, un informe de código dañino y la herramienta preventiva *#NoMoreCry*. Su cronología registró aún 2774 direcciones IP vulnerables el 16 de mayo y 239 direcciones que habían contactado con uno de los dominios maliciosos o de control observados.

Las primeras noticias también mencionaron medidas preventivas o incidencias en otras grandes empresas españolas. Sin embargo, varias afirmaciones iniciales fueron rectificadas, no llegaron a documentarse con el mismo detalle o confundían desconexiones preventivas con infecciones confirmadas. Por ello, las evaluaciones oficiales posteriores se centraron en el número agregado de infecciones y en los casos cuya afectación pudo acreditarse.

 Otros países y sectores

WannaCry afectó o provocó desconexiones preventivas en organizaciones de sanidad, transporte, telecomunicaciones, administración pública, industria, energía, educación y logística. La siguiente relación recoge ejemplos ampliamente documentados y no constituye una lista exhaustiva:

La Agencia de la Unión Europea para la Ciberseguridad destacó que el ataque alcanzó infraestructuras y servicios de salud, energía, transporte, finanzas, telecomunicaciones y fabricación. El incidente impulsó además la primera cooperación operativa a escala de la Unión Europea bajo los procedimientos comunes de respuesta cibernética desarrollados por ENISA y los Estados miembros.

 Pagos y pérdidas económicas

Las tres carteras codificadas en el malware podían observarse públicamente en la cadena de bloques, aunque no revelaban por sí mismas la identidad de quienes controlaban los fondos. Las cifras variaron con el precio del bitcoin y la fecha de cálculo. Symantec informó de que las carteras llegaron a acumular más de 140 000 dólares y que los fondos permanecieron inmóviles casi tres meses antes de ser retirados en agosto de 2017.

La cantidad recaudada fue pequeña frente a la escala del incidente. Las estimaciones del daño económico mundial oscilaron desde cientos de millones hasta varios miles de millones de dólares, según si se contabilizaban únicamente restauración técnica y pérdida de actividad o también consecuencias indirectas. Estas cifras no son directamente comparables y no existe un cálculo global único aceptado.

 Respuesta defensiva y recuperación

 Parches y contención

La medida preventiva principal era instalar MS17-010, publicado casi dos meses antes del brote. Tras el ataque, Microsoft distribuyó además actualizaciones extraordinarias para Windows XP, Windows 8 y Windows Server 2003, pese a que ya se encontraban fuera del soporte general. La compañía recomendó también deshabilitar SMBv1 cuando no fuera necesario, restringir el tráfico SMB en los perímetros de red, mantener soluciones antimalware actualizadas y aislar los equipos comprometidos.

El dominio registrado por Hutchins dio tiempo a organizaciones de regiones todavía poco afectadas para parchear y segmentar redes. Aun así, la protección dependía de que el equipo pudiera resolver y contactar el dominio. Bloquearlo sin haber eliminado la infección podía hacer que la muestra continuara con el cifrado, por lo que Microsoft y otros equipos de respuesta recomendaron no impedir esa comunicación durante la contención de las variantes conocidas.

 Coordinación institucional

Europol coordinó el intercambio de información policial y técnica entre países, mientras que equipos nacionales de respuesta a incidentes publicaron indicadores de compromiso, reglas de detección, herramientas preventivas y recomendaciones. ENISA consideró la reacción el primer caso en que se activaron a escala de la Unión Europea los mecanismos operativos comunes de cooperación cibernética.

En España, CCN-CERT e INCIBE-CERT difundieron alertas, parches, indicadores y procedimientos de desinfección. La herramienta *#NoMoreCry* del CCN-CERT estaba orientada a prevenir la ejecución de la muestra en equipos todavía no cifrados; no era un descifrador universal de archivos ya afectados.

 Posibilidades de descifrado

No se publicó una clave maestra capaz de recuperar de forma general todos los archivos cifrados por WannaCry. Europol y el proyecto *No More Ransom* advirtieron que la recuperación dependía principalmente de copias de seguridad o de circunstancias técnicas muy concretas.

Herramientas como *WannaKey* y *WanaKiwi* aprovecharon el hecho de que, en determinadas versiones de Windows, los números primos empleados para construir la clave RSA podían permanecer en memoria después de ser liberados. Su éxito requería que el equipo no se hubiera reiniciado y que la memoria no hubiera sido sobrescrita, entre otras condiciones; por ello no constituían una solución universal.

 Atribución

La atribución evolucionó con el tiempo. En mayo de 2017, investigadores de Kaspersky detectaron un fragmento de código compartido entre una variante temprana de WannaCry y una puerta trasera utilizada anteriormente por el Grupo Lazarus. Symantec encontró otras coincidencias en herramientas, infraestructura y métodos observados en los ataques previos de febrero a abril. Ambos análisis consideraron que los indicios merecían investigación, aunque una coincidencia de código aislada no demostraba por sí sola la autoría y era teóricamente posible una operación de bandera falsa.

El 19 de diciembre de 2017, el Gobierno británico declaró que el NCSC consideraba «altamente probable» que actores norcoreanos conocidos como Lazarus fueran responsables. Estados Unidos efectuó una atribución pública similar.

En septiembre de 2018, el Departamento de Justicia estadounidense acusó a Park Jin Hyok de participar en una conspiración que incluía el ataque a Sony Pictures Entertainment, el robo al Banco de Bangladés y el desarrollo de WannaCry 2.0. La acusación lo vinculó a una entidad que trabajaba para el Gobierno norcoreano. En febrero de 2021, una acusación sustitutiva añadió a otros dos programadores militares norcoreanos y amplió la descripción de las campañas atribuidas al grupo.

Estas acusaciones y atribuciones oficiales no equivalen por sí solas a una condena judicial específica que haya determinado de forma definitiva quién escribió cada componente del malware. Por ello, las fuentes enciclopédicas suelen presentar la vinculación con Corea del Norte como una atribución de gobiernos y analistas, no como una autoría individual incontrovertida.

 Reacciones y controversias

El ataque reavivó el debate sobre la retención secreta de vulnerabilidades por parte de los servicios de inteligencia. Críticos como Edward Snowden sostuvieron que la NSA debería haber comunicado antes la vulnerabilidad a Microsoft. El presidente ruso Vladímir Putin responsabilizó políticamente a los servicios estadounidenses por haber desarrollado la herramienta que posteriormente fue filtrada, aunque no atribuyó por ello la ejecución de WannaCry a Estados Unidos.

Brad Smith, presidente y principal asesor jurídico de Microsoft, argumentó que la pérdida de herramientas ofensivas por parte de los gobiernos podía causar daños comparables a la sustracción de armamento convencional. Reclamó un marco internacional para que los Estados informaran de vulnerabilidades a los proveedores y protegieran mejor sus arsenales cibernéticos.

El incidente también puso de relieve problemas ordinarios de gestión: inventarios incompletos, dependencia de sistemas heredados, segmentación insuficiente, exposición innecesaria de SMB y lentitud en la instalación de parches. Los informes sobre el NHS concluyeron que el ataque era evitable con prácticas de seguridad básicas ya recomendadas y que ninguna organización sanitaria británica había aplicado íntegramente todas las medidas exigidas por su evaluación de preparación.

En el Reino Unido, el impacto se incorporó al debate político sobre la financiación y modernización del NHS. Las investigaciones posteriores, no obstante, distinguieron entre la existencia de equipos antiguos y el problema más amplio de no aplicar a tiempo actualizaciones disponibles a sistemas todavía soportados.

 Incidentes posteriores y legado

WannaCry continuó siendo detectado después de la oleada de mayo porque numerosos equipos siguieron expuestos a SMBv1 o conservaron copias del gusano. Los dominios hundidos recibieron durante años conexiones procedentes de sistemas que intentaban ejecutar variantes antiguas, lo que permitió observar la persistencia de máquinas sin limpiar o vulnerables.

En agosto de 2018, Taiwan Semiconductor Manufacturing Company (TSMC) interrumpió temporalmente parte de la producción en varias fábricas después de que un equipo infectado introdujera una variante de WannaCry durante la instalación de software en una nueva herramienta. La empresa declaró que el incidente se debió a un error operativo, no a un ataque dirigido, y que no comprometió la confidencialidad ni la integridad de sus datos. El episodio mostró que el malware seguía teniendo capacidad disruptiva más de un año después del brote mundial.

El brote se convirtió en un caso de estudio sobre ransomware autopropagable, seguridad de infraestructuras críticas y gestión de vulnerabilidades. Entre sus consecuencias duraderas se cuentan la publicación excepcional de parches para productos fuera de soporte, la revisión de planes de continuidad en sanidad e industria, una mayor presión para deshabilitar SMBv1 y el impulso del debate internacional sobre el acaparamiento gubernamental de vulnerabilidades.

 Véase también
 EternalBlue
 Grupo Lazarus
 DoublePulsar
 NotPetya
 Conficker
 SQL Slammer
 Ciberataque a Sony Pictures de 2014
 Ransomware
 Seguridad informática

 Referencias

 Enlaces externos
 Orientación de Microsoft sobre WannaCrypt
 Información de Europol sobre WannaCry
 Información de INCIBE-CERT
 CCN-CERT
