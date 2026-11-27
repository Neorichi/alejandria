---
type: Artículo de enciclopedia
title: Criptoanálisis
description: "El criptoanálisis (del griego kryptós, ‘escondido’, y analýein, ‘desatar’) es una rama de la criptología dedicada al estudio de los sistemas criptográficos con el objetivo de identificar sus debilidades y quebrantar su …"
resource: https://es.wikipedia.org/wiki/Criptoanálisis
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptoanálisis"}
license: CC BY-SA 4.0
id: eswiki-Criptoanálisis
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptoanálisis

El **criptoanálisis** (del griego *kryptós*, ‘escondido’, y *analýein*, ‘desatar’) es una rama de la criptología dedicada al estudio de los sistemas criptográficos con el objetivo de identificar sus debilidades y quebrantar su seguridad sin disponer de la información secreta asociada.
En un uso no técnico, la práctica suele denominarse «romper» o «forzar» un código, aunque estos términos poseen significados específicos dentro del argot de la disciplina.
Las personas que se dedican al criptoanálisis se denominan *criptoanalistas*.

Los métodos y técnicas del criptoanálisis han cambiado drásticamente a través de la historia de la criptografía, adaptándose a una creciente complejidad criptográfica. Los sistemas criptográficos han evolucionado desde los métodos de lápiz y papel del pasado, pasando por máquinas como Enigma, utilizada por los nazis durante la Segunda Guerra Mundial, hasta llegar a los sistemas basados en computadoras del presente. Al aumentar la potencia de cálculo de los sistemas criptográficos, también los esquemas criptográficos han ido haciéndose más complejos. A mediados de los años 1970 se inventó una nueva clase de criptografía: la criptografía asimétrica. Los métodos utilizados para romper estos sistemas son por lo general radicalmente diferentes de los anteriores, y usualmente implican resolver un problema cuidadosamente construido en el dominio de la matemática pura. El ejemplo más conocido es la factorización de enteros.

Los resultados del criptoanálisis han cambiado también: ya no es posible tener un éxito ilimitado al romper un código, y existe una clasificación jerárquica de lo que constituye un ataque en la práctica.

 Objetivo

El objetivo del **criptoanálisis** es encontrar debilidades en los sistemas criptográficos que permitan elaborar ataques criptoanalíticos que rompan su seguridad sin el conocimiento de información secreta. Para ello estudia en profundidad el diseño y propiedades de los sistemas criptográficos.

En un sistema criptográfico de cifrado, por ejemplo, un estudio criptoanalítico puede consistir en conseguir la clave secreta o simplemente en acceder al texto en claro sin siquiera tener dicha clave. Sin embargo, el criptoanálisis no solo se ocupa de los cifrados, sino que su ámbito es más general: estudia los sistemas criptográficos con el objetivo de sortear la seguridad de otros tipos de algoritmos y protocolos criptográficos.

Sin embargo, el criptoanálisis suele excluir los ataques que no tienen como objetivo primario los puntos débiles de la criptografía utilizada, como los basados en el soborno, la coerción física, el robo o el keylogging. Estos ataques representan un riesgo creciente para la seguridad informática, y en la práctica suelen resultar más efectivos que el criptoanálisis tradicional para vulnerar un sistema.

 Ámbitos de estudio
Para la consecución de su objetivo, de elaboración de ataques criptoanalíticos que 'rompan' la seguridad de los sistemas criptográficos, los *criptoanalistas* estudian los sistemas criptográficos con el objetivo de descubrir debilidades que se puedan aprovechar. Para ello estudian los sistemas desde distintos enfoques.

 Teoría de la información
La teoría de la información proporciona herramientas para evaluar la seguridad de los sistemas criptográficos. Por ejemplo, en los sistemas de cifrado se estudia la entropía de la clave, de los criptogramas y de los mensajes en claro. Como el mensaje en claro suele estar expresado en idiomas humanos, también es interesante el estudio de su entropía y en especial su ratio de entropía.

Los *criptoanalistas* también estudian el secreto de los sistemas criptográficos. Por ejemplo, en los sistemas de cifrado estudian el grado de secreto caracterizando aquellos sistemas que tienen secreto perfecto a nivel teórico. De su estudio se concluye que el secreto perfecto requiere que el número de claves sea al menos tan grande como el número de mensajes. Esto es impracticable excepto para los llamados cifradores de libreta de un solo uso. En la práctica la mayor parte de los sistemas tienen claves finitas. Para caracterizar la seguridad de estos sistemas los *criptoanalistas* han desarrollado el concepto de distancia de unicidad, que es el valor mínimo de caracteres cifrados que hacen que solo haya una clave posible que haya sido utilizada para obtener este criptograma. Para ello se aprovecha el concepto de la entropía condicional del conocimiento de la clave una vez conocido el texto cifrado.

Para un sistema de cifrado hay una serie de entropías condicionales interesantes:

Supongamos:
 Un mensaje  es sometido a un proceso de cifrado usando la clave , obteniendo .
  representa la probabilidad condicional de la clave K dado el criptograma recibido . A veces también se denota por .
  representa la probabilidad condicional del mensaje  dado el criptograma recibido . A veces también se denota por .

Entonces:
 Podemos medir la incertidumbre (la entropía) del conocimiento de la clave una vez conocido el texto cifrado, y por tanto medir la **equivocación de la clave**, , también denotada por , mediante la fórmula:

La primera igualdad es por la definición de la entropía condicional y la segunda por aplicación del teorema de Bayes.
Observar que si  significa que se podrá romper el cifrado, pues ya no hay incertidumbre. Esta anulación nos introduce en el concepto de distancia de unicidad.

 Podemos medir la incertidumbre (la entropía) del conocimiento del mensaje una vez conocido el texto cifrado, y por tanto medir la **equivocación del mensaje**, , también denotada por , mediante la fórmula:

La primera igualdad es por la definición de la entropía condicional y la segunda por aplicación del teorema de Bayes.

 Podemos medir la incertidumbre (la entropía) del conocimiento de la clave una vez conocido el texto cifrado y el mensaje en claro, y por tanto medir la **equivocación del aspecto de la clave**, , también denotada por , mediante la fórmula:

 Podemos medir la incertidumbre (la entropía) del conocimiento del mensaje una vez conocido el texto cifrado y la clave, denotado por  o por . Dada una clave, la relación entre texto cifrado y texto en claro es uno a uno y, por tanto, .

Se ha demostrado que se cumple la siguiente relación entre las distintas entropías:

De esta relación podemos sacar una conclusión:
El objetivo de cualquiera que use un cifrador es tener un valor de  alto para que el sistema tenga la máxima fortaleza posible en caso de que el atacante disponga tanto del texto cifrado como del texto claro (**ataque con texto claro conocido**). Sin embargo, por la expresión de la ecuación, para ello es necesario que  sea pequeño. Tener un valor pequeño de  implica que haya poca incertidumbre respecto al texto claro una vez conocido el texto cifrado (**ataque con solo texto cifrado disponible**), lo cual es contrario a los intereses de cualquiera que cifre un mensaje. Por tanto, es necesaria una solución de compromiso para que el sistema tenga una fortaleza aceptable frente a ambos tipos de ataque.

 Base matemática y potencia de cálculo
Por ejemplo, la criptografía asimétrica emplea problemas matemáticos "duros" como base para su seguridad, así que un punto obvio de ataque es desarrollar métodos para resolver el problema. Los algoritmos asimétricos se diseñan en torno a la conjeturada dificultad de resolver ciertos problemas matemáticos. Si se encuentra un algoritmo mejorado que puede resolver el problema, el criptosistema se ve debilitado. Ejemplos:

 La seguridad del protocolo Diffie-Hellman depende de la dificultad de calcular un logaritmo discreto. En 1983, Don Coppersmith encontró una manera más rápida de calcular logaritmos discretos (dentro de ciertos grupos), y por tanto obligó a los criptógrafos a utilizar grupos más grandes, o diferentes tipos de grupos.
 La seguridad del protocolo RSA depende parcialmente de la dificultad en la factorización de enteros. Por tanto, un avance en la factorización tendría un impacto claro en la seguridad de RSA. En 1980, se podía factorizar un número de 50 dígitos con un coste de  operaciones elementales de computación. Para 1984, la tecnología en algoritmos de factorización había avanzado hasta el punto de que se podía factorizar un número de 75 dígitos con las mismas  operaciones. Los avances en la tecnología de computación también han provocado que estas operaciones se puedan realizar en un tiempo mucho menor. La Ley de Moore predice empíricamente que las velocidades de computación continuarán aumentando. Las técnicas de factorización podrían mostrar un desarrollo parecido, pero con gran probabilidad dependerán de la capacidad y la creatividad de los matemáticos, ninguna de las cuales ha sido nunca satisfactoriamente predecible. Números de 150 cifras, como los utilizados en RSA, han sido factorizados. El esfuerzo fue mayor que el mencionado anteriormente, pero no estaba fuera de los límites razonables para un ordenador moderno. Al comienzo del , los números de 150 cifras ya no se consideran suficientemente grandes como clave para RSA. Números de varios cientos de dígitos se seguían considerando demasiado difíciles de factorizar en 2005, aunque los métodos probablemente continuarán mejorando con el tiempo, obligando a los tamaños de clave a mantener el ritmo de crecimiento o a desarrollar nuevos algoritmos.

Otra característica distintiva de los algoritmos asimétricos es que, a diferencia de los ataques sobre criptosistemas simétricos, cualquier *criptoanálisis* tiene la oportunidad de usar el conocimiento obtenido de la clave pública.

 Ataques criptoanalíticos
Los ataques criptoanalíticos consisten en la aplicación de estudios criptoanalíticos para explotar las debilidades de sistemas criptográficos y así 'romper' su seguridad.

Los ataques criptoanalíticos varían en potencia y en su capacidad de amenaza para los sistemas criptográficos. Se dice que un ataque explota una "**debilidad certificacional**" si es un ataque teórico que resulta improbable de aplicar en ninguna situación realista; muchos de los resultados demostrados en la investigación criptoanalítica moderna son de este tipo.

Cada ataque tiene sus propiedades, las cuales lo caracterizan y hacen que ese ataque sea más o menos realizable.

No todos los ataques criptoanalíticos tienen como objetivo la ruptura total del sistema. El objetivo de un ataque criptoanalítico es obtener información desconocida sobre el sistema criptográfico de forma que se vaya debilitando su seguridad.

 Clasificación
Los ataques criptoanalíticos se pueden clasificar en función de sus características.

 Clasificación según la actitud del atacante
Los ataques se pueden clasificar según la forma de actuar del atacante.

 Ataques pasivos
En los ataques pasivos, el atacante no altera la comunicación, solo la escucha o monitoriza, para obtener información.
Por tanto, este tipo de ataques suelen usar técnicas de escucha de paquetes (sniffing) y de análisis de tráfico.
Son difíciles de detectar, ya que no implican alteración de los datos.
En algunos casos, este tipo de ataques se pueden dificultar cifrando la información posible objetivo de escuchas.

Un estudio reciente sobre la ciberseguridad de los dispositivos portátiles utilizó ataques pasivos a diferentes relojes inteligentes para comprobar si tienen vulnerabilidades importantes y si son los mejores objetivos durante el proceso de emparejamiento.

 Ataques activos
Suponen alguna modificación del flujo de datos o la creación de flujos falsos. Hay muchas técnicas que se usan en este tipo de ataques. Ejemplos:
 Suplantación
 Modificación de mensajes: capturar paquetes para luego ser borrados (dropping attacks), manipulados, modificados (tagging attack) o reordenados
 Reactuación: captura de paquetes y retransmisiones
 Degradación: técnicas para que el servicio se degrade

 Clasificación según el conocimiento previo
El criptoanálisis puede realizarse bajo una serie de supuestos sobre cuánto puede observarse o descubrirse sobre el sistema en cuestión antes de realizar el ataque. Como punto de comienzo básico, se supone que, para los propósitos del análisis, el algoritmo general es conocido; esta es la máxima de Shannon, "el enemigo conoce el sistema". Este es un supuesto razonable en la práctica: a lo largo de la Historia hay incontables ejemplos de algoritmos secretos que fueron conocidos mediante el espionaje, la traición y la ingeniería inversa. (En algunas ocasiones, algunos códigos han sido reconstruidos mediante la pura deducción, por ejemplo, el código Lorenz y el código PURPLE, así como una cierta cantidad de códigos clásicos.)

Otros supuestos se pueden categorizar como sigue:
 **Ataque con solo texto cifrado disponible**: el criptoanalista solo tiene acceso a una colección de textos cifrados o codificados.
 **Ataque con texto claro conocido**: el atacante tiene un conjunto de textos cifrados de los que conoce el correspondiente texto claro o descifrado.
 **Ataque con texto claro escogido** (**ataque con texto cifrado elegido**): el atacante puede obtener los textos cifrados (claros) correspondientes a un conjunto arbitrario de textos claros (cifrados) de su propia elección.
 **Ataque adaptativo de texto claro escogido**: como un ataque de texto claro escogido, pero el atacante puede elegir textos claros subsiguientes basándose en la información obtenida de los descifrados anteriormente. Similarmente, existe el ataque adaptativo de texto cifrado escogido.
 **Ataque de clave relacionada**: como un ataque de texto claro escogido, pero el atacante puede obtener texto cifrado utilizando dos claves diferentes. Las claves son desconocidas, pero la relación entre ambas es conocida; por ejemplo, dos claves que difieren en un bit.

Estos tipos de ataque difieren evidentemente en la plausibilidad de que ocurran en la práctica. Aunque algunos son más probables que otros, los criptógrafos suelen adoptar un enfoque conservador y asumir el peor caso imaginable cuando diseñan algoritmos, razonando que si un sistema es seguro incluso contra amenazas tan poco realistas, entonces debería resistir también al criptoanálisis en el mundo real.

Los supuestos en los que se basan estos ataques son a menudo más realistas de lo que podría parecer a primera vista. Para obtener un ataque con texto claro conocido, el criptoanalista podría muy bien conocer o ser capaz de inferir una parte que probablemente forma parte del texto claro, como, por ejemplo, el encabezamiento de una carta cifrada ("Estimado Sr."), o que el inicio de una sesión de ordenador contenga las letras "LOGIN". Un ataque de texto claro escogido es menos probable, pero en algunos casos puede ser plausible: por ejemplo, si se convence a alguien de reenviar un mensaje que uno mismo le ha mandado antes, pero en forma cifrada. Los ataques de clave relacionada son básicamente teóricos, aunque pueden ser realistas en ciertas situaciones, como, por ejemplo, al construir funciones hash criptográficas utilizando un cifrado por bloques.

 Clasificación según el objetivo en criptoanálisis
Los resultados de un criptoanálisis también pueden variar en utilidad. Por ejemplo, el criptógrafo Lars Knudsen (Knudsen, 1998) clasificó varios tipos de ataque sobre cifrados por bloques de acuerdo con la cantidad y la calidad de la información secreta que pudiera ser descubierta:
 *Ruptura total* - el atacante deduce la clave secreta.
 *Deducción global* - el atacante descubre un algoritmo funcionalmente equivalente para el cifrado y descifrado de mensajes, pero no obtiene la clave.
 *Deducción local (o de instancia)* - el atacante descubre textos claros o cifrados adicionales a los conocidos previamente.
 *Deducción de información* - el atacante descubre alguna información en el sentido de Shannon que no era conocida previamente.
 *Distinción del algoritmo* - el atacante puede distinguir la información cifrada de una permutación al azar.

Se pueden aplicar estas categorías a los ataques sobre otros tipos de algoritmos.

 Clasificación según el coste
Los ataques se pueden categorizar por la cantidad de recursos que requieren. Estos pueden tomar la forma de:
 Tiempo: el número de "operaciones primitivas" que deben ser realizadas. Esta categoría es bastante vaga; las operaciones primitivas podrían considerarse como una instrucción básica de computación, como una suma, una operación XOR, un desplazamiento bit a bit, etc., o como métodos de cifrado enteros.
 Memoria: la cantidad de almacenamiento necesario para realizar el ataque.
 Datos: la cantidad de textos claros y cifrados necesaria.

En la criptografía académica, una *debilidad* o una *ruptura* en un algoritmo se definen de una manera bastante conservadora. Bruce Schneier resume esta posición de la siguiente manera: *"Romper un cifrado simplemente significa encontrar una debilidad en el cifrado que puede ser explotada con una complejidad inferior a la de la fuerza bruta. No importa que la fuerza bruta pudiera requerir 2128 cifrados; un ataque que requiera 2110 cifrados se consideraría una ruptura... puesto de una manera simple, una ruptura puede ser tan solo una debilidad certificacional: una evidencia de que el código no es tan bueno como se publicita"* (Schneier, 2000).

 Ejemplos
Hay multitud de métodos de ataque criptoanalíticos. Estos se pueden clasificar según si están especializados en algún tipo de criptografía o si son más generales. Los principales son los siguientes:
 Especializados en cifrado clásico:
 Análisis de frecuencias
 Método Kasiski
 Índice de coincidencia
 Índice mutuo de coincidencia
 Especializados en criptografía simétrica:
 Criptoanálisis diferencial
 Criptoanálisis lineal
 Criptoanálisis integral
 Criptoanálisis estadístico
 Criptoanálisis de módulo n
 Ataque XSL (**eXtended Sparse Linearisation**)
 Ataque de deslizamiento
 Generales (aplicados en distintos ámbitos):
 Ataque de cumpleaños
 Ataque Man-in-the-middle
 Ataque Meet-in-the-middle
 Ataque de fuerza bruta
 Jardinería (criptoanálisis)
 Análisis de energía

 Ordenadores cuánticos
Los ordenadores cuánticos son potencialmente útiles para el criptoanálisis. Debido a que los estados cuánticos pueden existir en una superposición (es decir, estar entrelazados), es posible un nuevo paradigma computacional, en el que un bit no representa tan solo los estados 0 y 1, sino cualquier combinación lineal de estos. Peter Shor, de los Laboratorios Bell, probó la posibilidad, y varios equipos han demostrado uno u otro aspecto de la computación cuántica en los años transcurridos desde entonces. Por el momento, solo se ha demostrado una muy limitada prueba de posibles diseños. No hay, a fecha de 2006, una perspectiva creíble de un ordenador cuántico real y utilizable.

Sin embargo, de construirse un ordenador cuántico, muchas cosas cambiarían. La computación en paralelo sería probablemente la norma, y varios aspectos de la criptografía cambiarían.

En particular, dado que un ordenador cuántico sería capaz de realizar búsquedas de claves mediante fuerza bruta extremadamente rápidas, tamaños de clave considerados hoy en día más allá de los recursos de cualquier atacante por fuerza bruta quedarían al alcance de este ataque. Los tamaños de clave necesarios para quedar más allá de la capacidad de un ordenador cuántico serían considerablemente más grandes que los actuales. Algunos escritores de divulgación han declarado que ningún cifrado permanecería seguro de estar disponibles los ordenadores cuánticos. Otros aseguran que simplemente añadiendo bits a las longitudes de las claves se evitarán los ataques de fuerza bruta, incluso con ordenadores cuánticos.

Una segunda posibilidad es que el aumento en capacidad computacional pueda hacer posibles otros ataques de búsqueda de claves, más allá de la simple fuerza bruta, contra uno o varios de los algoritmos actualmente inexpugnables. Por ejemplo, no todo el progreso en la factorización mediante números primos se ha debido a una mejora de los algoritmos. Una parte se debe al incremento del poder computacional de los ordenadores, y la existencia de un ordenador cuántico en funcionamiento podría acelerar considerablemente las tareas de factorización. Este aspecto es bastante predecible, aunque no claramente. Lo que no puede ser anticipado es un avance en el campo teórico que requiera la computación cuántica, que pudiera hacer realizables ataques actualmente impracticables o incluso desconocidos. En ausencia de un método para predecir estos avances, solo nos queda esperar.

Se desconoce si existe un método de cifrado en tiempo polinómico que requiera un tiempo exponencial para su descifrado, incluso para un ordenador cuántico.

 Historia del criptoanálisis
El criptoanálisis ha evolucionado conjuntamente con la criptografía, y la competición entre ambos puede ser rastreada a lo largo de toda la historia de la criptografía. Las claves nuevas se diseñaban para reemplazar los esquemas ya rotos, y nuevas técnicas de criptoanálisis se desarrollaban para abrir las claves mejoradas. En la práctica, se considera a ambas como las dos caras de la misma moneda: para crear un sistema criptográfico seguro, es necesario tener en cuenta los descubrimientos del criptoanálisis. De hecho, hoy en día se suele invitar a la comunidad científica a que trate de romper las nuevas claves criptográficas, antes de considerar que un sistema es lo suficientemente seguro para su uso.

 Criptoanálisis clásico

Aunque la expresión criptoanálisis es relativamente reciente (fue acuñada por William F. Friedman en 1920), los métodos para romper códigos y cifrados son mucho más antiguos. La primera explicación conocida del criptoanálisis se debe al sabio árabe del , Yusuf Yaqub ibn Ishaq al-Sabbah Al-Kindi, en su *Manuscrito para Descifrar Mensajes Criptográficos*. Este tratado incluye una descripción del método de análisis de frecuencias (Ibraham, 1992).

El análisis de frecuencias es la herramienta básica para romper los cifrados clásicos. En todas las lenguas conocidas, ciertas letras del alfabeto aparecen más frecuentemente que otras; por ejemplo, en español, las vocales son muy frecuentes, ocupando alrededor del 45 % del texto, siendo la E y la A las que aparecen en más ocasiones, mientras que la frecuencia sumada de F, Z, J, X, W y K no alcanza el 2 %. Igualmente, se pueden reunir estadísticas de aparición de pares o tríos de letras. El análisis de frecuencias revelará el contenido original si el cifrado utilizado no es capaz de ocultar estas estadísticas. Por ejemplo, en un cifrado de sustitución simple (en el que cada letra es simplemente sustituida por otra), la letra más frecuente en el texto cifrado sería un candidato probable para representar la letra "E".

El análisis de frecuencias se basa tanto en el conocimiento lingüístico como en las estadísticas, pero al volverse cada vez más complicados los cifrados, las matemáticas se convirtieron gradualmente en el enfoque predominante en el criptoanálisis. Este cambio fue particularmente evidente durante la Segunda Guerra Mundial, cuando los esfuerzos para romper los códigos del Eje requirieron nuevos niveles de sofisticación matemática. Más aún, la automatización fue aplicada por primera vez en la Historia al criptoanálisis, bajo la forma de los dispositivos Bomba y Colossus, una de las primeras computadoras.

 Criptoanálisis moderno

Aunque la computación fue utilizada con gran éxito durante la Segunda Guerra Mundial, también hizo posible nuevos métodos criptográficos que eran órdenes de magnitud más complejos que los empleados hasta la fecha. Tomada como un todo, la criptografía moderna se ha vuelto mucho más impenetrable al criptoanalista que los métodos de pluma y papel del pasado, y parece que en la actualidad llevan ventaja sobre los métodos del puro criptoanálisis. El historiador David Kahn escribió que son muchos los criptosistemas en venta hoy por parte de cientos de compañías comerciales que no pueden ser rotos por ningún método conocido de criptoanálisis, y que incluso un ataque de texto claro escogido no permite en ciertos sistemas romper otros mensajes, por lo que, en cierto sentido, el criptoanálisis estaría "muerto", aunque —matizaba— hay más de un modo de encontrar debilidades (Observaciones sobre el 50 Aniversario de la National Security Agency, 1 de noviembre de 2002). Kahn menciona a continuación las mayores posibilidades para la intercepción, la colocación de dispositivos grabadores ("bugging"), los ataques de canal lateral y la criptografía cuántica como sustitutos de los métodos tradicionales del criptoanálisis.

Kahn podría haberse apresurado demasiado al declarar al criptoanálisis muerto; aún no se han extinguido los cifrados débiles. En medios académicos, se presentan regularmente nuevos diseños, y también son rotos frecuentemente: el cifrado por bloques Madryga, de 1984, demostró ser vulnerable a un ataque con solo texto cifrado disponible en 1998; FEAL-4, propuesto como sustituto para el algoritmo estándar de cifrado de datos DES, fue demolido por una avalancha de ataques de la comunidad académica, muchos de los cuales no eran enteramente realizables en condiciones prácticas. En la industria, igualmente, los cifrados no están exentos de fallos: por ejemplo, los algoritmos AS/1, AS/2 y CMEA, usados en la industria de teléfonos móviles, pueden ser rotos en horas, minutos o incluso en tiempo real por equipo informático ampliamente disponible. En 2001, se demostró que el algoritmo WEP, utilizado para proteger redes Wi-Fi, es susceptible de ser atacado mediante un ataque de clave relacionada.

 Los resultados del criptoanálisis

Los criptoanálisis exitosos han influido sin lugar a dudas en la Historia. La capacidad de leer los pensamientos, supuestamente secretos, o los planes de otros puede ser una ventaja decisiva, y nunca con mayor razón que en tiempos de guerra. Por ejemplo, durante la Primera Guerra Mundial, el descifrado del Telegrama Zimmermann fue capital para la entrada de los Estados Unidos en la guerra. En la Segunda Guerra Mundial, el criptoanálisis de los códigos alemanes, incluyendo la máquina Enigma y el código Lorenz, ha sido considerado desde un factor que apenas acortó la guerra en algunos meses en Europa, hasta un elemento crucial que determinó el resultado final (véase ULTRA). Los Estados Unidos también se beneficiaron del criptoanálisis del código japonés PURPLE durante la contienda (véase MAGIC).

Todos los gobiernos han sido conscientes desde antiguo de los potenciales beneficios del criptoanálisis para la inteligencia militar, tanto en lo puramente bélico como en lo diplomático, y han establecido con frecuencia organizaciones dedicadas en exclusiva al descifrado de códigos de otras naciones, por ejemplo GCHQ y NSA, organizaciones americanas todavía muy activas hoy en día. En 2004, surgió la noticia de que los Estados Unidos habían roto los códigos utilizados por Irán.

 Referencias

 Bibliografía
 Helen Fouché Gaines, "Cryptanalysis", 1939, Dover. ISBN 0-486-20097-3
 Abraham Sinkov, *Elementary Cryptanalysis: A Mathematical Approach*, Mathematical Association of America, 1966. ISBN 0-88385-622-0
 Ibraham A. "Al-Kindi: The origins of cryptology: The Arab contributions", *Cryptologia*, 16(2) (April 1992) pp. 97–126.
 David Kahn, "The Codebreakers - The Story of Secret Writing", 1967. ISBN 0-684-83130-9
 Lars R. Knudsen: Contemporary Block Ciphers. Lectures on Data Security 1998: 105-126
 Bruce Schneier, "Self-Study Course in Block Cipher Cryptanalysis", *Cryptologia*, 24(1) (January 2000), pp. 18–34.
 Friedrich L. Bauer: "Decrypted Secrets". Springer 2002. ISBN 3-540-42674-4
 Friedman, William F., Military Cryptanalysis, Part I, ISBN 0-89412-044-1
 Friedman, William F. Military Cryptanalysis, Part II, ISBN 0-89412-064-6
 Friedman, William F. Military Cryptanalysis, Part III, Simpler Varieties of Aperiodic Substitution Systems, ISBN 0-89412-196-0
 Friedman, William F. Military Cryptanalysis, Part IV, Transposition and Fractionating Systems, ISBN 0-89412-198-7
 Friedman, William F. y Lambros D. Callimahos, Military Cryptanalytics, Part I, Volume I, ISBN 0-89412-073-5
 Friedman, William F. y Lambros D. Callimahos, Military Cryptanalytics, Part I, Volume II, ISBN 0-89412-074-3
 Friedman, William F. y Lambros D. Callimahos, Military Cryptanalytics, Part II, Volume I, ISBN 0-89412-075-1
 Friedman, William F. y Lambros D. Callimahos, Military Cryptanalytics, Part II, Volume II, ISBN 0-89412-076-X

 Enlaces externos
En inglés:
 Basic Cryptanalysis (los archivos contienen unas cabeceras de 5 líneas que deben ser eliminadas)
 Distributed Computing Projects
 All lot of real encrypted messages on newsgroups
 Classic Javascript Cryptoanalysis Tools (solo funciona con IE 5 o posterior)
