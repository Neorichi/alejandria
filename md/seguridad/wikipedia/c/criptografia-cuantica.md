---
type: Artículo de enciclopedia
title: Criptografía cuántica
description: La criptografía cuántica es la criptografía que utiliza principios de la mecánica cuántica para garantizar la absoluta confidencialidad de la información transmitida.
resource: https://es.wikipedia.org/wiki/Criptografía_cuántica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_cuántica"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_cuántica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía cuántica

La **criptografía cuántica** es la criptografía que utiliza principios de la mecánica cuántica para garantizar la absoluta confidencialidad de la información transmitida. La criptografía cuántica como idea se propuso en 1970, pero hasta 1984 no se publicó el primer protocolo.

Una de las propiedades más importantes de la criptografía cuántica es que si un tercero intenta espiar durante la creación de la clave secreta, el proceso se altera detectándose al intruso antes de que se transmita información privada. Esto es consecuencia del teorema de no clonado.

La seguridad de la criptografía cuántica descansa en las bases de la mecánica cuántica, a diferencia de la criptografía de clave pública tradicional que descansa en supuestos de complejidad computacional no demostrada de ciertas funciones matemáticas.

La criptografía cuántica está cercana a una fase de producción masiva, utilizando láseres para emitir información en el elemento constituyente de la luz, el fotón, y conduciendo esta información a través de fibras ópticas.

 Conceptos básicos
La criptografía es la disciplina que trata de la transmisión y almacenamiento de datos de manera que no puedan ser comprendidos ni modificados por terceros. Los diferentes métodos de criptografía actualmente utilizados necesitan que dos personas que deseen comunicar información intercambien de forma segura una o más claves; una vez que las claves han sido intercambiadas, los interlocutores pueden transferir información con un nivel de seguridad conocido. Pero esta forma de trabajar basa la seguridad de las transmisiones exclusivamente en el intercambio de claves. La forma más segura de realizar este intercambio de claves es de manera presencial, pero ello no es posible en la mayoría de los casos, dado el múltiple número de interlocutores con los que se desea intercambiar información confidencial (bancos, tiendas en Internet, colegas de trabajo en sedes distantes, etcétera). De manera que el punto donde hay menor seguridad en el intercambio de información confidencial está en el proceso de intercambio y transmisión de las claves.

La mecánica cuántica describe la dinámica de cada partícula cuántica (fotones, electrones, etc.) en términos de estados cuánticos, asignando una probabilidad a cada posible estado de la partícula por medio de una función.

Algunos aspectos a considerar de la mecánica cuántica:

 Superposición: Una partícula puede poseer más de un estado a la vez, en otras palabras, se encuentra en realidad "repartida" entre todos los estados que le sean accesibles.

 La medición no es un proceso pasivo como se suponía en la mecánica clásica, ya que altera al sistema.

 Colapso de estados: Una partícula que se encuentra repartida entre todos sus estados accesibles, al ser medida se altera su estado superpuesto determinando en qué estado particular, de entre una variedad de estados posibles, se encuentra.

 Incertidumbre: En la teoría cuántica, algunos pares de propiedades físicas son complementarias (por ejemplo, la posición y el momentum), en el sentido de que es imposible saber el valor exacto de ambas. Si se mide una propiedad, necesariamente se altera la complementaria, perdiéndose cualquier noción de su valor exacto. Cuanto más precisa sea la medición sobre una propiedad, mayor será la incertidumbre de la otra propiedad.

 Entrelazamiento: Dos partículas cuánticas pueden tener estados fuertemente correlacionados, debido a que se generaron al mismo tiempo o a que interactuaron, por ejemplo, durante un choque. Cuando esto ocurre se dice que sus estados están entrelazados, lo que provoca que la medición sobre una de ellas determina inmediatamente el estado de la otra, sin importar la distancia que las separe. Este fenómeno se explica aplicando las leyes de conservación del momento y de la energía. (ver Paradoja EPR)

Las partículas utilizadas habitualmente en la criptografía cuántica son los componentes de la luz o fotones, y los estados que se utilizan para ser entrelazados o superpuestos entre sí son sus dos estados de polarización, que es una de las características conocidas de la luz, aunque no sea directamente perceptible.

Un fotón puede ser polarizado artificialmente en una dirección en particular con respecto a su dirección de desplazamiento. Dicha polarización puede ser detectada mediante el uso de filtros, orientados en el mismo sentido en el que la luz fue polarizada. Estos filtros dejan pasar los fotones polarizados en un estado y absorben los polarizados en el otro.

 Historia
La idea fundacional de la **criptografía cuántica** se atribuye a Stephen Wiesner, quien a comienzos de la década de 1970 formuló la **codificación conjugada** (*conjugate coding*). Su manuscrito fue rechazado entonces por el ámbito de la teoría de la información del IEEE, y se publicó años más tarde, en 1983, en *ACM SIGACT News*. En ese trabajo, Wiesner introdujo conceptos como el *dinero cuántico* y un canal de multiplexación cuántica que permite al receptor leer uno de dos mensajes codificados en observables no conmutativos (por ejemplo, polarizaciones lineal y circular), destruyendo la posibilidad de recuperar el otro al realizar la medición.

En 1984, Charles H. Bennett y Gilles Brassard presentaron el protocolo **BB84**, primer esquema práctico de distribución de claves cuánticas (QKD), que aprovecha estados cuánticos no ortogonales y el principio de indeterminación para detectar la presencia de un espía. Poco después, Bennett propuso una variante minimalista basada en solo dos estados, conocida como **B92** (1992).

En 1991, Artur Ekert desarrolló el protocolo **E91**, que propone un enfoque alternativo basado en entrelazamiento cuántico y en la verificación de desigualdades de Bell para garantizar la seguridad de la clave compartida.

Las primeras demostraciones experimentales de QKD se realizaron a finales de los años 1980 y principios de los 1990; un experimento pionero fue reportado por Bennett, Brassard y colaboradores en 1992. Para panoramas históricos y técnicos puede consultarse, entre otros, el repaso de Gisin y coautores.

 Intercambio de claves cuánticas

El intercambio de claves cuánticas (QKD, del inglés "quantum key distribution", distribución cuántica de claves) es un método de comunicación seguro que implementa un protocolo criptográfico utilizando propiedades de la mecánica cuántica. Permite que dos partes produzcan una clave secreta aleatoria compartida que solo ellos conocen, que luego puede usarse para cifrar y descifrar mensajes.

Una propiedad importante y única de la QKD es la capacidad de los dos usuarios que se comunican para detectar la presencia de un tercero que intenta obtener conocimiento de la clave. Esto resulta de un aspecto fundamental de la mecánica cuántica: el proceso de medición de un sistema cuántico en general perturba el sistema. Un tercero que intente espiar la clave debe de alguna manera medirla, introduciendo así anomalías detectables. Mediante el uso de superposiciones cuánticas o entrelazamiento cuántico y transmisión de información en estados cuánticos, se puede implementar un sistema de comunicación que detecte la escucha. Si el nivel de escucha está por debajo de un cierto umbral, se puede producir una clave que se garantiza que es segura (es decir, el espía no tiene información al respecto), de lo contrario, no es posible una clave segura y se interrumpe la comunicación.

La distribución de claves cuánticas solo se usa para producir y distribuir una clave, no para transmitir ningún dato de mensaje. Esta clave se puede usar con cualquier algoritmo de cifrado elegido para encriptar (y descifrar) un mensaje, que luego puede transmitirse a través de un canal de comunicación estándar. El algoritmo más comúnmente asociado con la QKD es la libreta de un solo uso.

El cifrado de la libreta de un solo uso es demostrablemente seguro. Consiste en emparejar el mensaje con una clave. La longitud de esta clave debe ser igual a la del mensaje, así cada bit del texto inicial se combina con otro bit de la clave realizando una suma modular.

Por ejemplo, se supone que se quiere enviar el mensaje “HOLA”. Para ello, a cada letra del abecedario se le adjudicará un número de 0 a 26 (“A” es 0, “B” es 1, etc). Si se quiere encriptar el mensaje, se necesita una clave con el mismo número de letras, por ejemplo “ZUMO”.
       H       O       L       A    mensaje
    7 (H)   14 (O)  11 (L)   0 (A)  mensaje
 +  25(Z)   20 (U)  12 (M)  14 (O)  clave
 =  32      34      23      14      mensaje + clave
 =  6 (G)    8 (I)  23 (X)  14 (O)  mensaje + clave (mod 26)
       G        I       X       O   mensaje cifrado
Cada letra del mensaje se suma modularmente con la letra correspondiente de la clave, para asegurarnos de que el resultado de esta suma vuelve a ser un número entre 0 y 26 (es decir, una letra del abecedario). Por tanto, el mensaje que se envía en lugar de “HOLA” es “GIXO”. Con el mensaje cifrado en su poder, el receptor solo tiene que realizar el proceso inverso para descifrar el mensaje. Es decir, ahora hay que restar la clave al mensaje encriptado.
        G       I       X       M   mensaje cifrado
     6 (G)   8 (I)  23 (X)  14 (O)  mensaje cifrado
 -  25 (Z)  20 (U)  12 (M)  14 (O)  clave
 = -19     -12      11       0      mensaje cifrado - clave
 =   7 (H)  14 (O)  11 (L)   0(A)   mensaje cifrado - clave (mod 26)
        H       O       L      A    mensaje

 Protocolo general
**Situación de partida**

La información cuántica permite que un emisor (Alice) envíe un mensaje a un receptor (Bob). Para ello disponen de lo siguiente

 Objetos cuánticos, es decir, objetos físicos que se comportan siguiendo las leyes de la física cuántica. En la práctica, estos objetos son fotones que pueden encontrarse en diferentes estados de polarización: pueden estar polarizados verticalmente (0), horizontalmente (1) o en cualquiera de los estados resultantes de superponer ambos. Dicha polarización puede ser detectada mediante el uso de filtros, que dejan pasar los fotones polarizados en un estado y absorben los polarizados en el otro.
 Un canal cuántico, que no es más que un canal físico de comunicación que puede transmitir información cuántica, así como clásica. Un ejemplo de canal cuántico es la conocida fibra óptica.

 Un canal clásico de comunicación que debe estar autentificado, es decir, Alice tiene que estar segura de que es a Bob a quien está enviando la información.

Ahora bien, la criptografía cuántica es lo que permite que Alice y Bob se comuniquen en secreto. En otras palabras, la criptografía cuántica hace posible detectar si el mensaje ha sido interceptado por un espía (Eva). Para llevar a cabo el protocolo de encriptamiento son necesarios dos elementos:

 Un algoritmo, que se encarga de manipular el mensaje para ocultarlo y hacerlo ilegible a terceros. Es decir, su función es la de encriptar el mensaje y desencriptarlo posteriormente para que pueda ser leído por el receptor. El algoritmo es conocido por las dos partes que se intercambian el mensaje, pudiendo llegar a ser incluso público. Es por ello que se necesita un elemento más para poder encriptar un mensaje.

 Una clave (secuencia de ceros y unos) conocida previamente por ambas partes, que es la que asegura que el proceso se mantenga privado, ya que como se ha dicho, el algoritmo puede ser de conocimiento público.

En función de la clave se pueden dividir los protocolos de encriptación en dos categorías: protocolos simétricos y antisimétricos. Los protocolos simétricos son aquellos en los que la clave es la misma para ambas partes, y los antisimétricos son aquellos en los que emisor y receptor poseen claves diferentes.

El establecimiento de la clave es el principal problema de la criptografía cuántica, ya que no hay forma de que Alice y Bob compartan una clave incondicionalmente segura mediante la información clásica.

No obstante, existen algunos algoritmos cuya seguridad está demostrada matemáticamente (como el cifrado de Vernam), o se basan en la complejidad de descifrarlo sin la clave secreta (sistema RSA, cuya seguridad no está rigurosamente probada). Algoritmos tales como el de Vernam y RSA son los más empleados hoy en día.

**Detección de espionaje**

La información clásica puede ser copiada sin que la información original se vea modificada. Por ello, trabajando con sistemas de comunicación clásicos no se puede saber con certeza si un mensaje ha sido manipulado por una tercera parte. Dicho de otro modo, en física clásica, Eva puede espiar y manipular el mensaje que Alice envía a Bob sin que ellos puedan descubrirlo.

Sin embargo, en mecánica cuántica el hecho de medir hace que el estado cuántico inicial se perturbe, se modifique. Esto se traduce en que si Eva intercepta el mensaje, Alice y Bob pueden descubrirlo fácilmente. Este hecho viene garantizado por:

 El teorema de no clonado. Este teorema nos asegura que “no pueden existir máquinas o dispositivos de clonación cuánticas”. En otras palabras, no es posible hacer copias exactas de la información cuántica.

 El tercer postulado de la mecánica cuántica o de la reducción del paquete de ondas, que asegura que al realizar una medida sobre un estado cuántico, este se está modificando.

Así, cuando Eva intercepta el mensaje entre Alice y Bob introduce anomalías (ruidos o errores), que pueden ser detectados por Alice y Bob.

Se puede demostrar que existe una relación entre la cantidad de anomalías introducidas en el mensaje y la cantidad de información que Eva ha interceptado, de esta manera es posible saber, no solo que Eva ha interceptado información, sino también la cantidad. Esta inspección es posible llevarla a cabo con las llamadas pruebas de seguridad, que combinan las leyes de la física cuántica y de la teoría de la información.

**Información secreta**

Primero, Alice y Bob evalúan el nivel de error y ruido que separan los dos conjuntos de datos. Las diferencias entre estos pueden provenir de:

 La intervención de Eva, que añade errores y ruido.

 Los errores y ruido de fondo, que no pueden ser evitados completamente.

Sin embargo, como los errores en la comunicación y los efectos de la observación de Eva no pueden ser distinguidos, por seguridad Alice y Bob deben suponer que todas las incoherencias son debidas a un espía.

Luego, gracias a las pruebas de seguridad y a ese nivel de ruido, Alice y Bob pueden evaluar la cantidad de información que ha interceptado Eva, llamada . A la misma vez, la teoría de la información les permite evaluar la cantidad de información que comparten después de la transmisión .

Finalmente, si la cantidad de información  es superior a cero, es decir, la cantidad de espionaje permanece por debajo de cierto umbral, entonces se puede extraer una clave secreta de tamaño máximo  de la trasmisión.

En el caso contrario, ninguna extracción es posible y  la transmisión debe ser interrumpida.

**Extracción de la clave**

En el caso en el que la información secreta, , sea superior a cero, Alice y Bob pueden empezar la extracción de la clave. Alice y Bob no comparten todavía una clave, sino datos correlacionados.

La extracción se compone por dos etapas: la reconciliación y la amplificación de la confidencialidad.

**Reconciliación de información**

La reconciliación de información es una forma de corrección de errores realizada entre las claves de Alice y Bob, para garantizar que ambas claves sean idénticas. Se lleva a cabo a través del canal público y, como tal, es vital minimizar la información enviada sobre cada clave, ya que Eva puede leerla.

Un protocolo común utilizado para la reconciliación de la información es el protocolo en cascada, propuesto en 1994. Este opera en varias rondas, con ambas claves divididas en bloques en cada ronda y comparando la paridad de esos bloques. Si se encuentra una diferencia en la paridad, entonces se realiza una búsqueda binaria para encontrar y corregir el error. Si se encuentra un error en un bloque de una ronda anterior que tenía la paridad correcta, entonces debe contenerse otro error en ese bloque; este error se encuentra y se corrige como antes. Este proceso se repite recursivamente.

Después de que se hayan comparado todos los bloques, Alice y Bob reordenan sus claves de la misma manera aleatoria, y comienza una nueva ronda. Al final de múltiples rondas, Alice y Bob tienen claves idénticas con alta probabilidad; sin embargo, Eva tiene información adicional sobre la clave debido a la información sobre la paridad intercambiada.

Últimamente, los turbocódigos, códigos LDPC y códigos polares se han utilizado para este propósito mejorando la eficiencia del protocolo en cascada.

**Amplificación de la privacidad**

La amplificación de la privacidad es un método para reducir y eliminar de manera efectiva la información parcial de Eva sobre la clave de Alice y Bob. Esta información parcial podría haberse obtenido tanto escuchando el canal cuántico durante la transmisión de la clave (introduciendo así errores detectables), como en el canal público durante la reconciliación de la información (donde se supone que Eva gana toda la información de paridad posible). La amplificación de privacidad utiliza la clave de Alice y Bob para producir una nueva clave más corta, de forma que Eva tenga una información insignificante sobre la nueva clave. Los bits de la clave pasan por un algoritmo que distribuye la ignorancia del espía sobre la clave final. De esta manera, la información del espía sobre la clave final puede hacerse arbitrariamente pequeña.

En primera aproximación, el tamaño de la clave final es igual al tamaño de la información compartida antes de la reconciliación, disminuido por el número de bits conocidos por el espía y disminuido por el número de bits que han pasado por el canal público durante la corrección de errores.

 Protocolo BB84
Este protocolo fue publicado en 1984 por Charles H. Bennett y Gilles Brassard, y con él se produce el nacimiento de la criptografía cuántica.

En este protocolo, la transmisión se logra utilizando fotones polarizados enviados entre el emisor (tradicionalmente de nombre Alice (en el lado A)) y el receptor (de nombre Bob (en el lado B)) mediante un canal cuántico, por ejemplo, una fibra óptica. Por otro lado, también se necesita la existencia de un canal público (no necesariamente cuántico) entre Alice y Bob, como por ejemplo Internet u ondas de radio, el cual se usa para mandar información requerida para la construcción la clave secreta compartida. Ninguno de los canales necesita ser seguro, es decir, se asume que un intruso (de nombre Eve) puede intervenirlos con el fin de obtener información.

Cada fotón representa un bit de información, cero o uno y la información se logra mediante la codificación de estados no-ortogonales, por ejemplo rectilíneamente (horizontal y vertical) o bien diagonalmente (en ángulos de 45° y 135°), como se muestra en la tabla de abajo. También se puede ocupar una polarización circular (horario o antihoraria). Tanto Alice como Bob, pueden emitir fotones polarizados.

**Primer paso**: El protocolo comienza cuando Alice decide enviar una secuencia de fotones polarizados a Bob. Para ello, Alice genera una secuencia aleatoria de bases, por ejemplo, entre rectilíneas (+) y diagonales (x), la cual es almacenada momentáneamente. Una vez hecho esto, Alice usa el canal cuántico para emitir a Bob un fotón polarizado al azar usando las bases que ella generó (un fotón por cada base), registrando la polarización con la que fue emitido.

Alice tiene entonces la secuencia de bases utilizadas y la polarización de los fotones emitidos.

La mecánica cuántica dice que no es posible realizar una medición que distinga entre 4 estados de polarización distintos si es que estos no son ortogonales entre sí, en otras palabras, la única medición posible es entre dos estados ortogonales (base). Es así que por ejemplo, si se mide en una base rectilínea, los únicos resultados posibles son horizontal o vertical. Si el fotón fue creado con una polarización horizontal o vertical (con un generador de estados rectilíneo), entonces esta medición arrojará el resultado correcto. Pero si el fotón fue creado con una polarización de 45° o 135° (generador diagonal), entonces la medición rectilínea arrojara un resultado de horizontal o vertical al azar. Es más, después de esta medición, el fotón quedará polarizado en el estado en el cual fue medido (horizontal o vertical), perdiéndose toda la información inicial de la polarización.

**Segundo paso**: Como Bob no sabe las bases que ocupó Alice para generar los fotones, no le queda otra opción que medir la polarización de los fotones usando una base aleatoria generada por él (rectilínea o diagonal).

Bob registra las bases que utilizó para medir los fotones y también los resultados de cada medición.

**Tercer paso**: Alice y Bob se contactan por medio del canal público para comunicarse las bases que utilizaron para generar y leer respectivamente: Bob envía las bases que él usó y Alice envía las bases que ella usó.

Ambos descartan las mediciones (bits) en donde no coincidieron en las bases (en promedio se descarta la mitad de los bits). Los bits que quedaron fueron generados y medidos con la misma base, por lo que la polarización registrada es la misma para Alice y para Bob.

Hasta este paso, en una comunicación ideal, Alice y Bob ya tienen una clave secreta compartida determinada por los bits que quedaron.

**Cuarto paso**: Dado que puede existir alguna impureza en el canal cuántico o, peor aún, un intruso pudo haber interceptado la transmisión de fotones, la polarización de los fotones pudo haber sido alterada por lo que Alice y Bob deben comprobar que efectivamente los bits que no fueron descartados coinciden en su valor.

Si un intruso intenta medir los fotones que mandó Alice, al igual que Bob no sabe con qué base se generaron, por lo que tiene que realizar sus mediciones usando bases al azar lo que inevitablemente introduciría una perturbación en los fotones enviados por Alice si es que no coinciden en la base. Tampoco podría generar los fotones originales de Alice ya que el teorema de no-clonación garantiza que es imposible reproducir (clonar) la información transmitida sin conocer de antemano el estado cuántico que describe la luz.

Si un intruso intentó obtener información de los fotones entonces, con una alta probabilidad, la secuencias de bits de Alice y Bob no coinciden. Con el fin de detectar la presencia del intruso, Alice y Bob revelan segmentos de la clave generada. Si difieren en una cantidad superior a un mínimo determinado, entonces se asume la existencia de un intruso y se aborta la comunicación.

Existen técnicas para que la información revelada de la clave sea lo menor posible (por ejemplo usando funciones de Hash). También existen técnicas para poder reparar la secuencia de bits en caso de que no haya habido un calce total (por ejemplo, en el caso de una interferencia).

**Quinto paso**: Para codificar un mensaje se puede utilizar el mismo canal cuántico con fotones polarizados, o utilizar el canal público cifrando el mensaje con un algoritmo de cifrado, ya que la clave para el cifrado se ha transmitido de manera absolutamente segura.

 Protocolo B92
El protocolo B92 es un protocolo parecido al BB84. En este protocolo, se supone que Alice prepara un bit clásico aleatoriamente, a, y dependiendo del resultado envía a Bob el qubit:

Bob, genera otro bit clásico aleatoriamente, a', y en función del resultado utiliza las bases:

De sus medidas, Bob obtiene el bit b, que puede tomar el valor 0 o 1, que corresponden a los estados -1 y +1 de las bases X y Z. Bob comunica el resultado b, pero manteniendo a' secreto. A continuación Alice y Bob seleccionan los bits en los que b=1, ya que b=0 solo si a=a' y  b=1 ocurre si a'=1-a, y esto ocurre con una probabilidad del 50%. La clave final es a para Alice y 1-a' para Bob.

En este protocolo, como es imposible para un espía medir los estados de Alice sin romper la relación entre Alice y Bob, estos pueden crear una clave de bits y a la vez establecer un límite para el ruido y espionaje durante la comunicación.

 Protocolo E91

El protocolo E91 o protocolo EPR, propuesto por Artur Ekert en 1991 toma este nombre de la paradoja de Einstein-Podolsky-Rosen. Este protocolo está basado en el entrelazamiento de pares de fotones.

El esquema de comunicación es similar al del protocolo BB84. La diferencia es que se necesita además una fuente que produzca una serie de pares de fotones entrelazados. Dicha fuente puede estar en manos de Alice, Bob o algún tercero, lo importante es que de cada par de fotones entrelazados producido, un fotón llegue a Alice y el otro a Bob.

Los posibles estados a los que puede colapsar un qubit:

Por lo que cuando dos qubits estén entrelazados, una vez realicemos una medida, ambos qubits colapsan al mismo valor

Se supone que Alice quiere enviar información a Bob; para ello se genera una secuencia de qubits entrelazados y cada uno de nuestros comunicadores puede enviar uno de los pares. Una vez ambos estén en comunicación, no importa quién haga primero la medida porque al estar entrelazados ambos obtendrán el mismo valor aleatorio.

Al igual que en otros protocolos, la medida de un qubit se puede expresar en distintas bases. En este caso se renombremos "x" y "+" para distinguirlas.

El procedimiento consta de 3 pasos:

**Primer paso:** Se origina una secuencia de qubits entrelazadas para Alice y Bob.

**Segundo paso:** Alice y Bob eligen de manera independiente una secuencia de bases para medir la serie.

**Tercer paso:** Alice y Bob comparan sus secuencias y mantienen únicamente los bits coincidentes en la misma base.

Sin embargo este proceso es demasiado simple por lo que será fácil de desenredar por un espía, Eva. Para solucionar este problema, Alice y Bob vuelven a analizar los resultados obtenidos usando esta vez la mitad de los valores no coincidentes que habían obtenido.

El protocolo original de Eckert era más sofisticado, estando constituido por tres bases en lugar de dos. La ventaja de este protocolo es que la clave se genera "naturalmente al azar", ya que es imposible saber de antemano qué polarización tendrá cada fotón.

Este test propuesto está basado en la desigualdad de Bell que nos sirve para describir los resultados de medir tres bases en dos qubits.

 Algoritmos en la criptografía cuántica
**Algoritmo de Shor**: Fue propuesto por Peter Shor en el año 1994. Este algoritmo logró demostrar una reducción exponencial en el tiempo de cálculo para la realización de factorizaciones en número primos. Este algoritmo realiza los procesos en paralelo por ello las compuertas cuánticas son capaces de realizar un número determinado de cálculo en forma simultánea. Para la resolución de problemas este algoritmo emplea matemáticas asociadas a la teoría de números, el análisis de Fourier, números complejos, entre otros. Este algoritmo dejaría obsoleto a algoritmos como el RSA.

**Algoritmo de Grover**: Fue inventado por Lov K. Grover en 1996. Es un algoritmo de carácter probabilístico, por lo que produce la respuesta correcta con una determinada probabilidad de error, que, no obstante, puede obtenerse tan baja como se desee por medio de iteraciones. Este algoritmo tiene múltiples implementación entre ellas la criptografía, podría aplicar fuerza bruta a una clave criptográfica simétrica de 128 bits en aproximadamente 2^64 iteraciones, o una clave de 256 bits en aproximadamente 2^128 iteraciones, este puede no ser necesariamente el algoritmo más eficiente.

**Algoritmo de Deutsch-Jozsa**: Es un algoritmo cuántico determinista propuesto por David Deutsch y Richard Jozsa en 1992. Este algoritmo es de poco uso práctico actual, es uno de los primeros ejemplos de un algoritmo cuántico que es exponencialmente más rápido que cualquier posible algoritmo clásico determinista. Este proporciona una solución para un caso específico simple y devuelve una función booleana (Falso o Verdadero) por lo que se vuelve determinista comparando dos funciones.

 Algoritmos de encriptación
Para entender qué son los algoritmos de encriptación se desarrollará primero qué es y cómo funcionan. Se entiende como algoritmo para encriptación a una función matemática usada en los procesos de encriptación y desencriptación. Trabaja en combinación con una llave (un número, palabra, frase, o contraseña) para encriptar y desencriptar datos. Para encriptar, el algoritmo combina matemáticamente la información a proteger con una llave provista. El resultado de este cálculo son los datos encriptados. Para desencriptar, el algoritmo hace un cálculo combinando los datos encriptados con una llave provista, siendo el resultado de esta combinación los datos desencriptados (exactamente igual a como estaban antes de ser encriptados si se usó la misma llave). Si la llave o los datos son modificados el algoritmo produce un resultado diferente.

Tenemos que estos algoritmos se dividen en tres tipos:

 **Algoritmo simétrico**: O bien conocidos como clave secreta  encripta y desencripta con la misma llave. Las principales ventajas de los algoritmos simétricos son su seguridad y su velocidad. Entre estos se encuentran: DES, RC2, IDEA, Blowfish, etc.

 **Algoritmo asimétrico**: O clave pública se caracteriza por usar una clave para encriptar y otra para desencriptar. Una clave no se derivará de la otra. Emplean longitudes de clave mucho mayores pero la complejidad de cálculo que comportan los hace más lentos. Por ello, los métodos asimétricos se emplean para intercambiar la clave de sesión mientras que los simétricos para el intercambio de información dentro. Acá se encuentran los siguientes: RSA, ElGamal, Diffie-Hellman, etc.

 **HASH**: Una función o método para generar claves o llaves que representen de manera casi unívoca a un documento, registro, archivo, etc., resumir o identificar un dato a través de la probabilidad, utilizando una función hash o algoritmo hash. Un hash es el resultado de dicha función o algoritmo. Entre estos están el: MD5, DSA, SHA-1, entre otros.

Estos algoritmos poseen una desventaja en común, la cual es que todos los algoritmos criptográficos mencionados anteriormente son vulnerables a los ataques de fuerza bruta (tratar sistemáticamente con cada posible clave de encriptación) buscando colisiones. La fuerza bruta es más fácil de aplicar en la medida que pasa el tiempo y nos referimos en la medida que pasa el tiempo al desarrollo de computadores cuánticos los cuales pueden explotar las vulnerabilidades con mayor facilidad.

Aprovechar las potencialidades de este tipo de computación requiere de la construcción de algoritmos cuánticos cuyo diseño está sujeto a las características matemáticas del problema a resolver (Gyongyosi and Imre, 2019). Uno de los primeros y más importantes hasta el momento es el algoritmo de Shor. Shor logró demostrar que su algoritmo reduce exponencialmente el tiempo necesario para la factorización de números y abrió el camino para el diseño de algoritmos cuánticos con aplicaciones en diferentes áreas del conocimiento.

 Implementación de la criptografía cuántica

 Experimental
En el 2008 se consiguió el sistema de intercambio de bits más alto hasta el momento, con claves seguras a 1 Mbit/s, en más de 20 km de fibra óptica, y 10 kbit/s, en más de 100 km de fibra. Fue logrado mediante una colaboración entre la Universidad de Cambridge y Toshiba, utilizando el protocolo BB84.

En agosto de 2015, la Universidad de Ginebra y Corning Inc. lograron la distancia de QKD más larga para fibra óptica (307 km). En el mismo experimento, se generó una tasa de intercambio de clave secreta de 12,7 kbit/s, convirtiéndola en la tasa de bits más alta para sistemas trabajando a distancias mayores de 100 km.

En junio de 2017, los físicos dirigidos por Thomas Jennewein en el Instituto de Computación Cuántica y la Universidad de Waterloo en Waterloo, Canadá, lograron la primera demostración de la distribución de claves cuánticas desde un transmisor terrestre a un avión en movimiento. Reportaron enlaces ópticos con distancias entre 3-10 km y generaron claves seguras de hasta 868 kilobytes de longitud.

También en junio de 2017, físicos chinos dirigidos por Pan Jianwei de la Universidad de Ciencia y Tecnología de China midieron fotones entrelazados a una distancia de 1203 km entre dos estaciones terrestres, sentando las bases para futuros experimentos intercontinentales de QKD. Más adelante en ese mismo año, el protocolo BB84 se implementó con éxito a través de enlaces de satélite desde *Micius* (que forma parte del proyecto chino de experimentos cuánticos a escala espacial, y que fue apodado así en honor al filósofo Mozi) a estaciones terrestres en China y Austria. Las claves se combinaron y el resultado se usó para transmitir imágenes y videos entre Pekín y Viena.

 Comercial
Algunas compañías que ofrecen sistemas comerciales de distribución de claves cuánticas son: ID Quantique (Ginebra) o MagiQ Technologies, Inc. (Nueva York).

En 2004, se llevó a cabo la primera transferencia bancaria del mundo utilizando QKD en Viena, Austria. La tecnología de cifrado cuántico proporcionada por la empresa suiza Id Quantique se utilizó en el cantón suizo de Ginebra para transmitir los resultados de la votación a la capital en las elecciones nacionales que tuvieron lugar el 21 de octubre de 2007.

 Ataques y pruebas de seguridad

 Interceptar y reenviar
El tipo más simple de ataque consiste en que Eva mide los estados cuánticos (fotones) enviados por Alicie y luego envía estados de reemplazo a Bob, preparados en el estado que ella mide. En el protocolo BB84, esto produce errores en la clave que comparten Alice y Bob. Como Eva no tiene conocimiento de la base en la que están codificados los estados enviados por Alice, solo puede adivinar en qué base medir, de la misma manera que Bob. Si elige correctamente, mide el estado correcto de polarización de fotones enviado por Alice y vuelve a enviar el estado correcto a Bob. Sin embargo, si elige incorrectamente, el estado que mide es aleatorio, y el estado enviado a Bob no puede ser el mismo que el enviado por Alicia. Si Bob luego mide este estado de la misma manera que Alice envió, él también obtiene un resultado aleatorio, ya que Eva le ha enviado un estado en la forma opuesta, con un 50% de posibilidades de un resultado erróneo (en lugar del resultado correcto que obtendría) sin la presencia de Eva. La tabla a continuación muestra un ejemplo de este tipo de ataque.

La probabilidad de que Eva elija la base incorrecta es del 50%, y si Bob mide este fotón interceptado en la base enviada por Alice obtiene un resultado aleatorio, es decir, tiene un 50% de probabilidad de obtener un resultado correcto y un 50% de uno incorrecto. La probabilidad de que un fotón interceptado genere un error en la cadena clave es entonces 50% × 50% = 25%. Si Alice y Bob comparan públicamente  de bits de sus claves (descartándolos así como bits de la clave, ya que ya no son secretos) la probabilidad de que encuentren desacuerdo e identifiquen la presencia de Eva es:

Así que para detectar a un espía con una probabilidad de , Alice y Bob deben comparar  bits de la clave.

 Ataque de intermediario
Como ningún principio de la mecánica cuántica puede distinguir de amigo o enemigo, la QKD sigue siendo susceptible a ataques de intermediario.

 Ataque de división del número de fotones
En el protocolo BB84, Alice envía estados cuánticos a Bob utilizando fotones individuales. En la práctica, muchas implementaciones utilizan pulsos de láser atenuados a un nivel muy bajo para enviar los estados cuánticos. Estos pulsos de láser contienen una cantidad muy pequeña de fotones, por ejemplo 0.2 fotones por pulso, que se distribuyen según una distribución de Poisson. Esto significa que la mayoría de los pulsos en realidad no contienen fotones (no se envía pulso), algunos pulsos contienen 1 fotón (que se desea) y algunos pulsos contienen 2 o más fotones. Si el pulso contiene más de un fotón, Eva puede dividir los fotones adicionales y transmitir el fotón individual restante a Bob. Esta es la base del ataque de división del número de fotones, donde Eva almacena estos fotones adicionales en una memoria cuántica hasta que Bob detecta el fotón único restante y Alicia revela la base de codificación. Eva puede medir sus fotones en la base correcta y obtener información sobre la clave sin introducir errores detectables.

Incluso con la posibilidad de un ataque se puede generar una clave segura, como se muestra en la prueba de seguridad GLLP, sin embargo, se necesita una cantidad mucho mayor de amplificación de privacidad.

Hay varias soluciones a este problema. La más obvia es utilizar una verdadera fuente de fotones individuales en lugar de un láser atenuado. Si bien esas fuentes aún se encuentran en una etapa de desarrollo, la QKD se ha llevado a cabo con éxito con ellas. Sin embargo, como las fuentes de corriente funcionan con una baja eficiencia y frecuencia, las tasas clave y las distancias de transmisión son limitadas. Otra solución es modificar el protocolo BB84, como se hace, por ejemplo, en el protocolo SARG04. La solución más prometedora es el protocolo de estado de señuelo, en el que Alice envía aleatoriamente algunos de sus pulsos de láser con un número de fotones promedio más bajo. Estos estados de señuelo se pueden usar para detectar un ataque, ya que Eva no tiene manera de saber qué pulsos son señal y cuáles señuelo.

 Lanzamiento de monedas cuánticas
Al contrario que la QKD, el lanzamiento de monedas cuánticas se produce cuando se generan qubits aleatorios entre dos jugadores que no confían entre sí porque ambos quieren ganar el lanzamiento de la moneda, lo que podría llevarlos a hacer trampas en una variedad de formas. La esencia del lanzamiento de monedas ocurre cuando los dos jugadores emiten una secuencia de instrucciones sobre un canal de comunicación que luego resulta en una salida. El protocolo consiste en los siguientes pasos:

 Alice primero elige una base aleatoria y una secuencia de qubits aleatorios. Luego, Alice codifica sus qubits elegidos como una secuencia de fotones que sigue la base elegida. Luego envía estos qubits como un tren de fotones polarizados a Bob a través del canal de comunicación.
 Bob elige una secuencia de lectura aleatoria para cada fotón individual. Luego lee los fotones y registra los resultados en dos tablas. Una tabla es de los fotones recibidos rectilíneos (horizontales o verticales) y la otra es de los fotones recibidos en diagonal. Bob puede tener huecos en sus tablas debido a pérdidas en sus detectores o en los canales de transmisión. Basado en esta tabla, Bob adivina qué base usó Alice y le comunica su suposición. Si adivinó correctamente, gana y si no, pierde.
 Alice informa si ganó o no al anunciar qué base utilizó. Luego, Alice confirma la información enviando a Bob su secuencia original de qubits que usó en el paso 1.
 Bob compara la secuencia de Alice con sus tablas para confirmar que no hubo trampa por parte de Alice. Las tablas deben corresponder a la base de Alice y no debe haber correlación con la otra tabla.

Para que Bob hiciera trampa, tendría que ser capaz de adivinar la base de Alicia con una probabilidad mayor del 50%. Para lograr esto, Bob debería poder determinar un tren de fotones polarizados aleatoriamente en una base a partir de un tren de fotones polarizados en otra base.

Alice, por otro lado, podía hacer trampa de dos maneras diferentes, pero tendría que tener cuidado porque Bob podría detectarlas fácilmente como una trampa. Cuando Bob envía una suposición correcta a Alicia, ella podría convencer a Bob de que sus fotones en realidad están polarizados al contrario de la suposición correcta de Bob. Alicia también podría enviarle a Bob una secuencia original diferente a la que realmente usó para vencer a Bob.

 Criptografía post-cuántica
La criptografía post-cuántica es la rama de la criptografía referida a algoritmos criptográficos que se consideran seguros contra un ataque de un ordenador cuántico. Desde 2018, esto no es cierto para los algoritmos de clave pública más populares, que se pueden romper con un ordenador cuántico hipotético suficientemente fuerte.

El problema con los algoritmos actuales es que su seguridad se basa en problemas (como la factorización de enteros o el logaritmo discreto) que se pueden resolver fácilmente en un ordenador cuántico suficientemente potente que ejecute el algoritmo de Shor. Aunque los ordenadores cuánticos experimentales actuales carecen de poder de procesamiento para romper cualquier algoritmo criptográfico real, muchos investigadores están diseñando nuevos algoritmos para prepararse para un momento en que la computación cuántica se convierta en una amenaza.

 Personaje Importantes en la Criptografía Cuántica
 Charles Bennett y Gilles Brassard: Descubrieron el concepto de criptografía cuántica y es uno de los padres fundadores de la teoría de la información cuántica moderna. Desarrolló un sistema de criptografía cuántica , conocido como BB84 , que permite la comunicación segura entre partes que inicialmente no comparten información secreta, basado en el principio de incertidumbre.
 Gilles Brassard: Es uno de los primeros pioneros de la información cuántica en el mundo. Sus avances más famosos son la invención de la criptografía cuántica y la tele transportación cuántica, ambas reconocidas universalmente como piedras angulares fundamentales de toda la disciplina.
 Emmy Noether: Para poder hablar de criptografía cuántica o incluso computación cuántica primero se pasa por la física cuántica, Emmy fue una matemática y física teórica de origen alemán. Egresada de la Universidad de Erlangen-Núrember. Ella realizó aportes importantes en el campo del álgebra y desarrolló el Teorema de Noether, el cual prueba que las leyes de la física clásica son independientes del tiempo y del espacio, lo cual sentó las bases de la física cuántica.
 Alba Cervera: De origen español es física con un máster en Astrofísica, Física de Partículas y Cosmología de la Universidad de Barcelona, ha sido galardonada con el IBM Q Awards. Actualmente está trabajando en la implementación de los algoritmos híbridos en la computación cuántica.

 Referencias

 Enlaces externos

 Implementaciones de Algoritmos Cuánticos para Principiantes. *Los Alamos National Laboratory*, Los Alamos, New Mexico 87545, USA (2018) 69 pag.

 La Computación Cuántica como Módulo de Secundaria A. Perry, R. Sun, C. Hughes, J. Isaacson, J. Turner (2020) Fermilab-FN-1077-T

 Fundamentos de Computación Cuántica - Notas de Clase (2022) Ronald de Wolf (2022) Universidad de Amsterdam.
