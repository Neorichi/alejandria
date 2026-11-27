---
type: Artículo de enciclopedia
title: Teoría de códigos
description: La teoría de códigos es una especialidad matemática que trata de las leyes de la codificación de la información.
resource: https://es.wikipedia.org/wiki/Teoría_de_códigos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Teoría_de_códigos"}
license: CC BY-SA 4.0
id: eswiki-Teoría_de_códigos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Teoría de códigos

La **teoría de códigos** es una especialidad matemática que trata de las leyes de la codificación de la información. A grandes rasgos, codificar es transformar una información en una señal convenida para su comunicación. Decodificar sería el proceso inverso y complementario del anterior por el cual la señal comunicada es transformada en la información original. El auge de las comunicaciones a partir de la segunda mitad del  motivó un fuerte desarrollo de la teoría de códigos.

 Introducción e historia

Puesto que los códigos se usan para comunicar información, uno de los problemas a los que todo código se enfrenta es el error sistemático y, también, el fortuito. La redundancia es el único medio de prevenir el error. Los lenguajes humanos tienen una gran redundancia que les da flexibilidad a costa, eso sí, de eficacia. Los códigos matemáticos utilizan una redundancia más racional.

Hay códigos llamados de *detección de errores*, que permiten detectar alteraciones en un mensaje codificado. Se utilizan sobre todo en entornos donde el mensaje puede ser reenviado tantas veces como se necesite. Los protocolos de Internet, por ejemplo, están formados por un anidamiento de codificaciones desde el nivel de transporte hasta el nivel físico, teniendo cada nivel su propio sistema de detección de errores.

Este tipo de códigos resulta inadecuado en entornos donde la comunicación no se puede repetir y se necesita asegurar hasta cierto punto que se va a recibir la información correcta. Un ejemplo típico y vistoso es cuando se envía una nave espacial a los confines del sistema solar y desde allí debe enviar una serie de fotografías antes de que se le acaben, digamos, las pilas. Se trata de una situación delicada, porque si las ondas electromagnéticas que portan la información llegan distorsionadas toda la misión fracasa. Un código que solo detectase que la información es incorrecta no serviría para nada. Es necesario algo más, un código no solo detector sino *corrector de errores*.

Por ejemplo, el sistema de codificación más sencillo puede consistir en que un "0" se representa un "no" y con un "1" un sí. En este caso, si quiero transmitir un "si", y se comete un error al transmitir un "0" en vez del "1", el receptor del mensaje hará lo opuesto a lo pedido. Pero si en cambio se conviene que "00" sea "no" y "11" sea "sí", entonces, si se comete un error en un dígito, y por ejemplo el receptor recibe un "01", detectará que hubo un error, aunque no sabrá cual es el mensaje correcto. En cambio si la convención es que "000" es "no" y "111" un sí, y se supiese que al transmitir un mensaje solo es posible, por la metodología utilizada, cometer un solo error de dígito, entonces, si al recibir un "001", el receptor sabrá que se trata de un "no". Así siguiendo, si transmitimos un bloque de ceros, o un bloque de unos, aunque se cometan algunos errores en la transmisión de algunos dígitos, se tendrá la casi certeza de cual es el error cometido en el mensaje recibido, y corregirlo.

En la actualidad, los avances que se están produciendo en esta disciplina están encaminados hacia la utilización de las bases de Groebner como herramienta para la codificación y decodificación en los códigos detectores de errores.

 El problema de la codificación eficiente
Uno de los principales problemas de la teoría de códigos es el siguiente. Supongamos que tenemos una fuente de información que emite o transmite "símbolos" de cierto conjunto  que por propósitos pedagógicos llamaremos simplemente "palabras", de forma que la probabilidad de emisión de una palabra sea independiente del símbolo anterior , siendo . Si  es un alfabeto de *D* "letras", ¿qué código debe asignársele a la palabra  usando "letras" del alfabeto de tal manera que se consiga una codificación tan económica como sea posible?
Formalmente una codificación es una aplicación  del conjunto de "palabras" en el conjunto de secuencias finitas de "letras" del alfabeto. Un mensaje es una secuencia finita de palabras, , si se dispone de una codificación de palabras, ésta se extiende inmediatamente a mensajes mediante concatenación:

Algunos tipos de codificaciones interesantes son:
 Una codificación es **unívocamente descifrable** si cualquier secuencia finita de  es la imagen de como mucho un mensaje, es decir, cuando la aplicación E es inyectiva.
 Una codificación es **instantáneamente descifrable**, o de tipo prefijo, si no existen dos palabras diferentes  y  tal que  es una secuencia inicial de .

 Desigualdad de Kraft

 Desigualdad de McMillan

Codificación criptográfica

La criptografía o codificación criptográfica es la práctica y el estudio de técnicas de comunicación segura en presencia de terceros (llamados adversarios). En términos más generales, se trata de construir y analizar protocolos que bloquean a los adversarios; diversos aspectos de la seguridad de la información, como la confidencialidad, la integridad de los datos, la autenticación y el no repudio son fundamentales para la criptografía moderna. La criptografía moderna existe en la intersección de las disciplinas de matemáticas, informática e ingeniería eléctrica. Las aplicaciones de la criptografía incluyen tarjetas de cajero automático, contraseñas de ordenador y comercio electrónico.

La criptografía antes de la era moderna era efectivamente sinónimo de *cifrado*, la conversión de información de un estado legible a aparentes *nonsense*. El autor de un mensaje cifrado compartió la técnica de decodificación necesaria para recuperar la información original solo con los destinatarios previstos, evitando así que personas no deseadas hicieran lo mismo. Desde la Primera Guerra Mundial y el advenimiento del ordenador, los métodos utilizados para llevar a cabo la criptología se han vuelto cada vez más complejos y su aplicación más extendida.

La criptografía moderna se basa en gran medida en la teoría matemática y la práctica informática; Los algoritmos criptográficos están diseñados en torno a suposiciones de dureza computacional, lo que hace que dichos algoritmos sean difíciles de romper en la práctica por parte de cualquier adversario. En teoría, es posible romper un sistema de este tipo, pero no es factible hacerlo por ningún medio práctico conocido. Por lo tanto, estos esquemas se denominan computacionalmente seguros; Los avances teóricos, por ejemplo, las mejoras en los algoritmos de factorización de enteros y la tecnología informática más rápida requieren que estas soluciones se adapten continuamente. Existen esquemas de seguridad teórica de la información que probablemente no se pueden descifrar ni siquiera con un poder de cómputo ilimitado; un ejemplo es la libreta de un solo uso, pero estos esquemas son más difíciles de implementar que los mejores mecanismos teóricamente rompibles pero computacionalmente seguros.

Codificación en línea

Un código de línea (también llamado modulación de banda base digital o método de transmisión de banda base digital) es un código elegido para su uso dentro de un sistema de comunicaciones para propósitos de transmisión de banda base. La codificación de línea se utiliza a menudo para el transporte de datos digitales.

La codificación de línea consiste en representar la señal digital para ser transportada por una señal discreta de amplitud y tiempo que está sintonizada de manera óptima para las propiedades específicas del canal físico (y del equipo receptor). El patrón  deforma de onda de voltaje o corriente que se utiliza para representar los 1 y 0 de datos digitales en un enlace de transmisión se denomina "codificación de línea". Los tipos comunes de codificación de línea son unipolar, polar, bipolar y Codificación Manchester.

Otras aplicaciones de la teoría de la codificación
Otra preocupación de la teoría de la codificación es diseñar códigos que ayuden a la sincronización. Se puede diseñar un código para que un cambio de fase se pueda detectar y corregir fácilmente y que se puedan enviar múltiples señales en el mismo canal.

Otra aplicación de códigos, utilizada en algunos sistemas de telefonía móvil, es el acceso múltiple por división de código (CDMA). A cada teléfono se le asigna una secuencia de código que no tiene correlación con los códigos de otros teléfonos. Al transmitir, la palabra clave se utiliza para modular los bits de datos que representan el mensaje de voz. En el receptor se realiza un proceso de demodulación para recuperar los datos. Las propiedades de esta clase de códigos permiten que muchos usuarios (con diferentes códigos) utilicen el mismo canal de radio al mismo tiempo. Para el receptor, las señales de otros usuarios aparecerán en el demodulador solo como un ruido de bajo nivel.

Otra clase general de códigos son los códigos de solicitud de repetición automática (ARQ). En estos códigos, el remitente agrega redundancia a cada mensaje para verificar errores, generalmente agregando bits de verificación. Si los bits de verificación no son consistentes con el resto del mensaje cuando llega, el receptor le pedirá al remitente que retransmita el mensaje. Todos los protocolos de red de área amplia excepto los más simples utilizan ARQ. Los protocolos comunes incluyen SDLC (IBM), TCP (Internet), X.25 (Internacional) y muchos otros. Existe un amplio campo de investigación sobre este tema debido al problema de hacer coincidir un paquete rechazado con un paquete nuevo. Normalmente se utilizan esquemas de numeración, como en TCP.

Pruebas en grupo
Para las pruebas en grupo se usa códigos de una manera diferente. Hay que considerar un gran grupo de artículos en los que muy pocos son diferentes de una manera particular (por ejemplo, productos defectuosos o sujetos de prueba infectados). La idea de las pruebas grupales es determinar qué elementos son "diferentes" utilizando la menor cantidad de pruebas posible. El origen del problema tiene sus raíces en la Segunda Guerra Mundial cuando las Fuerzas Aéreas del Ejército de los Estados Unidos necesitaban examinar a sus soldados para detectar sífilis.

Codificación analógica
La información se codifica de manera análoga en las redes neuronales de los cerebros, en el procesamiento de señales analógicas y la electrónica analógica. Los aspectos de la codificación analógica incluyen la corrección de errores analógicos,
compresión de datos analógicos y cifrado analógico.

Codificación neuronal
La codificación neuronal es un campo relacionado con la neurociencia que se ocupa de cómo la información sensorial y de otros tipos se representa en el cerebro mediante redes de neuronas. El objetivo principal de estudiar la codificación neuronal es caracterizar la relación entre el estímulo y las respuestas neuronales individuales o grupales y la relación entre la actividad eléctrica de las neuronas en el conjunto. Se cree que las neuronas pueden codificar información tanto digital como analógica, y que las neuronas siguen los principios de la teoría de la información y comprimen la información, y detectar y corregir errores en las señales que se envían por todo el cerebro y el sistema nervioso más amplio.

 Usos en el análisis de textos

El análisis de código es útil para intentar decodificar texto cifrado, si el código de protección utilizado es débil (por ejemplo, el código Caesar o Vigenère). La detección de las características estadísticas de un texto también permite verificar, incluso sin entender su lenguaje, si un texto ha tenido más de un autor (puede decirse que el todavía indescifrado Manuscrito Voynich tenía dos autores distintos). También permite analizar los textos de Víctor Hugo y, por estas características estadísticas, detectar la década de su escritura. El Centro Científico de IBM (IBM La Gaude, Francia) también estudió los discursos de Charles de Gaulle y mostró que estos discursos se extendieron con el tiempo, a excepción de algunos discursos «críticos» (como el del 30 de mayo de 1968). La Universidad de Stanford también comparó los vocabularios respectivos de Marcel Proust y Paul Valéry. El ingeniero Jean-Jacques Walter también llevó a cabo este análisis sobre el texto del Corán y defendió una tesis según la cual le atribuyó varias docenas de autores (al menos 30 autores diferentes, probablemente 50, como máximo 100), inicialmente en varios idiomas, durante un período de doscientos años..

 Referencias
 Notas

 Bibliografía

 Dominic Welsh (1988): *Codes and Cryptography*, Clarendon Press, Oxford, ISBN 0-19-853287-3

 Véase también
 Teoría de la información
