---
type: Artículo de enciclopedia
title: Radia Perlman
description: Radia Joy Perlman (1951, Portsmouth, Virginia) es una creadora de software e ingeniera de redes, experta, más conocida como la Madre de Internet.
resource: https://es.wikipedia.org/wiki/Radia_Perlman
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Radia_Perlman"}
license: CC BY-SA 4.0
id: eswiki-Radia_Perlman
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Radia Perlman

- **Lugar de nacimiento:** Portsmouth, Virginia
- **Nacionalidad:** Estadounidense
- **Ocupación:** Ingeniera de redes
- **Premios:** Ver sección Premios
- **Descripción:** Radia Joy Perlman

**Radia Joy Perlman** (1951, Portsmouth, Virginia) es una creadora de software e ingeniera de redes, experta, más conocida como la *Madre de Internet*. Actualmente trabaja para Dell EMC en Seattle, Estados Unidos, y anteriormente estuvo trabajando para Intel, para la que consiguió más de 47 patentes.

Como estudiante de pregrado, Perlman aprendió a programar robots a muy corta edad. Recibió su primer trabajo remunerado en 1971 como programadora a tiempo parcial para el Laboratorio LOGO en el (entonces) Laboratorio de Inteligencia Artificial del MIT, desarrollando software de sistemas de programación como los depuradores.

Trabajando bajo la supervisión de Seymour Papert, desarrolló una versión amigable para los niños del lenguaje de programación educativo para robótica LOGO, llamado TORTIS ("Toddler's Own Recursive Turtle Interpreter System"). Durante la investigación realizada en 1974–76, los niños pequeños, el menor de 3 años y medio, programaron un robot educativo LOGO llamado Turtle. Perlman ha sido descrita como una pionera en la enseñanza de programación para niños pequeños.

Como graduada de matemáticas en MIT, necesitaba encontrar un asesor para su tesis y se unió al grupo del LLUC PACHUC en BBN Technologies. Allí se involucró por primera vez en el diseño de protocolos de red. Perlman obtuvo un grado y un master en matemáticas. Obtuvo un doctorado en ciencias de la computación por el MIT en 1988. Su tesis doctoral en el MIT abordó el problema del enrutamiento cuando se producen fallos de red maliciosos y han sido la base para la mayor parte del trabajo en este campo.

Cuando estudiaba en el MIT a finales de los 60, era una de las aproximadamente 50 mujeres estudiantes, en una clase de aproximadamente 1,000 estudiantes. Para empezar, el MIT solo tenía un dormitorio para mujeres, lo que limita la cantidad de estudiantes que podían estudiar. Cuando las residencias para hombres en el MIT se convirtieron en mixtas, Perlman se mudó de las residencias para mujeres a una residencia mixta, donde se convirtió en la "mujer residente". Más tarde dijo que estaba tan acostumbrada al desequilibrio de género, que se volvió normal. Solo cuando vio a otras estudiantes entre una multitud de hombres, se dio cuenta de que "parecía un poco raro".

 Carrera
Famosa por ser la creadora del protocolo Spanning Tree (STP), mientras trabajó en Digital Equipment Corporation; el protocolo es fundamental para permitir la redundancia de rutas en las redes de área local (LAN). Perlman es autora de un libro de texto sobre redes y coautora de otro sobre seguridad de redes. Tiene más de 100 patentes emitidas. Fue miembro de Sun Microsystems y ha impartido cursos en la Universidad de Washington, la Universidad de Harvard y el MIT, y ha sido ponente principal en eventos en todo el mundo. Perlman ha sido galardonada con premios tales como los premios a los logros de toda una vida de USENIX y el SIGCOMM. Ha realizado numerosas contribuciones en otras áreas creando y estandarizando protocolos.

 Spanning Tree Protocol
Perlman inventó el algoritmo de STree y el protocolo Spanning Tree (STP). Mientras trabajaba como consultora en Digital Equipment Corporation (DEC) en 1984, se le asignó la tarea de desarrollar un protocolo sencillo que permitiera a los puentes de la red ubicar bucles en una red de área local (LAN). Se requería que el protocolo usara una cantidad constante de memoria cuando se implementara en los dispositivos de la red, sin importar el tamaño de la red. Construir y expandir redes puenteadas fue difícil porque los bucles, donde más de una ruta lleva al mismo destino, podrían provocar el colapso de la red. Las rutas redundantes en la red significaban que un puente podría enviar una trama en múltiples direcciones. Por lo tanto, los bucles podrían hacer que las tramas Ethernet no lleguen a su destino, inundando la red. Perlman utilizó el hecho de que los puentes tenían direcciones MAC únicas de 48 bits, y diseñó un protocolo de red para que los puentes dentro de la LAN se comunicaran entre sí. El algoritmo implementado en todos los puentes de la red permitió que los puentes designaran un puente raíz en la red. Cada puente luego mapeo la red y determinó la ruta más corta al puente raíz, desactivando otras rutas redundantes. A pesar de las preocupaciones de Perlman porque el protocolo Spanning Tree tardo aproximadamente un minuto en reaccionar cuando ocurrían cambios en la topología de la red, en el momento en el que un bucle podía interrumpir la red, el Instituto de Ingeniería Eléctrica y Electrónica lo estandarizó como 802.1D (IEEE). Perlman dijo que los beneficios del protocolo equivalen al hecho de que "no hay que preocuparse por la topología de la red" al cambiar la forma en que una LAN está interconectada. Sin embargo, Perlman ha criticado que se hicieron cambios en el transcurso de la estandarización del protocolo.

Del artículo "An Algorithm for Distributed Computation of a Spanning Tree in an Extended LAN": Enlace

 Algorhyme

 I think that I shall never see
 A graph more lovely than a tree.

 A tree whose crucial property
 Is loop-free connectivity.

 A tree which must be sure to span
 So packets can reach every LAN.

 First the root must be selected.
 By ID it is elected.

 Least cost paths from root are traced.
 In the tree these paths are placed.

 A mesh is made by folks like me
 Then bridges find a spanning tree.

 Bibliografía

Perlman es autora de dos libros sobre redes que aún no están traducidos al español.

 Premios
 2017 – Fellow of the Association for Computing Machinery, clase de 2016.
 2016 – National Inventors Hall of Fame induction.
 2014 – Internet Hall of Fame induction.
 2010 – Premio SIGCOMM.
 2006 – Lifetime Achievement Award—“the Flame”—USENIX por *En particular, reconoció el trabajo de la Dr. Perlman en el desarrollo del algoritmo de árbol de expansión que es de rigor en todos los productos de LAN hoy en día.*
 2005 – Anita Borg Institute Women of Vision Award por *Innovaciones en seguridad de redes, tecnologías de enrutamiento y otras contribuciones fundamentales para el funcionamiento y la expansión de Internet.*
 2003 – Silicon Valley Intellectual Property Law Association, *Inventors of the year*.
 2000 – Royal Institute of Technology, *Honorary Doctorate*. - (28 de junio de 2000)
 1997   – Nombrada por segunda ocasión una de las 20 personas más influyentes en la industria en el 25 aniversario de la revista *Data Communications* (sólo ella ha sido nombrada en dos ocasiones). – (15 de enero de 1997)
 1992   – Nombrada una de las 20 personas más influyentes en la industria en el 20 aniversario de la revista *Data Communications*. – (15 de enero de 1992)

 Referencias

 Enlaces externos
En español
 Artículo en El País sobre Radia Perlman *No me gustan los ordenadores, son demasiado frágiles*  29 de enero de 2009
 Artículo en El País en colaboración con Vodafone. Radia Perlman: *A todo el mundo le gusta culpar a los usuarios*  4 de septiembre de 2015
En inglés
 Biografía de Radia Perlman en 'Sun Microsystems'
 Patentes en 'Sun Microsystems'
 Inventor of the Week archive at MIT: Spanning Tree Algorithm
