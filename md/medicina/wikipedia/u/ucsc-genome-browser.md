---
type: Artículo de enciclopedia
title: UCSC Genome Browser
description: El UCSC Genome Browser es un navegador genómico en línea y descargable, alojado por la Universidad de California, Santa Cruz (UCSC).
resource: https://es.wikipedia.org/wiki/UCSC_Genome_Browser
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/UCSC_Genome_Browser"}
license: CC BY-SA 4.0
id: eswiki-UCSC_Genome_Browser
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# UCSC Genome Browser

- **Tipo:** Base de datos y navegador genómico en línea
- **Sede central:** Universidad de California en Santa Cruz
- **Referencias:** Navarro González & al. (2021)

El **UCSC Genome Browser** es un navegador genómico en línea y descargable, alojado por la Universidad de California, Santa Cruz (UCSC). Es un sitio web interactivo que ofrece acceso a datos de secuencias genómicas de múltiples especies de vertebrados e invertebrados y principales organismos modelo, integrados en una amplia colección de secuencias anotadas. El navegador es un visor gráfico optimizado para un uso rápido e interactivo y es de código abierto, diseñado sobre una base de datos MySQL para una visualización, examen y consulta de datos rápida y a varios niveles. Toda la información relativa a la base de datos, herramientas del navegador, archivos descargables y bibliografía se puede encontrar  en el sitio web del grupo de Bioinformática y Genómica de la UCSC.

 Historia
El UCSC Genome Browser comenzó a funcionar en el año 2000 como un recurso para la distribución de los primeros resultados extraídos del Proyecto Genoma Humano, siendo diseñado y mantenido por el estudiante Jim Kent y el profesor de Ciencias de la computación David Haussler de la Universidad de California, Santa Cruz. Fue fundado por el Instituto Médico Howard Hughes y el Instituto Nacional de Investigación del Genoma Humano (NHGRI), uno de los Institutos de Salud de los EE. UU. (NIH). En sus comienzos, el navegador solo mostraba la secuencia ensamblada del primer cromosoma secuenciado del genoma humano. Actualmente, tanto genetistas, biólogos moleculares, médicos, como estudiantes y profesores acceden a la información contenida en este navegador.

 Genomas
Desde su fundación, el navegador se ha expandido añadiendo genomas de todos los vertebrados e invertebrados para los cuales existe secuencias con alta cobertura, incluyendo actualmente genomas de 108 especies . Una alta cobertura es necesaria para el ensamblado de las diferentes secuencias de regiones contiguas. Las secuencias con una menor cobertura se incluyen como alineamientos múltiples en algunos navegadores aunque el estado fragmentado de estos ensamblados los vuelve inapropiados para todos los navegadores genómicos. En la siguiente tabla se muestran los organismos cuyo genoma está disponible en el UCSC Genome Browser.

Además de estas 108 especies y sus genomas, el UCSC Genome Browser también ofrece la herramienta *Assembly hubs*, un conjunto de directorios en línea con datos genómicos que pueden ser visualizados en el navegador e incluyen genomas que no están incluidos nativamente en la base de datos de la UCSC. Los usuarios pueden subir y anotar genomas únicos, para los cuales la UCSC no ofrece datos de anotación. Se puede consultar una lista completa de especies y sus genomas en el portal GenArk, incluyendo hasta 2 589 genomas compartidos entre las bases de datos de UCSC Genome Browser y *Assembly Hubs*. Un ejemplo disponible en la plataforma es el Proyecto de Genomas de Vertebrados.

 Funcionalidades
La producción actual de datos masivos de sistemas biológicos en la bibliografía científica hace necesario el uso de herramientas bioinformáticas para su colección y análisis. El UCSC Genome Browser ofrece una amplia colección de conjuntos de datos anotados, denominados *tracks* y presentados visualmente, los cuales incluyen alineamientos de ARNm, secuencias de elementos repetitivos en ADN, predicción de genes, datos de expresión génica, datos de asociación gen-enfermedad y secuencias de chips de genes disponibles en el mercado (ej.: Illumina y Agilent). La visualización de datos en el navegador se basa en mostrar las secuencias genómicas horizontalmente, indicando las representaciones gráficas y localización de los ARNm, genes etc. A lo largo del eje de coordenadas, hay bloques de colores indicando la localización de los alineamiento de diferentes tipos de datos. La capacidad del navegador para mostrar una gran variedad de datos de manera compacta y fácil de visualizar lo convierte en una herramienta muy útil para la integración de datos.

Para localizar una región o gen concretos, el usuario puede buscar por nombre, secuencia de ADN, un identificador específico de ARN, el nombre de una banda citológica (ej.: 20p13 para la banda 13 en el brazo corto del cromosoma 20), o por posición en un cromosoma (ej.: chr17:38,450,000-38,531,000 para buscar la región en torno al gen BRCA1).

El navegador también ofrece enlaces para acceder a información más detallada sobre la anotación de cualquier región. La sección de detalles en el *track* *Genes* ofrece una gran cantidad de enlaces a información específica sobre genes extraída de otras bases de datos, como OMIM y SwissProt.

A su vez, el navegador también está optimizado para un acceso de alta velocidad de los datos. Por ejemplo, es posible tener un acceso directo a los alineamiento de cualquier ARN con cualquiera de las especies disponibles mediante el pre-alineamiento de millones de secuencias de ARN procedentes de GenBank contra cada uno de los 244 genomas disponibles (muchas de las 108 especies tienen más de una versión de su genoma).

La yuxtaposición de múltiples tipos de datos permite a los investigadores visualizar la combinación de datos exacta que puede responder a sus consultas. Es posible exportar la información en formato imagen pdf/postscript para publicación en revistas científicas.

Una funcionalidad única y útil que distingue al UCSC Genome Browser de otros navegadores genómicos es la gran flexibilidad y variedad de maneras de visualización de datos. Cualquier secuencia de cualquier longitud se puede visualizar, desde un único nucleótido de ADN hasta un cromosoma completo con sus respectivos *tracks* de anotación biológica (ej.: el cromosoma 1 humano tiene una longitud de 245 millones de bases, Mb). Los investigadores pueden seleccionar un solo gen, un exón o una banda cromosómica, mostrando docenas o cientos de genes con cualquier combinación de *tracks* disponibles. Se puede aumentar/reducir el zum hasta en pantalla completa, así como arrastrar las coordenadas a diferentes regiones en el genoma.

Otra funcionalidad útil para los investigadores es la posibilidad de subir sus propios conjuntos de datos al navegador mediante la herramienta *Custom Tracks*. Esta permite customizar la información con datos propios en el contexto de un genoma de referencia. Los usuarios también pueden utilizar los datos contenidos por la UCSC, creando subconjuntos de datos que sean de interés mediante la herramienta *Table Browser* (por ejemplo, los SNPs que cambian la secuencia de aminoácidos de una proteína) y mostrarlos de manera personalizada como *Custom Tracks*.

Cualquier visualización de datos creada por los usuarios, incluidos los *Custom Tracks*, pueden ser compartidos con otros usuarios mediante la herramienta *Saved Sessions*.

 *Tracks*

En las imágenes se puede ver todas las categorías de *tracks* adicionales disponibles en el navegador, los cuales se pueden colocar en paralelo a los datos originales del navegador. Estas categorías son: mapeado y secuenciación, genes y predicción de genes, fenotipo y bibliografía, ARNm y EST, expresión génica, regulación, genómica comparativa, variación genética y repeticiones.

 Herramientas de análisis
El sitio web también ofrece herramientas de análisis genómicos, incluyendo una interfaz gráfica completa para buscar información en el navegador, la herramienta BLAT para alineamientos múltiples de secuencias formato FASTA contra cualquiera de las secuencias masivas de los genomas guardados en la base de datos (ej.: genoma humano = 3 230 millones de bases (Gb)).

La herramienta *LiftOver* permite la conversión entre diferentes versiones de un genoma de referencia de una especie o incluso entre especies. La herramienta *Genome Graphs* permite a los usuarios visualizar todos los cromosomas a la vez y ver los resultados de estudios de GWAS. El *Gene Sorter* muestra genes agrupados por parámetros no asociados a la localización en el genoma, por ejemplo: los patrones de expresión en tejidos.

 Acceso libre / espejos
El navegador es de código y acceso libre, sin uso comercial, y tiene sitios web espejos locales para múltiples grupos de investigación, permitiendo la visualización privada de los datos públicos. El UCSC Genome Browser tiene dos sitios web espejo a nivel mundial, mostrados en la tabla.

El código del navegador también se utiliza en instalaciones separadas por otros navegadores genómicos, el UCSC Malaria Genome Browser y el Archaea Browser.

 Véase también

 Ensembl
 ENCODE

 Referencias
