---
type: Artículo de enciclopedia
title: Enigma (máquina)
description: Enigma fue una máquina de rotores diseñada para cifrar y descifrar mensajes.
resource: https://es.wikipedia.org/wiki/Enigma_(máquina)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Enigma_(máquina)"}
license: CC BY-SA 4.0
id: eswiki-Enigma_(máquina)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Enigma (máquina)

**Enigma** fue una máquina de rotores diseñada para cifrar y descifrar mensajes. Patentada en 1918 por la empresa alemana Scherbius y Ritter, y construida e inventada por Arthur Scherbius, quien luego compró un patente para un aparato similar del inventor neerlandés Hugo Koch, se puso a la venta en 1923 para un uso comercial. En 1926, la Armada alemana la adoptó para uso militar y poco después su uso se extendió a las demás fuerzas armadas alemanas, especialmente durante la Segunda Guerra Mundial.

Su facilidad de manejo y su aparente robustez criptográfica fueron las principales razones para su implantación. Los alemanes confiaban tanto en su encriptado con más de 150 billones de combinaciones posibles que garantizaban la seguridad en las comunicaciones que la consideraron segura, pensamiento que compartía el mismo Karl Dönitz.

Sin embargo, gracias a las investigaciones llevadas a cabo por los servicios de inteligencia polacos, quienes instruyeron a su vez a los servicios franceses e ingleses en el sistema de cifrado, este fue finalmente descubierto, lo que precipitó el desenlace de la Segunda Guerra Mundial en favor de los Aliados. Estos aprovecharon además los fallos en los procedimientos de uso por parte de los operadores alemanes, que permitieron la interceptación de las tablas de descifrado y la captura de algunos aparatos.

La máquina equivalente británica, el Bombe, y varias estadounidenses, como la SIGABA (o M-135-C en el ejército), eran similares a Enigma. La primera máquina moderna de cifrado rotatorio, de Edward Hebern, era considerablemente menos segura que Enigma.

 Máquina

 Funcionamiento

La máquina Enigma fue un dispositivo electromecánico, lo que significa que usaba una combinación de partes mecánicas y eléctricas. El mecanismo estaba constituido fundamentalmente por un teclado similar al de las máquinas de escribir cuyas teclas eran interruptores eléctricos, un engranaje mecánico y un panel de luces con las letras del alfabeto.

La parte eléctrica consistía en una batería que encendía una lámpara de una serie de ellas, que representaban cada una de las diferentes letras del alfabeto. Se puede observar en la parte inferior de la imagen adjunta el teclado, y las lámparas son los circulitos que aparecen encima de aquel.

El corazón de la máquina Enigma era mecánico y constaba de varios rotores conectados entre sí. Cada rotor es un disco circular plano con 26 contactos eléctricos en cada cara, uno por cada letra del alfabeto. Cada contacto de una cara está conectado o cableado a un contacto diferente de la cara contraria. Por ejemplo, en un rotor en particular, el contacto número 1 de una cara puede estar conectado con el contacto número 14 en la otra cara y el contacto número 5 de una cara con el número 22 de la otra. Cada uno de los cinco rotores proporcionados con la máquina Enigma estaba cableado de una forma diferente y los rotores utilizados por el ejército alemán poseían un cableado distinto al de los modelos comerciales.

Dentro de la máquina había, en la mayoría de las versiones, tres ranuras para alojar los rotores. Cada uno de los rotores se encajaba en la ranura correspondiente de forma que sus contactos de salida se conectaban con los contactos de entrada del rotor siguiente. El tercer y último rotor se conectaba, en la mayoría de los casos, a un reflector que conectaba el contacto de salida del tercer rotor con otro contacto del mismo rotor para realizar el mismo proceso pero en sentido contrario y por una ruta diferente. La existencia del reflector diferencia la máquina Enigma de otras máquinas de cifrado de la época basadas en rotores. Este elemento, que no se incluía en las primeras versiones de la máquina, posibilitaba que la clave utilizada para el cifrado se pudiera emplear en el descifrado del mensaje. Se pueden observar en la parte superior de la imagen los tres rotores con sus correspondientes protuberancias dentadas que permitían girarlos a mano, colocándolos en una posición determinada.

Cuando se pulsaba una tecla en el teclado, por ejemplo la correspondiente a la letra A, la corriente eléctrica procedente de la batería se dirigía hasta el contacto correspondiente a la letra A del primer rotor. La corriente atravesaba el cableado interno del primer rotor y se situaba, por ejemplo, en el contacto correspondiente a la letra J en el lado contrario. Supongamos que este contacto del primer rotor estaba alineado con el contacto correspondiente a la letra X del segundo rotor. La corriente llegaba al segundo rotor y seguía su camino a través del segundo y tercer rotor, el reflector y de nuevo a través de los tres rotores en el camino de vuelta. Al final del trayecto, la salida del primer rotor se conectaba a la lámpara correspondiente a una letra, distinta de la A, en el panel de luces. El mensaje de cifrado se obtenía por tanto sustituyendo las letras del texto original por las proporcionadas por la máquina.

Cada vez que se introducía una letra del mensaje original, pulsando la tecla correspondiente en el teclado, la posición de los rotores variaba. Debido a esta variación, a dos letras idénticas en el mensaje original, por ejemplo AA, les correspondían dos letras diferentes en el mensaje cifrado, por ejemplo QL. En la mayoría de las versiones de la máquina, el primer rotor avanzaba una posición con cada letra. Cuando se habían introducido 26 letras y por tanto el primer rotor había completado una vuelta completa, se avanzaba en una muesca la posición del segundo rotor, y cuando este terminaba su vuelta, se variaba la posición del tercer rotor. El número de pasos que provocaba el avance de cada uno de los rotores era un parámetro configurable por el operario.

Debido a que el cableado de cada rotor era diferente, la secuencia exacta de los alfabetos de sustitución variaba en función de qué rotores estaban instalados en las ranuras (cada máquina disponía de cinco), su orden de instalación y la posición inicial de cada uno. A estos datos se les conocía con el nombre de configuración inicial, y eran distribuidos, mensualmente al principio y con mayor frecuencia a medida que avanzaba la guerra, en libros a los usuarios de las máquinas.

El funcionamiento de las versiones más comunes de la máquina Enigma era simétrico en el sentido de que el proceso de descifrado era análogo al proceso de cifrado. Para obtener el mensaje original solo había que introducir las letras del mensaje cifrado en la máquina, y esta devolvía una a una las letras del mensaje original, siempre y cuando la configuración inicial de la máquina fuera idéntica a la utilizada al cifrar la información.

 Criptoanálisis básico

Los cifrados, por supuesto, pueden ser descifrados, y la forma más efectiva de enfocarlo depende del método de cifrado. Al principio de la Primera Guerra Mundial, los departamentos de descifrado eran lo bastante avanzados como para poder descubrir la mayoría de los cifrados, si se dedicaban suficientes esfuerzos. Sin embargo, la mayoría de estas técnicas se basaban en conseguir cantidades suficientes de texto cifrado con una clave particular. A partir de estos textos, con suficiente análisis estadístico, se podían reconocer patrones y deducir la clave.

Los analistas buscan normalmente algunas letras y combinaciones frecuentes. Por ejemplo, en inglés, E, T, A, O, I, N y S son generalmente fáciles de identificar, por ser muy frecuentes (véase ETAOIN SHRDLU y EAOSR NIDLC en análisis de frecuencias); también NG, ST y otras combinaciones, muy frecuentes en inglés. Una vez que se identifican algunos (o todos) de estos elementos, el mensaje se descifra parcialmente, revelando más información sobre otras sustituciones probables. El análisis de frecuencia simple confía en que una letra es sustituida siempre por otra letra del texto original en el texto cifrado; si este no es el caso, la situación es más difícil.

Durante mucho tiempo, los criptógrafos procuraron ocultar las frecuencias usando varias sustituciones diferentes para las letras comunes, pero esto no puede ocultar completamente los patrones en las sustituciones para las letras del texto original. Tales códigos fueron utilizados extensamente hacia el año 1500.

Una técnica para hacer más difícil el análisis de frecuencia es utilizar una sustitución diferente para cada letra, no sólo las comunes. Este proceso sería normalmente muy costoso en tiempo y requería que ambas partes intercambiaran sus patrones de sustitución antes de enviar mensajes cifrados. A mitad del , una nueva técnica fue inventada por Alberti, ahora conocida generalmente como *cifrado polialfabético*, que proporcionó una técnica simple para crear una multiplicidad de patrones de sustitución. Las dos partes intercambiarían una cantidad de información pequeña (referida como la clave) y seguirían una técnica simple que produce muchos alfabetos de sustitución, y muchas sustituciones diferentes para cada letra del texto original. La idea es sencilla y eficaz, pero resultó ser más difícil de lo esperado. Muchos cifrados fueron implantaciones parciales del concepto, y eran más fáciles de romperse que los anteriores (p. ej. el cifrado de Vigenère).

Costó centenares de años hallar métodos fiables para romper los cifrados polialfabéticos. Las nuevas técnicas confiaron en estadística (p. ej. análisis de frecuencias) para descubrir información sobre la clave usada para un mensaje. Estas técnicas buscan la repetición de los patrones en el texto cifrado, que proporcionarían pistas sobre la longitud de la clave. Una vez que se sabe esto, el mensaje, esencialmente, se convierte en una serie de mensajes, cada uno con la longitud de la clave, a los cuales se puede aplicar el análisis de frecuencia normal. Charles Babbage, Friedrich Kasiski y William F. Friedman están entre los que aportaron la mayor parte del trabajo para desarrollar estas técnicas.

Se recomendó a los usuarios de los cifrados emplear no sólo una sustitución diferente para cada letra, sino también una clave muy larga, de manera que las nuevas técnicas de descifrado fallaran (o que por lo menos fueran mucho más complicadas). Sin embargo, esto es muy difícil de lograr; llevar a las partes que intercambian mensajes una clave larga requiere más tiempo, y los errores son más probables. El cifrado ideal de esta clase sería uno en el que una clave tan larga se pudiese generar de un patrón simple, produciendo un cifrado en que hay tantos alfabetos de substitución que la cuenta de ocurrencias y los ataques estadísticos fueran imposibles.

El uso de rotores múltiples en Enigma brindó un modo simple de determinar qué alfabeto de sustitución usar para un mensaje en particular (en el proceso de cifrado) y para un texto cifrado (en el de descifrado). A este respecto fue similar al cifrado polialfabético. Sin embargo, a diferencia de la mayoría de las variantes del sistema polialfabético, Enigma no tenía una longitud de clave obvia, debido a que los rotores generaban una nueva sustitución alfabética en cada pulsación, y toda la secuencia de alfabetos de sustitución podía cambiarse haciendo girar uno o más rotores, cambiando el orden de los rotores, etc., antes de comenzar una nueva codificación. En el sentido más simple, Enigma tuvo un repertorio de 26x26x26 = 17576 alfabetos de sustitución para cualquier combinación y orden de rotores dada. Mientras el mensaje original no fuera de más de 17576 pulsaciones, no habría un uso repetido de un alfabeto de sustitución. Pero las máquinas Enigma agregaron otras posibilidades. La secuencia de los alfabetos utilizados era diferente si los rotores eran colocados en la posición ABC, en comparación con ACB; había un anillo que rotaba en cada rotor que se podría fijar en una posición diferente, y la posición inicial de cada rotor era también variable. Y la mayoría de las Enigmas de uso militar añadieron un *stecker* (tablero de interconexión) que cambió varias asignaciones de clave (ocho o más, dependiendo del modelo). Así pues, esta clave se puede comunicar fácilmente a otro usuario. Son apenas algunos valores simples: rotores que utilizar, orden del rotor, posiciones de los anillos, posición inicial y ajustes del tablero de interconexión.

 El método de cifrado

Por supuesto, si la configuración estuviera disponible, un criptoanalista podría simplemente poner un equipo Enigma con la misma configuración y descifrar el mensaje. Uno podría mandar libros de configuración que usar, pero podrían interceptarse. En cambio, los alemanes establecieron un sistema astuto que mezcló los dos diseños.

Al principio de cada mes, se daba a los operadores de la Enigma un nuevo libro que contenía las configuraciones iniciales para la máquina. Por ejemplo, en un día particular las configuraciones podrían ser poner el rotor n.º 1 en la hendidura 7, el n.º 2 en la 4 y el n.º 3 en la 6. Están entonces rotados, para que la hendidura 1 esté en la letra X, la hendidura 2 en la letra J y la hendidura 3 en la A. Como los rotores podían permutarse en la máquina, con tres rotores en tres hendiduras se obtienen otras 3x2x1 = 6 combinaciones para considerar, para dar un total de 105456 posibles alfabetos.

A estas alturas, el operador seleccionaría algunas otras configuraciones para los rotores, esta vez definiendo sólo las posiciones o «giros» de los rotores. Un operador en particular podría seleccionar ABC, y éstos se convierten en la configuración del «mensaje para esa sesión de cifrado». Entonces teclearon la configuración del mensaje en la máquina que aún estaba con la configuración inicial. Los alemanes, creyendo que le otorgaban más seguridad al proceso, lo tecleaban dos veces, pero esto se desveló como una de las brechas de seguridad con la que «romper» el secreto de Enigma. Los resultados serían codificados para que la secuencia ABC tecleada dos veces pudiera convertirse en XHTLOA. El operador entonces gira los rotores a la configuración del mensaje, ABC. Entonces se teclea el resto del mensaje y lo envía por la radio.

En el extremo receptor, el funcionamiento se invierte. El operador pone la máquina en la configuración inicial e introduce las primeras seis letras del mensaje. Al hacer esto él verá ABCABC en la máquina. Entonces gira los rotores a ABC e introduce el resto del mensaje cifrado, descifrándolo.

Este sistema era excelente porque el criptoanálisis se basa en algún tipo de análisis de frecuencias. Aunque se enviaran muchos mensajes cualquier día con seis letras a partir de la configuración inicial, se asumía que esas letras eran al azar. Mientras que un ataque en el propio cifrado era posible, en cada mensaje se usó un cifrado diferente, lo que hizo que el análisis de frecuencia fuera inútil en la práctica.

La Enigma fue muy segura. Tanto que los alemanes confiaron mucho en ella. El tráfico cifrado con Enigma incluyó de todo, desde mensajes de alto nivel sobre las tácticas y planes, a trivialidades como informes del tiempo e incluso las felicitaciones de cumpleaños.

 Ejemplo de cifrado

El siguiente es un mensaje auténtico enviado el 7 de julio de 1941 por la División SS-Totenkopf sobre la campaña contra Rusia, en la Operación Barbarroja. El mensaje (enviado en dos partes) fue descifrado por Geoff Sullivan y Frode Weierud, dos miembros del Crypto Simulation Group (CSG).

El mensaje fue cifrado para el modelo de tres rotores con el reflector B (habrá que usar el mismo modelo para descifrarlo, o uno compatible). Para descifrar el mensaje, primero hay que configurar la máquina con la información diaria especificada en los libros de códigos alemanes para ese mes. Para el 7 de julio de 1941 era:

El operador de la máquina debía colocar esa configuración antes de enviar o recibir el primer mensaje del día. Cogería los rotores (*Walzenlage*) 2, 4 y 5 (en ese orden), y movería el anillo de cada rotor a las posiciones 2, 21 y 12 respectivamente, como se indica en *Ringstellung* (a veces la configuración se puede ver en las letras correspondientes a la posición del anillo; en este caso serían B U L), y los insertaría en la máquina. También debía colocar los cables conectores uniendo en la parte baja de la máquina las posiciones que se indican en *Steckerverbindungen*, uniendo A con V, B con S, C con G, etc. Esta configuración se mantendrá en todos los mensajes del día, y con ella ya se pueden empezar a descifrar mensajes.

El mensaje original se envió en dos partes (ya que el tamaño máximo por cada mensaje era de 250 letras). Cada mensaje tiene una cabecera, que se enviaba sin cifrar (y es la única parte del mensaje que podía tener números); en este caso:

En la cabecera se indicaba la hora a la que se mandaba el mensaje (en este caso 1840 representa las 18:40), cuántas partes componían el mensaje (seguido de TLE, de *Teile*) y qué parte era (seguido de TL, de *Teil*) si había más de una, el tamaño del texto cifrado y dos grupos de tres letras (que eran diferentes y aleatorios en cada mensaje). El primer grupo era la configuración inicial y el segundo la clave cifrada del mensaje. El operador moverá los tres rotores a la letra indicada por el primer grupo (W X C), y tecleará el otro grupo, la clave cifrada (K C H), que le dará al operador la clave sin cifrar, en este caso B L A). A continuación pondrá los tres rotores en las posiciones B L A y tecleará el resto del mensaje cifrado, teniendo en cuenta que las cinco primeras letras corresponden al *Kenngruppe*, que indicará quiénes pueden leer el mensaje (en este caso se puede ignorar).

Haciendo el mismo proceso con la otra parte del mensaje, el resultado es:

Uniendo los mensajes, y usando las *X* como espacios (algunos espacios faltan en el mensaje original), y algunas abreviaturas (entre corchetes) queda:

Los nombres propios se ponían dos veces seguidas (por ejemplo, *KURTINOWA*), y algunas combinaciones de letras se sustituían, por ejemplo, CH por Q (en *SIQER*, que es *sicher*), y los números debían escribirse con letras. El texto traducido sería:

 Guerra civil española

Durante la guerra civil española, el bando sublevado dispuso de al menos veinte máquinas *Enigma* que le permitieron al general Franco mantener una comunicación secreta y permanente con sus generales. Las diez primeras fueron vendidas por los nazis al bando sublevado en noviembre de 1936 cuando el avance franquista se detuvo a las puertas de Madrid. Sin embargo, no se trataba del modelo más avanzado (era el D de la gama comercial), ya que a los alemanes les preocupaba que alguna de ellas pudiera caer en manos de los soviéticos, que apoyaban a los republicanos, o de los servicios secretos británicos desplegados en España. El encargado del adiestramiento de los militares que iban a utilizarla fue el comandante Antonio Sarmiento —miembro del Estado Mayor y jefe de la Oficina de Escuchas y Descifrado del Cuartel General del Generalísimo—, quien en un informe redactado en Salamanca en noviembre de 1936 afirmaba: «Para dar una idea del grado de seguridad que se consigue con estas máquinas basta decir que el número de combinaciones posibles de acordar se eleva a la fabulosa cifra de 1 252 962 387 456». A principios de 1937 se compraron diez máquinas más del mismo modelo. Actualmente una de las máquinas forma parte de la colección estable del Museo Histórico Militar de Sevilla. La máquina data de diciembre de 1938, cuando recaló en Sevilla, asignada al Ejército del Sur. Posteriormente, en julio de 1939, pasó al Estado Mayor de la Segunda Región Militar en Sevilla.

La presencia de estas máquinas en ayuda del frente sublevado obligó al gobierno de la República a hacerle frente en la contienda. Siete criptógrafos españoles procedentes del servicio secreto de la República y exiliados en Francia, entre ellos el vallisoletano Antonio Camazón, trabajaron junto con franceses y polacos en el descifrado de los mensajes de la máquina Enigma. Su trabajo fue expuesto en el documental *Equipo D: los códigos olvidados* de Jorge Laplace.

 Segunda Guerra Mundial

 «Rompiendo» Enigma

El esfuerzo que rompió el cifrado alemán empezó en 1928, cuando los polacos interceptaron una máquina Enigma enviada de Berlín a Varsovia y equivocadamente no protegida como equipaje diplomático. No era una versión militar, pero proporcionó una pista de que los alemanes podrían estar utilizando una máquina de tipo Enigma en el futuro. Cuando el ejército alemán comenzó a usar Enigmas modificadas años después, los polacos intentaron «romper el sistema» buscando el cableado de los rotores usados en la versión del ejército y encontrando una manera de recuperar las configuraciones usadas para cada mensaje en particular.

A finales de 1932, el matemático polaco Marian Rejewski logró uno de los mayores descubrimientos significativos en la historia del criptoanálisis usando técnicas fundamentales de matemáticas y estadística al encontrar una manera de combinarlas. Así, logró descifrar el código, pero al no tener acceso a las propias máquinas y su cableado, los investigadores polacos no pudieron descifrar los mensajes encriptados hasta recibir del servicio de inteligencia francés datos de la configuración. Dotados de esta nueva información, los polacos pudieron construir una réplica, a partir de la cual pudieron ya descifrar los mensajes alemanes.

Por ejemplo, digamos que un operador escogió QRS como configuración para el mensaje. Él pondría la máquina con la configuración inicial del día, y entonces escribió QRSQRS. Esto se convertiría en algo como JXDRFT; parece un balbuceo, pero la pista que Rejewski aprovechó fue que el disco se había movido tres posiciones entre los dos juegos de QRS; nosotros sabemos que J y R son originalmente la misma letra y lo mismo para XF y DT. No sabemos qué letras son, ni tampoco tenemos que saberlo, porque mientras hay un número grande de configuraciones del rotor, hay sólo un número pequeño de rotores que tendrán una letra que va de J a R, X a F y D a T. Rejewski llamó a estos modelos *cadenas*.

Encontrar las cadenas apropiadas de las 10545 combinaciones era toda una tarea. Los polacos (particularmente los colegas de Rejewski, Jerzy Rozycki y Henryk Zygalski) desarrollaron un número de métodos de ayuda. Una técnica utilizaba unas tiras en blanco para cada rotor mostrando cuáles letras podrían encadenarse, bloqueando las letras que no podrían encadenarse. Los usuarios tomarían las tiras sobreponiéndolas, buscando las selecciones donde estaban completamente claras las tres letras. Los británicos también habían desarrollado tal técnica cuando tuvieron éxito en romper la Enigma comercial, aunque intentaron (y no lograron) romper las versiones militares de Enigma.

La disposición de estas letras en los rotores creó, por parte del servicio de inteligencia y su jefe del Deuxième Bureau Francés, George Bertrand, grupos denominados por ellas. «Cada equipo tenía una fracción para aumentar el rendimiento» (entre los tres grupos de expertos en criptografía integrados por franceses, polacos y españoles). El «Equipo D» estaba integrado por siete españoles exiliados procedentes del servicio secreto de la República («5 oficiales y dos comisarios políticos», los define) y dirigido por Camazón.

Por supuesto, unos cuantos miles de posibilidades eran aún muchas para probar. Para ayudar con esto, los polacos construyeron máquinas que consistían en «enigmas en paralelo» que llamaron *bomba kryptologiczna* (bomba criptológica). Es posible que el nombre fuera escogido de un tipo de postre helado local, o del tictac que hacían las máquinas cuando generaban las combinaciones; los franceses cambiaron el nombre a *bombe* y los angloparlantes a *bomb* (nada apunta a algo explosivo). Entonces se cargarían juegos de discos posibles en la máquina y podría probarse un mensaje en las configuraciones, uno tras otro. Ahora las posibilidades eran sólo centenares. Esos centenares son un número razonable para atacar a mano.

Los polacos pudieron determinar el cableado de los rotores en uso por aquel entonces por el ejército alemán y, descifrar buena parte del tráfico del Ejército alemán en los años 1930 hasta el principio de la Segunda Guerra Mundial. Recibieron alguna ayuda secreta de los franceses, quienes tenían un agente (Hans Thilo-Schmidt, con nombre código Asch) en Berlín con acceso a las claves programadas para Enigma, manuales, etc. Los hallazgos del criptoanalista Rejewski no dependieron de esa información; no fue siquiera informado sobre el agente francés, ni tuvo acceso a ese material.

Sin embargo, en 1939, al añadir los alemanes dos rotores más a la máquina, y los polacos, conscientes de que la invasión alemana se acercaba e incapaces de extender sus técnicas con los recursos disponibles, decidieron compartir los resultados de sus investigaciones con los aliados franceses y británicos en una reunión secreta acontecida el 26 y 27 de julio de 1939 en la localidad de Pyry, cerca de Varsovia.

Mientras que en el pasado utilizaban solamente tres rotores y los movían simplemente de ranura en ranura, ahora introdujeron dos rotores adicionales, usando así tres de cinco rotores a cualquier hora. Los operadores también dejaron de enviar dos veces las tres letras correspondientes a la configuración individual al principio de cada mensaje, lo que eliminó el método original de ataque.

Todo eso se envió a Francia en valija diplomática; la parte británica fue a Bletchley Park. Hasta entonces, el tráfico militar alemán de Enigma había dado por vencidos tanto a británicos como a franceses, y ellos consideraron la posibilidad de asumir que las comunicaciones alemanas permanecerían en la oscuridad durante toda la guerra.

Casi todo el personal de la sección de criptografía polaca dejó Polonia durante la invasión alemana y la mayoría de ellos terminaron en Francia, trabajando con criptógrafos franceses en transmisiones alemanas. Algunos criptógrafos polacos fueron capturados por los alemanes antes de que salieran de Polonia o en tránsito, pero nada fue revelado sobre el trabajo de Enigma. La labor continuó en Francia, en la «Estación PC Bruno», hasta la caída de este país (y también un poco después). Algunos de los integrantes del equipo franco-polaco escaparon entonces a Inglaterra; ninguno participó en el esfuerzo británico en criptoanálisis contra las redes de Enigma. Cuando el propio Rejewski supo (poco antes de su muerte) del trabajo llevado a cabo en Bletchley Park, que él había empezado en Polonia en 1932, y de su importancia en el curso de la guerra y la victoria aliada, quedó sorprendido.

 Ultra

Con la ayuda polaca en masa, los británicos comenzaron a trabajar en el tráfico alemán de Enigma. A principios de 1939 el servicio secreto británico instaló su escuela gubernamental de códigos y cifrado (GC&CS) en Bletchley Park, 80km al norte de Londres, para quebrar el tráfico de mensajes enemigos si fuera posible. También prepararon una red de interceptación para capturar el tráfico cifrado destinado a los descifradores en Bletchley. Había una gran organización que controlaba la distribución de los resultados, secretos, de información descifrada. Se establecieron reglas estrictas para restringir el número de personas que supieran sobre la existencia de Ultra para asegurar que ninguna acción alertaría a las potencias del Eje de que los Aliados poseían tal conocimiento. Al inicio de la guerra, el producto de Bletchley Park tenía por nombre en clave «Boniface» para dar la impresión a los no iniciados de que la fuente era un agente secreto. Tal fue el secretismo alrededor de los informes de *Boniface* que sus informes se llevaron directamente a Winston Churchill en una caja cerrada con llave, de la cual el primer ministro tenía personalmente la llave. La información así producida fue denominada «Ultra».

En Bletchley Park, matemáticos y criptógrafos británicos, entre ellos Alan Turing, jugadores de ajedrez y bridge, y fanáticos de los crucigramas, se enfrentaron a los problemas presentados por las muchas variaciones alemanas de Enigma, y encontraron medios de quebrar muchas de ellas. Los ataques británicos contra los equipos Enigma eran similares en concepto a los métodos polacos originales, pero basados en diseños diversos. Primero, el ejército alemán había cambiado sus prácticas (más rotores, diversas configuraciones, etc.), así que las técnicas polacas sin modificaciones dejaron de ser efectivas. En segundo lugar, la marina alemana había tenido prácticas más seguras, y nadie había roto el tráfico adicional.

Un nuevo ataque confió en el hecho de que el reflector (una cualidad patentada de Enigma) garantizase que ninguna letra pudiera ser codificada como ella misma, de manera que una A nunca podría volver a ser una A. Otra técnica asumía que varias expresiones comunes en alemán, como «Heil Hitler» o «por favor responde», se encontrarían frecuentemente en uno u otro texto sin cifrar; las suposiciones exitosas acerca del texto original eran conocidas en Bletchley como *cribas*. Con un fragmento del texto probable original y el conocimiento de que ninguna letra pudiera ser codificada como ella misma, no era raro que un fragmento del texto cifrado correspondiente pudiera ser identificado. Esto proporciona una pista acerca de la configuración del mensaje, de la misma manera que los polacos antes de la Guerra.

Los mismos operadores alemanes dieron una inmensa ayuda a los descifradores en varias ocasiones. En un caso, se solicitó a un operador que enviara un mensaje de prueba, por lo que simplemente tecleó la letra T repetidamente. Un analista británico recibió un mensaje largo sin una sola T en las estaciones de intercepción, e inmediatamente comprendió lo que había pasado. En otros casos, operadores de Enigma usaban constantemente las mismas configuraciones para codificar un mensaje, a menudo sus propias iniciales o las de sus novias. Se pusieron analistas a buscar estos mensajes en el mar de tráfico interceptado todos los días, permitiendo a Bletchley utilizar las técnicas polacas originales para encontrar las configuraciones iniciales durante el día. Otros operadores alemanes emplearon el mismo formulario para los informes diarios, en su mayoría para los informes de tiempo, de manera que la misma criba pudo usarse todos los días.

En el verano de 1940, descifradores británicos, que estuvieron descifrando con éxito los códigos de la Luftwaffe, fueron capaces de entregarle a Churchill información acerca de la entrega secreta de mapas de Inglaterra e Irlanda a las fuerzas de invasión de la Operación León Marino.

Desde sus inicios, la versión de Enigma utilizada por la marina se sirvió de una variedad más amplia de rotores que las versiones de la fuerza aérea o del ejército, así como varios métodos operacionales que la hacían más segura que las demás variantes de Enigma. Virtualmente no había indicios de las configuraciones iniciales de las máquinas, y había pocos textos para usarlas con claridad. Métodos distintos y mucho más difíciles debieron utilizarse para descifrar el tráfico entre las Enigma de la marina, y debido a la amenaza de los U-boats que navegaban tranquilamente por el Atlántico después de la caída de Francia, debió aplicarse una alternativa más directa de descifrado.

El 7 de mayo de 1941, la Real Armada capturó deliberadamente un barco meteorológico alemán, junto con equipos y códigos de cifrado, y dos días después el U-110 fue capturado, también equipado con una máquina Enigma, un libro de códigos, un manual de operaciones y otras informaciones que permitieron que el tráfico submarino de mensajes codificados se mantuviera roto hasta finales de junio, cosa que los miembros de la Armada prosiguieron haciendo poco después. Aunque para este momento, tanto británicos como estadounidenses disponían de máquinas Enigma e incluso tenían la capacidad de descifrar el código alemán gracias a los esfuerzos llevados por el equipo que lideraba Alan Turing, dicha captura facilitó los trabajos futuros de los criptógrafos aliados.

 Tras la guerra; revelación pública

El hecho de que el cifrado de Enigma había sido roto durante la guerra permaneció en secreto hasta finales de los años '60. Las importantes contribuciones al esfuerzo de la guerra de muchas grandes personas no fueron hechas públicas, y no pudieron compartir su parte de la gloria, pese a que su participación fue probablemente una de las razones principales por las que los Aliados ganaran la guerra tan rápidamente como lo hicieron. Finalmente, la historia salió a la luz.

Tras el fin de la guerra, los británicos y estadounidenses vendieron las máquinas Enigma sobrantes a muchos países alrededor del mundo, que se mantuvieron en la creencia de la seguridad de ésta. Su información no era tan segura como ellos pensaban, lo que, por supuesto, fue la razón de que británicos y estadounidenses pusieran a su disposición las máquinas.

En 1967, David Kahn publicó su libro *The Codebreakers*, que describe la captura de la máquina Enigma Naval del U-505 en 1945. Comentó que en aquel momento ya se podían leer los mensajes, necesitando para ello máquinas que llenaban varios edificios. Hacia 1970 los nuevos cifrados basados en ordenadores se comenzaron a hacer populares a la vez que el mundo migraba a comunicaciones computarizadas, y la utilidad de Enigma (y de las máquinas de cifrado rotatorio en general) rápidamente decrecía. En ese momento se decidió descubrir el pastel y comenzaron a aparecer informes oficiales sobre las operaciones de Bletchley Park en 1974.

En febrero de 2006, y gracias a un programa de traducción de este tipo de mensajes denominado «Proyecto-M4», se logró descifrar uno de los últimos mensajes que quedaban por descifrar aún tras la rendición alemana.

Con la ayuda de ordenadores particulares, se ha podido descifrar el contenido enviado por un sumergible desde el Atlántico, y cuya traducción decía así: «Señal de radio 1132/19. Contenido: Forzados a sumergirnos durante ataque, cargas de profundidad. Última localización enemiga: 8:30h, cuadrícula AJ 9863, 220 grados, 8 millas náuticas. [Estoy] siguiendo [al enemigo]. [El barómetro] cae 14 milibares. NNO 4, visibilidad 10».

 Simuladores

 Véase también
 Código Lorenz
 Magic (criptografía)
 The Imitation Game
 Enigma (película)
 Dispositivo Clave 41

 Referencias

 Bibliografía

 Enlaces externos

 Simulador de la Máquina Enigma by Aguilmo, 2009
 Simulador digital de la máquina Enigma
 Enigma, comentada enLa guía del principiante al cifrado
 *Enigma - una famosa historia de criptología* por Martin Oberzalek
 Simulador de Enigma M3/M4 para IPhone/IPod Touch
 Simulación de la máquina Enigma del Ejército y la Marina por Dirk Rijmenants
 *La máquina de cifrado Enigma*, por Tony Sale, el autor original del museo Bletchley Park
 Simulación de la máquina Enigma por Russell Schwager
 *La máquina Enigma* por Román Ceano en Kriptopolis
 Código fuente, máquina Enigma de 3 rotores, en lenguaje C por Martín Di Luzio
