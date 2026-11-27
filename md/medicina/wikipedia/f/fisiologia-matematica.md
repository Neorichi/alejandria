---
type: Artículo de enciclopedia
title: Fisiología matemática
description: "La fisiología matemática es una ciencia que combina conocimientos de varias áreas (ciencia interdisciplinaria), ya que involucra la fisiología cuantitativa como una herramienta diagnóstica, vinculando modelos …"
resource: https://es.wikipedia.org/wiki/Fisiología_matemática
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Fisiología_matemática"}
license: CC BY-SA 4.0
id: eswiki-Fisiología_matemática
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Fisiología matemática

**La fisiología matemática**  es una ciencia que combina conocimientos de varias áreas (ciencia interdisciplinaria), ya que involucra la fisiología cuantitativa como una herramienta diagnóstica, vinculando modelos matemáticos con la práctica clínica. Investiga principalmente cómo las matemáticas pueden utilizarse para comprender cuestiones fisiológicas, con modelos, que son un conjunto matemático, implementadas en software como modelos computacionales, que generan resultados en función de las entradas. Estas pueden incluir parámetros del modelo, condiciones iniciales, condiciones de contorno y geometría de la célula, del tejido o del órgano completo. Las entradas suelen tener un significado fisiológico y suelen obtenerse mediante medición directa o calibración indirecta a partir de datos experimentales, o bien heredadas de otros modelos o componentes del modelo. Principalmente, investiga formas en que las matemáticas pueden usarse para comprender cuestiones fisiológicas . A su vez, también describe cómo las cuestiones fisiológicas pueden conducir a nuevos problemas matemáticos. El campo puede agruparse en dos áreas de aplicación fisiológica: fisiología celular (incluidos los tratamientos matemáticos de las reacciones bioquímicas, el flujo iónico y la regulación de la función ) y fisiología de sistemas (incluida la electrocardiología, la circulación y la digestión).

 Historia
El trabajo pionero de Hodgkin y Huxley (1952) sobre la generación del potencial de acción (PA) en el axón gigante del calamar. Usando ecuaciones diferenciales acopladas, desarrollaron un modelo que combinaba elementos resistivos y capacitivos para describir los flujos iónicos de Na+ y K+. La contribución fundamental de su trabajo fue el  Modelo matemático del PA mediante ecuaciones diferenciales. El alternar entre modelo y experimento introdujo las bases de la fisiología matemática, que fue el enfoque de Hodgkin y Huxley.

Influenciados por Hodgkin y Huxley, Richard FitzHugh y Wilfrid Rall. FitzHugh simplificaron las ecuaciones de Hodgkin-Huxley a un sistema de dos variables, aportando nuevos conocimientos sobre la dinámica de la excitabilidad y los fenómenos de umbral.

Wilfrid Rall, se considera pionero de la neurociencia computacional, ya que aplicó la teoría del cable para demostrar que la ramificación dendrítica afecta el procesamiento de señales sinápticas. Introdujo el modelado compartimental y fue de los primeros en usar computadoras en neurociencia. Los modelos cuestionaron la idea de que las neuronas poseían un potencial eléctrico homogéneo, revelando el papel clave de las dendritas en dirigir la corriente hacia el soma. A pesar de que sus planteamientos no fueron aceptados de inmediato, nociones como la integración espacial y la disminución del potencial en las dendritas son ahora pilares de la neurociencia.

Hoy en día, el uso de los modelos matemáticos en fisiológica se han diversificado y expandido usando diferentes plataformas virtuales para la realización de los modelados por ejemplo:

 Áreas de aplicación

 Fisiología celular
Algunos ejemplos, se han modelado las oscilaciones de Ca²⁺ mediante ecuaciones diferenciales ordinarias (ODEs), integrando la dinámica de canales iónicos y la liberación de insulina para la señalización intracelular (calcio, AMPc, MAPK), en células β pancreáticas. También se ha propuesto un modelo cinético para la vía MAPK/ERK, incorporando mecanismos de retroalimentación ultrasensible. Se han utilizado enfoques de cinética enzimática en el metabolismo energético (glucólisis, mitocondria) se ha comparado la glucólisis en sistemas *in vivo* e *in silico*  . Además, se han desarrollado simulaciones para estudiar la fosforilación oxidativa y su acoplamiento con el transporte de electrones. Para el ciclo celular y apoptosis las transiciones entre las fases G1, S, G2 y M del ciclo celular se han modelado con ODEs, incluyendo la regulación por ciclinas y quinasas . Por otro lado, se han descrito redes de interacciones entre caspasas y proteínas Bcl-2 para estudiar la apoptosis. Y en el caso del transporte de membrana y canales iónicos se han caracterizado los estados conformacionales de la bomba Na⁺/K⁺ ATPasa, mientras que otros estudios han empleado modelos de Markov para predecir la apertura y cierre estocástico de canales iónicos, entre otros.

 Fisiología de sistemas
Los avances en modelado computacional han transformado la comprensión de sistemas fisiológicos. En electrocardiología, los modelos con ODEs reproducen el potencial de acción ventricular y su correlación con el ECG, mientras que enfoques híbridos combinan redes neuronales con parámetros fisiológicos para detectar isquemias. Los estudios de arritmias emplean PDEs para explicar reentradas espirales y simulaciones 3D realistas guían ablaciones en fibrilación auricular. Paralelamente, la hemodinámica se modela mediante Navier-Stokes para flujo arterial con estenosis y sistemas 1D para propagación de ondas de presión, integrados con ODEs que describen el barorreflejo y control autonómico.  La microcirculación se caracteriza por modelos de difusión de O₂ que consideran hemoglobina y el intercambio capilar mediante ecuaciones de Starling modificadas. En el ámbito digestivo, los modelos metabólicos del microbioma revelan su impacto en enfermedades, complementados con simulaciones de motilidad gastrointestinal que incluyen vaciado gástrico y peristaltismo intestinal. La digestión se cuantifica mediante cinética enzimática de nutrientes y transporte iónico, mientras que modelos PBPK integran estos procesos para predecir absorción de fármacos.

 Referencias

 Enlaces externos
