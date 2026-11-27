---
type: Artículo de enciclopedia
title: Biochip fenotípico
description: "El biochip fenotípico (en inglés: phenotype microarrays) es una tecnología de alto rendimiento usada para la caracterización fenotípica de células sobre microplaca."
resource: https://es.wikipedia.org/wiki/Biochip_fenotípico
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Biochip_fenotípico"}
license: CC BY-SA 4.0
id: eswiki-Biochip_fenotípico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Biochip fenotípico

El **biochip fenotípico** (en inglés: phenotype microarrays) es una tecnología de alto rendimiento usada para la caracterización fenotípica de células sobre microplaca. A través de este sistema de biochips fenotípicos pueden monitorearse simultáneamente un elevado número de respuestas fenotípicas celulares a fuentes de carbono, de nitrógeno, de fósforo o de resistencia  a diversos componentes. Estas reacciones fenotípicas se registran durante toda la cinética respiratoria celular (similar a la curva de crecimiento celular) o en su punto final.

 Usos
El uso de los biochips fenotípicos de alto rendimiento tiene una gran importancia en la caracterización metabólica de bacterias, hongos, levaduras y líneas celulares animales, tales como células tumorales humanas. Al igual que los biochips de ADN (del inglés, DNA microarrays) o de proteínas  pueden ensayar miles de genes o proteínas al mismo tiempo, los biochips fenotípicos (PMs) miden cuantitativamente miles de fenotipos celulares a la vez. Asimismo, los biochips fenotípicos también poseen potencial para ser usados en el análisis funcional de genes o para mejorar la anotación de genomas. Sin embargo, al contrario de las tecnologías moleculares de alto rendimiento disponibles hasta ahora, los biochips fenotípicos usan células vivas, lo que proporciona una información más completa de la biología de la célula. Las principales aplicaciones de esta tecnología se centran en el campo de la biología de sistemas, de la fisiología y taxonomía microbiana y en el estudio fisiológico de células madre humanas.
Una de las principales ventajas de los PMs sobre las curvas de crecimiento celulares es que la respiración celular puede ser medida en condiciones ambientales donde la división celular y por ende, el crecimiento no son posibles. Asimismo, las reacciones respiratorias se detectan normalmente antes que las curvas de crecimiento.

 Tecnología
Una fuente de carbono dispuesta en un pocillo de la microplaca puede ser transportada al interior celular y metabolizada,  produciendo NADH  que dará lugar a un potencial redox y a un flujo de electrones que reducirán el indicador de tetrazolio (ej. tetrazolio violeta), provocando así la aparición de un color violeta en el pocillo. Cuanto más rápido sea el metabolismo de una célula, más rápida será la aparición del color en la microplaca. La aparición del color violeta se considera un resultado positivo, significando que la fuente de carbono es utilizada por la célula como fuente de energía.  No obstante, las microplacas deben ser incubadas en condiciones apropiadas, disponiendo de un lector automático que registre las lecturas de la intensidad del color formado durante la reducción del indicador de tetrazolio en cada periodo de tiempo determinado, por ejemplo a intervalos de 15 minutos.
Todo lo anterior referente al uso por parte de un organismo de una determinada fuente de carbono puede aplicarse a otros macronutrientes como fuentes de nitrógeno, de sulfuro o de fósforo y sus derivativos, así como al efecto de suplementos auxótrofos, antibióticos, metales pesados u otros componentes inhibitorios sobre la respiración celular.

 Estructura de datos
En las reacciones positivas, las cinéticas respiratorias aparecen como curvas sigmoidales análogas a las típicas curvas de crecimiento celular. De esta manera, y al igual que en las curvas de crecimiento celular, las curvas de respiración celular encierran valiosa información en la longitud de la fase de latencia  λ, la tasa de respiración μ (pendiente de la curva), el máximo valor de respiración celular A y el área bajo la curva (del inglés, area under the curve AUC). No obstante, al contrario de las curvas de crecimiento celulares, no existe la típica fase de muerte celular, ya que el indicador reducido de tetrazolio es insoluble.

 Aplicación informática
Ya se encuentran comercialmente disponibles aplicaciones informáticas que solucionan el almacenaje, la recuperación y análisis de los datos fenotípicos procedentes de las tecnologías de alto rendimiento. El paquete libre “opm”, basado en R, es una poderosa aplicación informática que contiene las herramientas necesarias para analizar los datos obtenidos de PM, incluyendo manejo, visualización y análisis estadísticos de los datos fenotípicos, estimación de los parámetros de las curvas de respiración, generación y edición de gráficos, manejo de metadatos, generación automática de informes taxonómicos, discretización de datos para fines filogenéticos y la posibilidad de exportar al formato YAML la información analizada. El paquete “opm” ha sido desarrollado y es mantenido por la Colección Alemana de Microorganismos y Cultivos Celulares (del alemán *Deutsche Sammlung von Mikroorganismen und Zellkulturen*). Otras aplicaciones informáticas son PheMaDB, que proporciona una solución al almacenaje, recuperación y análisis de los datos fenotípicos de alto rendimiento, y PMViewer, centrado en la representación gráfica de los mismos, sin embargo ninguno de ellos ofrece la posibilidad de analizar estadísticamente los datos fenotípicos (no publicado).

 Referencias

 Enlaces externos
 opm website  at the DSMZ
 opm website  at the Comprehensive R Archive Network repository
 PheMaDB website
