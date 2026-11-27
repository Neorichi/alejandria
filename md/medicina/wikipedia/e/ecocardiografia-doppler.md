---
type: Artículo de enciclopedia
title: Ecocardiografía Doppler
description: La ecocardiografía Doppler es un procedimiento que utiliza la ecografía Doppler para examinar el corazón.
resource: https://es.wikipedia.org/wiki/Ecocardiografía_Doppler
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ecocardiografía_Doppler"}
license: CC BY-SA 4.0
id: eswiki-Ecocardiografía_Doppler
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ecocardiografía Doppler

La **ecocardiografía Doppler** es un procedimiento que utiliza la ecografía Doppler para examinar el corazón. Un ecocardiograma utiliza ondas sonoras de alta frecuencia para crear una imagen del corazón, mientras que el uso de la tecnología Doppler permite determinar la velocidad y la dirección del flujo sanguíneo mediante el efecto Doppler.

 Descripción
Un ecocardiograma puede, en ciertos límites, producir una evaluación precisa de la dirección del flujo sanguíneo y la velocidad de la sangre y del tejido cardíaco en cualquier punto arbitrario mediante el efecto Doppler. Una de las limitaciones es que el haz de ultrasonidos debe ser lo más paralelo posible al flujo sanguíneo. Las medidas de velocidad permiten evaluar las áreas y la función de las válvulas cardíacas, cualquier comunicación anormal entre el lado izquierdo y derecho del corazón, cualquier fuga de sangre a través de las válvulas (ingurgitación valvular), el cálculo de la salida cardíaca y el cálculo de la relación E/A (una medida de la disfunción diastólica ). Los medios de contraste de microburbujas llenos de gas con ultrasonidos mejorados con contraste se pueden utilizar para mejorar la velocidad u otras medidas médicas relacionadas con el flujo.

Una ventaja de la ecocardiografía Doppler es, que se puede utilizar para medir el flujo sanguíneo dentro del corazón sin procedimientos invasivos como el cateterismo cardíaco.

Además, con parámetros de filtro/ganancia ligeramente distintos, el método puede medir las velocidades de los tejidos mediante ecocardiografía Doppler tisular. La combinación de flujo y velocidades de los tejidos puede utilizarse para estimar la presión de llenado del ventricular izquierdo, aunque sólo en determinadas condiciones.

Aunque "Doppler" se ha convertido en sinónimo de "medida de velocidad" en imagen médica, en muchos casos no se mide el desplazamiento de frecuencia (desplazamiento Doppler) de la señal recibida, sino el cambio de fase (cuando llega la señal recibo). Sin embargo, el resultado del cálculo terminará siendo idéntico.

Este procedimiento se utiliza a menudo para examinar el corazón de los niños para detectar enfermedades cardíacas porque no existe ningún requisito de edad o tamaño.

 Imagen Doppler 2D
A diferencia de la imagen Doppler 1D, que sólo puede proporcionar velocidad unidimensional y depende del ángulo del haz al flujo, la estimación de la velocidad en 2D mediante ultrasonidos Doppler es capaz de generar vectores de velocidad con componentes de velocidad axial y lateral. La velocidad 2D es útil incluso si existen condiciones de flujo complejas como la estenosis y la bifurcación. Existen dos métodos principales de estimación de la velocidad en 2D mediante ultrasonidos: el seguimiento de manchas y el Doppler vectorial de haz cruzado, que se basan en medir los cambios de tiempo y los cambios de fase respectivamente.

 Doppler vectorial
Doppler vectorial es una extensión natural de la imagen Doppler 1D tradicional basada en el cambio de fase. El cambio de fase se encuentra tomando la autocorrelación entre los ecos de dos rasgos consecutivos. La idea principal del Doppler vectorial es dividir al transductor en tres aberturas: una en el centro como apertura de transmisión y dos a cada lado como aberturas de recepción. Los cambios de fase medidos desde las aberturas izquierda y derecha se combinan para dar las componentes de velocidad axial y lateral. Las posiciones y ángulos relativos entre las aberturas se ajustarán según la profundidad del buque y la posición lateral de la región de interés.

 Seguimiento de manchas
l seguimiento de manchas, que es un método bien establecido en compresión de vídeo y otras aplicaciones, puede utilizarse para estimar el flujo sanguíneo en sistemas de ecografía. La idea básica del seguimiento de speckle es encontrar la mejor coincidencia de un speckle determinado de un fotograma dentro de una región de búsqueda en fotogramas posteriores. La decorrelación entre fotogramas es uno de los principales factores que degradan su rendimiento. La decorrelación es causada principalmente por la diferente velocidad de los píxeles dentro de un speckle, puesto que no se mueven como un bloque. Esto es menos grave cuando se mide el flujo en el centro, donde la velocidad de cambio de velocidad es la más baja. El flujo en el centro suele tener la mayor magnitud de velocidad, llamada "velocidad máxima". Es la información más necesaria en algunos casos como el diagnóstico de estenosis. Hay principalmente tres métodos para encontrar la mejor coincidencia: SAD (Suma de la diferencia absoluta), SSD (Suma de la diferencia al cuadrado) y Correlación cruzada. Supongamos  es un píxel en el núcleo y  es el píxel mapa desplazado por  en la región de búsqueda.

SAD se calcula como:

SSD se calcula como:

El coeficiente de correlación cruzada normalizada se calcula como:

donde  y  son los valores medios de  y  respectivamente. El  El par que da la D más baja para SAD y SSD, o la mayor ρ para la correlación cruzada, se selecciona como estimación del movimiento. Entonces, la velocidad se calcula como el movimiento dividido por la diferencia de tiempo entre los fotogramas. Normalmente, se toma la mediana o media de las estimaciones múltiples para dar un resultado más preciso.

 Precisión del subpíxel
En los sistemas de ecografía, la resolución lateral suele ser muy inferior a la resolución axial. La mala resolución lateral de la imagen en modo B provoca también una mala resolución lateral en la estimación del flujo. Por tanto, se necesita una resolución de subpíxel para mejorar la precisión de la estimación en la dimensión lateral. Mientras tanto, podríamos reducir la frecuencia de muestreo a lo largo de la dimensión axial para ahorrar cálculos y memorias si el movimiento del subpíxel se estima con precisión suficiente. En general, existen dos tipos de métodos para obtener la precisión del subpíxel: métodos de interpolación, como el ajuste parabólico, y métodos basados en fases en las que se encuentra el retraso máximo cuando la fase de la función de correlación cruzada analítica cruza cero.

 Método de interpolación (ajuste parabólico)

Como se muestra en la figura de la derecha, el ajuste parabólico puede ayudar a encontrar el pico real de la función de correlación cruzada. La ecuación para el ajuste parabólico en 1D es:

donde  es la función de correlación cruzada y  es la cima encontrada originalmente.  entonces se utiliza para encontrar el desplazamiento de los dispersores después de la interpolación. Para el escenario 2D, esto se realiza tanto en dimensiones axiales como laterales. Se pueden utilizar otras técnicas para mejorar la precisión y robustez del método de interpolación, incluido el ajuste parabólico con compensación de sesgo y la interpolación de filtro coincidente.

 Método basado en fases
La idea principal de este método es generar una fase lateral sintética y utilizarla para encontrar la fase que cruza cero en el pico de retraso.

La figura de la derecha ilustra el procedimiento de creación de la fase lateral sintética como primer paso. Básicamente, el espectro lateral se divide en dos para generar dos espectros con frecuencias centrales distintas de cero. La correlación cruzada se realiza tanto para la señal arriba como para la baja, creando  y  respectivamente. La función de correlación lateral y la función de correlación axial se calculan de la siguiente forma:

Tienen la misma magnitud y el pico entero se encuentra mediante métodos tradicionales de correlación cruzada. Después de localizar el pico entero, se extrae una región de 3 por 3 que envuelve el pico con su información de fase. Tanto para las dimensiones laterales como axiales, se encuentran los cruces por cero de una función de correlación unidimensional en los retrasos de la otra dimensión y se crea una línea lineal de mínimos cuadrados en consecuencia. La intersección de ambas líneas da la estimación del desplazamiento 2D.

 Comparación entre Doppler vectorial y seguimiento de speckle
Ambos métodos podrían utilizarse para la imagen vectorial de velocidad 2D, pero el seguimiento de manchas sería más fácil de extender a 3D. Además, en Doppler vectorial, la profundidad y la resolución de la región de interés están limitadas por el tamaño de la apertura y el ángulo máximo entre las aberturas de transmisión y recepción, mientras que Speckle Tracking tiene la flexibilidad de alternar el tamaño del núcleo y la región de búsqueda para adaptarse. a un requisito de resolución distinta. Sin embargo, el Doppler vectorial es menos complejo computacionalmente que el seguimiento de manchas.

 Estimación del caudal volumétrico
La estimación de la velocidad a partir del Doppler convencional requiere el conocimiento del ángulo haz a flujo (ángulo de inclinación ) para producir resultados razonables para flujos regulares y hace un mal trabajo para estimar patrones de flujo complejos, como los debidos a la estenosis y/o la bifurcación. La estimación del caudal volumétrico requiere integrar la velocidad a través de la sección transversal del recipiente, con supuestos sobre la geometría del recipiente, complicando aún más las estimaciones del flujo. Los datos Doppler 2D pueden utilizarse para calcular el caudal volumétrico en determinados planes de integración. El plan de integración se elige para ser perpendicular al haz, y la potencia Doppler (generada a partir del modo Doppler de potencia de la ecografía Doppler ) se puede utilizar para diferenciar entre los componentes que se encuentran dentro y fuera del vaso. Este método no requiere conocimientos previos del ángulo Doppler, el perfil de flujo y la geometría del vaso.

 Promesa del 3D
Hasta hace poco, las imágenes de ecografía eran vistas en 2D y se habían confiado en especialistas altamente entrenados para orientar correctamente la sonda y seleccionar la posición dentro del cuerpo en la imagen con sólo pocos y complejos indicios visuales. La medida completa de vectores de velocidad 3D hace posibles muchas técnicas de postproceso. No sólo se puede medir el flujo volumétrico a través de cualquier plano, sino que también se puede calcular otra información física, como el estrés y la presión, a partir del campo de velocidad 3D. Sin embargo, es bastante difícil medir el flujo sanguíneo complejo para dar vectores de velocidad debido a la velocidad de adquisición rápida y los cálculos masivos necesarios para ello.

 Referencias
