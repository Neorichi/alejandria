---
type: Artículo de enciclopedia
title: Desbordamiento de búfer
description: "En seguridad informática y programación, un desbordamiento de búfer (del inglés buffer overflow o buffer overrun) es un error de software que se produce cuando un programa no controla adecuadamente la cantidad de datos …"
resource: https://es.wikipedia.org/wiki/Desbordamiento_de_búfer
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Desbordamiento_de_búfer"}
license: CC BY-SA 4.0
id: eswiki-Desbordamiento_de_búfer
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Desbordamiento de búfer

En seguridad informática y programación, un **desbordamiento de búfer** (del inglés *buffer overflow* o *buffer overrun*) es un error de software que se produce cuando un programa no controla adecuadamente la cantidad de datos que se copian sobre un área de memoria reservada a tal efecto (buffer): Si dicha cantidad es superior a la capacidad preasignada, los bytes sobrantes se almacenan en zonas de memoria adyacentes, sobrescribiendo su contenido original, que probablemente pertenecían a datos o código almacenados en memoria. Esto constituye un fallo de programación.

En las arquitecturas comunes de computadoras no existe separación entre las zonas de memoria dedicadas a datos y las dedicadas a programa, por lo que los bytes que desbordan el buffer podrían grabarse donde antes había instrucciones, lo que implicaría la posibilidad de alterar el flujo del programa, llevándole a realizar operaciones imprevistas por el programador original. Esto es lo que se conoce como una vulnerabilidad.

Una vulnerabilidad puede ser aprovechada por un usuario malintencionado para influir en el funcionamiento del sistema. En algunos casos el resultado es la capacidad de conseguir cierto nivel de control saltándose las limitaciones de seguridad habituales. Si el programa con el error en cuestión tiene privilegios especiales constituye en un fallo grave de seguridad.

Se denomina shellcode al código ejecutable especialmente preparado que se copia al host objeto del ataque para obtener los privilegios del programa vulnerable.

La capacidad de los procesadores modernos para marcar zonas de memoria como protegidas puede usarse para aminorar el problema. Si se produce un intento de escritura en una zona de memoria protegida se genera una excepción del sistema de acceso a memoria (segfault), seguido de la terminación del programa. Por desgracia para que esta técnica sea efectiva los programadores han de indicar al sistema operativo las zonas que se necesita proteger, programa a programa y rutina a rutina, lo que supone un problema para todo el código heredado.

Existen diferentes tipos de protección contra ataques de desbordamiento de búfer. Estos incluyen sistemas como StackGuard que identifica el comportamiento de los ataques y los verifica de manera eficiente.

 Descripción técnica

Un desbordamiento de búfer ocurre cuando los datos que se escriben en un búfer corrompen aquellos datos en direcciones de memoria adyacentes a los destinados para el búfer, debido a una falta de validación de los datos de entrada. Esto se da comúnmente al copiar cadenas de caracteres de un búfer a otro.

 Ejemplo básico

En este ejemplo, un programa tiene definidos dos elementos de datos continuos en memoria: un buffer de 8 bytes tipo string, A, y otro de dos bytes tipo entero, B. Al comienzo, A contiene bytes nulos y B contiene el número 3 (cada carácter se representa mediante un byte).

  0
  0
  0
  0
  0
  0
  0
  0
  0
  3
   Buffer A
  Buffer B

A continuación, el programa intenta almacenar la cadena de caracteres "demasiado" en el buffer A, seguido de bytes nulos para marcar el fin de string. Al no validarse la longitud de la cadena, se sobrescribe el valor de B:

  'd'
  'e'
  'm'
  'a'
  's'
  'i'
  'a'
  'd'
  'o'
  0
   Buffer A
  Buffer B

A pesar de que el programador no quería cambiar el contenido del búfer B, el valor de éste ha sido reemplazado por un número equivalente a parte de la cadena de caracteres. Para este ejemplo, en un sistema big-endian que use ASCII, el carácter 'o' seguido del byte nulo equivale al número 28416.

Si B fuese la única variable aparte de A definida en el programa, la escritura de datos que sobrepasen los límites de B generarían un error como segmentation fault, concluyendo así el programa.

 Código fuente de ejemplo

En el siguiente ejemplo se presenta un código fuente en C con un error de programación. Una vez compilado, el programa generará un desbordamiento de buffer si se lo invoca desde la línea de comandos con un argumento lo suficientemente grande, pues este argumento se usa para llenar un buffer, sin validar previamente su longitud.

Strings de 9 caracteres o menos no provocarán desbordamiento de buffer. Por el contrario, strings de 10 caracteres o más, sí: Esto siempre es incorrecto, aunque no siempre resultará en un error del programa o segmentation fault.

Este programa puede reescribirse en forma más segura usando la función strncpy de la siguiente manera:

 Historia de abusos

Uno de los primeros aprovechamientos de los que hay registro de desbordamiento de búferes fue en 1988. Fue uno de los muchos que usó el gusano Morris para propagarse en Internet. El programa abusado fue un servicio de Unix llamado fingerd.

Más tarde, en 1995, Thomas Lopatic redescubrió en forma independiente el desbordamiento de búfer y publicó sus descubrimientos en la lista de correo sobre seguridad Bugtraq. Un año después, en 1996, Elias Levy (conocido también como Aleph One) publicó en la revista *Phrack* su artículo "Smashing the Stack for Fun and Profit", una introducción paso a paso para aprovecharse de vulnerabilidades de desbordamientos de búfer basados en la pila.

Desde entonces, por lo menos dos de los gusanos más importantes de Internet se han aprovechado de los desbordamientos de búfer para comprometer un gran número de sistemas. En 2001, el gusano Code Red se aprovechó de un desbordamiento de búfer en el Internet Information Services (IIS) 5.0 de Microsoft y en 2003 el gusano SQL Slammer comprometió máquinas corriendo Microsoft SQL Server 2000.

 Stack smashing

El pisado de pila o *stack smashing* es un tipo de desbordamiento de buffer que es aprovechado por algunos virus y otros programas maliciosos para tomar control sobre una aplicación, o provocar su terminación. Esto sucede cuando, por algún error imprevisto, se ingresa a la pila de la aplicación más datos que los que ésta puede contener, lo que provoca que esta se "desborde" y algunos datos se sobreescriban. Para evitar que suceda esto, los compiladores se mejoran cada día dejándole tiempo al programador para pensar en lo que realmente importa.

La siguiente sería una explicación de qué es, cómo se hace y cómo se previene el desbordamiento de pila, con el valor agregado de posibilitar una nueva herramienta que ayudará a explicar errores comunes de programación. El siguiente ejemplo está inspirado en la funcionalidad incluida en el nuevo compilador por defecto de la distribución Debian (en su versión inestable):

Este es un ejemplo común de un programa C vulnerable:

Este programa simple acepta un argumento y lo copia a un buffer estático. Este es un error de programación clásico, si este programa fuese compilado a un ejecutable setuid/setgid (ejecutable por cualquiera como si fuese el dueño) permitiría a un atacante ganar permisos fácilmente.

Como se van a demostrar las nuevas funciones del nuevo compilador, hay que asegurarse de compilar el ejemplo anterior con gcc-3.3 de la siguiente forma:

user@pc:/tmp$ gcc-3.3 -o buggy buggy.c

Antes de determinar si se puede romper, se deben ejecutar dos pruebas:

user@pc:/tmp$ /tmp/buggy
Uso: /tmp/buggy argumento
user@pc:/tmp$ /tmp/buggy test
Argumento copiado

Ambas funcionan como se espera. Ahora, se ejecuta la prueba pasando un argumento más largo para determinar si se desborda el buffer estático:

user@pc:/tmp$ ./buggy `perl -e 'print "X"x2048'`
Argumento copiado
Violación de segmento

Como se observa, la prueba fue exitosa: el buffer se desbordó con un argumento de más de 2000 caracteres, resultando en una violación de segmento. Ahora, un archivo de núcleo puede permitir depurarlo para identificar las direcciones de memoria utilizadas por el proceso:

user@pc:/tmp$ ulimit -c 09999999
user@pc:/tmp$ ./buggy `perl -e 'print "X"x3333'`
Argumento copiado
Violación de segmento (con archivo de núcleo)

Al correr el depurador gdb se puede ver el programa:

user@pc:/tmp$ gdb ./buggy core
GNU gdb 6.4.90-debian
...
El programa finalizó con señal 11, Violación de segmento
1. 0 0x58585858 in ?? 
(gdb) info registers eip
eip 0x58585858 0x58585858

Se puede observar que EIP muestra la dirección de memoria de la siguiente instrucción que será ejecutada (0×58585858). Esto significa que efectivamente se tomó el control del ejecutable con el script malicioso.

El explotar el ejecutable para correr una línea de comandos habiendo hecho esto es trivial y, por lo general, puede ser automatizado:

user@pc:~/cmd-overflow$ make
gcc-3.3 -o cmd-overflow -Wall -ggdb cmd-overflow.c
gcc-3.3 -o cmd-vuln -Wall -ggdb cmd-vuln.c
user@pc:~/cmd-overflow$ ./cmd-overflow --target=/tmp/buggy --args='%' --size=2048
Argumento copiado
shell-3.1$ id
uid=1000(user) gid=1000(user) groups=29(audio), 44(video), 46(plugdev), 100(users), 1000(user)
shell-3.1$ exit
exit

Se utiliza aquí un programa simple para crear un argumento de 2048 bytes de longitud que contiene el código requerido para correr una línea de comandos, y luego se ejecuta el programa defectuoso con este argumento construido a medida.

Se produjo el desbordamiento del buffer al correr este código, lo cual resultó en la ejecución de una línea de comandos. Si el programa se hubiese sido ejecutado en Linux con el flag setuid por un superusuario se hubieran ganado los privilegios del superusuario.

 Véase también
 Seguridad informática
 Inseguridad informática
 Desbordamiento de pila
 HoF
 Ping de la muerte
 Privacidad digital
 Exploit
 Bug
 Subdesbordamiento de búfer

 Referencias
