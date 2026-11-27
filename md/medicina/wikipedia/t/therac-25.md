---
type: Artículo de enciclopedia
title: Therac-25
description: El Therac-25 fue un acelerador lineal de radioterapia producido por AECL, sucesor de los modelos Therac-6 y Therac-20 (las unidades anteriores fueron producidas en asociación con CGR).
resource: https://es.wikipedia.org/wiki/Therac-25
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Therac-25"}
license: CC BY-SA 4.0
id: eswiki-Therac-25
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Therac-25

El **Therac-25** fue un acelerador lineal de radioterapia producido por AECL, sucesor de los modelos Therac-6 y Therac-20 (las unidades anteriores fueron producidas en asociación con CGR). El aparato estuvo comprometido en al menos seis accidentes entre junio de 1985 y enero de 1987, en los que varios pacientes recibieron sobredosis de radiación.

Tres de los pacientes murieron como consecuencia directa en el que para entonces fue el accidente más grave en los 35 años de los aceleradores lineales médicos. Estos accidentes pusieron en duda la fiabilidad del control por *software* de sistemas de seguridad crítica, convirtiéndose en caso de estudio en la informática médica y en la ingeniería de *software*.

 Historia

La empresa francesa CGR fabricó los aceleradores lineales *Neptune* y *Sagittaire*.

A principios de la década de 1970 CGR y la empresa pública canadiense *Atomic Energy Commission Limited* (AECL) colaboraron en la construcción de los aceleradores lineales controlados por una minicomputadora DEC PDP-11: el Therac-6, que producía rayos X de hasta 6 MeV, y el Therac-20, que podía producir rayos X o electrones de hasta 20 MeV. El ordenador añadía cierta facilidad de uso porque el acelerador podía funcionar sin él. CGR desarrolló el software para el Therac-6 y reutilizó algunas subrutinas para el Therac-20.

En 1981 las dos compañías cancelaron su acuerdo de colaboración. AECL desarrolló un nuevo concepto de doble pasada para la aceleración de electrones en un espacio más reducido, cambiando su fuente de energía de klistrón a magnetrón. En ciertas técnicas se utilizan directamente los electrones producidos, mientras que en otras se les hace colisionar contra un blanco (*target*) de número atómico alto para producir haces de rayos X. Este concepto de acelerador dual se aplicó al Therac-20 y al Therac-25, siendo éste mucho más compacto, versátil y fácil de usar. También resultaba más económico para un hospital tener una máquina dual que pudiera aplicar tratamientos de electrones y de rayos X, en vez de dos máquinas.

El Therac-25 se diseñó como una máquina controlada por un ordenador y algunos mecanismos de seguridad pasaron de hardware a software. AECL decidió no duplicar algunos mecanismos de seguridad. AECL reutilizó módulos y rutinas de código del Therac-20 para el Therac-25.

El primer prototipo del Therac-25 se construyó en 1976. Se comenzó a comercializar a finales de 1982.

El software para el Therac-25 fue desarrollado por una persona durante varios años usando lenguaje ensamblador PDP-11. Era una evolución del software del Therac-6. En 1986 el programador abandonó AECL. En un pleito los abogados no pudieron identificar al programador ni conocer su cualificación y experiencia.

Se instalaron 5 máquinas en Estados Unidos y 6 en Canadá.
Tras los accidentes, en 1988 AECL disolvió la sección *AECL Medical* y la empresa *Theratronics International Ltd* se encargó de realizar el mantenimiento de las máquinas Therac-25 instaladas.

 Diseño

La máquina ofrecía dos modos de radioterapia:
 Terapia de haz de electrones directo, que entregaba pequeñas dosis de electrones de alta potencia (de 5 a 25 MeV) por cortos períodos de tiempo.
 Terapia por rayos X de muy alto voltaje (o terapia de fotones), que entregaba rayos X creados mediante colisión de electrones de alta potencia (25 MeV) contra un blanco (*target*), y luego los pasaba por un filtro difusor y un colimador.
También disponía del modo de luz visible (*field light mode*) que permitía ajustar la posición del paciente iluminando la zona de tratamiento con luz visible.
Cuando se operaba en el modo de haz de electrones de baja potencia, ese haz era emitido directamente desde la máquina, propagado hasta obtener una concentración segura mediante escáneres magnéticos. En el modo de rayos X, la máquina estaba diseñada para interponer cuatro componentes en la ruta del rayo de electrones:
 Blanco, que convertía el haz de electrones en rayos X.
 Filtro difusor, que repartía el haz por un área más amplia.
 Juego de bloques movibles (colimador), que daba forma al haz de rayos X para ajustarlo a la zona de tratamiento.
 Cámara de iones de rayos X, que medía la potencia del haz.
El paciente se coloca en una camilla fija. Por encima de él hay una placa giratoria a la que están fijados los componentes que modifican el haz de electrones. La placa giratoria tiene una posición para el modo de rayos X (fotones), otra posición para el modo de electrones y una tercera posición para realizar ajustes mediante luz visible. En esta posición no se espera un haz de electrones, y una luz que se refleja en un espejo de acero inoxidable simula al haz. En esta posición no hay una cámara de iones que actúe como dosímetro de radiación entregada porque no se espera que funcione el haz de radiación.
La placa giratoria tiene unos microinterruptores que indican la posición al ordenador. Cuando la placa está en una las tres posiciones fijas permitidas un émbolo la bloquea por enclavamiento. En este tipo de máquinas tradicionalmente se usaban bloqueos electromecánicos para asegurarse que la placa giratoria estaba en la posición correcta antes de iniciar el tratamiento. En el Therac-25 se sustituyeron por comprobaciones de software.

 Casos
 Kennstone Regional Oncology Center, 1985

Un Therac-25 llevaba funcionando seis meses en Marietta, Georgia, Estados Unidos y el 3 de junio de 1983 aplicó un tratamiento de radioterapia tras una lumpectomía a una mujer de 61 años.
El tratamiento era de 10 MeV de electrones. La paciente sintió un calor abrasador en la zona. En los días siguientes tuvo enrojecimiento de la zona, el hombro se le bloqueó y tuvo espasmos. El enrojecimiento pasó del pecho hacia la espalda, lo que indicaba una quemadura por radiación, pero los médicos no podían explicarla. El físico del hospital consultó a AECL sobre el incidente. Calculó que la dosis aplicada fue entre 15 000 y 20 000 rad (*radiation absorbed dose*) cuando debería haber sido de 200 rad. Una dosis de 1000 rad puede ser mortal para una radiación de cuerpo completo.
En octubre de 1985 la paciente demandó al hospital y al fabricante de la máquina. En noviembre de 1985 AECL fue notificado de la demanda. En marzo de 1986 AECL comunicó a la FDA que había recibido una demanda de la paciente.

Debido a la sobredosis de radiación tuvieron que extirparle el pecho quirúrgicamente, un brazo y hombro quedaron inmovilizados y sufrió dolor constante. La función de impresión de tratamiento no estaba activada en el momento del tratamiento y no quedó registro de los datos de radiación aplicados. Se llegó a un acuerdo extrajudicial para resolver el pleito.
 Ontario Cancer Foundation, 1985

El Therac-25 llevaba funcionando en la clínica seis meses cuando el 26 de julio de 1985 una paciente de 40 años estaba recibiendo su tratamiento número 24 para un cáncer de cuello de útero. El operador activó el tratamiento, pero a los cinco segundos la máquina se paró con el mensaje de error «H-tilt», la indicación de pausa de tratamiento y el dosímetro indicando que no se había aplicado radiación. El operador pulsó la tecla  (*Proceed*: continuar). La máquina se paró otra vez. El operador repitió el proceso cinco veces hasta que la máquina suspendió el tratamiento. Se llamó a un técnico y no encontró ningún problema. La máquina trató otros seis pacientes en el mismo día.

La paciente se quejó de quemazón e hinchazón en la zona y fue hospitalizada el 30 de julio. Se sospechó de una sobredosis de radiación y la máquina fue retirada del servicio. El 3 de noviembre de 1985 la paciente falleció de cáncer, aunque en la autopsia se mencionó que en caso de no haber fallecido entonces, se le habría tenido que colocar una prótesis de cadera debido a los daños de la sobredosis de radiación. Un técnico calculó que recibió entre 13 000 y 17 000 rad.

El incidente se comunicó a la FDA y a la *Canadian Radiation Protection Bureau*.

AECL sospechó que podría haber un error con tres microinterruptores que informaban de la posición de la placa giratoria. AECL no pudo replicar un fallo de los microinterruptores y la prueba del microinterruptor no fue concluyente. AECL cambió el método para que fuera tolerante al fallo de uno de ellos y modificó el software para que comprobara si la placa giratoria se movía o estaba en la posición de tratamiento.

AECL afirmó que las modificaciones suponían un incremento de cinco órdenes de magnitud en la seguridad.

 Yakima Valley Memorial Hospital, 1985

En diciembre de 1985 una mujer desarrolló un eritema con un patrón de bandas paralelas en la zona del tratamiento. El personal del hospital mandó una carta el 31 de enero de 1986 a AECL sobre el incidente. AECL respondió en dos páginas detallando las razones por las que la sobredosis de radiación era imposible en el Therac-25, tanto por fallo de la máquina como por error del operador.

A los seis meses la paciente desarrolló úlceras crónicas bajo la piel por necrosis de tejido. Se le operó y se le colocaron injertos de piel. La paciente siguió viviendo con secuelas menores.

 East Texas Cancer Center, Tyler, marzo de 1986
Durante  dos años trataron a más de 500 pacientes con el Therac-25. El 21 de marzo de 1986 un paciente acudió para su novena sesión de tratamiento para un tumor en la espalda. El tratamiento era de 22 MeV de electrones con una dosis de 180 rad en una zona de 10x17 cm, con una radiación acumulada en 6 semanas de 6000 rad.

La operadora experimentada introdujo los datos de la sesión y se dio cuenta de que había escrito como tipo de tratamiento una X en vez de una E. Con el cursor subió hacia arriba y cambió la X por una E y como el resto de parámetros eran correctos pulsó  hasta bajar a la casilla de órdenes. Todos los parámetros marcaban «Verificado» y se mostraba el mensaje «Rayos preparados». Pulsó la tecla  («Beam on»). La máquina se paró y mostró el mensaje «Malfunction 54» (error 54). También mostró «Treatment pause» (pausa de tratamiento). El manual decía que el mensaje «Malfunction 54» era un error «dose input 2» (dosis de entrada 2). Más adelante un técnico testificó que «dose input 2» significaba que la radiación suministrada era o muy alta o muy baja.

El monitor de radiación (dosímetro) marcaba 6 unidades suministradas cuando había demandado 202 unidades. La operadora pulsó  (*Proceed*: continuar). La máquina se volvió a parar con el mensaje «Malfunction 54» (error 54) y el dosímetro marcó que había entregado menos unidades que las requeridas. La cámara de vigilancia de la sala de radiación estaba desconectada y el interfono se había roto ese día.

Con la primera dosis el paciente sintió como una descarga eléctrica y un crepitar de la máquina. Como era su novena sesión se dio cuenta de que no era normal. Comenzó a levantarse de la mesa para pedir ayuda. En ese momento la operadora pulsó la  para continuar el tratamiento. El paciente sintió una descarga de electricidad por el brazo como si le arrancara la mano. Llegó hasta la puerta y comenzó a golpearla hasta que la abrió la operadora. Inmediatamente fue reconocido por un médico, que observó eritema intenso en la zona, sospechando que había sido una simple descarga eléctrica. Mandó al paciente a casa. El físico del hospital revisó la máquina y como estaba calibrada según las especificaciones siguió tratando pacientes durante todo el día. Lo que no sabían es que el paciente había recibido una dosis masiva de entre 16 500 a 25 000 rad en menos de un segundo sobre un área de un cm². El crepitar de la máquina lo había producido una saturación de las cámaras de ionización, que tuvo como consecuencia que indicaran que la dosis de radiación aplicada había sido muy baja.

Durante las semanas siguientes el paciente tuvo parálisis del brazo izquierdo, náuseas, vómitos y terminó siendo hospitalizado por mielitis de la médula espinal inducida por la radiación. Las piernas, medio diafragma y las cuerdas vocales terminaron paralizadas. Además tuvo recurrentes infecciones de herpes simplex en la piel. Falleció cinco meses después de la sobredosis.

Desde el día siguiente del accidente técnicos de AECL revisaron la máquina y no pudieron replicar el error 54. Comprobaron la toma a tierra de la máquina para descartar la descarga eléctrica como causa. La máquina volvió a estar operativa el 7 de abril de 1986.

 East Texas Cancer Center, Tyler, abril de 1986

El 11 de abril de 1986 un paciente iba a recibir un tratamiento de electrones para un cáncer de piel en la cara. La prescripción era de 10 MeV para un área de 7x10 cm. La operadora era la misma que había en el incidente de marzo, tres semanas antes. Tras rellenar todos los datos del tratamiento se dio cuenta de que tenía que cambiar el modo de X a E. Así lo hizo y pulsó   para bajar a la casilla de órdenes. Como se mostraba «Beam ready» (Rayos listos) pulsó   (*Proceed*: continuar). La máquina se paró produciendo gran ruido, que se oyó por el intercomunicador. Se mostró el error 54. La operadora entró en la sala y el paciente sentía fuego en la cara. El paciente falleció el 1 de mayo de 1986. La autopsia mostró daño por radiación en el lóbulo temporal derecho y en el tronco cerebral.

El físico del hospital suspendió los tratamientos de la máquina y lo comunicó a AECL. Tras un trabajo extenuante el físico y la operadora fueron capaces de reproducir el mensaje de error 54. Determinaron que la rapidez en la edición de la entrada de datos era un factor clave en la producción del error 54. Tras mucha práctica pudo reproducir a voluntad el error 54. En AECL no podían reproducir el error y solo lo consiguieron tras seguir las indicaciones del físico para que la introducción de datos fuera muy rápida.

AECL calculó que la dosis proporcionada en el accidente fue de 25 000 rad.
 Yakima Valley Memorial Hospital, 1987

El 17 de enero de 1987 un paciente iba a recibir un tratamiento con dos exposiciones de verificación de película de 4 y 3 rad y un tratamiento de electrones de 79 rad. Se puso película bajo el paciente y le administraron 4 rad con una apertura de 22x18 cm. La máquina paró, la apertura se abrió hasta 35x35 cm y se administró una dosis de 3 rad. La máquina paró. El operador entró en la sala para retirar las placas de película y ajustar la posición del paciente. Usó el control manual dentro de la sala para ajustar la placa giratoria. Salió de la sala olvidando las placas de película y en la cabina, tras ver el mensaje «Beam ready», pulsó la tecla  para disparar los rayos. Tras 5 segundos la máquina se paró y mostró un mensaje que desapareció rápidamente. Como la máquina estaba en pausa, el operador pulsó  (*Proceed*: continuar). La máquina paró mostrando como razón «Flatness». El operador escuchó al paciente por el intercomunicador y entró a la sala. El paciente había sentido como una quemadura. La pantalla mostraba que solo le habían administrado 7 rad. A las pocas horas el paciente mostró quemaduras en la piel de la zona. Cuatro días más tarde el enrojecimiento de la zona tenía un patrón con bandas similar al producido en el incidente del año anterior y del que no habían hallado la causa. AECL comenzó una investigación, pero no pudo reproducir el fallo.

El físico del hospital realizó pruebas con placas de película. Dos exposiciones con rayos X cuando la placa giratoria estaba en la posición de ajuste con luz visible produjeron unas fotografías similares a las que el operario dejó olvidadas en el día del accidente. El paciente estuvo expuesto entre 8000 y 10 000 rad en lugar de los 86 rad prescritos.
El paciente falleció en abril de 1987 por complicaciones debidas a la sobredosis de radiación. Los familiares presentaron una demanda que terminó con un acuerdo extrajudicial.

 Causas

La comisión investigadora concluyó que las causas primarias de los accidentes fueron malas prácticas de desarrollo, análisis de requerimientos y un mal diseño de *software*, y no por errores aislados en el código fuente. En particular, el programa de la Therac-25 fue diseñado de tal manera que era casi imposible encontrar y subsanar fallos automáticamente.

Los investigadores encontraron otras causas secundarias:
 AECL no mandó revisar el código fuente a una entidad independiente.
 AECL no consideró el diseño del *software* durante su evaluación de posibles fallos y de gestión de riesgos.
 El sistema notificaba un error y detenía los rayos X, pero solamente mostraba el mensaje «*MALFUNCTION*» (error de funcionamiento) seguido de un número del 1 al 64 (relativo al número de canal analógico/digital). El manual de la máquina no explicaba el problema implicado en los códigos de error, y por lo tanto el operario acababa por cerrar la advertencia y proceder con el tratamiento. Un operario reportó que tenía cada día una media de 40 errores «*MALFUNCTION*».
 El personal de AECL, así como los operarios de las máquinas, inicialmente no creían en las quejas de los pacientes; esto podría explicarse por la alta confianza que tenían en la máquina. En los cursos de operación para los operadores AECL enfatizaba que había tantos mecanismos de seguridad que era imposible dar una sobredosis de radiación.

También se encontraron problemas de ingeniería:
 Uno de los fallos sólo ocurría cuando se introducía rápidamente una secuencia particular de teclas en la terminal VT100, que controlaba la computadora PDP-11 de la Therac-25. El operador había rellenado todas las casillas y estaba en la casilla de órdenes cuando se daba cuenta de que había un error en la casilla del tipo de haz que contenía una X (Rayos X) cuando debía contener una E (haz de Electrones). Para corregirlo usaba el cursor  hasta subir a la casilla, escribir una E y bajar con el cursor  hasta la casilla de órdenes, escribir una B y pulsar . La secuencia completa era                       . Si esta secuencia se realizaba en menos de 8 segundos la máquina podía aplicar una radiación de hasta 1000 veces la que se pretendía entregar. Esto ocurría muy raramente y se desconocía que existiera tal error.

 El diseño no contaba con un sistema de seguridad mecánico que previniese que el haz de electrones operase en el modo de alta energía sin el blanco en su posición.
 La ingeniería había reutilizado código de modelos más antiguos, que sí que contaban con sistemas de seguridad mecánicos. Esos dispositivos de seguridad no podían avisar cuando se activaban, por lo que no había sospecha de fallos en el *software*.
 El *software* no podría comprobar que los sensores estuvieran funcionando correctamente (bucle abierto). El fabricante añadió más tarde conmutadores redundantes.
 El proceso del equipamiento de control no se sincronizaba de manera adecuada con el proceso de la interfaz de operario, y por ello ocurrían condiciones de carrera si el técnico cambiaba la configuración rápidamente. Hacer ajustes velozmente era algo improbable durante las pruebas iniciales, ya que los operarios no tenían la suficiente experiencia. El software permitía el acceso concurrente a la memoria compartida y no había una sincronización real aparte de las variables compartidas.
 El programa cambiaba una variable bandera incrementándola, en vez de asignarle un valor fijo. Ocasionalmente ocurría un desbordamiento de variable, haciendo que se ignoraran chequeos de seguridad en ese momento.
 El programa estaba escrito en lenguaje ensamblador, un lenguaje de bajo nivel que requiere más trabajo de diseño, programación y pruebas. Además, se programó sobre un sistema operativo propio.

 Problemas de software

El diseño general de software era inseguro. Entre los errores de software había dos condiciones de carrera.

Cuando la salida o estado de un proceso es dependiente de una secuencia de eventos que se ejecutan en orden arbitrario y van a trabajar sobre un mismo recurso compartido, se puede producir un error cuando dichos eventos no llegan (se ejecutan) en el orden que el programador esperaba. El término se origina por la similitud de dos procesos compitiendo en carrera por llegar antes que el otro, de manera que el estado y la salida del sistema dependerán de cuál llegó antes, pudiendo provocarse inconsistencias y comportamientos impredecibles y no compatibles con un sistema determinista.

 Rutinas de entrada de datos

Los accidentes de Tyler se produjeron por problemas en las rutinas de entrada de datos que permitían ejecutar la prueba de ajuste antes de que todos los parámetros de la prescripción hubieran sido introducidos y comprobados. Era un problema de condición de carrera.

La tarea de monitoreo de tareas («Treat») controlaba las fases del tratamiento ejecutando ocho subrutinas. Se usaba la variable Tphase («Treatment Phase»: fase de tratamiento) que indicaba la fase del tratamiento que debía ejecutarse. Tras la ejecución de una subrutina Treat se reprogramaba a sí misma. La subrutina «Datent» («Data entry»: entrada de datos) se comunicaba con la tarea gestora del teclado («keyboard handler task») mediante la variable compartida «Data-entry completion flag» (bandera de rellenado de la entrada de datos) para determinar si todos los datos de la prescripción habían sido introducidos correctamente. El gestor del teclado reconoce el cumplimentado de los datos de entrada y cambia la variable para indicarlo. Una vez que fija el valor, la subrutina Datent detecta que la variable ha cambiado su estado y entonces cambia el valor de la variable Tphase de 1 (Data Entry:entrada de datos) a 3 (Set-Up Test: prueba de ajuste). En este caso la subrutina Datent sale a la subrutina Treat, que se reprograma a sí misma y comienza la ejecución de la subrutina Set-Up Test. Si la variable (Data entry completion) no se ha movido, Datent no cambia el valor de Tphase y sale hacia el cuerpo principal de Treat. Treat se reprograma a sí misma, esencialmente reprogramando la subrutina Datent.

Una vez que todos los parámetros se han introducido, Datent llama a la subrutina Magnet, que ajusta los imanes en un proceso que dura 8 segundos para tener en cuenta el proceso de histéresis. Magnet llama a una subrutina Ptime que introduce un retraso. Como se necesitan ajustar varios imanes, Ptime entra y sale varias veces. Para indicar el ajuste de imanes una variable bandera se inicializa al entrar a la subrutina Magnet y se pone a 0 a la salida de Ptime. La subrutina Ptime comprueba una variable compartida colocada por el gestor de teclado, que indica la presencia de peticiones de edición. Si hay ediciones, Ptime borra la variable bandera de ajuste de imanes y sale a Magnet, que a su vez sale a Datent. Pero Ptime solo comprueba la variable de edición si la variable de ajuste de imanes está activada. Como Ptime la borra en su primera ejecución, cualquier edición ejecutada en los sucesivos ciclos de Ptime, no será reconocida. Así que cualquier cambio en el modo o en la energía reflejado en la pantalla y en las variables de modo y energía, no será percibido por Datent para que pueda ajustar los parámetros de la máquina.

Parte del problema se arregló tras el accidente cambiando la puesta a cero de la variable de ajuste de imanes al final de la subrutina Magnet (cuando los imanes se habían ajustado) en lugar de al final de la subrutina Ptime.

 Desbordamiento de variable

Este error se dio en los accidentes de Yakima por una condición de carrera en la que falló un mecanismo de seguridad por software que permitió la activación de la máquina en una situación incorrecta.
La función de ajuste con luz visible (*field-light feature*) permite colocar al paciente de forma muy precisa para su tratamiento. Normalmente, el operador introduce los parámetros en la pantalla, entra en la sala y realiza los últimos ajustes manuales. En la pantalla se refleja que hay un estado «no verificado». Tras los ajustes todos los parámetros muestran el mensaje «verificado». El operador pulsa el botón «Set» en el control manual o escribe «Set» en la pantalla. Entonces la máquina colocará el colimador en la posición adecuada para el tratamiento.

En el programa, tras introducir la prescripción y ser verificada por la rutina Datent, la variable de control Tphase se cambia para que se inicie la rutina Set-Up Test. Cada pasada de la rutina Set-Up Test incrementa en 1 la variable compartida Class3. Un valor distinto de 0 indica que hay una inconsistencia y el tratamiento no se debe  producir. Un valor de 0 para Class3 indica que hay consistencia de los parámetros y se pueden disparar los rayos. Tras poner un valor en la variable Class3, la rutina Set-Up Test comprueba errores en el sistema comprobando que la variable compartida F$mal tenga un valor distinto de 0, que indicaría que no está preparada para el tratamiento. Entonces se reprogramaría la subrutina Set-Up Test. Cuando F$mal vale 0 (todo correcto para el tratamiento), la subrutina Set-Up Test hace que la variable Tphase valga 2, lo que hace que reprograme la subrutina Set-Up Done y el tratamiento continúe. El mecanismo de comprobación de enclavamiento lo realiza la tarea concurrente Housekeeper (Hkeper). La comprobación del colimador superior la realiza una subrutina de Hkeper llamada Lmtchk. Lmtchk comprueba primero la variable Class3. Si Class3 contiene algo distinto de 0, Lmtchk llama a la subrutina Chkcol para comprobar el colimador. Si Class3 contiene 0, se puentea Chkcol y no se comprueba la posición del colimador superior. La subrutina Chkcol escribe en el bit 9 de la variable compartida F$mal según la posición del colimador superior (que a su vez es comprobada por la subrutina Set-Up Test de Datent y así puede decidir si se reprograma o si procede con Set-Up Done).

Durante el ajuste de la máquina para una sesión de tratamiento, Set-Up Test se ejecuta cientos de veces porque se reprograma a sí misma esperando que ocurran otros eventos. En el código, la variable Class3 se incrementa 1 en cada pasada de Set-Up Test. Como la variable Class3 tiene 1 byte (8 bits) solo puede contener hasta el valor 255 decimal. Cada 256 pasadas de la rutina Set-Up Test, la variable se desborda y pasa a tener un valor 0 (se pueden aplicar los rayos). Eso significa que cada 256 pasadas de la rutina Set-Up Test, el colimador superior no se comprobará y sus errores no se detectarán.

La sobredosis se producía cuando el operador pulsaba el botón Set (o escribía Set en el teclado) en el preciso instante en el que Class3 se desbordaba y pasaba a 0. Entonces Chkcol no se ejecutaba, y F$mal no se actualizaba para indicar que el colimador superior todavía estaba en la posición de ajuste con luz visible (*Field-light position*). El software conectaba la máxima potencia de 25 MeV sin un blanco (*target*) y sin aplicar un filtro difusor al haz, resultando en un haz de electrones altamente concentrado.

AECL corrigió este problema cambiando la variable Class3 a un valor fijo distinto de 0 (en vez de incrementarla) en cada pasada de la rutina Set-Up Test.

 Lecciones aprendidas

La importancia de la seguridad frente a la facilidad de uso del operador. Hacer una interfaz amigable puede entrar en conflicto con los objetivos de seguridad.
Los accidentes casi nunca son simples. Normalmente implican sucesos interdependientes con factores técnicos, humanos y organizativos.
Uno de los errores más serios es la tendencia a creer que se ha determinado la causa de un accidente sin tener la evidencia adecuada para llegar a esa conclusión (por ejemplo el microinterruptor en el accidente de Hamilton) o sin investigar todos los factores contribuyentes.
Otro error es pensar que la corrección de un error de programación particular prevendrá todos los accidentes futuros.
Los accidentes se suelen atribuir al error humano. Casi todos los factores involucrados se pueden atribuir a fallos humanos. Incluso los fallos por desgaste de material podrían definirse como fallo humano si no se ha dispuesto la redundancia adecuada o no se instruido al personal para mantener y reemplazar las piezas desgastadas. Concluir que un accidente es resultado de un error humano no es significativo ni ayuda mucho.

En los accidentes en sistemas complejos hay que considerar todos los factores contribuyentes. En el Therac-25 fueron:

 Gestión inadecuada y falta de procedimientos para el seguimiento de los incidentes reportados.

 Sobreconfianza en el software y retirada de los bloqueos y enclavamientos físicos convirtiendo al software en un «single point of failure» (punto único de fallo) que puede llevar a un accidente. El software no debe tener la responsabilidad exclusiva de la seguridad.

 Hay una tendencia en los ingenieros a ignorar el software. En la investigación inicial de los incidentes del Therac-25 se supuso que la causa estaba en el hardware y la investigación se centró en el hardware.
 En sistemas de control de procesos un error de software se puede atribuir a un fallo de hardware. Sin una investigación minuciosa con registros de sucesos detallados, no es posible determinar si un sensor proporcionó información errónea, el software ordenó un comando incorrecto o el actuador tuvo un error esporádico.

 No había comprobaciones independientes de que el software estaba operando correctamente. La verificación de todos los errores no puede recaer en los operadores y menos cuando no se les proporcionan los medios para hacerlo. El software del Therac-25 mentía a los operadores y no detectaba que se había producido una sobredosis. Las cámaras de ionización del sistema no podían manejar la alta densidad de ionización de un haz de electrones sin filtro difusor a corrientes altas. Las cámaras de ionización se saturaban e indicaban que se había aplicado una dosis baja. Los ingenieros deben diseñar pensando en el peor caso posible.

 Toda empresa que fabrique equipos de riesgo debe tener registros de incidentes, de riesgo, de trazabilidad y procedimientos de control de calidad.

 Prácticas de ingeniería de software mejorables. La documentación no debe proporcionarse *a posteriori*. Se deben establecer prácticas de control de calidad de software. Los diseños deben mantenerse simples. Desde el principio deben establecerse registros que puedan permitir la trazabilidad y la auditoría de errores. El software debe someterse a pruebas extensas al nivel de módulos. Realizar todas las pruebas en un sistema completo no es adecuado. La reutilización de módulos de software en otro sistema no garantiza la seguridad y puede llevar a diseños peligrosos. El software de procedencia desconocida (SOUP) es el código que no tiene la documentación formal o fue desarrollado por un tercero y no tiene evidencia de los controles establecidos durante su proceso de desarrollo. Este código, por definición, es capaz de producir fallos. Es muy importante llevar a cabo un análisis de riesgos de cualquier código SOUP que se vaya a introducir en un proyecto y justificar las razones para hacerlo.

 Evaluaciones de riesgo no realistas y sobreconfianza en esas evaluaciones. La afirmación de AECL de que la seguridad se había incrementado cinco órdenes de magnitud como resultado del cambio de un microinterruptor tras el accidente de Hamilton es difícil de justificar.

 En los proyectos de seguridad crítica se deben incorporar procedimientos especiales para el análisis de la seguridad y el diseño. La seguridad debe asegurarse incluso cuando haya errores de software. El Therac-20 contenía el mismo error de software que el Therac-25 implicado en las muertes de Tyler, pero tenía los seguros y enclavamientos físicos que mitigaron sus consecuencias. La protección contra los errores de software también puede implementarse en el propio software.

 Obligación de reportar los incidentes a las agencias reguladoras y a otros usuarios del sistema. AECL no reportó los primeros incidentes a los reguladores ni a otros usuarios. Los usuarios mantuvieron al menos tres reuniones para comentar los incidentes y proponer mejoras.

 Secuencia de sucesos principales

Leyenda

 Véase también
 Error de *software*
 Condición de carrera

 *Software* propietario

 Referencias

 Bibliografía
 BAASE, S, "A Gift of Fire", Pearson Prentice Hall, 2008.
 BOWSHER, C .A. Medical device recalls : Examination of selected cases. Technical Report Geport GO/PE MD-9 0 -6, U.S. Government Accounting Organization, 1990.
 KIVEL, M., editor. Radiological Health Bulletin, volume XX: 8. Center for Devices and Radiological Health, Food and Drug Administration, Maryland, 1986.
 LEVESON, Nancy G., TURNER, Clark S., An investigation of the Therac-25 accidents. IEEE Computer, 26(7) 18 - 41, 1993.
 MILLER, Ed, The Therac-25 experience. In Conference of State Radiation Control Program Directors, 1987.
 RAWLINSON, J.A., Report on the Therac-25. In OCTRF/OCI Physicists Meeting , Kingston, Ontario, 1987.
 SALTOS, R., Man killed by accident with medical radiation. Boston Globe, 1986.

 Enlaces externos
 The Therac-25 Accidents (PDF), by Nancy Leveson (the 1995 update of the IEEE Computer article mentioned below)
 Leveson, Nancy G., and Turner, Clark S. (July 1993). "An Investigation of the Therac-25 Accidents," *Computer* (IEEE), *26*(7):18-41.
 Short summary of the Therac-25 Accidents

  Clase universitaria sobre el Therac-25. UC Berkeley CS 61A, 2010
  Presentación del problema del Therac-25
