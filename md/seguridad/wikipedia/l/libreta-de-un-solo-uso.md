---
type: Artículo de enciclopedia
title: Libreta de un solo uso
description: "En criptografía, la libreta de uso único, también llamado libreta de un solo uso (del inglés one-time pad), es un tipo de algoritmos de cifrado por el que el texto en claro se combina con una clave aleatoria o «libreta» …"
resource: https://es.wikipedia.org/wiki/Libreta_de_un_solo_uso
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Libreta_de_un_solo_uso"}
license: CC BY-SA 4.0
id: eswiki-Libreta_de_un_solo_uso
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Libreta de un solo uso

En criptografía, la **libreta de uso único**, también llamado **libreta de un solo uso** (del inglés *one-time pad*), es un tipo de  algoritmos de cifrado por el que el texto en claro se combina con una clave aleatoria o «libreta» igual de larga que el texto en claro y que sólo se utiliza una vez. Fue inventado en 1917. Si la clave es verdaderamente aleatoria, nunca se reutiliza y, por supuesto, se mantiene en secreto, se puede demostrar que el método de la libreta de uso único es indescifrable. Uno de sus sinónimos puede ser **cuaderno**.

La parte del nombre relativa a la «libreta» procede de las implementaciones iniciales en las que la clave se distribuía en forma de libreta de papel, de manera que la página podía romperse y destruirse tras su uso. Para facilitar la ocultación, a veces la libreta era físicamente muy pequeña.

El **cifrado de Vernam** pertenece a este tipo de cifrado, de hecho ambos fueron creados por la misma persona, Gilbert Vernam. El sistema de Vernam era un cifrado que combinaba un mensaje con una clave que se leía de un bucle de cinta de papel. En su forma original, el sistema de Vernam no era irrompible porque la clave se podía reutilizar. El uso único vino un poco después, cuando Joseph Mauborgne reconoció que si la cinta de la clave era completamente aleatoria, se incrementaría la dificultad criptoanalítica. Algunos autores emplean el término «cifrado de Vernam» como sinónimo de «libreta de uso único», mientras que otros lo utilizan para cualquier cifrado de flujo aditivo, incluyendo los basados en un generador de números pseudoaleatorios criptográficamente seguro; abajo lo usaremos en este último sentido.

 Secreto
Al principio se reconocía que la libreta de uso único de Vernam-Mauborgne era muy difícil de romper, pero su estatus especial fue descubierto por Claude Shannon unos 25 años después. Usando elementos de la teoría de la información, demostró que la libreta de uso único tenía una propiedad que él llamó *secreto perfecto*: esto es, el texto cifrado no proporciona absolutamente ninguna información acerca del texto en claro. Por tanto, la probabilidad *a priori* de un mensaje en claro *M* es igual que la probabilidad *a posteriori* de un mensaje en claro *M* dado el correspondiente texto cifrado. Y de hecho todos los textos en claro son igualmente probables. Esto es una poderosa noción de dificultad criptoanalítica.

A pesar de la demostración de Shannon, la libreta de uso único tiene en la práctica serias desventajas:

 requiere libretas de un solo uso perfectamente aleatorias
 la generación e intercambio de las libretas de uso único tiene que ser segura, y la libreta tiene que ser al menos tan larga como el mensaje
 hace falta un tratamiento cuidadoso para asegurarse de que siempre permanecerán en secreto para cualquier adversario, y es necesario deshacerse de ellas correctamente para evitar cualquier reutilización parcial o completa —de ahí el «uso único».

Estas dificultades de implementación han provocado casos en los que se han roto algunos sistemas de libreta de uso único, y son tan serios que han evitado que la libreta de uso único haya sido adoptada como una herramienta generalizada de seguridad informática.

En particular, el uso único es absolutamente necesario. Si una libreta de un solo uso se utiliza tan sólo dos veces, unas sencillas operaciones matemáticas pueden reducirla a un cifrado de clave corrida. Si ambos textos en claro están en lenguaje natural (por ejemplo, en inglés o en ruso), aunque ambos sean secretos, hay muchas posibilidades de que sean recuperados con criptoanálisis, posiblemente con algunas ambigüedades. Por supuesto, del mensaje más largo de los dos sólo se podrá recuperar la parte que solape con el mensaje más corto, además, quizás, de un poco más completando una palabra o frase. La explotación más famosa de esta vulnerabilidad es el proyecto VENONA.

La libreta de uso único no proporciona ningún mecanismo para asegurar la integridad del mensaje, y en teoría un atacante en el medio que conozca el mensaje exacto que se está enviando podría sustituir fácilmente parte o todo el mensaje con un texto de su elección que sea de la misma longitud. Se pueden usar las técnicas estándar para evitar esto, como un código de autentificación de mensaje, pero carecen de la prueba de seguridad de la que gozan las libretas de uso único.

 Historia
 Desarrollo técnico
La historia de la libreta de uso único está marcada por cuatro descubrimientos separados pero muy relacionados.

El primer sistema de libreta de uso único era eléctrico. En 1917, Gilbert Vernam (de AT&T) inventó y posteriormente patentó un cifrado basado en la tecnología de teletipo. Cada carácter del mensaje se combinaba eléctricamente con un carácter de una clave en cinta de papel. El capitán Joseph Mauborgne (más tarde capitán del ejército de los Estados Unidos y después jefe del Signal Corps) se dio cuenta de que la secuencia de la clave podía ser completamente aleatoria y que, en tal caso, el criptoanálisis sería más difícil. Juntos inventaron el primer sistema de cinta de un solo uso.

El segundo desarrollo fue el sistema de libreta de papel. Los diplomáticos llevaban mucho tiempo usando códigos y cifrados para la confidencialidad y para minimizar los gastos en telégrafo. En el caso de los códigos, las palabras y las frases se convertían en grupos de números (normalmente 4 o 5 dígitos) utilizando un libro de códigos de tipo diccionario. Para más seguridad, podían combinarse números secretos (normalmente con suma modular) con cada grupo codificado antes de la transmisión, y los números secretos se cambiaban periódicamente (esto se llamaba supercifrado). A principio de los años 20, tres criptógrafos alemanes, Werner Kunze, Rudolf Schauffler y Erich Langlotz, que se dedicaban a romper sistemas así, se dieron cuenta de que nunca podrían romperse si se usaba un número aditivo separado, escogido al azar, para cada grupo codificado. Tenían libretas de papel duplicadas con líneas de grupos de números aleatorios. Cada página tenía un número de serie y ocho líneas. Cada línea tenía seis números de 5 dígitos. Una página se usaba como hoja de trabajo para codificar un mensaje y luego se destruía. El número de serie de la página se enviaba con el mensaje codificado. El destinatario haría el procedimiento a la inversa y luego destruiría su copia de la página. El Ministerio de Asuntos Exteriores alemán puso en funcionamiento este sistema en 1923.

 Ejemplo
Supongamos que Alicia quiere enviarle el mensaje 'HOLA' a Bernardo. Supongamos también que previamente, de alguna manera, se han producido dos libretas de papel que contienen idénticas secuencias de letras aleatorias y que se han enviado por vía segura a ambos. Alicia elige la página apropiada sin utilizar de la libreta.

Normalmente la manera de hacer esto se decide *a priori*, por ejemplo «usar la hoja número 12 el Día del Trabajador», o «usar la siguiente hoja disponible para el siguiente mensaje». El material de la hoja seleccionada es la *clave* para este mensaje. Todas las letras de la libreta se combinarán de una forma predeterminada con una letra del mensaje. Es común, aunque no obligatorio, asignar a cada letra un valor numérico: por ejemplo, «A» es 0, «B» es 1, y así hasta la «Z», que es 26.

En este ejemplo, la técnica es combinar la clave y el mensaje usando la suma modular. Se hace la suma módulo 27 (si se contabiliza la A como 0, siendo por tanto Z=26) de los valores numéricos de las letras correspondientes al mensaje y la clave. Si la clave empieza por:

 X M C K

y el mensaje es «HOLA», entonces el cifrado se haría de la siguiente manera:

   24 (X)  12 (M)   2 (C)  10 (K) clave
 +  7 (H)  15 (O)  11 (L)   0 (A) mensaje
 = 31      27      13      10     clave + mensaje
 =  4 (E)   0 (A)  13 (N)  10 (K) Resultado (mod 27) = texto cifrado

Nótese que cuando el número es mayor que 26, entonces, por aritmética modular, el valor resultante queda truncado.

El texto cifrado que habría que enviarle a Bernardo sería entonces «EANK». Para obtener el texto en claro, Bernardo utiliza la página clave correspondiente y realiza el mismo proceso, pero a la inversa. Ahora, la clave es *restada* del texto cifrado, de nuevo usando aritmética modular:

    27      27      27      27     valor 27
 +   4 (E)   0 (A)  13 (N)  10 (K) texto cifrado
 -  24 (X)  12 (M)   2 (C)  10 (K) clave
 =   7      15      38      27     27 + texto cifrado - clave
 =   7 (H)  15 (O)  11 (L)   0 (A) resultado (mod 27) = texto descifrado

Nótese que a todo valor se le suma previamente 27, y al final se aplica igualmente el módulo 27.

Así, Bernardo recupera el texto en claro de Alicia, el mensaje vital «HOLA». Tanto Alicia como Bernardo destruyen la hoja con la clave inmediatamente después de su uso, previniendo así su reutilización y un ataque contra el cifrado que sería trivial en esencia. La KGB enviaba con frecuencia a sus agentes libretas de uso único impresas en minúsculas hojas de «papel flash» —papel convertido químicamente en nitrocelulosa, que arde casi instantáneamente y no deja cenizas.

La libreta de un solo uso clásica del espionaje (que solía consistir en verdaderas libretas de papel -a menudo minúsculas para su fácil ocultación-, un lápiz afilado y el uso de algún cálculo mental) se puede implementar en forma de software usando ficheros de datos como entrada (texto en claro), salida (texto cifrado) y clave (la secuencia aleatoria requerida).

A menudo se utiliza la operación XOR para combinar el texto en claro con la clave, y es especialmente atractiva en computación, ya que normalmente es una instrucción máquina nativa y por tanto es muy rápida. Sin embargo, no es trivial asegurar que la clave es realmente aleatoria, que sólo se utiliza una vez, que nunca acaba en manos de adversarios y que queda completamente destruida tras su empleo. Las partes auxiliares de una implementación de la libreta de uso único por software presentan verdaderos desafíos: el manejo/transmisión seguro del texto en claro, claves verdaderamente aleatorias y el uso único de la clave.

 Seguridad
Las libretas de uso único son seguras desde el punto de vista de la teoría de la información, en el sentido de que el mensaje cifrado no le proporciona a un criptoanalista ninguna información sobre el mensaje original. Esto es una poderosa noción de seguridad, desarrollada por primera vez durante la Segunda Guerra Mundial por Claude Shannon y demostrada matemáticamente por Shannon en la misma época. Sus resultados fueron publicados en el *Bell Labs Technical Journal* en 1949. Las libretas de uso único, utilizadas adecuadamente, son seguras en este sentido incluso contra adversarios con poder computacional infinito. Para seguir con el ejemplo de arriba, supongamos que Eva intercepta el texto cifrado de Alicia: «EANK». Si Eva dispusiera de una potencia computacional infinita, hallaría rápidamente que la clave «XMCK» produciría el texto en claro «HOLA», pero también hallaría que la clave «FCJR» produciría el texto en claro «ZYES», un mensaje igualmente plausible:
    27      27      27      27     valor 27
 +   4 (E)   0 (A)  13 (N)  10 (K) texto cifrado
 −   5 (F)   2 (C)   9 (J)  18 (R) posible clave
 =  26      25      31      19     27 + texto cifrado - posible clave
 =  26 (Z)  25 (Y)   4 (E)  19 (S) resultado (mod 27) = posible texto descifrado
De hecho, es posible «descifrar» cualquier mensaje con el mismo número de caracteres a partir del texto cifrado simplemente usando una clave diferente, y no existe ninguna información en el texto cifrado que le permita a Eva escoger entre las posibles lecturas del texto cifrado.

La mayoría de los algoritmos de cifrado convencionales, tanto simétricos como asimétricos, utilizan patrones complejos de sustitución y trasposición. En el caso del mejor algoritmo que se usa en la actualidad, no se sabe si existe un procedimiento criptoanalítico que pueda revertir (o revertir parcialmente) esas transformaciones sin conocer la clave utilizada durante el cifrado.

En términos prácticos, para el mejor de ellos no se conoce un procedimiento así, aunque puede que existan algoritmos computacionales que puedan hacerlo en un tiempo 'razonable'. Uno de los principales problemas sin resolver en teoría de la computabilidad está relacionado con este problema; si P=NP, entonces sería al menos posible que se puedan hallar algoritmos así, y seguramente se buscarían con más ahínco que hoy en día. Y aunque se demuestre que no, algunos criptosistemas actuales todavía podrían romperse. Sin embargo, la libreta de uso único no sería menos segura si se demostrara que P=NP. En la actualidad se cree que P≠NP, y por tanto es dudoso que esta cuestión tenga relevancia práctica para el criptoanálisis o para el diseño de algoritmos de cifrado.

 Ataques
Aunque las libretas de uso único son demostrablemente seguras si se generan y utilizan adecuadamente, un pequeño error puede posibilitar un criptoanálisis exitoso:

 En 1944–1945, la Signal Security Agency del ejército de EE. UU. consiguió resolver un sistema de libreta de uso único utilizado por el Ministerio de Asuntos Exteriores alemán para su tráfico de alto nivel, de nombre en clave GEE (Erskine, 2001). El GEE era inseguro porque las libretas no eran completamente aleatorias — la máquina empleada para generar las libretas producía una salida predecible.

 En 1945, EE. UU. descubrió que los mensajes Canberra-Moscú se estaban cifrando primero mediante un libro de códigos y luego a base de una libreta de uso único. Sin embargo, la libreta de uso único era la misma que utilizaba Moscú para los mensajes Washington D. C.-Moscú. Combinado con el hecho de que algunos mensajes Canberra-Moscú incluían documentos gubernamentales británicos que eran conocidos, esto permitió que se rompieran algunos de los mensajes cifrados.

 Las agencias de espionaje soviéticas empleaban libretas de uso único para asegurar las comunicaciones con los agentes y los controladores de los agentes. El análisis demostró que estas libretas las generaban personas utilizando máquinas de escribir. Este método, por supuesto, no es «verdaderamente» aleatorio, ya que implica que ciertas secuencias de teclas convenientes sean más probables que otras, aunque demostró ser efectivo en general. Sin copias de las claves usadas, sólo ofrecían esperanzas de criptoanálisis algunos defectos en el método de generación o la reutilización de las claves. A principios de los 40, la inteligencia estadounidense y británica consiguió romper parte del tráfico de libreta de uso único hacia Moscú durante la Segunda Guerra Mundial, como resultado de ciertos errores cometidos al generar y distribuir las claves.

 Requisitos para una verdadera aleatoriedad
Para explicar la libreta de uso único es necesario distinguir entre dos nociones de seguridad. La primera es la seguridad teórica del sistema de libreta de uso único demostrada por Shannon. La segunda es la seguridad ofrecida por los cifrados más punteros (por ejemplo, el AES) diseñados con los principios aprendidos durante la larga historia de la rotura de códigos y sujetos al testeo intensivo en un proceso de estandarización, bien en público o por un servicio de seguridad de primera clase (**seguridad empírica**). La primera está demostrada matemáticamente y está sujeta a la disponibilidad práctica de los números aleatorios. La segunda no está demostrada pero recibe la confianza de la mayoría de los gobiernos para proteger sus secretos más vitales.

 Métodos que pueden ofrecer seguridad empírica pero no tienen seguridad de Shannon
Si la clave la genera un programa determinista, entonces no es aleatoria ni se puede afirmar que el sistema de cifrado ofrezca la seguridad teórica de la libreta de uso único. Se llama cifrado de flujo. Generalmente estos utilizan una clave pequeña que se usa como semilla para un flujo pseudoaleatorio largo, que luego se combina con el mensaje empleando algún mecanismo como los de la libreta de uso único (por ejemplo, XOR). Los cifrados en flujo pueden ser seguros en la práctica, pero no pueden ser absolutamente seguros en el mismo sentido demostrable de la libreta de uso único.

Los cifrados Fish usados por el ejército alemán en la Segunda Guerra Mundial resultaron ser cifrados en flujo inseguros, no útiles libretas de uso único automatizadas como pretendían sus diseñadores. Bletchley Park rompía uno de ellos regularmente, la máquina de cifrado de Lorenz.

Sin embargo, si se utiliza un famoso generador de números pseudoaleatorios criptográficamente seguro moderno, puede formar la base de un cifrado en flujo empíricamente seguro. Hay muchos diseños bien probados en el dominio público, que varían desde la simplicidad del RC4 al uso de un cifrado en bloque como el AES en modo contador. Parecería que hay pocos motivos para inventar nuevos cifrados en flujo, pero se piensa desde hace tiempo que la NSA y las agencias similares emplean un esfuerzo considerable en los cifrados en flujo para sus clientes gubernamentales.

 Métodos que no ofrecen seguridad empírica ni seguridad de Shannon
La similitud entre los cifrados en flujo y las libretas de uso único lleva a menudo a que los criptográficamente incautos inventen cifrados en flujo inseguros bajo la creencia falsa de haber desarrollado una versión práctica de la libreta de uso único. Una versión especialmente insegura son los generadores de números aleatorios que se distribuyen en muchos (quizás la mayoría) de las bibliotecas accesorias de los lenguajes de programación o en forma de llamadas al sistema operativo. Normalmente producen secuencias que pasan alguna (o muchas) pruebas estadísticas, pero sin embargo son rompibles por técnicas criptoanalíticas. Durante un tiempo, el ANSI C estándar restringía la salida de la rutina de números aleatorios del lenguaje C a un entero de precisión simple, 16 bits para la mayoría de las implementaciones, dando 32768 valores distintos antes de repetirse. Esto es completamente inseguro y fácilmente rompible por fuerza bruta (para situarnos, basta saber que una computadora de 1 GHz que tarde 10 000 ciclos de reloj en comprobar un offset del ciclo RNG (un número ridículamente grande) tardaría menos de un tercio de segundo en comprobar todos los offsets posibles). Los generadores de números aleatorios estándar no sirven para propósitos criptográficos, concretamente para la libreta de uso único. En particular, el relativamente reciente algoritmo tornado de Mersenne, admirado ampliamente, aunque es lo bastante «aleatorio» para la mayoría de los usos de simulación o investigación, mejor que la mayoría de los generadores de su mismo tipo, y también bastante rápido, no debe utilizarse para generar claves de libreta de un solo uso. El algoritmo es determinista y no fue diseñado para la seguridad criptográfica.

Además, los valores conocidos públicamente como los dígitos finales de los tiempos de las carreras de maratón, los precios de cierre de valores de bolsa, por muy poco conocidos que sean, las temperaturas o presiones atmosféricas diarias, etc., aunque aparentemente aleatorios, son predecibles —después de que se produzca el hecho. De hecho, tampoco pueden usarse secuencias verdaderamente aleatorias que hayan sido publicadas, ya que si se identifican son predecibles. Un ejemplo es la publicación de una tabla de un millón de números aleatorios por la Rand Corp en 1950; ha pasado todos los tests estadísticos de aleatoriedad hasta ahora, y se cree que es verdaderamente aleatoria. Pero, al haberse publicado, es completamente predecible. También lo son los dígitos de pi, e, fi y otros números irracionales o trascendentales; puede que las secuencias sean aleatorias (una cuestión abierta, en realidad), pero son completamente predecibles.

 Conseguir la seguridad de Shannon
Para conseguir la seguridad de Shannon se necesita una fuente de datos aleatorios perfectamente impredecibles. Una base teórica para la existencia física de la impredecibilidad es la mecánica cuántica. Sus afirmaciones de impredecibilidad están sujetas a la comprobación experimental. *Ver:* Experimentos de Bell. Otra base es la teoría de los sistemas dinámicos inestables y la teoría del caos. Estas teorías sugieren que incluso en el mundo determinista de la mecánica newtoniana, los sistemas reales evolucionan de maneras que no se pueden predecir en la práctica porque haría falta conocer las condiciones iniciales con una precisión que crece exponencialmente con el tiempo.

Para que se puedan usar en una libreta de uso único, los datos deben mostrar una aleatoriedad perfecta. En la práctica, la mayoría de las fuentes muestran alguna imperfección o desviación. La calidad de la aleatoriedad se mide por entropía. Un bit perfectamente aleatorio tiene una entropía uno. Una idea procedente de Von Neumann es utilizar un algoritmo para combinar varios bits aleatoriamente imperfectos, con una entropía menor que uno, para producir un bit con entropía igual a uno. Este proceso se llama **destilación de entropía** o **blanqueamiento de Von Neumann**, y permite generar en la práctica datos aleatorios adecuados para su uso en una libreta de uso único. El blanqueamiento de Von Neumann consiste en lo siguiente:

En Linux (y otros sistemas tipo Unix), el generador de números aleatorios del kernel, /dev/random, utiliza el ruido ambiental para generar datos aleatorios y es mejor que muchos diseños basados en llamadas al sistema. Intenta estimar la cantidad de entropía que recoge y se bloquea si el fondo de entropía se agota. Pretende ser, y se piensa que realmente es, mejor que muchos generadores parecidos, y si es así, está muy cerca de ser satisfactoriamente aleatorio. Pero este proceso es lento en sistemas que tienen pocas fuentes de ruido utilizables. Sin embargo, puede alimentarse con entropía adicional leyendo de un dispositivo generador de ruido.

Linux también proporciona /dev/urandom, que emplea un algoritmo determinista para generar los datos cuando no hay ruido ambiental disponible. Existen diseños mejorados, como el algoritmo de Yarrow. Las claves de libreta de uso único generadas con este método (es decir, con generadores de números aleatorios deterministas) carecen de la seguridad teórica de una libreta de uso único. Yarrow ofrece al menos tanta fuerza como un cifrado en bloque basado en el Triple DES.

Si una computadora que se utiliza para generar libretas de uso único queda comprometida por un virus informático u otros malwares, o por un adversario que consiga acceso físico, el software puede ser modificado para que transmita los datos o genere datos aparentemente aleatorios que en realidad son predecibles. Una forma de reducir este riesgo es generar libretas en una máquina que nunca esté conectada a una red informática y que preferiblemente no se utilice para ninguna otra tarea. Si se recogen los datos en dispositivos de almacenamiento nuevos y vírgenes (por ejemplo, un disquete o un CD-R), se elimina otra fuente de infección de malware. Si se van a producir libretas de papel, es mejor que la impresora también sea dedicada. Una opción puede ser emplear un ordenador portátil antiguo para generar las libretas, borrado y reinstalado con una copia confiable de un sistema operativo de código abierto, como Linux o BSD. Su pequeño tamaño permitiría guardarlo fácilmente en una caja fuerte cuando no esté en funcionamiento.

 Referencias
