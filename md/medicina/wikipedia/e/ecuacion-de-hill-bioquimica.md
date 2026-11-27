---
type: Artículo de enciclopedia
title: Ecuación de Hill (bioquímica)
description: En bioquímica y farmacología, la ecuación de Hill hace referencia a dos formulaciones estrechamente relacionadas que describen la unión de ligandos a macromoléculas en función de la concentración del ligando.
resource: https://es.wikipedia.org/wiki/Ecuación_de_Hill_(bioquímica)
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ecuación_de_Hill_(bioquímica)"}
license: CC BY-SA 4.0
id: eswiki-Ecuación_de_Hill_(bioquímica)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ecuación de Hill (bioquímica)

En bioquímica y farmacología, la **ecuación de Hill** hace referencia a dos formulaciones estrechamente relacionadas que describen la unión de ligandos a macromoléculas en función de la concentración del ligando. Un ligando se define como una sustancia que forma un complejo con una biomolécula para cumplir una función biológica, mientras que una macromolécula es una molécula de gran tamaño, como una proteína, caracterizada por una organización estructural compleja. La unión proteína–ligando suele modificar la estructura de la proteína diana, modificando así su función celular.

La distinción entre las dos ecuaciones de Hill radica en si miden *la ocupación* o *la respuesta.* La **ecuación de Hill** refleja la ocupación de las macromoléculas: la fracción saturada o unida por el ligando.   Esta ecuación es formalmente equivalente a la isoterma de Langmuir. Por el contrario, la **ecuación de Hill** propiamente dicha refleja la respuesta celular o tisular al ligando: la salida fisiológica del sistema, como la contracción muscular.

La ecuación de Hill fue formulada originalmente por Archibald Hill en 1910 para describir la curva sigmoidea de unión de O2 a la hemoglobina.

La unión de un ligando a una macromolécula suele ser mayor si ya existen otros ligandos presentes en la misma macromolécula (esto se conoce como unión cooperativa). La ecuación de Hill es útil para evaluar el grado de cooperatividad en la unión de uno o varios ligandos a una enzima o receptor. El **coeficiente de Hill** permite cuantificar el nivel de interacción entre los distintos sitios de unión de los ligandos.

La ecuación de Hill (para la respuesta) es importante en la construcción de curvas dosis-respuesta.

 Proporción de receptores unidos a ligando

La ecuación de Hill se expresa comúnmente de las siguientes maneras:

 ,

dónde

  = fracción de la concentración de la proteína receptora que está unida al ligando.
 [L] = concentración total de ligando.
  = constante de disociación aparente, derivada de la ley de acción de masas.
  = concentración de ligando que produce la ocupación del 50% de los sitios de unión.
  = coeficiente de Hill

El caso especial donde  es una ecuación de Monod.

 Constantes
En farmacología, θ a menudo se denota como , donde A es el ligando (equivalente a L) y R el receptor.  puede expresarse como la fracción del receptor total que está unido al ligando:  .  se define como la relación entre la tasa de disociación (kd) del complejo ligando-receptor y su tasa de asociación (ka):  ).  Kd es la constante de equilibrio para la disociación.  se define de manera que , Esto también se conoce como constante de disociación microscópica y es la concentración de ligando que ocupa la mitad de los sitios de unión. En la literatura reciente, esta constante a veces se denomina .

 Ecuación de Gaddum
La ecuación de Gaddum es una generalización adicional de la ecuación de Hill, que incorpora la presencia de un antagonista competitivo reversible. La ecuación de Gaddum se deriva de forma similar a la ecuación de Hill, pero con 2 equilibrios: el del ligando con el receptor y el del antagonista con el receptor. Por lo tanto, la ecuación de Gaddum tiene dos constantes: las constantes de equilibrio del ligando y la del antagonista.

 Gráfico de Hill

El gráfico de Hill es la reorganización de la ecuación de Hill en una línea recta.

Tomando el recíproco de ambos lados de la ecuación de Hill, reordenando e invirtiendo nuevamente se obtiene: . Tomando el logaritmo de ambos lados de la ecuación conduce a una formulación alternativa de la ecuación de Hill-Langmuir:

 .

Esta última forma de la ecuación de Hill es ventajosa porque una gráfica de ***' versus  produce un gráfico lineal, que se denomina **gráfico de Hill.*' Debido a que la pendiente de un gráfico de Hill es igual al coeficiente de Hill para la interacción bioquímica, la pendiente se denota por  . Por tanto, una pendiente mayor que uno indica una unión cooperativa positiva entre el receptor y el ligando, mientras que una pendiente menor que uno indica una unión cooperativa negativa.

 Respuesta tisular

Se debe distinguir entre la cuantificación de la unión de fármacos a receptores y la cuantificación de la respuesta de fármacos. Puede que no exista necesariamente una relación lineal entre ambos valores. A diferencia de la definición previa de la ecuación de Hill en este artículo, la IUPHAR define la ecuación de Hill en términos de la respuesta tisular , como   Donde [A] representa la concentración del fármaco,  es el coeficiente de Hill y corresponde a la concentración del fármaco que produce el 50 % de la respuesta máxima. Mientras que las constantes de disociación (descritas en la sección anterior) se refieren al proceso de unión del ligando, la  refleja la respuesta tisular.

Esta forma de la ecuación puede reflejar las respuestas de los tejidos, células y poblaciones a los fármacos y puede utilizarse para generar curvas de dosis-respuesta. La relación entre  y la CE50 puede ser bastante compleja ya que una respuesta biológica será la suma de innumerables factores; un fármaco tendrá un efecto biológico diferente si hay más receptores presentes, independientemente de su afinidad.

El modelo de Del Castillo–Katz se emplea para vincular la ecuación de Hill con la activación del receptor, al introducir un segundo equilibrio entre el receptor unido al ligando y su forma activada.

El análisis estadístico de la respuesta en función del estímulo puede realizarse mediante métodos de regresión, como el modelo *probit* o el modelo *logit**,* u otros procedimientos como el método de Spearman-Kärber. Los modelos empíricos basados en regresión no lineal suelen preferirse frente a la aplicación de transformaciones de los datos que linealicen la relación dosis–respuesta.

 Coeficiente de Hill
El coeficiente de Hill es una medida de ultrasensibilidad (es decir, qué tan pronunciada es la curva de respuesta).

El coeficiente de Hill,  o , puede describir la cooperatividad (o posiblemente otras propiedades bioquímicas, dependiendo del contexto en el que se utilice la ecuación de Hill). Cuando corresponda, el valor del coeficiente de Hill describe la cooperatividad de la unión del ligando de la siguiente manera:

 . **Unión cooperativa positiva**: Una vez que una molécula de ligando se une a la enzima, su afinidad por otras moléculas de ligando aumenta. Por ejemplo, el coeficiente de Hill para la unión de oxígeno a la hemoglobina (un caso de cooperatividad positiva) se encuentra en el rango de 1,7–3,2
 . **Unión cooperativa negativa**: Una vez que una molécula de ligando se une a la enzima, su afinidad por otras moléculas de ligando disminuye.
 . **Unión no cooperativa (completamente independiente)**: La afinidad de la enzima por una molécula de ligando no depende de si otras moléculas de ligando ya están unidas. Cuando n=1, se obtiene un modelo que puede describirse mediante la cinética de Michaelis–Menten, en el cual: , siendo *Kₘ* la constante de Michaelis–Menten.

El coeficiente de Hill se puede calcular aproximadamente en términos del *índice de cooperatividad* de Taketa y Pogell  de la siguiente manera:

 .

dónde CE90 y CE10 son los valores de entrada necesarios para producir el 10% y el 90% de la respuesta máxima, respectivamente.
 Forma reversible
La forma más común de la ecuación de Hill es su forma irreversible. Sin embargo, al construir modelos computacionales, a menudo se requiere una forma reversible para modelar la inhibición del producto. Por esta razón, Hofmeyr y Cornish-Bowden idearon la ecuación de Hill reversible.

 Relación con los coeficientes de elasticidad
El coeficiente de Hill también está íntimamente relacionado con el coeficiente de elasticidad, donde se puede demostrar que el coeficiente de Hill es igual a:

dónde  es la saturación fraccionaria, , y  el coeficiente de elasticidad.

Esto se obtiene tomando la pendiente de la ecuación de Hill:

y expandiendo la pendiente usando la regla del cociente. El resultado muestra que la elasticidad nunca puede exceder  ya que la ecuación anterior se puede reorganizar como:

 Aplicaciones
La ecuación de Hill se utiliza ampliamente en farmacología para cuantificar los parámetros funcionales de un fármaco. y también se utilizan en otras áreas de la bioquímica.

La ecuación de Hill puede usarse para describir relaciones dosis-respuesta, por ejemplo, la probabilidad de apertura de un canal iónico (P-abierto) frente a la concentración de ligando.

 Regulación de la transcripción genética
La ecuación de Hill puede aplicarse para modelar la velocidad de producción de un producto génico cuando su gen regulador está controlado por factores de transcripción (por ejemplo, activadores y/o represores). Esto resulta adecuado cuando un gen está regulado por múltiples sitios de unión para factores de transcripción, en cuyo caso los factores de transcripción pueden unirse al ADN de manera cooperativa.

Si la producción de proteína del gen  es regulada positivamente (**activada**) por un factor de transcripción , entonces la tasa de producción de proteína  se puede modelar como una ecuación diferencial en términos de la concentración de proteína  activada:

 ,

donde  es la tasa máxima de transcripción del gen

De la misma manera, si la producción de proteína del gen  es regulada negativamente (**reprimida**) por un factor de transcripción , entonces la tasa de producción de proteína  puede modelarse como una ecuación diferencial en términos de la concentración de proteína  activada:

 ,

donde  es la tasa máxima de transcripción del gen

 Limitaciones
Debido a su suposición de que las moléculas de ligando se unen al receptor simultáneamente, la ecuación de Hill ha sido criticada como un modelo físicamente poco realista, Además, el coeficiente de Hill no debe considerarse una aproximación confiable del número de sitios de unión cooperativos de un ligando en un receptor excepto en los casos en que la unión del primer ligando y de los posteriores resulte en una cooperatividad positiva extrema.

A diferencia de modelos más complejos, la relativamente simple ecuación de Hill ofrece poca información sobre los mecanismos fisiológicos subyacentes de las interacciones proteína-ligando. Sin embargo, esta simplicidad es lo que la convierte en un modelo empírico útil, ya que su uso requiere poco conocimiento *previo* sobre las propiedades de la proteína o el ligando estudiado. No obstante, se han propuesto otros modelos más complejos de unión cooperativa.

Las medidas de sensibilidad global, como el coeficiente de Hill, no caracterizan el comportamiento local de las curvas en forma de S. En cambio, estas características se reflejan adecuadamente en la medida del coeficiente de respuesta.

Existe un vínculo entre el coeficiente de Hill y el coeficiente de Respuesta, como se muestra a continuación. Altszyler et al. (2017) han demostrado que estas medidas de ultrasensibilidad pueden estar relacionadas.

 Coeficiente de unión
 Gráfico de Bjerrum
 Unión cooperativa
 Curva de Gompertz
 Modelo de adsorción de Langmuir
 Función logística
 Cinética de Michaelis-Menten
 Ecuación de Monod

 Referencias

 Enlaces externos
 Calculadora de ecuaciones de Hill
