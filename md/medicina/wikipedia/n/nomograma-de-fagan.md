---
type: Artículo de enciclopedia
title: Nomograma de Fagan
description: "En medicina basada en la evidencia, el nomograma de Fagan es un recurso gráfico utilizado para el cálculo de la probabilidad post-test, conociendo la probabilidad pre-test y la razón de verosimilitud (en inglés, …"
resource: https://es.wikipedia.org/wiki/Nomograma_de_Fagan
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nomograma_de_Fagan"}
license: CC BY-SA 4.0
id: eswiki-Nomograma_de_Fagan
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nomograma de Fagan

En medicina basada en la evidencia, el **nomograma de Fagan** es un recurso gráfico utilizado para el cálculo de la probabilidad post-test, conociendo la probabilidad pre-test y la razón de verosimilitud (en inglés, Likelihood Ratio, o LR) .

Fue planteado por primera vez en 1975 por el médico Terrence J. Fagan, como una simple aplicación del teorema de Bayes, el cual describe la probabilidad de que un evento ocurra basado en el conocimiento previo de las condiciones que podrían estar relacionadas con el mismo.

 Descripción

Según la RAE, se entiende por nomograma a una representación gráfica bidimensional, que permite realizar con rapidez cálculos numéricos aproximados.

En el caso concreto del nomograma de Fagan, se representa por tres escalas graduadas equidistantes:

 La escala de la izquierda, graduada del 0.1 al 99.9%, representa tasa de prevalencia o la probabilidad pre-test , es decir, el porcentaje de la población estudiada que presenta el resultado buscado.
 La escala central, graduada del 10-3 a 2000 en términos de razón de verosimilitud, representa la capacidad de la prueba utilizada para seleccionar adecuadamente a la población que presenta o no el resultado buscado. En otras palabras, establece la medida en que el resultado de una prueba, ya sea positivo o negativo, modifica el porcentaje de una población que presenta cierta condición buscada.
 La escala de la derecha, graduada del 0.1 al 99.9%, representa la probabilidad post-test, reflejando el porcentaje de la población seleccionada a través de la prueba, que presenta el resultado deseado.

 Utilización
El nomograma de Fagan ha encontrado su mayor uso en las prácticas de medicina basada en la evidencia, como un recurso que permite ofrecerle datos objetivos al clínico sobre la probabilidad de que un paciente presente cierta enfermedad después de realizar una prueba dicotómica.

Para poder utilizar esta herramienta se debe conocer, a través de datos epidemiológicos como estudios de prevalencia (disponibles p.ej. en el portal VizHub del estudio Global Burden of Disease de 2019), o experiencia personal, el porcentaje de la población estudiada que presenta enfermedad que se pretende estudiar. Este dato corresponde a la probabilidad pre-test, y su disponibilidad representa una de las mayores limitantes en el uso de los modelos Bayesianos para guiar la toma de decisiones clínicas.En segundo lugar, se debe conocer el desempeño diagnóstico de la prueba dicotómica a utilizar. Este dato se obtiene de estudios de precisión diagnóstica realizados para el test elegido. En caso de no mencionarse, se debe calcular la razón de verosimilitud del estudio a partir de la sensibilidad y especificidad reportadas en el estudio:

La **razón de verosimilitud positiva** (**LR+** por sus siglas en inglés), se calcula con la siguiente fórmula

A su vez, la **razón de verosimilitud negativa** (**LR-** por sus siglas en inglés), se calcula con la siguiente fórmula

En el nomograma, se identifica en la escala de la izquierda el valor correspondiente con la probabilidad pre-test. De ahí, se trazan dos líneas rectas, una correspondiente a un resultado positivo en la prueba (**representado por el LR+)** y otra correspondiente a un resultado negativo en la prueba (**representado por el LR-**). Estas líneas se originan de la escala de probabilidad pre-test, pasan a través del valor correspondiente al LR en la escala central, y terminan en la escala de la derecha. El valor al que llegan las líneas representa la probabilidad post-test de la prueba.

De esta manera, el nomograma de Fagan permite identificar rápidamente la probabilidad de que un paciente sometido a una prueba dicotómica presente cierta enfermedad, dependiendo el resultado obtenido en la misma.

 Ejemplo
En la imagen de la derecha, se ha estimado una probabilidad pre-test de 5%, una LR+ de 50 y LR- de 0.1.

 Para un paciente con un resultado positivo, el médico traza la línea roja que cruza la tercera escala en 72. Por lo tanto, puede estimar la probabilidad de que su paciente esté enfermo en un 72%.
 En el caso de un paciente con un resultado negativo, el médico traza la línea verde que se cruza con la tercera escala en 0.5. La probabilidad de que el paciente enferme es entonces de sólo el 0.5%, es decir, en 5 casos de 1000 personas con un resultado negativo y una prevalencia pre-test similar.

 Limitaciones y nuevas propuestas

 Limitaciones del nomograma de 1975
El nomograma de Fagan, en su propuesta original, tuvo una serie de limitaciones que impedían su uso en la práctica clínica. Estas limitaciones incluían:

 El teorema de Bayes original fue diseñado para utilizar razones de momios, no probabilidades; por lo que se requiere una conversión algebraica para calcular la probabilidad.
 La mayoría de los estudios de validación de pruebas diagnósticas reportan su desempeño en términos de sensibilidad y especificidad, mismas que requieren ecuaciones especiales para ser convertidas en razones de verosimilitud.

 Nomograma del teorema de Bayes (2011)

Considerando estas dificultades, se publicó en 2011 una versión actualizada del nomograma de Fagan, nombrada "nomograma del teorema de Bayes". Esta herramienta soluciona los problemas arriba descritos al integrar escalas que permiten determinar la razón de verosimilitud utilizando la sensibilidad y especificidad de la prueba realizada. Así mismo, permite la utilización de razones de momios (en inglés, Odds Ratio) para estimar la probabilidad pre-test de una prueba, alineandose con el diseño original del teorema de Bayes.

 Nomograma de Fagan de dos pasos (*two-step Fagan's nomogram)* (2013)
Otra propuesta para solventar las limitaciones asociadas al nomograma original es el llamado "nomograma de Fagan de dos pasos", propuesto en 2013 por CG Caraguel. Este modelo agrega un paso inicial, de ahí la denominación de "dos pasos", que permite el cálculo de la razón de verosomilitud de la prueba utilizando la sensibilidad y especificidad típicamente reportadas en los estudios de precisión diagnóstica. El desempeño estadístico de este modelo se validó de manera independiente en un estudio comparándolo con la determinación de probabilidad post-test utilizando otros nomogramas, demostrando que incrementa la precisión de herramientas ya existentes para el pronóstico de cáncer de próstata.

 Referencias

__INDEXAR__
