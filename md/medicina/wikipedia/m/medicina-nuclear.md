---
type: Artículo de enciclopedia
title: Medicina nuclear
description: "La medicina nuclear es una especialidad de la medicina en la que se utilizan radiotrazadores o radiofármacos (formados por un fármaco transportador y un isótopo radiactivo) para el diagnóstico y tratamiento de …"
resource: https://es.wikipedia.org/wiki/Medicina_nuclear
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Medicina_nuclear"}
license: CC BY-SA 4.0
id: eswiki-Medicina_nuclear
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Medicina nuclear

La **medicina nuclear** es una especialidad de la medicina en la que se utilizan radiotrazadores o radiofármacos (formados por un fármaco transportador y un isótopo radiactivo) para el diagnóstico y tratamiento de enfermedades. Estos radiofármacos se aplican dentro del organismo humano por diversas vías (la más utilizada es la vía intravenosa). Una vez que el radiofármaco está dentro del organismo, se distribuye por diversos órganos dependiendo del tipo empleado. La distribución de este es detectado por un aparato detector de radiación llamado gammacámara y almacenado digitalmente. Luego se procesa la información obteniendo imágenes de todo el cuerpo o del órgano en estudio. Estas imágenes, a diferencia de la mayoría de las obtenidas en radiología, son imágenes funcionales y moleculares, es decir, muestran cómo están funcionando los órganos y tejidos explorados o revelan alteraciones de los mismos a un nivel molecular.

Por lo general, las exploraciones de medicina nuclear no son invasivas y carecen de efectos adversos.

Se utiliza para diagnosticar y determinar la gravedad y tratamiento de una o varias enfermedades, incluyendo cáncer en diversos tipos, enfermedades cardíacas, gastrointestinales, endocrinas, desórdenes neurológicos, y otras anomalías dentro del cuerpo. Debido a que los procedimientos de medicina nuclear pueden detectar actividades moleculares dentro del cuerpo, ofrecen la posibilidad de identificar enfermedades en sus etapas tempranas, así también como las respuestas inmediatas de los pacientes a las intervenciones terapéuticas.

Los procedimientos de medicina nuclear pueden llevar mucho tiempo. Las radiosondas pueden tardar desde horas hasta días en acumularse en el área del cuerpo a estudiar y el diagnóstico por imágenes puede llevar varias horas, aunque en algunos casos se encuentran disponibles nuevos equipos que pueden reducir considerablemente el tiempo del procedimiento.

“La medicina nuclear ha sido, durante mucho tiempo, desconocida tanto para pacientes como para enfermeras; sin embargo, se está incorporando de manera creciente a los hospitales. Los pacientes que acuden a esos servicios requieren cuidados de enfermería, derivados tanto de la diversidad de exploraciones con características particulares, como de patologías susceptibles de ser estudiadas y/o tratadas con estos procedimientos. Tradicionalmente las actuaciones del profesional de enfermería han estado ligadas a problemas de colaboración y al propio desarrollo de la exploración, quedando los cuidados relacionados con los problemas de enfermería en un segundo plano o en manos de enfermeras de otros niveles asistenciales. No obstante, los cuidados de enfermería en medicina nuclear experimentan desde los años 1990 un notable avance, acompañado de una paulatina adaptación de la propia enfermería para dotarlos de calidad y un carácter propio. Una vez que las enfermeras empiezan a centrar su praxis en los cuidados de enfermería, se hace preciso sistematizar su método de trabajo para ofrecer una asistencia de calidad”.

La medicina nuclear es una rama de las imágenes médicas que utiliza cantidades muy pequeñas de material radiactivo para diagnosticar variedad y gravedad incluyendo muchos tipos de cáncer gastrointestinales, trastornos y otras anomalías dentro del cuerpo.

 Filtros de imagen en medicina nuclear

 Filtrado de imágenes

El filtrado las imágenes médicas, en este caso las imágenes de medicina nuclear, pueden asemejar a los filtros paso de banda, debido al estudio de las imágenes en el espacio de las frecuencias (espacio de Fourier).

Los parámetros a fijar son: tamaño de píxel y número de bytes por píxel. Estos parámetros determinan la máxima resolución espacial y la máxima discriminación en intensidad que se puede obtener. La elección de los valores de estos parámetros viene determinada por el problema que se estudia.

Del mismo modo que la representación de una señal temporal unidimensional se puede realizar en los dominios temporal y frecuencial, la representación de una imagen también puede realizarse en los dominios espacial y frecuencial.

La transformada de Fourier permite pasar de una representación a la otra. Hay que destacar que la representación de una imagen bidimensional en el dominio frecuencial es también una señal bidimensional que puede ser tratada como una imagen con valores en el campo complejo.

Los cambios bruscos de intensidad y los detalles finos van asociados a componentes de alta frecuencia, de modo que si se eliminan estos componentes, la imagen resultante que se obtiene a partir de la transformada de Fourier inversa carece de estos detalles finos.

 Filtros paso-baja

Este filtro efectúa un filtrado paso-baja cuyo grado de filtrado se controla por el radio del círculo. Un filtro muy abrupto puede producir oscilaciones en la imagen (fenómeno de Gibbs) por lo que suelen emplearse filtros paso-baja como el indicado a la derecha, que tienen una variación más suave. Son filtros con valores altos en el origen y que se atenúan hacia altas frecuencias.

Un filtro paso-baja puede implementarse también en el dominio espacial mediante convolución con una máscara de filtrado. La implementación de este filtro en el dominio espacial presenta ventajas en tiempo de cálculo frente a una implementación en el dominio frecuencial. Como regla general, si la respuesta impulsional del filtro es de tamaño menor que 12x12 píxels, el filtrado es mejor realizarlo en el dominio especial.

El radio del círculo, que determina el grado de filtrado, se expresa como fracción de la frecuencia de Nysquist.

 Filtro paso-alta

La implementación de un filtro paso-alta puede realizarse en el espacio de Fourier, con un planteamiento complementario al del filtro paso-baja.

El efecto de este filtro, que actúa por multiplicación en el espacio de Fourier será, pues, de potenciación de la alta frecuencia y eliminación de la baja frecuencia. Son filtros de realce o de extracción de contornos.

Un filtro paso-alta puede implementarse también por convolución en el dominio espacial.

Un ejemplo de filtro paso de alta es el filtro laplaciano, el cual es omnidireccional y extrae contornos en todas direcciones.

Con este tipo de filtros, la detección del contorno es perfecta en las imágenes sintéticas sin ruido, pero en la imagen con ruido del estudio real, el filtro no sólo no detecta el contorno sino que potencia el ruido. Este refuerzo del ruido es una característica de los filtros paso-alta.

El grado de filtrado se controla con el radio del círculo interior, que controla la frecuencia de corte.

 Ejemplos de exploraciones

 Gammagrafía renal: se utiliza para examinar la morfología y función de los riñones con el fin de detectar cualquier anomalía, como infecciones u obstrucción del flujo urinario.
 Gammagrafía de tiroides: se utiliza para evaluar la morfología y función tiroideas, especialmente en el hipertiroidismo.
 Gammagrafía ósea: se utiliza para evaluar enfermedades de los huesos y articulaciones, ya sean de origen tumoral, inflamatorio, degenerativo, traumatológico, metabólico o vascular.
 Gammagrafía con galio-67 (Ga67): se utiliza para diagnosticar enfermedades inflamatorias o infecciosas activas, tumores y abscesos.
 Centellograma Tiroideo con tecnecio-99m (Tc99m): se utiliza para localizar nódulos en la tiroides e identificar el mejor tratamiento (esto lo determina el médico).
 Centellograma Tiroideo con iodo-131 (I131) o Captación tiroidea: se utiliza para descubrir mal funcionamiento de la tiroides, generalmente hipertiroidismo, el cual es tratado con dosis de iodo-131 (menores a 30 mCI).
 Dosis Ablativa de iodo-131: se utiliza para destruir las células cancerosas remanentes después de la extirpación de la tiroides.
 Rastreo Corporal con iodo-131: se utiliza para saber si la dosis ablativa aplicada ha sido efectiva en un 100 %, de lo contrario debe darse una nueva dosis.

La medicina nuclear es un tipo de estudio que se hace para poder ver los órganos o algún fallo.

 Véase también
 Electromedicina
 Tecnología sanitaria
 Seguridad nuclear
 Gammagrafía
 Tomografía computarizada de emisión monofotónica
 Tomografía por emisión de positrones

 Referencias

Enlaces externos

 Sociedad Española de Medicina Nuclear
 Medicina Nuclear en El Salvador, Centroamérica.
 Salud - Organismo Internacional de Energía Atómica.
