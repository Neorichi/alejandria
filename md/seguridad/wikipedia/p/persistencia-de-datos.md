---
type: Artículo de enciclopedia
title: Persistencia de datos
description: La persistencia de datos es la representación residual de datos que han sido de alguna manera nominalmente borrados o eliminados.
resource: https://es.wikipedia.org/wiki/Persistencia_de_datos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Persistencia_de_datos"}
license: CC BY-SA 4.0
id: eswiki-Persistencia_de_datos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Persistencia de datos

La **persistencia de datos** es la representación residual de datos que han sido de alguna manera nominalmente borrados o eliminados. Este residuo puede ser debido a que los datos han sido dejados intactos por un operativo de eliminación nominal, o por las propiedades físicas del medio de almacenaje. La persistencia de datos posibilita en forma inadvertida la exhibición de información sensible si el medio de almacenaje es dejado en un ambiente sobre el que no se tiene control (p. ej., se tira a la basura, se le da a un tercero).

Con el correr del tiempo, se han desarrollado varias técnicas para contrarrestar la persistencia de datos. Dependiendo de su efectividad y de su intención, a menudo se los clasifica como compensación o purga/higienización. Métodos específicos incluyen la sobre escritura, la desmagnetización, el cifrado, y la destrucción física.

 Causas
Muchos sistemas operativos, administradores de archivos y otros programas proveen facilidades que hacen que el archivo no sea inmediatamente eliminado cuando el usuario solicita esa acción. En su lugar, el archivo es trasladado a un área de retención que permite al usuario fácilmente revertir la acción si ha cometido un error.

Incluso cuando no se proporciona un área de retención de archivos eliminados explícita, o cuando el usuario no la usa, los equipos normales realmente no quitan el contenido de un archivo cuando se lo intenta eliminar. En lugar de eso, simplemente eliminan la entrada del archivo del índice del sistema de archivos porque esto requiere menos trabajo y por lo tanto es una solución más rápida. Los contenidos del archivo – los verdaderos datos – permanecen en el medio de almacenamiento. Los datos permanecerán allí hasta que el sistema operativo reutilice el espacio para nuevos datos. En algunos sistemas, suficientes metadatos del sistema de archivos son conservados para facilitar la recuperación de los datos por programas utilitarios fácilmente disponibles. Aun cuando la recuperación se ha tornado imposible, los datos, hasta que sean sobrescritos, pueden ser leídos por programas que leen los sectores del disco directamente. Los forenses informáticos a menudo emplean dichos programas.

Del mismo modo, el reformateo, el reparticionamiento o la imagen recreada de un sistema no siempre garantiza escribir sobre todas las áreas del disco aunque todos harán que el disco parezca vacío ó, en el caso de la imagen recreada, vacío a excepción de los archivos presentes en la imagen, al ser examinados con la mayoría de los programas.

 Contramedidas
Habitualmente se reconocen tres niveles de eliminación de datos persistentes:

 Compensación
Compensación es la remoción de los datos sensibles de un medio de almacenamiento de tal manera que hay seguridad de que los datos no podrán ser reconstruidos utilizando las funciones normales del sistema o programas de recuperación de archivos/datos. Los datos pueden aún ser recuperables, pero eso requerirá técnicas especiales de laboratorio.

 Purga
Purga o higienización es la remoción de datos sensibles de un dispositivo de almacenamiento con el objeto de que los datos no puedan ser reconstruidos utilizando alguna de las técnicas conocidas. La purga, proporcional a la sensibilidad de los datos, generalmente se efectúa antes de dejar libres de control los dispositivos de almacenamiento, en los casos en que se descartan viejos medios de almacenamiento o se trasladan dichos medios a computadoras con diferentes requerimientos de seguridad.

 Destrucción
El medio de almacenamiento es físicamente destruido. Su efectividad varía. Dependiendo de la densidad de grabación del medio y/o de la técnica de destrucción, esta técnica puede dejar datos recuperables por métodos de laboratorio. A su vez, la destrucción física cuando se utilizan los métodos apropiados, es generalmente considerada como el método más seguro posible.

 Métodos específicos

 Sobre escritura
Un método común de contrarrestar los datos persistentes es sobre escribir el medio de almacenaje con nuevos datos. Esto se llama a menudo limpieza o trituración de un archivo o de un disco. Es una opción popular y de bajo costo de algunos programas debido a que a menudo puede ser implementado simplemente en dichos programas y puede ser selectivamente dirigido solo hacia una parte del medio de almacenaje. La sobre escritura es generalmente un método aceptable de compensación siempre y cuando el medio de almacenaje sea grabable y no esté dañado.

La técnica de sobre escritura más simple escribe los mismos datos en todas partes, a menudo simplemente una muestra de ceros. Como mínimo, esto evitará que los datos sean recuperados simplemente por la lectura del medio de almacenaje utilizando las funciones habituales del sistema.

Para contrarrestar técnicas de recuperación de datos más avanzadas, a menudo se prescriben muestras de sobre escritura específicas. Estas pueden ser muestras que intentan erradicar cualquier traza de firmas. Por ejemplo, escribiendo en forma repetida, muestras alterantes de unos y ceros puede ser más efectiva que utilizar sólo ceros. Frecuentemente se indican combinaciones de muestras. De hecho, no es necesario sobrescribir datos varias veces. La esencia de la sobrescritura es reemplazar los datos existentes con otro contenido. La eficacia de la destrucción de datos no depende ni del contenido de los datos que se destruyen ni del patrón de sobrescritura.

Un desafío de la sobre escritura es que ciertas áreas del disco pueden ser inaccesibles por degradación de los medios o por otros errores. La sobre escritura por software puede ser problemática en medios de alta seguridad que requieren controles más fuertes de la mezcla de datos que la que puede proveer el programa en uso. El uso de técnicas avanzadas de almacenamiento también puede hacer inefectivo la sobre escrituración basada en archivos.

 Factibilidad de recuperar datos sobre escritos
Peter Gutmann investigó la recuperación de datos de medios de almacenaje nominalmente sobre escritos a mediados de la década del 90. El sugirió que la microscopia por fuerza magnética puede ser capaz de recuperar dichos datos y desarrolló patrones de sobre escritura específicos, para controladores específicos, para contrarrestar este tipo de recuperación. Estos patrones se conocen como el método de Gutmann.

Daniel Feenber, un economista del privado National Bureau of Economic Research, afirma que las posibilidades de recuperar datos sobre escritos de un disco duro moderno son una "leyenda urbana". También señala “la brecha de 18½ minutos que Rose Mary Woods creo en una cinta de Richard Nixon discutiendo sobre el caso Watergate”. La información de la brecha aún no ha sido recuperada y Feenberg afirma que recuperarla sería una tarea fácil comparada con la recuperación de una señal digital de alta densidad.

Para noviembre de 2007, el Departamento de Defensa de los Estados Unidos consideraba que la sobre escritura era un método aceptable para compensar medios magnéticos dentro de la misma área/zona de seguridad, pero no como un método de higienización. Solamente aceptaba como método de higienización la de magnetización o la destrucción física.

Por el otro lado, de acuerdo a la Publicación Especial 800-88 del 2006 NIST (p.7): "Los estudios han demostrado que la mayoría de los medios de almacenaje pueden ser efectivamente compensados con una sobre escritura" y “para los discos ATA fabricados con posterioridad a 2001 (de más de 15 GB), los términos compensación e higienización han convergido”. Un análisis de Wright y colaboradores de técnicas de recuperación, incluyendo microscopia por fuerza magnética, también concluyen que una simple limpieza es todo lo que se necesita en los controladores modernos”. Señalan que el largo tiempo que requieren múltiples limpiezas “han creado una situación en la que muchas organizaciones ignoran totalmente el tema – lo que ocasiona filtraciones y pérdidas."

 De magnetización
De magnetización es la remoción o reducción del campo magnético de un disco o controlador utilizando un dispositivo llamado de magnetizador que ha sido diseñado para el medio de almacenaje que se desea borrar. Aplicado a medios magnéticos, la de magnetización puede purgar el medio rápida y efectivamente.

La de magnetización a menudo torna los discos duros inoperables, ya que borra el formateo de bajo nivel que solamente es efectuado en las fábricas durante la fabricación. Es posible, sin embargo, devolver el disco duro a un estado funcional si el fabricante accede a reformatearlo. Los disquetes desmagnetizados pueden ser generalmente reformateados y reutilizados con el hardware habitual de los consumidores.

En algunos entornos de alta seguridad, puede que se requiera utilizar un de magnetizador que ha sido aprobado para la tarea. Por ejemplo, en las jurisdicciones gubernamentales y militares de los Estados Unidos, puede que se exija el uso de un de magnetizador de la “Lista de Productos Evaluados” de la NSA.

 Cifrado

El cifrado de datos antes de que sea almacenado en el medio puede mitigar las preocupaciones sobre la persistencia de datos. Si la clave criptográfica es suficientemente fuerte y cuidadosamente controlada (p. ej., no sujeta a persistencia de datos) puede hacer que sea irrecuperable en forma efectiva cualquier dato del medio. .

El cifrado puede hacerse sobre la base de archivo por archivo o sobre todo el disco. Sin embargo, si la clave es almacenada, aunque sea temporalmente, en el mismo sistema que los datos, puede pasar a ser un dato remanente y ser recuperada por un atacante por medio de un ataque de arranque en frío.

 Destrucción física
Una cuidadosa destrucción física de todo el medio de almacenaje es generalmente considerado como el método más seguro de contrarrestar la persistencia de datos. Sin embargo, el proceso generalmente lleva tiempo y es engorroso. La destrucción física puede requerir métodos extremadamente cuidadosos ya que aún un muy pequeño fragmento del medio puede contener grandes cantidades de información.

Las técnicas de destrucción específica incluyen:

 Rotura física del medio por molienda, trituración, etc.
 Incineración.
 Cambio de estado ( por ejemplo licuefacción o vaporización de un disco sólido).
 Aplicación de químicos corrosivos, tales como ácidos, a las superficies de grabación.
 Para medios magnéticos, la elevación de la temperatura por encima de la temperatura de Curie.
 Para muchos medios de almacenaje eléctrico volátil y no volátil, la aplicación de extremadamente altos voltajes, muy por encima de las especificaciones operacionales.

 Complicaciones

 Áreas inaccesibles
Los medios de almacenaje pueden tener aéreas que son inaccesibles por métodos normales. Por ejemplo, los discos magnéticos pueden desarrollar “sectores averiados” después de que los datos han sido grabados, y las cintas tienen brechas entre las distintas grabaciones. Los discos duros modernos a menudo tienen un re mapeo automático de sectores marginales o pistas que el sistema operativo no puede siquiera detectar. Los intentos de contrarrestar la persistencia de datos por sobre escritura puede no ser exitosa en tales situaciones, ya que los datos persistentes pueden persistir in estas áreas nominalmente inaccesibles.

 Medios de almacenaje avanzados
Sistemas de almacenaje de datos con características más sofisticadas pueden hacer que la sobre escritura sea inefectiva, especialmente la basada en la sobre escritura por archivo.

Los sistemas de archivos con journaling incrementan la integridad de los datos al registrar las operaciones de escritura en múltiples ubicaciones y mediante la aplicación de semántica de tipo transaccional. En estos sistemas, los datos persistentes pueden persistir en ubicaciones “fuera” de las ubicaciones de almacenamiento nominal del archivo.

Algunos sistemas de archivos implementan copy-on-write ó control de versiones con la intención de que al escribir en un archivo nunca se sobrescriba los datos ya ubicados.

Tecnologías tales como RAID y técnicas de anti fragmentación pueden hacer que los datos del archivo sean escritos en múltiples ubicaciones, ya sea por diseño (tolerancia de falla), o como datos persistentes.

El wear levelling es una técnica que también puede derrotar el borrado de los datos, al relocalizar los bloques escritos entre el momento en que originalmente fueron escritos y el momento en que se están sobrescribiendo.

 Medios ópticos
Los medios ópticos no son magnéticos y no son afectados por la de magnetización. Los medios ópticos de escritura única (CD-R, DVD-R, etc.) tampoco pueden ser purgados por sobre escritura. Los medios ópticos de lectura/escritura tales como CD-RW y DVD-RW, pueden ser sobrescritos. Métodos para higienizar exitosamente los discos ópticos incluyen la de laminación-abrasión de la capa metálica, trituración, electro destrucción (como por exposición a microondas), y la sumersión en solventes poli carbonatados (p.ej., acetona).

 Datos en RAM
Se ha observado persistencia de datos en SDRAM, la que típicamente se considera volátil (es decir que sus componentes se borran con la pérdida de la potencia eléctrica). En el estudio, a veces se observó retención de datos a temperatura ambiente.

Otro estudio encontró persistencia de datos en una DRAM, también con retención de datos durante minutos o segundos a temperatura ambiente y "durante toda una semana sin refresco cuando se lo enfrió con nitrógeno líquido Los autores del estudio fueron capaces de usar un ataque de arranque en frío para recuperar claves criptográficas para varios populares sistemas de cifrado total del disco. Pese a cierto grado de degradación de la memoria, fueron capaces de aprovecharse de la redundancia en la forma en que las claves se almacenan después de que se han expandido para ser usadas eficientemente como en el caso de las claves maestras. Los autores recomiendan que las computadoras sean apagadas más que dejadas en el estado de “dormidas” cuando no están bajo el control físico del dueño, y en ciertos casos, como si uno posee el programa Bitlocker que se configure también un PIN para el arranque. Los chips de RAM modernos tienen incorporados un módulo de auto refresco de tal manera que pueden retener los datos mientras reciban energía y una señal de reloj.

 Estándares
 US NIST Special Publication 800-88: Guía para la higienización de los medios (Guidelines for Media Sanitization)

 US DoD 5220.22-M: Manual de operaciones del programa de seguridad industrial nacional (National Industrial Security Program Operating Manual [NISPOM])
 Las actuales ediciones no contienen más referencias a métodos de higienización específicos. Los patrones de higienización se dejan en manos de la Cognizant Security Authority.
 Pese a que el texto NISPOM en sí mismo nunca describió métodos específicos para higienización, ediciones pasadas (1995 y 1997) contenían explícitos métodos de higienización dentro de la tabla DDS Y C&M que estaban insertadas después de la Sección 8-306.
 El Defense Security Service (DSS) provee una matriz de compensación e higienización (Clearing and Sanitization Matrix = C&SM)que especifica los métodos.
 Para la edición de noviembre de 2007 del DSS C&M, la sobre escritura dejó de ser un método aceptable para la higienización de los medios magnéticos. Solamente se acepta la demagnetización (con un demagnetizador aprobado por la NSA) o la destrucción física.
 NAVSO P5239-26
 AR380-19
 RCMP B2-002: *IT Media Overwrite and Secure Erase Products*

 Véase también
 Cómputo forense
 Criptografía
 Recuperación de datos
 Chatarra electrónica
 Estructuras de datos persistentes
 Cifrado
 Método de Gutmann
 Triturador de papel
 Archivo de texto (discusión de seguridad)

 Software
 BCWipe (usado por Bruce Schneier)
 Blancco
 Darik's Boot and Nuke
 Data Shredder
 Eraser (recomendado por *Consumer Reports*)
 HDDerase
 PGP Desktop
 shred (part of the GNU Coreutils package)

Hay docenas de otras herramientas para varios sistemas operativos.

 Notas
.

 Referencias
  (Rainbow Series "Forrest Green Book"[sept 1991])
 Tutorial on Disk Drive Data Sanitization Gordon Hughes, UCSD Center for Magnetic Recording Research, Tom Coughlin, Coughlin Associates
 Why Information Must Be Destroyed - Overview of paper-based destruction  Ben Rothke, CISSP, British Telecom
 Why Information Must Be Destroyed Part 2 - Overview of digital-based destruction  Ben Rothke, CISSP, British Telecom

 Enlaces externos
