---
type: Artículo de enciclopedia
title: Nicholas Carlini
description: Nicholas Carlini es un investigador afiliado a Google DeepMind que ha publicado investigaciones en los campos de la seguridad informática y el aprendizaje automático.
resource: https://es.wikipedia.org/wiki/Nicholas_Carlini
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nicholas_Carlini"}
license: CC BY-SA 4.0
id: eswiki-Nicholas_Carlini
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nicholas Carlini

- **Título tesis:** Evaluación y diseño de defensas robustas de redes neuronales
- **Año tesis:** 2018 - Universidad de California en Berkeley
- **Supervisor doctoral:** David Wagner

**Nicholas Carlini** es un investigador afiliado a Google DeepMind que ha publicado investigaciones en los campos de la seguridad informática y el aprendizaje automático. Es conocido por su trabajo en aprendizaje automático antagónico, particularmente su trabajo en el ataque Carlini & Wagner en 2016. Este ataque fue particularmente útil para derrotar la destilación defensiva, un método utilizado para aumentar la robustez del modelo, y desde entonces ha sido efectivo contra otras defensas contra la entrada adversaria. En 2018, demostró un ataque al modelo DeepSpeech de Mozilla, mostrando que se podían incorporar comandos ocultos en las entradas de voz, que el modelo ejecutaría incluso si fueran inaudibles para los humanos. También dirigió un equipo en UC Berkeley que rompió con éxito siete de las once defensas contra ataques adversarios presentadas en la Conferencia Internacional sobre Representaciones de Aprendizaje de 2018.

Además de su trabajo sobre ataques antagónicos, ha realizado contribuciones significativas para comprender los riesgos de privacidad de los modelos de aprendizaje automático. En 2020, reveló que los modelos de lenguaje grandes, como GPT-2, podrían memorizar y generar información de identificación personal. Su investigación demostró que este problema empeoraba con modelos más grandes y luego mostró vulnerabilidades similares en modelos de imágenes generativas, como Stable Diffusion.

 Biografía
Nicholas Carlini obtuvo su Licenciatura en Ciencias de la Computación y Matemáticas de la Universidad de California, Berkeley, en 2013. Posteriormente continuó sus estudios en la misma universidad, donde realizó un doctorado bajo la supervisión de David Wagner, finalizándolo en 2018. Se hizo conocido por su trabajo en aprendizaje automático antagónico. En 2016, trabajó junto a Wagner para desarrollar el ataque Carlini & Wagner, un método para generar ejemplos antagónicos contra modelos de aprendizaje automático. Se demostró que el ataque es útil contra la destilación defensiva, un mecanismo popular en el que se entrena un modelo de estudiante basándose en las características de un modelo padre para aumentar la solidez y la generalización de los modelos de estudiante. El ataque ganó popularidad cuando se demostró que la metodología también era efectiva contra la mayoría de las otras defensas, volviéndolas ineficaces. En 2018, Carlini demostró un ataque contra el modelo DeepSpeech de Mozilla Foundation, donde mostró que al ocultar comandos maliciosos dentro de la entrada de voz normal, el modelo de voz respondería a los comandos ocultos incluso cuando los comandos no fueran discernibles para los humanos. Ese mismo año, Carlini y su equipo de la Universidad de California en Berkeley demostraron que, de los 11 artículos que presentaban defensas a ataques adversarios aceptados en la conferencia ICLR de ese año, siete de las defensas podían romperse.

Desde 2021, él y su equipo han estado trabajando en un modelo extenso de lenguaje, creando un cuestionario en el que los humanos generalmente obtuvieron un puntaje del 35%, mientras que los modelos de IA obtuvieron un puntaje del 40%, y GPT-3 obtuvo un 38% que podría mejorarse al 40% mediante algunas indicaciones. El modelo con mejor rendimiento en la prueba fue UnifiedQA, un modelo desarrollado por Google específicamente para preguntas de respuesta y conjuntos de respuestas. También ha desarrollado métodos para hacer que grandes modelos de lenguaje como ChatGPT respondan preguntas dañinas como cómo construir bombas.

También es conocido por su trabajo estudiando la privacidad de los modelos de aprendizaje automático. En 2020, demostró por primera vez que los modelos extensos de lenguaje memorizarían algunos datos de texto con los que fueron entrenados. Por ejemplo, descubrió que GPT-2 podía generar información de identificación personal. Luego dirigió un análisis de modelos más grandes y estudió cómo la memorización aumentaba con el tamaño del modelo. Luego, en 2022, mostró la misma vulnerabilidad en los modelos de imágenes generativas, y específicamente en los modelos de difusión, al demostrar que Stable Diffusion podía generar imágenes de los rostros de las personas en las que fue entrenado. Luego de esto, Carlini demostró que ChatGPT a veces también generaba copias exactas de las páginas web en las que fue entrenado, incluida información de identificación personal. Algunos de estos estudios han sido citados desde entonces por los tribunales al debatir el estatus de los derechos de autor de los modelos de IA.

 Otros trabajos
Recibió el premio Best of Show en el IOCCC 2020 por implementar un juego de tres en línea completamente con llamadas a printf, ampliando el trabajo de un artículo de investigación suyo de 2015. Los jueces comentaron sobre su presentación: «El Best of Show de este año (carlini) es una forma tan novedosa de ofuscación que merecería una mención especial en la (futura) lista Best of IOCCC».

 Premios

 Premio al mejor artículo de estudiantes, IEEE S&P 2017 («Hacia la evaluación de la robustez de las redes neuronales«)
 Premio al mejor artículo, ICML 2018 («Los gradientes ofuscados dan una falsa sensación de seguridad: cómo eludir las defensas ante ejemplos adversarios»)
 Premio al mejor artículo, USENIX 2021 («Envenenamiento del conjunto de datos no etiquetados del aprendizaje semisupervisado»)
 Premio al mejor artículo, USENIX 2023 («Auditoría estricta del aprendizaje automático diferencialmente privado»)
 Premio al mejor artículo, ICML 2024 («Robo de parte de un modelo de lenguaje de producción»)
 Premio al mejor artículo, ICML 2024 («Consideraciones para el aprendizaje privado diferencial con preentrenamiento público a gran escala»)

 Referencias
