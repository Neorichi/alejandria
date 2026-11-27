---
type: Artículo de enciclopedia
title: Equation Group
description: "The Equation Group, clasificado como una amenaza persistente avanzada, es un actor de amenazas altamente sofisticado sospechoso de estar vinculado a la unidad de Operaciones de Acceso a la medida (TAO por sus siglas en …"
resource: https://es.wikipedia.org/wiki/Equation_Group
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Equation_Group"}
license: CC BY-SA 4.0
id: eswiki-Equation_Group
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Equation Group

- **Nombre:** Equation Group
- **Tipo:** Amenaza persistente avanzada
- **Productos:** Stuxnet, Flame, EternalBlue

The **Equation Group**, clasificado como una amenaza persistente avanzada, es un actor de amenazas altamente sofisticado sospechoso de estar vinculado a la unidad de Operaciones de Acceso a la medida (TAO por sus siglas en inglés) de la Agencia de Seguridad Nacional (NSA) de los Estados Unidos . Kaspersky Labs los describe como uno de los grupos de ciberataques más sofisticados del mundo y "los más avanzados... que hemos visto", operando junto a los creadores de Stuxnet y Flame . La mayoría de sus objetivos han estado en Irán, Rusia, Pakistán, Afganistán, India, Siria y Malí .

El nombre se originó por uso extensivo de cifrado que el grupo hacía. En 2015, Kaspersky documentó 500 infecciones de malware por parte del grupo en al menos 42 países, aunque reconoció que el número real podría ser de decenas de miles debido a su protocolo de autodestrucción.

En 2017, WikiLeaks publicó una discusión en el seno de la CIA sobre cómo había sido posible identificar al grupo. Un comentarista escribió que "Equation Group, tal como está etiquetado en el informe, no se relaciona con un grupo específico sino con una colección de herramientas" utilizadas para hackear.

 Descubrimiento
En la Cumbre de Analistas de Kaspersky Security celebrada en México el 16 de febrero de 2015, Kaspersky Lab anunció el descubrimiento de Equation Group. Según el informe de Kaspersky Lab, el grupo ha estado activo desde al menos 2001, con más de 60 actores. El malware utilizado en sus operaciones, denominado EquationDrug y GrayFish, es capaz de reprogramar el firmware de los discos duros . Debido a las técnicas avanzadas involucradas y al alto grado de encubrimiento, se sospecha que el grupo tiene vínculos con la NSA, pero Kaspersky Lab no ha identificado a los actores detrás del grupo.

 Vínculos probables con Stuxnet y la NSA
En 2015, los hallazgos de la investigación de Kaspersky sobre Equation Group señalaron que su cargador, "Grayfish", tenía similitudes con un cargador descubierto anteriormente, "Gauss",  de otra serie de ataques, y señaló por separado que Equation Group usaba dos ataques de día cero. ataques utilizados posteriormente en Stuxnet ; los investigadores concluyeron que "el tipo similar de uso de ambos exploits juntos en diferentes gusanos informáticos, aproximadamente al mismo tiempo, indica que el grupo EQUATION y los desarrolladores de Stuxnet son los mismos o trabajan en estrecha colaboración".

 Firmware
También identificaron que la plataforma se había difundido en ocasiones por interdicción (interceptación de CD legítimos enviados por un organizador de congresos científicos por correo ), y que la plataforma tenía la capacidad "sin precedentes" de infectar y transmitirse a través del firmware del disco duro de varios de los principales fabricantes de discos duros, y de crear y utilizar áreas de disco ocultas y sistemas de disco virtual para sus propósitos, una proeza que para lograrse requeriría de acceso al código fuente del fabricante, y que la herramienta fue diseñada para precisión quirúrgica, yendo tan lejos como para excluir países específicos por IP y marcar como objetivos a nombres de usuario específicos en foros de internet .

 Palabras clave y marcas de tiempo
Las palabras clave de la NSA "STRAITACID" y "STRAITSHOOTER" se han encontrado dentro del malware. Además, las marcas de tiempo en el malware parecen indicar que los programadores trabajaron abrumadoramente de lunes a viernes en lo que correspondería a un día laboral de 08:00 a 17:00 (8:00 a. m. a 5:00 p. m.) en una zona horaria del este de los Estados Unidos. .

 El exploit LNK
El equipo global de investigación y análisis de Kaspersky, también conocido como GReAT, afirmó haber encontrado una pieza de malware que contenía "privLib" de Stuxnet en 2008. Específicamente contenía el exploit LNK encontrado en Stuxnet en 2010. Fanny se clasifica como un gusano que afecta a determinados sistemas operativos Windows e intenta propagarse lateralmente a través de una conexión de red o almacenamiento USB .  Kaspersky declaró que sospecha que Equation Group existe desde antes que Stuxnet, según el tiempo de compilación registrado de Fanny.

 Enlace con IRATEMONK
F-Secure afirma que el firmware malicioso del disco duro de Equation Group es el programa TAO "IRATEMONK", uno de los elementos del catálogo NSA ANT expuesto en un artículo de *Der Spiegel* de 2013. IRATEMONK brinda al atacante la capacidad de tener su aplicación de software instalada de manera persistente en ordenadores de escritorio y portátiles, aunque se formatee el disco, se borren sus datos o se reinstale el sistema operativo. Infecta el firmware del disco duro, que a su vez agrega instrucciones al registro de inicio maestro del disco que hace que el software se instale cada vez que se inicia el ordenador. Es capaz de infectar ciertos discos duros de Seagate, Maxtor, Western Digital, Samsung, IBM, Micron Technology y Toshiba.

 2016 la brecha de Equation Group
En agosto de 2016, un grupo de hackers autodenominado " The Shadow Brokers " anunció que había robado código de Equation Group. Kaspersky Lab notó similitudes entre el código robado y el código conocido anterior de las muestras de malware de Equation Group que tenía en su poder, incluidas peculiaridades exclusivas de la forma en que Equation Group implementa el algoritmo de cifrado RC6 y, por lo tanto, concluyó que el anuncio era legítimo. Las fechas más recientes de los archivos robados son de junio de 2013, lo que llevó a Edward Snowden a especular que un posible bloqueo resultante de su filtración de los esfuerzos de vigilancia global y nacional de la NSA detuvo la violación de Equation Group por parte de The Shadow Brokers. Los exploits contra Cisco Adaptive Security Appliances y los firewalls de Fortinet se presentaron en algunas muestras de malware publicadas por The Shadow Brokers. EXTRABACON, un exploit de Simple Network Management Protocol contra el software ASA de Cisco, era un exploit de día cero en el momento del anuncio. Juniper también confirmó que sus firewalls NetScreen se vieron afectados. El exploit EternalBlue se utilizó para llevar a cabo el dañino ataque de ransomware WannaCry en todo el mundo.

 Referencias

 Enlaces externos

 *Grupo de ecuaciones: preguntas y respuestas* de Kaspersky Lab, versión: 1.5, febrero de 2015
 Una ecuación de Fanny: "Soy tu padre, Stuxnet" de Kaspersky Lab, febrero de 2015

 fuente fanny.bmp - en GitHub, 30 de noviembre de 2020

 Redacción técnica: en GitHub, 10 de febrero de 2021
