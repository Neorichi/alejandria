---
type: Artículo de enciclopedia
title: Antivirus
description: Los antivirus son programas cuyo objetivo es detectar y eliminar virus informáticos.
resource: https://es.wikipedia.org/wiki/Antivirus
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Antivirus"}
license: CC BY-SA 4.0
id: eswiki-Antivirus
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Antivirus

Los **antivirus** son programas cuyo objetivo es detectar y eliminar virus informáticos. Con el paso del tiempo, los antivirus han evolucionado hacia programas más avanzados que además de buscar y detectar virus informáticos consiguen bloquearlos, desinfectar archivos y prevenir una infección de estos. Actualmente son capaces de reconocer otros tipos de *malware*, como *spyware*, gusanos, troyanos, *rootkits* y pseudovirus.

 Historia

Uno de los primeros antivirus que se tiene documentado fue El realizado de manera exprofeso por Omri y Rakvi (Universidad Hebrea de Jerusalén) para combatir al virus Jerusalén en 1987. Luego agregaron detección para otras amenazas informáticas y fundaron la compañía BRM. El *software* fue vendido a Symantec (ahora llamada NortonLifeLock); en los años siguientes Check Point invirtió una gran cantidad de dinero para desarrollar más opciones de *software* contra virus.

 Funcionamiento
Los antivirus utilizan distintos tipos de mecanismos para detectar virus. Como demostró Frederick Cohen ningún método es totalmente efectivo para identificar un virus. Los tipos de mecanismos más usados por los antivirus para detectar virus son:
 Basados en **Firma de virus**: El antivirus dispone de una base de datos en las que almacena firmas de virus. En el pasado estas firmas eran hashes con los que se intentaba ajustar todos los ficheros del equipo analizado. Esta medida es fácil de eludir cambiando cualquier instrucción del código y el hash resultante no coincidiría con ninguna firma de la base de datos. No tardó en sofisticarse esa técnica y se empezó a intentar buscar una secuencia de bytes concreta en cada muestra de *malware* que lo identificara, así de esta manera, tendrías que saber que parte del código es con la que han identificado tu binario para modificarla y no ser detectable. Es habitual el uso de reglas para declarar patrones específicos para detectar un *malware* concreto. Para luchar contra estas firmas en los *malware* se emplearon codificadores que modificaban todo el código del binario. Ejemplos de codificadores son el básico XOR o el “Shikata ga nai” de Metasploit que añadía una capa de polimorfismo, generando una cadena de bits diferente cada vez que se produce la codificación. También surgieron los packers que encapsulaban el código dentro del binario y lo cifraban, de tal manera que las firmas no eran capaces de ser útiles. La debilidad de estos sistemas es que en el código hay que añadir las instrucciones necesarias para el desempaquetado del código y eso puede generar firmas que identifiquen un binario como potencialmente malicioso.
 Basados en **Detección heurística**: Consiste en el escaneo de los archivos buscando patrones de código que se asemejan a los que se usan en los virus. Ya no es necesaria una coincidencia exacta con una firma de virus almacenada sino que se buscan similitudes más generales aplicando algoritmos.
 Basados en **Detección por comportamiento**: consiste en escanear el sistema tras detectar un fallo o mal funcionamiento. Por lo general, mediante este mecanismo se pueden detectar *software* ya identificado o no, pero es una medida que se usa tras la infección.
 Basados en la **Detección por caja de arena (o sandbox)**: consiste en ejecutar el *software* en máquinas virtuales y determinar si el *software* ejecuta instrucciones maliciosas o no. A pesar de que este mecanismo es seguro, toma bastante tiempo ejecutar las pruebas antes de ejecutar el *software* en la máquina real.
 Basados en la **Detección por inteligencia artificial**: consiste en el uso de tecnologías de inteligencia artificial para detectar comportamiento malicioso. Ejemplos de antivirus que usan estas tecnologías son MIT AI2 (desarrollado por el MIT y IBM Watson for Cyber Security (desarrollado por IBM).
 Basado en **Indicadores de compromiso** (IDC): Una vez los IDC han sido identificados pueden ser utilizados para la detección temprana de intentos de ataque que utilizan sistemas antivirus.

Los antivirus tradicionalmente se ejecutan en el sistema analizado y utiliza la red para actualizar su *software* y datos. Los **antivirus en la nube** lo que hacen es delegar la mayor parte del procesamiento del antivirus en la nube. Hay que establecer decisión de que procesamientos son lo suficientemente importantes como para incluirlas en el cliente local sin saturar y cuáles deberían permanecer en un servidor en la nube. Las principales ventajas que se tienen son: acceso más rápido a actualizaciones de *software* y datos (no depender de actualización manual o de las actualizaciones automáticas programadas), el cliente del antivirus en el equipo a analizar es mucho más pequeño y requiere poco procesamiento dejando recursos para nuestro uso, facilidad de uso e instalación. Las principales desventajas son: dependencia con respecto a la conexión, posibles problemas de privacidad al enviar datos a la nube y posible foco de infección secundaria al subir datos a la nube.

El antivirus de puerta de enlace se puede utilizar para proteger contra una variedad de ataques, incluidos los ataques de kits de exploits. Además, la prevención de intrusiones y el antispyware también se utilizan para evitar ataques de kits de exploits. También existen formas para que los suscriptores reciban estos sistemas de prevención de forma continua, lo que les ayuda a defenderse mejor de los ataques.

 Planificación
La planificación consiste en tener preparado un plan de contingencia en caso de que una emergencia de virus se produzca, así como disponer al personal de la formación adecuada para reducir al máximo las acciones que puedan presentar cualquier tipo de riesgo. Cada antivirus puede planear la defensa de una manera, es decir, un antivirus puede hacer un escaneado completo, rápido o de vulnerabilidad según elija el usuario.

 Consideraciones de software
El *software* es otro de los elementos clave en la parte de planificación. Se debería tener en cuenta la siguiente lista de comprobaciones para tu seguridad:

 Tener el *software* indispensable para el funcionamiento de la actividad, nunca menos pero tampoco más. Tener controlado al personal en cuanto a la instalación de *software* es una medida que va implícita. Asimismo, tener controlado el *software* asegura la calidad de la procedencia de este (no debería permitirse *software* pirata o sin garantías). En todo caso un inventario de *software* proporciona un método correcto de asegurar la reinstalación en caso de desastre.
 Disponer del *software* de seguridad adecuado. Cada actividad, forma de trabajo y métodos de conexión a Internet requieren una medida diferente de aproximación al problema. En general, las soluciones domésticas, donde únicamente hay un equipo expuesto, no son las mismas que las soluciones empresariales.
 Métodos de instalación rápidos. Para permitir la reinstalación rápida en caso de contingencia.
 Asegurar licencias. Determinados *'softwares* imponen métodos de instalación de una vez, que dificultan la reinstalación rápida de la red. Dichos programas no siempre tienen alternativas, pero ha de buscarse con el fabricante métodos rápidos de instalación.
 Buscar alternativas más seguras. Existe *'oftware* que es famoso por la cantidad de agujeros de seguridad que introduce. Es imprescindible conocer si se puede encontrar una alternativa que proporcione iguales funcionalidades, pero permitiendo una seguridad extra.

 Consideraciones de la red
Disponer de una visión clara del funcionamiento de la red permite poner puntos de verificación de filtrado y detección ahí donde la incidencia es más claramente identificable. Sin perder de vista otros puntos de acción es conveniente:

 Mantener al máximo el número de recursos de red en modo de solo lectura. De esta forma se impide que computadoras infectadas los propaguen.
 Centralizar los datos. De forma que detectores de virus en modo *batch* puedan trabajar durante la noche.
 Realizar filtrados de *firewall* de red. Eliminar los programas que comparten datos, como pueden ser los P2P; Mantener esta política de forma rigurosa, y con el consentimiento de la gerencia.
 Reducir los permisos de los usuarios al mínimo, de modo que solo permitan el trabajo diario.
 Controlar y monitorizar el acceso a Internet. Para poder detectar en fases de recuperación cómo se ha introducido el virus, y así determinar los pasos a seguir.

 Formación del usuario
Esta es la primera barrera de protección de la red.

 Antivirus
Es conveniente disponer de una licencia activa de antivirus. Dicha licencia se empleará para la generación de discos de recuperación y emergencia. Sin embargo, no se recomienda en una red el uso continuo de antivirus.

El motivo radica en la cantidad de recursos que dichos programas obtienen del sistema, reduciendo el valor de las inversiones en *hardware* realizadas. Aunque si los recursos son suficientes, este extra de seguridad puede ser muy útil.

Sin embargo, los filtros de correos con detectores de virus son imprescindibles, ya que de esta forma se asegurará una reducción importante de elecciones de usuarios no entrenados que pueden poner en riesgo la red.

 *Firewalls*

Filtrar contenidos y puntos de acceso. Eliminar programas que no estén relacionados con la actividad. Tener monitorizado los accesos de los usuarios a la red, permite asimismo reducir la instalación de **'software**' que no es necesario o que puede generar riesgo para la continuidad del negocio. Su significado es barrera de fuego y no permite que otra persona no autorizada tenga acceso desde otro equipo al tuyo.

 Reemplazo de *software*
Los puntos de entrada en la red la mayoría de las veces son el correo, las páginas web, y la entrada de ficheros desde discos, o de computadoras ajenas a la empresa.

Muchas de estas computadoras emplean programas que pueden ser reemplazados por alternativas más seguras.

Es conveniente llevar un seguimiento de cómo distribuyen bancos, y externos el *software*, valorar su utilidad.

 Centralización y *backup*
La centralización de recursos y garantizar el *backup* de los datos es otra de las pautas
fundamentales en la política de seguridad recomendada.

La generación de inventarios de **'software**', centralización de este y la capacidad de generar instalaciones rápidas proporcionan métodos adicionales de seguridad.

Es importante tener localizado dónde se sitúa la información en la empresa. De esta forma podemos realizar las copias de seguridad de forma adecuada.

Control o separación de la informática móvil, dado que esta está más expuesta a las contingencias de virus.

 Empleo de sistemas operativos más seguros
Para servir ficheros no es conveniente disponer de los mismos sistemas operativos que se emplean dentro de las estaciones de trabajo, ya que toda la red en este caso está expuesta a los mismos retos. Una forma de prevenir problemas es disponer de sistemas operativos con arquitecturas diferentes, que permitan garantizar la continuidad de negocio.

 Temas acerca de la seguridad
Existen ideas instaladas por parte de las empresas de antivirus parte en la cultura popular que no ayudan a mantener la seguridad de los sistemas de información.

 **Mi sistema no es importante para un cracker**. Este tema se basa en la idea de que no introducir contraseñas seguras en una empresa no entraña riesgos pues «¿Quién va a querer obtener información mía?» Sin embargo, dado que los métodos de contagio se realizan por medio de programas automáticos, desde unas máquinas a otras, estos no distinguen buenos de malos, interesantes de no interesantes. Por tanto, abrir sistemas y dejarlos sin claves es facilitar la vida a los virus.

 **Estoy protegido pues no abro archivos que no conozco**. Esto es falso, pues existen múltiples formas de contagio, además los programas realizan acciones sin la supervisión del usuario poniendo en riesgo los sistemas.

 **Como tengo antivirus estoy protegido**. Únicamente estoy protegido mientras el antivirus sepa a lo que se enfrenta y como combatirlo. En general los programas antivirus no son capaces de detectar todas las posibles formas de contagio existentes, ni las nuevas que pudieran aparecer conforme las computadoras aumenten las capacidades de comunicación.

 **Como dispongo de un *firewall* no me contagio**. Esto únicamente proporciona una limitada capacidad de respuesta. Las formas de infectarse en una red son múltiples. Unas provienen directamente de accesos a mi sistema (de lo que protege un *firewall*) y otras de conexiones que realizó (de las que no me protege). Emplear usuarios con altos privilegios para realizar conexiones tampoco ayuda.

 Véase también

 Heurística en antivirus
 Antispyware
 Aislamiento de procesos (informática)
 CARO
 EICAR
 SMADAV
 Privacidad

 Referencias
