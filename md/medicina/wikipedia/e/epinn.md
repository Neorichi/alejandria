---
type: Artículo de enciclopedia
title: EpiNN
description: EpiNN (Epigenetic Neural Network) es un algoritmo de aprendizaje profundo diseñado para identificar regiones genómicas relevantes para el sistema inmunitario utilizando datos epigenéticos.
resource: https://es.wikipedia.org/wiki/EpiNN
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/EpiNN"}
license: CC BY-SA 4.0
id: eswiki-EpiNN
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# EpiNN

**EpiNN** (*Epigenetic Neural Network*) es un algoritmo de aprendizaje profundo diseñado para identificar regiones genómicas relevantes para el sistema inmunitario utilizando datos epigenéticos. Este método integra herramientas de bioinformática y aprendizaje supervisado para explorar cómo la regulación epigenética afecta a los genes implicados en la inmunidad adaptativa e innata. EpiNN ha demostrado ser efectivo en la identificación de loci genómicos asociados con enfermedades autoinmunes y otros rasgos relacionados con el sistema inmunitario, destacando por su capacidad de anotar genes relevantes para el sistema inmunitario, a partir de datos epigenéticos.

 Diseño y arquitectura
**EpiNN** utiliza una red neuronal convolucional (*CNN*) que toma como entrada datos epigenéticos procesados del proyecto Epigenome Roadmap. Estos datos se codifican como imágenes RGB, en las que los colores representan 15 estados epigenéticos derivados de *ChromHMM*. Las filas de estas imágenes corresponden a 111 tipos de tejidos y células, mientras que las columnas representan segmentos de 200 pares de bases del genoma humano.

El modelo está entrenado a partir de una lista elaborada a mano de 888 genes relacionados con el sistema inmunitario, elegidos por su relevancia en procesos biológicos como la identidad celular inmune y el ciclo inmunitario. Durante el entrenamiento, EpiNN aprende a identificar patrones epigenéticos que caracterizan regiones genómicas relacionadas con funciones inmunitarias lógicas. Una vez entrenado, el modelo asigna una puntuación a cada región genómica basada en la probabilidad de que esté implicada en funciones del sistema inmunitario, pudiendo predecir así regiones relevantes para el sistema inmunitario.

 Funcionalidad
El algoritmo se centra en analizar marcadores epigenéticos clave, como H3K4me3 (asociado a promotores activos) y H3K27me3 (vinculado a represión génica). Estas marcas permiten a EpiNN identificar regiones reguladoras no codificantes que desempeñan un papel crucial en la expresión génica.

Al realizar el análisis sobre todo el genoma con esta aproximación, EpiNN detectó 2765loci relevantes para el sistema inmunitario, incluyendo genes y regiones previamente no caracterizados. Entre sus predicciones, EpiNN fue capaz de identificar un posible nuevo sitio de inicio de transcripción específico de células inmunes en el *gen DNMT1*, conocido por su papel en la metilación del ADN.

 Aplicaciones
EpiNN presenta múltiples aplicaciones en investigación biomédica y desarrollo clínico:

 **Identificación de loci relacionados con enfermedades inmunitarias**:  EpiNN ha demostrado ser particularmente útil para identificar regiones genómicas asociadas con enfermedades autoinmunes como la artritis reumatoide, la enfermedad de Crohn y la esclerosis múltiple. Las anotaciones EpiNN también han demostrado estar enriquecidas para la herencia en rasgos relevantes para el sistema inmune adaptativo e innato.

 **Medicina personalizada y estudios de población**:  Al ser capaz de detectar efectos genéticos específicos en distintas poblaciones, EpiNN puede contribuir al desarrollo de terapias personalizadas basadas en la susceptibilidad genética. Por ejemplo, ha identificado diferencias significativas entre poblaciones europeas y asiáticas en loci inmunitarios clave, indicando posibles interacciones gen‑ambiente.

 **Descubrimiento de nuevas dianas fármacos**:  El uso de EpiNN podría ayudar al desarrollo de nuevos fármacos por su capacidad para identificar regiones relevantes para el sistema inmune y enfermedades inmunitarias, que podrían servir de futuras dianas terapéuticas.

 **Mayor conocimiento de otras patologías**:  Además de su relevancia en enfermedades autoinmunes, las regiones anotadas por EpiNN han mostrado asociación con otras patologías, como enfermedades respiratorias y dermatológicas, donde la inmunidad desempeña un papel central.

 **Comprensión de la regulación epigenética en células del sistema inmunitario**:  EpiNN complementa métodos tradicionales basados en la transcripción al identificar regiones no codificantes con funciones regulatorias clave. Esto incluye la anotación de ARN largos no codificantes (*lncRNAs*) y microARNs, ambos implicados en la respuesta inmune.

 Ventajas frente a otros métodos tradicionales
EpiNN presenta varias ventajas en comparación con otras herramientas existentes como *IRIS* o *ImmunoGene*, que están basadas en datos de expresión génica:
 **Aporta información novedosa**: Tiene en cuenta los datos epigenéticos, y no únicamente datos de transcriptómica, mostrando tamaños de efecto para la heredabilidad significativamente mayores mediante las anotaciones EpiNN que con las otras anotaciones.
 **Mayor sensibilidad para regiones no codificantes**: Identifica regiones que no afectan directamente a proteínas, pero que son cruciales para la regulación génica.
 **Capacidad para la detección de regiones inmunorrelevantes en múltiples poblaciones**: Permite analizar diferencias genéticas entre poblaciones, lo cual es fundamental para estudios de diversidad genética y desarrollo de terapias globales.

 Referencias

 Véase también
 Epigenética
 Red neuronal convolucional
 Sistema inmunitario
 Enfermedades autoinmunes
