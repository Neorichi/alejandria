---
type: Artículo de enciclopedia
title: Software de prevención de pérdida de datos
description: "Una solución de prevención de pérdida de datos (PPD) es un sistema que está diseñado para detectar potenciales brechas de datos/ transmisiones de datos y prevenirlos a través de monitoreo, detección y bloqueo de …"
resource: https://es.wikipedia.org/wiki/Software_de_prevención_de_pérdida_de_datos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Software_de_prevención_de_pérdida_de_datos"}
license: CC BY-SA 4.0
id: eswiki-Software_de_prevención_de_pérdida_de_datos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Software de prevención de pérdida de datos

Una solución de prevención de pérdida de datos (PPD) es un sistema que está diseñado para detectar potenciales brechas de datos/ transmisiones de datos y prevenirlos a través de monitoreo, detección y bloqueo de información sensible mientras está **en uso** (acciones de extremos), **en movimiento** (tráfico de red) y **en reposo** (almacenamiento de datos). En incidentes de filtración de datos, información sensible es divulgada a personal no autorizado, ya sea con intenciones maliciosas o por un error inadvertido. Dichos datos sensibles pueden ser información de compañías, propiedad intelectual (PI), información financiera, datos de tarjetas de crédito y otra información dependiendo del negocio y la industria.

Los términos "pérdida de datos" y "filtración de datos" están cercanamente relacionados y son comúnmente usados indistintamente, a pesar de que son diferentes en cierto sentido. Los incidentes de pérdida de datos se convierten en incidentes de filtración de datos en los casos donde el medio que contenga información sensible sea perdido y subsecuentemente adquirido por un grupo no autorizado. Sin embargo, una filtración de datos es posible sin que haya pérdida de datos. Otros términos asociados con la **prevención de filtración de datos** son **detección y prevención de filtración de datos**, **prevención de filtración de información**, **monitoreo y filtrado de contenido**, **protección y control de información**, y **sistema de prevención de extrusión**, que se opone a un sistema de prevención de intrusos.

Categorías de software de PPD
Los medios tecnológicos empleados para lidiar con incidentes de filtración de datos pueden ser divididos en las siguientes categorías: medidas estándar de seguridad, medidas de seguridad avanzadas o inteligentes, control de acceso y encripción y sistemas PPD designados.

Medidas estándar de seguridad
Medidas estándar de seguridad, como firewalls, sistemas de detección de intrusos y software de antivirus, son mecanismos que están comúnmente disponibles y que resguardan computadoras en contra de ataques externos al igual que de ataques internos. El uso de firewall, por ejemplo, limita el acceso de externos a la red interna y un sistema de detección de intrusos detecta intrusiones realizadas por externos. Los ataques internos pueden ser evitados a través de escaneos realizados por antivirus que detectan Troyanos instalados en PC's que envían información confidencial y a través del uso de lo clientes ligeros que operan en una arquitectura cliente-servidor sin personal o información sensible almacenada en la computadora del cliente.

Medidas de seguridad avanzadas
Las medidas de seguridad avanzadas emplean el aprendizaje de máquinas y algoritmos de razonamiento temporal para detectar accesos anormales a datos (bases de datos o sistemas de recuperación de información) o intercambio anormal de correos electrónicos, honeypots para detectar al personal autorizado sin intenciones maliciosas y actividad basada en verificación (dinámica de reconocimiento de pulsaciones de teclado) y monitoreo de actividad de usuario para detectar acceso anormal a datos.

Soluciones designadas PPD
Las soluciones designadas PPD detectan y previenen intentos no autorizados de copiado o envío de información sensible, intencional o no intencionalmente, sin autorización, principalmente por personal autorizado a acceder dicha información. Para clasificar cierta información como sensible, estas soluciones usan mecanismos, tales como igualación de datos, información estructurada de huellas dactilares, métodos estadísticos, igualación de expresiones regulares y reglas, lexicografía publicada, definiciones conceptuales y palabras clave.

Tipos de sistemas PPD

Red PPD (información en movimiento)
Típicamente, es una solución de software o hardware que es instalada en el puerto de egreso de una red cerca del perímetro. Analiza el tráfico de red para detectar información sensible que está siendo enviada violando las políticas de seguridad de información.

PPD de extremos (información en uso)
Dichos sistemas corren en estaciones de trabajo de usuarios o servidores en la organización. Como los sistemas basados en red, los sistemas basados en extremos pueden direccionar comunicaciones internas y externas y, en consecuencia, pueden ser utilizados para controlar el flujo de información entre grupos o usuarios(pared china). También pueden controlar comunicaciones vía correo electrónico o mensajería instantánea antes de que sean almacenados en el registro corporativo, de esta manera, una comunicación bloqueada(una que nunca se haya enviado y por lo tanto no se le aplican reglas de retención) no será identificada en una situación de descubrimiento legal subsecuente. Los sistemas de extremo tienen la ventaja de poder monitorear y controlar el acceso físico a dispositivos(dispositivos móviles con capacidad de almacenamiento de datos) y en algunas casos pueden acceder a información antes de ser encriptada. Algunos sistemas basados en extremos, proveen aplicaciones de control para bloquear intentos de transmisión de información confidencial y proveen retroalimentación inmediata al usuario. Tienen la desventaja de necesitar ser instalados en cada estación de trabajo en la red, no pueden ser utilizados en dispositivos móviles(celulares y PDAs) o en lugares donde prácticamente no pueden ser instalados, por ejemplo, una estación de un café internet.

Identificación de datos
Soluciones PPD incluyen varias técnicas para identificar información confidencial o sensible. Algunas veces confundida con descubrimiento, la identificación de datos es un proceso por el cual las organizaciones utilizan tecnología PPD para determinar qué buscar y en que datos buscar (en movimiento, en reposo o en uso).

Los datos son clasificados como  **estructurados** o **no estructurados**. Datos estructurados residen en campos fijos dentro de un archivo como una hoja de cálculo, mientras que los datos no estructurados se refieren a texto en formato libre como documentos en archivos PDF. Se estima que el 80% de datos no son estructurados y el 20% son estructurados.
La clasificación de datos se divide en **análisis de contenido**, concentrado en datos estructurados, y **análisis contextual** que busca en el lugar de origen, la aplicación o el sistema que generó los datos.

Métodos para describir datos sensibles en abundancia. Pueden dividirse en dos categorías **métodos precisos** y **métodos imprecisos**.

**Métodos precisos** son, por definición, aquellos que involucran registro de contenido y que no activan casi ningún incidente falso positivo.
Todos los demás métodos son **imprecisos**y pueden incluir: palabras clave, lexicografías, expresiones regulares, expresiones regulares extendidas, tags de metadatos, análisis bayesiano, análisis estadístico tal como aprendizaje máquina, etc.

La fortaleza del motor de análisis está directamente correlacionado a su eficacia. **La eficacia de la identificación PPD es importante para disminuir o evitar falsos positivos y negativos**. La eficacia puede depender de numerosas variables, algunas pueden depender de la situación o de la tecnología.**Las pruebas en busca de eficacia se recomiendan para garantizar que una solución tiene virtualmente cero falsos positivos o negativos.**Tasas altas de falsos positivos causarían que el sistema fuera DPD no PPD.

Detección de filtración de datos
Algunas veces, un distribuidor de datos provee información sensible a un conjunto de grupos terceros. Un tiempo después, una parte de los datos es encontrada en un lugar no autorizado(en internet o en la computadora de un usuario). Entonces, el distribuidor tiene la obligación de investigar si la filtración de datos vino de uno o más grupos terceros o si fue juntada independientemente para otros propósitos.

Datos en reposo
"Datos en reposo" se refiere a información vieja almacenada ya sea, en la computadora de un cliente, en una red de almacenamiento o un servidor de datos o incluso en un sistema de respaldo, como un CD o un casete. Esta información es de gran preocupación para las empresas e instituciones gubernamentales simplemente porque mientras más tiempo estén esos datos almacenados y sin utilizarse, pueden ser obtenidos por individuos no autorizados a tenerlos.Por ejemplo, el módulo de descubrimiento de data in rest puede navegar en los recursos compartidos de la organización, para identificar la existencia de archivos con información de clientes o transacciones financieras y ubicarlos en su correspondiente sitio de alojamiento

 Véase también
Eliminadores de metadatos

 Referencias

 Enlaces externos
 Cost of a Data Breach
 Cornell Spider, Open Source Data-at-Rest Data Loss Prevention Software by Cornell University
 Security Checklist White Paper by Druva
