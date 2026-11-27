---
type: Artículo de enciclopedia
title: Monitor clínico
description: Un monitor de signos vitales, monitor clínico o monitor fisiológico es un dispositivo o una combinación de dispositivos que se utilizan para medir y controlar los parámetros vitales de un paciente.
resource: https://es.wikipedia.org/wiki/Monitor_clínico
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Monitor_clínico"}
license: CC BY-SA 4.0
id: eswiki-Monitor_clínico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Monitor clínico

Un **monitor de signos vitales, monitor clínico** o **monitor fisiológico** es un dispositivo o una combinación de dispositivos que se utilizan para medir y controlar los parámetros vitales de un paciente. Entre las diversas abreviaturas se utilizan "monitor de noche", "monitor de paciente", "monitor de datos vitales", "monitor médico" o simplemente "monitor".

Los monitores se utilizan principalmente como sistema de control del **paciente** durante la anestesia durante las operaciones, con pacientes críticos en cuidados intensivos, durante exámenes con sedación o con otros cuadros clínicos que requieren un seguimiento continuo (*monitorización*). Los dispositivos móviles están disponibles para utilizarlos con pacientes de emergencia.

 Descripción
Es un dispositivo utilizado para controlar las constantes vitales humanas. Mide y registra constantemente signos vitales como el electrocardiograma, la frecuencia cardíaca, la presión arterial y la temperatura corporal, y avisa con una alarma cuando el estado del paciente se vuelve anormal. Recientemente, muchos dispositivos están equipados con un pulsioxímetro.

El dispositivo puede consistir en uno o más sensores, procesamiento de datos de estos sensores y un dispositivo de visualización. También puede contener una interfaz de comunicación para grabar, procesar o mostrar datos biométricos fuera del propio monitor.

 Historia

Fue comercializado en 1964 por Hironan Kubota de Nihon Kohden Kogyo. En el pasado, el tipo estacionario se utilizaba principalmente para aplicaciones relacionadas con la medicina, pero en los últimos años se ha vuelto más pequeño y ligero, y se utiliza en una variedad de aplicaciones combinándolo con microcontroladores como el Arduino o con ordenadores portátiles.

Los primeros monitores electrónicos eran analógicos, para mostrar una pantalla de osciloscopio, donde sólo se mostraba una sola forma de onda de datos de un sensor, por ejemplo para medidas de EKG. Esto supuso el uso de equipos altamente especializados. Debía utilizarse un dispositivo independiente para cada tipo de medida, por ejemplo para la medida de la presión arterial y para la medida del EKG. La llegada de pantallas más modernas, osciloscopios o CRT, permitió mostrar múltiples formas de onda, por ejemplo, la presión arterial y la frecuencia cardíaca se pueden mostrar en una pantalla a la vez. Estos dispositivos analógicos salvaron muchas vidas, pero también tenían muchas limitaciones y malas características. En comparación con los dispositivos actuales, tenían poca sensibilidad, alta sensibilidad en las interferencias electromagnéticas, no permitían la lectura numérica de los datos medidos, etc.

Los instrumentos modernos actuales utilizan procesadores digitales de la señal (DSP) para el procesamiento digital de los datos medidos, lo que ha permitido la miniaturización y la portabilidad del equipo. El procesamiento digital también permite cálculos arbitrarios a partir de datos medidos, por ejemplo, el promedio, el mínimo, el máximo, el uso de varios filtros para suprimir la influencia de la interferencia electromagnética. Las pantallas digitales LCD se utilizan para mostrar los datos, permitiendo que se muestren múltiples parámetros medidos junto con otros datos calculados al mismo tiempo.

A medida que la investigación biomédica, la nanotecnología y la nutrigenómica avanzan, se adentran en las capacidades de autocuración del ser humano y en la creación de conciencia de las limitaciones de la intervención médica mediante fármacos químicos, enfocado sólo en el tratamiento médico de la vela escola, no hay investigaciones que muestren los enormes daños que pueden causar los medicamentos, los investigadores están trabajando para satisfacer la necesidad de un estudio más exhaustivo y un seguimiento clínico continuo personal de las condiciones de salud, manteniendo la intervención médica aquí realizada como últimos recursos.

 Partes básicas del dispositivo

 Sensores
El monitor utiliza varios sensores para detectar el estado del paciente. Por ejemplo, sensores para la medida de ECG, sensor de oxigenación de la sangre, sensor de temperatura. Estos son mayoritariamente convertidores de magnitudes no eléctricas a eléctricas, o en el caso del ECG, electrodos que detectan directamente potenciales de tensión. Todos los sensores deben incluir cables de alimentación y conectores para la conexión al monitor. El fabricante normalmente los suministra como accesorios en sus dispositivos.

 Circuitos de procesamiento de datos
Estos circuitos se utilizan para procesar la señal de los sensores. Su tarea es evaluar señales individuales y convertirlas en un formato adecuado para el almacenamiento y visualización en un monitor. Los amplificadores de instrumentos son la base, puesto que las señales biológicas suelen ser muy débiles. En los dispositivos modernos, la mayor parte del procesamiento de la señal se realiza digitalmente. Los circuitos de separación son una parte integral, que por un lado garantizan la seguridad del paciente y, por otro, protegen al dispositivo de la destrucción si llega un alto voltaje no deseado a la entrada.

 Visualizadores
Los datos fisiológicos se muestran continuamente en la pantalla del monitor. Los datos se muestran a lo largo de una línea de tiempo. Antes se utilizaban pantallas de tipo CRT, hoy en día las pantallas de tipo LCD se utilizan casi exclusivamente. Los flujos de los sensores se pueden complementar con información adicional calculada a partir de datos medidos, se pueden mostrar máximos, mínimos y valores medidos medios.

 Interfaz de comunicación
Algunos modelos de monitores de signos vitales tienen una interfaz de red. Gracias a ello, los datos medidos pueden enviarse continuamente a una estación central de control, por ejemplo a la UCI. Entonces, una persona es suficiente para operar y controlar varios dispositivos. Utilizando modelos portátiles, equipados con una interfaz inalámbrica y batería, podemos conseguir la telemetría. Este dispositivo lo lleva el paciente.

Con la monitorización digital, se está desarrollando cada vez más la capacidad de incluir datos fisiológicos de los sistemas de monitorización directamente en los registros electrónicos de salud de un hospital. Para ello, las normas sanitarias desarrolladas a tal fin por organizaciones tales como IEEE o HL7. Estos métodos recientemente utilizados reducen la posibilidad de errores humanos en la creación de la documentación y pueden a veces reducir el consumo de papel. Mediante la evaluación automática de ECG, también se puede incluir un diagnóstico en los registros. los programas del monitor aseguran la correcta codificación de los mensajes en función del estándar utilizado. Estos mensajes se envían a la aplicación principal, que los decodifica e incorpora a las entradas correctas del paciente.

 Alarma
El monitor de signos vitales suele incluir también una función de alarma, por ejemplo en forma de señales sonoras acústicas que alertan al personal de operación si se cumple una determinada condición, por ejemplo si un determinado parámetro supervisado supera un límite establecido.

 Dispositivos móviles
Se abre un espacio completamente nuevo con el uso de dispositivos móviles portátiles, en algunos casos incluso implantables debajo de la piel. Estos dispositivos forman el llamado BAN, cuyo centro es, por ejemplo, un teléfono inteligente equipado con una aplicación especial que recoge todos los datos medidos. La atención sanitaria a distancia se llama telemedicina.

 Parámetros controlados

El monitor está pensado para controlar las funciones vitales básicas. Las funciones medidas difieren según el tipo de monitor y su finalidad.

 Presión sanguínea

La presión arterial se mide con mayor frecuencia mediante un método no invasivo llamado método oscilométrico, que se basa en medir los cambios de presión en un brazal a presión. La presión arterial determina cuál es la fuerza que ejerce la sangre cuando pasa por las arterias.

 Frecuencia cardíaca

La frecuencia cardíaca se lee, por ejemplo, cuando se mide un EKG o cuando se mide la oxigenación de la sangre con pulsioximetría. El personal de operación podrá elegir a partir de qué curso se calculará la frecuencia cardíaca.

 Frecuencia respiratoria

Cuando se mide la frecuencia respiratoria, el monitor del paciente suele detectar la impedancia transtorácica, normalmente entre dos electrodos de ECG pegados al cuerpo o pecho del paciente. A medida que el pecho se mueve durante la respiración, se producen cambios en la impedancia transtorácica y el monitor del paciente puede mostrar una forma de onda respiratoria y un valor numérico de respiraciones por minuto.

 Temperatura corporal
La temperatura corporal puede medirse por contacto con un termómetro o sin contacto mediante métodos ópticos.

 ECG
Un electrocardiograma (ECG por abreviar) es un registro del cambio temporal del potencial eléctrico causado por la actividad cardíaca. Son los datos básicos que controla el monitor. Los dispositivos más sencillos sólo permiten la medida básica de ECG de tres derivaciones, pero muchos dispositivos modernos pueden medir las 12 derivaciones.

 Saturación de oxígeno

Normalmente se mide mediante un aparato óptico llamado pulsioxímetro, utilizando un sensor colocado en el dedo de la extremidad superior o en el lóbulo de la oreja. Se mide el porcentaje de hemoglobina a la que se une el oxígeno. Por tanto, se trata de la saturación de oxígeno periférica, a menudo llamada SpO2.

 Otros parámetros controlados

 Parámetros respiratorios
Esta monitorización puede que sea necesaria para otros parámetros como la presión venosa central, la presión intracraneal, la medición del caudal cardíaco, el análisis del contorno de polvo ( PiCCO ) los valores de presión arterial pulmonar en un catéter de arteria pulmonar o formas especiales de electroencefalografía (EEG).

 Medida de presión invasiva
La medida de la presión con el braguete sólo puede realizarse en determinados intervalos de tiempo. Si es necesario medir la presión arterial continuamente, cateterizar al paciente para medir la presión invasiva.

 Monitorización de la glucosa en sangre
 Los dispositivos de control de glucosa en sangre in vivo pueden transmitir datos a un ordenador que puede ayudar con las sugerencias de la vida diaria para el estilo de vida o la nutrición y con el médico puede realizar sugerencias para estudios posteriores en personas que están en riesgo y ayudar a prevenir la diabetes mellitus tipo 2.

 Monitorización del estrés
 Los biosensores pueden proporcionar avisos cuando los signos de los niveles de estrés aumentan antes de que el ser humano pueda notarlo y proporcionar alertas y sugerencias. Los modelos de redes neuronales profundas que utilizan datos de imágenes de fotopletismografía (PPGI) de cámaras móviles pueden evaluar los niveles de estrés con un alto grado de precisión (86%).

 Biosensor de serotonina
 Los futuros biosensores de serotonina pueden ayudar con trastornos del estado de ánimo y depresión.

 Nutrición basada en análisis de sangre continua
 En el ámbito de la nutrición basada en la evidencia, un implante de laboratorio con chip que puede realizar análisis de sangre las 24 horas del día, los 7 días de la semana, puede proporcionar resultados continuos y un ordenador puede proporcionar sugerencias o alertas nutricionales.

 Psiquiatra en un chip
 En ciencias clínicas del cerebro, la entrega de fármacos y los biosensores basados en Bio-MEMS in vivo pueden ayudar a prevenir y tratar precozmente los trastornos mentales.

 Monitorización de la epilepsia
 En la epilepsia, las próximas generaciones de monitorización de vídeo-EEG a largo plazo pueden predecir las convulsiones epilépticas y prevenirlas con cambios en la actividad de la vida diaria como el sueño, el estrés, la nutrición y la gestión del estado de ánimo.

 Seguimiento de la toxicidad
 Los biosensores inteligentes pueden detectar materiales tóxicos como el mercurio y el plomo y proporcionar alertas.

 Software del dispositivo

Los monitores de signos vitales modernos son en realidad pequeños ordenadores que realizan el procesamiento digital de datos grabados. Su parte integral es, por tanto, los programas adecuados, que deben garantizar:

 Conexión y funcionamiento de todas las entradas de funciones medidas
 Cálculo de los valores requeridos y parámetros de las señales medidas
 Visualización de los datos de salida en el monitor
 Comunicación con el personal de servicio
 Posibilidad de configurar parámetros de los canales de medida, por ejemplo sensibilidad, rango
 Opción por calibrar sensores de medida
 Posible escritura de datos en la impresora conectada
 Comunicación con un almacenamiento remoto de datos medidos

Básicamente, es un sistema incrustado. Los programas los suministra el fabricante.com aparte del dispositivo.

 Uso
Los monitores de signos vitales se utilizan principalmente en los quirófanos para controlar al paciente durante la cirugía y en la UCI o ARO para garantizar una supervisión constante del paciente.

Además, se pueden utilizar para mediciones a largo plazo de pacientes con fines de examen, los llamados Sistemas Holter. En este caso, suele ser registros de 24 horas, pero en ocasiones también de 48 o 72 horas, tanto en un entorno hospitalario como para personas que se mueven con libertad, donde se utilizan principalmente pequeños dispositivos portátiles.

Un caso importante es su uso para poder vigilar al paciente durante la anestesia.

 Referencias

 Bibliografía

 Pietka, E.; Badura, P.; Kawa, J. [et al.].. Information Technology in Biomedicine. Springer International Publishing, 2019 (Advances in Intelligent Systems and Computing). ISBN 978-3-030-23762-2.

 Enlaces externos

 Monitoring vidas
 Prístroje sledující vida, Hospital IN
 Personal Medical Monitoring Devices, iHealth
