---
type: Artículo de enciclopedia
title: SegWit
description: "Segregated Witness (en español Testigo Segregado), popularmente conocido como SegWit, es una característica y formato de transacción propuesto por Blockstream y Bitcoin Core para Bitcoin (BTC) activado mediante un Soft …"
resource: https://es.wikipedia.org/wiki/SegWit
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SegWit"}
license: CC BY-SA 4.0
id: eswiki-SegWit
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SegWit

**Segregated Witness** (en español **Testigo Segregado**), popularmente conocido como **SegWit**, es una característica y formato de transacción propuesto por Blockstream y Bitcoin Core para Bitcoin (BTC) activado mediante un Soft Fork Activado por el Usuario el 24 de agosto de 2017 y adoptado también por las criptomonedas alternativas Litecoin, DigiByte, Bitcore y Vertcoin.

Fue presentado bajo el nombre formal de "*Segregated Witness (Capa de Consenso)*" a través de la "*Propuesta de mejora de Bitcoin BIP141*".

Su propósito principal es solucionar el problema de maleabilidad de transacciones y mitigar el impacto negativo del *límite máximo del tamaño de los bloques* en la velocidad del procesamiento de las transacciones de la red de Bitcoin (BTC). Esto lo aborda dividiendo la transacción en dos segmentos, quitando la firma de desbloqueo (la cual denomina datos del "testigo") de su lugar original y añadiéndola como una estructura separada al final. Adicionalmente, contabiliza el restante original del segmento de datos normalmente, mientras que el segmento del "testigo" lo contabiliza como una cuarta parte de su tamaño real.

 Antecedentes

 Escasez de espacio en los bloques de Bitcoin
Bitcoin asienta sus transacciones en un registro público, descentralizado y transparente que se actualiza añadiendo bloques de datos vinculados de forma retroactiva mediante el uso de hashes criptográficos. Cada bloque de datos almacena información sobre quienes envían y reciben *bitcoins*, así como la firma criptográfica que aprueba cada transacción. Si bien originalmente, no existía un tamaño máximo de los bloques, debido a sospechas de que un atacante podría intentar ejecutar un ataque DDoS Satoshi Nakamoto decidió agregar un límite máximo de 1 MB en el tamaño de los bloques como medida temporal de prevención. El objetivo de esto era que si un atacante intentaba saturar la red, su acción sería detectado instantáneamente y su ataque sería rechazado.

Como consecuencia de esta característica, a medida que fue aumentando la demanda de espacio en cadena, el mismo comenzó a hacerse escaso debido a dicha limitación.
 Problemas de escalabilidad y maleabilidad
Según la perspectiva de Bitcoin Core, el diseño actual de la blockchain de Bitcoin tiene dos principales deficiencias:

 **Escalabilidad**: Los nuevos bloques se añaden al registro en intervalos aleatorios que promedian los 10 minutos. Esto, en conjunto con el límite impuesto al tamaño de los bloques, limita el número de transacciones que es posible asentar en el mismo. Debido a la negativa de escalar los bloques por encima de 1 MB por medio de una bifurcación dura (como recomendó Satoshi en 2010 y como ha hecho Bitcoin Cash), se ha planteado la necesidad de solucionar este problema acudiendo a la realización masiva de transacciones fuera de la cadena, la aceptación de transacciones sin esperar su inclusión en el registro (denominadas *0-conf* o *transacciones de confirmación cero*), y/u otros cambios radicales del protocolo, como en el caso de FlexTrans (Transacciones Flexibles), que propone hacer las transacciones muchos más pequeñas cambiando la forma en la que están descritas a un sistema de etiquetado, permitiendo así más transacciones por bloque.

 **Maleabilidad**: El problema de maleabilidad de las transacciones plantea que aunque cada transacción esté firmada criptográficamente, dicha firma no abarca todos los datos de la transacción, lo que hace posibles varias formas diferentes de perder o robar bitcoins. Aunque una serie de soluciones diferentes para esto han sido propuestas, el problema aún existe.

 SegWit como solución
SegWit es presentado por Bitcoin Core como un aumento "de facto" del tamaño de los bloques debido a que cambia la definición del tamaño para medirlo como en términos de millón de *unidades* en lugar de en *bytes*. Los datos de firma del testigo serían separados del registro del árbol de Merkle, el cual contiene información sobre quién está enviando o recibiendo los bitcoines, y se moverían hasta el final. Además, cada byte de ellos se contarían como si fuesen un cuarto de una *unidad*. El efecto general de esto sería cambiar el tamaño promedio del bloque de 1 MB a aproximadamente 1.8 MB. También aborda el problema de maleabilidad de las firmas, al moverlas fuera de los datos de la transacción y haciéndolas imposibles de cambiar, la identificación de la transacción ya no es maleable. Esto hace que Bitcoin sea más seguro de usar, lo cual mejoraría su compatibilidad con Lightning Network (un sistema que permite procesar micro-pagos de forma casi gratuita e instantánea que sólo requeriría usar la blockchain al principio y al final de su ejecución) lo que sería ligeramente arriesgado mientras el problema de maleabilidad exista. Y adicionalmente, propone mantener una importante compatibilidad con aquellos nodos que ejecuten versiones no actualizadas del software.

 Historia
Según la especificación BIP141 publicada en el repositorio de Github de Bitcoin Core por Eric Lombrozo, Johnson Lau y Pieter Wuille, SegWit fue diseñado para activarse el 15 de noviembre de 2017 mediante el estándar BIP 9,  el cual permite señalizar apoyo a una propuesta de actualización de la red a través de los escabezados de los bloques minados en la cadena de bloques.

 UASF, SegWit2x y otras polémicas
Debido a una controversia sobre el escalado de Bitcoin, inicialmente no había certeza sobre si el uso de BIP141 sería suficiente para concretar la activación de SegWit en la red Bitcoin.

El 25 de febrero de 2017 un desarrollador identificado bajo el seudónimo de *Shaolinfry* propuso a través de la lista de correo *bitcoin-dev*  un esquema alternativo denominado BIP148 o UASF.

Este esquema consistiría en que a partir del 1 de agosto de ese mismo año los nodos que lo ejecutasen rechazarían cualquier bloque que no incluyese una señalización en apoyo a la activación de SegWit vía BIP9.Algunos desarrolladores como Gregory Maxwell, fueron críticos con la característica indicando que podría ocasionar el desperdició de recursos y la división de la cadena afectando la seguridad de la blockchain.

El 23 de mayo de 2017 un grupo considerable de empresas identificadas como el Digital Currency Group (no confundir con la Digital Currency Initiative del Laboratorio de medios de comunicación del MIT) publicaron un acuerdo llamado *Bitcoin Scaling Agreement at Consensus 2017* (posteriormente conocido simplemente como *Acuerdo de Nueva York* o *NYA*) en apoyo a *SegWit2Mb* (más tarde conocida simplemente como *SegWit2x*), una propuesta que ofrecía la activación de SegWit y el aumento posterior del tamaño de los bloques a 2 MB por medio de una bifurcación dura en los próximos seis meses (alrededor del 23 de mayo de 2017).

El 19 de junio de 2017 la propuesta de SegWit2x ya contaba con un apoyo de al menos 79,9% del poder minero, sin embargo la misma fue controvertida debido a que el desarrollo del proyecto estaba limitado a un grupo cerrado de desarrolladores.

En junio de 2017, el debate en torno a SegWit se complicó aún más con afirmaciones de que podría violar patentes presentadas ante la USIPO.

 Activación de SegWit
A mediados de julio de 2017 se hizo evidente que los mineros apoyaban la implementación de Segwit como parte de un acuerdo antes del UASF BIP148 del 1 de agosto de 2017 que intentaba evitar una eventual bifurcación de la red.

El 21 de julio de 2017, los mineros de Bitcoin realizaron una actualización de software denominada BIP91, que establecía que SegWit se activaría cuando fuese minado el bloque número 477120. El 8 de agosto de 2017 se alcanzó otro hito cuando el 100 % de los grupos mineros indicaron compatibilidad con SegWit, aunque esta no se activaría hasta el 21 de agosto como mínimo (después de lo cual los mineros comenzarían a rechazar bloques que no incluyesen transacciones SegWit).

El 23 de agosto de 2017, es activado oficialmente Segwit durante el minado del bloque 481822, con un 99.95% de apoyo en la red.

Segregated Witness fue activado oficialmente en agosto de 2017.

 Acontecimientos posteriores

Durante la primera semana de octubre, la proporción de transacciones de red que utilizaban SegWit aumentó de 7 % a 10 %, indicando un aumento más grande en índice de uso.

El 8 de noviembre de 2017 los desarrolladores de SegWit2x anunciaron la cancelación de la bifurcación dura prevista para el 16 de noviembre de 2017 debido a la falta de consenso.

A partir de febrero de 2018, las transacciones de SegWit superan el 30 %.

 Propuestas de mejora de Bitcoin (BIP) relacionadas
**BIP91:** Umbral reducido Segwit MASF – Fue activado el 27 de julio de 2017.
**BIP141:** Segregated Witness (Ca*pa de Consenso)* – Fue activado el 23 de agosto de 2017.
**BIP142:** Formato de Dirección para Segregated Witness – Fue descartado y reemplazado por BIP 173.
**BIP143:** Firma de Verificación de Transacción para la Versión 0 del Programa Witness – Fue activado el 24 de agosto de 2017.
**BIP144:** Segregated Witness (Peer Services) – Fue activado el 24 de agosto de 2017.
**BIP148:** Activación obligatoria del despliegue de Segwit – Fue activado (ordenó la activación de BIP141, 143, 144).
**BIP173:** Direcciones de tipo Bech32, liberadas como parte de la versión 0.16.0 del cliente Bitcoin Core el 26 de febrero de 2018.

 Referencias
