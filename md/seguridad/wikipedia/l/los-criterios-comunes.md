---
type: Artículo de enciclopedia
title: Los criterios comunes
description: "Los Criterios Comunes(CC) tienen su origen en 1990 y surgen como resultado de la armonización de los criterios sobre seguridad de productos software ya utilizados por diferentes países con el fin de que el resultado del …"
resource: https://es.wikipedia.org/wiki/Los_criterios_comunes
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Los_criterios_comunes"}
license: CC BY-SA 4.0
id: eswiki-Los_criterios_comunes
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Los criterios comunes

Los Criterios Comunes(CC) tienen su origen en 1990 y surgen como resultado de la  armonización de los criterios sobre seguridad de productos software ya utilizados por diferentes países con el fin de que el resultado del proceso de evaluación pudiese ser aceptado en múltiples países.
Los CC permiten comparar los resultados entre evaluaciones de productos independientes. Para ello, se proporcionan un conjunto común de requisitos funcionales para los productos de TI (Tecnologías de la Información). Estos productos pueden ser hardware, software o firmware. El proceso de evaluación establece un nivel de confianza en el grado en el que el producto TI satisface la funcionalidad de seguridad de estos productos y ha superado las medidas de evaluación aplicadas.
Los CC son útiles como guía para el desarrollo, evaluación o adquisición de productos TI que incluyan alguna función de seguridad. La lista de productos certificados según los CC se encuentra disponible en la web de Common Criteria.

 Historia
El origen de los Criterios Comunes podemos encontrarlo en los criterios usados por diferentes países para la evaluación de la seguridad de los productos software desarrollados. Los CC combinan criterios de los:
- TCSEC (del inglés Trusted Computer System Evaluation Criteria) frecuentemente conocido como “Libro Naranja” y usados por el Departamento de Defensa de EE. UU.
- ITSEC (del inglés Information Technology Security Evaluation Criteria) comúnmente conocido como “Libro Blanco” y utilizados en Europa, y;
- CTCPEC (del inglés Canadian Trusted Computer Product Evaluation Criteria) utilizados en Canadá.
En 1999 los Criterios Comunes en su versión 2.0 fueron adoptados por la International Organization for Standardization (ISO) como estándar internacional. En la actualidad los CC se encuentran estandarizados bajo la serie de normas ISO/IEC 15408 (ISO/IEC 15408-1,2009), (ISO/IEC 15408-2,2008) y (ISO/IEC 15408-3,2008) aunque la última versión se encuentra disponible en la web del Common Criteria.

 Funcionamiento
Con el fin de poder certificar un producto según los Criterios Comunes se deben comprobar, por parte de uno de los laboratorios independientes aprobados, numerosos parámetros de seguridad que han sido consensuados y aceptados por 22 países de todo el mundo. El proceso de evaluación incluye la certificación de que un producto software específico verifica los siguientes aspectos:
 Los requisitos del producto están definidos correctamente.
 Los requisitos están implementados correctamente.
 El proceso de desarrollo y documentación del producto cumple con ciertos requisitos previamente establecidos.
Los Criterios Comunes establecen entonces un conjunto de requisitos para definir las funciones de seguridad de los productos y sistemas de Tecnologías de la Información y de los criterios para evaluar su seguridad. El proceso de evaluación, realizado según lo prescrito en los Criterios Comunes, garantiza que las funciones de seguridad de tales productos y sistemas reúnen los requisitos declarados. Así, los clientes pueden especificar la funcionalidad de seguridad de un producto en términos de perfiles de protección estándares y de forma independiente seleccionar el nivel de confianza en la evaluación de un conjunto definido desde el EAL1 al EAL7.

 Perfiles de Protección
Un perfil de protección (Protection Profile) define un conjunto de objetivos y requisitos de seguridad, independiente de la implantación, para un dominio o categoría de productos que cubre las necesidades de seguridad comunes a varios usuarios. Los perfiles de protección son reutilizables y normalmente públicos y están compuestos de:
 Requisitos funcionales (SFR, Security Funcional Requirement) proporcionan mecanismos para hacer cumplir la política de seguridad. Como ejemplos de requisitos funcionales mencionar la protección de datos de usuario, el soporte criptográfico, la autenticación, la privacidad o el control de acceso.
 Requisitos de confianza o aseguramiento (SAR, Security Assurance Requirement)  proporcionan la base para la confianza en que un producto verifica sus objetivos de seguridad.
Los requisitos de confianza se han agrupado en niveles de confianza en la evaluación (EAL, Evaluation Assurance Levels) que contienen requisitos de confianza construidos específicamente en cada nivel. Los EALs proporcionan una escala incremental que equilibra el nivel de confianza obtenido con el coste y la viabilidad de adquisición de ese grado de confianza. El incremento de confianza de un EAL a otro se obtiene incrementando rigor, alcance y/o profundidad en el componente y añadiendo componentes de confianza de otras familias de confianza (por ejemplo, añadiendo nuevos requisitos funcionales).
Una lista de los perfiles de protección validados se puede encontrar en

 Metodología de perfil de protección basada en los criterios comunes
Los Criterios Comunes (CC) contienen el criterio de evaluación que permite a un evaluador informar si un Perfil de Protección (PP) es completo, consistente y técnicamente válido.

Un PP debe presentarse como un documento orientado al usuario, y se ajustará al contenido de los requerimientos descritos en CC. La metodología es la siguiente:

1)     Introducción

Contendrá el documento administrador y un panorama del PP como se indica a continuación:

·       El documento administrador se refiere a la identificación del PP que proporcionará la etiqueta y la información descriptiva necesaria para identificar, clasificar, registrar y cruzar referencias en un PP.

·       El panorama del PP recopilará el PP en su forma narrativa, será lo suficiente detallado a fin de que los lectores de la introducción puedan determinar sin lugar a duda si el PP es de interés para la organización.

2)     Descripción de objeto de evaluación

En esta parte del PP se describe al objeto de evaluación a fin de entender sus requerimientos de seguridad. Asimismo, si el objeto de evaluación es un producto o sistema cuya función primordial es la seguridad, esta parte del PP puede ser usada entonces para describir el amplio contexto de aplicación dentro del cual se aplicará. Así la descripción:

·       Añade detalles que complementan la información que aparece en la Introducción.

·       Va dirigido principalmente al técnico administrador.

·       Incluye una descripción funcional, la cual es más detallada y va más allá de una descripción de las características de seguridad.

·       Contiene una descripción de la frontera del objeto de evaluación, informando de manera muy clara qué es lo que está contenido en el objeto de evaluación, y qué es lo que está fuera de él.

·       Debe ser consistente técnicamente.

3)     Entorno de seguridad

Se deben describir los aspectos de seguridad del entorno en el cual se pretende utilizar el objetivo de evaluación y la forma como se espera éste sea empleado, de manera que debe incluir:

·       Una descripción de las hipótesis.

·       Una descripción de las amenazas.

·       Una descripción de las políticas de seguridad organizacional.

Considerando todo aquello que interactúa con el objeto de evaluación y que se encuentra en el entorno como, por ejemplo: los sistemas físicos y lógicos, tipos de usuarios, hardware y software, será necesario discutir los aspectos del entorno de seguridad por separado a fin de distinguir el dominio del entorno del objeto de evaluación.

Con base en lo anterior podemos decir que en el entorno de seguridad:

·       La descripción se enfoca principalmente a las necesidades del usuario y con ello facilita la definición de requerimientos.

·       El análisis considera los diversos factores con los que interactúa.

·       Su análisis hace explícitas las hipótesis que se plantea al desarrollar el PP y las expectativas sobre el entorno que no se resolverán en otros ámbitos.

·       Su análisis identifica las amenazas a las que está expuesto el objeto de evaluación y determina las políticas de seguridad que deberán operar para resguardar el entorno.

4)     Hipótesis

A través de las hipótesis se busca mostrar aspectos de seguridad del entorno, . Se busca información necesaria para entender el uso del objeto sujeto a evaluación, se deben de contemplar el entorno en el que se encuentra, los factores que lo pueden afectar y la forma del comportamiento del objeto. Se deben de tomar en cuentan las siguientes consideraciones:

·       Considerar las hipótesis necesarias según el entorno de trabajo y la interacción con los elementos que la rodean.

·       La identificación entre las hipótesis con el objeto debe ser identificadas según el entorno físico, personal, la conectividad y los procedimientos que realizará.

·       No incluir información de las funciones de seguridad que se requieran o deseen implementar.

·       Identificar las hipótesis con alguna etiqueta o nombre.

5)     Amenazas

Se describirán todas aquellas acciones que pongan en riego a los bienes de la organización. Se deben de tomar en cuenta las amenazas que afecten al desarrollo de los requerimientos, se debe de crear una especie de clasificación dentro de las amenazas para identificar en cuales de ellas se necesita protección, los métodos de ataque a los cuales debe de estar preparado, estar prevenido de los eventos indeseables, así como de los agentes amenazantes. Los agentes de amenaza deben de estar escritos por aspectos como experiencia, recursos disponibles y motivación, mientras que los ataques deben de diferenciarse por métodos de arranque, vulnerabilidades explotadas. Por lo que este apartado debe contener:

·       Las amenazas que permiten desarrollar requerimientos.

·       Las amenazas que sean relevante así determinando cuales son los bienes que necesitan protección, así identificando los métodos de ataque y quienes o cuales son los agentes amenazadores.

·       Las descripciones de las amenazas deben de concisa.

·       Una etiqueta o nombre para facilitar referencias.

6)     Políticas de seguridad de la organización

A partir del estudio de las amenazas es posible determinar las políticas de seguridad como un conjunto de reglas de seguridad. La explicación y la interpretación de los informes de política pueden esclarecer el conjunto de objetivos de seguridad, para ello se tiene:

·       Determinar políticas de seguridad informática para la organización, así como los requisitos que no son posibles satisfacer.

·       Definir políticas como lo son un conjunto de reglas a las que debe de estar sujeto el objeto de evaluación.

·       Asignar etiqueta o nombre a cada política.

7)     Objetivos

Una vez que ya se tienen bases como lo es las hipótesis amenazas y políticas de seguridad durante el análisis del entorno de seguridad, se establecerá los objetivos de seguridad colocando primordialmente los objetivos del perfil de protección. Los objetivos se pueden agrupar en dos categorías:

·       Objetivos de seguridad para el objeto de evaluación: estos deben de estar documentados y referidos a los aspectos de las amenazas para ser contrarrestadas por el objeto de evaluación.

·       Objetivos de seguridad para el entorno: estos deben de estar documentados y referidos a los aspectos de las amenazas no contrarrestadas por el objeto de evaluación.

A su vez, los objetivos de seguridad indicarán:

·       Cómo se hace frente a las amenazas y a las políticas desde el punto de vista de las hipótesis.

·       La naturaleza de los requerimientos.

·       El grado de efectividad esperado.

·       El enfoque particular de cada objetivo.

·       Relación entre el objetivo, las políticas y las amenazas cuya relación puede ser uno a uno, uno a muchos, o muchos a uno.

·       Un objetivo de seguridad para cada requerimiento funcional.

·       Cualquier objetivo de seguridad que se deba cumplir en el entorno.

·       Cualquier responsabilidad de procedimientos que se refiera a la administración y uso de medidas de defensa del objeto de evaluación como objetos de seguridad, y debe incluir hasta qué punto se satisfagan los requerimientos.

·       El tipo de cada objetivo, esto es, si es de tipo preventivo, detectivo o correctivo.

·       Una etiqueta o nombre a cada objetivo para facilitar las referencias.

8)     Requerimientos

Con respecto a los requerimientos, es necesario realizar una valoración de los bienes, a fin de determinar el nivel de seguridad y de garantía necesarios y seleccionar los requerimientos de garantía de la tecnología de la información con base en el valor de los activos que se desean proteger. Para este fin es necesario consultar el catálogo de requerimientos incluidos en el CC.

El informe de los requerimientos de seguridad definirá los requerimientos que le permitan al objeto de evaluación y a su entorno funcionar seguramente. A estos requerimientos se les define en dos categorías:

·       Requerimientos funcionales: aquellos que se refieran a que el objeto de evaluación opere.

·       Requerimientos de garantía: aquellos que garanticen que el objeto de evaluación es seguro y por lo tanto el usuario de éste lo considere confiable.

9)     Justificación

La justificación debe de realizarse considerándose los pasos anteriores: objetivos y requerimientos de seguridad. En el caso de los objetivos se demostrará que son fáciles de seguir para todos los aspectos identificados en el entorno de seguridad del objeto de evaluación, y que es conveniente cubrirlos; en el caso de los requerimientos, se demostrará que será de gran utilidad reunir el conjunto de requerimientos de seguridad, y que es fácil de seguir para alcanzar los objetivos planteados.

10) Definición de arquitectura

Se deben de seleccionar los mecanismos y herramientas para llevar a cabo su implementación para lo cual es necesario:

·       Diseñar la arquitectura de seguridad basada en los requerimientos identificados.

·       Llevar a cabo la selección de las herramientas que logren los objetivos planteados, hagan cumplir las políticas de seguridad y contrarresten las amenazas identificadas.

·       Buscar soluciones que protejan el objeto de evaluación, así como el software y el hardware asociados al entorno de seguridad.

11) Implementación

Durante la implementación se lleva a cabo la instalación de las herramientas de seguridad siguiendo las indicaciones dadas por el fabricante a través de los manuales y configurándolas de acuerdo con las políticas de seguridad. Para ello:

·       Se instalan las herramientas seleccionadas.

·       La configuración de las herramientas se hace obedeciendo las políticas de seguridad.

·       Se lleva a cabo las pruebas pertinentes.

·       El esquema de seguridad está en reproducción.

 Niveles de confianza
Los niveles de confianza en la evaluación definidos en el ISO/IEC 15408-3 [ISO 15408-3 2005] van desde EAL1 (el menor) a EAL 7 (el mayor) y se definen de forma acumulativa (verificaciones de nivel n+1 implican realizar las de nivel n, 1 ≤ n ≤ 7):
 EAL1 (funcionalidad probada): es aplicable donde se requiere tener cierta confianza de la operación correcta, y donde además, las amenazas a la seguridad no son vistas como serias. Una evaluación en este nivel debe proporcionar evidencia de que las funciones del objeto de  evaluación son consistentes con su documentación, y que proporcionan protección útil contra amenazas identificadas.
 EAL2 (estructuralmente probado): requiere la cooperación del desarrollador en términos de la distribución de la información del diseño, y los resultados de las pruebas y proporciona confianza a través de un análisis de las funciones de seguridad, usando una especificación funcional y de interfaz, manuales y diseño de alto nivel del producto para entender el comportamiento de seguridad. Además, en este nivel se verifica que el desarrollador realizó un análisis de vulnerabilidades a través de la ejecución de pruebas de caja negra  (black-box).
 EAL3 (probado y verificado metódicamente): permite a un desarrollador alcanzar una máxima garantía de ingeniería de seguridad positiva en el estado de diseño sin la alteración substancial de prácticas de desarrollo válidas existentes. El análisis en este nivel se apoya en las pruebas de caja gris  (grey box), la confirmación selectiva independiente de los resultados de las pruebas del desarrollador, y la evidencia de búsqueda de vulnerabilidades obvias del desarrollador. Además, se realizan controles del entorno de desarrollo y de gestión de configuración del producto.
 EAL4 (diseñado, probado y revisado metódicamente): este nivel le permite a un desarrollador alcanzar máxima garantía de ingeniería de seguridad positiva basada en buenas prácticas de desarrollo comercial, las cuales, aunque rigurosas, no requieren del conocimiento especializado substancial, destreza, ni otros recursos. En este caso, el análisis se apoya en el diseño de bajo nivel de los módulos del producto y se realiza búsqueda de vulnerabilidades independiente de las pruebas realizadas  por el desarrollador. Los controles de desarrollo se apoyan en un modelo de ciclo de vida de desarrollo, identificación de las herramientas utilizadas y gestión de configuración automatizada.
 EAL5 (diseñado y probado semiformalmente): permite a un desarrollador alcanzar máxima garantía de ingeniería de seguridad positiva mediante la aplicación moderada de técnicas de ingeniería de seguridad. La confianza se apoya, en este caso, en un modelo formal y una presentación semiformal de la especificación funcional y el diseño de alto nivel. La búsqueda de vulnerabilidades debe asegurar la resistencia relativa a los ataques de penetración.
 EAL6 (diseño verificado y probado semiformalmente): permite a los desarrolladores alcanzar una alta garantía en la aplicación de técnicas de ingeniería de seguridad para un entorno de desarrollo riguroso y donde el objeto de evaluación es considerado de gran valor para la protección del alto costo o estimación de esos bienes contra riesgos significativos. Además, es aplicable para el desarrollo de objetos de evaluación, destinados a salvaguardar la seguridad informática en situaciones de alto riesgo donde el valor de los bienes protegidos justifica los costos adicionales. El análisis en este nivel se apoya en un diseño modular y en una presentación estructurada de la implementación del producto. La búsqueda de vulnerabilidades debe mostrar una alta resistencia a los ataques de penetración.
 EAL7 (diseño verificado y probado formalmente): es aplicable al desarrollo de objetos de evaluación de seguridad, para su aplicación en situaciones de muy alto riesgo o donde el alto valor de los bienes justifica los más altos costos. La aplicación práctica del nivel EAL7 está limitada actualmente a objetos de evaluación con seguridad estrechamente enfocada a la funcionalidad, y que es sensible al análisis formal y extenso. Este EAL representa un incremento significativo respecto a la garantía de nivel EAL6 a través  del requisito de análisis de gran amplitud, mediante representaciones formales y correspondencia formal y pruebas de gran amplitud. Además, el evaluador confirmará de forma independiente y completa los resultados de las pruebas de caja blanca  (White-box) realizadas por el desarrollador.
Los niveles EAL 5 al 7 incluyen modelos y demostraciones semi-formales y formales por tanto, se aplican a productos con objetivos de seguridad muy específicos (entorno militar, por ejemplo). Por otra parte, estos niveles requieren de la generación de una gran cantidad de documentación durante el proceso de desarrollo que debe entregarse al evaluador para que éste pueda confirmar la información.
Finalmente, para la aplicación de los Criterios Comunes, existe una metodología con los criterios a evaluar para cada uno de los niveles de confianza estandarizada por la Norma ISO/IEC 18045 (ISO 18045, 2008) y denominada CEM (Common Methodology for IT Security Evaluation) disponible en la web de Common Criteria

 Enlaces externos

Sitio web oficial de Common Criteria
Organismo de Certificación. Esquema Nacional de Evaluación y Certificación de la Seguridad de las Tecnologías de la Información. España

 Referencias

 ISO/IEC 15408-1: 2005. Information technology - Security techniques - Evaluation criteria for IT security - Part 1: Introduction and general model.
 ISO/IEC 15408-2: 2008. Information technology - Security techniques - Evaluation criteria for IT security - Part 2: Security functional requirements.
 ISO/IEC 15408-3: 2008. Information technology - Security techniques - Evaluation criteria for IT security -- Part 3: Security assurance requirements.
 ISO/IEC 18045: 2008. Information technology -- Security techniques - Methodology for Information Technology Security Evaluation.
 López Barrientos, M. J., & Quezada Reyes, C. (2006). Fundamentos de Seguridad Informática. México: UNAM, Facultad de Ingeniería.
