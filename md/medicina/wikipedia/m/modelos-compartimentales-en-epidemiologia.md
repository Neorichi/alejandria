---
type: Artículo de enciclopedia
title: Modelos compartimentales en epidemiología
description: Los modelos compartimentales constituyen una técnica utilizada para simplificar la modelización matemática de las enfermedades infecciosas.
resource: https://es.wikipedia.org/wiki/Modelos_compartimentales_en_epidemiología
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelos_compartimentales_en_epidemiología"}
license: CC BY-SA 4.0
id: eswiki-Modelos_compartimentales_en_epidemiología
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelos compartimentales en epidemiología

Los modelos compartimentales constituyen una técnica utilizada para simplificar la modelización matemática de las enfermedades infecciosas. La población se divide en compartimentos, asumiendo que cada individuo en un mismo compartimento tiene las mismas características.

Su origen se encuentra a principios del , siendo un trabajo importante la primera investigación de Kermack y McKendrick en 1927. Los modelos suelen investigarse mediante ecuaciones diferenciales ordinarias (las cuales son determinísticas), pero también se pueden observar en un marco estocástico, el cual es más realista pero también más complicado de analizar.

Los modelos compartimentales se pueden utilizar para predecir las características de propagación de una enfermedad, por ejemplo, la prevalencia (número total de infectados) o la duración de una epidemia.

Además, el modelo permite comprender cómo diferentes situaciones pueden afectar el resultado de la epidemia, por ejemplo, cuál es la técnica más eficiente para emitir un número limitado de vacunas en una determinada población.
 El modelo SIR
El modelo SIR es uno de los modelos compartimentales más simples y muchos modelos derivan de este modelo básico. El modelo consta de tres compartimentos: S para el número de susceptibles, I para el número de infectados y R para el número de recuperados (o inmunes). Este modelo es razonablemente predictivo para enfermedades infecciosas que se transmiten de humano a humano y donde la recuperación confiere resistencia duradera, como el sarampión, las paperas y la rubéola.

Estas variables (S, I y R) representan el número de personas en cada compartimiento en un momento concreto. Para representar que el número de individuos susceptibles, infectados y recuperados puede variar con el tiempo (incluso si el tamaño de la población total permanece constante), los números precisos se convierten en una función de t (tiempo): S(t), I(t) y R(t). Para una enfermedad específica en una población específica, estas funciones pueden calcularse para predecir posibles brotes y controlarlos.
 El modelo SIR es dinámico en tres sentidos
En cuanto a la función variable de la t, el modelo es dinámico en tanto que los números en cada compartimento pueden fluctuar con el tiempo. La importancia de este aspecto dinámico es más evidente en una enfermedad endémica con un corto período infeccioso, como el sarampión en el Reino Unido antes de la introducción de la vacuna en 1968. Estas enfermedades tienden a ocurrir en ciclos de brotes debido a la variación en el número de casos susceptibles (S(t)) a lo largo del tiempo. Durante una epidemia, el número de individuos susceptibles decrece rápidamente a medida que se infectan y, en consecuencia, entran en los compartimentos de infectados y recuperados. La enfermedad no puede brotar de nuevo hasta que el número de susceptibles haya vuelto a acumularse, por ejemplo, como resultado de la descendencia, que nace en el compartimento susceptible.

Cada miembro de la población suele pasar de susceptible a infectado, y a recuperado. Esto se puede mostrar como un diagrama de flujo en el que los cuadros representan los diferentes compartimentos y las flechas la transición entre compartimentos, por ejemplo:
 Tasas de transición
Para que el modelo sea completamente específico, las flechas se tienen que etiquetar con las tasas de transición entre los compartimentos. Entre S y I, la tasa de transición es βI, donde β es el número promedio de contactos por persona por tiempo, multiplicado por la probabilidad de transmisión de la enfermedad en un contacto entre un sujeto susceptible y uno infectado.  Entre I y R, la tasa de transición es γ (simplemente es la tasa de recuperación o muerte, es decir, el número de recuperados o muertos durante un día, dividido entre el número total de infectados de ese mismo día, suponiendo que el «día» es la unidad de tiempo).  Si la duración de la infección es indicada como D, entonces γ = 1/D, ya que un individuo experimenta una recuperación en D unidades de tiempo.  Se asume que la permanencia de cada sujeto en los estados epidémicos es una variable aleatoria con distribución exponencial.  Se pueden utilizar distribuciones más complejas y realistas (como la distribución de Erlang) con algunas modificaciones.
 Tratamiento determinístico biomatemático del modelo SIR
 El modelo SIR sin dinámica vital.
La dinámica de una epidemia, por ejemplo la gripe, a menudo es mucho más rápida que la dinámica del nacimiento y la muerte, por lo tanto, el nacimiento y la muerte suelen omitirse en modelos compartimentales simples.  El sistema SIR sin la denominada dinámica vital (nacimiento y muerte, a veces denominada demografía), descrito anteriormente, puede expresarse mediante el siguiente conjunto de ecuaciones diferenciales ordinarias:

donde  es el conjunto de la población susceptible,  es el conjunto de infectados,  el de la población sin la enfermedad (por muerte o recuperación) y  la suma de los tres.

Este modelo fue propuesto por primera vez por O. Kermack y Anderson Gray Mckendrick, como un caso especial de lo que ahora llamamos la teoría de Kermack y McKendrick, y dio seguimiento al trabajo de McKendrick con Ronald Ross.  Este sistema es no lineal, sin embargo, es posible derivar su solución analítica de forma cerrada. Otras herramientas numéricas incluyen métodos de Monte Carlo, como el algoritmo Gillespie. Primero, nótese que:

a lo que sigue:

expresando en términos matemáticos la constante de población .  Nótese que la relación anterior implica que tan solo se tiene que estudiar dos de las tres ecuaciones.

En segundo lugar, observamos que la dinámica de la clase infecciosa depende de la siguiente relación:

el llamado número básico de reproducción (también llamada ratio básica reproductiva).  Esta ratio está derivada como el número de nuevas infecciones esperadas (estas nuevas infecciones se llaman secundarias) de una sola infección en una población donde todos los sujetos son susceptibles. Esta idea se puede comprobar mejor si se establece el tiempo típico entre contactos como  y el tiempo típico hasta que no se tiene la enfermedad como .  Desde aquí sigue que, en general, el número de contactos con una persona infecciosa antes de que ya no tenga la enfermedad es:

Dividiendo la primera ecuación diferencial entre un tercio, separando las variables e integrando los datos obtenemos

donde  y  son los números iniciales de, respectivamente, susceptibles y sin enfermedad.  Si escribimos  para la proporción inicial de susceptibles y  and
 para los susceptibles y sin enfermedad, respectivamente, en el límite  se obtiene

(nótese que el compartimento de infecciosos se vacía en este límite).

Esta ecuación trascendente tiene una solución en términos de la función  de Lambert, que es:

Esto muestra que al final de una epidemia, a no ser que , no todos los individuos de una población no tienen la enfermedad, por lo tanto algunos pueden ser susceptibles.  Esto quiere decir que el final de una epidemia está causada por el descenso en el número de infecciosos y no por la falta de sujetos susceptibles.

El rol del número básico de reproducción es extremadamente importante. De hecho, si reescribimos la ecuación para un individuo infeccioso de la siguiente manera:

vemos que si:

entonces:

habrá un brote epidémico con un número más alto de casos (lo que puede alcanzar a una gran parte de la población).  Por el contrario:

entonces:

independientemente del tamaño inicial de la población susceptible, la enfermedad nunca puede causar un brote epidémico.  Como consecuencia, está claro que el número básico reproductivo es muy importante.

 La fuerza de la infección
Hay que tener en cuenta que en el modelo anterior la función:

modela la ratio de transición del compartimento susceptible al infeccioso, así que se llama fuerza de la infección.  Sin embargo, para clases de enfermedades más comunicables, es más realista considerar la fuerza de la infección que no depende del número absoluto de infecciosos, pero de la fracción (con respecto a la constante total de población ):

Capasso y, después, otros autores han propuesto fuerzas no-lineares para modelar de manera más realista el proceso de contagio.

 Soluciones analíticas exactas al modelo SIR
En el 2014, Harko y coautores derivaron una solución analítica exacta al modelo SIR. En el caso sin dinámica vital, para , etc. , corresponde a la siguiente parametización:

para

con condiciones iniciales

donde  satisface .  Con la ecuación trascendental  anterior, sigue que , si  y.

Se encontró una solución analítica equivalente a los rendimientos de Miller:

Aquí  se puede interpretar como el número esperado de transmisiones que un individuo ha recibido por tiempo .  Estas dos soluciones están relacionadas por

Efectivamente, el mismo resultado puede encontrarse en el trabajo original de Kermack y Mckendrick.

Estas soluciones se entienden mejor si vemos que todos los términos en la parte de la derecha de las ecuaciones diferenciales son proporcionales a .  Las ecuaciones pueden ser divididas por , y el tiempo reescalado para que el operador en la izquierda se convierta simplemente en , donde , por ejemplo .  Las ecuaciones diferenciales son ahora lineares y la tercera, con forma  const. , muestra que  y  (y arriba ) se crean simplemente lineares.

 El modelo SIR con dinámica vital y población constante
Considere una población caracterizada por una tasa de mortalidad  y una ratio de nacimiento , y donde enfermedades comunicables se propagan.  El modelo de transmisión es:

para el cual el equilibrio sin enfermedad (DFE, en inglés) es:

En este caso, podemos derivar el número de reproducción básico:

que tiene propiedades de entrada.  De hecho, independientemente de los valores biológicos iniciales, podemos ver que:

El punto EE, es el Equilibrio Endémico (la enfermedad no está erradicada y se mantiene en la población).  Con argumentos heurísticos, uno puede ver que  se puede leer como el promedio de infecciones causadas por un solo sujeto infeccioso en una población susceptible.  La relación biológica anterior implica que si el número es igual o menor que 1 la enfermedad se extingue; por el contrario, si es mayor, la enfermedad se quedara permanentemente endémica en la población.

 Modelo SIS

Algunas infecciones, por ejemplo las de la gripe común y la influenza, no confieren inmunidad duradera. Estas infecciones no dan inmunización al recuperarse de la infección, y los individuos vuelven a ser susceptibles.

Tenemos el modelo:

Nótese que denominar con *N* al total de la población:

.

A lo que sigue:

,

Las dinámicas infecciosas se rigen por una logística funcional que implica :

Es posible encontrar una solución analítica a este modelo (transformando las variables:  y sustituyéndolas por ecuaciones de campo), para que la ratio de reproducción básica sea mayor que la unidad.  La solución se presenta como:

.

where  is the endemic infectious population, , and .  As the system is assumed to be closed, the susceptible population is then .

Como caso especial, se obtiene la función logística usual asumiendo que .  Esto también se puede considerar en el modelo SIR con , en este caso no se quitará nada.  Ese es el *modelo SI*. La ecuación diferencial usando  se reduce a:

A la larga, en este modelo, todos los individuos se infectan.

 Explicaciones sobre el modelo SIR básico

 El modelo MSIR

En muchas infecciones, incluyendo el sarampión, los bebés no nacen en el compartimento susceptible, sino que son inmunes a la enfermedad durante los primeros meses de vida debido a la protección de los anticuerpos maternos (transmitidos a través de la placenta y adicionalmente a través del calostro). Esto se denomina inmunidad pasiva. Este detalle adicional puede demostrarse con una clase M (para la inmunidad maternal) al inicio del modelo

Para indicar esto matemáticamente, se añade un compartimento adicional, M(t), que tiene como resultado las siguientes ecuaciones diferenciales:

 Para indicar esto matemáticamente, se añade un compatimento adicional *M*(*t*)*.*  Esto resulta en las siguientes ecuaciones:

 Estado de portador
Algunas personas que han tenido una enfermedad infecciosa como la tuberculosis nunca se recuperan completamente y siguen llevando la infección, pese a que no sufren la enfermedad. Pueden volver a entrar al compartimento de infectados y sufrir síntomas (como en la tuberculosis) o pueden seguir infectando a otros en su estado de portador, a pesar de no padecer síntomas. El ejemplo más famoso de esto es, probablemente, Mary Mallon, que infectó a 22 personas con fiebre tifoidea. El compartimento de portadores está marcado con C.

 Modelo SEIR
Para muchas infecciones importantes existe un período de incubación significativo durante el cual los individuos han sido infectados, pero aún no son infecciosos por sí mismos. Durante este periodo el individuo se encuentra en el compartimento E (de exposición).

Asumiendo que el período de incubación es una variable aleatoria con distribución exponencial con parámetro (el periodo medio de incubación es ) y asumiendo la presencia de dinámicas vitales en la ratio de nacimiento  iguales a la ratio de muertes , obtenemos este modelo:

Tenemos  pero tan solo es constante porque la asunción (degenerativa) de que las muertes y nacimientos son iguales; en general  es variable.

Para este modelo, el número de reproducción básico es:

Similar al modelo SIR, tenemos el equilibrio sin enfermedad (DFE) (*N*,0,0,0) y el Equilibrio Endémico (EE); se puede ver que, de manera independiente a las condiciones biológicas iniciales:

esto mantiene:

En el caso de ratios de contacto que varían periódicamente , la condición para la atracción global del DFE es siguiendo un sistema linear con coeficientes periódicos:

es estable (tiene los valores de Floquet dentro de la unidad círculo en el plano complejo)

 Modelo SEIS
El modelo SEIS contempla el período de exposición, o periodo latente de la enfermedad, dando lugar a un compartimento adicional, E(t).

En este modelo, una infección no deja inmune a los individuos que se han recuperado; estos vuelven a ser suscptibles, volviendo al compartimento*S*(*t*).  Le ecuación diferencial siguiente describe el modelo:

 Modelo MSEIR
En el caso de una enfermedad con los factores de inmunidad pasiva y un período de latencia, existe el modelo MSEIR.

 Modelo MSEIRS
Un modelo MSEIRS es similar al modelo MSEIR, pero la inmunidad en la clase R sería temporal, por lo que los individuos recuperarían su susceptibilidad cuando terminara la inmunidad temporal.

 Tasas de contacto variables y epidemias plurianuales o caóticas.
Es bien sabido que la probabilidad de contraer una enfermedad no es constante en el tiempo. Algunas enfermedades son estacionales, tales como los virus del resfriado común, que son más frecuentes durante el invierno. Con las enfermedades de la infancia, tales como el sarampión, las paperas y la rubéola, existe una fuerte correlación con el calendario escolar, por lo que durante las vacaciones escolares la probabilidad de contraer dicha enfermedad disminuye notablemente. Como consecuencia, para muchas clases de enfermedades se debe considerar una fuerza de infección con tasa de contacto periódica y variable ('estacional').

Como consecuencia, para muchas clases de enfermedades, uno debe considerar la fuerza de infección con una ratio de contacto variable periódicamente ('estacional')

con un periodo T igual a un año.

Por lo tanto, nuestro modelo se convierte en

(las dinámicas de los recuperados siguen la forma ).  Una serie de ecuaciones diferenciales no-lineares con parámetros variables periódicos.  Es sabido que esta clase de sistema dinámico puede sufrir interesantes y complejos fenómenos de resonancia paramétrica no-linear.  Es fácil de ver si:

donde si la integral es mayor que uno, la enfermedad no morirá y puede haber estas resonancias.  Por ejemplo, considerando la ratio de contacto variable periódica como la entrada del sistema, la salida es una función periódica cuyo periodo es un múltiple del periodo de entrada.

Esto permitió ayudar a explicar los brotes epidémicos polianuales (típicamente bienales) de algunas enfermedades infecciosas como interacción entre el período de las oscilaciones de la tasa de contacto y el seudo-período de las fluctuaciones que se encuentran cerca de la región endémica. Notablemente, el comportamiento también puede ser cuasi-periódico o incluso caótico.

 Modelización de la vacunación
El modelo SIR se puede modificar para modelar la vacunación.  Normalmente estos introducen un compartimento adicional al modelo SIR, , para individuos vacunados.  A continuación, algunos ejemplos.

 Vacunando recién nacidos
En presencia de enfermedades transmisibles, una de las principales tareas es la erradicación mediante medidas de prevención y, si es posible, mediante el establecimiento de un programa de vacunación masiva. Considérese una enfermedad por la cual el recién nacido está vacunado (con una vacuna que administra inmunidad de por vida) a un ritmo :

donde  es la clase de sujetos vacunados.  Esto muestra inmediatamente que::

entonces tenemos que tratar con un comportamiento a mayor plazo de  e, por lo que:

En otras palabras, si

el programa de vacunación no es capaz de erradicar la enfermedad, al contrario, permanecerá endémica, aunque a niveles inferiores que si no hubiera vacunas.  Esto quiere decir que el modelo matemático sugiere que para una enfermedad cuyo número de reproducción básico puede llegar a ser 18, se deberían vacunar al menos al 94. 4% de los recién nacidos para erradicar la enfermedad.

 Vacunación e información
Las sociedades modernas están enfrentándose al desafío de la exención “racional", es decir, la decisión de la familia de no vacunar a los niños como consecuencia de una comparación "racional" entre el riesgo percibido por la infección y los posibles daños por la vacuna. Para valorar si este comportamiento es realmente racional, es decir, si esto puede igualmente llevar a la erradicación de la enfermedad, simplemente hay que asumir que la tasa de vacunación es una función creciente del número de sujetos infecciosos:

En este caso la condición de erradicación se convierte en:

La línea de la ratio de vacunación debería ser más alta que el umbral de "vacunación obligatoria" que, en caso de exención, no puede mantenerse.  Entonces, la exención "racional" puede ser miope puesto que está basada en la baja incidencia debido a la alta cobertura de la vacuna, en lugar de tener en cuenta un futuro rebrote de la infección debido a un descenso en la cobertura.

 Vacunación de los no recién nacidos
En el caso de que además haya vacunas a no recién nacidos a una tasa ρ, la ecuación para el sujeto susceptible y vacunado se debe modificar de la siguiente manera :

que lleva a la siguiente condición de erradicación:

 Estrategia de vacunación frecuente
Esta estrategia vacuna repetidamente a un grupo de edad definido (como niños pequeños o ancianos) en una población susceptible a lo largo del tiempo.  Con esta estrategia, se retira inmediatamente al grupo de individuos susceptibles, lo que permite la eliminación de una enfermedad infecciosa, (como el sarampión), de toda la población. Cada unidad de tiempo T, una fracción constante p de sujetos susceptibles se vacunan en un tiempo relativamente corto (respecto a la dinámica de la enfermedad). Esto lleva a las siguientes ecuaciones diferenciales impulsivas para los sujetos susceptibles y vacunados:

Es fácil de ver que si proponemos  se obtiene que la dinámica de los sujetos susceptibles se da por:

y la condición de erradicación es:

 La influencia de la edad: modelos estructurados por edad
La edad influye profundamente en la propagación de la enfermedad en una población, especialmente en la tasa de contacto. Esta tasa resume la efectividad de los contactos entre sujetos susceptibles e infecciosos. Teniendo en cuenta las edades de las clases epidémicas  (to limit ourselves to the susceptible-infectious-removed scheme) such that:

(donde es la edad máxima admisible) y las dinámicas no se describen, como uno pensaría, con una "simple" ecuación diferencial parcial, sino por ecuaciones integro-diferenciales:

donde:

es la fuerza de infección que, por supuesto, dependerá del contactp kernel  en la interacción entre edades.

La complejidad se agrega por las condiciones iniciales de los recién nacidos (es decir, por a=0), que son fáciles de infectar y eliminar:

pero que son no-locales para la densidad de los recién nacidos susceptibles:

donde  son las fertilidades de los adultos.

Además, definiendo ahora la densidad de la población total  se obtiene:

En el caso más simple de fertilidades iguales en las tres clases epidémicas, se obtiene que para tener equilibrio demográfico la siguiente necesaria y suficiente condición vinculando la fertilidad  con la mortalidad  se tiene que mantener:

y el equilibrio demográfico es:

automáticamente asegurando la existencia de una solución libre de enfermedad:

Un número de reproducción básico se puede calcular como el radio espectral de un operador funcional apropiado.
 Otras consideraciones dentro de los modelos compartimentales epidémicos
 Transmisión vertical
En el caso de algunas enfermedades como el SIDA y la Hepatitis B, es posible que la descendencia de los padres infectados nazca con la infección. La transmisión de la enfermedad por medio de la madre se denomina transmisión vertical. La afluencia de miembros adicionales en la categoría infectada puede considerarse dentro del modelo al incluir una fracción de los miembros recién nacidos en el compartimento infectado.
 Transmisión vectorial
Las enfermedades transmitidas indirectamente entre seres humanos, - por ejemplo, la malaria que se transmite por medio de mosquitos - se transmiten a través de un vector. En estos casos, las transferencias de infección de humanos al insecto y un modelo epidémico deben incluir ambas especies, generalmente requiriendo más compartimentos que un modelo de transmisión directa.
 Otros
Otros casos que necesitan considerarse al modelar una epidemia incluyen cosas como las siguientes: Mezclas no homogéneas Infectividad variable Distribuciones que son espacialmente no uniformes Enfermedades causadas por macroparásitos
 Modelos epidémicos determinísticos contra estocásticos
Es importante destacar que los modelos determinísticos que aquí se presentan son válidos únicamente en poblaciones suficientemente grandes y en consecuencia deben ser utilizados con precaución. Para ser más precisos, estos modelos sólo son válidos en el límite termodinámico, donde la población es efectivamente infinita. En modelos estocásticos, el equilibrio endémico a largo plazo obtenido previamente, no se mantiene, ya que existe una probabilidad finita de que el número de individuos infectados disminuya por debajo de uno en un sistema.  En un sistema real, el patógeno puede no propagarse, ya que ningún huésped estaría infectado. Sin embargo, en modelos de campo determinísticos, el número de infectados puede asumir valores reales, concretamente, valores no enteros de huéspedes infectados, y el patógeno aún puede persistir en el sistema con un número de huéspedes que es menor a uno, pero más de cero.
 Véase también
Modelización matemática en epidemiología
Problema de unidad de área modificable
Matriz de última generación
Asesoramiento de riesgo
Ratio de ataque

 Referencias

 Lectura adicional

 N. Bacaër, J. Ripoll, R. Bravo de la Parra, X. Bardina, S. Cuadrado: *Matemáticas y epidemias* (2021) Paris, ISBN 979-10-343-8464-8. Pdf

 Enlaces externos
Modelo SIR: Experimentos en línea con JSXGraph
 SIR model: Online experiments with JSXGraph
