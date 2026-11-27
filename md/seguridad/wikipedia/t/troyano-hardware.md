---
type: Artículo de enciclopedia
title: Troyano Hardware
description: Un Troyano Hardware (o en inglés Hardware Trojan Horse (HTH), o circuito malicioso) es una modificación malintencionada de los circuitos de un circuito integrado.
resource: https://es.wikipedia.org/wiki/Troyano_Hardware
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Troyano_Hardware"}
license: CC BY-SA 4.0
id: eswiki-Troyano_Hardware
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Troyano Hardware

Un **Troyano Hardware** (o en inglés *Hardware Trojan Horse *(HTH), o circuito malicioso) es una modificación malintencionada de los circuitos de un circuito integrado. Un troyano hardware está completamente caracterizado por su representación física y su comportamiento. La carga útil de un HTH es toda la actividad que el troyano ejecuta cuando se activa. En general, los troyanos maliciosos tratan de eludir o desactivar la seguridad de un sistema: puede filtrar información confidencial de la emisión de radio. El HTH también podría deshabilitar, trastornar o destruir todo el chip o los componentes del circuito.

 Trasfondo

Los negocios de la actualidad son a escala global y por esa razón, la externalización de tareas es un método común para aumentar ingresos de las compañías. Es por eso que los dispositivos de hardware integrados son producidos en el extranjero. Pero la subcontratación representa una amenaza grave, especialmente para las agencias gubernamentales. Por lo general, los sectores amenazados son los militares, las finanzas, la energía o el sector político.

La integridad del hardware, es decir, un chip que no tenga modificaciones en comparación con el diseño del chip original, no está garantizada. Todo el mundo que tenga acceso al proceso de fabricación de un chip puede hacer alteraciones maliciosas para el diseño. La fabricación de circuitos integrados que se fabrican en las industrias no confiables es algo común. Un adversario puede tratar de ocultar los componentes adicionales, por lo tanto, son necesarias avanzadas técnicas de detección para tal fin.

 Ataques en la historia

En el año 1991, Estados Unidos realizó varios ataques a Irak mediante el envío de impresoras infectadas con el "virus AF/91", lo que les permitió su difusión en las computadoras que poseían el sistema operativo Windows y el posterior apagón de las instalaciones de radares.

Mientras tanto, los profesionales en seguridad informática acceden a las empresas que les solicitan auditorías mediante impresoras conectadas a redes locales.

 Características

Un HTH puede ser caracterizado por su representación física, su fase de activación y su fase de acción.

 Características físicas

Una de estas características físicas de Troyano es el tipo. El tipo de un Troyano puede ser funcional o paramétrico. Un troyano es funcional si el adversario añade o elimina todos los transistores o puertas para el diseño del chip original. El otro tipo de troyano, el troyano paramétrico, modifica el circuito original, por ejemplo, adelgazamiento de hilos, el debilitamiento de los flip-flops o transistores, sometiendo el chip a la radiación, o usando Focused Ion-Beams (FIB) para reducir la fiabilidad de un chip.

El tamaño de un Troyano es su extensión física o el número de componentes del que está hecho. Debido a que un Troyano puede constar de muchos componentes, el diseñador puede distribuir las partes con una lógica maliciosa en el chip. La lógica adicional puede ocupar un lugar en el chip donde se necesite para modificar, agregar o eliminar una función. Si la función del Troyano lo exige, los componentes maliciosos pueden estar dispersos. Esto se conoce como "distribución suelta". Por otro lado un troyano puede consistir en sólo unos pocos componentes, por lo que el área es pequeña, donde la lógica maliciosa ocupa el diseño del chip, que se denomina "distribución ajustada".

Si el adversario no ahorra esfuerzos, a continuación, se regenera el diseño, de manera que la colocación de los componentes del circuito integrado (CI) se altera. En casos raros, la dimensión chip está alterado. Estos cambios son alteraciones estructurales.

 Características de activación

El troyano típico está basado en una condición: Se activa mediante sensores, estados lógicos internos, un patrón determinado insumo o un valor de cómputo interno. Basados en esas condiciones, los troyanos son detectables con trazos de energía hasta cierto punto cuando está inactivo. Esto es debido a las corrientes de fuga generadas por el gatillo o que activan el circuito de contador del HTH.

Los Troyanos Hardware pueden ser activados de diferentes maneras: Un troyano puede ser activado internamente, que significa que controla una o más señales dentro del CI. La circuitería malintencionada podría esperar realizando una cuenta regresiva lógica añadida al chip por un atacante, de manera que el troyano despierta después de un intervalo de tiempo específico, en este caso, el oponente es capaz de activarlo externamente. Puede haber una lógica maliciosa dentro de un chip, que se usa un sensor de antena o el adversario puede dar órdenes desde fuera del chip. Por ejemplo un troyano podría estar dentro del sistema de control de un misil de crucero, aunque el propietario del misil no lo sabe, el enemigo será capaz de apagar los cohetes por radio.

Un troyano que está siempre encendido puede ser reducido por un alambre. Un chip que se modifica de esta manera puede producir errores o no, cada vez que se utiliza el alambre intensamente. Siempre activa circuitos que son difíciles de detectar con trazos de energía.

En este contexto, los troyanos combinacionales y los troyanos secuenciales se distinguen. Un troyano monitoriza las señales internas combinacionales hasta que una condición específica ocurre. Un troyano secuencial es también una condición interna activa basada en circuito, pero sigue de cerca las señales internas y búsquedas de secuencias no para un estado o condición específica, como los troyanos combinacionales hacen.

 Accionar característico

Un HTH podría modificar la función del chip o cambios paramétricos en las propiedades del chip (por ejemplo, provoca un retraso del proceso). La información confidencial también puede transmitirse al adversario (como la transmisión de información de clave).

 Dispositivos periféricos con HTH

Un vector de amenaza relativamente nuevo para las redes y los puntos finales de red es un HTH apareciendo como un dispositivo físico periférico que está diseñado para interactuar con el extremo de la red usando el protocolo del dispositivo aprobado como un periférico de comunicación.

Por ejemplo, un teclado USB que oculta todos los ciclos de procesamiento maliciosos desde el punto final de red de destino a la que está fijado mediante la comunicación con el extremo de red de destino mediante canales deseados USB. Una vez que los datos confidenciales se exfiltraron desde el punto final de la red de destino a la HTH, el HTH puede procesar los datos y decidir qué hacer con ellos: los almacena en la memoria para su posterior recuperación física en la HTH o posiblemente los exfiltra a Internet de forma inalámbrica o mediante el extremo comprometido de red como un pivote.

 Potencial de amenaza

Un troyano común es pasivo para un intervalo de tiempo más un dispositivo de alteración que está en uso, pero la activación puede causar un daño fatal. Si el troyano se activa la funcionalidad se puede cambiar, el dispositivo puede ser destruido o averiado, puede filtrar información confidencial o destruir la seguridad y protección. Los troyanos son sigilosos, eso significa que la condición previa para la activación es un evento muy raro. Las técnicas tradicionales de pruebas no son suficientes. Un defecto de fabricación puede encontrarse en una posición aleatoria, mientras que los cambios maliciosos están en una buena posición para evitar la detección.

 Detección de los Troyanos Hardware

 Inspección física

En primer lugar, la capa moldeada es cortada para revelar los circuitos, entonces, el ingeniero repetidamente escanea la superficie mientras que muele las capas a viruta.

Hay varias operaciones para explorar los circuitos. Los métodos típicos de inspección visual son:

 Microscopía óptica (MO),
 Microscopía electrónica de barrido (SEM),
 Análisis de circuitos de imágenes por pico-segundos (PICA),
 Imágenes de contraste de tensión (VCI),
 Alteración ligera tensión inducida (LIVA) o,
 Carga inducida de alteración de voltaje (CIVA).

 Testeo funcional

Este método de detección estimula los puertos de entrada de un chip y monitoriza la salida para detectar defectos de fabricación. Si los valores lógicos de salida no coinciden con el patrón auténtico, podría detectarse un defecto o un Troyano Hardware.

 Autoprueba

El *Built-in self-test* o autoprueba (BIST) y Diseño-para-prueba (DFT) es una funcionalidad adicional en el chip utilizada para verificar la funcionalidad del chip.

BIST y DFT se implementan como circuitos adicionales (lógica en el chip) para monitorizar las señales de estímulo de entrada, y / o asistir en la detección de defectos. Por un lado, estas técnicas se utilizan para detectar los errores de fabricación, pero también podría utilizarse para detectar una lógica no deseada (malicioso) en el chip. Dependiendo del propósito de la BIST, que posiblemente podría ser utilizado para detectar la presencia de lógica no deseada (maliciosa), pero sería altamente dependiente de la funcionalidad BIST en sí mismo.

La funcionalidad BIST menudo existe para realizar en alta velocidad una verificación en donde no es posible el uso de cadenas de análisis u otras de baja velocidad de capacidades DFT. Es más probable que el DFT fuera apropiado para reconocer lógica no deseada.

Un verdadero chip genera una firma familiar, pero un chip defectuoso o alterado muestra una firma desconocida. La firma puede tener cualquier número de salidas de datos desde el chip: un análisis de la cadena entera o un resultado intermedio de datos. Los chips más modernos se funden o se desactivan a través de la configuración de hardware, la capacidad del chip dependerá para realizar el BIST o el DFT fuera de un entorno de fabricación, lo que es importante porque el DFT o el BIST pueden, por sí mismos, ser utilizados en un ataque en el chip.

 Análisis del canal lateral

Cada dispositivo que se encuentra eléctricamente activo emite señales diferentes como campos magnéticos y eléctricos. Estas señales, que son causadas por la actividad eléctrica, y se pueden analizar para obtener información sobre el estado y los datos de los procesos de los dispositivos.

Existen métodos avanzados para medir estos efectos secundarios que se han desarrollado y que son muy sensibles a ataques del canal lateral. Por lo tanto, es posible detectar troyanos fuertemente acopladas través de la medición de estas señales analógicas. Los valores medidos se puede utilizar como una firma para el dispositivo analizado. También es común que un conjunto de valores de medición se evalúen para evitar errores de medición u otras inexactitudes.

 Véase también
 Circuito integrado

 Bibliografía
 Mainak Banga y Michael S. Hsiao: *A Region Based Approach for the Identification of Hardware Trojans*, Bradley Department of Electrical and Computer Engineering, Virginia Tech., Host'08, 2008
 A. L. D’Souza y M. Hsiao: *Error diagnosis of sequential circuits using region-based model, Proceedings of the IEEE VLSI Design Conference*, January, 2001, pp. 103–108.
 C. Fagot, O. Gascuel, P. Girard y C. Landrault: *On Calculating Efficient LFSR Seeds for Built-In Self Test*, Proc. Of European Test Workshop, 1999, págs. 7–14
 G. Hetherington, T. Fryars, N. Tamarapalli, M. Kassab, A. Hassan y J. Rajski: *Logic BIST for large industrial designs, real issues and case studies*, ITC, 1999, págs. 358–367
 W. T. Cheng, M. Sharma, T. Rinderknecht y C. Hill: *Signature Based Diagnosis for Logic BIST*, ITC 2006, Oct. 2006, págs. 1–9
 Rajat Subhra Chakraborty, Somnath Paul y Swarup Bhunia: *On-Demand Transparency for Improving Hardware Trojan Detectability*, Department of Electrical Engineering and Computer Science, Case Western Reserve University, Cleveland, OH, USA
 Yier Jin y Yiorgos Makris: *Hardware Trojan Detection Using Path Delay Fingerprint*, Department of Electrical Engineering Yale University, New Haven
 Reza Rad, Mohammad Tehranipoor y Jim Plusquellic: *Sensitivity Analysis to Hardware Trojans using Power Supply Transient Signals*, 1st IEEE International Workshop on Hardware-Oriented Security and Trust (HOST'08), 2008
 Dakshi Agrawal, Selcuk Baktir, Deniz Karakoyunlu, Pankaj Rohatgi y Berk Sunar: *Trojan Detection using IC Fingerprinting*, IBM T.J. Watson Research Center, Yorktown Heights, Electrical \& Computer Engineering Worcester Polytechnic Institute, Worcester, Massachusetts, Nov 10, 2006
 Xiaoxiao Wang, Mohammad Tehranipoor y Jim Plusquellic: *Detecting Malicious Inclusions in Secure Hardware, Challenges and Solutions*, 1st IEEE International Workshop on Hardware-Oriented Security and Trust (HOST'08), 2008
 Miron Abramovici y Paul Bradley: *Integrated Circuit Security - New Threats and Solutions*
 Zheng Gong y Marc X. Makkes: *Hardware trojan side-channels based on physical unclonable functions* - WISTP 2011

 Referencias
