---
type: Artículo de enciclopedia
title: Prueba de apuesta
description: Un algoritmo de prueba de apuesta, también conocido por la sigla PoS (del inglés proof of stake), es un protocolo de consenso distribuido que asegura en una red de una criptomoneda la posesión de dichas monedas.
resource: https://es.wikipedia.org/wiki/Prueba_de_apuesta
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Prueba_de_apuesta"}
license: CC BY-SA 4.0
id: eswiki-Prueba_de_apuesta
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Prueba de apuesta

Un algoritmo de **prueba de apuesta**, también conocido por la sigla **PoS** (del inglés *proof of stake*), es un protocolo de consenso distribuido que asegura en una red de una criptomoneda la posesión de dichas monedas. Con PoS la probabilidad de encontrar un bloque de transacciones y recibir el premio correspondiente es directamente proporcional a la cantidad de monedas que uno tiene *delegadas*, evitando así que la confianza venga dada por la cantidad de trabajo invertido. Es un sistema diferente a la prueba de trabajo usada en la minería de criptodivisas como el bitcóin.

Se basa en la suposición de que quienes poseen más unidades de una moneda basada en PoS están especialmente interesados en la supervivencia y el buen funcionamiento de la red que otorga valor a dichas monedas y por tanto son ellos los más indicados para cargar con la responsabilidad de proteger al sistema de posibles ataques. Es por eso que el protocolo los premia con una menor dificultad para encontrar bloques (es inversamente proporcional al número de monedas que demuestren poseer).  Algunas de las Blockchains que utilizan esta tecnología son: Cardano, Algorand, Tezos y Polkadot.

Estrategias
Peercoin, lanzado en 2012, fue la primera criptomoneda que usaba prueba de apuesta. Realmente es un algoritmo híbrido entre prueba de trabajo y prueba de apuesta en la que la apuesta se basa en la edad de las monedas (en inglés, *coin-age*) del minero. Las monedas por edad es una medida de las monedas que posee y el número de días que están en el monedero. Para minar un bloque en Peercoin un minero tiene que resolver un problema SHA-256 similar al de Bitcoin. Sin embargo, la dificultad del problema a resolver será bajada basándose en la cantidad de monedas que está dispuesto a gastar. Para implementarlo el bloque incluye una transacción especial *coinstake* 'apuesta de monedas' en la cual se gastan monedas. La edad de las monedas consumidas en la transacción de apuesta de monedas decide cómo de difícil es la prueba de trabajo. El objetivo de todo esto es asegurar que el proceso de minado sea aleatorio y no dependa del poder computacional del minero.

Posteriormente se han desarrollado otras formas de algoritmos de prueba de apuesta como:
 Prueba de apuesta pura: consiste en simplemente hacer la construcción de bloques más fácil para aquellos que pueden mostrar que controlan una gran cantidad de moneda. Es similar a como actúa Peercoin solo que la age no se tiene en cuenta. La desventaja de este enfoque es que, a diferencia de Peercoin en el cual se gasta la coin-age después de construir un bloque, el más rico siempre tiene más facilidad para construir las pruebas los bloques de la cadena.
 Prueba de depósito o en inglés *Proof-of-deposit*: en este enfoque cuando las monedas son usadas por los creadores de bloques para crear un bloque, son congeladas hasta que se confirmen cierta cantidad de bloques. Esto es similar a la que se hace con las coin-age: En lugar de recompensar a un minero por almacenar monedas que no han sido gastadas durante un largo tiempo en el pasado, el sistema recompensa a los mineros que están dispuestos a tener monedas inmóviles durante largo tiempo en el futuro.
 Prueba de puesta alquilada o en inglés *Leased Proof of Stake (LPoS)*: la idea principal de esta variante consiste en que los poseedores de tokens pueden alquilar sus nodos para realizar el proceso de generación de nuevos bloques. Cuando un usuario alquila sus tokens, estos se quedan bloqueados, de forma que no se pueden gastar hasta que el usuario cancele el arrendamiento. Cuanto mayor sea la cantidad alquilada a un nodo, mayores serán las posibilidades de que ese nodo sea seleccionado para crear el siguiente token, recibiendo así una recompensa.
 Prueba de apuesta delegada o en inglés *Delegated Proof of Stake (DPoS)*: en esta variante todos los usuarios de la red ponen en juego sus tokens y, por medio de una votación democrática, deciden qué delegados pueden generar el nuevo bloque en la cadena de bloques. Cada poseedor de al menos un token puede votar sobre quién valida las transacciones en la red, y el poder del voto se pondera según el número de tokens que posea el usuario. Esta votación se realiza de manera continua y los delegados ineficaces pueden ser sustituidos por otro en cualquier instante. Esto implica que los delegados se vean obligados a actuar de manera correcta si desean seguir recibiendo el apoyo de sus votantes. Los delegados reciben recompensas de producción de bloques cada vez que validan un bloque en la cadena de bloques y, como retribución por respaldar a un delegado, sus votantes reciben una parte proporcional a la cantidad de tokens confiados en ese delegado.
 Prueba de apuesta líquida o en inglés *Liquid Proof of Stake (LPoS)*: en este enfoque la delegación es opcional. Se permite a los dueños de los tokens delegar sus derechos de validación a otros usuarios sin tener que renunciar a la propiedad de sus tokens. Los usuarios deciden si apostar sus propios tokens o si delegar sus derechos de validación a otros usuarios. Como resultado, la red es más igualitaria, ya que usuarios con grandes cantidades de tokens pueden convertirse en validadores apostando sus propios tokens sin requerir colaboración externa pero, por otro lado, también los usuarios con menos tokens y sin capacidad para validar bloques por sí mismos, pueden apostar apoyando a usuarios más grandes o formando coaliciones con otros usuarios. Mientras que en DPoS el número de nodos validadores es fijo, aquí es dinámico.
Prueba de importancia o en inglés *Proof of Importance (PoI)*: este protocolo, el cual fue introducido por NEM y se basa en la prueba de apuesta, incluye más variables a la hora de elegir al nodo validador. Esto se hace para intentar solventar los problemas que puede causar el PoS como, por ejemplo, la priorización de entidades en función de la cantidad de tokens que posee.  Este protocolo recompensa a los usuarios que quieren validar un nuevo bloque, eligiéndolos en función del número de transacciones que se han realizado en el último mes, haciendo que se le dé menos importancia a la cantidad de monedas que se aportan para la validación y más importancia a la cantidad de movimientos realizados.
Prueba de validación o en inglés *Proof of Validation (PoV)*: en este mecanismo el consenso se logra por medio de nodos de validación. Todos estos nodos almacenan una copia de toda la secuencia de transacciones que se han producido en una cadena de bloques, así como una copia de las cuentas de usuario identificables por la clave pública de un usuario y los tokens que ese nodo posee. Los usuarios tienen la posibilidad de apostar tokens dentro de los nodos de validación, de modo que el número de tokens apostados determina el número de nodos que pasa a poseer ese validador.  Para confirmar un nuevo bloque es necesario que un grupo de validadores con al menos dos tercios del poder de voto total de la red, envíen un voto para confirmar ese bloque.
Prueba de apuesta híbrida o en inglés *Hybrid Proof of Stake (HPoS):* La mayoría de sistemas que implementan este mecanismo utilizan elementos de PoW y PoS para realizar las operaciones de validación de una transacción. El procedimiento habitual es el siguiente: mineros de PoW  generan nuevos bloques que van a guardar la transacción y después se validan estos bloques mediante PoS, de forma que se vota si estos bloques son seguros o no, registrándolos así en la cadena de bloques.  Este protocolo ayuda a mantener la seguridad del sistema, ya que combate el problema del 51%, haciendo que sea mucho más difícil conseguir el monopolio para la generación de un bloque.

Problemas
Los algoritmos de prueba de apuesta son un área activa de investigación y se tienen una serie de problemas.

Problema de nada en juego
El problema de nada en juego, en inglés *nothing-at-stake* o también *stake-grinding* consiste en que realmente confirmar bloques, salvo la consideración de que están dañando el sistema del que son participantes, no tiene ningún coste real por lo que no se incentiva el consenso.  Veamos un ejemplo:

Supongamos que un atacante con una proporción de monedas inferior al 50 % intenta crear una cadena alternativa de k bloques.  Este ataque fallará con una probabilidad que crece exponencialmente con k. En la minería de prueba de trabajo un ataque fallido tiene un coste significativo porque el minero podría haber ganado las recompensas al minar en lugar de malgastar los recursos en el ataque fallido. Sin embargo en este tipo de algoritmos el coste no existe. Un minero puede usar su participación para minar en la actual cadena más larga mientras simultáneamente intenta crear una bifurcación de la cadena. Si su cadena alternativa tiene éxito habrá consumido una cantidad grande de su participación. Si falla, el registro de su intento fallido no será reflejada en la cadena más larga. Una actuación racional de un minero podría ser constantemente intentar hacer una bifurcación de la cadena.

Se han hecho varios intentos para solucionar este problema. La mayoría de esquemas utilizan puntos de control para prevenir bifurcaciones largas lo cual es una pequeña amenaza a considerarse un protocolo de consenso descentralizado. Ethereum ha propuesto una técnica a la que llama 'recorte' que permite el castigo a los mineros que intenten bifurcar la cadena.

Exposición de las monedas

Con PoS la probabilidad de encontrar un bloque de transacciones es directamente proporcional a la cantidad de monedas que uno tiene acumuladas, lo cual en primera instancia implica que el monedero esté conectado a la red, lo cual a su vez implica que el monedero está expuesto a posibles problemas de seguridad. Para intentar evitar este problema se ha desarrollado una variante del protocolo a la que se llama prueba de apuesta delegada, también conocido por las siglas DPoS (del inglés *Delegated Proof of Stake*). En esta variante se permite que los nodos propietarios de monedas deleguen sus privilegios para construir nuevos bloques en un nuevo tipo de nodos llamados representantes. Ejemplo de sistema usando este algoritmo es BitShares.

Ahorrando para atacar
En algunos sistemas que usan PoS es posible ahorrar derechos para conseguir mucho poder de minado para poder introducir una bifurcación de la cadena. Esto es posible incluso si se usan sistemas como Slasher para desalentar las bifurcaciones. Para evitar este tipo de ataques Peercoin limita el parámetro edad a 90 días cuando calcula la edad de las monedas.

Ataque del 51 %
Si un apostante obtiene el 51 % del factor de apuesta, entonces puede mantenerlo para siempre apostando por encima de sus propios bloques, tomando de esta forma el control de la cadena. Incluso si un participante emergiera apostando recompensas y transacciones, el apostante del 51 % obtendrá esta nueva apuesta y lentamente se aproximará hasta llegar al 100 %. En el minado por prueba de trabajo, incluso si existiera un minero con el 51 % siempre sería posible que algún nuevo minero pudiera emerger con más equipamiento de minería y energía y reducir la mayoría del minero del 51 %. Con la prueba de apuesta es mucho más difícil evitar este problema.

Análisis
Ventajas:
 Se puede llegar a tener un grado de seguridad equivalente al obtenido con prueba de trabajo pero con un gasto energético menor.
 Reducción de la huella de carbono: dado que no se necesita tanta potencia para mantener la cadena de bloques segura, se reduce drásticamente el consumo energético.
 Mejora de la descentralización ya que cada usuario puede apostar en la red siempre y cuando cumpla con su cuota de apuesta.
 La entrega de recompensas es más proporcional debido al sistema seudoaleatorio a la hora de elegir el nodo ganador, abandonando la carrera tecnológica del sector minero.
Desventajas:
 Al dejar el monedero en línea se expone a problemas de seguridad.
 Como los fondos que protegen están asociados a una dirección IP es más difícil mantener el anonimato.
 Demasiado poder para los mayores tenedores de monedas.

Ejemplos
Es usado en distintas criptomonedas como por ejemplo:
 Cardano (DPOS), prueba de apuesta delegada
 Peercoin(mezcla PoW y PoS).
 Nxt (enteramente PoS).
 E-Dinarcoin EDR (DPOS), prueba de apuesta delegada
 Gridcoin
 BlackCoin
 Reddcoin
 NAV Coin (en fase PoS)
 DeepOnion Coin (en fase PoS)
 PIVX (enteramente PoS).
 Arepacoin (mezcla PoW y PoS)
 Scolcoin (en fase PoS).
 DogeCash (enteramente PoS).
 Tezos (LPoS), prueba de apuesta líquida.
 Waves (LPoS), prueba de apuesta arrendada.
 NIX (LPoS), prueba de apuesta arrendada.
 Algorand, prueba de apuesta pura
 Decred (HPoS), prueba de apuesta híbrida.

 Véase también
 Prueba de trabajo

 Referencias
