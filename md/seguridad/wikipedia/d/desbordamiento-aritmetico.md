---
type: Artículo de enciclopedia
title: Desbordamiento aritmético
description: "En programación, se produce un desbordamiento de enteros cuando una operación aritmética intenta crear un valor numérico que está fuera del rango que puede representarse con un número dado de dígitos, ya sea mayor que …"
resource: https://es.wikipedia.org/wiki/Desbordamiento_aritmético
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Desbordamiento_aritmético"}
license: CC BY-SA 4.0
id: eswiki-Desbordamiento_aritmético
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Desbordamiento aritmético

En programación, se produce un **desbordamiento de enteros** cuando una operación aritmética intenta crear un valor numérico que está fuera del rango que puede representarse con un número dado de dígitos, ya sea mayor que el máximo o menor que el mínimo valor representable.

El resultado más común de un desbordamiento es que se almacenan los dígitos representables menos significativos del resultado; se dice que el resultado se *envuelve* alrededor del máximo (es decir, el resultado obtenido se corresponde a aplicar el módulo del máximo admisible, una potencia entera de la base interna de cálculo, generalmente dos en las computadoras modernas, pero a veces diez u otro número).

Una condición de desbordamiento puede dar resultados que conducen a un comportamiento no deseado. En particular, si no se ha anticipado esta posibilidad, el desbordamiento puede comprometer la fiabilidad de un programa y su seguridad.

Para algunas aplicaciones, como los temporizadores y los relojes, puede ser conveniente ajustar el desbordamiento. El estándar C11 indica que para enteros sin signo, el ajuste de módulo es el comportamiento definido y el término desbordamiento nunca se aplica: "un cálculo que involucre operandos sin signo nunca puede desbordarse".

En algunos procesadores como las tarjetas gráficas (GPUs) y procesadores digitales de señales (DSPs) que soportan aritmética de saturación, los resultados desbordados se "fijan", es decir, se establecen en el valor mínimo o máximo del rango representable, en lugar de modularse con respecto al máximo.

Origen
La arquitectura interna de un procesador determina el rango de valores que se pueden representar en sus registros. Aunque la gran mayoría de las computadoras pueden realizar aritmética de precisión múltiple con los operandos de la memoria, lo que permite que los números sean arbitrariamente largos y se eviten los desbordamientos, el ancho del registro limita el tamaño de los números individuales que pueden operarse (por ejemplo, sumar o restar) usando una instrucción única por operación. Los anchos de registro binarios típicos para enteros sin signo incluyen:

 8 bits: valor máximo representable 28 - 1 = 255
 16 bits: valor máximo representable 216 - 1 = 65,535
 32 bits: valor máximo representable 232 - 1 = 4,294,967,295 (el ancho más común para computadoras personales a comienzos de los años 2000)
 64 bits: valor máximo representable 264 - 1 = 18,446,744,073,709,551,615 (el ancho más común para los procesadores de las computadoras personales hacia 2020),
 128 bits: valor máximo representable 2128 - 1 = 340,282,366,920,938,463,374,607,431,768,211,455

Cuando una operación aritmética produce un resultado mayor que el máximo anterior para un entero de N bits, un desbordamiento reduce el resultado al módulo de la N-ésima potencia de 2, reteniendo solo los bits menos significativos del resultado y provocando una *vuelta total*.

En particular, multiplicar o sumar dos enteros puede resultar en un valor que es inesperadamente pequeño, y restar de un entero pequeño puede causar un ajuste a un valor positivo grande (por ejemplo, la suma de enteros de 8 bits 255 + 2 da como resultado 1, que es  y, de manera similar, la resta 0 - 1 da como resultado 255, una representación complemento a dos de −1).

Dicha *envolvente* puede causar problemas de seguridad: si se utiliza un valor desbordado como el número de bytes para asignar a un búfer, el búfer se asignará de forma inesperadamente pequeña, lo que podría provocar un desbordamiento del búfer que, dependiendo de su uso, podría a su vez causa la ejecución de código arbitrario.

Si la variable es del tipo entero con signo, un programa puede suponer que una variable siempre contiene un valor positivo. Un desbordamiento de enteros puede hacer que el valor se ajuste y se vuelva negativo, lo que viola la suposición del programa y puede conducir a un comportamiento inesperado (por ejemplo, la adición de enteros de 8 bits de 127 + 1 da como resultado −128, un complemento de dos de 128). Una solución para este problema en particular es usar tipos de enteros sin signo para los valores que un programa espera y asume que nunca serán negativos.

Banderas
La mayoría de las computadoras tienen dos indicadores del procesador dedicados para verificar las condiciones de desbordamiento.

La bandera de acarreo se activa cuando el resultado de una suma o resta, considerando los operandos y el resultado como números sin signo, no cabe en el número dado de bits. Esto indica un desbordamiento con un acarreo del bit más significativo. Una operación inmediatamente posterior a "agregar con acarreo" o "restar con préstamo" usaría el contenido de este indicador para modificar un registro o una ubicación de memoria que contenga la parte superior de un valor de varias palabras.

La bandera de desbordamiento también se activa cuando el resultado de una operación en números con signo no tiene el signo que se podría predecir a partir de los signos de los operandos, por ejemplo, un resultado negativo al sumar dos números positivos. Esto indica que se ha producido un desbordamiento y que el resultado presentado (el complemento a dos), no coincide con el resultado verdadero, que no cabría en el número dado de bits.

Variaciones de definición y ambigüedad

Para un tipo sin signo, cuando el resultado ideal de una operación está fuera del rango de los tipos representables y el resultado devuelto se obtiene mediante ajuste, entonces este evento se define comúnmente como un desbordamiento.

En contraste, el estándar C11 define que este evento no es un desbordamiento y establece que "un cálculo que involucre operandos sin signo nunca puede desbordarse".

Cuando el resultado ideal de una operación de enteros está fuera del rango de los tipos representables y el resultado devuelto se obtiene mediante fijación, entonces este evento se define comúnmente como una saturación.

El uso varía según si una saturación es o no un desbordamiento.
Para eliminar esta ambigüedad, pueden usarse los términos desbordamiento
y saturación.

El término *subdesbordamiento* se usa más comúnmente para las matemáticas de punto flotante y no para la aritmética de enteros.
Sin embargo, se pueden encontrar muchas referencias a este concepto para enteros.
Cuando se utiliza el término de *subdesbordamiento* de un entero, significa que el resultado ideal estaba más cercano a menos infinito, que el valor representable del tipo de salida más cercano a menos infinito.

Cuando se utiliza el término subdesbordamiento entero, puede incluir todos los tipos de desbordamientos o solo los casos en los que el resultado ideal queda más cercano al infinito positivo que el valor representable del tipo de salida más cercano al infinito positivo.

Cuando el resultado ideal de una operación no es un entero exacto, el significado de desbordamiento puede ser ambiguo en los casos límite.

Considérese el caso donde el resultado teórico tiene un valor 127.25 y el valor máximo representable del tipo de salida es 127. Si el desbordamiento se define como el valor ideal que está fuera del rango representable del tipo de salida, este caso se clasificaría como un desbordamiento.

Para las operaciones que tienen un comportamiento de redondeo bien definido, la clasificación de desbordamiento puede necesitar posponerse hasta que se aplique el redondeo.

El estándar C11 define que las conversiones de punto flotante a entero deben redondearse hacia cero. Si se usa C para convertir el valor de coma flotante 127.25 a entero, entonces se debe aplicar primero el redondeo para obtener una salida de entero ideal de 127. Dado que el entero redondeado está en el rango de salidas, el estándar C no clasificaría esta conversión como un desbordamiento.

Métodos para mitigar problemas de desbordamiento de enteros

Hay varios métodos de manejo de desbordamiento:

 Evitación: Al asignar variables con tipos de datos que son lo suficientemente grandes como para contener todos los valores que posiblemente puedan computarse y almacenarse en ellos, siempre es posible evitar el desbordamiento. Incluso cuando el espacio disponible o los tipos de datos fijos proporcionados por un lenguaje de programación o entorno son demasiado limitados para permitir que las variables se asignen *defensivamente* con tamaños generosos, al ordenar cuidadosamente las operaciones y verificar los operandos por adelantado, a menudo es posible asegurar *a priori* que el resultado nunca será mayor de lo que se puede almacenar. Las herramientas de análisis estático de software, las técnicas de verificación formal y el diseño por contrato se pueden utilizar para garantizar de manera más segura y sólida que no se produzca un desbordamiento accidental.
 Manejo: Si se anticipa que podría producirse un desbordamiento, entonces se pueden insertar pruebas en el programa para detectar cuándo sucede y disponer otro procesamiento para mitigarlo. Por ejemplo, si un resultado importante calculado a partir de las entradas del usuario se desborda, el programa puede detenerse, rechazar la entrada y quizás solicitarle al usuario una entrada diferente, en lugar de que el programa continúe con la entrada desbordada no válida y, en consecuencia, no funcione correctamente. Por ejemplo, es posible agregar dos números cada uno de dos bytes de ancho usando solo una adición de bytes en los pasos siguientes: primero agréguense los bytes bajos y luego agréguense los bytes altos, pero si es necesario efectuar un acarreo de los bytes bajos, esto es un desbordamiento aritmético de la adición de bytes y se hace necesario detectar e incrementar la suma de los bytes altos. las CPUs generalmente tienen una forma de detectar esto para admitir la adición de números más grandes que su tamaño de registro, normalmente utilizando un bit de estado; la técnica se llama aritmética de precisión múltiple.
 Propagación: si un valor es demasiado grande para almacenarlo, se le puede asignar un valor especial que indica que se ha producido un desbordamiento y luego todas las operaciones sucesivas devuelven este valor de indicador. Estos valores a veces se denominan NaNs, "no un número" en inglés. Esto es útil para que el problema pueda verificarse una vez al final de un cálculo largo en lugar de después de cada paso. Esto a menudo se admite en el hardware de punto flotante, llamado FPUs.

Los lenguajes de programación implementan varios métodos de mitigación contra un desbordamiento accidental: Ada, Seed7 (y ciertas variantes de lenguajes funcionales), desencadenan una condición de excepción en el desbordamiento, mientras que Python (desde la versión 2.4) convierte a la perfección la representación interna del número para que coincida con su crecimiento, transformándolo a long, cuya capacidad solo está limitada por la memoria disponible.

La implementación de la detección de desbordamiento en tiempo de ejecución UBSan también está disponible para los compiladores de C.

En lenguajes con compatibilidad nativa para precisión arbitraria y seguridad de tipos (como Python o Common Lisp), los números se promueven a un tamaño más grande automáticamente cuando se producen desbordamientos, o se lanzan excepciones (condiciones señaladas) cuando existe una restricción de rango. El uso de dichos idiomas puede ser útil para mitigar este problema. Sin embargo, en algunos de estos lenguajes, las situaciones de rebosamiento de un entero son todavía posibles. Un ejemplo es la optimización explícita de una ruta de código que el gestor de tareas considera un cuello de botella. En el caso de Common Lisp, esto es posible mediante el uso de una declaración explícita para anotar una variable a una palabra de tamaño de máquina (fixnum) y bajando el nivel de seguridad de tipo a cero para un bloque de código particular.

En Java 8, hay métodos para controlar el rebosamiento, por ejemplo, como , que arrojarán  en caso de desbordamiento.

El Equipo de Respuesta ante Emergencias Informáticas (CERT) desarrolló el modelo entero *As-Infinitly Ranged (AIR)*, un mecanismo en gran medida automatizado para eliminar el desbordamiento y el truncado de enteros en C/C++ mediante el manejo de errores en tiempo de ejecución.

En computación gráfica o procesamiento de señales, es típico trabajar con datos que van de 0 a 1 o de −1 a 1. Un ejemplo de esto es una imagen en escala de grises, donde 0 representa negro, 1 representa blanco y los valores intermedios representan distintos tonos de gris. Una operación que se podría querer realizar es iluminar la imagen multiplicando cada píxel por una constante. La aritmética de saturación permite simplemente multiplicar *ciegamente* cada píxel por esa constante sin preocuparse por el desbordamiento, simplemente por mantener un resultado razonable de que todos estos píxeles mayores que 1 (es decir, "más brillantes que el blanco") se vuelven blancos; y todos los valores "más oscuros que el negro", simplemente se vuelven negros.

Ejemplos

El desbordamiento aritmético no anticipado es una causa bastante común de errores de programación. Dichos errores de desbordamiento pueden ser difíciles de descubrir y diagnosticar porque pueden manifestarse solo para conjuntos de datos de entrada muy grandes, que es menos probable que se usen en las pruebas de validación.

Si se toma la media aritmética de dos números al sumarlos y se divide por dos, como se hace en muchos algoritmos de búsqueda, se produce un error si la suma (aunque no la media resultante) es demasiado grande para ser representada y, por lo tanto, se desborda.

 Un desbordamiento aritmético no manejado en el software de dirección del motor fue la causa principal del fracaso del vuelo inaugural del cohete Ariane 5 de la misión Cluster en 1996. El software había sido considerado libre de errores, ya que se había utilizado en muchos vuelos anteriores, pero siempre en el lanzamiento de cohetes más pequeños, con menor aceleración que la del Ariane 5. Frustrantemente, la parte del software en la que se produjo el error de desbordamiento ni siquiera tenía que estar funcionando para el Ariane 5 en el momento en que causó que el cohete fallara; era un proceso de lanzamiento para un antecesor más pequeño del Ariane 5, que había permanecido en el software cuando fue adaptado para el nuevo cohete. Además, la causa real del fallo fue un problema en la especificación de ingeniería de cómo el software debía manejar el desbordamiento numérico cuando se detectara: debía realizar un volcado de diagnóstico a su bus, que se habría conectado al equipo de prueba durante los ensayos del software durante el desarrollo, pero fue conectado a los motores de dirección de los cohetes durante el vuelo. El volcado de datos empujó la boquilla del motor hacia un lado, lo que sacó al cohete del control aerodinámico y precipitó su rápida desintegración en el aire.

 El 30 de abril de 2015, la Administración Federal de Aviación anunció que ordenaba a los operadores del Boeing 787 restablecer su sistema eléctrico periódicamente, para evitar un desbordamiento de enteros que podría provocar la pérdida de energía eléctrica y el accionamiento de la turbina de aire de impacto. Boeing implementó un *parche* informático en el cuarto trimestre de aquel año. La Agencia Europea de Seguridad Aérea hizo lo mismo el 4 de mayo de 2015. El error se produce después de 231 centisegundos (días ), lo que indica un entero con signo de 32 bits.

 Los errores de desbordamiento son evidentes en algunos juegos de ordenador. En el juego de arcade *Donkey Kong*, es imposible avanzar más allá del nivel 22 debido a un desbordamiento de entero en su bonificación por tiempo. El juego toma el número de nivel en el que se encuentra el usuario, lo multiplica por 10 y agrega 40. Cuando alcanzan el nivel 22, el número de tiempo/bonificación es 260, que es demasiado grande para su registro de 256 bits de 8 bits, por lo que se restablece a 0 y otorga los 4 restantes como tiempo/bonificación, demasiado corto para terminar el nivel. En *Donkey Kong Jr. Math*, cuando se intenta calcular un número por encima de 10000, solo se muestran los primeros 4 dígitos. El desbordamiento es la causa del famoso nivel "split-screen" en *Pac-Man* y de "Nuclear Gandhi" en *Civilization*. También causó el mismo problema en "Tierras lejanas" del "Minecraft", que existía desde el período de desarrollo de Infdev hasta la Beta 1.7.3 ; sin embargo, más tarde se reparó en la versión Beta 1.8, pero aún existe en las versiones Pocket Edition y Windows 10 Edition de *Minecraft*. En el juego Super Nintendo Lamborghini American Challenge, el jugador puede hacer que su cantidad de dinero caiga por debajo de $0 durante una carrera al ser multado por el límite del dinero restante después de pagar la tarifa por una carrera. Entonces se produce un error en el número entero y se le otorga al jugador $ 65,535,000 más de lo que hubiera tenido después de volverse negativo. Se produce un fallo similar en , donde el jugador puede caer en una cantidad negativa al viajar rápido sin fondos suficientes, luego proceder al evento donde el jugador es robado y se le ha retirado toda su moneda. Después de que el juego intente llevarse el dinero de los jugadores a una cantidad de 0, al jugador se le otorga 2147482963 en la moneda del juego.

 Microsoft / IBM MACRO Assembler (MASM) Versión 1.00, y probablemente todos los programas creados por el mismo compilador de Pascal, tuvieron un error de signo y de desbordamiento de enteros en el código de configuración de la pila, lo que les impidió ejecutarse en máquinas DOS más recientes o emuladores bajo algunas configuraciones con más de 512 KB de memoria. El programa se cuelga o muestra un mensaje de error y sale a DOS.

 En 2014, el video musical de PSY Gangnam Style recibió tantas vistas en YouTube que rompió el número de audiencia máximo posible dentro de un entero de 32 bits con signo. Posteriormente, YouTube modificó el valor de conteo máximo a un entero de 64 bits.

 En agosto de 2016, una máquina de Casino en Resorts World Casino imprimió un boleto con un premio de $ 42.949.672,76 como resultado de un error de desbordamiento. El Casino se negó a pagar esta cantidad, lo que calificó como un mal funcionamiento, ya que en su defensa la máquina afirmaba claramente que el pago máximo era de $ 10 000, por lo que cualquier premio mayor debía ser el resultado de un error de programación. La Corte Suprema de Iowa falló a favor del Casino.

Véase también
 Desbordamiento de búfer
 Desbordamiento de montículo
 Mezclado de punteros
 Pruebas de software
 Desbordamiento de pila
 Análisis estático de software
 Señal (informática)

Referencias

Enlaces externos
 Phrack # 60, Desbordamientos de enteros básicos
 Phrack # 60, protección de enteros de Big Loop
 Detección eficiente y precisa de ataques basados en enteros
 Clasificación de amenazas WASC - Desbordamientos de enteros
 Comprensión del desbordamiento de enteros en C / C ++
 Binary Overflow - Binary Arithmetic
 ISO C11 estándar
