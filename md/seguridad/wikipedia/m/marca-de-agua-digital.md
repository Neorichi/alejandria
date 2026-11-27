---
type: Artículo de enciclopedia
title: Marca de agua digital
description: La marca de agua digital es una técnica esteganográfica de ocultación de información.
resource: https://es.wikipedia.org/wiki/Marca_de_agua_digital
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Marca_de_agua_digital"}
license: CC BY-SA 4.0
id: eswiki-Marca_de_agua_digital
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Marca de agua digital

La **marca de agua digital** es una técnica esteganográfica de ocultación de información. Su objetivo principal es poner de manifiesto el uso ilícito de cierto servicio digital por parte de un usuario no autorizado.

Concretamente, esta técnica consiste en insertar un mensaje (oculto o no) en el interior de un objeto digital (imágenes, audio, vídeo, texto, software), un grupo de bits que contiene información sobre el autor o propietario intelectual del objeto digital tratado (copyright).

Otra técnica relacionada es la huella digital, donde se introduce en el objeto digital una marca que además de contener información sobre el copyright, contiene información del usuario que ha adquirido los derechos de uso de ese objeto. De esta forma se puede perseguir la distribución ilegal de servicios digitales.

 Características
Una técnica de marca de agua debe cumplir los siguientes requisitos:

 ser imperceptible: invisible/visible al observador;
 no debe degradar el objeto que pretende proteger;
 debe ser robusta: la eliminación o reducción de la marca no debe ser difícil o idealmente posible sin degradar la calidad del objeto digital; asimismo, debe soportar procesos habituales de transformación (compresión, filtrado, conversión de formato, distorsión geométrica, etcétera, y
 no debe ser ambigua: la marca debe identificar inequívocamente al propietario intelectual, de tal forma que este pueda reclamar su pertenencia.

Pese a estas premisas, también existen marcas de agua que son perceptibles y que degradan el objeto, como por ejemplo las marcas de agua superpuestas a imágenes que indican la propiedad de las mismas.

 Generación y detección
El diagrama de generación de un objeto marcado será el siguiente:

Asimismo, el proceso inverso, para saber si un objeto está marcado o no, y por tanto obtener la información almacenada en dicha marca, será:

 Clasificación

Una marca de agua es llamada "robusta" con respecto a una transformación, si la información incrustada puede ser detectada confiablemente de la señal marcada.

 Robustez

Una marca de agua es llamada "fragil", si falla en ser detectada después de leves modificaciones. Las marcas de agua frágil son comúnmente usadas para las detección de falsificaciones.

 Perceptibilidad

Una marca de agua es llamada "imperceptible", si la señal de cubierta original y la señal marcada son perceptualmente indistinguible.

 Capacidad

Se refiere a la cantidad de información que puede ser oculta en una unidad de tiempo o en un portador.

 Tipos
Para la extracción de la información contenida en la marca (M) o para conocer si un objeto está marcado o no con una información concreta, se necesitan ciertos datos. En función de éstos y de lo que se desea obtener, hay distintos tipos de marca de agua digital:

 **Privada:** se necesita tener el objeto original (I)
 Tipo I:
 Tipo II:

 **Semiprivada:** se necesita tener la marca (M)

 **Pública:** no necesita ni del objeto original (I) ni la marca (M)

 **Visible:** en estos casos, la marca de agua digital es visible y deteriora el objeto digital, mediante la clave (K) podemos obtener el objeto original sin pérdidas debido a la marca.

 Técnicas
Se conocen dos grandes tipos de técnicas de marca de agua digital:

 **Técnicas espaciales**: implican la modificación de algún componente en el dominio espacial, son fáciles de implementar y son frágiles frente a ataques (ejemplo: sustitución de bits de menor peso).
 **Técnicas espectrales**: implican la modificación de algún componente en el dominio transformado frecuencial, son complicadas de implementar y robustas frente a modificaciones. (ejemplos: modificación de los coeficientes DCT, ensanchamiento de espectro, etcétera).

 Ejemplos
Algunos ejemplos de inserción de marcas en objetos concretos son los siguientes. (En el caso de imágenes y audio, la inserción de dichas marcas no tienen por qué influir en su representación visual o auditiva.)

**Imágenes**
 Modificación del bit de menor peso (LSB: *less significant bit*) de algunos pixeles de la imagen, elegidos mediante una secuencia seudoaleatoria (S. Walton). Al tratarse del bit de menor peso de un píxel, éste se ve sometido a un cambio imperceptible de color.
 Modificación de los coeficientes de la DCT (*Discrete Cosinus Transformation* o transformada discreta de coseno) (Tirkel *et al.*).
 Ensanchamiento del espectro frecuencial (Cox *et al.*)

**Audio**
 Modificación del bit de menor peso de algunas muestras del archivo de sonido, elegidos mediante una secuencia seudoaleatoria
 Ensanchamiento del espectro frecuencial
 Ocultación de eco (D. Gruhl *et al.*)

**Texto**
 Modificación del espaciado entre líneas
 Modificación del espaciado entre palabras

 Ataques
Estas técnicas serán susceptibles a diversos ataques, que se diferenciarán en tipos según su objetivo:

 **Ataques a la robustez:** Se logran reduciendo o eliminando completamente la presencia de la marca. Por ejemplo, en una imagen, si la marca se halla en los LSB de algunos pixeles, al cambiar dichos LSB en *todos* los pixeles de la imagen, la marca queda totalmente eliminada.
 **Ataques a la presentación:** modificando el objeto digital de forma que no se pueda detectar la marca. Como indica su nombre, dicha marca será visible.
 **Ataques a la interpretación:** crear una situación, mediante una modificación de la marca, en la cual la propiedad del objeto no pueda ser reclamada por nadie. Por ejemplo, si a un objeto digital que ya tenía una marca se le añade otra nueva, será imposible interpretar cuál se añadió antes y, por tanto, quién es el titular de los derechos del objeto digital.

 Utilidad
Esta todavía es una tecnología joven e inmadura que ofrece posibilidades potenciales y ventajosas a compañías de protección de datos multimedia y de derechos intelectuales (protege frente a la copia ilegal).

Existe una relación de compromiso entre la cantidad de información que puede ser almacenada en una marca y la robustez de dicha marca. Es decir, cuanta más información haya, menos robusta será la marca de agua.

Actualmente, la marca de agua digital no ofrece garantías totales, ya que, como se ha visto, dichas técnicas son vulnerables a ataques malintencionados.

 Véase también
 Huella digital
 Marca de agua
