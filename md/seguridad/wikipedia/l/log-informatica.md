---
type: Artículo de enciclopedia
title: Log (informática)
description: "En informática, se usa el término registro, log o historial de log para referirse a la grabación secuencial en un archivo o en una base de datos de todos los acontecimientos (eventos o acciones) que afectan a un proceso …"
resource: https://es.wikipedia.org/wiki/Log_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Log_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Log_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Log (informática)

En informática, se usa el término **registro**, ***log*** o **historial de *log*** para referirse a la grabación secuencial en un archivo o en una base de datos de todos los acontecimientos (eventos o acciones) que afectan a un proceso particular (aplicación, actividad de una red informática, etc.). De esta forma constituye una evidencia del comportamiento del sistema.

Por derivación, el proceso de generación del *log* se le suele llamar guardar, registrar o *loguear* (un neologismo del inglés *logging*) y al proceso o sistema que realiza la grabación en el *log* se le suele llamar *logger* o registrador.

Generalmente los acontecimientos vienen anotados con:
 El momento exacto o marca temporal (fecha, hora, minuto, segundo) en el que ocurrió lo que permite analizar paso a paso la actividad.
 Una o más categorizaciones del acontecimiento registrado. Es frecuente usar categorías distintas para distinguir la importancia del acontecimiento estableciendo distintos niveles de registro los cuales suelen ser: depuración, información,  advertencia y error.

La mayoría de los registros se almacenan en texto sin formato o en XML. De esta forma, el *log* puede ser fácilmente leído y procesado. Sin embargo, otras veces son construidos directamente por dispositivos usando campos magnéticos y pulsos electrónicos que pueden ser recolectados y analizados con herramientas y técnicas especiales.

 Definición
Registro de actividad o log:

 Etimología
El uso de este anglicismo es debido a las traducciones del inglés de la jerga informática. En inglés el término *log* designa el cuaderno de bitácora en el cual el comandante de un navío consigna los acontecimientos que sobrevienen durante la travesía. Una versión dice que origen es la corredera (*log* en inglés), un instrumento al que se le enganchaba una cuerda con nudos que se lanzaba desde los barcos para medir la rapidez de la embarcación. Otra versión dice que a la entrada de un cuartel había una garita, una *log cabin* en la cual había un registro en el que se consignaba las entradas/salidas de los soldados del cuartel y a la que se le llamaba el *log cabin book* y por extensión el *log book*. Así, se entraba (*log in*) y se salía (*log out*).

Tipos
De aplicaciones
Los *logs* de aplicaciones graban cronológicamente las operaciones durante el funcionamiento de la aplicación. Su función  forma parte de la lógica de la aplicación. Por lo tanto, no debería estar detenida durante el funcionamiento de la misma.

Del sistema
Los archivos de registros de sistema graban cronológicamente los acontecimientos que sobrevienen a nivel de componentes del sistema. Por ejemplo, los sistemas Unix y similares usan syslogd para crear y adichos registros y usan el protocolo Syslog para enviar hacia otros ordenadores especializados en recolectar y analizar dicha información.

 Registros
Si la grabación se realiza en un fichero, se llama fichero de registros o archivo de *log* (en inglés *log file*) al archivo que contiene las grabaciones. En estos ficheros los eventos vienen por orden cronológico de tal forma que la generación correcta de estos ficheros es grabar la información concatenando el nuevo contenido al final del contenido del fichero actual.

Típicamente se asigna una línea por acontecimiento, comenzando por el momento exacto o marca temporal (fecha, hora, minuto, segundo) en el que tuvo lugar.

 Análisis
Al estar su mayoría en texto plano, se pueden utilizar herramientas como grep, find así como uso de expresiones regulares para detectar patrones o información específica.

A su vez puede existir el intercambio y comparación de información con bases de datos de amenazas tales como VirusTotal, Malware Information Sharing Platform u otras plataformas de inteligencia contra amenazas mediante software cómo Fail2ban.

 Aplicaciones
Tener un registro de todos los acontecimientos que han ido sucediendo es muy útil. Ejemplos de uso:
 Análisis forense.
 Detección de intrusos.
 Depuración de errores. Por ejemplo, el análisis, normalmente estadístico, de los registros permite hacer hipótesis sobre los errores.
 Auditoría

 Seguridad y confidencialidad
Los *logs* pueden contener información confidencial que no debe ser revelada por privacidad o incluso porque su revelación hace vulnerable la seguridad del sistema. En estos casos es necesaria proteger la confidencialidad de la información. Para solucionar estos problemas se usan en los *logs* técnicas de cifrado.

El valor de los logs como evidencia disminuye si no podemos demostrar que no han sido modificados por entidades no autorizadas. En general es necesario proteger la integridad de la información.

Las investigaciones en el campo de los logs seguros han sido principalmente enfocadas en el campo de la integridad ya que el cifrado es en sí mismo un problema aparte. Sin embargo ha habido investigaciones específicas sobre cifrado en logs pero para proveerlo en un entorno complejo centrado en aportar integridad.

Supongamos que tenemos un único *logger* o registrador que es inicialmente confiable pero que puede ser corrompido en algún momento. Sería bueno garantizar que después de que el registrador ha sido corrompido no pueda manipular los registros creados antes de la corrupción. Para ello se puede usar hardware de almacenamiento en el que solo se pueda escribir una vez pero se pueda leer muchas veces (Write Once Read Many) o simplemente impresoras. A veces estos sistemas no son viables y se usan técnicas criptográficas de *detección de manipulaciones* que no protegen frente a modificaciones pero permiten detectar si se han producido dichas modificaciones.

En estos sistemas criptográficos, cuando comienza el proceso de autenticación, el *logger* crea una clave de verificación. Esta clave de verificación puede entonces ser distribuida a un conjunto de verificadores o puede ser publicado a cualquiera dependiendo del tipo de algoritmo usado: firma digital o MAC. La ventaja de los sistemas con firma digital es que cualquiera puede verificar la integridad y los verificadores no pueden modificar el log sin ser detectados. La ventaja de los sistemas MAC es que son más rápidos. Como el registrador es confiable al inicio del proceso, la clave de verificación es siempre escogida de forma adecuada.

Sin embargo, cuando un atacante toma el control del sistema puede tener acceso a cualquier clave almacenada y por tanto podría generar pruebas falsas y modificar los ficheros de *logs* sin ser registrados. Para mitigar este problema se han desarrollado sistemas que buscan conseguir integridad hacia delante. Para ello en lugar de tener una clave secreta se tiene una serie de claves secretas donde cada clave posterior puede ser generada a partir de la clave anterior vía un procedimiento específico pero no es posible el proceso inverso. Los esquemas de firma digital o de MAC que consiguen integridad hacia adelante  se dice que son seguras hacia delante. Si se trata de un sistema de firma digital se dice que es firma segura adelante

Cuando se define el esquema se define el evento que tiene que ocurrir para pasar de usar una clave a usar la siguiente. Normalmente el criterio suele ser que haya pasado un tiempo especificado o se hayan registrado cierto número de eventos. Cuando esto sucede es muy importante borrar toda evidencia de la clave anterior y garantizar que dicha información es irrecuperable.

A partir de esta idea se han diseñado distintos sistemas que han agregado distintas peculiaridades para añadir más seguridad, como por ejemplo:
 Cada entrada en el registro se almacena junto con una data para detectar ataques de reordenamiento.
 Muchos esquemas cuentan el número de entradas en el log y añaden números de secuencia. Esto ayuda a determinar el orden de las entradas en el log.
 Otros esquemas proponen usar cadenas resumen donde cada entrada en el *log* es aumentada añadiendo el valor *hash* de la entrada previa en el *log*. Esto permite detectar ataques de reordenamiento y el borrado de entradas en el *log*.
 Otros esquemas añaden una marca para identificar el número de clave de la secuencia que se está utilizando. A esto se les llama marcas de época. Esto permite hacer más fácil la verificación.
 Si el esquema loguea independientemente de la cantidad de tiempo que pasa puede ser muy útil añadir entradas de *log* que indique exclusivamente la hora actual en intervalos regulares (se les llama entradas de metrónomo)
 Algunos esquemas emplean de forma adicional cifrado para proteger la confidencialidad de los mensajes.

Las investigaciones más importantes sobre este campo son:
 Mihir Bellare y Bennet Yee en 1997 introdujeron la noción de integridad adelante usando esquemas MAC y propusieron el uso de número de secuencia y marcas de época para proteger el borrado de entradas en el historial.
 Bruce Schneier y John Kelsey en 1998 y 1999 idearon un sistema más concreto para logs seguros usando MAC. Su esquema incluye cifrado de las entradas de log y un mecanismo para garantizar que un semiconfiable verificador V puede leer entradas de log individuales
 Basado en el esquema de Bruce Schneier y John Kelsey, Jason E. Holt crea en 2006 Logcrypt. Su principal aportación es sustituir por firmas digitales las MAC. Este cambio empeora el rendimiento pero permite que los ficheros sean públicamente verificables ya que la clave pública puede hacerse pública.
 Giorgia Azzurra Marson y Bertram Poettering en 2013 usando MAC desarrollan un sistema una especie de cadena de hash  sobre una función de un solo sentido, donde uno puede construir el elemento n a partir del elemento i (n>i) sin tener que evaluar la función n-i veces.
 Di Ma y Gene Tsudik desde 2008 han encontrado debilidades en los sistemas similares al propuesto por Bruce Schneier y John Kelsey que permiten a un atacante que un verificador pueda aceptar un fichero de registros modificado (ataque de detección diferida) y ataques que permiten borrar una o más entradas del registro de *log* que estén al final del mismo (ataque de truncamiento). Para solucionarlas proponen el uso de firmas con agregación secuencial seguras adelante.
 Attila A. Yavuz, Ning peng y Michael K. Reiter han propuesto mejoras para usar firmas con agregación secuencial seguras adelante que sean menos pesadas computacionalmente.
 Brent R. Waters y otros en 2003 proponen mejoras en el cifrado de las entradas del log.
 Vasilios Stathopoulos y otros en 2006 construyen el esquema de Bruce Schneier y John Kelsey añadiendo otro autoridad confiable que recibe firma del estado del *log* periódicamente. Esto da una forma adicional para detectar modificaciones del fichero de registros.
 Wengsheng Xu y otros en 2005 construyen un servicio web para ficheros de registros usando el esquema de Bruce Schneier y John Kelsey y usando una Base de Computador Confiable para almacenar las claves criptográficas.

Véase también
 Blog, contracción de *web log*
 Seguridad informática

Referencias
