---
type: Artículo de enciclopedia
title: Detección automática de fraude
description: La detección automática de fraude es el proceso de descubrir fraude utilizando máquinas, comúnmente computadoras con software diseñado específicamente para esto.
resource: https://es.wikipedia.org/wiki/Detección_automática_de_fraude
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Detección_automática_de_fraude"}
license: CC BY-SA 4.0
id: eswiki-Detección_automática_de_fraude
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Detección automática de fraude

La **detección automática de fraude** es el proceso de descubrir fraude utilizando máquinas, comúnmente computadoras con software diseñado específicamente para esto. Es uno de los medios más utilizados para la detección de fraude en la actualidad, debido a que los volúmenes de información a ser analizados por los analistas de las compañías encargados de detectar posibles estafas son demasiado grandes, haciéndose indispensable la asistencia de software capaz de efectuar minería de datos y extracción de conocimiento para obtener información relevante.

Impacto del fraude
Anualmente las empresas, gobiernos y personas en general experimentan pérdidas millonarias a nivel mundial como producto del fraude. Solo en los Estados Unidos en el 2004 se estimaron pérdidas de 264 000 millones de dólares por causa del fraude, de todos los sectores el que más pérdidas presentó fue el de las telecomunicaciones 150 000 millones, seguido por las aseguradoras con 67 000 millones y después están las pérdidas causadas por el lavado de dinero que fueron de 40 000 millones.
Los tipos de fraude son muy diversos, puesto que abarca prácticamente cualquier tipo de engaño o estafa, algunos de los más comunes son:
El **fraude de identidad** que es cuando un usuario deshonesto que ha cometido algún abuso en la utilización de un servicio, lo solicita nuevamente bajo una identidad falsa, ejemplo son los servicios de telefonía donde en el contrato del servicio se entrega un nombre y una dirección falsa por lo que nunca se paga la factura y cuando se le cancela el servicio, abre otro contrato con otra identidad, esto también es un ejemplo del **fraude de suscripción**.
El fraude contra las aseguradoras es aquel en el cual se le hace creer a las compañías aseguradoras que los daños recibidos por el objeto del seguro fueron mayores que los reales, entre otros.
En **subastas en línea** los estafadores suelen crear una cuenta con la que se va a realizar la falsa venta y varias cuentas cómplices para que lo califiquen como un vendedor confiable y cuando el cliente ha pagado entonces nunca le envían su compra.

Técnicas para la detección automática de fraude
La primera industria en utilizar técnicas para la prevención del fraude fueron las compañías telefónicas, las compañías de seguro y los bancos. Uno de los primeros ejemplos de aplicación exitosa de técnicas para el análisis de los datos en la industria bancaria fue el sistema para el asesoramiento contra el fraude Falcon, el cual está basado en una red neuronal.

El fraude en las transacciones comerciales en internet, ha surgido recientemente como una gran preocupación puesto que el fraude en ellas es 12 veces mayor que en las realizadas en las tiendas. Las estafas que implican teléfonos móviles, pólizas de seguro, declaraciones de impuestos, transacciones de tarjetas de crédito, etc. representan un gran problema para los negocios y los gobiernos, pero detectarlos y prevenirlos no es tarea fácil en la actualidad, puesto que el fraude es un crimen adaptativo, por lo tanto necesita métodos de detección especialmente inteligentes para detectarlo. Estos métodos se encuentran fundamentalmente en las áreas de la extracción de conocimientos en bases de datos (KDD), la minería de datos, el aprendizaje automático y la estadística. Ellos ofrecen soluciones aplicables y exitosas en la lucha contra el fraude en distintas áreas.

Las técnicas utilizadas para la detección de fraude se dividen en dos clases principales: técnicas estadísticas e inteligencia artificial.

Técnicas estadísticas
Ejemplos de técnicas estadísticas de análisis de datos son:
Técnicas de procesamiento de datos para la detección, validación, corrección de errores y completamiento de datos perdidos o incorrectos.
Cálculo de varios parámetros estadísticos como promedios, percentiles, métricas de rendimiento, distribuciones probabilísticas, y otras. Por ejemplo los promedios pueden incluir la duración promedio de llamadas telefónicas, el promedio de la cantidad de llamadas por mes y el de los retrasos al pagar las facturas.
Modelos y distribuciones de probabilidad de varias actividades de negocios, ambos en función de varios parámetros o distribuciones probabilísticas.
Perfiles computarizados de los usuarios.
Análisis de series de datos contra tiempo cuando este resulta relevante para los mismos.
Clasificación y agrupamiento de los datos para encontrar patrones y asociaciones entre los grupos.
Algoritmos de emparejamiento para detectar anomalías en el comportamiento de las transacciones o los usuarios al compararlos con los perfiles previamente creados.
También son necesarias técnicas para eliminar falsas alarmas, estimar los riesgos y predecir el comportamiento futuro de las transacciones y usuarios actuales.

Técnicas de inteligencia artificial
El manejo del fraude es una actividad que requiere un uso intensivo del conocimiento. Las principales técnicas de Inteligencia artificial utilizadas para ello son:

Minería de datos para clasificar, agrupar y segmentar los datos y de modo automático encontrar asociaciones y regularidades en los datos que puedan representar patrones interesantes, incluidos aquellos relacionados con el fraude.
Sistemas expertos que expresan la experiencia en la detección de fraude en forma de reglas.
Reconocimiento de patrones para detectar de forma aproximada clases, grupos o patrones con comportamiento sospechosos, esto puede hacerlo de forma completamente automática (utilizando aprendizaje no supervisado) o comparando con un conjunto entrenante inicial (aprendizaje supervisado).
Técnicas de Aprendizaje automático para identificar características propias del fraude.
Redes neuronales capaces de aprender patrones sospechosos a partir de ejemplos y utilizarlos después para su detección.

Utilización de las características sociales del fraude
El fraude es, en muchos casos, un fenómeno social y por lo tanto la detección del mismo se puede beneficiar grandemente de analizar las relaciones de los usuarios, detectando patrones en las interacciones que se repitan de un usuario fraudulento al otro, este análisis es de especial utilidad en escenarios donde los estafadores utilizan cómplices para sus estafas y es muy importante para la detección del fraude de identidad.
Para este análisis se suele representar a los usuarios y sus relaciones mediante grafos. Las técnicas más utilizadas para detectar a los usuarios fraudulentos en estos modelos son las **Redes Bayesianas** y los **Modelos Ocultos de Markov**, debido a su capacidad de manejar incertidumbre y ofrecer una probabilidad de que se haya detectado fraude o no.

Aplicaciones
La detección automática de fraude está integrada en muchas áreas de la vida cotidiana, se utilizan sistemas de este tipo para evitar:
El fraude telefónico, basándose en la duración de las llamadas, el costo de las mismas, los números a los que se llama y la comparación de los perfiles con los de conocidos usuarios fraudulentos.
Estafas en ventas en línea, utiliza sobre todo información de las relaciones con otros usuarios pues muchas veces los estafadores crean cuentas falsas que utilizan como cómplices para aumentar su confiabilidad como vendedor en esa red, pero después de cometer una estafa y abandonar una identidad suelen reutilizar las cuentas cómplices para la siguiente, por lo tanto esto se usa para su detección.
El fraude contra las compañías aseguradores dada su naturaleza variada obliga a la combinación de múltiples métodos de detección, los cuales van desde sistemas basados en reglas, análisis de relaciones de los implicados en la investigación hasta reconocimiento de patrones en el texto de documentos.
Muchos otros tipos de fraude.

Es importante señalar que la detección automática de fraude no pretende eliminar el trabajo de los analistas humanos, sino eliminar la información superflua y resaltar los datos que podrían ser de utilidad, así como los casos donde es más probable que se haya cometido fraude, pero en la mayoría de los casos la decisión es tomada en última instancia por los analistas humanos.

Véase también
 Fraude
 Minería de datos
 Red neuronal artificial
 Inteligencia artificial
 Reconocimiento de patrones
 Algoritmo de agrupamiento
 Estadística
 Red bayesiana

Referencias
