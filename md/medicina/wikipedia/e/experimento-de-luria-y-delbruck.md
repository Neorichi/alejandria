---
type: Artículo de enciclopedia
title: Experimento de Luria y Delbrück
description: El experimento llamado test de fluctuación, demuestra que en bacterias, las mutaciones genéticas se producen en ausencia de selección, en lugar de producirse como respuesta a la selección.
resource: https://es.wikipedia.org/wiki/Experimento_de_Luria_y_Delbrück
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Experimento_de_Luria_y_Delbrück"}
license: CC BY-SA 4.0
id: eswiki-Experimento_de_Luria_y_Delbrück
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Experimento de Luria y Delbrück

El experimento llamado **test de fluctuación**, demuestra que en bacterias, las mutaciones genéticas se producen en ausencia de selección, en lugar de producirse como respuesta a la selección. Por lo tanto, la teoría de la selección natural de Darwin que actúa sobre mutaciones aleatorias puede también aplicarse sobre las bacterias y otros organismos más complejos. Max Delbrück y Salvador Luria ganaron en 1969 el Premio Nobel en Fisiología o Medicina en parte por este trabajo.

 Historia
Hacia la década de 1940 los conceptos de herencia y mutación estaban generalmente aceptados, aunque el papel del ADN como material hereditario aún no había sido establecido. Se creía que las bacterias eran de algún modo diferentes y que podían desarrollar mutaciones genéticas heredables dependiendo de las condiciones en las que se encontraran. Estos interrogantes podrían resumirse en la pregunta: ¿las mutaciones en bacterias son pre-adaptativas (preexistentes) o post-adaptativas (adaptación directa)? Luria (PhD de James Watson) estaba obsesionado particularmente con esta idea, y se encontraba decidido a solucionarla. Se le ocurrió el experimento mientras observaba una máquina tragaperras durante un baile en la Universidad de Indiana.

En su experimento, Luria y Delbrück inocularon una pequeña cantidad de bacterias (*Escherichia coli*) en varios tubos de cultivo separados. Tras un período de crecimiento, sembraron volúmenes iguales de estos cultivos en agar que contenía el fago T1 (virus). Si la resistencia al virus en las bacterias se encontraba causada por una activación inducida en bacterias, esto es, si la resistencia no estaba provocada por componentes genéticos heredables, entonces cada placa debería contener aproximadamente el mismo número de colonias resistentes. Suponiendo una frecuencia de mutación constante, la hipótesis de Luria era que si las mutaciones ocurrían después y en respuesta a la exposición al agente selectivo, el número de supervivientes se distribuiría en acorde a una distribución de Poisson con la media equivalente a la varianza. Esto no fue lo que Luria y Delbrück encontraron: en lugar de lo esperado por la hipótesis, el número de colonias resistentes variaba drásticamente según la placa: la variancia era considerablemente mayor a la media.

Luria y Delbrück propusieron que aquellos resultados podían explicarse por la existencia de una tasa constante de mutaciones en cada generación de bacterias creciendo en los tubos de cultivo iniciales. Basado en esas suposiciones, Delbrück ideó una distribución de probabilidad (ahora llamada distribución de Luria-Delbrück) que relacionaba los resultados obtenidos de manera consistente. La distribución que sigue los resultados que se esperaban en la hipótesis (la distribución de Poisson) predecía resultados inconsistentes con los datos obtenidos. Por lo tanto, la conclusión fue que las mutaciones en bacterias, así como en otros organismos, son más bien aleatorias que dirigidas.

Los resultados de Luria y Delbrück fueron confirmados de un modo más gráfico pero menos cuantitativo por Newcombe. Newcombe incubó bacterias en una placa de Petri durante pocas horas, y después la replicó en placa sobre otras dos nuevas placas de Petri tratadas con fago. La primera placa permaneció sin expandirse, mientras que la segunda se extendió, es decir, las células bacterianas fueron desplazadas permitiendo que algunas células en ciertas colonias formaran sus propias nuevas colonias. Si las colonias contenían células bacterianas resistentes antes de entrar en contacto con el virus fago, uno esperaría que algunas de esas células formaran nuevas colonias resistentes sobre la placa re-extendida para encontrar un número más alto de bacterias supervivientes en ella. Cuando ambas placas fueron incubadas para el crecimiento, había de hecho 50 veces más colonias bacterias en la placa re-extendida. Esto mostraba que las mutaciones bacterianas que aportaban resistencia al virus se habían producido de manera aleatoria durante la primera incubación. Una vez más, las mutaciones tuvieron lugar antes de que la selección fuera aplicada.

Más recientemente, los resultados de Luria y Delbrück fueron cuestionados por Cairns y otros, que estudiaban mutaciones en el metabolismo de azúcares como una forma de estrés medioambiental. Algunos científicos sugieren que este resultado puede haber sido provocado por selección para amplificación de genes y/o una frecuencia de mutación más alta en células incapaces de dividirse. Otros han defendido el experimento y proponen mecanismos que cuentan que el fenómeno observado es consistente con la mutagénesis adaptativa.

Esta distribución fue determinada por primera vez por Haldane. Un manuscrito no publicado fue descubierto en 1991 en la University College de Londres en el que se describía esta distribución. La derivación es distinta, pero los resultados son difíciles de computar sin la ayuda de una computadora.

 Descripción del test
Una pequeña cantidad de células son usadas para inocular cultivos paralelos en un medio no selectivo. Los cultivos son crecidos hasta la saturación para obtener densidades celulares equitativas. Las células son plantadas sobre medio selectivo para obtener un número de mutantes ( *r* ). Las diluciones son plantadas sobre medio enriquecido para calcular el número total de células viables ( *N*t ). El número de mutantes que aparece en el cultivo saturado es una medida tanto de la tasa de mutación como de cuándo aumenta el número de mutantes durante el crecimiento del cultivo: los mutantes que aparezcan pronto durante el crecimiento del cultivo propagarán muchos más mutantes que aquellos que salgan más tarde durante el crecimiento del cultivo. Esos factores provocan que la frecuencia ( *r* / *N*t ) varíe considerablemente, incluso si el número de sucesos mutacionales ( *m* ) es el mismo. La frecuencia no es una medida suficientemente precisa de la mutación y la tasa de mutación ( *m* / *N*t ) debería ser siempre calculada.

La estimación de la tasa de mutación ( *m* ) es compleja. Luria y Delbrück estudiaron estimaron este parámetro a partir de la media de la distribución pero este estimador se mostró posteriormente parcial. El método de la mediana fue introducido en 1949. Este método se basa en la ecuación

Este método ha sido mejorado desde entonces, pero los nuevos métodos mejorados son complejos. El estimador de máxima verosimilitud Ma-Sandri-Sarkar es por el momento el estimador mejor conocido. Varios métodos y estimaciones adicionales han sido descritos.

Dos aplicaciones web para el cálculo de la tasa de mutación están disponibles gratuitamente: Falcor y bz-rates. Bz-rates implementa una versión generalizada del estimador de máxima verosimilitud Ma-Sandri-Sarkar que puede cuantificar la tasa de crecimiento diferencial relativo entre células mutantes y células salvajes así como un estimador generado por función que puede estimar tanto la tasa de mutación como la tasa de crecimiento diferencial. Un ejemplo por Jones et al. se muestra en este artículo.

 Distribución

En todos estos modelos la tasa de mutación (*µ*) i la tasa de crecimiento (*β*) se supone que son constantes. El modelo puede ser fácilmente generalizado para relajar esas y otras restricciones. Estas tasas tienden a diferir en condiciones no experimentales. Los modelos también requieren que *N**t* *m* >> 0, donde *N**t* es el número total de organismos. Esta suposición es probable que se cumplan en la mayoría de situaciones realistas o experimentales.

Luria y Delbrück estimaron la tasa de mutación a partir de la ecuación

Donde *β* es la tasa de crecimiento celular, *n*0 es el número inicial de bacterias en cada cultivo, t es el tiempo, y

Donde  es el número de cultivos sin bacterias resistentes y  es el número total de cultivos.

El modelo de Lea y Coulson difería del original en que ellos consideraban una colección de procesos de nacimiento y muerte independientes (un proceso de Poisson filtrado). Comparaciones numéricas de estos dos modelos con valores realistas de los parámetros se han mostrado que difieren sólo ligeramente. La función generadora para este modelo fue encontrada por Barlett en 1978 y es

Donde *µ* es la tasa de mutación (supuesta de ser constante),  con *β* como la tasa de crecimiento celular (también supuesta de ser constante) y *t* es el tiempo.

La determinación de *µ* a partir de esta ecuación se ha comprobado que es difícil, pero una solución fue descubierta en 2005. La diferenciación de la función generadora respecto a *µ* permite la aplicación del método de Newton-Raphson que junto con el uso de una función score permite la obtención de intervalos de confianza para *µ*.

 Biología molecular

El mecanismo de resistencia al fago T1 es debido a mutaciones en el gen *fhu*A, una proteína de membrana que actúa como receptor de T1. El producto del gen *ton*B también es requerido para la infección por T1. La proteína FhuA está implicada activamente en el transporte de ferricromo, albomicina y rifamicina. También confiere sensibilidad a microcina J25 y colicina M y actúa como receptor para los fagos T5 y phi80, así como T1.

La proteína FhuA tiene un dominio beta-barril (residuos 161 a 714) que se cierra por un dominio globular (residuos 1 a 160). Dentro del domino globular se encuentra la región de unión a TonB (residuos 7 a 11). La gran membrana que se extiende por los dominios barril β monoméricos tiene 22 láminas β de longitud variable, varias de las cuales se extienden más allá del núcleo hidrofóbico de la membrana, por el espacio extracelular. Existen 11 giros extracelulares numerados de L1 a L11.  El giro L4 es al que se une el fago T1.

 Referencias

Enlaces externos
 On Mutation lab
 Profiles in Science: The Salvador E. Luria Papers Información sobre Salvador Luria proveniente del National Library of Medicine
