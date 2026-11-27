---
type: Artículo de enciclopedia
title: Aprendizaje automático antagónico
description: El aprendizaje automático antagónico (AAA) es el estudio de los ataques contra algoritmos de aprendizaje automático (AA) y de los mecanismos de defensa contra tales ataques.
resource: https://es.wikipedia.org/wiki/Aprendizaje_automático_antagónico
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Aprendizaje_automático_antagónico"}
license: CC BY-SA 4.0
id: eswiki-Aprendizaje_automático_antagónico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Aprendizaje automático antagónico

El **aprendizaje automático antagónico (AAA)** es el estudio de los ataques contra algoritmos de aprendizaje automático (AA) y de los mecanismos de defensa contra tales ataques. Una encuesta de mayo de 2020 revela que los expertos señalan la enorme necesidad de reforzar la protección de los sistemas de aprendizaje automático en los usos industriales.

Para entenderlo, hay que tener en cuenta que la mayoría de las técnicas de aprendizaje automático están diseñadas para funcionar en conjuntos de problemas específicos, suponiendo que los datos de formación y de prueba se generan a partir de la misma distribución estadística (IID). Sin embargo, este supuesto suele incumplirse peligrosamente en casos prácticos de alto riesgo, en los que los usuarios pueden suministrar intencionadamente datos falsos que incumplan el supuesto estadístico.

Algunos de los ataques más comunes en el aprendizaje automático antagónico son los ataques de evasión, los ataques de envenenamiento de datos, los ataques bizantinos y la extracción de modelos.

 Historia
En la Conferencia sobre Spam del MIT, celebrada en enero de 2004, John Graham-Cumming demostró que un filtro *antispam* de aprendizaje automático podía utilizarse para derrotar a otro filtro *antispam* de aprendizaje automático si éste aprendía por sí mismo qué palabras añadir a un correo electrónico no deseado para que no fuera clasificado como tal.

En 2004, Nilesh Dalvi y otros observaron que los clasificadores lineales utilizados en los filtros de correo spam podían ser derrotados mediante simples "ataques de evasión", ya que los responsables del spam (en inglés, *spammers*) insertaban "palabras buenas" en sus correos electrónicos no deseados. (Alrededor de 2007, algunos *spammers* incorporaban ruido aleatorio a las palabras difusas dentro del "spam de imágenes" con el fin de burlar los filtros basados en ROC).

En 2006, Marco Barreno y colaboradores publicaron *Can Machine Learning Be Secure?* (en español, ¿Puede ser seguro el aprendizaje automático?), donde describían una amplia taxonomía de ataques. Incluso en 2013, muchos investigadores seguían confiando en que los clasificadores no lineales (como las máquinas de vectores de soporte y las redes neuronales) podrían ser resistentes a los ataques, hasta que Battista Biggio y otros demostraron los primeros ataques basados en gradientes contra este tipo de modelos de aprendizaje automático (2012 -2013).

En 2012, las redes neuronales profundas comenzaron a dominar los problemas de visión por ordenador. A partir de 2014, Christian Szegedy y otros demostraron que las redes neuronales profundas podían ser burladas por atacantes, empleando una vez más un ataque basado en gradientes para crear perturbaciones antagónicas.

Recientemente, se ha observado que los ataques antagónicos son más difíciles de producir en el entorno práctico debido a las diferentes restricciones ambientales que anulan el efecto de los ruidos. Por ejemplo, cualquier pequeña rotación o ligera iluminación en una imagen antagónica puede acabar con el efecto antagónico. Además, investigadores como Nicholas Frosst, de Google Brain, señalan que es mucho más fácil hacer que los vehículos autónomos se salten las señales de alto eliminando físicamente la propia señal, en lugar de crear ejemplos antagónicos.

Frosst también cree que la comunidad del aprendizaje automático antagónico asume incorrectamente que los modelos formados con una determinada distribución de datos funcionarán igual de bien usando una distribución de datos completamente distinta. Él sugiere que debería explorarse un nuevo enfoque del aprendizaje automático, y actualmente está trabajando en una red neuronal única que tiene características más parecidas a la percepción humana que los enfoques más actualizados.

Aunque el aprendizaje automático antagónico sigue estando muy arraigado en el mundo académico, grandes empresas tecnológicas como Google, Microsoft e IBM han empezado a recopilar documentación y bases de código de fuente abierta para que otros puedan evaluar concretamente la solidez de los modelos de aprendizaje automático y minimizar el riesgo de ataques antagónicos.

 Ejemplos
Algunos ejemplos son los ataques a filtros *antispam*, en los que los mensajes spam son ofuscados al escribir incorrectamente palabras "malas" o insertar palabras "buenas"; los ataques a la seguridad informática, como la ofuscación de código malicioso (en inglés, *malware*) en paquetes de red o la modificación de las características de un flujo de red para confundir a los detectores de amenazas; los ataques al reconocimiento biométrico, en los que pueden explotarse rasgos biométricos falsos para hacerse pasar por un usuario legítimo; o para poner en peligro las galerías de plantillas de usuarios que se adaptan a rasgos actualizados con el paso del tiempo.

Algunos investigadores demostraron que cambiando solo un píxel era posible engañar a los algoritmos de aprendizaje profundo. Otros imprimieron en 3D una tortuga de juguete con una textura diseñada para que la IA de detección de objetos de Google la clasificara como un rifle, independientemente del ángulo desde el que se mirara la tortuga. Para crear la tortuga sólo se necesitó tecnología de impresión 3D de bajo coste disponible en el mercado.

Se demostró que la imagen de un perro retocada por una máquina parecía un gato tanto para los ordenadores como para los humanos. Un estudio de 2019 reveló que los humanos pueden adivinar la forma en que las máquinas clasificarán las imágenes antagónicas. Se han descubierto métodos para alterar la apariencia de una señal de alto de forma que un vehículo autónomo la clasifique como una señal de fusión de tráfico o de límite de velocidad.

McAfee atacó y engañó al antiguo sistema Mobileye de Tesla para que condujera a 80 km/h por encima del límite de velocidad con solo añadir una tira de cinco centímetros de cinta negra a una señal de límite de velocidad.

Patrones antagónicos en anteojos o ropa, diseñados para engañar a los sistemas de reconocimiento facial o a los lectores de matrículas, han dado lugar a una industria nicho de ropa con estilo "encubierto" (en inglés, *stealth streetwear*).

Un ataque antagónico a una red neuronal puede permitir a un atacante inyectar algoritmos en el sistema objetivo. Asimismo, los investigadores pueden crear entradas de audio antagónicas para disfrazar comandos dirigidos a asistentes inteligentes en audio de apariencia benigna; hay literatura paralela que explora la percepción humana ante tales estímulos.

Los algoritmos de agrupación se utilizan en el campo de la seguridad. El análisis de *malware* y virus informáticos tiene como objetivo identificar familias de *malware* y generar firmas de detección específicas.

 Modalidades de ataque

 Taxonomía
Los ataques contra algoritmos de aprendizaje automático (supervisado) se han clasificado en tres categorías principales:

 Influencia en el clasificador: Un ataque puede influir en el clasificador perturbando la fase de clasificación. Esto puede ir precedido de una fase de exploración para identificar vulnerabilidades. Las capacidades del atacante pueden verse limitadas por la presencia de restricciones de manipulación de datos.

 Violación de la seguridad: Un ataque puede suministrar datos maliciosos que acaben siendo clasificados como legítimos. Los datos maliciosos suministrados durante la formación pueden hacer que los datos legítimos sean rechazados después de la formación .

 Especificidad: Un ataque dirigido intenta permitir una intrusión/perturbación específica. Por el contrario, un ataque indiscriminado provoca un caos general.

Esta taxonomía se ha ampliado en un modelo de amenaza más completo que permite suposiciones explícitas sobre el objetivo del atacante, el conocimiento del sistema atacado, la capacidad de manipular los datos de entrada/componentes del sistema y sobre la estrategia de ataque. Esta taxonomía se ha ampliado para incluir dimensiones de estrategias de defensa contra ataques antagónicos.

 Estrategias
A continuación se exponen algunos de los escenarios de ataque más frecuentes:

 Envenenamiento de datos
El envenenamiento de datos (en inglés, *data poisoning*) consiste en contaminar el conjunto de datos de formación con datos diseñados para aumentar los errores en la salida. Dado que los algoritmos de aprendizaje dependen de sus conjuntos de datos de formación , el envenenamiento puede reprogramar algoritmos con intenciones potencialmente maliciosas. Han surgido inquietudes especialmente en relación con los datos de formación generados por los usuarios, por ejemplo, para la recomendación de contenidos o los modelos de lenguaje natural. La proliferación de cuentas falsas ofrece muchas posibilidades de envenenamiento. Según informes, Facebook elimina alrededor de 7.000 millones de cuentas falsas al año. El envenenamiento de datos es la principal fuente de preocupación con respecto a usos industriales.

En las redes sociales, las campañas de desinformación intentan sesgar los algoritmos de recomendación y moderación para impulsar determinados contenidos en detrimento de otros.

Un caso particular de envenenamiento de datos es el ataque de puerta trasera, cuyo objetivo es enseñar un comportamiento específico a entradas con un detonante determinado, por ejemplo, un pequeño defecto en imágenes, sonidos, vídeos o textos.

Por ejemplo, los sistemas de detección de intrusos suelen formarse a partir de datos recopilados. Un atacante puede envenenar estos datos inyectando muestras maliciosas durante su funcionamiento que posteriormente afecten al reformación.

 Ataques bizantinos
A medida que se amplía el aprendizaje automático, este suele depender de múltiples máquinas de computación. Así, en el aprendizaje federado los dispositivos periféricos colaboran con un servidor central, normalmente enviando gradientes o parámetros de modelos. Sin embargo, algunos de estos dispositivos pueden desviarse de su comportamiento esperado, ya sea para perjudicar el modelo del servidor central o para sesgar los algoritmos hacia determinados comportamientos (por ejemplo, amplificando la recomendación de contenidos desinformativos). Por otra parte, si la formación  se realiza en una sola máquina, el modelo es muy vulnerable a un fallo de la máquina o a un ataque a la máquina; la máquina es un punto único de fallo. De hecho, el propietario de la máquina también pudiera insertar puertas traseras indetectables.

Actualmente, las principales soluciones para que los algoritmos de aprendizaje (distribuido) sean resistentes a una minoría de participantes malintencionados (es decir, bizantinos) se basan en reglas agregación de gradientes sólidos. Las reglas de agregación sólida no siempre funcionan, especialmente cuando los datos de los participantes tienen una distribución no-IID. Sin embargo, en el contexto de participantes honestos heterogéneos, como usuarios con diferentes hábitos de consumo para los algoritmos de recomendación o estilos de escritura para modelos de lenguaje, existen teoremas de imposibilidad demostrables sobre lo que cualquier algoritmo de aprendizaje sólido puede garantizar.

 Evasión
Los ataques de evasión consisten en explotar la imperfección de un modelo formado. Por ejemplo, los *spammers* y los hackers intentan a menudo eludir la detección ofuscando el contenido de los correos basura y el *malware*. Las muestras se modifican para eludir la detección, es decir, para ser clasificadas como legítimas. Esto no implica influir en los datos de formación . Un claro ejemplo de evasión es el spam basado en imágenes, en el que el contenido del spam se incrusta dentro de una imagen adjunta para eludir el análisis textual de los filtros *antispam*. Otro ejemplo de evasión viene dado por los ataques de suplantación de identidad (en inglés, *spoofing*) contra los sistemas de verificación biométrica.

Los ataques de evasión pueden dividirse generalmente en dos categorías principales: ataques de caja negra y ataques de caja blanca.

 Extracción de modelos
La extracción de modelos implica que un adversario examine un sistema de aprendizaje automático de caja negra para extraer los datos con los que fue formado. Esto puede causar problemas cuando los datos de formación o el propio modelo son sensibles y confidenciales. Por ejemplo, la extracción de modelos podría utilizarse para extraer un modelo de negociación de acciones patentado que el atacante podría utilizar para su propio beneficio financiero.

En casos extremos, la extracción de modelos puede conducir al robo de modelos, que corresponde a la extracción de una cantidad suficiente de datos del modelo para permitir la reconstrucción completa del mismo.

Por otro lado, la inferencia de pertenencia es un ataque de extracción de modelos orientado, que infiere el propietario de un punto de datos, a menudo aprovechando el sobreajuste (en inglés, *overfitting*) resultante de prácticas deficientes de aprendizaje automático. Lo preocupante es que a veces esto se puede conseguir incluso sin conocer los parámetros de un modelo objetivo o sin tener acceso a ellos, lo que plantea problemas de seguridad para los modelos formados con datos confidenciales, incluidos, entre otros, los historiales médicos y/o la información de identificación personal. Con la aparición del aprendizaje por transferencia y la accesibilidad pública de muchos modelos de aprendizaje automático de última generación, las empresas tecnológicas se ven cada vez más atraídas a crear modelos basados en modelos públicos, lo que proporciona a los atacantes información de libre acceso sobre la estructura y el tipo de modelo utilizado.

 Categorías

 Aprendizaje antagónico de refuerzo profundo
El aprendizaje antagónico de refuerzo profundo es un área activa de investigación en el aprendizaje reforzado que se centra en las vulnerabilidades de las políticas aprendidas. En esta área de investigación, algunos estudios mostraron inicialmente que las políticas de aprendizaje reforzado son susceptibles a manipulaciones antagónicas imperceptibles. Aunque se han propuesto algunos métodos para superar estas susceptibilidades, en los estudios más recientes se ha demostrado que las soluciones propuestas distan mucho de ofrecer una representación exacta de las vulnerabilidades actuales de las políticas de aprendizaje de refuerzo profundo.

 Procesamiento antagónico de lenguaje natural
Se han introducido ataques antagónicos al reconocimiento de voz para aplicaciones de voz-a-texto (en inglés, *speech-to-text*), en particular para la implementación a Mozilla de *DeepSpeech*.

 Tipos de ataques específicos
Existe una gran variedad de ataques antagónicos que pueden utilizarse contra los sistemas de aprendizaje automático. Muchos de ellos funcionan tanto en sistemas de aprendizaje profundo como en modelos de aprendizaje automático tradicionales, como SVM y regresión lineal. Una muestra de alto nivel de estos tipos de ataque incluyen:

 Ejemplos Antagónicos
 Ataques de troyanos / Ataques de Puerta Trasera
 Inversión de Modelos
 Inferencia de Pertenencia

 Ejemplos antagónicos
Un ejemplo antagónico se refiere a una entrada de datos especialmente diseñada para que parezca "normal" a los humanos, pero que provoca una clasificación errónea en un modelo de aprendizaje automático. A menudo se usa una forma de "ruido" especialmente diseñado para provocar las clasificaciones erróneas. A continuación se presentan algunas técnicas actualizadas de generación de ejemplos antagónicos en la literatura (que no constituyen una lista exhaustiva).

 Ataque de evasión basado en gradientes
 Método de signo de gradiente rápido (*Fast Gradient Sign Method* o FGSM)
 Descenso de gradiente proyectado (*Projected Gradient Descent* o PGD)
 Ataque de Carlini y Wagner (C&W)
 Ataque de parche antagónico

 Ataques de caja negra
Los ataques de caja negra en el aprendizaje automático antagónico presuponen que el atacante sólo puede obtener resultados de las entradas proporcionadas y no tiene conocimiento de la estructura o los parámetros del modelo. En este caso, el ejemplo antagónico se genera utilizando un modelo creado desde cero o sin utilizar ningún modelo (excluyendo la posibilidad de consultar el modelo original). En cualquier caso, el objetivo de estos ataques es crear ejemplos antagónicos que puedan transferirse al modelo de caja negra en cuestión.

 Ataque Cuadrado
El Ataque Cuadrado (en inglés, *Square Attack*) se introdujo en 2020 como un ataque antagónico de evasión de caja negra basado en la consulta de puntuaciones de clasificación sin necesidad de información de gradiente. Como ataque de caja negra basado en puntuaciones, este enfoque antagónico es capaz de consultar las distribuciones de probabilidad entre las clases de salida del modelo, pero no tiene ningún otro acceso al modelo en sí. Según los autores de la investigación, el Ataque Cuadrado propuesto requería menos consultas que los ataques de caja negra basados en puntuaciones más actualizados en el momento.

Para describir la función objetivo, el ataque define el clasificador como , con  representando las dimensiones de la entrada y  como el número total de clases de salida.  devuelve la puntuación (o una probabilidad entre 0 y 1) de que la entrada  pertenece a la clase , lo que permite que la salida de clase del clasificador para cualquier entrada  se defina como . El objetivo de este ataque es el siguiente:

En otras palabras, encontrar algún ejemplo antagónico perturbado  tal que el clasificador lo clasifique incorrectamente dentro de alguna otra clase bajo la restricción de que  y   sean similares. A continuación, el estudio define la pérdida  como  y propone que la solución para encontrar el ejemplo antagónico  es resolver el siguiente problema de optimización con restricciones:

En teoría, el resultado es un ejemplo antagónico que tiene una gran confianza en la clase incorrecta, pero que también es muy similar a la imagen original. Para encontrar ese ejemplo, Ataque Cuadrado utiliza la técnica de búsqueda aleatoria iterativa para perturbar aleatoriamente la imagen con la esperanza de mejorar la función objetivo. En cada paso, el algoritmo perturba solo una pequeña sección cuadrada de píxeles, de ahí el nombre de Ataque Cuadrado, que termina en cuanto se encuentra un ejemplo antagónico para mejorar la eficiencia de la consulta. Por último, dado que el algoritmo de ataque utiliza puntuaciones y no información de gradiente, los autores del estudio indican que este enfoque no se ve afectado por el enmascaramiento de gradiente, una técnica común utilizada anteriormente para evitar los ataques de evasión.

 Ataque Triple Salto
El Ataque Triple Salto (en inglés, *HopSkipJump Attack*) Este ataque de caja negra también se propuso como un ataque eficiente de consulta, pero que se basa únicamente en el acceso a cualquier clase de salida predicha por una entrada. En otras palabras, el Ataque Triple Salto no requiere la capacidad de calcular gradientes o el acceso a los valores de puntuación como el Ataque Cuadrado, y sólo requerirá la salida de predicción de clase del modelo (para cualquier entrada dada).

El ataque propuesto se divide en dos enfoques diferentes, dirigido y no dirigido, pero ambos se construyen a partir de la idea general de añadir perturbaciones mínimas que conduzcan a un resultado diferente del modelo. En el enfoque dirigido, el objetivo es hacer que el modelo clasifique erróneamente la imagen perturbada con una etiqueta objetivo específica (que no es la etiqueta original). En el enfoque no dirigido, el objetivo es hacer que el modelo clasifique erróneamente la imagen perturbada con cualquier etiqueta que no sea la original.

Los objetivos de ataque de ambos son como se muestra a continuación donde  es la imagen original, es la imagen antagónica,  es una función de distancia entre imágenes,  es la etiqueta objetivo, y  es la función de etiqueta de clase de clasificación del modelo:

Para resolver este problema, el ataque propone la siguiente función límite  tanto para el enfoque no dirigido como para el dirigido:

Esto puede simplificarse aún más para visualizar mejor el límite entre los distintos ejemplos antagónicos potenciales:

Con esta función límite, el ataque sigue entonces un algoritmo iterativo para encontrar ejemplos antagónicos  para una imagen dada  que satisfaga los objetivos del ataque.

 Inicializar  hasta algún punto donde
 Iterar a continuación
 Búsqueda de límites
 Actualización del gradiente
 Calcular el gradiente
 Determinar el tamaño del paso

La búsqueda de límites utiliza una búsqueda binaria modificada para encontrar el punto en el que el límite (definido por ) se cruza con la línea entre  y . El siguiente paso consiste en calcular el gradiente para  y actualizar el valor original de  utilizando este gradiente y un tamaño de paso preestablecido. Los autores de Triple Salto demuestran que este algoritmo iterativo convergerá, llevando a  a un punto justo a lo largo del límite que está muy cerca en distancia a la imagen original.

Sin embargo, como Triple Salto es un ataque de caja negra propuesto y el algoritmo iterativo anterior requiere el cálculo de un gradiente en el segundo paso iterativo (al que los ataques de caja negra no tienen acceso), los autores proponen una solución para el cálculo del gradiente que sólo requiere las predicciones de salida del modelo. Mediante la generación de muchos vectores aleatorios en todas las direcciones, denotados como , se puede calcular una aproximación del gradiente utilizando la media de estos vectores aleatorios ponderados por el signo de la función límite en la imagen  donde  es el tamaño de la perturbación del vector aleatorio:

El resultado de la ecuación anterior da una aproximación cercana del gradiente requerido en el paso 2 del algoritmo iterativo, completando el Triple Salto como un ataque de caja negra.

 Ataques de caja blanca
Los ataques de caja blanca suponen que el atacante tiene acceso a los parámetros del modelo, además de poder obtener las etiquetas de las entradas proporcionadas.

 Método de signo de gradiente rápido
Uno de los primeros ataques propuestos para generar ejemplos antagónicos fue propuesto por los investigadores de Google Ian J. Goodfellow, Jonathon Shlens y Christian Szegedy. El ataque se denominó Método del Signo de Gradiente Rápido (FGSM, por sus siglas en inglés), y consiste en añadir a la imagen una cantidad lineal de ruido imperceptible y hacer que un modelo la clasifique incorrectamente. Este ruido se calcula multiplicando el signo del gradiente con respecto a la imagen que queremos perturbar por una pequeña constante épsilon. A medida que epsilon aumenta, el modelo tiene más probabilidades de ser burlado, pero las perturbaciones también se vuelven más fáciles de identificar. A continuación se muestra la ecuación para generar un ejemplo antagónico donde  es la imagen original,  es un número muy pequeño,  es la función de gradiente,  es la función de pérdida,  son los pesos del modelo, e  es la etiqueta verdadera.

Una propiedad importante de esta ecuación es que el gradiente se calcula con respecto a la imagen de entrada ya que el objetivo es generar una imagen que maximice la pérdida para la imagen original de etiqueta verdadera . En el descenso del gradiente tradicional (para la formación del modelo), el gradiente se utiliza para actualizar los pesos del modelo, ya que el objetivo es minimizar la pérdida del modelo en un conjunto sólido de datos verdaderos. El método de signo gradiente rápido se propuso como una forma rápida de generar ejemplos antagónicos para evadir el modelo, basándose en la hipótesis de que las redes neuronales no pueden resistir ni siquiera cantidades lineales de perturbaciones en la entrada.

 Carlini y Wagner (C&W)
En un esfuerzo por analizar los ataques y defensas antagónicos existentes, los investigadores de la Universidad de California, Berkeley, Nicholas Carlini y David Wagner en 2016 proponen un método más rápido y sólido para generar ejemplos antagónicos.

El ataque propuesto por Carlini y Wagner comienza intentando resolver una difícil ecuación de optimización no lineal:

Aquí el objetivo es minimizar el ruido , añadido a la entrada original , de manera que el algoritmo de aprendizaje automático  predice la entrada original con delta (o ) como alguna otra clase . Sin embargo en lugar de utilizar directamente la ecuación anterior, Carlini y Wagner proponen utilizar una nueva función  tal que:

Esto condensa la primera ecuación en el problema siguiente:

y aún más en la siguiente ecuación:

Carlini y Wagner proponen entonces el uso de la siguiente función en lugar de  utilizando , una función que determina las probabilidades de clase para una entrada dada . Cuando se sustituye, esta ecuación puede considerarse como la búsqueda de una clase objetivo que es más segura que la siguiente clase más probable por una cantidad constante:

Cuando se resuelve utilizando el descenso de gradiente, esta ecuación es capaz de producir ejemplos antagónicos más fuertes en comparación con el método de signo de gradiente rápido que también es capaz de eludir la destilación defensiva, una defensa que se propuso en su día como eficaz contra los ejemplos antagónicos.

 Defensas

Diversos investigadores han propuesto un planteamiento en varios pasos para proteger el aprendizaje automático.

 Modelado de amenazas - Formalizar los objetivos y capacidades de los atacantes con respecto al sistema objetivo.
 Simulación de ataque - Formalizar el problema de optimización que el atacante intenta resolver según las posibles estrategias de ataque.
 Evaluación del impacto de los ataques.
 Diseño de contramedidas.
 Detección de ruido (para ataques basados en la evasión).
 Lavado de información - Alterar la información recibida por los atacantes (para ataques de robo de modelos).

 Mecanismos
Se han propuesto varios mecanismos de defensa contra la evasión, el envenenamiento y los ataques a la privacidad, incluyendo:

 Algoritmos de aprendizaje seguro.
 Algoritmos resistentes a ataques bizantinos.
 Sistemas clasificadores múltiples.
 Algoritmos escritos por IA.
 IAs que exploran el entorno de formación; por ejemplo, en el reconocimiento de imágenes, navegando activamente por un entorno 3D en lugar de escanear pasivamente un conjunto fijo de imágenes 2D.
 Aprendizaje con preservación de la privacidad.
 Algoritmo de escalera para competiciones tipo Kaggle.
 Modelos teóricos de juegos.
 Desinfección de los datos de formación.
 Formación antagónica.
 Algoritmos de detección de puertas traseras.
 Técnicas de enmascaramiento/ofuscación del gradiente: para evitar que el atacante se aproveche del gradiente en ataques de caja blanca. Esta familia de defensas se considera poco fiable, ya que estos modelos siguen siendo vulnerables a los ataques de caja negra o pueden eludirse de otras maneras.
 En la literatura se han propuesto conjuntos de modelos, pero se debe tener cuidado al usarlos: normalmente la agrupación de clasificadores débiles da como resultado un modelo más preciso, pero esto no parece aplicarse en el contexto antagónico.

 Véase también

 Fawkes (software de encubrimiento de imágenes)
 Reconocimiento de patrones
 Máquina de aprendizaje extremo
 Aprendizaje automático basado en reglas

 Referencias

 Enlaces externos
