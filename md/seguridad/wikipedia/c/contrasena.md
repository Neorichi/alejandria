---
type: Artículo de enciclopedia
title: Contraseña
description: Una contraseña, clave o código de acceso es una forma de autentificación que utiliza información secreta para controlar el acceso hacia algún recurso.
resource: https://es.wikipedia.org/wiki/Contraseña
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Contraseña"}
license: CC BY-SA 4.0
id: eswiki-Contraseña
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Contraseña

Una **contraseña**, **clave** o **código de acceso** es una forma de autentificación que utiliza información secreta para controlar el acceso hacia algún recurso. La contraseña debe mantenerse en secreto ante aquellos a quien no se les permite el acceso. A aquellos que desean acceder a la información se les solicita una clave; si conocen o no conocen la contraseña, se concede o se niega el acceso a la información según sea el caso.

El uso de contraseñas se remonta a la antigüedad: los centinelas que vigilaban una posición solicitaban el «santo y seña» al que quisiera pasar a cierta área. Solamente le permiten el acceso a aquella persona que conoce la seña. Igualmente se utilizaba en las rondas nocturnas cuando se encontraba algún miembro del mismo bando y no ser confundido con enemigo. En la era tecnológica, las contraseñas son usadas comúnmente para controlar el acceso a sistemas operativos de computadoras protegidas teléfonos celulares, decodificadores de TV por cable, cajeros automáticos de efectivo, etc. Un típico ordenador puede hacer uso de contraseñas para diferentes propósitos, incluyendo conexiones a cuentas de usuario, accediendo al correo electrónico de los servidores, accediendo a bases de datos, redes, y páginas web, e incluso para leer noticias en los periódicos (diarios) electrónicos.

En la lengua inglesa se tienen dos denominaciones distintivas para las contraseñas: **password** (palabra de acceso) y **pass code** (código de acceso), donde la primera no implica necesariamente usar alguna palabra existente (sin embargo, es normal emplear alguna palabra familiar o de fácil memorización por parte del usuario), la primera suele asociarse también al uso de códigos alfanuméricos (también llamado **PIT** - *Personal Identification Text*), mientras que la segunda frecuentemente se liga a la utilización de algún código numérico (asimismo llamado **PIN** - *Personal Identification Number*). Esto ocurre igualmente en el habla española, ya que en ocasiones clave y contraseña se usan indistintamente

 Balance entre seguridad y comodidad
Aunque con excepciones, cuanto más cómoda de recordar sea una contraseña implicará una mayor facilidad para un atacante de adivinarla. Es decir, si algún recurso está protegido por una contraseña, entonces la seguridad se incrementa con el consecuente aumento de molestia para los usuarios. El nivel de seguridad es inherente dada una política de contraseñas en particular, que está influida por diversos factores que se mencionarán a continuación. Sin embargo, no existe un método único que sea pues el mejor para definir un balance adecuado entre la seguridad y comodidad de acceso directo ante todo.

Algunos sistemas protegidos por contraseñas plantean pocos o ningún riesgo a los usuarios si estos se revelan, por ejemplo, una contraseña que permita el acceso a la información de un sitio web gratuito. Otros plantean un modesto riesgo económico o de privacidad, por ejemplo, una **contraseña** utilizada para acceder al **correo electrónico**, o alguna contraseña para algún teléfono celular. Aun así, en otras situaciones, puede tener consecuencias severas, si la contraseña es revelada. Por ejemplo, como las situaciones para limitar el acceso de expedientes sobre tratamientos del sida o el control de estaciones de energía.

 Factores en la seguridad de un sistema de contraseñas
La seguridad de un sistema protegido por contraseña depende de varios factores. El sistema debe estar diseñado para sondear la seguridad (Ver seguridad e inseguridad de computadoras). Aquí se presentan algunos problemas sobre la administración de contraseñas que deben ser considerados:

 Posibilidad de que algún atacante pueda adivinar o inventar la contraseña
La posibilidad de que algún atacante pueda proporcionar una contraseña que adivinó es un factor clave al determinar la seguridad de un sistema. Algunos sistemas imponen un límite de tiempo después de que sucede un pequeño número de intentos fallidos de proporcionar la clave. Al no tener otras vulnerabilidades, estos sistemas pueden estar relativamente seguros con simples contraseñas, mientras estas no sean fácilmente deducibles, al no asignar datos fácilmente conocidos como nombres de familiares o de mascotas, el número de matrícula del automóvil o contraseñas sencillas como "*administrador*" o "*123456*".

Otros sistemas almacenan o transmiten una pista a modo de sugerencia de recordatorio de la contraseña, de manera que la propia pista puede ser fundamental para el acceso de algún atacante. Cuando esto ocurre, (y suele ser común), el atacante intentará suministrar contraseñas frecuentemente en una alta proporción, quizás utilizando listas extensamente conocidas de contraseñas comunes. También están sujetas a un alto grado de vulnerabilidad aquellas contraseñas que se usan para generar claves criptográficas, por ejemplo, cifrado de discos, o seguridad wifi, por lo tanto son necesarias contraseñas más inaccesibles en estos casos.

 Formas de almacenar contraseñas
Algunos sistemas almacenan contraseñas como archivos de texto. Si algún atacante gana acceso al archivo que contienen las contraseñas, entonces todas estas se encontrarán comprometidas. Si algunos usuarios emplean diferentes cuentas, éstas estarán comprometidas de igual manera. Los mejores sistemas almacenan las contraseñas en una forma de protección criptográfica, así, el acceso a la contraseña será más difícil para algún espía que haya ganado el acceso interno al sistema, aunque la validación todavía sigue siendo posible.

Un esquema criptográfico común almacena solamente el texto de la contraseña codificado, conocido como *hash*. Cuando un usuario teclea la contraseña en este tipo de sistema, se genera a partir de la contraseña y mediante un algoritmo el código hash equivalente para esa contraseña, y si el resultante (hash) coincide con el valor almacenado, se permite el acceso al usuario.

El texto codificado de la contraseña se crea al aplicar una función criptográfica usando la contraseña y normalmente, otro valor conocido como *salt* en inglés. El *salt* previene que los atacantes construyan una lista de valores para contraseñas comunes. Las funciones criptográficas más comunes son la MD5 y SHA1. Una versión modificada de DES fue utilizada en los primeros sistemas Unix.

Si la función que almacena la contraseña está bien diseñada, no es computacionalmente factible revertirla para encontrar el texto directamente. Sin embargo, si algún atacante gana acceso a los valores (y muchos sistemas no los protegen adecuadamente), puede usar gran cantidad de herramientas disponibles para comparar los resultados cifrados de cada palabra dentro de una colección, como un diccionario. Están ampliamente disponibles largas listas de contraseñas posibles en muchos lenguajes y las herramientas intentarán diferentes variaciones
uestran con su existencia la relativa fortaleza de las diferentes opciones de contraseña en contra de ataques. El uso derivado de una función para una clave puede reducir este riesgo
Desafortunadamente, existe un conflicto fundamental entre el uso de estas funciones y la necesidad de un reto de autenticación; este último requiere que ambas partes se pueden una a otra para conocer el secreto compartido (es decir, la contraseña), y al hacer esto, el servidor necesita ser capaz de obtener el secreto compartido en su forma almacenada. En los sistemas Unix al hacer una autenticación remota, el secreto compartido se convierte en la forma burda de la contraseña, no la contraseña en sí misma; si un atacante puede obtener una copia de la forma burda de la contraseña, entonces será capaz de acceder al sistema remotamente, incluso sin tener que determinar cuál fue la contraseña original.

 Método de retransmisión de la contraseña al usuario
Las contraseñas pueden ser vulnerables al espionaje mientras son transmitidas a la máquina de autenticación o al usuario. Si la contraseña es llevada como señal eléctrica sobre un cableado no asegurado entre el punto de acceso del usuario y el sistema central que controla la base de datos de la contraseña, está sujeta a espionaje por medio de métodos de conexiones externas en el cableado. Si esta es enviada por medio de Internet, cualquier persona capaz de ver los paquetes de información que contienen la información de acceso puede espiar la contraseña con pocas posibilidades de detección. Los cable módem pueden ser más vulnerables al espionaje que DSL los módems y las conexiones telefónicas, el ethernet puede estar o no sujeto a espionaje, dependiendo particularmente de la opción del hardware de la red y del cableado. Algunas organizaciones han notado un incremento significativo de las cuentas robadas después de que los usuarios se conecten por medio de conexiones por cable.

El riesgo de intercepción de las contraseña mandadas por Internet pueden ser reducidos con una capa de transporte de seguridad (TLS - Transport Layer Security, previamente llamada SSL) que se integra en muchos navegadores de Internet. La mayoría de los navegadores muestran un icono de un candado cerrado cuando el TLS está en uso. Vea criptografía para otras maneras en las que pasar la información puede ser más seguro.

 Procedimientos para cambiar las contraseñas
Usualmente, un sistema debe proveer una manera de cambiar una contraseña, ya sea porque el usuario sospeche que la contraseña actual ha (o ha sido) descubierto, o como medida de precaución. Si la nueva contraseña es introducida en el sistema de una manera no cifrada, la seguridad puede haberse perdido incluso antes de que la nueva contraseña haya sido instalada en la base de datos. Si la nueva contraseña fue revelada a un empleado de confianza, se gana poco. Algunas páginas web incluyen la opción de recordar la contraseña de un usuario de una manera no cifrada al mandárselo por correo electrónico.

Los *Sistemas de Administración de Identidad*, se utilizan cada vez más para automatizar la emisión de reemplazos para contraseñas perdidas. La identidad del usuario se verifica al realizar algunas preguntas y compararlas con las que se tienen almacenadas. Preguntas típicas incluyen las siguientes: "¿Dónde naciste?", "¿Cuál es tu película favorita?", "¿Cuál es el nombre de tu mascota?" En muchos casos las respuestas a estas preguntas pueden ser adivinadas, determinadas con un poco de investigación, u obtenidas a través de estafa con ingeniería social. Mientras que muchos usuarios han sido advertidos para que nunca revelen su contraseña, muy pocos consideran el nombre de su película favorita para requerir este tipo de seguridad.

 Longevidad de una contraseña
El forzar a los usuarios a que cambien su contraseña frecuentemente (ya sea semestralmente, mensualmente o en lapsos más frecuentes) asegura que una contraseña válida en manos equivocadas sea finalmente inútil. Muchos sistemas operativos proveen esta opción, aunque esta no se usa universalmente. Los beneficios de seguridad son limitados debido a que los atacantes frecuentemente sacan provecho de una contraseña tan pronto como esta es revelada. En muchos casos, particularmente con las cuentas de administradores o cuentas "raíz", una vez que un cracker ha ganado acceso, puede realizar alteraciones al sistema operativo que le permitirán accesos futuros incluso si la contraseña inicial ya ha expirado.

Forzar cambios de contraseña frecuentemente hace que los usuarios tiendan a olvidar cual es la contraseña actual, y por esto se da la consecuente tentación de escribir las claves en lugares a la vista o que reutilicen contraseñas anteriores, lo cual niega cualquier beneficio de seguridad. Al implementar este tipo de política se requiere una cuidadosa consideración de los factores humanos.

 Número de usuarios por cada contraseña
En algunas ocasiones, una sola contraseña controla el acceso de un dispositivo, por ejemplo, para la red de un rúter, o para un teléfono móvil. Sin embargo, en el caso de un sistema informático, una contraseña se almacena generalmente para cada nombre de usuario, de este modo haciendo que todos los accesos puedan ser detectables (excepto, por supuesto, en el caso de usuarios que comparten la misma contraseña).

En estos casos, un usuario potencial debe proporcionar un nombre y una contraseña. Si el usuario provee una contraseña que coincide con el almacenado para el nombre de usuario, entonces se le permite el acceso al sistema del ordenador. Este también es el caso de los cajeros automáticos, con la excepción de que el nombre de usuario es el número de cuenta almacenado en la tarjeta del cliente, y que el PIN es normalmente muy corto (de 4 a 6 dígitos).

La asignación de contraseñas separadas a cada usuario de un sistema es normalmente preferible que hacer que una sola contraseña sea compartida por varios usuarios legítimos del sistema. Esto se da en parte porque la gente está más dispuesta a revelar a otra persona (quién no puede estar autorizada) una contraseña compartida que era exclusivamente para su propio uso. Contraseñas individuales para cada usuario también son esenciales si los usuarios son responsables por sus actividades, tales como en los casos de transacciones financieras o consulta de expedientes médicos.

 Diseño de software protegido
Técnicas comunes utilizadas para mejorar la seguridad de sistemas de software protegidas por contraseñas incluyen:

 No repetir la contraseña en la pantalla de visualización cuando se está accediendo.
 Permitir contraseñas de una longitud adecuada (algunos sistemas de Unix limitan contraseñas a 8 caracteres)
 Obligar a que la contraseña tenga algún carácter especial y algún número
 Requerir a los usuarios volver a ingresar su contraseña después de un período de inactividad.
 Hacer cumplir una política de contraseñas para asegurar contraseñas importantes.
 Requerir periódicamente cambios de contraseña.
 Asignar contraseñas al azar.
 Proveer una opción alternativa al uso de teclados.
 Al cambiar la contraseña, comprobar que no se parece a las contraseñas anteriormente usadas.

 Factores en la seguridad de contraseñas individuales
 Probabilidad que una contraseña pueda ser descubierta
Estudios en la producción de sistemas informáticos han indicado por décadas constantemente que cerca de 40% de las contraseñas elegidas por usuarios se conjeturan fácilmente.

 Muchos de los usuarios no cambian la contraseña que viene predeterminada en muchos de los sistemas de seguridad. Las listas de estas contraseñas están disponibles en Internet.

 Una contraseña puede ser descubierta si un usuario elige como contraseña un dato personal que sea fácil de averiguar (por ejemplo: el número de ID o el número de cuenta de un estudiante, el nombre del novio/a, la fecha de cumpleaños, el número telefónico, etc.). Los datos personales sobre individuos están ahora disponibles en diferentes fuentes, muchas de ellas están en línea, y pueden obtenerse frecuentemente por alguien que use técnicas de ingeniería social, como actuar como un trabajador social que realiza encuestas.

 Una contraseña es vulnerable si puede encontrarse en una lista. Los diccionarios (frecuentemente de forma electrónica) están disponibles en muchos lenguajes, y existen listas de contraseñas comunes.

 En pruebas sobre sistemas en vivo, los ataques de diccionarios son rutinariamente acertados, por lo que el software implementado en este tipo de ataques ya se encuentra disponible para muchos sistemas. Una contraseña muy corta, quizás elegida por conveniencia, es más vulnerable si un hacker puede obtener la versión criptográfica de la contraseña. Las computadoras son en la actualidad lo suficientemente rápidas para intentar todas las contraseñas en orden alfabético que tengan menos de 7 caracteres, por ejemplo:

Una **contraseña débil** sería una que fuese muy corta o que fuese la predeterminada, o una que pudiera adivinarse rápidamente al buscar una serie de palabras que es posible encontrar en diccionarios, nombres propios, palabras basadas en variaciones del nombre del usuario. Una contraseña fuerte debe ser suficientemente larga, al azar, o producirse solo por el usuario que la eligió, de modo tal que el 'adivinarla' requiera un largo tiempo. Ese tiempo 'demasiado largo' variará de acuerdo al atacante, sus recursos, la facilidad con la que la contraseña se pueda descubrir, y la importancia de esta para el atacante. Por lo tanto, una contraseña de un estudiante quizás no valga la pena para invertir más de algunos segundos en la computadora, mientras que la contraseña para acceder al control de una transferencia de dinero del sistema de un banco puede valer varias semanas de trabajo en una computadora.

'Fuerte' y 'débil' tienen significado solamente con respecto a tentativas de descubrir la contraseña de un usuario, ya sea por una persona que conoce al usuario, o una computadora que trate de usar millones de combinaciones. En este contexto, los términos pueden tener una precisión considerable. Pero nótese que una contraseña 'fuerte' en este sentido puede ser robada, truqueada o extraída del usuario ya sea mediante la extracción del historial de un teclado, grabada mediante aparatos de comunicación o copiada de notas dejadas por olvido.

Ejemplos de contraseñas débiles incluyen las siguientes: *administrador*, *123456*, "nombre del usuario", "nombre de la mascota", xx/xx/xx - fechas importantes, ya que la mayoría de estas se encuentran en bases de datos o en diccionarios (dictionary search attack). Según Bruce Schneier, la contraseña más utilizada es *password1*.

Ejemplos de contraseñas fuertes serían las siguientes: *tastywheeT34*, *partei@34!* y *#23kLLflux*. Estas contraseñas son largas y usan combinaciones de letras mayúsculas y minúsculas, de números y de símbolos. No pueden hallarse fácilmente en listas de contraseñas y son suficientemente largas para provocar que una búsqueda burda resulte impráctica en la mayor parte de los casos. Nótese que algunos sistemas no permiten símbolos como #, @ y ! en contraseñas y son más difíciles de encontrar en algunos teclados diseñados para ciertos países. En estos casos, agregar uno o dos caracteres (letra o número) puede ofrecer una seguridad equivalente. También es importante observar que, a partir de la publicación en Internet de este texto que está usted leyendo, estos ejemplos específicos de contraseñas ya no resultarán buenas opciones: ejemplos de discusiones públicas sobre contraseñas son buenos candidatos para incluirse en las listas de diccionarios para atacar sistemas.

El método más efectivo para generar contraseñas es seleccionar suficientes caracteres al azar, aunque este tipo de contraseñas son las más difíciles de recordar. Algunos usuarios desarrollan frases o palabras compuestas que tienen letras al azar como iniciales de varias palabras. Otra manera de elaborar contraseñas al azar que sean más memorables es usar palabras al azar o sílabas en lugar de letras al azar.

En ocasiones se recomienda el uso de recuerdos personales, es decir, elementos o datos que sean memorables para una persona en particular pero no para otras. Por ejemplo: la contraseña *yt21cvpppv* es difícil de recordar, pero se deriva de la frase "Yo tenía 21 cuando visité París por primera vez", posiblemente muy fácil de recordar para el usuario que vivió esa experiencia. Sin embargo, si la primera visita a París fue un hecho muy trascendente para un usuario en particular, es posible que otra persona que conozca a ese usuario y sepa de la importancia que para él tuvo ese viaje pueda adivinar más o menos fácilmente la contraseña y, por lo tanto, esta no sería una opción sensata para utilizarse como contraseña.

 Probabilidad de que una contraseña pueda ser recordada
Las contraseñas más seguras son largas, y con caracteres al azar. Con un mismo número de caracteres, la contraseña será más fuerte (ofrecerá mayor seguridad al usuario) si incluye una mezcla de mayúsculas y minúsculas, números y otros símbolos (cuando es posible utilizar estos últimos). Desafortunadamente, desde la perspectiva de seguridad, estos tipos de contraseña son los más difíciles de recordar.

El forzar a los usuarios a utilizar contraseñas creadas 'al azar' por el sistema asegura que la contraseña no tendrá conexión con el usuario y, por lo tanto, no podrá ser encontrada en ningún diccionario. Varios sistemas operativos incluyen esta opción. Aunque es provechoso desde el punto de vista de seguridad, muchos usuarios evitan tales medidas y la cooperación del usuario es generalmente esencial para un sistema de seguridad.

Los usuarios de computadoras suelen recibir la advertencia en el sentido de que "nunca deben escribir la contraseña en ninguna parte, sin excepción" y de que "nunca deben usar la contraseña para más de una cuenta". Estas declaraciones, aunque suenan bien en teoría, ignoran la realidad de que un usuario de computadoras puede tener docenas de cuentas protegidas por contraseña. Tienen la consecuencia involuntaria de que muchos usuarios seleccionan contraseñas débiles, incluso para cuentas importantes, y terminan por utilizar la misma contraseña en todas ellas.

Si el usuario escribe las contraseñas en algún lugar para poder recordarlas posteriormente, no deberá guardarlas en lugares obvios (agendas, debajo de los teclados, al reverso de las fotografías, etc.). La peor ubicación (y, sin embargo, la más común) es en una nota pegada en la computadora. Las cajas con candado para objetos valiosos son una mejor opción para el resguardo de información importante como las contraseñas. Existe software disponible para computadoras portables (palm, computadoras portátiles muy pequeñas) que almacenan las contraseñas de numerosas cuentas de manera cifrada. Otra opción puede ser elegir una sola contraseña para cuentas de poca importancia, y elegir contraseñas más rigurosas para un menor número de aplicaciones relevantes como las cuentas de banco en línea.

En una conferencia de seguridad en 2005, un experto de Microsoft declaró: "*Creo que la política sobre contraseñas debería decir que ustedes deban escribir sus contraseñas en algún lugar para recordarlas posteriormente. Yo tengo 68 contraseñas diferentes. Si no se me permite escribirlas en algún lugar, ¿adivinen que es lo que voy a hacer? Voy a usar la misma contraseña en cada una de mis cuentas*."

¿Qué es más desventajoso? ¿Usar contraseñas débiles fáciles o usar contraseñas fuertes pero escritas en algún lugar visible? Este dilema puede provocar un gran debate entre los expertos. La seguridad práctica requiere a menudo alcanzar un equilibrio entre los requisitos de conflicto y los factores humanos.

 Probabilidad de que una contraseña sea descubierta
Las contraseñas pueden ser descubiertas mediante navegación en la red, robo, extorsión, allanamiento, amenazas u otros métodos. La búsqueda en los contenedores de basura ha resultado ser fructífera en situaciones donde se desechan datos importantes sin suficiente precaución (como se ha probado recientemente con el reciente robo de identidades). El número de caracteres de una contraseña no sólo puede ser determinado al espiar la pantalla del usuario, sino también al contar el número de clics al teclear una contraseña. Una investigación publicada por IBM en 2004 muestra que cada tecla de un teclado tiene un sonido distintivo, lo que permite tonalizar datos, incluidas las contraseñas, para que puedan ser recuperadas al analizar grabaciones de un dispositivo de sonido o *bug* (véase Criptoanálisis acústico).

El obtener contraseñas mediante manipulación psicológica de los usuarios es un ejemplo de ingeniería social. Un atacante puede telefonear a un usuario y decir: "Hola, le hablamos de Control de Sistemas. Estamos haciendo una prueba de seguridad. ¿Puede proporcionarme su contraseña para que podamos proceder?" Los administradores de sistema y demás personal de soporte técnico casi nunca necesitan conocer la contraseña de un usuario para poder realizar sus trabajos. Los administradores de sistema con privilegios de "raíz" o incluso sus superiores pueden cambiar las contraseñas de los usuarios sin su permiso, así que no tienen necesidad de requerirlas. Además, éstos evitarán pedir las contraseñas, precisamente porque no desean crear el hábito de revelar las contraseñas a cualquiera.

 Otras alternativas para control de acceso
Las numerosas maneras en las que las contraseñas reusables pueden comprometer la seguridad han impulsado el desarrollo de otras técnicas. Desafortunadamente, ninguna se ha vuelto tan disponible universalmente para los usuarios que buscan una alternativa más segura.

Contraseñas de un solo uso Tener contraseñas que solamente son válidas en una ocasión (OTP) hace que los ataques potenciales resulten ineficaces. Aunque para la mayoría de los usuarios las contraseñas de un solo uso resultan extremadamente inconvenientes, se han implementado ampliamente en la banca personal en línea, donde se les conoce como TANs. Ya que la mayoría de los usuarios sólo realizan un pequeño número de transacciones cada semana, el uso de contraseñas de un solo uso no ha generado insatisfacción en los usuarios en estos casos.

Símbolos de seguridad Son similares a las contraseñas de un solo uso, pero el valor que debe ingresarse aparece en un pequeño F.O.B., y este cambia cada minuto.

Verificación de dos pasos Consiste en el uso de un segundo código el cual es enviado por medio de una llamada o un mensaje de texto a un teléfono móvil proporcionado previamente por el usuario, de este modo la única persona que puede acceder a la cuenta es quien posea la contraseña y el teléfono móvil donde será enviado el código. Existe un inconveniente con este método de acceso ya que está sujeto a la disponibilidad del teléfono. Es decir, en caso de robo, pérdida o se encuentre fuera del área de cobertura no se tendría el segundo código para ingresar. Una solución para este inconveniente es tener registrado un equipo de confianza donde no es necesario ingresar el segundo código y desde este desactivar la verificación de dos pasos. Sitios web que usan este tipo de método de acceso son Facebook y Google.

Mediante dispositivos móviles Existe aplicaciones que permiten enviar una clave encriptada desde un dispositivo móvil a una computadora de escritorio. Contraseña que el sitio web al que se ha tratado de acceder puede reconocer y aceptar, en lugar de tener que tipearla. Algunas de ellas son la desarrollada por la empresa estadounidense *Cleff* y la denominada *LaunchKey*.

Autenticación única El Inicio de Sesión Único (Single Sign-On, SSO) es un procedimiento de autenticación que habilita a un usuario determinado a acceder a varios sistemas con una sola instancia de identificación.

Controles de acceso Se basan en la criptografía pública dominante, es decir, SSH. Las claves necesarias son demasiado grandes para memorizar y deben almacenarse en una computadora local, en un símbolo de seguridad o en un dispositivo de memoria portable, como por ejemplo en una memoria flash o en un disco flexible.

Métodos biométricos Permiten la personalización basándose en características personales inalterables, aunque en la actualidad tienen altas tasas de error y requieren hardware adicional para escaneo de rasgos corporales (por ejemplo, las huellas digitales, el iris ocular, etc.). Un ejemplo de esto es la aplicación móvil *OneID*, diseñada para sistemas *Single Sign-On*. Una coalición de empresas denominada *Alianza Fido*, se dedica a proveer y suministrar soluciones de este tipo. Un ejemplo es *YubiKey*, producido por *Yubico*, una empresa afiliada a la Alianza Fido.

Mediante onda cerebrales Científicos de un laboratorio de la Universidad de California están, a fines de 2013, trabajando en un dispositivo que mide las ondas cerebrales y prescinde de cualquier otro método de identificación. Este consiste en un «auricular simple y económico».

 Las contraseñas en la ficción
Las contraseñas aparecen con mucha frecuencia en la ficción, sobre todo en la ciencia ficción. Las siguientes son algunas de las más conocidas:

 *¡Ábrete, sésamo!*: Contraseña para abrir la caverna del cuento árabe anónimo *Alí Babá y los cuarenta ladrones*.
 *Rumpelstiltskin*: Nombre del duende mágico *Rumpelstiltskin*, del cuento del mismo nombre.
 Otros ejemplos: Cuando Harry Potter proporciona una contraseña a una pintura mágica para entrar a su dormitorio.
 En la película o libro del Señor de los Anillos cuando Gandalf quiere entrar en Minas Moria y la palabra clave para ingresar es «Mellon»

 Véase también
 Clave
 Número de identificación personal  (PIN)
 Texto de identificación personal (PIT)
 Contraseñas shadow
 Hacker
 Criptografía
 John the Ripper
 Generador aleatorio de contraseñas

 Referencias

 Bibliografía
 Burnett, Mark. *Perfect Passwords*. Syngress; 1a edición, 200 páginas (1 de noviembre de 2005) ISBN 1-59749-041-5
 Burnett, Mark. *Hacking the Code: ASP.NET Web Application Security*. Syngress; 1a edición, 472 páginas (mayo de 2004) ISBN 1-932266-65-8

 Enlaces externos

 La contraseña Perfecta
 ¿Cómo crear contraseñas seguras?
 Ataques comunes y sus soluciones (en inglés)
 Generador de Contraseñas Seguras
 Generador de Contraseñas Fáciles de Recordar
 Auditar contraseña wifi segura
 Generador online de contraseñas
