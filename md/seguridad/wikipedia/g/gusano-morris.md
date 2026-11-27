---
type: Artículo de enciclopedia
title: Gusano Morris
description: El gusano Morris fue el primer ejemplar de malware autorreplicable que afectó a Internet (entonces ARPANET).
resource: https://es.wikipedia.org/wiki/Gusano_Morris
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Gusano_Morris"}
license: CC BY-SA 4.0
id: eswiki-Gusano_Morris
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Gusano Morris

El **gusano Morris** fue el primer ejemplar de malware autorreplicable que afectó a Internet (entonces ARPANET). El 2 de noviembre de 1988, aproximadamente 6000 de los 60 000 servidores conectados a la red fueron infectados por este gusano informático, lo que motivó que se creara el Equipo de Respuesta ante Emergencias Informáticas (CERT, por sus siglas en inglés) en respuesta a las necesidades expuestas durante el incidente.

 Qué ocasionó
Se estima que en ese momento el tamaño de Internet era de unos 60 000 ordenadores, y el gusano afectó cerca de 6 000 sistemas de ordenadores en los Estados Unidos (incluyendo el centro de investigación de la NASA) y dejó casi inútiles algunos de ellos. En realidad nunca se sabrá exactamente cuántas resultaron infectadas porque con el hecho de reiniciar el equipo se eliminaban todos los datos del gusano (y se contenía la infección) así que los afectados son solo un número estimado.

El programa intentaba averiguar las contraseñas de otras computadoras usando una rutina de búsqueda que permutaba los nombres de usuarios conocidos, una lista de las contraseñas más comunes y también búsqueda al azar. Descubrieron que no todas las computadoras eran afectadas, sino que solo se propagó en las computadoras VAX de DEC (Digital Equipment Corp) y las fabricadas por Sun Microsystems, que empleaban Unix.

El programa estaba aprovechando algunos defectos de la versión de la Universidad de Berkeley del sistema UNIX. Integrantes de dicha Universidad y del MIT de Massachusetts y de Purdue intentaron trabajar en forma coordinada para capturar una copia del programa y analizarlo. Casualmente en Berkeley se celebraba la reunión anual de expertos en UNIX la mañana del 3 de noviembre, rápidamente capturaron y diseccionaron al gusano y en la tarde habían distribuido los parches necesarios para cerrar las brechas de seguridad aprovechadas por el gusano. Se trataba de un ejemplo de 99 líneas de código que, aprovechándose de una debilidad de Sendmail, se replicaba de una máquina a otra. Se estableció que la infección no fue realizada por un virus, sino por un programa gusano, diseñado para reproducirse a sí mismo indefinidamente y no para eliminar datos.

No fue programado con intención de causar daño, pero a causa de un bug en su código, los efectos fueron catastróficos para la época. Produjo fallos en cientos de computadoras en universidades, corporaciones y laboratorios de gobierno en todo el mundo antes de que fuera rastreado y eliminado. Era el ataque del que fue llamado «Gusano de Internet», y la prensa cubrió el tema con frases como «el mayor asalto jamás realizado contra los sistemas de la nación». Erradicarlo costó casi un millón de dólares, sumado a las pérdidas por haberse detenido casi toda la red, siendo estimadas las pérdidas totales en 96 millones de dólares (una cifra significativa en aquel momento).

Este primer ataque a la infraestructura computacional de Internet llevó a la creación del CERT (Computer Emergency Response Team), un equipo de respuesta a emergencias en computadoras.

 Autor del gusano

El autor fue Robert Tappan Morris, estudiante de 23 años, que declara haber cometido un error al propagar el gusano. Fue detenido cuando uno de sus amigos habló con el reportero del área de computación del New York Times para intentar convencerlo de que todo había sido un accidente, que el gusano no provocaba daños y que el autor estaba arrepentido.

Creó un programa con gran capacidad de reproducirse, pero jamás pensó que se propagaría tan rápida y extensamente. Su idea no era hacer que las computadoras se ralentizaran, sino que el programa se copiara una vez en cada máquina y luego se escondiera en la red. La motivación de Morris se desconoce, aunque es posible que pretendiera una broma práctica de alta tecnología, aprovechando esos errores.

Un estudio detallado del código del Gusano de Morris viene a demostrar la existencia de dos programadores. Todo parece indicar que Robert Morris utilizó parte de los programas creados por su padre en los años 60: el juego consistía en crear un programa que al reproducirse fuera ocupando toda la memoria, al tiempo que borraba de ella al programa del contrincante. Lo que hizo fue pedirle a su padre, un experto en seguridad de la National Security Agency encargada de romper los códigos, un ejemplar de un artículo clásico en el tema, que el propio padre de Morris y Ken Thompson habían escrito una década antes en Laboratorios Bell, donde su padre fue uno de los desarrolladores del UNIX.

Cada contraseña rota permitía que el gusano penetrara en otras máquinas donde el poseedor de la contraseña tuviera cuentas. Cuando se percató de que su programa estaba propagándose por la red, pidió a un amigo que enviara un correo electrónico pidiendo disculpas y las instrucciones para acabar con el programa. Pero en el caos que se originó, su mensaje de correo electrónico pasó desapercibido.

Según informe de la NASA, algunas editoriales dedicadas al acontecimiento retratan a Morris como un héroe por develar los peligros de una red abierta y en desarrollo.

 Condena
El juicio se realizó en enero de 1990, y aunque sus abogados aseguraban que Morris «intentaba ayudar a la seguridad de Internet cuando su programa se salió de su control por accidente», la fiscalía argumentó que el gusano no se trataba de un error, sino de «un ataque contra el gobierno de los Estados Unidos».

Fue declarado culpable por un jurado federal, lo que se convirtió en la primera condena por la ley de fraudes informáticos de 1986. El juez del caso expresó que no creía que las circunstancias presentaran «fraude y engaño», por lo que lo sentenció a tres años de libertad condicional, 400 horas de trabajo social y una multa de 10.050 dólares.

 Referencias

 Véase también
 Virus Jerusalén
 Virus Brain
 SQL Slammer

 Enlaces externos
 Código fuente del gusano
