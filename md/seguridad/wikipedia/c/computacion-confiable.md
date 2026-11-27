---
type: Artículo de enciclopedia
title: Computación confiable
description: La computación confiable, también conocida por las siglas TC (del inglés trusted computing) es un conjunto de tecnologías propuestas por el Trusted Computing Group (TCG) que deben cumplir el hardware de los sistemas.
resource: https://es.wikipedia.org/wiki/Computación_confiable
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Computación_confiable"}
license: CC BY-SA 4.0
id: eswiki-Computación_confiable
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Computación confiable

La **computación confiable**, también conocida por las siglas **TC** (del inglés *trusted computing*) es un conjunto de tecnologías propuestas por el Trusted Computing Group (TCG) que deben cumplir el *hardware* de los sistemas. Su objetivo es proteger computadoras de programas de ataques que no pueden ser protegidos por soluciones puramente *software*. Ejemplos de computadores donde se aplican estas tecnologías: computadoras personales, computadoras que alojan servidores, sistemas embebidos y dispositivos móviles.

La Computación Confiable es controvertida dado que la maquinaria no está solamente asegurada para su propietario, sino también asegurada *contra su propietario*.  Tal controversia ha conducido a oponentes de la computación confiable, como el activista del software libre Richard Stallman, a referirse a ella como *computación traicionera*, incluso hasta el punto de que algunos artículos académicos han comenzado a poner comillas de sospecha alrededor de "computación confiable".

 Motivación y objetivos
Para proteger los sistemas de computadoras y redes de ataques normalmente se confía en distintos tipos de herramientas *software* (p. ej. librerías de firma digital o módulos del kernel)  o *firmware* (p. ej. cortafuegos). Sin embargo, el *software* puede ser manipulado local o remotamente (conexiones por red) por:
Usuarios privilegiados.
Usuarios no privilegiados que explotan vulnerabilidades o configuraciones inseguras.

Por tanto es casi imposible proteger un sistema de ataques al *software* si solo se confía en defensas *software*. Para progresar en tener plataforma seguras el Trusted Computing Group ha desarrollado un conjunto de especificaciones que el *hardware* debería cumplir. Las plataformas hardware que cumplen este conjunto de especificaciones las llaman Plataformas confiables porque tienen como objetivo aportar un entorno seguro para la ejecución de *software* dando lugar a lo que llaman computación confiable.

 Descripción
El TCG define tres características fundamentales que debe cumplir una plataforma confiable:
Medición de la integridad, registro e informe. Una plataforma confiable tiene que poder medir su propia integridad , almacenar localmente las medidas (necesario almacenamiento seguro en espacios de memoria blindados) y poder informar de estos valores a entidades remotas (atestar la medidas recogidas). En este contexto se entiende como medir la integridad al proceso de obtener la configuración de ciertos elementos del sistema que pueden afectar a su confiabilidad, tanto firmware como software (BIOS, ROM opcionales, cargadores, configuraciones, núcleos de sistema operativo, librerías y aplicaciones), y realizar un resumen criptográfico del mismo que sirva como medida. Normalmente también se suele tener un paso intermedio de registro de metadatos a un registro de mediciones almacenadas las cuales no residen en espacios de memoria blindados. Estos registros pueden usarse para otras operaciones pero hay que tener en cuenta que pueden ser fácilmente comprometidos pues no están almacenados es espacios de memoria blindados.
Capacidades protegidas. Son un conjunto de comandos especiales que tienen  permisos exclusivos para acceder a espacios de memoria blindados (espacio de memoria donde es seguro almacenar y operar con datos sensibles). Son vitales para la confianza del sistema. Son desarrollada mediante una mezcla adecuada de *hardware* y *firmware*.
Atestación. Es el proceso de garantizar la exactitud de la información de estado de un componente. Por ejemplo si se tiene una plataforma tienen que asegurar a otra que está en cierto estado (incluyendo *software* y hardware). Para ello se tiene que proporcionar dos tipos de información:
Una medida del estado actual.
Una prueba que garantiza que la medida es correcta y refleja realmente el estado de la plataforma
Será el verificador el que decidirá si la medida y la prueba son suficientes. Con base en esta información la entidad remota puede tomar la decisión de confiar en la plataforma y darle alguna autorización. Por ejemplo se podría establecer un protocolo en la que entidad remota verifica toda la pila del *software* desde el *firmware*, sistema operativo y aplicaciones. La decisión de en qué aplicaciones y plataformas confiar es una decisión de política de seguridad. la atestación da a la entidades de computación la habilidad de aceptar conexiones solo de aquellos que cumplan su política. Por ejemplo una VPN corporativa puede desear aceptar conexiones solo de clientes que ejecutan un sistema operativo verificado a nivel de parches y ejecutan un programa de cortafuegos con un conjunto de reglas de configuración suficientemente estricto. La atestación provee el mecanismo para forzar esta clase de políticas.

En  computadoras personales es habitual introducir un chip TPM y una especie de pre-BIOS para sustentar características de computación confiable

 Cadena de confianza
Para hacer atestaciones es necesario medir la integridad de la plataforma. Las plataformas normalmente consisten en muchos componentes separados interactuando (controladores, sistema operativo, aplicaciones, etc.). Estos componentes tienen que ser medidos individualmente y sus medidas tienen que ser almacenadas. Es necesario establecer que la integridad de un componente tiene que ser medida antes de que el componente sea ejecutado y se le pase el control. Por ejemplo, si se tiene un proceso de arranque de una computadora personal:
 El objetivo es obtener una medida de la integridad del sistema operativo de la plataforma. Se podría escribir una aplicación que tomara la medida del sistema operativo y la guardar de forma segura. El problema es que la aplicación usaría funciones que confiarían en el sistema operativo subyacente que está midiendo. Un ataque potencial podría ser modificar aquellas funciones del sistema operativo que son usadas por la aplicación para que tome las medidas de forma equívoca. La forma de tomar las medidas puede estar comprometida. De esta forma el sistema operativo tiene que ser medido antes de que el control sea pasado al mismo. Por tanto debe ser tomadas en el cargador de arranque. Por análogas razones el cargador de arranque tiene que ser medido por la BIOS. La BIOS debería también debería ser medida, sin embargo en las plataformas tradicionales la BIOS es el primer componente que es ejecutada. Por eso en las plataformas confiables es necesario tener un componente al que se llama CRTM (del inglés *core root of trust for measurement*) que es el responsable de medir la integridad de la BIOS. Este CRTM consiste en una serie de instrucciones para la CPU que normalmente están almacenados en un chip de la placa base. Cuando arranca la plataforma, estas instrucciones son ejecutadas por la CPU, causando que la BIOS sea medida. Después de ello se continúa con la ejecución de la BIOS.

De esta forma se dice que se ha establecido una cadena de confianza donde el CRTM es la raíz de las medidas. Se confía de forma ciega en las instrucciones del CRTM que están puesto en un chip insertado en la placa base por el fabricante.

El TCG define tres clases de raíces de confianza o RoT (del inglés *root of trust*). Son inherentemente seguras y todas las entidades involucradas tienen que confiar en ellas. Además, su comportamiento erróneo no puede ser detectado. Estos son:
Raíz de confianza para mediciones o RTM (del inglés *root of trust for measurement*). Es un motor de computación que se encarga de realizar las mediciones de integridad de los dispositivos que forman la plataforma.
Normalmente se trata del propio motor de cómputo de la plataforma, controlado por el núcleo del RTM o CRTM que es el primer conjunto de instrucciones ejecutado se establece una nueva cadena de confianza. Cuando el sistema es reseteado, la CPU empieza ejecutando el CRTM.
Otras veces es realizado directamente por el propio hardware usando un procesador de última generación.
Raíz de confianza para el almacenamiento o RTS (del inglés *root of trust for storage*). Es el que alberga de forma segura las medidas de integridad y protege los datos y claves criptográficas usadas por la plataforma confiable y almacenados  en almacenamientos externos. El RTS también puede proteger de forma robusta y segura claves y datos. Por ejemplo suele ser usado para almacenar claves, passwords y certificados digitales
Raíz de confianza para informes o RTP (del inglés *root of trust for reporting*). Es el que informa de forma fiable a otras entidades de las mediciones almacenadas en el RTS.

 Críticas
 Gestión de derechos digitales
Se proporciona un entorno perfecto para evitar los denominados como usos no autorizados de material con *copyright*, especialmente, aunque no limitado a, películas de vídeo y música.

Esto se debe a que el sistema puede realizar un control de las actividades del usuario y puede restringir la posibilidad de que haga algo que no le hayan permitido explícitamente las compañías. Por ejemplo, para evitar que se haga una copia de un vídeo de alta resolución que la compañía vendedora haya prohibido en la gestión de derechos digitales, el sistema impedirá que se reproduzca con esa calidad, o incluso por completo (según lo especificado por el vendedor del contenido) si, por ejemplo, existiera una salida no certificada y controlada por dicho sistema.

Como se puede imaginar, esto desata la discusión de ¿a quién obedece —debe obedecer— la computadora?. Evidentemente, un usuario normal no desea comprar un equipo que va a hacer las funciones de policía hacia él, vigilando todas sus acciones, y penalizando además el rendimiento y el coste del sistema.

 Restricciones para uso software libre
Algunas versiones de la computación confiable requerirán que el sistema operativo esté específicamente autorizado por una compañía particular. Los sistemas operativos libres no podrán ser instalados. Además, requerirán que cada programa sea específicamente autorizado por el desarrollador del sistema operativo. No podrá ejecutar aplicaciones libres en tales sistemas.

Otro asunto es que, según las leyes de cada país, si usted averigua cómo deshacerse de las restricciones y usar el sistema a su antojo y se lo comunica a alguien, eso podría constituir un delito. Frente a ello, fundaciones como la Electronic Frontier Foundation y la Free Software Foundation han levantado la voz y se oponen de múltiples formas a la restricción de derechos de los usuarios.

 Véase también
 Gestión de derechos digitales
 Windows Vista

 Enlaces externos
 Sitio web oficial del grupo de computación confiable (en inglés)
 Análisis de costes del sistema de protección de contenidos de Windows Vista (en inglés)
 Discusión acerca de a quién debe obedecer el ordenador
 Sitio web de la Electronic Frontier Foundation acerca de la computación confiable (en inglés)
 Pequeña animación respecto a la computación confiable (en inglés)
 Sitio web contra la Trusted Computing Platform Alliance (en inglés)
