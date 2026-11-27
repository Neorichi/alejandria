---
type: Artículo de enciclopedia
title: Operación Triangulación
description: Operación Triangulación (en inglés, Operation Triangulation) es un ciberataque dirigido contra dispositivos iOS que se ejecuta mediante una cadena de cuatro ataques de día cero.
resource: https://es.wikipedia.org/wiki/Operación_Triangulación
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Operación_Triangulación"}
license: CC BY-SA 4.0
id: eswiki-Operación_Triangulación
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Operación Triangulación

**Operación Triangulación** (en inglés, Operation Triangulation) es un ciberataque dirigido contra dispositivos iOS que se ejecuta mediante una cadena de cuatro ataques de día cero. Fue identificado por primera vez en junio de 2023 y se distingue por su complejidad técnica sin precedentes entre los ataques a iOS. Se estima que afectó a miles de víctimas.

 Objetivos del ataque
El objetivo de este ataque era espiar: extraer mensajes y contraseñas de los dispositivos, grabar conversaciones y obtener datos de geolocalización. La cantidad exacta de víctimas es incierta debido al alto nivel de sigilo de los atacantes, pero algunas fuentes estiman que se trata de varios miles, entre los cuales se encuentran organizaciones comerciales, gubernamentales y diplomáticas de Rusia y sus representantes en el extranjero.

 Cronología de los eventos
**1 de junio de 2023:** Kaspersky anuncia el descubrimiento de rastros de un nuevo tipo de malware en algunos dispositivos iOS de sus empleados. Este sigiloso malware, diseñado con fines de espionaje, solo se pudo detectar por intercambios de datos sospechosos con los iPhones infectados. Los investigadores detectaron rastros de infecciones que datan de 2019. El ataque se denominó **Operation Triangulation.**
Por la misma fecha, Kaspersky lanzó una herramienta llamada triangle_check que permite a los usuarios verificar si sus dispositivos iOS han sido comprometidos y determinar si han sido víctimas del ataque.

**21 de junio de 2023:** Kaspersky publica una investigación sobre el implante TriangleDB, utilizado en el ataque.

Ese mismo día, Apple lanza actualizaciones para iOS 15.x y 16.x que corrigen dos vulnerabilidades explotadas en el ataque: CVE-2023-32434 en el núcleo de iOS y CVE-2023-32435 en el motor de navegación WebKit. Estas vulnerabilidades permitían infectar dispositivos iPhone de manera silenciosa, eludiendo los sistemas de seguridad de iOS.

**24 de julio de 2023:** Apple publica actualizaciones para iOS 15.x y 16.x que solucionan la vulnerabilidad CVE-2023-38606 en el núcleo de iOS y CVE-2023-41990 en el mecanismo de procesamiento de fuentes FontParser. Estas vulnerabilidades también formaban parte de la cadena de infección de Operation Triangulation.

**23 de octubre de 2023:** Kaspersky publica información acerca de las múltiples etapas de validación que utilizan los atacantes para seleccionar a sus víctimas. Estos filtros permiten infectar solo a objetivos específicos y, de ese modo, evitar ser detectados por expertos en ciberseguridad.

**26 de octubre de 2023:** Kaspersky presenta un informe en la Security Analyst Summit sobre el proceso de investigación de Operation Triangulation y los esfuerzos por identificar todos los componentes de la cadena de infección.

**27 de diciembre de 2023:** Kaspersky presenta un informe en el Chaos Communication Congress sobre la cadena de ataque completa y las cuatro vulnerabilidades utilizadas en el ataque, incluidas las funciones no documentadas de los procesadores de Apple.

**28 de diciembre de 2023:** El reconocido hacker Hector Martin se entera de que Operation Triangulation utilizó funciones no documentadas de los procesadores de Apple y difunde información sobre posibles mecanismos y propósitos.

 Detalles técnicos
Operation Triangulation es un ataque contra iOS de extrema complejidad técnica y sin precedentes entre los de su tipo: la cadena de infección consta de 14 pasos, utiliza cuatro ataques de día cero y explota funciones de hardware no documentadas de los procesadores de Apple. Todos los ataques que trascendieron infectaron versiones de iOS hasta 15.7.x, pero las técnicas son efectivas hasta iOS 16.2.

El código malicioso se ejecuta cuando un iPhone recibe un iMessage especialmente diseñado e invisible para el usuario. Luego, se descargan componentes adicionales desde los servidores de mando de Operation Triangulation que otorgan privilegios en el dispositivo infectado y despliegan un software espía con amplio acceso a su contenido y funciones.

 Mecanismo de infección
La infección inicial se lleva a cabo mediante el iMessage invisible. El archivo malicioso del iMessage, adjunto como un .watchface (un diseño de pantalla de reloj, que es básicamente un archivo ZIP con un PDF incrustado), ejecuta un código que abre Safari en segundo plano para que se carguen los próximos componentes de la cadena de infección desde un sitio web.

Este sitio contiene un script de validación que analiza los parámetros del teléfono infectado y decide si la infección debe continuar mediante el uso de la tecnología de Canvas fingerprinting, que dibuja un triángulo en la página web para identificar de manera única a las víctimas. Este triángulo es el que da nombre a toda la campaña.

El ataque utiliza las vulnerabilidades de día cero CVE-2023-41990, CVE-2023-32434 y CVE-2023-38606.

Luego de una validación, el script de la página web también utiliza la vulnerabilidad CVE-2023-32435, carga un código binario en la memoria del dispositivo, obtiene privilegios de superusuario y realiza una verificación más detallada del *smartphone* para evaluar si es de interés para los atacantes. Este validador binario también elimina rastros del iMessage recibido y, finalmente, carga TriangleDB, el implante malicioso principal.

El malware solo opera en la memoria del dispositivo, por lo que se borra tras un reinicio. Sin embargo, los atacantes pueden reenviar el iMessage e infectar nuevamente a la víctima.

 Funciones no documentadas de Apple
Para evadir las protecciones de memoria en las generaciones recientes de procesadores Apple (A12–A16), el exploit de la vulnerabilidad del núcleo CVE-2023-38606 usa funciones de hardware no documentadas.

Es decir, este exploit escribe en registros MMIO que no están descritos en la documentación y no son utilizados por aplicaciones ni el sistema operativo iOS. Como resultado, el código del exploit puede modificar áreas protegidas del núcleo de iOS. Los investigadores de Kaspersky sugieren que este mecanismo probablemente fue creado para la depuración del propio procesador.

Algunos expertos sostienen que "muy pocos, o nadie, excepto Apple y proveedores de chips como ARM Holdings", podrían saber sobre esta función. Hector Martin describió un posible mecanismo de explotación basado en escrituras directas en la caché de memoria, lo que a veces permite evadir determinados mecanismos de protección.

 Funciones del implante TriangleDB
El malware TriangleDB tiene una estructura modular que le permite extender sus funciones mediante la descarga de módulos adicionales desde el servidor.

La versión básica del malware permite subir archivos del dispositivo al servidor de los atacantes, extraer datos del llavero de iOS, rastrear la geolocalización de la víctima, y modificar archivos y procesos en el dispositivo.

Algunos módulos adicionales sobre los que se tiene conocimiento permiten acceder al micrófono por tiempo prolongado (aunque el móvil esté en modo avión), ejecutar consultas en bases de datos almacenadas en el dispositivo y robar chats WhatsApp y Telegram.

 Métodos de detección y eliminación
**Bloqueo de actualizaciones**

Un indicador de que un dispositivo ha sido blanco de Operation Triangulation es la imposibilidad de descargar actualizaciones de iOS. Sin embargo, algunos dispositivos infectados han podido actualizarse con normalidad.

**Análisis de la copia de seguridad de iTunes**

Algunos rastros del ataque se pueden encontrar en los archivos del sistema del iPhone. Dado que no es posible acceder a estos archivos desde el propio dispositivo, se recomienda hacer una copia de seguridad del iPhone en iTunes y luego analizarla con la herramienta triangle_check.

**Análisis de conexiones de red**

El código malicioso de Operation Triangulation establece conexiones con los servidores de los atacantes, y se ha publicado un listado de las direcciones utilizadas que todos pueden consultar.

**Eliminación de la infección**

Para dispositivos que ya han sido comprometidos, los expertos recomiendan seguir los siguientes pasos para evitar la reinfección: restablecer valores de fábrica, desactivar iMessage, actualizar iOS a una versión más reciente.

 Autoría
Kaspersky no ha emitido declaraciones oficiales sobre el origen del ataque ni lo ha atribuido a ningún grupo o país.

Sin embargo, el 1 de junio de 2023, el Servicio Federal de Seguridad de Rusia (FSB) emitió un comunicado sobre el descubrimiento de malware en teléfonos Apple, indicando que explotaba "vulnerabilidades proporcionadas por el fabricante". El FSB acusó directamente a Apple de colaborar con la NSA y afirmó que varios miles de teléfonos fueron infectados, incluyendo dispositivos fuera de Rusia en países de la OTAN, el espacio postsoviético, Israel, Siria y China.

Ese mismo día, Apple emitió un comunicado para negar las acusaciones.

Cabe destacar que el FSB y Kaspersky hicieron declaraciones por separado, pero algunos expertos coinciden en que ambos hacen clara referencia a Operation Triangulation.

 Consecuencias
Apple negó públicamente cualquier tipo de vinculación con agencias de inteligencia para implantar puertas traseras y lanzó varias actualizaciones para corregir las vulnerabilidades aprovechadas por Operation Triangulation.

Entre julio y agosto de 2023, varias organizaciones gubernamentales y comerciales de Rusia prohibieron el uso de dispositivos Apple para fines oficiales, entre ellas el Ministerio de Desarrollo Digital, el Ministerio de Industria y Comercio, el Ministerio de Transporte, el Servicio Federal de Impuestos, y el servicio de Ferrocarriles de Rusia. Un tiempo más adelante, el Banco Central y el Ministerio de Situaciones de Emergencia de Rusia adoptaron la misma medida.

En la misma línea, en septiembre de 2023, el gobierno chino expandió la prohibición del uso de iPhones para empleados de empresas estatales.

Por su parte, en 2024, el Ministerio de Defensa de Corea del Sur anunció la prohibición de móviles iPhone por motivos de seguridad, sin afectar el uso de móviles con Android.

 Repercusión y opinión pública
El código utilizado por Operation Triangulation ha sido calificado como el más complejo de la historia.

Lo qué más llama la atención del ataque es que quienes lo perpetraron conocían las funciones no documentadas de los chips de Apple y que utilizaron cuatro vulnerabilidades de día cero en un mismo ataque.

Entre las opiniones que más trascendieron, destacan la del criptógrafo Bruce Schneier, quien describió el ataque como "absurdamente sofisticado" y un "asunto de nivel estatal", y la de Elon Musk, quien mostró interés por la complejidad del ataque y las posibles maneras de defenderse.

 Referencias
