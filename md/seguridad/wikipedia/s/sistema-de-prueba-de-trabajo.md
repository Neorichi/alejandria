---
type: Artículo de enciclopedia
title: Sistema de prueba de trabajo
description: "Un algoritmo de prueba de trabajo, sistema de prueba de trabajo o simplemente sistema PoW (del inglés Proof-Of-Work system) es un sistema que tiene como objetivo desincentivar y dificultar comportamientos indeseados …"
resource: https://es.wikipedia.org/wiki/Sistema_de_prueba_de_trabajo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sistema_de_prueba_de_trabajo"}
license: CC BY-SA 4.0
id: eswiki-Sistema_de_prueba_de_trabajo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sistema de prueba de trabajo

Un **algoritmo de prueba de trabajo**, **sistema de prueba de trabajo** o simplemente **sistema PoW** (del inglés *Proof-Of-Work system*) es un sistema que tiene como objetivo desincentivar y dificultar comportamientos indeseados como ataques DDoS o spam. Requiere que el cliente del servicio realice algún tipo de trabajo que tenga cierto coste y que es verificado fácilmente en la parte del servidor. Normalmente el trabajo consiste en realizar un cómputo en el ordenador del cliente.

La característica clave de la estrategia es su asimetría: El trabajo debe ser moderadamente difícil (pero factible) por el lado del cliente, pero fácil de verificar por el lado del servidor.

Luego del lanzamiento de Bitcoin en 2009 y del surgimiento de las criptomonedas el término se hizo mucho más conocido por su uso para dotar de seguridad a sistemas monetarios peer-to-peer.

 Tipos

Existen dos clases de protocolos para los sistemas PoW:

 Los protocolos de **desafío-respuesta** asumen un enlace interactivo directo entre el cliente y el servidor. El servidor elige un desafío, por ejemplo un elemento de un conjunto con una propiedad específica; luego el cliente encuentra una respuesta apropiada en el conjunto, la cual es enviada de vuelta al servidor, que procede a verificarla. Como el desafío es elegido en el momento por el servidor, su dificultad puede ser adaptada según la carga actual del servicio. El trabajo por parte del cliente está acotado y su varianza es baja.

 Los protocolos de **solución-verificación** no asumen un enlace como en el caso anterior: debido a esto el desafío debe ser auto-impuesto antes de que el cliente pueda buscar una solución, y el servidor debe verificar tanto el desafío elegido como la solución encontrada. La mayoría de los casos corresponden a procedimientos iterativos probabilísticos no acotados con alta varianza, como Hashcash.

Más aún, las funciones utilizadas por los distintos protocolos pueden ser de 2 tipos:

 **CPU-bound**, donde el cómputo se ejecuta a la velocidad del procesador, que cambia visiblemente en el tiempo siguiendo la ley de Moore, y también de servidores dedicados a dispositivos portátiles.

 **Memory-bound** donde la velocidad de cómputo depende de la velocidad de acceso a la memoria principal (que a su vez puede estar limitada por latencia o ancho de banda insuficiente), la cual se espera que sea menos sensitiva a las evoluciones de hardware.

Finalmente, algunos sistemas POW ofrecen **cómputos de atajo** que permiten a participantes que conocen algún secreto, típicamente una llave privada, acceder al servicio generando trabajo mínimo. La idea es que, por ejemplo, un dueño de una lista de correos pueda enviar mensajes a todos los inscritos sin incurrir en un alto costo. Si esta característica es o no deseable depende del escenario en que se use el sistema POW.

Implementaciones
A lo largo de la historia algoritmos de prueba de trabajo han sido propuestos y/o implementados en una variedad de sistemas entre los cuales podemos mencionar:

 Hashcash

Hashcash es un método que agrega un string al encabezado de un correo electrónico que prueba que el emisor dedicó un poco de tiempo para calcular dicho string. La idea es que como el emisor le dedicó tiempo a calcular el string y enviar el correo, es improbable que este sea spam. Por otro lado el receptor puede, con un costo computacional casi nulo, verificar que el string es válido.

 Reusable Proof of Work

Precursores de Bitcoin y basados en Hashcash, un sistema RPOW difiere de un sistema POW normal en que después de que un servidor recibe una prueba de trabajo ("moneda POW") de un cliente, este puede cambiar esta moneda ya gastada por otra que no lo esté, que puede ser utilizada para acceder a otro servidor que también requiera la entrega de una prueba de trabajo. De esta manera el servidor se ahorra el costo de hacer el trabajo requerido, usando en cambio el trabajo que este ha recibido por sus servicios. El otro servidor a su vez también puede cambiar la prueba de trabajo recibida por otra que pueda usar.

 Criptomonedas
Bitcoin y Un gran número de criptomonedas, utiliza sistemas de prueba de trabajo como mecanismo para controlar, limitar y validar la creación de unidades monetarias, así como para verificar la validez de las transacciones y evitar el doble gasto de fondos. En este caso, el sistema de prueba de trabajo permite la transferencia de valor descentralizada entre los participantes de la red sin depender de ninguna institución centralizada. Entre las criptomonedas alternativas que implementan algoritmos de prueba de trabajo  puros o híbridos se pueden mencionar a Ethereum, Bitcoin Cash, Nano y Litecoin.

Elección del algoritmo de prueba de trabajo
Con la experiencia de uso de los algoritmo de prueba de trabajo, especialmente en Bitcoin, se ha argumentado que el algoritmo elegido sería mejor si cumpliera ciertas restricciones:
**Resistencia frente a tecnologías ASIC**. En Bitcoin la especialización del proceso de minado, para hacerlo rentable, está provocando que el poder para crear bloques se esté centralizando en aquellos que emplean economías de escala para competir e invierte en tecnologías ASIC.  Esto provoca la centralización del poder de producción de bloques en entidades externas. Por este inconveniente si se quiere usar algoritmos de prueba de trabajo es bueno que sean resistentes a la tecnología ASIC.
**Prueba de trabajo útil** del inglés *Proof-Of-Useful-Work*. En Bitcoin la cantidad de trabajo computacional que hoy día se gasta en el proceso de minería es extraordinario. Se estima que se han gastado varios cientos de megavatios. Por eso se plantea usar algoritmos de consenso por prueba de trabajo de tal forma que el trabajo que se realice se pueda aprovechar para obtener algún beneficio. Por ejemplo el algoritmo de consenso de Primecoin (buscan primos con ciertas características) y de Permacoin (basado en almacenamiento distribuido de información dando lugar a la llamada **prueba de almacenamiento** del inglés *proof-of-storage* o **prueba de recuperación** del inglés *proof-of-retrievability*).

 Referencias

 Enlaces externos
 Hashcash (Inglés)
 Sistema de Finney (Inglés)
 Bit gold. *Describe un sistema monetario completo (including generation, storage, assay, and transfer) basado en funciones POW, y el problema de la arquitectura de máquinas generado por el uso de estas funciones. (Inglés)*
