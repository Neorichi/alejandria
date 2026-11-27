---
type: Artículo de enciclopedia
title: Esteganografía
description: "La esteganografía (del griego στεγανός steganos, \"cubierto\" u \"oculto\", y γράφω grapho, \"escribir\") trata el estudio y aplicación de técnicas que permiten ocultar mensajes u objetos, dentro de otros, llamados …"
resource: https://es.wikipedia.org/wiki/Esteganografía
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Esteganografía"}
license: CC BY-SA 4.0
id: eswiki-Esteganografía
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Esteganografía

La **esteganografía** (del griego στεγανός *steganos*, "cubierto" u "oculto", y γράφω *grapho*, "escribir") trata el estudio y aplicación de técnicas que permiten ocultar mensajes u objetos, dentro de otros, llamados *portadores*, para que no se perciba su existencia. Es decir, procura ocultar mensajes dentro de otros objetos y de esta forma establecer un canal encubierto de comunicación, de modo que el propio acto de la comunicación pase *inadvertido* para observadores que tienen acceso a ese canal.

Una forma de diferenciar la esteganografía con la criptografía común es que la criptografía solo cifra los archivos manteniendo el archivo original visible, pero al abrirlo mostrará una secuencia de caracteres que no permitirá su lectura y para ver su contenido original es necesario conocer la clave. En la esteganografía, puede verse un archivo con un formato diferente, y para conocer su contenido original será necesario conocer la clave y el software con el que se ocultó.

Esta ciencia ha suscitado mucho interés en los últimos años, especialmente en el área de seguridad informática, debido a que ha sido utilizada por organizaciones criminales y terroristas. No obstante, no se trata de nada nuevo, pues se lleva empleando desde la antigüedad, y tradicionalmente la han utilizado las instituciones policíacas, militares y de inteligencia, y también criminales o civiles que desean evadir el control gubernamental, especialmente en regímenes tiránicos.

La esteganografía clásica se basaba únicamente en el desconocimiento del canal encubierto utilizado, mientras que en la era moderna también se emplean canales digitales (imagen, video, audio y protocolos de comunicaciones, entre otros) para alcanzar el objetivo. En muchos casos, el objeto contenedor es conocido, y lo que se ignora es el algoritmo de inserción de la información en dicho objeto.

Para que pueda hablarse de esteganografía, debe haber voluntad de comunicación encubierta entre el emisor y el receptor.

 Diferencias con la criptografía
Si bien la esteganografía puede confundirse con la criptografía, por ser ambas parte de los procesos de protección de la información, son disciplinas distintas, tanto en su forma de implementarse como en su objetivo mismo.

Mientras que la criptografía se utiliza para cifrar o codificar información de manera que sea ininteligible para un probable intruso, a pesar de que conozca su existencia, la esteganografía oculta la información en un portador de modo que *no sea advertido el hecho mismo* de su existencia y envío. De esta última forma, un probable intruso ni siquiera sabrá que se está transmitiendo información sensible.

Sin embargo, la criptografía y la esteganografía pueden complementarse, dando un nivel de seguridad extra a la información, es decir, es muy común (aunque no imprescindible) que el mensaje a esteganografiar sea previamente cifrado, de tal modo que a un eventual intruso no solo le costará advertir la presencia de la mensajería oculta, sino que, si la llegara a descubrir, la encontraría cifrada.

 Motivación
La utilidad del uso de la esteganografía se manifiesta en el llamado problema del prisionero (Gustavus J. Simmons, 1983). Resumidamente, en el problema del prisionero tenemos dos prisioneros, A y B, que quieren comunicarse de forma confidencial para escapar. El problema es que solo pueden intercambiar mensajes a través de un guardián. El guardián puede leer, modificar o generar él mismo los mensajes. Si el guardián detecta cualquier comunicación que pueda ser utilizada para escapar (por ejemplo, si detecta un cifrado), dejará de transmitir los mensajes. En este escenario, los prisioneros necesitan establecer un canal encubierto.

El uso de la esteganografía permite disponer de un canal encubierto de forma que es posible comunicarse sin ser detectado. La estrategia que sigue la esteganografía para resolver el problema del prisionero es esconder los datos que deben ser detectados, entre los mensajes permitidos por el guardián.

 Funcionamiento y terminología
La idea que sigue la esteganografía es enviar el mensaje oculto (E) “escondido” en un mensaje de apariencia inocua (C) que servirá de “camuflaje”. Esto es, se aplica una función de esteganografía . El resultado de aplicar la función (O), se envía por un canal inseguro y puede ser visto sin problemas por el guardián. Finalmente, el otro prisionero recibe el objeto O y, aplicando la función inversa , puede recuperar el mensaje oculto.

La terminología típica usada en la esteganografía es:

 Se define como *esquema esteganográfico* al conjunto de componentes que permite llevar a cabo la comunicación esteganográfica.
 El *portador* es todo aquel conjunto de datos que es susceptible de ser alterado para incorporarle el mensaje que queremos mantener en secreto. Puede ser de muchos tipos o formatos. Ejemplos: imagen (en sus distintos formatos), audio (en sus distintos formatos), texto plano, archivos binarios, un mensaje de protocolo de comunicación.
 Se habla de *mensaje legítimo* para referirse al mensaje transportado por el portador.
 Se llama *mensaje esteganográfico* al mensaje que queremos mantener en secreto y queremos esconder dentro del portador. Puede ser de distintos tipos o formatos. Ejemplos: imagen (en sus distintos formatos), audio (en sus distintos formatos), texto plano, archivos binarios.
 *Estego-algoritmo* es el algoritmo esteganográfico que indica cómo realizar el procedimiento de incorporación del mensaje que queremos mantener en secreto en el portador.
 La acción de ocultar el mensaje dentro del portador se denomina *empotrar* (del inglés *to embed*).
 Se llama *estegomensaje* al resultado de empotrar el mensaje esteganográfico dentro del portador.
 La acción de la recuperación, a partir del estego-mensaje, del mensaje oculto esteganográfico se denomina *extraer*.
 Por el rol desempeñado dentro del proceso esteganográfico, el emisor también se llama *embebedor* y el receptor, *extractor*. Al igual que en todo acto de comunicación convencional, es común que los roles de emisor y receptor se intercambien sucesivamente entre las partes que se comunican.
Se llama *esteganalista* o *estegoanalista* a la persona que intenta determinar la existencia o ausencia de un mensaje esteganográfico. Obsérvese que basta con determinar la existencia del mensaje; no tiene que llegar al contenido en sí. Es decir, un esteganalista es el que hace estegoanálisis.
Los *canales de selección* son canales adicionales al portador utilizado para embeber donde se comunica qué posiciones del portador se utilizan para la comunicación esteganográfica. Por ejemplo, si el portador es un libro de texto, un canal de selección podría estar definido por una sucesión de números naturales que representan la posición de cada una de las palabras dentro del libro de texto, que se deben considerar para construir el mensaje esteganográfico.
Las *clases de equivalencia* corresponden a pares de elementos del portador utilizado que tienen una interpretación semántica equivalente en la comunicación legítima, pero el uso de un elemento u otro tiene un significado acordado en la comunicación esteganográfica. Por ejemplo, las palabras 'lindo' y 'bonito' son sinónimos en español y podrían utilizarse indistintamente en un contexto. Un lector no notaría la diferencia en la semántica del texto, pero puede aprovecharse para construir el mensaje esteganográfico.

La capacidad de alterar el portador de manera imperceptible es posible gracias a la existencia de redundancia en el mismo. Las alteraciones pueden realizarse tanto en el contenido como en otros parámetros; por ejemplo, en el tiempo de respuesta en la emisión del portador.

 Clasificación según el estegoalgoritmo
El estegoalgoritmo es el algoritmo esteganográfico que indica cómo realizar el procedimiento de incorporación del mensaje esteganográfico en el portador para obtener el estegomensaje. Según el tipo de estegoalgoritmo, es posible distinguir dos tipos de esteganografía: esteganografía pura y esteganografía de clave secreta.

 Esteganografía pura
En este tipo de esteganografía, el estego-algoritmo establece un método fijo para incorporar el mensaje esteganográfico en el portador para obtener el estego-mensaje. En esta estrategia se está suponiendo que el guardián del problema del prisionero no conoce nada sobre el estego-algoritmo. Por tanto, la seguridad se basa en la oscuridad. Este enfoque para conseguir la seguridad pocas veces funciona y es especialmente desastroso en el caso de la criptografía.

 Esteganografía de clave secreta
En este tipo de esteganografía, el estego-algoritmo está parametrizado por una clave esteganográfica a la que se le llama estegoclave, que define cómo aplicar el algoritmo. Por ejemplo, la estegoclave podría indicar el lugar dentro del portador a partir del cual se comienza a realizar la incorporación del mensaje secreto. El emisor y el receptor deben acordar previamente tanto el estego-algoritmo como la estego-clave.

El proceso de extracción consiste en aplicar el estego-algoritmo y la estego-clave necesarios al estego-mensaje recibido para obtener el mensaje esteganográfico.

En este escenario, el guardián del problema del prisionero puede conocer el estegoalgoritmo, pero no conoce la estego-clave, que se emplea en el mismo. En esta estrategia, la seguridad se basa en el principio de Kerckhoffs. Aplicado a la esteganografía, el principio de Kerckhoffs podría incluir, como información revelable, el acceso a la información portadora antes de que se le aplique el estego-algoritmo.

 Historia
Estos son algunos ejemplos o historias que demuestran que la esteganografía ha estado presente desde tiempos antiguos y que constantemente va evolucionando.

 Heródoto
Probablemente uno de los ejemplos más antiguos del uso de que la esteganografía sea el referido por Heródoto en *Las historias*. En este libro, describe cómo un personaje tomó un cuadernillo de dos hojas o tablillas, rayó bien la cera que las cubría y en la madera misma grabó el mensaje y lo volvió a cubrir con cera regular. Otra historia, en el mismo libro, relata cómo otro personaje había rasurado a navaja la cabeza de su esclavo de mayor confianza, le tatuó el mensaje en el cuero cabelludo, esperó después a que le volviera a crecer el cabello y lo mandó al receptor del mensaje, con instrucciones de que le rasuraran la cabeza.

El científico italiano Giovanni Battista della Porta descubrió cómo esconder un mensaje dentro de un huevo cocido. El método consistía en preparar una tinta mezclando una onza de alumbre y una pinta de vinagre, y luego se escribía en la cáscara. La solución penetra en la cáscara porosa y deja un mensaje en la superficie de la albúmina del huevo duro, que solo se puede leer si se pela el huevo.

 Primer libro
El origen del vocablo *esteganografía* se remonta a principios del . El abad alemán Johannes Trithemius escribió un libro al que tituló *Steganographia*. En él se trataban temas referentes a la encriptación de mensajes, así como métodos para conjurar a los espíritus. El libro en cuestión se considera hoy en día un libro maldito y es muy apreciado por los esoteristas. Aparte de este título, también publicó *Polygraphiae Libri Sex*, un compendio de seis tomos sobre criptografía que no participaba de los elementos esotéricos de su libro anterior.

 Otros libros
 En *Sueño de Polífilo* (*Hypnerotomachia Poliphili*, ed. Aldus Manutius), escrito por Francesco Colonna en 1499, se puede obtener la frase *Poliam frater Franciscus Columna peramavit* (‘El hermano Francesco Colonna amó apasionadamente a Polia’) si se toma la primera letra de los treinta y ocho capítulos.
 Gaspar Schott (1665): *Schola steganographica*.
 Ian Caldwell, Dustin Thomason (2004): *Enigma del cuatro*.
 Lev Grossman (2004): *El códice secreto*.

 Segunda Guerra Mundial
Durante la Segunda Guerra Mundial, se usaron los microfilmes, en los puntos de las íes o en los signos de puntuación, para enviar mensajes. Los prisioneros usaban i, j, t y f para ocultar mensajes en código morse. Pero uno de los sistemas más ingeniosos se conoce con el nombre de *Null Cipher*. Consiste en enviar un mensaje, lo más común posible, y elegir cierta parte de él para ocultar el mensaje real. Un ejemplo es el texto siguiente:

*Apparently neutral's protest is thoroughly discounted and ignored. Isman hard hit. Blockade issue affects pretext for embargo on by products, ejecting suets and vegetable oils*. (Al parecer la protesta neutral es completamente descontada e ignorada. Isman afectados. Problema de bloqueo afecta pretexto de embargo sobre los productos, consigue expulsar sebo y aceites vegetales)

Si tomamos la segunda letra de cada palabra, aparece el mensaje *Pershing sails from NYr June i.* ("Pershing zarpa desde Nueva York el 1 de junio.")

 Tintas invisibles
No está claro desde qué época se comenzaron a utilizar, pero sin duda se han usado a lo largo de la historia y hasta la actualidad. Las más conocidas se pueden clasificar en dos categorías:

 Básicas: sustancias con alto contenido en carbono: leche, orina, zumo de limón, jugo de naranja, jugo de manzana, jugo de cebolla, solución azucarada, miel diluida, coca cola diluida, vino, vinagre, etc. Básicamente, sin importar cuál de las “tintas” mencionadas se utilice, el mensaje quedará invisible, y al calentar la superficie donde se escribió, el carbono reaccionará, y aparecerá el mensaje en un tono marrón.
 Más sofisticadas: aparecen tras una reacción química, o tras ser expuestas a la luz de cierta longitud de onda (IR, UV y otras).

 Esteganografía clásica y moderna
**Esteganografía “clásica”:** métodos completamente oscuros.
 Protección basada en desconocer el canal encubierto específico que se está usando.

**Esteganografía moderna:** uso de canales digitales:
 Archivo de texto (páginas web, código fuente, etc.)
 Audio digital
 Imágenes y vídeo digitales
 Archivos ejecutables
 Protocolos de comunicaciones

 Técnicas digitales
Existen numerosos métodos y algoritmos utilizados para ocultar la información dentro de archivos multimedia: imágenes, audio y vídeo. A continuación se indican algunos de los más usados.

 Enmascaramiento y filtrado
En este caso la información se oculta dentro de una imagen digital empleando marcas de agua que incluyen información, como el derecho de autor, la propiedad o licencias. El objetivo es diferente de la esteganografía tradicional (básicamente comunicación encubierta), ya que es añadir un atributo a la imagen que actúa como cubierta. De este modo se amplía la cantidad de información presentada.

 Algoritmos y transformaciones
Esta técnica oculta datos basados en funciones matemáticas que se utilizan a menudo en algoritmos de la compresión de datos. La idea de este método es ocultar el mensaje en los bits de datos menos importantes.

 Inserción en el bit menos significativo
Este es el método moderno más común y popular usado para esteganografía, también es uno de los llamados **métodos de sustitución**. Consiste en hacer uso del bit menos significativo de los píxeles de una imagen y alterarlo. La misma técnica puede aplicarse a vídeo y audio, aunque no es lo más común. Hecho así, la distorsión de la imagen en general se mantiene al mínimo (la perceptibilidad es prácticamente nula), mientras que el mensaje es esparcido a lo largo de sus píxeles. Esta técnica funciona mejor cuando el archivo de imagen es grande, posee fuertes variaciones de color ("imagen ruidosa") y también aventaja cuanto mayor sea la profundidad de color. Asimismo esta técnica puede utilizarse eficazmente en imágenes a escala de gris, pero no es apropiada para aquellas en color de 8 bit paletizadas (misma estructura que las de escalas de gris, pero con paleta en color). En general, los mejores resultados se obtienen en imágenes con formato de color RGB (tres bytes, componentes de color, por píxel).

**Ejemplo:**

El valor (1 1 1 1 1 1 1 1) es un número binario de 8 bits. Al bit ubicado más a la derecha se le llama "bit menos significativo" (LSB) porque es el de menor peso, alterándolo cambia en la menor medida posible el valor total del número representado.

Un ejemplo de esteganografía: Ocultamiento de la letra "A".
Si se tiene parte de una imagen con píxeles con formato RGB (3 bytes), su representación original podría ser la siguiente (3 píxeles, 9 bytes):

(1 1 0 1 1 0 1 0)     (0 1 0 0 1 0 0 1)     (0 1 0 0 0 0 1 1)

(0 0 0 1 1 1 1 0)     (0 1 0 1 1 0 1 1)     (1 1 0 1 1 1 1 1)

(0 0 0 0 1 1 1 0)     (0 1 0 0 0 1 1 1)     (0 0 0 0 0 1 1 1)

El mensaje a cifrar es ‘A’ cuya representación ASCII es (0 1 0 0 0 0 0 1), entonces los nuevos píxeles alterados serían:

(1 1 0 1 1 0 1 **0**)     (0 1 0 0 1 0 0 **1**)     (0 1 0 0 0 0 1 **0**)

(0 0 0 1 1 1 1 **0**)     (0 1 0 1 1 0 1 **0**)     (1 1 0 1 1 1 1 **0**)

(0 0 0 0 1 1 1 **0**)     (0 1 0 0 0 1 1 **1**)     (0 0 0 0 0 1 1 1)

Observar que se ha sustituido el bit del mensaje (letra A, marcados en negritas) en cada uno de los bits menos significativos de color de los 3 píxeles. Fueron necesarios 8 bytes para el cambio, uno por cada bit de la letra A, el noveno byte de color no se utilizó, pero es parte del tercer pixel (su tercer componente de color).

El método del LSB funciona mejor en los archivos de imágenes que tienen una alta resolución y usan gran cantidad de colores. En caso de archivos de audio, favorecen aquellos que tienen muchos y diferentes sonidos que poseen una alta tasa de bits.

Además este método no altera en absoluto el **tamaño** del archivo portador o cubierta (por eso es "una técnica de sustitución"). Posee la desventaja de que el tamaño del archivo portador debe ser mayor al mensaje a embeber; se necesitan 8 bytes de imagen por cada byte de mensaje a ocultar; es decir, la capacidad máxima de una imagen para almacenar un mensaje oculto es de su 12,5 %. Si se pretende emplear una mayor porción de bits de la imagen (por ejemplo, no solo el último, sino los dos últimos), puede comenzar a ser perceptible al ojo humano la alteración general provocada.

 Técnicas más utilizadas según el tipo de medio

 En documentos
El uso de esteganografía en los documentos puede funcionar con solo añadir un espacio en blanco y las fichas a los extremos de las líneas de un documento. Este tipo de esteganografía es extremadamente eficaz, ya que el uso de los espacios en blanco y tabs no es visible para el ojo humano, al menos en la mayoría de los editores de texto, y se producen de forma natural en los documentos, por lo que en general es muy difícil que levante sospechas.

 En imágenes

El método más utilizado es el LSB, puesto que para un computador un archivo de imagen es simplemente un archivo que muestra diferentes colores e intensidades de luz en diferentes áreas (píxeles). El formato de imagen más apropiado para ocultar información es el BMP (color de 24 bits), debido a que es el de mayor proporción (imagen no comprimida) y normalmente es de la más alta calidad. Finalmente se prefiere optar por formatos BMP de 8 bits o bien otros tales como el GIF, por ser de menor tamaño. Se debe tener en cuenta que el transporte de imágenes grandes por Internet puede despertar sospechas.

Cuando una imagen es de alta calidad y resolución, es más fácil y eficiente ocultar y enmascarar la información dentro de ella.

La desventaja del método LSB es que es el más conocido y popular, por tanto el más estudiado. Deja marcas similares a ruido blanco en el portador (imagen contenedora), lo cual la convierte en altamente detectable o vulnerable a ataques de estegoanálisis, para evitarlo se recurre a dispersar el mensaje, en general usando secuencias aleatorias.

Es importante notar que si se oculta información dentro de un archivo de imagen y este es convertido a otro formato, lo más probable es que la información oculta dentro sea dañada y, consecuentemente, resulte irrecuperable.

 En audio
Cuando se oculta información dentro de archivos de audio, por lo general la técnica usada es *low bit encoding* (baja bit de codificación), que es similar a la LSB que suele emplearse en las imágenes. El problema con el *low bit encoding* es que en general es perceptible para el oído humano, por lo que es más bien un método arriesgado que alguien lo use si están tratando de ocultar información dentro de un archivo de audio.

*Spread Spectrum* también sirve para ocultar información dentro de un archivo de audio. Funciona mediante la adición de ruidos al azar a la señal de que la información se oculta dentro de una compañía aérea y la propagación en todo el espectro de frecuencias.

Otro método es *Echo data hiding*, que usa los ecos en archivos de sonido con el fin de tratar de ocultar la información. Simplemente añadiendo extra de sonido a un eco dentro de un archivo de audio, la información puede ser ocultada. Lo que este método consigue mejor que otros es que puede mejorar realmente el sonido del audio dentro de un archivo de audio.

 En vídeo
En vídeo, suele utilizarse la transformada de coseno discreta (, DCT). DCT funciona cambiando ligeramente cada una de las imágenes en el vídeo, solo de manera que no sea perceptible por el ojo humano. Para ser más precisos acerca de su funcionamiento, DCT altera los valores de ciertas partes de las imágenes, por lo general las redondea. Por ejemplo, si parte de una imagen tiene un valor de 6,667, lo aproxima hasta 7.

La esteganografía en vídeo es similar a la aplicada en las imágenes, además de que la información está oculta en cada fotograma de vídeo. Cuando solo una pequeña cantidad de información que está oculta dentro del código fuente por lo general no es perceptible a todos. Sin embargo, cuanta mayor información se oculte, más perceptible será.

 En archivos de cualquier tipo

Uno de los métodos más fáciles de implementar es el de inyección o agregado de bytes al final del archivo. Esta técnica consiste, esencialmente, en agregar o adosar al final de un archivo, de cualquier tipo, otro archivo que será el contenedor del "mensaje a ocultar", también de cualquier tipo. Esta metodología es la más versátil, pues permite usar cualquier tipo de archivo como portador (documentos, imágenes, audio, vídeos, ejecutables, etc) y añadir al final del archivo contenedor el "paquete enviado", que es otro archivo, también de cualquier tipo.

Esta es una técnica que *no se vale de las limitaciones humanas* (vista y oído) para implementar la estrategia esteganográfica, sino que se vale de la forma de funcionamiento de la aplicaciones software que utilizan el portador. No degradan el contenido del portador de ninguna forma, por ejemplo, si es una imagen, permanecerá intacta; ya que el "mensaje" se le inyecta o adosa al final de la misma y la aplicación usada para visualizarla la mostrará normalmente hasta donde ella finalice. Esto es debido a que todo tipo de archivo, en su cabecera, entre otros, contiene ciertos bytes fijos (en cantidad y ubicación) usados exclusivamente para indicar el tamaño del archivo. La aplicación que utilice un archivo, de cualquier tipo, siempre lee su cabecera primero, adquiere ese valor como su tamaño (en cantidad de bytes) y seguidamente lee el resto del archivo hasta el final indicado por dicho valor. De modo que si se coloca algo (mensaje) más allá del valor de ese parámetro, no será leído por la aplicación normal, por tanto no detectado, y el archivo portador funcionará normalmente.

Si bien es la técnica más sencilla de implementar, y de uso muy difundido, *tiene la gran desventaja* que provoca **crecimiento del portador**, tanto como el tamaño de su mensaje, siendo por tanto una estrategia fácilmente detectable. Un sencillo programa de estegoanálisis lo detecta por la sola lectura de su cabecera y la comprobación del tamaño real de archivo portador; incluso cualquier usuario desconfiado puede muchas veces sospechar del portador por su tamaño ocupado en disco en relación con su contenido.
Otra desventaja, aunque muy relativa y eventual, es que el crecimiento del portador podría ser limitante a la hora de trasferirlo por las redes, particularmente por Internet.

Los programas o software que utilizan esta técnica son llamados joiners, básicamente unen dos archivos, el portador y el de mensaje, manteniendo el valor inicial del tamaño en bytes indicado en la cabecera del primero. Esta es una técnica no utilizada si se pretende obtener características de indetectabilidad.

Si no se requiere reunir requisitos de indetectabilidad, es uno de los métodos preferidos por su sencillez, flexibilidad y escasas limitaciones. Prácticamente cualquier tipo de portador es admitido, con o sin compresión, incluso módulos ejecutables. En algunos casos provoca corrupción del portador, lo cual no es gran problema: practicada la técnica e inyectado el mensaje se prueba el portador con su aplicación correspondiente, si se ha degradado y/o no funciona bien, sencillamente toma otro, del mismo u otro tipo y se repite la operación.

 Otros
Una nueva técnica esteganográfica implica el inyectar retardos (conocidos por su traducción al inglés como "delays") imperceptibles a los paquetes enviados sobre la red desde el teclado. Los retardos en el tecleo de los comandos en algunos usos (telnet o software de escritorio remoto) pueden significar un retardo en paquetes, y los retardos en los paquetes se pueden utilizar para codificar datos.

 Estegoanálisis
Lo que la esteganografía esencialmente hace es explotar las limitaciones de la percepción humana (excepto en el método de inyección), ya que los sentidos humanos (vista y oído) tienen límites para percibir información extraña intercalada en su contenido; pero existen aplicaciones software disponibles que pueden hacer ese trabajo de detección, por diversas técnicas analíticas, al estudio y aplicación de ellas corresponde lo denominado estegoanálisis.

Mientras que con la esteganografía se intenta estudiar e implementar métodos para enviar mensajes encubiertos en portadores de apariencia inocua o normal, con el estegoanálisis se estudian las formas de detectar la presencia de mensajes ocultos en potenciales portadores (no necesariamente de extraerlos).

Debido a que la esteganografía es invasiva, es decir, deja huellas en el medio de transporte utilizado, las técnicas de estegoanálisis intentan detectar estos cambios, usando incluso complejos mecanismos estadísticos. Las técnicas de estegoanálisis,  normalmente, hasta el momento, solo llegan a brindar nivel de probabilidad de existencia de un mensaje encubierto en un portador.

 Algoritmos estegoanalíticos
Los algoritmos estegoanalíticos se pueden catalogar en diferentes maneras, destacando: según la información disponible y según la finalidad buscada.

 Según la información disponible
Existe la posibilidad de catalogar estos algoritmos en función de la información que ostente el estegoanalista en cuanto a mensajes en claro y cifrados. Se trata de una técnica similar a la criptografía, sin embargo, poseen varias diferencias:

 Chosen stego attack: el estegoanalista percibe el estego objeto final y el algoritmo estenográfico empleado.
 Known cover attack: el estegoanalista comprende el objeto conductor inicial y el estego objeto final.
 Known stego attack: el estegoanalista conoce el objeto portador inicial y el estego objeto final, además del algoritmo usado.
 Stego only attack: el estegoanalista percibe exclusivamente el estego objeto.
 Chosen message attack: el estegoanalista, a raíz de un mensaje seleccionado por él, origina un estego objeto.
 Known message attack: el estegoanalista detenta el estego objeto y el mensaje encubierto, el cual es conocido por éste

 Según la finalidad buscada
El propósito primordial de la esteganografía es transferir información de manera inadvertida, sin embargo, es posible que un atacante ostente dos pretensiones diferentes:

 Estegoanálisis pasivo: no efectúa alteraciones en el estego objetivo, por tanto, examina dicho estego objetivo con el fin de establecer si traslada información encubierta y recobra el mensaje escondido, la clave empleada o los dos.
 Estegoanálisis activo: varía el estego objetivo inicial, por consiguiente, pretende reprimir el traslado de información, si existe.

 Software de esteganografía

 * StegHide* Software esteganográfico que soporta cifrado y compresión. Trabaja con archivos JPEG, BMP, WAV y AU y tiene licencia GNU
 * Steghide UI* Interfaz gráfica de usuario (GUI) para StegHide de licencia GNU

 Véase también

 Criptografía
 Marca de agua digital
 Cifrado negable
 Polygraphia

 Referencias

 Enlaces externos
 *Disappearing Cryptography* por Peter Wayner
  editado por Stefan Katzenbeisser y Fabien, A.P. Petitcolas
 *Information Hiding: Steganography and Watermarking—Attacks and Countermeasures* por Neil F. Johnson, Zoran Duric y Sushil Jajodia

 Artículos de esteganografía (en inglés)
 QuickStudy:Steganography: Hidden Data en computerworld.com
 Steganography Articles, Links, and Whitepapers en Forensics.nl
 Ejemplos que demuestran las imágenes ocultadas en otras imágenes
 FBI Article: An Overview of Steganography for the Computer Forensics Examiner
 Cryptography and Steganography (versión web de diapositivas del PowerPoint), 2002. Elonka Dunin ' presentación de una descripción de esteganografía, así como una discusión de si Al - qaeda pudo haber utilizado esteganografía para planear los ataques del 11 de septiembre de 2001
 Steganography & Digital Watermarking— Papers e información relacionada con la esteganografía y el estegoanálisis por Neil F. Johnson desde 1995 hasta el presente.
 Detecting Steganographic Content on the Internet, 2001. Paper by Niels Provos and Peter Honeyman, Center for Information Technology Integration, University of Michigan
  Rights Protection for Natural Language Text, incluye varios artículos sobre este tema
  Network Steganography Project, includes articles on network steganography (Wireless LANs and VoIP) - provided by Krzysztof Szczypiorski and Wojciech Mazurczyk.
  Principle and applications of BPCS-Steganography, Paper original de BPCS-Steganography.

 Artículos de esteganoanálisis (en inglés)
 Steganalysis Papers en ataques contra esteganografía, marcas de agua y contramedidas a estos ataques.
 Cyber warfare: steganography vs. steganalysis Para muchos métodos y herramientas listos que son desarrollados para ocultar la información en datos de las multimedias, un número igual de métodos listos y herramientas que se están desarrollando para detectar y revelar sus secretos.
 "Detecting Steganographic Content on the Internet", PDF file, 813 KB.
 Alguna páginas de ejemplos Gaspar Schott's Schola steganographica
 Analyzing steganography applications: Ejemplos prácticos en cómo un cierto número de softwares de esteganografía trabaja.
