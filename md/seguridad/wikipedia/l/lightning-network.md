---
type: Artículo de enciclopedia
title: Lightning Network
description: La red Lightning, en inglés Lightning Network, es una red entre pares (P2P) concebida como sistema de segunda capa para Bitcoin (BTC) que permite hacer micropagos de forma casi instantánea.
resource: https://es.wikipedia.org/wiki/Lightning_Network
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Lightning_Network"}
license: CC BY-SA 4.0
id: eswiki-Lightning_Network
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Lightning Network

- **Titulo:** Protocolo Lightning
- **Tipocabecera:** comunicación
- **Etiqueta1:** Familia:
- **Datos1:** Familia de protocolos de Internet
- **Etiqueta2:** Uso:
- **Datos2:** Pagos electrónicos
- **Etiqueta3:** Puerto:
- **Datos3:** 9735/TCP
- **Seccion4:** Lightning en el modelo TCP/IP
- **Etiqueta5:** Aplicación

La **red Lightning**, en inglés **Lightning Network**, es una red entre pares (P2P) concebida como sistema de segunda capa para Bitcoin (BTC) que permite hacer micropagos de forma casi instantánea.

Su diseño original fue publicado en enero de 2016 por Joseph Poon y Thaddeus Dryja.

 Conceptos fundamentales

Lightning Network propone que la escritura sobre la cadena de bloques se utilice exclusivamente para gestionar la apertura y cierre de canales de pagos bidireccionales.

Un usuario puede enviar bitcoines a cualquier otro destino dentro de la red Lightning. Para ello, la red encamina cada transacción mediante enrutamiento «cebolla» entre nodos no confiables, siguiendo una ruta formada por varios canales de pagos contiguos hasta alcanzar al destinatario final. Los pagos se tramitan de manera casi instantánea y con comisiones reducidas. A su vez, el receptor de los fondos puede tener la certeza de que no va a sufrir un ataque de doble gasto, que ninguno de los nodos intermedios puede robar los fondos y que mantiene el control total de los nuevos bitcoines recibidos.

Las transacciones que se tramitan a través de los canales de pagos se hacen fuera de bloque, es decir, no se registran en la cadena de bloques. Cada entidad que mantenga abierto un canal de pagos tiene la responsabilidad de guardar el estado asociado a la última transacción que haya enviado o recibido a través de ese canal, desechando por innecesarias cualquier otra transacción que haya recibido previamente. De esta manera, los dispositivos adaptados para el internet de las cosas pueden tramitar miles de transacciones con unos requisitos de *hardware* mínimos, tanto en capacidad de procesamiento como en almacenamiento de datos.

La red Lightning también permite la interconexión entre distintas cadenas de bloques. En una definición flexible del término, se puede considerar que Lightning Network proporciona una funcionalidad similar a un bus de servicio empresarial para entornos de arquitectura orientada a servicios, aunque en este caso, de acceso abierto y orientado a la coordinación de cadenas de bloques heterogéneas, como cadenas laterales y otras.

Las bajas comisiones hacen que Lightning sea especialmente apropiado para el envío y recepción de micropagos. Como los pagos son fuera de cadena, al menos a nivel teórico, sería posible hacer pagos incluso inferiores a la unidad mínima aceptable en la cadena de bloques (un satoshi, una cienmillonésima de bitcóin).

 Historia
Joseph Poon y Thaddeus Dryja publicaron un borrador del diseño de Lightning Network en febrero de 2015.

Lightning Network ha sido respaldado por el empresario de pagos móviles Jack Dorsey.

 2017 Primera transacción de Lightning en Litecoin
El 10 de mayo de 2017, Christian Decker de Blockstream realizó el primer pago completo y seguro de Lightning en una red que no sea de prueba, y el primer pago de Lightning en Litecoin, enviando un pago microscópico que normalmente no es posible ni económico en una blockchain, totalmente liquidado en una fracción de segundo.

 Antorcha Bitcoin Lightning de 2019
El 19 de enero de 2019, el usuario seudónimo de Twitter hodlonaut comenzó una prueba promocional de la Red Lightning a modo de juego enviando 100.000 satoshis (0,001 bitcoin) a un destinatario de confianza donde cada destinatario añadía 10.000 satoshis (0,34 dólares en ese momento) para enviar al siguiente destinatario de confianza. El pago de la "antorcha de rayo" llegó a personalidades notables como el CEO de Twitter Jack Dorsey, el creador de Litecoin Charlie Lee, la CEO de Lightning Labs Elizabeth Stark, y el CEO de Binance "CZ" Changpeng Zhao, entre otros. La antorcha de rayo se pasó 292 veces antes de alcanzar el límite anteriormente codificado de 4.390.000 satoshis. El pago final de la antorcha del rayo se envió el 13 de abril de 2019 como una donación de 4.290.000 satoshis (217,78 dólares en ese momento) a Bitcoin Venezuela, una organización sin ánimo de lucro que promueve el bitcoin en Venezuela.

 2021 Adopción en El Salvador
En junio de 2021, la Asamblea Legislativa de El Salvador votó una legislación para que el Bitcoin sea de curso legal en El Salvador. La decisión se basó en el éxito del ecosistema de Bitcoin Beach en El Zonte que utilizó una billetera basada en LN. El gobierno ha introducido un monedero que utiliza el protocolo Lightning Network mientras que da la libertad a los ciudadanos de utilizar otros monederos Bitcoin Lightning.

 Número de nodos
En septiembre de 2022, la capacidad de la red supera los 4600 bitcoins y existen 17 000 nodos con un total de 86 000 canales activos.

 Implementaciones principales
Varios equipos están desarrollando distintas implementaciones de la red Lightning  como *software* libre. Algunas de ellas son las siguientes:

 lnd: el primer daemon de la red Lightning, escrito en Go y desarrollado por Lightning Labs. Actualmente esta es la implementación que más popularidad ha conseguido y que más recursos tiene disponibles para que nuevos desarrolladores puedan crear aplicaciones para Lightning (Lapps) más fácilmente.
 C-lightning: el cliente escrito en C desarrollado por Blockstream.
 Lit: un cliente ligero con su propio monedero que no necesita ejecutar un nodo de Bitcoin.
 Eclair: el cliente para Lightning escrito en Scala de la empresa ACINQ.

 Consecuencias económicas
 Sobre la oferta monetaria

Para poder enviar fondos desde un emisor es necesario que los canales de pagos que participan en la ruta completa hasta el destino mantengan suficientes bitcoines reservados dentro de cada uno de esos canales de pagos. Si no es así, el pago no podrá llevarse a cabo, y el protocolo deberá encontrar otra ruta diferente que cumpla con esos requisitos.

Así, los fondos bajo el control de los nodos Lightning participan en la creación de la ruta de pago al destinatario, pero no pueden ser gastados para otros propósitos. Esto provoca que la parte de la base monetaria disponible para pagos sea sensiblemente inferior al número total de bitcoines obtenidos por minería, acentuando su carácter deflacionario original a medida que la red se extiende y aumenta el número de nodos Lightning y las rutas disponibles.

 Sobre la tasa de interés
Un operador de nodos de enrutamiento debe comprometer capital propio y al mismo tiempo debe atraer al capital de otros operadores de nodos de rutado para tramitar pagos hacia el exterior y ganar comisiones. Para que las rutas se adapten a las necesidades dinámicas de los usuarios finales, se genera un mercado de arrendamiento de canales similar al de los bonos. A diferencia de estos, no existe riesgo de impago ya que el arrendatario solo mantiene el control de los bitcoines durante un periodo previamente acordado, y los fondos comprometidos solo se pueden usar en la red Lightning para ofrecer liquidez en la red.

Los arrendamientos de canales que pagan una prima dan como resultado un nuevo instrumento de generación de rendimiento de bajo riesgo. Ese coste de capital en la red Lightning fija la tasa de interés. Como existen duraciones variables de arrendamiento, se construye una curva de ganancias que marca la tasa de interés a corto y largo plazo. Este instrumento puede servir de base para construir productos estructurados de mayor nivel y derivados financieros.

 Contratos inteligentes
Sobre la base de la red Lightning se espera que en el futuro también sea posible ejecutar contratos inteligentes sin registrar sus términos legales en la cadena de bloques. Por ejemplo, dos usuarios pueden acordar un contrato de futuros y recibir el resultado desde una máquina oráculo en la fecha de vencimiento, que dispararía el pago para cada uno de los partícipes según lo convenido de manera irrevocable.

 Monederos

 Muun Wallet: Monedero de custodia propia y código abierto con soporte para hacer transacciones tanto en la red Lightning como en Bitcoin.

 Wallib: Una billetera global para realizar transacciones a través de Bitcoin y Lightning.

 Strike: No está construido sobre una red monetaria opcional, está construido sobre LA red monetaria.
 Blue Wallet: Blue Wallet es compatible con los monederos Bitcoin y Lightning.

 Véase también

 https://lightning.network
 https://dci.mit.edu/lightning-network/
 https://lists.linuxfoundation.org/pipermail/lightning-dev/
 https://www.criptonoticias.com/criptopedia/que-es-lightning-network-red-canales-pago-bitcoin-blockchain/

 Referencias
