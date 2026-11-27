---
type: Artículo de enciclopedia
title: Radioterapia conformada en tres dimensiones
description: "La radioterapia conformada tridimensional (RT3D) es la forma de radioterapia externa en la que el haz de radiación se ajusta al volumen de tratamiento delimitado en imágenes obtenidas en un simulador de tomografía axial …"
resource: https://es.wikipedia.org/wiki/Radioterapia_conformada_en_tres_dimensiones
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Radioterapia_conformada_en_tres_dimensiones"}
license: CC BY-SA 4.0
id: eswiki-Radioterapia_conformada_en_tres_dimensiones
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Radioterapia conformada en tres dimensiones

La **radioterapia conformada tridimensional  (RT3D**) es la forma de radioterapia externa en la que el haz de radiación se ajusta al volumen de tratamiento delimitado en imágenes obtenidas en un simulador de tomografía axial computarizada (TAC).

La planificación del tratamiento con radioterapia ha cambiado a partir de 1970 por la capacidad de delimitar tumores y estructuras normales adyacentes en tres dimensiones utilizando escáneres de TAC y / o RMN y programas informáticos especializados en planificación de radioterapia.

Cuando el volumen de tratamiento se adapta a la forma del tumor, se reduce la toxicidad de la radiación a los tejidos normales adyacentes, lo que permite administrar una dosis de radiación más alta al tumor que la que permitirían las técnicas convencionales (**RT2D**), donde las estructuras de los tejidos blandos son a menudo difíciles de evaluar en radiografías convencionales y los tejidos normales difíciles de proteger.

La planificación tridimensional de la RT3D o **simulación virtua**l se basa en el uso de radiografías reconstruidas y generadas por computadora y el cálculo volumétrico de dosis para administrar un haz externo de forma precisa y discriminatoria de radiación.

 Requisitos tecnológicos de la RT3D
El avance de la RT3D con respecto a la técnica bidimensional (RT2D) requiere la integración de una serie de complejos procesos tecnológicos

 Simulación con tomografía axial computarizada (TAC)

También llamado TAC de planificación que se suele fusionar con otras técnicas de imagen diagnósticas como la resonancia magnética nuclear o la tomografía por emisión de positrones.

El TAC de simulación es un TAC similar a los de radiodiagnóstico con tres particularidades: El anillo (*gantry*) por el que pasa el paciente es más amplio que el de TAC diagnóstico, la camilla sobre la que se acuesta el paciente es plana, dura y de las mismas características que la mesa de tratamiento del acelerador lineal y la habitación donde se realiza el TAC de simulación dispone de unos láseres de posición o alineamiento (sagital y laterales).

El TAC de simulación se realiza según el protocolo de cada localización tumoral que describe lacomo decúbito supino, prono o lateral, posición de los brazos y las piernas, inmovilización de parte o todo el paciente mediante dispositivos específicos que se anclan a la mesa del TAC y control de movimiento respiratorio como el TAC4D.

Es preciso colocar unas marcas radiopacas en la piel del paciente, generalmente esferas de plomo menores de 2 mm, en la intersección de los láseres de posición sobre la superficie del paciente, que tras la realización del TAC se suelen tatuar para ser visibles en la colocación del paciente al inicio y durante el tratamiento de forma exacta.

El TAC de simulación lo realizan los Técnicos Superiores de Radioterapia y dosimetría.

 Delimitación de los volúmenes de interés

Con el TAC de simulación se obtienen imágenes axiales de la parte del cuerpo donde se localiza el volumen de tratamiento. Las, *regions of interest* (ROI) se delinean o *contornean* en cada corte de TAC para poder reconstruirse tridimensionalmente. Los ROI pueden clasificarse en:

 **Órganos de riesgo**, *organ at risk* (OAR): Son los órganos, tejidos o estructuras anatómicas sanas que tienen un límite de dosis de radiación determinado, expresado como dosis máxima en un punto o a un volumen, como la médula espinal, el corazón, los pulmones. La delimitación de los órganos de riesgo lo realizan los técnicos de radioterapia supervisados por el Oncólogo Radioterápico basado en guías o atlas consensuadas internacionalmente.
 **Volúmenes blanco**: Son los volúmenes que contienen al tumor y se definen con exactitud en el reporte ICRU 50 y 62, que define el Oncólogo Radioterápico.
 **GTV**, *Gross tumor volum*e: Es el volumen macroscópico palpable o visible en la exploración física y demostrable en su localización y extensión en las pruebas de imagen diagnósticas que define el tumor, las adenopatías o las metástasis de una enfermedad oncológica.
 **CTV**, *Clinical target volume*:  Es el volumen de tejido que contiene el GTV demostrable y/o la enfermedad maligna subclínica microscópica que varía según la extensión, localización y tipo de cáncer. Existen guías de recomendación internacionales avaladas por las sociedades científicas de Oncología Radioterápica.
 **PTV**, *Planning target volume*: Es el **volumen de tratamiento** definido como el volumen que contiene al CTV más un margen de seguridad (*setup*) que depende de la precisión tecnológica de cada unidad o servicio de radioterapia. Es un concepto geométrico y se define para seleccionar los tamaños y configuraciones de los haces de radiación apropiados que asegura que en el CTV se absorba la dosis prescrita.

 Radiografías reconstruidas digitalmente (DRR) con visión del haz (BEV)

Con el TAC de planificación se obtienen(**DRR**, *Digital Reconstructed Radiograph*). Una DRR es una imagen radiográfica virtual de la proyección del haz de radiación sobre su eje, obtenida mediante algoritmos de procesado de imagen a partir de la información de los cortes axiales del TAC, y que representa energías de los fotones típicas del ámbito de radiodiagnóstico (80-120 KeV). Las DRR son generadas por el propio sistema de planificación. Es decir, a partir de la geometría del campo y de la anatomía del paciente se genera una imagen de proyección similar a una radiografía. Con los datos de la TAC se simula el proceso de generación de radiografías mediante diferentes métodos como atenuación del camino de diferentes rayos, o simulación Monte Carlo.

La(**BEV**, *Beam’s Eye View*) es la visualización de la posición y forma de la proyección de un haz de radiación determinado a la forma y posición del volumen de tratamiento (PTV) y de los órganos de riesgo (OARs). Es la vista en tres dimensiones del PTV y OARs según la visualización de un observador que estuviera ubicado en la fuente de radiación y que mirara hacia el isocentro.

Las DRRs son un elemento muy importante en el proceso de simulación virtual y verificación de la posición del paciente en radioterapia al compararlas con las imágenes reales obtenidas durante el tratamiento como las imágenes portales.

 Conformación de haz adaptado al volumen

La conformación del haz de radiación es una forma importante de reducir al mínimo la dosis absorbida en los tejidos sanos (OARs). En la radioterapia externa convencional (RT2D) los aceleradores lineales médicos disponían de colimadores secundarios (*jaws*) que sólo generaban campos de tratamiento rectangulares. Dado que los volúmenes de tratamiento no son rectangulares, la conformación del haz se realizaba con bloques individuales de *cerroben* que se colocaban debajo del colimador secundario. Los inconvenientes de estos bloques personalizados son múltiples: requieren mucho tiempo en su elaboración individual pues se debían fabricar tantos moldes como campos precisaba el tratamiento, ocupaban mucho espacio tanto en su elaboración como almacenamiento y sobre todo eran tóxicos por su composición al ser una aleación de plomo, cadmio, bismuto y estaño.
En la década de los 90 se diseñaron los colimadores multiláminas (CML, *multileaf collimator*), compuestos entre 40 y 160 láminas dispuestas a pares opuestos, que bloquean selectivamente el haz de radiación. Al poder controlar las láminas de forma remota y programada electrónicamente, se puede generar casi cualquier forma de campo complejo con buena precisión. Las ventajas del **colimador multiláminas** son: el menor tiempo en la preparación y ejecución del tratamiento, disminución del gasto en la elaboración de bloques individuales y eliminación de la toxicidad y accidentes provocados por el cerroben.

Con el desarrollo tecnológico y de los colimadores multiláminas surgió la forma avanzada de RT3D que es la Radioterapia de Intensidad Modulada (IMRT).
 Sistemas computarizados de planificación

La planificación computarizada  (**TPS**, *Treatment Planning System*) es una parte fundamental dentro del procedimiento de la radioterapia conformada tridimensional, que incluyen diversas aplicaciones complejas:

 El procesamiento de las imágenes del TAC de simulación con respecto al volumen de tratamiento, los volúmenes de tejido normal (OARs) y la superficie de los contornos del cuerpo del paciente.

 Corrección de heterogeneidad tisular: la densidad electrónica que compone cada tejido de la anatomía humana está estrechamente relacionada con la escala de grises o unidades Hounsfield que proporciona el TAC de simulación.

 Producción de radiografías digitales reconstruidas (DRR).

 Diseño de los ángulos del haz de radiación que se proyectan en el volumen (campos de tratamiento) que se visualizan en la proyección visual del haz (BEV) en lugar de emplear radiografías de simulación convencionales como en RT2D.

 Cálculo de las distribuciones relativas de dosis para cada acelerador lineal, energía en mega-voltios y modalidad de tratamiento

 Suma de las dosis relativas provenientes de los diferentes haces

 Prescripción de la dosis de radiación en un punto, en una, en una superficie de isodosis o un nivel de dosis en un histograma dosis volumen (HDV).

 Cálculo de las unidades del monitor (tiempo) para una determinada dosis prescrita, siempre y cuando hayan sido introducidos correctamente los datos de calibración en el sistema de planificación

 Datos de salida, que deben ser claros y precisos e incluir la distribución de isodosis en forma gráfica.

 Análisis de histograma de dosis-volumen (DVH)

Un  (DVH, *Dose-volume histogram*) es un gráfico de distribución de frecuencia de dosis acumulada con respecto al volumen, que resume gráficamente la distribución de la radiación simulada dentro de un volumen de interés de un paciente que resultaría de un determinado plan de tratamiento de radioterapia.

Los DVH son una herramienta útil para comparar diferentes planes de tratamiento en un paciente específico al mostrar claramente la uniformidad de la dosis en el volumen de tratamiento (PTV) y los puntos calientes o de alta dosis en los órganos o tejidos normales adyacentes (OAR). También puede estimar la probabilidad de control tumoral (TCP, *tumor control probability*) y la probabilidad de complicaciones en el tejido normal (NTCP, *normal tissue complication probability*).

Los DVH no proporcionan información posicional de los volúmenes considerados, debiendo recurrir a la visualización  de las curvas de isodosis en los diferentes planos del espacio que nos proporciona la simulación virtual en los cortes del TAC de planificación.

 Conexión de la computadora con el acelerador lineal

El acelerador lineal recibe todos los parámetros de la simulación virtual del plan de tratamiento aprobado conjuntamente por el radiofísico y el oncólogo radioterápico para la administración de la radiación. El día delo puesta en tratamiento se verifica con imágenes radiográficas la correcta posición del paciente para la localización exacta del volumen de tratamiento, al compararlas con las imágenes virtuales DDR.

Existen varios sistemas de verificación de imagen durante el tratamiento que aseguran la posición precisa del paciente para la correcta administración de la radiación. En la RT2D se utilizaban radiografías simples resistente a la radiación de megavoltaje, en la RT3D se implementan los dispositivos electrónicos de imagen portal (**EPID**, *electronic portal imaging devices*) que permiten ver el campo real de tratamiento de un paciente en el acelerador lineal sin la intervención de placas radiográficas, a través de una pantalla.

Los avances tecnológicos de los sistemas de verificación de imagen durante el tratamiento proporcionan seguridad en la administración de la radiación, surgiendo la Radioterapia Guiada por Imagen (**IGRT**, *Image-guided radiation therapy*), que junto con los avances en la RT3D, aparece en el  formas avanzadas de radioterapia como la Radioterapia de Intensidad modulada (IMRT)

 Referencias
