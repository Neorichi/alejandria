---
type: Artículo de enciclopedia
title: Agujero de seguridad
description: Un agujero de seguridad o vulnerabilidad es un fallo en un sistema de información que se puede explotar para violar la seguridad del sistema.
resource: https://es.wikipedia.org/wiki/Agujero_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Agujero_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Agujero_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Agujero de seguridad

Un **agujero de seguridad** o **vulnerabilidad** es un fallo en un sistema de información que se puede explotar para violar la seguridad del sistema.

Los académicos definen una vulnerabilidad como una debilidad en el sistema que es aprovechada por una amenaza, que representa un factor potencial que podría conducir a un evento que cause daño a un sistema. Las amenazas pueden incluir pérdida de datos, autenticación débil, tecnología compartida, errores humanos y violaciones de datos.

 Tipos
Ejemplos de tipos de vulnerabilidades según la naturaleza del mismo:
 De software. Ejemplos:
 Inyección SQL
 Desbordamiento de búfer
 Clickjacking
 Condiciones de carrera
 Cross-site request forgery
 Cross-site scripting
 De hardware
 Del entorno físico del sistema
 Del personal involucrado
 De procedimientos de administración, organización y seguridad involucrados
 De la red de comunicaciones utilizada

 Prevención
La mejor política contra los agujeros de seguridad, reducir su número y facilitar su localización, es prevenirlos en el proceso de desarrollo. Para ello se ha creado el ciclo de vida de desarrollo seguro de software (S-SDLC) el cual incorpora la seguridad dentro del ciclo de vida de desarrollo del software. Cada fase el ciclo de vida tiene en cuenta la seguridad conseguir maximizar la seguridad.

Ejemplos de buenas prácticas para conseguir un software con menos vulnerabilidades:
 Mantener las herramientas de desarrollo actualizadas
 Usar buenas prácticas de codificación
 Establecer requisitos de seguridad
 Eliminar del software los módulos y archivos que no se utilicen.
 Registrar todos los eventos en un log.
 Evitar mostrar mensajes de error tal cual los genera el sistema
 Usar autorizaciones además de autenticar.
 Separar los datos de las instrucciones de control
 Validar todos los datos explícitamente.
 Identificar datos sensibles y como se les debería gestionar
 Usar procedimientos de actualización seguros
 La  configuración por defecto debe ser una configuración segura
 Uso de herramientas de prueba especialmente diseñadas para la detección de vulnerabilidades. Por ejemplo:
 Fuzzers. Se basan en inyectar entradas con datos aleatorios y verificar el comportamiento
 Herramientas de prueba de seguridad de aplicaciones (AST, del inglés *Application Security Testing*. Son herramientas que prueban la seguridad de las aplicaciones. Dependiendo de su funcionamiento se pueden clasificar en:
 Basadas en el análisis del código (SAST, del inglés *Static Application Security Testing*)
 Basada en el análisis en la salida obtenida al ejecutar con ciertas entradas (DAST, del inglés *Dynamic Application Security Testing*)
 Herramientas de análisis en tiempo real de la ejecución (RAST, del inglés *Run-time Application Security Testing*). Están inmersas en el entorno de ejecución y analizan como se realiza la ejecución.
 Herramientas de análisis interactivo (IAST, del inglés *Interactive Application Security Testing*). Combinan la observación interna y externa de una aplicación en ejecución. Se suelen implementar como un agente dentro del entorno de ejecución de prueba. Pueden probar si vulnerabilidades conocidas en el código son realmente explotables en ejecución.
 Herramientas híbridas que combinan varias de las estrategias antes mencionadas.

 Hitos o etapas
En el tiempo de vida de una vulnerabilidad podemos distinguir los siguientes hitos o etapas importantes:
 **Nacimiento**. Durante el proceso de desarrollo del **producto** por parte del **proveedor** (por ejemplo, el vendedor o una comunidad de desarrolladores de software) se introducen una serie de **defectos**. Estos defectos pueden ser de diseño, implementación o de gestión. Algunos de esos defectos pueden convertirse en riesgos para la seguridad del producto y por tanto para la seguridad del **usuario** del producto. Un defecto se convierte en una **vulnerabilidad** si hace que el comportamiento del sistema sea tal que pueda ser aprovechado para conseguir acceso no autorizado, elevación de privilegios, denegación de servicio o cualquier otra forma de romper la seguridad del sistema. No se consideran vulnerabilidades que son detectadas y corregidas antes del despliegue.
 **Descubrimiento**. Este hito ocurre cuando se tiene conocimiento de la existencia de la vulnerabilidad. Si la vulnerabilidad es creada intencionadamente entonces el nacimiento y el descubrimiento ocurren simultáneamente. Se llama **descubridor** a la primera persona que revela un defecto y determina que ese defecto es una vulnerabilidad. Si el descubridor no es conocido se dice que es anónimo.
 **Comunicación de la vulnerabilidad**. Este hito ocurre una vez que el descubridor revela la vulnerabilidad a alguien más. Esta transferencia de información puede ser de distintos tipos. Ejemplos: completa y pública vía (revelación completa) o comunicación privada entre hackers. Se llama **originador** (en inglés *originator*) o **revelador** (en inglés *discloser*) a la persona u organización que informa de la vulnerabilidad al proveedor del producto. Observar que el descubridor y el originador pueden ser personas distintas.
 **Corrección**. Ocurre cuando el vendedor del producto analiza la vulnerabilidad, localiza cual es el problema, y lanza una versión al público que resuelve la vulnerabilidad.
 **Publicación**. Es cuando el conocimiento de la vulnerabilidad se extiende a una audiencia importante dándole publicidad.
 **Automatización de explotación**. Es cuando a partir de la vulnerabilidad se crea una herramienta o script que automatiza la explotación de la vulnerabilidad. A esta herramienta o script se le llama **exploit**. De esta forma se permite que no sólo expertos sobre el tema (hackers) puedan vulnerar la seguridad. De esta forma se tiene una herramienta que permite a otros usuarios inexpertos (script kiddies) vulnerarla.
 **Muerte**. Ocurre cuando el número de sistemas vulnerables al exploit es insignificante. Esto puede haber sucedido porque el sistema ha sido retirado, el sistema ha sido arreglado mediante algún parche, o porque los hackers no tienen interés en explotarla.

Estos eventos no necesariamente ocurren estrictamente en este orden. Por ejemplo:
 La publicación y la corrección puede suceder al mismo tiempo, particularmente en casos donde el descubridor de la vulnerabilidad es el propio vendedor del producto, el cual usa el arreglo de la vulnerabilidad como parte de la propia publicidad del producto.
 La corrección de una vulnerabilidad no tiene por qué suceder antes de la automatización de la explotación. Si se construye un exploit antes de que la vulnerabilidad sea corregida por el proveedor, se dice que se trata de un **exploit de día cero** que da lugar a ataques de día cero.
 El descubrimiento se puede producir en el mismo momento del nacimiento, es decir, se trata de una vulnerabilidad intencionada. Se especula que algunos sistemas tienen desde el origen agujeros de seguridad intencionados conocidos por alguna de las partes que interviene en el diseño y/o desarrollo. Este tipo vulnerabilidades funcionaría a modo de puerta trasera o caballo de Troya. Ejemplos:
 En 2007, el gobierno de los Estados Unidos lanzó la un estándar para la generación de números aleatorios. Se proponían cuatro generadores de números pseudoaleatorios. Uno de ellos, el Dual EC DRBG, promovido por la NSA, tenía una puerta trasera que consistía en un conjunto de números secretos que permitían predecir la salida a partir de recopilar una pequeña porción de los resultados anteriores.
 Se ha hablado mucho de las supuestas presiones que recibió PGP Corporation para introducir una puerta trasera en su software. Esta supuesta puerta trasera permitiría a la ciertas organizaciones (por ejemplo, FBI, NSA ) poder descifrar el contenido cifrado con esta herramienta. Para camuflar esta supuesta puerta trasera se especula que se presionó a PGP Corporation para que hiciera el código de PGP (software de código abierto) tan enrevesado y extenso que no se pudiera detectar tal puerta trasera. Esto provocó que muchos usuarios se quedaran con las versiones antiguas, fácilmente verificables, y promovió la creación de software alternativo.
 Otro caso es la supuesta introducción de una puerta trasera en openBSD promocionada por el FBI.

 Búsqueda de vulnerabilidades y motivaciones para su publicación
La búsqueda de vulnerabilidades de seguridad es realizada principalmente por dos tipos de personas u organizaciones:
 Los atacantes de sistemas. Pueden aprovechar las vulnerabilidades para hacer vulnerables a los sistemas y conseguir de forma **ilegal** beneficios monetarios de ello, ya sea directamente (por ejemplo, permitiendo el uso de tarjetas de crédito ajenas) o indirectamente (por ejemplo, vendiendo información privada sobre las víctimas). Por su propia naturaleza este tipo de investigadores del vulnerabilidades no están interesados en la **revelación** de las vulnerabilidades descubiertas ya que así se aseguran de que la vulnerabilidad no sea arreglada y así puedan seguir beneficiándose de la misma.
 Profesionales de la informática y en especial de la seguridad. Estos profesionales, por distintas motivaciones, estudian de forma **legal** los sistemas y muchas veces logran encontrar vulnerabilidades. Este tipo de personas están interesadas en la **revelación** de la información. De esta forma acreditan haber encontrado la misma y así pueden apuntarse el mérito. Las motivaciones que tienen estos profesionales para encontrar la vulnerabilidades podríamos resumirlas en:
 Reputación. El que una persona o organización sea acreditada como la primera en descubrir una vulnerabilidad particular es muy importante en el mundo de la seguridad informática. Por un lado a las personas les acredita de habilidades y esto puede usarse para aumentar sus ingresos o conseguir mejores trabajos. Para una empresa también es importante porque puede utilizarse para conseguir clientes basándose en el alto nivel del personal que trabaja para ella.
 Perjudicar a competidores. Por ejemplo un desarrollador o compañía puede tener especial interés en buscar vulnerabilidades a productos de la competencia para poner en dificultades al proveedor y desacreditar sus productos. De esta forma se consigue mejorar la posición en el mercado del producto propio.
 Forzar al proveedor del producto a mejorar su calidad y que tenga más interés en producir software más seguro.
 Disfrutar del desafío intelectual de encontrar vulnerabilidades.
 Obtener gratificaciones monetarias por parte del proveedor del producto o de otra entidad.

 Tratamiento de la información sobre vulnerabilidades
Las formas de conseguir información sobre vulnerabilidades son las siguientes:
 Investigación sobre el funcionamiento de productos
 Investigación del funcionamiento de código malicioso que se aprovechan de vulnerabilidades
 A través de informes que revelan ese tipo de información.

Los dos aspectos fundamentales a estudiar sobre el tratamiento de la información sobre vulnerabilidades son:
 Como se difunde esa información (transmisión de la información)
 Como se gestiona para tener toda la información disponible (Gestión de la información)

 Transmisión de la información
Supongamos que alguien no implicado en un producto descubre una vulnerabilidad. Este puede tomar 4 opciones principales:
 No hacer nada
 Utilizarla y aprovechar dicha vulnerabilidad para vulnerar la seguridad del sistema.
 Intentar venderla a alguien interesado. Este es el punto de partida del llamado mercado de vulnerabilidades.
 **Revelarla** de forma pública y extensiva.

Los tres primeros casos podríamos agruparlos diciendo que adoptan una política de revelación basada en no revelar públicamente la información (cada uno por motivos distintos). En el último caso el individuo se enfrentaría a tomar una decisión sobre qué política de revelación pública de la información quiere usar.

 Fecha de revelación
La fecha de revelación es la fecha en la que se describe por primera vez la vulnerabilidad en un canal con las siguientes características:
 Libremente disponible al público
 La información es publicada por una fuente confiable e independiente. Se suele considerar un canal confiable cuando es una fuente aceptada de información de seguridad en la industria (por ejemplo, CERT/CC, Security Focus, Secunia, Microsoft Security Bulletin, USCERT y FrSIRT)
 La vulnerabilidad ha sido sometida al análisis de expertos que evalúan el riesgo de la revelación. Esto garantiza la calidad de la información divulgada y asegura que aporta suficientes detalles para permitir determinar el riesgo propio.

 Política de revelación
Si el sujeto quiere revelar públicamente la información sobre la vulnerabilidad, se enfrenta a una compleja pregunta: ¿Cómo revelar la información sobre dicha vulnerabilidad? La información sobre vulnerabilidades, cuando se revela, puede obligar al proveedor del producto a tomar acciones rápidamente para arreglar el defecto que lo hace posible; Sin embargo, esta misma información puede amplificar los riesgos para los usuarios y dar poder a aquellos que con malas intenciones quieren explotar la vulnerabilidad antes de que sea arreglada.

La política a seguir es un tema controvertido y no sólo es exclusivo del mundo informático. Por ejemplo en el pasado hubo controversias en el mundo de la cerrajería sobre la distribución del conocimiento de las vulnerabilidades que tenían las cerraduras.

Teniendo en cuenta los diversos factores (costes, beneficios y riesgos) se han propuesto distintos tipos de prácticas y políticas para la revelación de la información sobre vulnerabilidades. Las propuestas podríamos clasificarlas en 3 tipos: No revelar, revelación completa y prácticas a medio camino entre una otra (revelación parcial).

 No revelar

Podríamos considerar que la **no revelación** pública (extensiva) de la información sobre la vulnerabilidad es en sí misma una política de revelación. La información se mantiene en **secreto**. Este enfoque se basa en dar prioridad a mantener en secreto la vulnerabilidad frente a dar publicidad a la información para podernos proteger frente a ella.

Algunas veces en lugar de una no revelación absoluta, la información sobre la vulnerabilidad se comparte de forma restringida (**pseudosecreto**). Cuanto más amplio sea el número de personas que conocen la vulnerabilidad se incrementa el riesgo para los usuarios finales. La información puede revelarse por ejemplo a:
 El proveedor del sistema para que arregle la vulnerabilidad
 Otros investigadores (hackers).
 Alguien que compra esa información. De esta forma se establece un mercado de vulnerabilidades.

Muchas veces el descubridor de la vulnerabilidad toma esta política y la información se va divulgando por canales privados hasta que llega a cierta organización o persona que decide publicarla para evitar daños mayores.

 Revelación completa

La estrategia de **revelación completa**, **revelación total** o **divulgación masiva** (en inglés *full disclosure*) consiste en revelar a **toda** la comunidad (divulgación masiva) **toda** la información disponible sobre un problema de seguridad en cuanto este es conocido. Por ejemplo se puede dar información de como se encontró el fallo, qué sistemas son vulnerables, como explotar la seguridad o como protegerse frente al fallo. Se revelan todo tipo de detalles sobre el fallo y esta información tan detallada puede ser usada por hackers malintencionados para desarrollar exploits que permitan aprovechar la vulnerabilidad a cualquiera que lo utilice, aunque no entiendan el funcionamiento del mismo (script kiddies).

 Revelación parcial

Las políticas de revelación **revelación parcial** (en inglés *partial disclosure*) intentan establecerse como punto intermedio entre la política de seguridad por oscuridad y la política de revelación completa. Intentan aprovechar buenas ideas de una y otra política para situarse en un punto intermedio con mejores características. Se han desarrollado distintos modelos pero cada uno tiene sus inconvenientes considerándose el problema de la política de revelación como un problema abierto y pendiente de solución.

 Mercado de vulnerabilidades
Alrededor del mundo de los agujeros de seguridad se ha ido creando una importante actividad económica, dando lugar a negocios a veces muy lucrativos. El activo con el que se negocia es la información sobre la vulnerabilidad. El negocio suele estar en:
 La compra/venta de información sobre vulnerabilidades. El negocio puede ser con dinero o en especie (por ejemplo, publicidad sobre el descubridor o recompensando con un servicio de pago de forma gratuita). Puede haber intermediarios. Puede haber varias formas de realizar la compra/venta. Ejemplos: venta directa en exclusiva, venta directa sin exclusividad (lo mismo se puede vender a varios), subastas tradicionales, subastas con más de un ganador. El problema de las subastas es la habilidad de comunicar la calidad de la vulnerabilidad si divulgar la información sobre la vulnerabilidad. Esto se intenta conseguir dando unos mínimos detalles sobre la vulnerabilidad o el establecimiento de intermediarios de confianza que permitan establecer la calidad de la vulnerabilidad manteniendo la información en riguroso secreto (este tipo de intermediarios están apareciendo en el mercado *underground*).
 La contratación de personas/equipos que se dedican a la búsqueda de vulnerabilidades ya sea de forma interna o externa a la propia organización. Por ejemplo, hay multitud de empresas que se dedican a la auditoría de seguridad.
 La venta de productos (por ejemplo, antivirus, IDS, IPS o cortafuegos) que detectan, solucionan o mitigan el impacto de vulnerabilidades.
 Proveedores de productos que permiten detectar o aprovechar vulnerabilidades de otros productos.

Se ha propuesto que la existencia de un mercado de vulnerabilidades puede ser una buena idea para incentivar a los proveedores de sistemas para que se preocupen más en mejorar la seguridad de sus productos y en arreglar rápidamente las vulnerabilidades que se vayan encontrando.

 Motivaciones
Las motivaciones para la existencia de este tipo de mercado son, en última instancia:
 Conseguir ganancia económica. Este es el principal motivo para la existencia de este mercado.
 Consecución de una herramienta defensiva u ofensiva para poderla utilizar en cierto tipo de conflictos (guerra en red y guerra informática).

 Actores
Los actores en este mercado son:
 Productores de información:
 Hackers
 investigadores
 Consumidores:
 Gobiernos (guerra en red, guerra informática)
 Proveedores de sistemas objeto de los ataques.
 Proveedores de sistemas que protegen frente a ataques
 Atacantes maliciosos
 Intermediarios

 Mercado de vulnerabilidades y proveedores de productos
Los proveedores de productos juegan un papel especial en este mercado ya que el mercado se basa en la existencia de fallos en sus productos, lo que les puede provocar la pérdida de confianza y finalmente la pérdida de clientes. La existencia de un mercado de vulnerabilidades no les beneficia ya que:
 Desincentiva que investigadores les revelen la información sin pagar.
 Cuanto más mercado haya más competencia por obtener la información, más vale esa información y por tanto será más difícilmente accesible para los proveedores.
 Cuanto más mercado haya más competencia por obtener la información, más vale esa información y por tanto más se incentiva al descubrimiento de estas vulnerabilidades.

Por tanto intentan no fomentarlo aunque están siendo obligados por su crecimiento a entrar poco a poco en él para no verse excluidos cada vez más del conocimiento de las vulnerabilidades de sus propios productos. Por ejemplo cada vez es más frecuente la convocatoria de concursos remunerados para la búsqueda de vulnerabilidades.

Para fomentar la revelación de la información sin pagar están tomando una serie de iniciativas como por ejemplo:
 Facilitar el contacto para la comunicación de vulnerabilidades (por ejemplo, direcciones de correo electrónico o formularios web en su sitios web).
 Dedicación de recursos para la pronta respuesta y colaboración con los descubridores de vulnerabilidades.
 Establecimiento de buenas relaciones con investigadores para fomentar que les revelen la información. Ejemplos:
 Participación en conferencias de hackers e investigadores (por ejemplo, Black Hat Briefings).
 Crear sus propias conferencias (por ejemplo, Blue Hat).
 Invitar a sus dependencias a investigadores para que les enseñen como consiguen encontrar vulnerabilidades en sus productos.
 Agradecimiento público de las colaboraciones con los descubridores. De esta forma se da reputación a los investigadores.

 Tipos de mercado
Podemos hablar de dos mercados de vulnerabilidades claramente diferenciados: el lícito y el ilícito. Al ser una diferencia puramente legal, dependerá de la jurisdicción del país en el que estemos el que ciertos negocios pertenezcan a uno u otro mercado. Por este motivo las contrataciones de hackers con propósitos más controvertidos se realiza en países con legislación no muy restrictiva por ejemplo: Brasil, Rusia y Ucrania.

Para que el mercado lícito sea realmente efectivo tiene que:
 Atraer a los investigadores de vulnerabilidades. Para ello:
 Los precios tienen que ser comparables o superiores a los que da el mercado negro y ser lo suficientemente altos para que merezca la pena el esfuerzo. Hay que tener en cuenta que el mercado underground facilita la venta a múltiples compradores la misma información. En 2006 se estimaba que lo que pagaban a los investigadores empresas lícitas dedicadas a este negocio era equivalente a vender el producto a 3 actores maliciosos en el mercado underground. Lo que pagaban a los investigadores empresas proveedoras de productos era equivalente a vender el producto a 1 actor maliciosos en el mercado underground.
 Atraer la confianza de los investigadores. Para ello es habitual anunciarse en los entornos de los investigadores como las conferencias Blackhat y DEF CON de Estados Unidos o RootedCON de España.
 Ganar aceptación en la industria y por tanto clientes para sus productos. El objetivo es implantar la idea de que esta industria permite protegerse frente a vulnerabilidades que posiblemente ya circulan en el mercado ilícito. Para ello suelen utilizar políticas de revelación responsable y colaboran de forma activa para la corrección de dichas vulnerabilidades. También se suele pedir que el propio proveedor dé cierta publicidad al descubridor de la vulnerabilidad.
 Desarrollar el negocio de forma que permita obtener beneficios. El objetivo es crear productos (por ejemplo, boletines de información, productos software como antivirus, IDS, IPS o cortafuegos) que permitan protegerse frente a las vulnerabilidades antes de que el proveedor arregle la vulnerabilidad.

 Inconvenientes
Los principales inconvenientes de este tipo de mercado tienen que ver con la revelación de la información, la incentivación a los investigadores y el aumento de los precios de las vulnerabilidades

 Revelación de la información
La existencia del mercado de vulnerabilidades provoca una resistencia a que los agujeros de seguridad sean revelados para que puedan ser arreglados. La información sobre la vulnerabilidad pierde valor cuanto más gente la conoce y pierde totalmente el valor cuando el problema es arreglado y ya no existe. Por tanto hay una tendencia, para proteger el valor de la información, a mantener la información oculta. Todo esto repercute en una menor seguridad de los productos.

En general las más importantes empresas que se dedican a este negocio están comunican a los proveedores sobre las vulnerabilidades que encuentran. Sin embargo hay algunas compañías pequeñas que **no** lo hacen. Esta política de no revelación de vulnerabilidades es muy criticada pero no se suele considerar ilegal ya que la información es vendida con descargo de responsabilidad diciendo que esa información debería ser usado para pruebas internas, no para burlar la ley.

Los gobiernos, dependen del tipo de vulnerabilidad que encuentren, informan al proveedor del producto o no. Si se trata de un punto débil de sistemas que ellos mismos usan entonces comunicarán al proveedor. Si por ejemplo se trata de una vulnerabilidad utilizada en una herramienta ofensiva, entonces no revelará al proveedor la información sobre dicha vulnerabilidad

 Motiva la búsqueda de vulnerabilidades
La existencia de un mercado donde vender las vulnerabilidades provoca que haya una mayor investigación de vulnerabilidades, lo que provoca que se descubran más y por tanto haya un conjunto más amplio de vulnerabilidades activas que causas inseguridad a los usuarios

 Aumento de los precios de las vulnerabilidades
La existencia de un mercado cada vez más amplio de vulnerabilidades provoca que los precios suban. Esto provoca que la información sea menos accesibles a los proveedores que en definitiva son los que arreglan la vulnerabilidad para **todos** sus clientes.

 Ejemplos
Ejemplos de negocios en el mundo de las vulnerabilidades:
 Casi desde el principio de los sistemas de información ha habido, y sigue habiendo, un **mercado negro** o **mercado underground** e **ilícito** de vulnerabilidades en el que los atacantes venden información no revelada públicamente sobre vulnerabilidades para que otros puedan aprovecharlas de forma ilícita (por ejemplo, robar dinero, causar daños, espionaje, recopilar información para chantaje, divulgación de información falsa como verdadera (para por ejemplo hacer pump and dump) o adware indeseado. Un ejemplo contrastado de uso del mercado underground para la venta de información sobre vulnerabilidades es el caso de la vulnerabilidad del Microsoft Windows WMF rendering fue vendida en el mercado ilícito. Hay dos tipos de negocios relacionados con este tipo de mercado: La contratación para atacar un objetivo específico (por ejemplo, persona u organización) y por otro lado la compra de productos ya elaborados y listos para ser usados (exploits). Para ponerse en contacto, las partes de este tipo de mercado usan canales de IRC y sitios web específicos. Al ser un mercado ilícito los negocios no son públicos y esto facilita la venta del mismo producto a distintos compradores y así sacar un mayor beneficio.
 TippingPoint, una división de 3Com, ofrece sistemas de detección de intrusos para protegerse contra vulnerabilidades. Esta compañía aplica una política de seguridad de revelación responsable.
 iDefense, una compañía de Verisign, se dedica a la venta de información sobre vulnerabilidades. Dispone de un servicio de suscripción en el que los miembros pagan por recibir notificaciones sobre las vulnerabilidades y sobre soluciones o formas de mitigar el impacto de dichas vulnerabilidades hasta que el proveedor provea una solución. Esta compañía aplica una política de seguridad de revelación responsable.
 Algunos proveedores de productos convocan Bug Bounty's que son convocatorias para que hackers e investigadores sobre seguridad investiguen sus productos y, si encuentran e informan sobre vulnerabilidades se les gratifica por ello. Algunas de las organizaciones que han convocado este tipo de concursos son Mozilla, Microsoft, Google o Facebook.
 Muchos gobiernos tienen programas en los que vulnerabilidades que no son públicas pueden ser usados de forma defensiva u ofensiva con el objetivo de defender los intereses de los que detentan el poder. En 2001 ya se pensaba que más de 20 países tenían o estaban desarrollado capacidades para desarrollar ataques informáticos (guerra en red y guerra informática).
 Wabisabi Labi era un site que permitía la adquisición de vulnerabilidades. Permitía cuatro tipo de transacciones: Subastas tradicionales, subastas con más de un ganador, compras inmediatas y compras de un comprador exclusivo.
 Argeniss, Inmunity y GLEG Ltd son pequeñas compañías que contratan a sus propios investigadores y venden suscripciones a sus servicios para proveer información sobre las vulnerabilidades que encuentran. Esta información no la comunican a los proveedores de los productos a que se refieren. De esta forma incrementan el valor y el tiempo de vida de las vulnerabilidades con las que comercian. Le dan a la información un carácter privado. Esto ha tenido importantes críticas desde el punto de vista ético.

 Gestión de la información
Hay distintas iniciativas cuyo propósito es gestionar información sobre vulnerabilidades.

 Iniciativas del MITRE
El MITRE tiene distintas catálogos que permiten hacer un seguimiento de las vulnerabilidades (**CVE**), debilidades documentadas (**CWE**) y patrones de ataque (**CAPEC**). Los tres catálogos están estrechamente vinculadas, es decir, una vulnerabilidad es explotada gracias a una debilidad conseguida en un software o hardware, que a su vez ha sido aprovechada a través de un patrón de ataque. Por tanto, cada vez que cualquiera de las tres listas recibe una nueva entrada, ésta es considerada, comprobada y estudiada, por lo que muy probablemente se puedan generar o complementar los registros en cualquiera de las otras.

Asociado a las anteriores el MITRE tiene un formato (**CPE**) para identificar de forma detallada sistemas, productos y plataformas

 CVE

El MITRE CVE List o simplemente **CVE** es un catálogo de vulnerabilidades que asocia a cada vulnerabilidad conocida un identificador único que se conoce como **CVE-ID**. Este código CVE-ID es usado  como estándar de nomenclatura de vulnerabilidades por la mayoría de repositorios de vulnerabilidades para identificar cada vulnerabilidad. Además del identificador el catálogo describe en qué consiste la vulnerabilidad, que versiones del software están afectadas, posible solución al fall (si existe) o como configurar para mitigar la vulnerabilidad.

 CWE
El Common Weakness Enumeration o **CWE** es un catálogo de debilidades documentadas de software y hardware habituales que podría derivar en vulnerabilidades. Por ejemplo, inyección SQL (CWE-89) o desbordamiento de búfer (CWE-120) son entradas de este catálogo. Es muy utilizada por distintas herramientas de seguridad encargadas de identificar estas debilidades y para promover la identificación de las vulnerabilidades, mitigación y su prevención. Para cada debilidad se  aporta un identifcador **CWE-ID**, que es usado como estándar, y datos como la descripción, tiempo de introducción, ejemplos etc.

 CAPEC
El Common Attack Pattern Enumeration and Classification o **CAPEC** es un catálogo de patrones de ataque que recolecta información sobre ellos, junto a un esquema de clasificación exhaustiva. Un patrón de ataque es la descripción del método utilizado para la explotación de una vulnerabilidad, es decir, modelo para hacer un exploit de la vulnerabilidad. Muchas de las vulnerabilidades que se registran comparten patrones de ataques. Por ejemplo, el patrón de ataque 'Explotar confianza en cliente' (CAPEC-22) es un  patrón de ataque para canales cliente/servidor con autenticación y integridad de datos, en el que se aprovecha la confianza entre el cliente y el servidor para ejecutar un tipo de ataque en el que el servidor lo toma por un cliente válido. A cada patrón de ataque se le asocia un identificador **CAPEC-ID**, que es usado como estándar, y luego se aportan datos como la descripción, mitigaciones, recursos o habilidades necesarias para el ataque,...

 CPE
El Common Platform Enumeration o **CPE** es un formato que permite identificar con exactitud, con un nombre único y estándar sistemas, productos y plataformas. Es usado para determinar de forma totalmente unívoca y exacta las versiones, ediciones o idiomas, de un producto que están afectadas por una vulnerabilidad por una vulnerabilidad. EL NIST mantiene una versión autorizada para su distribución como parte de su iniciativa NVDB.

Por ejemplo para referirse a Microsoft Internet Explorer 8.* SP? (sin edición y en cualquier lenguaje) se usa:
 wfn:[part=”a”,vendor=”microsoft”,product=”internet_explorer”, version=”8.*”,update=”sp?”,edition=NA,language=ANY]

 Valoración de vulnerabilidades
Hay distintas iniciativas para evaluar de forma estándar la criticidad de las vulnerabilidades. Se basan en dar puntuaciones a partir de distintos criterios. Estos métodos estándar permiten establecer criterios representativos del riesgo en la organización, lo que se suele traducir en una priorización consciente de las medidas de seguridad que se desean aplicar.

 CVSS
El **Common Vulnerability Score System** o **CVSS** es un estándar abierto definido por el Forum of Incident Response and Security Teams (FIRST) que cuantifica las vulnerabilidades estimando el impacto derivado de la misma. Se usa un puntaje del 1 al 10 y para establecerlo se usan una serie de métricas públicas. Este estándar es usado por la National Vulnerability Database y por el Common Vulnerabilities and Exposures. La forma de establecer las medidas va evolucionando, produciendo nuevas versiones del estándar.

 CWSS
Creado por el MITRE como parte del proyecto CWE y contando con el apoyo del gobierno de los Estados Unidos, el **Common Weakness Scoring System** o **CWSS** es un estándar que pretende ser una evolución del CVSS. Sigue un criterio más avanzado que su antecesor. Por ejemplo: Se tienen en cuenta los efectos de los procesos críticos de negocio, determina hasta qué punto esa vulnerabilidad podría ser aprovechada por hackers (puede otorgar acceso a documentos en modo de sólo lectura o si las cosas serían más graves y se podría acceder en modo de escritura, pudiendo modificar datos o eliminarlos).

El CWSS está orientado a los desarrolladores y a facilitar su trabajo estableciendo criterios para su utilización durante la fase de desarrollo de un programa. Por ejemplo si se descubre un buffer overflow durante una auditoría de código, se le asigna una prioridad CWSS baja si los datos que disparan ese suceso no son ingresados por el usuario sino que son parte del funcionamiento aleatorio del programa.

No existe una web, servicio o aplicación pública que utilice este sistema. En sus inicios, este sistema se solía promover a través de publicaciones (como por ejemplo los documentos desarrollados entre el MITRE y SANS Institute del tipo Top 25 Most Dangerous Software Errors), sin embargo, en la actualidad es difícil encontrar información reciente asociada a debilidades de software. Puede deberse a que hoy por hoy la lista CWE se actualiza muy poco y a que las empresas de desarrollo de software protegen el código de sus aplicaciones y su estudio, valoración y resolución se suele gestionar de manera privada sin compartir la información.

 Repositorios de vulnerabilidades
Además de la CVE del MITRE, que funciona más como fuente de información básica que proporciona una identificación estándar de vulnerabilidades, hay distintas bases de datos de vulnerabilidades:

 La National Vulnerability Database o **NVDB** es el repositorio de vulnerabilidades del NIST, una agencia de la Administración de Tecnología del Departamento de Comercio de los Estados Unidos.  Para facilitar el uso y clasificación de vulnerabilidades, este repositorio usa SCAP, un estándar para expresar (formatos y nomenclaturas) y manipular información relacionada con la seguridad sobre fallos y configuraciones. Para evaluar las vulnerabilidades usa CVSS.
 Vulnerability Assessment Platform (Vulners) es un repositorio de vulnerabilidades correlacionados con sus exploits. Actualiza regularmente su base de datos de más de 70 fuentes.
 Vulnerability Database (VulDB).
 CVE Details.
 Vulnerability Notes Database o **VND** es un repositorio de vulnerabilidades del CERT Coordination Center/CC de la Universidad Carnegie Mellon.
 WPScan Vulnerability Database es un repositorio de vulnerabilidades asociadas a WordPress.

 Buscadores de vulnerabilidades
El volumen de crecimiento de las vulnerabilidades junto a la existencia de distintos repositorios de vulnerabilidades, las cuales a su vez no suelen ser muy cómodas de consultar, ha provocado la aparición de software que se encarga de buscar automáticamente en los distintos repositorios de vulnerabilidades. Es frecuente que estas herramientas también consulten varias bases de datos de exploits. Ejemplos de este tipo de herramientas son Pompem, vFeed y vulnerability-alerter

Otro enfoque consiste en descargar toda la información, almacenarla en una base de datos y hacer consultas sobre ella. Este es el enfoque de por ejemplo cve-search

 Casos famosos
Varias industrias, incluida la industria de salud, los bancos e, incluso, el gobierno de los Estados Unidos, se han visto afectadas por brechas de seguridad por causa de vulnerabilidades de sistemas.

Casos incluyen:
 En junio de 2005, un servidor de mantenimiento de tarjetas de crédito fue crackeado por un grupo de personas, aprovechando un error en el código de verificación. Esto generó pérdidas por 10000000 de dólares estadounidenses.
 El FBI sufrió un ataque de un usuario que usó cuentas de correo, obtuvo contraseñas y otros datos de relevancia, a través de un puerto que estaba abierto en el código web.
 En Windows 98, ciertas contraseñas de usuario se exponen en las carpetas, que pueden ser leídas en MS-DOS.

 Véase también
 Error de software
 Exploit
 Seguridad informática
 Common Vulnerabilities and Exposures
 Packet Storm
 Privacidad digital

 Referencias

 Bibliografía
 Andrew Cencini et ali., *Software Vulnerabilities: Full-, Responsible-, and Non-Disclosure*, diciembre de 2005.
 Stephen A. Sheperd, *Vulnerability Disclosure. How do we define Responsible Disclosure?* SANS Institute, abril de 2003.
 Jaziar Radianti et ali., *Toward a Dynamic Modeling of the Vulnerability Black Market.* Faculty of Engineering and Science, Agder University. Octubre de 2006.
 George K. Kostopoulos, *Cyberspace and Cybersecurity.* CRC Press. 2013.
 Michael Sutton y Frank Nagle, *Emerging Economic Models for Vulnerability Research.* Proceedings of the Workshop on the Economics of Information Security. 2006.

 Enlaces externos
  CVE: Listado de vulnerabilidades comunes clasificadas y publicadas junto con proveedores de soluciones.
  Vigilance vulnerabilities: Ver técnica vulnerabilidades y sus soluciones.
 Secuser.com: Portal francés dedicado a la seguridad de las tecnologías.
 info.corroy.org: Una visión general del actual equipo de seguridad.
 Netcraft
 NIST SAMAT: Métrica de Software Assurance y la herramienta de evaluación de proyectos.
 Microsoft: Microsoft Security Response Center definición.
