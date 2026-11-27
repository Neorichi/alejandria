---
type: Artículo de enciclopedia
title: Seguridad de la contraseña
description: La seguridad de la contraseña es una medida de la efectividad de una contraseña contra ataques de adivinación o de fuerza bruta.
resource: https://es.wikipedia.org/wiki/Seguridad_de_la_contraseña
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_de_la_contraseña"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_de_la_contraseña
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad de la contraseña

La **seguridad de la contraseña** es una medida de la efectividad de una contraseña contra ataques de adivinación o de fuerza bruta. En su forma habitual, estima cuántas pruebas necesitaría un atacante que no tiene acceso directo a la contraseña, en promedio, para adivinarla correctamente. La seguridad de una contraseña depende de la longitud, la complejidad y la imprevisibilidad.

El uso de contraseñas seguras reduce el riesgo general de una infracción de seguridad, pero las contraseñas seguras no reemplazan la necesidad de otros controles de seguridad eficaces. La efectividad de una contraseña de una seguridad determinada está fuertemente determinada por el diseño y la implementación de los factores (conocimiento, propiedad, inherencia). El primer factor es el foco principal de este artículo.

La velocidad a la que un atacante puede enviar contraseñas adivinadas al sistema es un factor clave para determinar la seguridad del sistema. Algunos sistemas imponen un tiempo de espera de varios segundos después de un pequeño número (por ejemplo, tres) de intentos fallidos de introducción de contraseña. En ausencia de otras vulnerabilidades, dichos sistemas se pueden proteger de manera efectiva con contraseñas relativamente simples. Sin embargo, el sistema debe almacenar información sobre las contraseñas del usuario de alguna forma y si esa información es robada, digamos al violar la seguridad del sistema, las contraseñas del usuario pueden estar en riesgo.

En 2019, el NCSC del Reino Unido analizó bases de datos públicas de cuentas violadas para ver qué palabras, frases y cadenas de caracteres usaba la gente. El primero de la lista fue 123456, que aparece en más de 23 millones de contraseñas. La segunda cadena más popular, 123456789, no fue mucho más difícil de descifrar, mientras que las cinco primeras incluían "qwerty", "contraseña" y 1111111.

 Creación de contraseña
Las contraseñas se crean de forma automática (utilizando equipo de aleatorización) o por un humano; el último caso es más común. Si bien la seguridad de las contraseñas elegidas al azar contra un ataque de fuerza bruta se puede calcular con precisión, determinar la seguridad de las contraseñas generadas por humanos es un desafío.

Normalmente, a los seres humanos se les pide que elijan una contraseña, a veces guiados por sugerencias o restringidos por un conjunto de reglas, al crear una nueva cuenta para un sistema informático o un sitio web de Internet. Solo son posibles estimaciones aproximadas de la fuerza, ya que los humanos tienden a seguir patrones en tales tareas, y esos patrones generalmente pueden ayudar a un atacante. Además, las listas de contraseñas comúnmente elegidas están ampliamente disponibles para que las utilicen los programas de adivinación de contraseñas. Dichas listas incluyen los numerosos diccionarios en línea para varios lenguajes humanos, bases de datos violadas de texto sin formato y contraseñas hash de varias cuentas comerciales y sociales en línea, junto con otras contraseñas comunes. Todos los elementos de dichas listas se consideran débiles, al igual que las contraseñas que son simples modificaciones de ellos.

Aunque actualmente están disponibles programas de generación de contraseñas aleatorias que están pensados para ser fáciles de usar, todavía suelen generar contraseñas aleatorias y difíciles de recordar, lo que a menudo hace que las personas elijan implementar las suyas propias. Sin embargo, esto es intrínsecamente inseguro porque los estilos de vida, las preferencias de entretenimiento y otras cualidades individualistas clave de la persona  entran en juego para influir en la elección de la contraseña, mientras que la prevalencia de las redes sociales en línea ha hecho que obtener información sobre las personas sea mucho más fácil.

 Validación de adivinar la contraseña
Los sistemas que usan contraseñas para la autenticación deben tener alguna forma de verificar cualquier contraseña ingresada para obtener acceso. Si las contraseñas válidas simplemente se almacenan en un archivo del sistema o en una base de datos, un atacante que obtenga suficiente acceso al sistema obtendrá todas las contraseñas de usuario, lo que le dará al atacante acceso a todas las cuentas del sistema atacado y posiblemente a otros sistemas donde los usuarios emplean las mismas, o contraseñas similares. Una forma de reducir este riesgo es almacenar solo un hash criptográfico de cada contraseña en lugar de la contraseña en sí. Los hash criptográficos estándar, como la serie Secure Hash Algorithm (SHA), son muy difíciles de revertir, por lo que un atacante que se apodera del valor hash no puede recuperar directamente la contraseña. Sin embargo, el conocimiento del valor hash permite al atacante probar rápidamente las conjeturas sin conexión. Los programas de descifrado de contraseña están ampliamente disponibles y probarán una gran cantidad de contraseñas de prueba contra un hash criptográfico robado.

Las mejoras en la tecnología informática siguen aumentando la velocidad a la que se pueden probar las contraseñas adivinadas. Por ejemplo, en 2010, el Georgia Tech Research Institute desarrolló un método para usar GPGPU para descifrar contraseñas mucho más rápido. Elcomsoft inventó el uso de tarjetas gráficas comunes para una recuperación más rápida de la contraseña en agosto de 2007 y pronto presentó la patente correspondiente en los Estados Unidos. En 2011, había productos comerciales disponibles que afirmaban tener la capacidad de probar hasta 112000 contraseñas por segundo en una computadora de escritorio estándar, utilizando un procesador de gráficos de alta gama para ese momento. Un dispositivo de este tipo descifrará una contraseña de 6 letras en mayúsculas o minúsculas en un día. Tenga en cuenta que el trabajo se puede distribuir en muchas computadoras para una aceleración adicional proporcional a la cantidad de computadoras disponibles con GPU comparables. Hay disponibles hashes especiales de estiramiento de teclas que tardan un tiempo relativamente largo en calcularse, lo que reduce la velocidad a la que se pueden adivinar. Aunque se considera una buena práctica utilizar el estiramiento de claves, muchos sistemas comunes no lo hacen.

Otra situación en la que es posible adivinar rápidamente es cuando la contraseña se utiliza para formar una clave criptográfica. En tales casos, un atacante puede comprobar rápidamente si una contraseña adivinada decodifica correctamente los datos cifrados. Por ejemplo, un producto comercial afirma probar 103000 contraseñas WPA PSK por segundo.

Si un sistema de contraseñas solo almacena el hash de la contraseña, un atacante puede calcular previamente los valores hash para las variantes de contraseñas comunes y para todas las contraseñas más cortas que una cierta longitud, lo que permite una recuperación muy rápida de la contraseña una vez que se obtiene su hash. Las listas muy largas de hashes de contraseñas precalculadas se pueden almacenar de manera eficiente utilizando tablas de arco iris. Este método de ataque puede frustrarse almacenando un valor aleatorio, llamado sal criptográfica, junto con el hash. La sal se combina con la contraseña al calcular el hash, por lo que un atacante que precalcule una tabla de arco iris tendría que almacenar para cada contraseña su hash con todos los valores de sal posibles. Esto se vuelve inviable si la sal tiene un rango lo suficientemente grande, digamos un número de 32 bits. Desafortunadamente, muchos sistemas de autenticación de uso común no emplean sales y las tablas de arco iris están disponibles en Internet para varios de estos sistemas.

 La entropía como medida de la fuerza de la contraseña
Es habitual en la industria informática especificar la seguridad de la contraseña en términos de entropía de la información, que se mide en bits y es un concepto de la teoría de la información. En lugar de la cantidad de conjeturas necesarias para encontrar la contraseña con certeza, se proporciona el logaritmo en base 2 de ese número, que comúnmente se conoce como la cantidad de "bits de entropía" en una contraseña, aunque esta no es exactamente la misma cantidad. como entropía de información. Una contraseña con una entropía de 42 bits calculada de esta manera sería tan fuerte como una cadena de 42 bits elegida al azar, por ejemplo, mediante un lanzamiento de moneda justo. Dicho de otra manera, una contraseña con una entropía de 42 bits requeriría 242 (4,398,046,511,104) intentos para agotar todas las posibilidades durante una búsqueda de fuerza bruta. Por lo tanto, al aumentar la entropía de la contraseña en un bit, el número de conjeturas requeridas se duplica, lo que hace que la tarea del atacante sea dos veces más difícil. En promedio, un atacante tendrá que probar la mitad del número posible de contraseñas antes de encontrar la correcta.

 Contraseñas aleatorias

Las contraseñas aleatorias consisten en una cadena de símbolos de longitud especificada tomados de algún conjunto de símbolos mediante un proceso de selección aleatoria en el que cada símbolo tiene la misma probabilidad de ser seleccionado. Los símbolos pueden ser caracteres individuales de un conjunto de caracteres (por ejemplo, el conjunto de caracteres ASCII), sílabas diseñadas para formar contraseñas pronunciables o incluso palabras de una lista de palabras (formando así una frase de contraseña).

La fuerza de las contraseñas aleatorias depende de la entropía real del generador de números subyacente; sin embargo, estos a menudo no son verdaderamente aleatorios, sino pseudoaleatorios. Muchos generadores de contraseñas disponibles públicamente utilizan generadores de números aleatorios que se encuentran en bibliotecas de programación que ofrecen entropía limitada. Sin embargo, la mayoría de los sistemas operativos modernos ofrecen generadores de números aleatorios criptográficamente fuertes que son adecuados para la generación de contraseñas. También es posible utilizar dados ordinarios para generar contraseñas aleatorias. Los programas de contraseñas aleatorias a menudo tienen la capacidad de garantizar que la contraseña resultante cumpla con una política de contraseñas local; por ejemplo, produciendo siempre una combinación de letras, números y caracteres especiales.

Para las contraseñas generadas por un proceso que selecciona aleatoriamente una cadena de símbolos de longitud, *L*, de un conjunto de *N* símbolos posibles, el número de contraseñas posibles se puede encontrar elevando el número de símbolos a la potencia *L*, es decir, *N**L*. El aumento de *L* o *N* fortalecerá la contraseña generada. La fuerza de una contraseña aleatoria medida por la entropía de la información es solo el logaritmo en base 2 o log2 del número de contraseñas posibles, asumiendo que cada símbolo de la contraseña se produce de forma independiente. Por lo tanto, la entropía de información de una contraseña aleatoria, *H*, viene dada por la fórmula:

donde *N* es el número de símbolos posibles y *L* es el número de símbolos en la contraseña. *H* se mide en bits. En la última expresión, *log* puede tener cualquier base.

Un byte binario se suele expresar mediante dos caracteres hexadecimales.

Para encontrar la longitud, *L*, necesaria para lograr la fuerza deseada *H*, con una contraseña extraída al azar de un conjunto de *N* símbolos, se calcula:

redondeado al siguiente número entero más grande.

La siguiente tabla usa esta fórmula para mostrar las longitudes requeridas de contraseñas generadas verdaderamente al azar para lograr las entropías de contraseña deseadas para conjuntos de símbolos comunes:

 Contraseñas generadas por humanos
Las personas son notoriamente pobres para lograr la entropía suficiente para producir contraseñas satisfactorias. Según un estudio en el que participaron medio millón de usuarios, la entropía media de la contraseña se estimó en 40.54 bits. Algunos magos de teatro explotan esta incapacidad para divertirse, de una manera menor, adivinando supuestas elecciones aleatorias (de números, digamos) hechas por miembros de la audiencia.

Así, en un análisis de más de 3 millones de contraseñas de ocho caracteres, la letra "e" se utilizó más de 1.5 millones de veces, mientras que la letra "f" se utilizó sólo 250000 veces. Una distribución uniforme habría tenido cada carácter utilizado unas 900000 veces. El número más común utilizado es "1", mientras que las letras más comunes son a, e, o y r.

Los usuarios rara vez hacen un uso completo de conjuntos de caracteres más grandes para formar contraseñas. Por ejemplo, los resultados de piratería obtenidos de un esquema de phishing de MySpace en 2006 revelaron 34000 contraseñas, de las cuales solo el 8.3% utilizaba mayúsculas, números y símbolos mixtos.

La fuerza total asociada con el uso de todo el conjunto de caracteres ASCII (números, mayúsculas y minúsculas y caracteres especiales) solo se logra si cada contraseña posible es igualmente probable. Esto parece sugerir que todas las contraseñas deben contener caracteres de cada una de varias clases de caracteres, quizás letras mayúsculas y minúsculas, números y caracteres no alfanuméricos. De hecho, tal requisito es un patrón en la elección de la contraseña y se puede esperar que reduzca el "factor de trabajo" de un atacante (en términos de Claude Shannon). Esta es una reducción en la "fuerza" de la contraseña. Un mejor requisito sería requerir una contraseña que NO contenga ninguna palabra en un diccionario en línea, o una lista de nombres, o cualquier patrón de matrícula de cualquier estado (en los Estados Unidos) o país (como en la UE). Si se requieren elecciones con patrones, es probable que los humanos las utilicen de formas predecibles, como poner en mayúscula una letra, agregar uno o dos números y un carácter especial. Esta previsibilidad significa que el aumento de la seguridad de la contraseña es menor en comparación con las contraseñas aleatorias.

 Publicación especial del INET 800-63-2
La publicación especial 800-63 del INET de junio de 2004 (revisión 2) sugirió un esquema para aproximar la entropía de las contraseñas generadas por humanos:

Usando este esquema, se estima que una contraseña de ocho caracteres seleccionada por humanos sin caracteres en mayúsculas y caracteres no alfabéticos o con cualquiera de los dos conjuntos de caracteres tiene 18 bits de entropía. La publicación del INET reconoce que en el momento del desarrollo, había poca información disponible sobre la selección de contraseñas en el mundo real. Investigaciones posteriores sobre la entropía de contraseñas seleccionadas por humanos utilizando datos del mundo real recientemente disponibles han demostrado que el esquema INET no proporciona una métrica válida para la estimación de entropía de contraseñas seleccionadas por humanos. La revisión de junio de 2017 de SP 800-63 (Revisión 3) elimina este enfoque.

 Consideraciones de uso y aplicación
Debido a que las configuraciones locales del teclado varían, no todos los 94 caracteres imprimibles ASCII se pueden usar en todas partes. Esto puede representar un problema para un viajero internacional que desea iniciar sesión en un sistema remoto usando un teclado en una computadora local. Muchos dispositivos portátiles, como tabletas y teléfonos inteligentes, requieren secuencias de turnos complejas o el intercambio de aplicaciones de teclado para ingresar caracteres especiales.

Los programas de autenticación varían en cuanto a los caracteres que permiten en las contraseñas. Algunos no reconocen las diferencias entre mayúsculas y minúsculas (por ejemplo, la "E" mayúscula se considera equivalente a la "e" minúscula), otros prohíben algunos de los otros símbolos. En las últimas décadas, los sistemas han permitido más caracteres en las contraseñas, pero aún existen limitaciones. Los sistemas también varían en la longitud máxima de contraseñas permitidas.

En la práctica, las contraseñas deben ser razonables y funcionales para el usuario final, así como lo suficientemente seguras para el propósito previsto. Las contraseñas que son demasiado difíciles de recordar pueden olvidarse y, por lo tanto, es más probable que se escriban en papel, lo que algunos consideran un riesgo para la seguridad. Por el contrario, otros argumentan que obligar a los usuarios a recordar contraseñas sin ayuda solo puede acomodar contraseñas débiles y, por lo tanto, plantea un mayor riesgo de seguridad. Según Bruce Schneier, la mayoría de las personas son buenas para proteger sus billeteras o carteras, que es un "gran lugar" para almacenar una contraseña escrita.

 Bits de entropía necesarios
El número mínimo de bits de entropía necesarios para una contraseña depende del modelo de amenaza para la aplicación dada. Si no se utiliza la extensión de clave, se necesitan contraseñas con más entropía.  RFC 4086, "Requisitos de aleatoriedad para la seguridad", publicado en junio de 2005, presenta algunos modelos de amenazas de ejemplo y cómo calcular la entropía deseada para cada uno. Sus respuestas varían entre 29 bits de entropía necesarios si solo se esperan ataques en línea, y hasta 96 bits de entropía necesarios para claves criptográficas importantes utilizadas en aplicaciones como cifrado donde la contraseña o la clave deben estar seguras durante un largo período de tiempo y estiramiento. no es aplicable. Un estudio de 2010 del Georgia Tech Research Institute basado en claves no extendidas recomendó una contraseña aleatoria de 12 caracteres, pero como requisito de longitud mínima. Tenga en cuenta que la potencia informática sigue creciendo, por lo que para evitar ataques fuera de línea, los bits necesarios de entropía también deberían aumentar con el tiempo.

El extremo superior está relacionado con los estrictos requisitos de elección de claves utilizadas en el cifrado. En 1999, un proyecto de la Electronic Frontier Foundation rompió el cifrado DES de 56 bits en menos de un día utilizando hardware especialmente diseñado. En 2002, *distribution.net* descifró una clave de 64 bits en 4 años, 9 meses y 23 días. Al 12 de octubre de 2011, distribution.net estima que descifrar una clave de 72 bits con el hardware actual tardará unos 45579 días o 124.8 años. Debido a las limitaciones actualmente conocidas de la física fundamental, no hay expectativas de que cualquier computadora digital (o combinación) sea capaz de romper el cifrado de 256 bits mediante un ataque de fuerza bruta. Aún se desconoce si las computadoras cuánticas podrán o no hacerlo en la práctica, aunque el análisis teórico sugiere tales posibilidades.

 Directrices para contraseñas seguras
 Pautas comunes
Las pautas para elegir buenas contraseñas generalmente están diseñadas para hacer que las contraseñas sean más difíciles de descubrir mediante adivinaciones inteligentes. Las pautas comunes defendidas por los defensores de la seguridad del sistema de software incluyen:

 Utilice una longitud mínima de contraseña de 10 o más caracteres si está permitido.
 Incluya caracteres alfabéticos en minúsculas y mayúsculas, números y símbolos si está permitido.
 Genere contraseñas al azar cuando sea posible.
 Evite usar la misma contraseña dos veces (por ejemplo, en múltiples cuentas de usuario y/o sistemas de software).
 Evite la repetición de caracteres, patrones de teclado, palabras del diccionario, secuencias de letras o números.
 Evite el uso de información que esté o pueda estar asociada públicamente con el usuario o la cuenta, como el nombre de usuario, los nombres de los antepasados o las fechas.
 Evite el uso de información que los colegas y/o conocidos del usuario puedan saber que está asociada con el usuario, como nombres de familiares o mascotas, vínculos románticos (actuales o pasados) e información biográfica (por ejemplo, números de identificación, nombres o fechas de ancestros).
 No utilice contraseñas que consistan totalmente en una combinación simple de los componentes débiles antes mencionados.

Algunas pautas desaconsejan anotar las contraseñas, mientras que otras, señalando la gran cantidad de sistemas protegidos con contraseña a los que los usuarios deben acceder, recomiendan anotar las contraseñas siempre que las listas de contraseñas escritas se guarden en un lugar seguro, no adjunto a un monitor o en un lugar desbloqueado cajón de escritorio. El NCSC recomienda el uso de un administrador de contraseñas.

El posible juego de caracteres para una contraseña puede estar limitado por diferentes sitios web o por la variedad de teclados en los que se debe ingresar la contraseña.

 Ejemplos de contraseñas débiles

Al igual que con cualquier medida de seguridad, las contraseñas varían en efectividad (es decir, fuerza); algunos son más débiles que otros. Por ejemplo, la diferencia de debilidad entre una palabra de diccionario y una palabra con ofuscación (es decir, las letras de la contraseña se sustituyen por, digamos, números, un enfoque común) puede costarle a un dispositivo de descifrado de contraseñas unos segundos más; esto agrega poca fuerza. Los ejemplos a continuación ilustran varias formas en que se pueden construir contraseñas débiles, todas las cuales se basan en patrones simples que dan como resultado una entropía extremadamente baja, lo que les permite probarse automáticamente a altas velocidades.:

 Contraseñas predeterminadas (suministradas por el proveedor del sistema y destinadas a cambiarse en el momento de la instalación): *contraseña*, *predeterminada*, *administrador*, *invitado*, etc. Las listas de contraseñas predeterminadas están ampliamente disponibles en Internet.
 Palabras de diccionario: *León*, *América*, *Tigre*, *Barcelona*, Alfa, etc., incluidas palabras en diccionarios que no están en español.
 Las palabras con números añadidos: *contraseña1*, *ciervo2000*, *juan1234*, etc., se pueden probar fácilmente de forma automática con poca pérdida de tiempo.
 Las palabras con una simple ofuscación: *contraseñ@*, *3liel*, *pez dorad0*, etc., se pueden probar automáticamente con poco esfuerzo adicional. Por ejemplo, una contraseña de administrador de dominio comprometida en el ataque de DigiNotar fue supuestamente *Pr0d@dm1n*.
 Palabras duplicadas: *cangrejocangrejo*, *altoalto*, *arbolarbol*, *fútbolfútbol*, etc.
 Secuencias comunes de una fila de teclado: *qwerty*, *123456*, *cachufala*, *eliel*, etc.
 Secuencias numéricas basadas en números bien conocidos como 911 (9-1-1, 9/11), 314159... (pi), 27182... (e), 112 (1-1-2), etc.
 Identificadores: *chernández123*, *13/2/1977*, *555–1234*, el nombre de usuario, etc.
 Contraseñas débiles en idiomas distintos del español, como contraseña (inglés) y ji32k7au4a83 (codificación de teclado bopomofo del chino).
 Cualquier cosa relacionada personalmente con un individuo: número de placa, número de seguro social, números de teléfono actuales o pasados, identificación del estudiante, dirección actual, direcciones anteriores, fecha de nacimiento, equipo deportivo, nombres/apodos/cumpleaños/iniciales de familiares o mascotas, etc. ser probado fácilmente de forma automática después de una simple investigación de los detalles de una persona.
 Fechas: las fechas siguen un patrón y hacen que su contraseña sea débil.

Hay muchas otras formas en que una contraseña puede ser débil, que corresponden a las fortalezas de varios esquemas de ataque; El principio fundamental es que una contraseña debe tener una alta entropía (generalmente se considera que es equivalente a la aleatoriedad) y no ser fácilmente derivable mediante ningún patrón "inteligente", ni deben mezclarse las contraseñas con información que identifique al usuario. Los servicios en línea a menudo proporcionan una función de restauración de contraseña que un pirata informático puede descubrir y, al hacerlo, puede omitir una contraseña. La elección de preguntas de restauración de contraseña difíciles de adivinar puede proteger aún más la contraseña.

 Repensar las pautas de cambio de contraseña
En diciembre de 2012, William Cheswick escribió un artículo publicado en la revista ACM que incluía las posibilidades matemáticas de lo fácil o difícil que sería descifrar contraseñas que se construyen utilizando los estándares comúnmente recomendados y, a veces, seguidos en la actualidad. En su artículo, William mostró que una contraseña alfanumérica estándar de ocho caracteres podía soportar un ataque de fuerza bruta de diez millones de intentos por segundo y permanecer ininterrumpida durante 252 días. Diez millones de intentos por segundo es la tasa aceptable de intentos utilizando un sistema de múltiples núcleos al que la mayoría de los usuarios tendrían acceso. También se podría lograr un grado mucho mayor de intentos, a una velocidad de 7 mil millones por segundo, cuando se utilizan GPU modernas. A este ritmo, la misma contraseña alfanumérica completa de 8 caracteres podría romperse en aproximadamente 0.36 días (es decir, 9 horas). Aumentar la complejidad de la contraseña a una contraseña alfanumérica completa de 13 caracteres aumenta el tiempo necesario para descifrarla a más de 900000 años a 7000 millones de intentos por segundo. Esto es, por supuesto, asumiendo que la contraseña no usa una palabra común que un ataque de diccionario podría romper mucho antes. El uso de una contraseña de esta fortaleza reduce la obligación de cambiarla con la frecuencia que requieran muchas organizaciones, incluido el gobierno de los Estados Unidos, ya que no podría romperse razonablemente en un período de tiempo tan corto.

 Política de contraseñas
Una política de contraseñas es una guía para elegir contraseñas satisfactorias. Está destinado a:

 Ayudar a los usuarios a elegir contraseñas seguras.
 Asegúrese de que las contraseñas sean adecuadas para la población objetivo.
 Proporcionar recomendaciones para los usuarios con respecto al manejo de sus contraseñas.
 Imponer un requisito para cambiar cualquier contraseña que se haya perdido o comprometida, y tal vez que ninguna contraseña se use más de un tiempo limitado.
 (En algunos casos) prescriben el patrón de caracteres que deben contener las contraseñas.
 Use una lista negra de contraseñas para bloquear el uso de contraseñas débiles o fáciles de adivinar.

Por ejemplo, la caducidad de la contraseña suele estar cubierta por las políticas de contraseñas. La caducidad de la contraseña tiene dos propósitos:

 Si se estima que el tiempo para descifrar una contraseña es de 100 días, los tiempos de expiración de la contraseña de menos de 100 días pueden ayudar a garantizar que el atacante no disponga de tiempo suficiente.
 Si una contraseña se ha visto comprometida, exigir que se cambie con regularidad debería limitar el tiempo de acceso del atacante.

Sin embargo, la caducidad de la contraseña tiene sus inconvenientes:

 Pedir a los usuarios que cambien las contraseñas con frecuencia fomenta contraseñas simples y débiles.
 Si uno tiene una contraseña realmente segura, no tiene mucho sentido cambiarla. Cambiar contraseñas que ya son seguras presenta el riesgo de que la nueva contraseña sea menos segura.
 Es probable que un atacante utilice inmediatamente una contraseña comprometida para instalar una puerta trasera, a menudo mediante la escalada de privilegios. Una vez que esto se logra, los cambios de contraseña no evitarán el acceso de futuros atacantes.
 Pasar de no cambiar nunca la contraseña a cambiar la contraseña en cada intento de autenticación (intentos de aprobación o falla) solo duplica la cantidad de intentos que el atacante debe realizar en promedio antes de adivinar la contraseña en un ataque de fuerza bruta. Se gana mucha más seguridad simplemente aumentando la longitud de la contraseña en un carácter que cambiando la contraseña en cada uso.

 Crear y manejar contraseñas
Las contraseñas más difíciles de descifrar, para una longitud y un conjunto de caracteres determinados, son las cadenas de caracteres aleatorias; si el tiempo suficiente, resisten los ataques de fuerza bruta (porque hay muchos personajes) y los ataques de adivinación (debido a la alta entropía). Sin embargo, estas contraseñas suelen ser las más difíciles de recordar. La imposición de un requisito para tales contraseñas en una política de contraseñas puede alentar a los usuarios a escribirlas, almacenarlas en dispositivos móviles o compartirlas con otros como una protección contra fallas de memoria. Si bien algunas personas consideran que cada uno de estos recursos de usuarios aumenta los riesgos de seguridad, otros sugieren lo absurdo de esperar que los usuarios recuerden contraseñas complejas distintas para cada una de las docenas de cuentas a las que acceden. Por ejemplo, en 2005, el experto en seguridad Bruce Schneier recomendó escribir la contraseña:

Las siguientes medidas pueden aumentar la aceptación de requisitos de contraseñas seguras, si se utilizan con cuidado:

 Un programa de entrenamiento. Además, formación actualizada para quienes no sigan la política de contraseñas (contraseñas perdidas, contraseñas inadecuadas, etc.).
 Recompensar a los usuarios de contraseñas seguras reduciendo la tasa o eliminando por completo la necesidad de cambios de contraseña (caducidad de la contraseña). La solidez de las contraseñas elegidas por el usuario se puede estimar mediante programas automáticos que inspeccionan y evalúan las contraseñas propuestas al establecer o cambiar una contraseña.
 Mostrar a cada usuario la fecha y hora del último inicio de sesión con la esperanza de que el usuario pueda notar un acceso no autorizado, sugiriendo una contraseña comprometida.
 Permitiendo a los usuarios restablecer sus contraseñas a través de un sistema automático, lo que reduce el volumen de llamadas a la mesa de ayuda. Sin embargo, algunos sistemas son en sí mismos inseguros; por ejemplo, las respuestas fáciles de adivinar o investigar a las preguntas de restablecimiento de contraseñas evitan las ventajas de un sistema de contraseñas seguro.
 Utilizando contraseñas generadas aleatoriamente que no permitan a los usuarios elegir sus propias contraseñas, o al menos ofreciendo contraseñas generadas aleatoriamente como opción.

 Técnicas de memoria
Las políticas de contraseñas a veces sugieren técnicas de memoria para ayudar a recordar contraseñas:

 Contraseñas mnemónicas: algunos usuarios desarrollan frases mnemotécnicas y las utilizan para generar contraseñas más o menos aleatorias que, sin embargo, son relativamente fáciles de recordar para el usuario. Por ejemplo, la primera letra de cada palabra en una frase memorable. La investigación estima que la fuerza de la contraseña de tales contraseñas es de aproximadamente 3.7 bits por carácter, en comparación con los 6.6 bits de las contraseñas aleatorias de caracteres imprimibles ASCII. Los tontos son posiblemente más memorables. Otra forma de hacer que las contraseñas que aparecen al azar sean más memorables es usar palabras aleatorias o sílabas en lugar de letras elegidas al azar.
 Mnemotécnicos posteriores al hecho: después de que se haya establecido la contraseña, invente un mnemónico que encaje. No tiene que ser razonable o sensato, solo memorable. Esto permite que las contraseñas sean aleatorias.
 Representaciones visuales de contraseñas: una contraseña se memoriza basándose en una secuencia de teclas presionadas, no en los valores de las teclas en sí, por ejemplo, una secuencia! qAsdE #2 representa un romboide en un teclado estadounidense. El método para producir tales contraseñas se llama PsychoPass; además, estas contraseñas con patrones espaciales se pueden mejorar.
 Patrones de contraseña: cualquier patrón en una contraseña facilita la adivinación (automatizada o no) y reduce el factor de trabajo del atacante.
 Por ejemplo, las contraseñas de la siguiente forma que no distingue entre mayúsculas y minúsculas: consonante, vocal, consonante, consonante, vocal, consonante, número, número (por ejemplo *zowl45*) se denominan contraseñas de Environ. El patrón de caracteres de vocales y consonantes alternas tenía la intención de hacer que las contraseñas fueran más fáciles de pronunciar y, por lo tanto, más memorables. Desafortunadamente, tales patrones reducen severamente la entropía de la información de la contraseña, lo que hace que los ataques de contraseña por fuerza bruta sean considerablemente más eficientes. En el Reino Unido, en octubre de 2005, se recomendó a los empleados del gobierno británico que utilizaran contraseñas de esta forma.

 Protección de contraseñas
Por lo general, se aconseja a los usuarios de computadoras que "nunca escriban una contraseña en ningún lugar, pase lo que pase" y que "nunca utilicen la misma contraseña para más de una cuenta". Sin embargo, un usuario de computadora común puede tener docenas de cuentas protegidas por contraseña. Los usuarios con varias cuentas que necesitan contraseñas a menudo se dan por vencidos y usan la misma contraseña para cada cuenta. Cuando los requisitos de complejidad de contraseñas variadas impiden el uso del mismo esquema (memorable) para producir contraseñas de alta resistencia, a menudo se crearán contraseñas simplificadas para satisfacer requisitos de contraseña irritantes y conflictivos. Se citó a un experto de Microsoft diciendo en una conferencia de seguridad de 2005: "Afirmo que la política de contraseñas debería decir que debe escribir su contraseña. Tengo 68 contraseñas diferentes. Si no puedo escribir ninguna de ellas, adivine qué voy a hacer? Voy a utilizar la misma contraseña en cada uno de ellos".

Hay software disponible para computadoras de mano populares que pueden almacenar contraseñas de numerosas cuentas en forma cifrada. Las contraseñas se pueden cifrar a mano en papel y recordar el método de cifrado y la clave. Incluso una mejor manera es cifrar una contraseña débil con uno de los algoritmos criptográficos o funciones hash comúnmente disponibles y probados y usar el cifrado como contraseña.

Se puede utilizar una única contraseña "maestra" con el software para generar una nueva contraseña para cada aplicación, basada en la contraseña maestra y el nombre de la aplicación. Este enfoque es utilizado por PwdHash de Stanford, Multiplicador de Contraseñas de Princeton, y otros administradores de contraseñas sin estado. En este enfoque, proteger la contraseña maestra es esencial, ya que todas las contraseñas se ven comprometidas si se revela la contraseña maestra y se pierden si la contraseña maestra se olvida o se extravía.

 Administradores de contraseñas

Un compromiso razonable por utilizar una gran cantidad de contraseñas es registrarlas en un programa de administración de contraseñas, que incluye aplicaciones independientes, extensiones de navegador web o un administrador integrado en el sistema operativo. Un administrador de contraseñas permite al usuario utilizar cientos de contraseñas diferentes, y solo tiene que recordar una única contraseña, la que abre la base de datos de contraseñas cifradas. No hace falta decir que esta contraseña única debe ser fuerte y estar bien protegida (no registrada en ninguna parte). La mayoría de los administradores de contraseñas pueden crear automáticamente contraseñas seguras utilizando un generador aleatorio de contraseñas criptográficamente seguro, además de calcular la entropía de la contraseña generada. Un buen administrador de contraseñas proporcionará resistencia contra ataques como el registro de claves, el registro del portapapeles y otras técnicas de espionaje de memoria.

 Véase también
 Keylogger
 Frase de contraseña
 Phishing
 Agujero de seguridad

 Referencias

 Enlaces externos
 RFC 4086: Requisitos de Aleatoriedad para la Seguridad
 Patrones de Contraseña: Los ataques de diccionario de próxima generación
