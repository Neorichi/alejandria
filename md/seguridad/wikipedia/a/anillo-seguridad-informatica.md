---
type: Artículo de enciclopedia
title: Anillo (seguridad informática)
description: "En ciencias de la computación, los dominios de protección jerárquica, con frecuencia llamados anillos de protección, son mecanismos para proteger datos y funcionalidad de los fallos (tolerancia a fallos) y …"
resource: https://es.wikipedia.org/wiki/Anillo_(seguridad_informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Anillo_(seguridad_informática)"}
license: CC BY-SA 4.0
id: eswiki-Anillo_(seguridad_informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Anillo (seguridad informática)

En ciencias de la computación, los **dominios de protección jerárquica**, con frecuencia llamados **anillos de protección**, son mecanismos para proteger datos y funcionalidad de los fallos (tolerancia a fallos) y comportamiento malicioso (seguridad de computadores). Este enfoque es diametralmente opuesto a la de la seguridad basada en capacidad.

Los sistemas operativos proporcionan diferentes niveles de acceso a los recursos. Un anillo de protección es uno de dos o más niveles jerárquicos o capas de privilegios dentro de la arquitectura de un sistema de computación. Esto es generalmente impuesto por el *hardware* por algunas arquitecturas de CPU que ofrecen diferentes modos de CPU en el chip o a nivel de microcódigo. Los anillos están dispuestas en una jerarquía desde los más privilegiados (de más confianza), usualmente numerado cero, hasta el menos privilegiado (de menos confianza), usualmente con el mayor número de anillo. En la mayoría de sistemas operativos, el anillo 0 es el nivel con la mayoría de los privilegios e interactúa más directamente con el *hardware*, como la CPU y la memoria.

Se proporcionan puertas especiales entre los anillos para permitir a un anillo exterior acceder a los recursos de un anillo interior de una manera predefinida, en vez de permitir un uso arbitrario. El correcto acceso por puertas entre los anillos puede mejorar la seguridad previniendo que los programas de un anillo o nivel de privilegio, mal usen los recursos destinados a los programas en otro anillo. Por ejemplo, se debe evitar que el programa espía corra como un programa de usuario en el anillo 3 y que así pueda encender una cámara web sin informar al usuario, puesto que el acceso al *hardware* debe ser una función reservada del anillo 1 para los controladores de dispositivos. Los programas como navegadores web corriendo en los anillos de números más altos, deben solicitar el acceso a la red, un recurso restringido a un anillo de numeración inferior.

 Implementaciones

Los anillos soportados en hardware fueron algunos de los conceptos más revolucionarios introducidos por el sistema operativo Multics, un altamente seguro predecesor de la familia UNIX de sistemas operativos de hoy. Sin embargo, la mayoría de los sistemas de propósito general usan solo dos anillos, incluso si el hardware en el que corren proporciona más modos de CPU. Por ejemplo, Windows XP y anteriores solo usa dos anillos, con el anillo 0 correspondiente al modo de núcleo y el anillo 3 para el modo de usuario.

Muchas modernas arquitecturas de CPU (incluyendo la popular arquitectura x86 de Intel) incluyen alguna forma de protección de anillo, aunque el sistema operativo Windows NT, al igual que el Unix, no explota plenamente esta característica. El OS/2 lo hizo hasta cierto punto, ya que usa tres anillos: el anillo 0 para el código del núcleo y los controladores de dispositivos, el anillo 2 para el código privilegiado (programas de usuario con permisos de acceso de entrada/salida) y el anillo 3 para el código sin privilegios (casi todos los programas de usuario). Bajo DOS, el núcleo, los controladores y las aplicaciones típicamente se ejecutan en el anillo 3, mientras que los manejadores de memoria del 386, como el EMM386 corren en el anillo 0. Adicionalmente, el EMM386 3.xx del DR-DOS puede correr opcionalmente algunos módulos (como el DPMS) en el anillo 1. OpenVMS usa cuatro modos de llamadas (en orden decreciente de privilegios): núcleo, ejecutivo, supervisor y usuario.

Ha habido un renovado interés en esta estructura de diseño, con la proliferación del software hipervisor Xen, el debate en curso sobre el núcleo monolítico o el micronúcleo (particularmente en grupos de noticias Usenet y foros de Internet), la estructura de diseño del anillo 1 de Microsoft como parte de su iniciativa NGSCB y los hipervisores empotrados en el *firmware*, como el Intel VT-x (anteriormente Vanderpool).

El original sistema Multics tenía ocho anillos, pero muchos sistemas modernos tienen menos. El hardware es consciente en todo momento del anillo actual del hilo de la instrucción que se está ejecutando, gracias a registros de máquina especiales. En algunos sistemas, las áreas de memoria virtual son asignadas en hardware a números de anillos. Un ejemplo es el Data General Eclipse MV/8000, en el que los tres primeros bits del PC sirve como el registro de anillo. Por lo tanto el código ejecutando con el PC Virtual PC en 0xE200000, estaría automáticamente en el anillo 7, por ejemplo, y llamar a una subrutina en una sección diferente de la memoria automáticamente causaría una transferencia de anillo.

El hardware restringe severamente las maneras en que el control puede ser pasado de un anillo a otro, y también impone restricciones en los tipos de acceso a la memoria que pueden ser hechos a través de los anillos. Típicamente hay una puerta especial o instrucción de llamada que transfiere el control de una manera segura hacia puntos de entrada predefinidos en anillos de menor nivel (de más confianza), esto funciona como una llamada de supervisor en muchos sistemas operativos que usan la arquitectura de anillo. Las restricciones de hardware están diseñadas para limitar las oportunidades para violaciones accidentales o maliciosas de seguridad. Además, el anillo más privilegiado puede tener capacidades especiales, (como el direccionamiento de memoria real que pasa por encima del hardware de memoria virtual).

En algunos sistemas, la protección del anillo puede ser combinada con los modos del procesador (maestro/núcleo/modo privilegiado versus esclavo/usuario/modo no privilegiado). Los sistemas operativos que corren en hardware que soporta ambas pueden usar las dos formas de protección o solo una.

El uso eficaz de la arquitectura de anillo requiere una estrecha cooperación entre el hardware y el sistema operativo. Los sistemas operativos diseñados para trabajar en múltiples plataformas de hardware pueden hacer solo un uso limitado de los anillos si no están presentes en cada una de las plataformas soportadas. Con frecuencia, el modelo de seguridad es simplificado a "núcleo" y "usuario", incluso si el hardware ofrece una granularidad más fina a través de anillos.

 Modo supervisor

El modo de supervisor es una bandera mediado por el *hardware* que puede ser cambiado por código corriendo en el software de nivel de sistema. Las tareas o hilos a nivel de sistema tendrán esta bandera activado mientras se están ejecutando, mientras que las aplicaciones en el espacio de usuario no. Esta bandera determina si sería posible ejecutar operaciones de código máquina como la modificación de registros para varias tablas de descriptores, o llevar a cabo operaciones tales como deshabilitar las interrupciones. La idea de tener dos modos diferentes para operar viene de "con más control, viene más responsabilidad" - se confía que nunca falle un programa en el modo supervisor, ya que un fallo puede provocar que todo el sistema operativo del computador falle y se detenga.

El modo supervisor es "un modo de ejecución en algunos procesadores que activa la ejecución de todas las instrucciones, incluyendo las privilegiadas. También puede dar acceso a un espacio de direcciones diferente, al hardware de manejo de memoria y otros periféricos. Este es el modo en que usualmente corre el sistema operativo".

En un núcleo monolítico, el sistema operativo corre en modo supervisor y las aplicaciones corren en modo de usuario. Otros tipos de sistemas operativos, como los que tienen un exonúcleo o micronúcleo no necesariamente comparten este comportamiento.

Algunos ejemplos del mundo del PC:

 Linux y Windows son dos sistemas operativos que usan supervisor/modo de usuario. Para realizar funciones especializadas, el código de modo de usuario debe realizar una llamada al sistema dentro del modo de supervisor o incluso al espacio del núcleo donde el código de confianza del sistema operativo llevará a cabo la tarea necesaria y retornará al espacio de usuario.

 DOS, así como otros sistemas operativos simples, y muchos dispositivos empotrados corren en el modo de supervisor permanentemente, lo que significa que los controladores pueden ser escritos directamente como programas de usuario. (Mientras no sean cargados manejadores de memoria 386 como el EMM386)

La mayoría de los procesadores tienen al menos dos modos diferentes. Los procesadores x86 tienen cuatro modos diferentes divididos en cuatro diferentes anillos. Los programas que corren en el anillo 0 pueden hacer cualquier cosa con el sistema, y el código que se ejecuta en anillo 3 debería ser capaz de fallar en cualquier momento sin que ello afecte al resto del sistema de computador. Los anillos 1 y 2 son raramente usados, pero puede ser configurados con diferentes niveles de acceso.

El cambio de "modo de usuario" a "modo núcleo" es, en la mayoría de los sistemas existentes, muy costoso. Se ha medido que, en la solicitud básica de getpid, cuesta entre 100 y 1500 ciclos en la mayoría de las máquinas. De ellos solo alrededor de 100 son para el swith real (70 desde el espacio del usuario al espacio del núcleo, y 40 de regreso), el resto es "sobrecoste para el núcleo". En el micronúcleo tipo L3 la minimización de esta sobrecarga reduce el coste total a alrededor de 150 ciclos.

Maurice Wilkes escribió: ... it eventually became clear that the hierarchical protection that rings provided did not closely match the requirements of the system programmer and gave little or no improvement on the simple system of having two modes only. Rings of protection lent themselves to efficient implementation in hardware, but there was little else to be said for them. [...] The attractiveness of fine-grained protection remained, even after it was seen that rings of protection did not provide the answer... This again proved a blind alley...

 ... con el tiempo quedó claro que la protección jerárquica que los anillos proporcionan no siempre concuerda con las exigencias del programador de sistema, y tener dos modos únicos en el sistema simple, dio poca o ninguna mejora. Anillos de protección se prestan a una implementación eficiente en el hardware, pero había poco más que decir acerca de ellos. [...] El atractivo de la protección de granular fina se mantuvo, incluso después de que se ha visto que los anillos de protección no direon la respuesta ... Esto de nuevo resultó ser un callejón sin salida...

Para ganar rendimiento y determinismo, algunos sistemas colocan las funciones que probablemente serían vistas como lógica de aplicación, en vez de como controladores de dispositivo, en modo núcleo; aplicaciones de seguridad (control de acceso, cortafuegos, etc.), y los monitores del sistema operativo son citados como ejemplos. Por lo menos un sistema de manejador de base de datos empotrado, eXtremeDB Kernel Mode, ha sido desarrollado específicamente para la implementación de modo de núcleo, para proporcionar una base de datos local para las funciones de aplicación basadas en el núcleo, y para eliminar los cambios de contexto que de lo contrario ocurren cuando interactúan las funciones del núcleo con un sistema de base de datos corriendo en modo usuario.

También está a la inversa. El núcleo Linux, por ejemplo, se inyecta una sección VDSO en los procesos que contiene funciones que requerirían normalmente una llamada al sistema, es decir, un anillo de transición. Pero en vez de hacer una llamada al sistema, estas funciones usan datos estáticos proporcionados por el núcleo que evitan la necesidad de una transición de anillo, lo que es más ligero que una llamada al sistema. La función gettimeofday puede ser proporcionada de esta manera.

 Modo de hipervisor

Los procesadores de Intel y AMD ofrecen instrucciones x86 de virtualización para que un hipervisor controle el acceso del *hardware* al anillo 0. A pesar de que son mutuamente incompatibles, tanto VT-x de Intel (nombre en clave "Vanderpool") como el AMD-V (nombre en clave "Pacifica") crea un nuevo anillo 1 para que un sistema operativo invitado pueda ejecutar operaciones de anillo 0 de forma nativa sin afectar a otros SO invitados o al sistema operativo anfitrión.

 Interoperatividad entre la CPU y los niveles de abstracción del sistema operativo

Muchas arquitecturas de hardware de CPU proporcionan mucha más flexibilidad de la que es explotada por los sistemas operativos que normalmente corren en ellas. El uso adecuado de los modos complejos de la CPU requiere una cooperación muy estrecha entre el sistema operativo y la CPU, y por lo tanto tiende a pegar el sistema operativo a la arquitectura de CPU. Cuando el sistema operativo y la CPU están diseñados específicamente el uno para el otro, esto no es un problema (aunque algunas de las características de *hardware* todavía puede dejarse sin explotar), pero cuando el sistema operativo está diseñado para ser compatible con arquitecturas múltiples, diferentes arquitecturas de CPU , una gran parte de las características de los modos de CPU pueden ser ignoradas por el sistema operativo. Por ejemplo, la razón por la que Windows usa solo dos niveles (anillo 0 y anillo 3) es que algunas arquitecturas de hardware que fueron soportadas en el pasado (como PowerPC o MIPS) implementaron solo dos niveles de privilegio.

Multics fue un sistema operativo diseñado específicamente para una arquitectura de CPU especial (que a su vez fue diseñada específicamente para Multics), y aprovechó completamente la ventaja de los modos de la CPU a su disposición. Sin embargo, fue una excepción a la regla. Hoy en día, este alto grado de interoperabilidad entre el sistema operativo y el *hardware* no suele ser rentable, a pesar de las ventajas potenciales para la seguridad y la estabilidad.

En última instancia, el propósito de distintos modos de operación para la CPU es proporcionar protección de hardware contra la corrupción accidental o deliberada del ambiente del sistema por el programa (y las correspondientes infracciones de la seguridad del sistema). Solo se les permite ejecutar en el ambiente sin restricciones de modo de núcleo a porciones de *software* del sistema de confianza, y entonces solo cuando sea absolutamente necesario. Todos los otros programas se ejecutan en uno o más modos de usuario. Si un procesador genera un fallo o condición de excepción en un modo de usuario, en la mayoría de los casos la estabilidad del sistema no se ve afectada, si un procesador genera un fallo o condición de excepción en el modo de núcleo, la mayoría de los sistemas operativos detendrán el sistema con un error no recuperable. Cuando una jerarquía de modos existe (seguridad basada en anillos), los fallos y excepciones en un nivel de privilegio solo puede desestabilizar los niveles de privilegios de numeraciones superiores. Por lo tanto, un fallo en el anillo 0 (el modo de núcleo con el más alto privilegio) estrellará todo el sistema, pero un fallo en el anillo 2 solo afectará a los anillos de 3 y siguientes y al anillo 2, a lo sumo.

Las transiciones entre los modos están a discreción del hilo en ejecución cuando la transición es desde un nivel de privilegio alto a uno de bajo privilegio (como desde el núcleo para los modos de usuario), pero las transiciones de menor a mayor nivel de privilegio puede tener lugar solo a través de puertas seguras controladas por *hardware* que son atravesadas ejecutando instrucciones especiales, o cuando son recibidas interrupciones externas.

Sistemas operativos de micronúcleo tratan de minimizar la cantidad de código que se ejecuta en modo privilegiado, a los fines de la seguridad y elegancia, pero en última instancia, sacrificando el rendimiento.

 Referencias

 Lectura adicional

 David T. Rogers:  Thesis, June 2003 (pdf)
 Glossary of Multics acronyms and terms: Ring
 William J. Caelli:  2002 (pdf)
 Haruna R. Isa, William R. Shockley, Cynthia E. Irvine: A Multi-threading Architecture for Multilevel Secure Transaction Processing 1999 (pdf)
 Ivan Kelly: Report Porting MINIX to Xen  2006
 Paul Barham, Boris Dragovic, Keir Fraser, Steven Hand, Tim Harris, Alex Ho, Rolf Neugebauer, Ian Pratt, Andrew Warfield: Xen and the Art of Virtualization 2003 (pdf)
 Marcus Peinado, Yuqun Chen, Paul England, and John Manferdelli: NGSCB: A Trusted Open System (pdf)
 Michael D. Schroeder, Jerome H. Saltzer: A Hardware Architecture for Implementing Protection Rings 1972 (pdf)
 Intel Architecture Software Developer's Manual Volume 3: System Programming (Order Number 243192) Chapter 4 Protection; section 4.5 Privilege levels. (pdf)
 Tzi-cker Chiueh, Ganesh Venkitachalam, Prashant Pradhan: Integrating segmentation and paging protection for safe, efficient and transparent software extensions 1999 Chapter 3: Protection hardware features in Intel X86 architecture; section 3.1 Protection checks. (pdf)
 Takahiro Shinagawa, Kenji Kono, Takashi Masuda: Exploiting Segmentation Mechanism for Protecting Against Malicious Mobile Code 2000 chapter 3 Implementation; section 3.2.1 Ring Protection (pdf)
 Boebert, William Earl and R. Kain. *A Practical Alternative to Hierarchical Integrity Policies*. Proceedings of the 8th National Computer Security Conference, 1985.
 Gorine, Andrei and Krivolapov, Alexander. Kernel Mode Databases: A DBMS technology for high-performance applications, *Dr. Dobb's Journal*, May, 2008.

 Véase también

 Llamada al sistema
 Modo protegido (Modo en los CPUs compatibles x86 de la serie 80286 o posterior)
 Multics
