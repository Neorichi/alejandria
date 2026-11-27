---
type: Artículo de enciclopedia
title: U-Net
description: U-Net es una red neuronal convolucional desarrollada para la segmentación de imágenes biomédicas en el Departamento de Informática de la Universidad de Friburgo.
resource: https://es.wikipedia.org/wiki/U-Net
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/U-Net"}
license: CC BY-SA 4.0
id: eswiki-U-Net
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# U-Net

**U-Net** es una red neuronal convolucional desarrollada para la segmentación de imágenes biomédicas en el Departamento de Informática de la Universidad de Friburgo. La red se basa en una red neuronal totalmente convolucional cuya arquitectura se modificó y amplió para trabajar con menos imágenes de entrenamiento y producir una segmentación más precisa. La segmentación de una imagen de 512 × 512 tarda menos de un segundo en una GPU moderna.

La arquitectura U-Net también se ha empleado en modelos de difusión para la eliminación iterativa de ruido en imágenes. Esta tecnología es la base de muchos modelos modernos de generación de imágenes, como DALL-E, Midjourney y Stable Diffusion.

 Descripción
La arquitectura U-Net procede de la denominada "red totalmente convolucional" propuesta por Long, Shelhamer y Darrell en 2014.

La idea principal consiste en complementar una red de contracción habitual con capas sucesivas, en las que las operaciones de agrupamiento se sustituyen por operadores de remuestreo. Así, estas capas aumentan la resolución de la salida. A continuación, una capa convolucional sucesiva puede aprender a ensamblar una salida precisa basándose en esta información.

Una modificación importante en U-Net es que hay un gran número de canales de características en la parte de muestreo ascendente, que permiten a la red propagar la información de contexto a capas de mayor resolución. Como consecuencia, la ruta expansiva es más o menos simétrica a la parte de contracción, y da lugar a una arquitectura en forma de U. La red sólo utiliza la parte válida de cada convolución, sin capas totalmente conectadas. Para predecir los píxeles de la región fronteriza de la imagen, el contexto que falta se extrapola reflejando la imagen de entrada. Esta estrategia de mosaico es importante para aplicar la red a imágenes de gran tamaño, ya que de otro modo la resolución se vería limitada por la memoria de la GPU.

 Historia
U-Net fue creada por Olaf Ronneberger, Philipp Fischer y Thomas Brox en 2015 y publicada en el artículo "U-Net: Convolutional Networks for Biomedical Image Segmentation". Es una mejora y desarrollo de FCN: Evan Shelhamer, Jonathan Long, Trevor Darrell (2014). "Redes totalmente convolucionales para la segmentación semántica".

 Arquitectura de red
La red consta de una ruta de contracción y una ruta expansiva, lo que le confiere la arquitectura en forma de u. La ruta de contracción es una red convolucional típica que consiste en la aplicación repetida de convoluciones, cada una de ellas seguida de una unidad lineal rectificada (ReLU) y una operación de agrupación máxima. Durante la contracción, la información espacial se reduce mientras que la información de características aumenta. La vía expansiva combina la información espacial y de rasgos mediante una secuencia de convoluciones ascendentes y concatenaciones con rasgos de alta resolución procedentes de la vía de contracción.

 Aplicaciones

Existen muchas aplicaciones de U-Net en la segmentación de imágenes biomédicas, como la segmentación de imágenes cerebrales (*BRATS*) y la segmentación de imágenes hepáticas (*siliver07*), así como la predicción de sitios de unión de proteínas. Las implementaciones de U-Net también han encontrado uso en las ciencias físicas, por ejemplo en el análisis de micrografías de materiales. También se han aplicado variaciones de U-Net para la reconstrucción de imágenes médicas. A continuación se presentan algunas variantes y aplicaciones de U-Net:

 Regresión por píxeles mediante U-Net y su aplicación al enfoque panorámico;
 3D U-Net: Aprendizaje de segmentación volumétrica densa a partir de anotación dispersa;
 TernausNet: U-Net con codificador VGG11 preentrenado en ImageNet para segmentación de imágenes.
 Traducción de imagen a imagen para estimar las manchas fluorescentes.
 En la predicción de sitios de unión de la estructura de las proteínas.

 Referencias

 Variantes modernas y aplicaciones clínicas
U-Net ha demostrado un rendimiento excepcional incluso con conjuntos de datos de entrenamiento pequeños, algo común en medicina. Sus principales variantes modernas incluyen:
 **nnU-Net** (no-new-U-Net): una versión auto-configurable que ajusta automáticamente los hiperparámetros según el conjunto de datos, dominando competiciones internacionales de segmentación médica.
 **Attention U-Net**: incorpora mecanismos de atención que permiten a la red enfocarse en regiones relevantes de la imagen, mejorando la segmentación de estructuras pequeñas.

Las **conexiones de salto** (*skip connections*) constituyen la innovación arquitectónica clave de U-Net: conectan directamente capas del encoder con capas correspondientes del decoder, transfiriendo información de alta resolución que se perdería durante la compresión. Esto permite combinar el contexto semántico ("qué" hay en la imagen) con la localización precisa ("dónde" está).

En medicina, U-Net se utiliza rutinariamente para:
 Segmentación de cáncer de mama en mamografías y ultrasonido.
 Delimitación de órganos en riesgo para planificación de radioterapia.
 Segmentación de núcleos celulares en patología digital.

 Implementaciones
 Tensorflow Unet by J Akeret (2017)
 U-Net source code from Pattern Recognition and Image Processing at Computer Science Department of the University of Freiburg, Germany.
