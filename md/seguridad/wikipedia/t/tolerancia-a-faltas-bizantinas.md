---
type: Artículo de enciclopedia
title: Tolerancia a faltas bizantinas
description: "La tolerancia a faltas bizantinas (BFT) es la resistencia de un sistema informático tolerante a faltas, en particular los sistemas informáticos distribuidos, a fallas de componentes electrónicos donde hay información …"
resource: https://es.wikipedia.org/wiki/Tolerancia_a_faltas_bizantinas
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Tolerancia_a_faltas_bizantinas"}
license: CC BY-SA 4.0
id: eswiki-Tolerancia_a_faltas_bizantinas
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Tolerancia a faltas bizantinas

La **tolerancia a faltas bizantinas** (BFT) es la resistencia de un sistema informático tolerante a faltas, en particular los sistemas informáticos distribuidos, a fallas de componentes electrónicos donde hay información imperfecta sobre si un componente falla. En una "falla bizantina", un componente, como un servidor, puede aparecer de manera incoherente, fallando y funcionando para sistemas de detección de fallas, presentando diferentes síntomas a diferentes observadores. Es difícil para los otros componentes declarar que falló y cerrarlo fuera de la red, ya que primero necesitan llegar a un consenso sobre qué componente falla. El término se deriva del problema de los generales bizantinos, donde los actores deben acordar una estrategia concertada para evitar una falla catastrófica del sistema, pero algunos de los actores no son confiables. También se ha hecho referencia a la tolerancia a faltas bizantinas con las frases **consistencia interactiva** o **congruencia de fuente**, **avalancha de error**, **problema de acuerdo bizantino**.

 Trasfondo
Una falta bizantina es cualquier falta que presenta síntomas diferentes a diferentes observadores. Una falla bizantina es la pérdida de un servicio del sistema debido a una falta bizantina en sistemas que requieren consenso.

El objetivo de la tolerancia a faltas bizantinas es poder defenderse contra fallas bizantinas, en las cuales los componentes de un sistema fallan con síntomas que impiden que algunos componentes del sistema lleguen a un acuerdo entre ellos, donde tal acuerdo es necesario para el correcto funcionamiento del sistema. Los componentes que funcionan correctamente de un sistema tolerante a faltas bizantinas podrán proporcionar el servicio del sistema, suponiendo que no haya demasiados componentes defectuosos.

Las fallas bizantinas se consideran la clase de fallas más general y más difícil entre los modos de falla. El llamado modo de falla fallida ocupa el extremo más simple del espectro. Mientras que el modelo de falla fallida simplemente significa que la única manera de fallar es un bloqueo de nodo, detectado por otros nodos, las fallas bizantinas no implican restricciones, lo que significa que el nodo fallido puede generar datos arbitrarios, pretendiendo ser uno correcto. Por lo tanto, las fallas bizantinas pueden confundir a los sistemas de detección de fallas, lo que hace que la tolerancia a fallas sea difícil. A pesar de la analogía, una falla bizantina no es necesariamente un problema de seguridad que involucre interferencia humana hostil: puede surgir exclusivamente de fallas eléctricas.

Los términos falta y falla se usan aquí de acuerdo con las definiciones estándar creadas originalmente por un comité conjunto sobre "Conceptos y terminología fundamentales" formado por el Comité técnico de computación confiable y tolerancia a fallas de la IEEE Computer Society y el Grupo de trabajo IFIP 10.4 sobre informática confiable y Tolerancia a fallos. Una versión de estas definiciones también se describe en la página de Wikipedia de confiabilidad.

 El problema de los generales bizantinos
*Bizantino* se refiere al problema de los generales bizantinos, un problema de acuerdo (descrito por Leslie Lamport, Robert Shostak y Marshall Pease en su artículo de 1982, "El problema de los generales bizantinos") en el que un grupo de generales comanda una parte del ejército bizantino , rodea una ciudad. Estos generales desean formular un plan para atacar la ciudad. En su forma más simple, los generales solo deben decidir si atacar o retirarse. Algunos generales prefieren atacar, mientras que otros prefieren retirarse. Lo importante es que cada general acuerde una decisión común, ya que un ataque poco entusiasta de unos pocos generales se convertiría en una derrota y sería peor que un ataque coordinado o una retirada coordinada.

El problema se complica por la presencia de generales traidores que no solo votan por una estrategia subóptima, sino que pueden hacerlo selectivamente. Por ejemplo, si nueve generales votan, cuatro de los cuales apoyan el ataque mientras que otros cuatro están a favor de la retirada, el noveno general puede enviar un voto de retirada a esos generales a favor de la retirada, y un voto de ataque al resto. Aquellos que recibieron un voto de retiro del noveno general se retirarán, mientras que el resto atacará (lo que puede no ser bueno para los atacantes). El problema se complica aún más por el hecho de que los generales están físicamente separados y tienen que enviar sus votos a través de mensajeros que pueden no entregar votos o pueden falsificar votos.

La tolerancia a faltas bizantinas se puede lograr si los generales leales (no defectuosos) tienen un acuerdo mayoritario sobre su estrategia. Tenga en cuenta que puede haber un valor de voto predeterminado para los mensajes perdidos. Por ejemplo, a los mensajes faltantes se les puede dar el valor "nulo". Además, si el acuerdo es que los votos "nulos" son la mayoría, se puede usar una estrategia predeterminada preasignada (por ejemplo, retirada).

El mapeo típico de esta historia en los sistemas informáticos es que las computadoras son los generales y sus enlaces del sistema de comunicación digital son los mensajeros. Aunque el problema está formulado en la analogía como un problema de toma de decisiones y de seguridad, en electrónica, no se puede resolver simplemente con firmas digitales criptográficas, porque las fallas como los voltajes incorrectos pueden propagarse a través del proceso de cifrado. Por lo tanto, un componente puede aparecer funcionando para un componente y defectuoso para otro componente, lo que impide formar un consenso sobre si el componente es defectuoso o no.

 Ejemplos de fallas bizantinas
Varios ejemplos de fallas bizantinas que han ocurrido se dan en dos journal papers equivalentes. Estos y otros ejemplos se describen en las páginas web de NASA DASHlink. Estas páginas web también describen algunas fenomenologías que pueden causar fallas bizantinas.

Los errores bizantinos se observaron con poca frecuencia y en puntos irregulares durante las pruebas de resistencia para los submarinos de la clase Virginia recién construidos, al menos hasta 2005 (cuando los problemas se informaron públicamente).

En un problema similar se usa como ejemplo a enjambres de abejas. Ellas tienen que encontrar un nuevo hogar, y muchas exploradoras y demás abejas tienen que llegar a un consenso sobre a cuál de los hogares candidatos podrían volar. Y luego todos tienen que volar allí, con su reina. El enfoque de las abejas funciona de manera confiable, pero cuando los investigadores ofrecen dos colmenas, igualmente atractivas según todos los criterios de las abejas, se produce una catástrofe, el enjambre se rompe y todas las abejas mueren.

 Soluciones tempranas
Varias soluciones fueron descritas por Lamport, Shostak y Pease en 1982. Comenzaron por señalar que el problema de los generales puede reducirse a resolver un problema de "comandante y tenientes" donde los tenientes leales deben actuar al unísono y que su acción debe corresponder a lo que el Comandante ordenó en el caso de que el Comandante sea leal.
 Una solución considera escenarios en los que los mensajes pueden falsificarse, pero que serán tolerantes a faltas bizantinas siempre que el número de generales traidores no sea igual o exceda un tercio de los generales. La imposibilidad de tratar con un tercio o más de los traidores finalmente se reduce a probar que el problema de un Comandante y dos Tenientes no puede ser resuelto, si el Comandante es traidor. Para ver esto, supongamos que tenemos un Comandante A traicionero y dos Tenientes, B y C: cuando A le dice a B que ataque y C a retirarse, y B y C se envían mensajes entre sí, reenviando el mensaje de A, ni B ni C pueden averiguar quién es el traidor, ya que no es necesariamente A--otro Teniente podría haber falsificado el mensaje supuestamente de A. Se puede demostrar que si n es el número de generales en total, y t es el número de traidores en ese n , entonces hay soluciones al problema solo cuando n> 3t y la comunicación es sincrónica (retardo acotado).
 Una segunda solución requiere firmas de mensajes no forzables. Para los sistemas de seguridad crítica, las firmas digitales (en los sistemas informáticos modernos, esto se puede lograr en la práctica usando la criptografía de clave pública) pueden proporcionar tolerancia a faltas bizantinas en presencia de un número arbitrario de generales traidores. Sin embargo, para los sistemas de seguridad crítica, los códigos de detección de errores sencillos, como los CRC, proporcionan una cobertura más débil pero a menudo suficiente a un costo mucho más bajo. Esto es cierto para las faltas bizantinas y no bizantinas. Por lo tanto, los métodos de firma digital criptográfica no son una buena opción para los sistemas de seguridad crítica, a menos que también haya una amenaza de seguridad específica. Si bien los códigos de detección de errores, como los CRC, son mejores que las técnicas criptográficas, ninguno proporciona una cobertura adecuada para la electrónica activa en los sistemas de seguridad crítica. Esto se ilustra mediante el escenario de CRC de Schrödinger donde un mensaje protegido por CRC con un solo bit bizantino defectuoso presenta datos diferentes para diferentes observadores y cada observador ve un CRC válido.
 También se presenta una variación de las dos primeras soluciones que permiten el comportamiento tolerante a faltas bizantinas en algunas situaciones en las que no todos los generales se pueden comunicar directamente entre sí.
Varias arquitecturas de sistema fueron diseñadas hacia 1980 que implementaron la tolerancia a faltas bizantinas. Estos incluyen: FTMP de Draper, MMFCS de Honeywell y SIFT de SRI.

 Práctica de la tolerancia a faltas bizantinas
En 1999, Miguel Castro y Barbara Liskov introdujeron el algoritmo de "Práctica de tolerancia de faltas bizantinas" (PBFT), que proporciona replicación de estado de máquina bizantina de alto rendimiento, procesando miles de solicitudes por segundo con aumentos de latencia en sub-milisegundos.

Después de PBFT, se introdujeron varios protocolos BFT para mejorar su robustez y rendimiento. Por ejemplo, Q/U, HQ, Zyzzyva y ABsTRACT, etc. abordaron los problemas de rendimiento y costo; mientras que otros protocolos, como Aardvark y RBFT, abordaron sus problemas de robustez. Además, Adapt intentó hacer uso de los protocolos BFT existentes, cambiando entre ellos de una manera adaptativa, para mejorar la solidez y el rendimiento del sistema a medida que cambian las condiciones subyacentes. Además, se introdujeron protocolos BFT que aprovechan los componentes fiables para reducir el número de réplicas, por ejemplo, A2M-PBFT-EA y MinBFT.

 Software
UpRight es una biblioteca de código abierto para la construcción de servicios que toleran los bloqueos ("up") y los comportamientos bizantinos ("right") que incorporan muchas de las innovaciones de estos protocolos.

Además de PBFT y UpRight, está la biblioteca BFT-SMaRt,, una biblioteca de replicación de máquinas de estado tolerantes a faltas bizantinas de alto rendimiento desarrollada en Java. Esta biblioteca implementa un protocolo muy similar al de PBFT, además de protocolos complementarios que ofrecen transferencia de estado y reconfiguración sobre la marcha de hosts. BFT-SMaRt es el esfuerzo más reciente para implementar la replicación de máquina de estado, que aún se mantiene activamente.

Archistar utiliza una delgada capa de BFT para la comunicación. Crea un prototipo de un sistema de almacenamiento seguro en varias nubes utilizando Java con licencia bajo LGPLv2. El enfoque se basa en la simplicidad y la legibilidad, y pretende ser la base de futuros proyectos de investigación.

Askemos es una plataforma de programación concurrente, garbage-collected y persistente, en la cima de las máquinas de estado replicadas que tolera las faltas bizantinas. Es un prototipo de un entorno de ejecución que facilita los contratos inteligentes.

Tendermint es un software de uso general para la replicación de máquinas de estado BFT. Usando un protocolo de socket, permite que las máquinas de estado se escriban en cualquier lenguaje de programación, y proporciona medios para que la máquina de estado pueda influir en los elementos del consenso, como la lista de procesos activos. Tendermint se implementa en el estilo de una cadena de bloques, que amortiza los gastos generales de BFT y permite una recuperación más rápida de la falla.

 En la práctica
Un ejemplo de BFT en uso es bitcoin, un sistema de moneda digital peer-to-peer. La red bitcoin funciona en paralelo para generar una cadena de prueba de trabajo de estilo Hashcash. La cadena de prueba de trabajo es la clave para superar las fallas bizantinas y alcanzar una visión global coherente del estado del sistema.

Algunos sistemas de aeronaves, como el Sistema de manejo de información de la aeronave Boeing 777 (a través de su red ARINC 659 SAFEbus), el sistema de control de vuelo del Boeing 777 y los sistemas de control de vuelo Boeing 787, utilizan tolerancia a faltas bizantinas. Debido a que estos son sistemas en tiempo real, sus soluciones de tolerancia a faltas bizantinas deben tener una latencia muy baja. Por ejemplo, SAFEbus puede lograr tolerancia a faltas bizantinas con un orden de un microsegundo de latencia agregada.

Algunas naves espaciales como el sistema de vuelo del SpaceX Dragon consideran a la tolerancia a faltas Bizantinas en su diseño.

Los mecanismos de tolerancia a faltas bizantinas utilizan componentes que repiten un mensaje entrante (o simplemente su firma) a otros destinatarios de ese mensaje entrante. Todos estos mecanismos suponen que el acto de repetir un mensaje bloquea la propagación de los síntomas bizantinos. Para sistemas que tienen un alto grado de criticidad de seguridad o protección, estas suposiciones deben probarse como verdaderas para un nivel aceptable de falta de cobertura. Al proporcionar evidencias a través de pruebas, una dificultad es crear una gama suficientemente amplia de señales con síntomas bizantinos. Tal prueba probablemente requerirá inyectores de faltas especializados.

 Véase también

 Commit atómico
 Algoritmo Brooks–Iyengar
 Lista de conceptos matemáticos con nombres de lugares
 Lista de términos relacionados con algoritmos y estructuras de datos
 Paxos bizantino
 Acuerdo cuántico bizantino

 Referencias

 Enlaces externos
 Ocean Store replica los datos con un protocolo de compromiso tolerante a errores bizantinos.
 práctica de tolerancia de errores bizantinos
 Tolerancia de errores bizantinos en el RKBExplorer
 UpRight es una biblioteca de código abierto para la replicación de máquinas de estado tolerantes a crasheos y tolerantes a bizantinos.
 Bft-SMaRt es una biblioteca de replicación de máquinas de estados tolerante a errores Bizantinos de alto rendimiento desarrollada en Java con simplicidad y solidez como requisitos principales.
