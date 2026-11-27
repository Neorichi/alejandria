---
type: Artículo de enciclopedia
title: Característica corriente-tensión
description: "Una característica corriente-tensión o curva I-V (del inglés current-voltage) es una relación, generalmente representada como un diagrama o gráfico, entre la corriente eléctrica que atraviesa un circuito, dispositivo o …"
resource: https://es.wikipedia.org/wiki/Característica_corriente-tensión
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Característica_corriente-tensión"}
license: CC BY-SA 4.0
id: eswiki-Característica_corriente-tensión
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Característica corriente-tensión

Una **característica corriente-tensión** o **curva I-V** (del inglés *current-voltage*) es una relación, generalmente representada como un diagrama o gráfico, entre la corriente eléctrica que atraviesa un circuito, dispositivo o material, y la tensión correspondiente, o diferencia de potencial, aplicada entre sus terminales. Este tipo de representación es fundamental para caracterizar el comportamiento eléctrico de componentes y materiales, y constituye una herramienta esencial en electrónica, electrofisiología, fotovoltaica y ciencia de materiales.

 Fundamento físico
La relación entre corriente y tensión está gobernada por las propiedades eléctricas del material o dispositivo. En términos generales, la corriente que fluye a través de un elemento es función de la tensión aplicada: . La forma de esta función determina si el dispositivo es lineal o no lineal, pasivo o activo, y si presenta efectos como resistencia negativa o histéresis.

La potencia instantánea disipada o generada por el dispositivo viene dada por . En el plano I-V, esta potencia es proporcional al área del rectángulo formado por las coordenadas de un punto de operación.

 En electrónica

En electrónica, la relación entre la corriente continua (CC) que circula por un dispositivo electrónico y la tensión continua (CC) entre sus terminales se denomina curva característica corriente-tensión. Los ingenieros electrónicos utilizan estas gráficas para determinar los parámetros básicos de un dispositivo (como la resistencia dinámica, la tensión umbral o la corriente de saturación) y modelar su comportamiento en un circuito eléctrico.

En componentes electrónicos con más de dos terminales, como tubos de vacío y transistores, la relación corriente-tensión en un par de terminales puede depender de la corriente o tensión en un tercer terminal. Esto se suele representar en un gráfico de corriente-tensión más complejo con múltiples curvas (familia de curvas), cada una de las cuales corresponde a un valor diferente de la variable de control.

Por ejemplo, el diagrama de la derecha muestra una familia de curvas I-V para un MOSFET en función del voltaje de drenaje-fuente , con la tensión de sobreexcitación  como parámetro. Se distinguen claramente dos regiones de operación: la región lineal (óhmica) y la región de saturación (activa).

 Medición de curvas I-V
La curva I-V de un componente eléctrico se puede medir con un instrumento llamado trazador de curvas o mediante una fuente de alimentación programable y un multímetro. Existen equipos especializados, como los analizadores de parámetros de semiconductores (por ejemplo, el Keysight B1500A o el Keithley 4200), que permiten trazar automáticamente familias de curvas y extraer parámetros de modelo.

 Tipos de curvas I-V
La forma de la curva característica de un componente eléctrico revela mucho sobre sus propiedades de funcionamiento. Las curvas I-V de diferentes dispositivos se pueden agrupar en categorías:

 Componentes activos frente a pasivos
 **Componentes pasivos (cargas)**: Sus curvas I-V se limitan al primer y tercer cuadrante del plano I-V, pasando por el origen. Consumen energía eléctrica del circuito, convirtiéndola en calor, luz o trabajo mecánico. Ejemplos: resistencias, bombillas, motores eléctricos. En estos dispositivos, la corriente convencional fluye en la dirección del campo eléctrico (del terminal positivo al negativo), por lo que las cargas pierden energía potencial.

 **Componentes activos (fuentes)**: Sus curvas I-V pasan por el segundo o cuarto cuadrante. Pueden generar electricidad, convirtiendo otra forma de energía en energía eléctrica. En estos cuadrantes, la corriente fluye del terminal negativo al positivo (en contra del campo eléctrico), y las cargas ganan energía potencial. Ejemplos: baterías, generadores, células solares.

 Lineal vs. no lineal
 **Lineal**: Una línea recta que pasa por el origen representa un elemento de circuito lineal. La relación I-V es de proporcionalidad directa, y la resistencia es constante. Obedece la ley de Ohm. Ejemplos: resistencias lineales, condensadores ideales (en corriente continua), inductores ideales (en corriente continua).
 **No lineal**: Una línea curva representa un elemento no lineal. La resistencia (o su recíproca, la conductancia) varía con la tensión o la corriente aplicada. Ejemplos: diodos, transistores, varistores.

 Resistencia negativa vs. resistencia positiva
 **Resistencia positiva**: La curva I-V tiene pendiente positiva (creciente) en toda su extensión. Es el comportamiento más común.
 **Resistencia negativa**: La curva I-V es no monótona y presenta regiones con pendiente negativa (decreciente). En esas regiones, un aumento de tensión provoca una disminución de la corriente. Los dispositivos con resistencia negativa (como el diodo túnel y el diodo Gunn) se utilizan para fabricar amplificadores y osciladores de alta frecuencia.

 Histéresis vs. univaluación
 **Univaluada (monótona)**: La corriente es una función unívoca de la tensión. Para cada valor de tensión hay un único valor de corriente.
 **Con histéresis**: La relación corriente-tensión depende no solo de la tensión instantánea, sino también del historial de tensiones previas. La curva I-V forma bucles cerrados, y cada rama se recorre en una dirección específica (marcada con flechas). Ejemplos: inductores y transformadores con núcleo ferromagnético, tiristores (SCR, DIAC, TRIAC), memristores y tubos de descarga de gas (como las lámparas de neón).

 En electrofisiología

Las curvas I-V también se utilizan ampliamente en el campo de la electricidad biológica, particularmente en la subdisciplina de la electrofisiología. En este contexto, el voltaje se refiere al potencial de membrana (diferencia de potencial a través de la membrana celular), y la corriente es el flujo de iones cargados a través de canales iónicos en dicha membrana.

Por convención, en electrofisiología se define la corriente como positiva cuando fluye desde el interior de la célula hacia el exterior (**corriente de salida**), lo que corresponde a la salida de iones positivos (p. ej., K+) o la entrada de iones negativos (p. ej., Cl-). La corriente negativa (**corriente de entrada**) corresponde a la entrada de iones positivos (p. ej., Na+, Ca^{+2}) o la salida de iones negativos.

La figura de la derecha muestra una curva I-V representativa de una neurona típica:
 La línea azul (lineal) representa la contribución de los canales de potasio (K+), que son poco dependientes del voltaje (rectificadores pasivos).
 La línea amarilla (no lineal) representa la contribución de los canales de sodio (Na+), que son fuertemente dependientes del voltaje y muestran una región de resistencia negativa (responsable del potencial de acción).
 La línea verde (suma de ambas) es la curva I-V total de la célula, que determina cómo responde la membrana a estímulos eléctricos.

El estudio de estas curvas permite comprender la excitabilidad neuronal, la propagación del potencial de acción y el efecto de fármacos sobre los canales iónicos.

 En sistemas fotovoltaicos
En energía solar fotovoltaica, la curva I-V de una célula, módulo o panel solar es fundamental para determinar su rendimiento. Una célula solar típica tiene una curva I-V que se desplaza hacia el cuarto cuadrante (generación de potencia) cuando se ilumina. Los parámetros clave extraídos de la curva I-V son:

 **Corriente de cortocircuito (ISC)**: corriente cuando la tensión es cero.
 **Tensión de circuito abierto (VOC)**: tensión cuando la corriente es cero.
 **Punto de máxima potencia (MPP)**: punto de la curva donde el producto V·I es máximo.
 **Factor de forma (FF)**: relación entre la potencia máxima y el producto VOC · ISC. Un factor de forma cercano a 1 indica una célula de alta calidad.

El seguimiento del punto de máxima potencia (MPPT) es una técnica utilizada en inversores solares para mantener el panel operando en su MPP bajo condiciones variables de irradiancia y temperatura.

 Véase también
 Seguimiento del punto de máxima potencia (MPPT)
 Voltametría
 Ley de Ohm
 Diodo
 Transistor
 Trazador de curvas
 Resistencia negativa
 Histéresis
 Memristor

 Referencias

 Enlaces externos
 Simulación interactiva de la ley de Ohm y curvas I-V – PhET (University of Colorado)
 Tutorial sobre curvas I-V de dispositivos semiconductores – All About Circuits (en inglés)
 Curva I-V en células solares – PV Education (en inglés)
