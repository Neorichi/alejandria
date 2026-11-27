---
type: Artículo de enciclopedia
title: Modelado PBPK
description: "El modelado farmacocinético con base fisiológica (modelado PBPK, por sus siglas en inglés) es una técnica de modelamiento matemático de la farmacocinética para predecir la absorción, distribución, metabolismo y …"
resource: https://es.wikipedia.org/wiki/Modelado_PBPK
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelado_PBPK"}
license: CC BY-SA 4.0
id: eswiki-Modelado_PBPK
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelado PBPK

El **modelado farmacocinético con base fisiológica** (**modelado PBPK***,* por sus siglas en inglés) es una técnica de modelamiento matemático de la farmacocinética para predecir la absorción, distribución, metabolismo y excreción (ADME) de un compuesto en humanos y otras especies animales. El modelado PBPK se usa en investigación y desarrollo farmacéutico, así como en evaluación de riesgo en la salud.

 Descripción

Los modelos PBPK se esfuerzan en ser mecanicistas y matemáticamente transcribir descripciones anatómicas, fisiológicas, físicas, y químicas de los fenómenos de los procesos ADME. Algún grado de simplificación residual y empirismo está todavía presente en esos modelos, pero tienen un dominio extendido de aplicabilidad comparados con los modelos farmacocinéticos clásicos. Dada esa propiedad, modelos PBPK puede tener usos puramente predictivos, excepto otros usos, como la inferencia estadística, que se ha hecho posible por el auge de herramientas estadísticas Bayesianas capaces para ocuparse de modelos complejos. Esto es verdadero para la valoración del riego de toxicidad y auge terapéutico de la droga.

Los modelos PBPK hacen un intento para confiar *a priori* en la estructura anatómica y fisiológica del cuerpo. Estos son usualmente también modelos del multicompartimiento, pero los compartimientos corresponden a los órganos predefinidos o los tejidos finos, para los cuales las interconexiones corresponden a los flujos de sangre o linfa. Un sistema de ecuaciones diferenciales todavía le pueden ser escritos, pero sus parámetros representan flujos sanguíneos, tasa pulmonar de ventilación, volúmenes del órgano, etcétera, información disponible en publicaciones científicas. Ciertamente, la descripción del cuerpo es simplificada y un balance es necesario entre la complejidad y la simplicidad. Además de la ventaja de dejar el reclutamiento de información *a priori* acerca de valores de esos parámetros, estos modelos también facilitan transposiciones interespecies o extrapolación de un modo de administración a otro (por ejemplo, de inhalación a vía oral). Un ejemplo de un modelo PBTK de 7 compartimientos, adecuado para describir el destino de muchos solventes en el cuerpo mamífero, es dado en la figura lateral.

 Historia

Es interesante notar que el primer modelo farmacocinético descrito en la literatura científica fue de hecho un modelo PBPK. Este llevó, sin embargo, a problemas de cómputo intratables para la época. El foco cambió entonces a modelos más simples, para los cuales se podían obtener soluciones analíticas (aquellas soluciones eran sumas de términos exponenciales, que llevaban más adelante a simplificaciones). La disponibilidad de computadores y algoritmos de integración numérica marcaron un renovado interés en los modelos fisiológicos a principios de los 70.

 Usos del modelado PBPK
Los modelos PBPK son modelos compartimentales como muchos otros, pero tienen unas cuantas ventajas sobre los llamados modelos farmacocinéticos "clásicos", que son menos aterrizados en fisiología. Los Modelos PBPK pueden ser usados en primer lugar para abstaer y en algún momento componer información dispar (De experimentos bioquímicos o fisicoquímicos, experimentos toxicológicos o farmacológicos *in vitro* o *in vivo*, etc.). También dan acceso a las concentraciones internas de químicos en sus metabolitos, en particular en el sitio de sus efectos, sean terapéuticos o tóxicos. Finalmente, también ayudan a la interpolación y extrapolación de conocimiento entre:

 Dosis: *p. ej.* de las altas concentraciones ocupadas usualmente en experimentos de laboratorio hacia aquellas encontradas en el ambiente.
 Duración de la exposición: *p. ej.* de continua a discontinua, de una a múltiples exposiciones.
 Rutas de administración: *p. ej.* de exposición a la inhalación, a la ingestión.
 Especies: *p. ej.*, transposiciones de roedores a humanos, antes de dar una droga por primera vez a sujetos en un ensayo clínico, o cuando la experimentación con humanos se considera antiética, como cuando el compuesto es tóxico sin beneficio terapéutico.
 Individuales: *p. ej.*, en machos a hembras, de adultos a niños, de no-embarazadas a embarazadas.

Algunas extrapolaciones son "paramétricas": Solo cambios en los valores de entrada o de parámetros son necesarios para conseguir la correcta extrapolación (usualmente casos de extrapolación de dosis y tiempo de exposición). Otros son "no-paramétricos" en el sentido que se necesitó un cambio en el modelo en sí (*p. ej.*, cuando se extrapola hacia una mujer embarazada, las ecuaciones del feto deben ser consideradas).

 Véase también
 Farmacocinética
 Farmacodinámica
 Farmacia

 Referencias

 Bibliografía
 Balant L.P. Gex-Fabry M. (1990) *Physiological pharmacokinetic modelling* Xenobiotica 20: 1241-1257.

 Bouvier d’Yvoire M., Prieto P., Blaauboer B.J., Bois F., Boobis A., Brochot C., Coecke S., Freidig A., Gundert-Remy U., Hartung T., Jacobs M. N., Lavé T., Leahy D.E., Lennernäs H., Loizou G.D., Meek B., Pease C., Rowland M., Spendiff M., Yang J., Zeilmaker M. (2007) *Physiologically-based kinetic modelling (PBK modelling): meeting the 3Rs agenda - The report and recommendations of ECVAM Workshop 63a*, Alternatives to Laboratory Animals, 35:661–671.

 Menzel D.B. (1987) *Physiological pharmacokinetic modeling* Environmental Science and Technology 21:944-950.

 Droz P.O., Guillemin M.P. (1983) *Human styrene exposure - V. Development of a model for biological monitoring* International Archives of Occupational and Environmental Health 53:19-36.

 Gerlowski L.E., Jain R.K. (1983) *Physiologically based pharmacokinetic modeling: principles and applications* Journal of Pharmaceutical Sciences 72: 1103-1127.

 Ramsey J.C., Andersen M. (1984) *A physiologically based description of the inhalation pharmacokinetics of styrene in rats and humans* Toxicology and Applied Pharmacology 73: 159-175.

 Reddy M. *et al.* (2005) *Physiologically Based Pharmacokinetic Modeling: Science and Applications*, Wiley-Interscience.
