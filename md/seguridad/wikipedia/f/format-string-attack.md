---
type: Artículo de enciclopedia
title: Format String Attack
description: "Format String Attack es un ataque cibernético, el cual se produce cuando los datos enviados a través de una cadena de entrada de caracteres son evaluados como un comando por la aplicación o servidor al cual van …"
resource: https://es.wikipedia.org/wiki/Format_String_Attack
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Format_String_Attack"}
license: CC BY-SA 4.0
id: eswiki-Format_String_Attack
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Format String Attack

**Format String Attack** es un ataque cibernético, el cual se produce cuando los datos enviados a través de una cadena de entrada de caracteres son evaluados como un comando por la aplicación o servidor al cual van dirigidos. De esta forma, el atacante podría ejecutar código, leer la pila o causar un error de segmentación en la aplicación en ejecución, lo que provocaría nuevos comportamientos que podrían comprometer la seguridad o la estabilidad del sistema al que van dirigidos.

 Introducción
Muchos programadores usan mal ciertas funciones de procesado de cadenas de caracteres, como por ejemplo:
   printf (nombre);
   printf (“Me llamo %s\n”, nombre);

Otro ejemplo llamativo sería:
   char temp [32];
   sprintf (temp,”Me llamo %s”, nombre);

Los formatos más comunes que se pueden utilizar para el formato de cadenas son:
 **d** → Formato de enteros.
 **%i** → Formato de enteros (igual que %d).
 **%f** → Formato de punto flotante.
 **%u** → Formato sin signo.
 **%x** → Formato hexadecimal.
 **%p** → Muestra el correspondiente valor del puntero.
 **%c** → Formato de carácter.

 Componentes
Para entender el ataque, es necesario comprender los componentes que lo constituyen:

 **La función de formato:** es una función de conversión ANSI C, como printf, fprintf, que convierte una variable primitiva del lenguaje de programación en una representación de cadena legible por humanos.
 **La cadena de formato:** es el argumento de la función de formato y es una cadena ASCII Z que contiene parámetros de texto y formato, como:
    printf ("La fecha de nacimiento es: %d \n", 1974);
 **El parámetro de cadena de formato:** como% x% s, define el tipo de conversión de la función de formato.

El ataque podría ejecutarse cuando la aplicación no valide correctamente la entrada enviada.
En este caso, si un parámetro de cadena, como %x, se inserta en los datos publicados, la cadena es analizada por la función correspondiente al formato y se ejecuta la conversión especificada en los parámetros.
Sin embargo, se esperan más argumentos como entrada, y si estos argumentos no se proporcionan, la función podría leer o escribir en la pila.

De esta manera, es posible definir una entrada bien diseñada que podría cambiar el comportamiento del formato de la función de la aplicación, permitiendo así al atacante causar una denegación de servicio (DNS) o provocar la ejecutar comandos arbitrarios.

Si la aplicación utiliza funciones de formato en el código fuente, que es el encargado de interpretar los caracteres de formato. El atacante podría explorar la vulnerabilidad insertando caracteres de formato en el sitio web.
Por ejemplo, si la función printf se utiliza para imprimir el nombre de usuario insertado en algunos campos de la página, el sitio web podría ser vulnerable a este tipo de ataque. Como mostramos a continuación:
   printf (nameUser);

Hay una serie de funciones de formato definidas en el ANSI C, algunas utilizadas para cubrir necesidades básicas
y otras más complejas basadas en estas primeras, que si bien no entran dentro del estándar, si están disponibles
para su uso.

**Funciones básicas:**
 **printf** → Imprime el flujo ’stdout’.
 **fprintf** → Imprime el flujo de un fichero.
 **sprintf** → Imprime en una cadena.
 **snprintf** → Imprime en una cadena comprobando la longitud.
 **vprintf** → Imprime en ’stdout’ desde una estructura va_arg.
 **vfprintf** → Imprime en un fichero desde una estructura va_arg.
 **vsprintf** → Imprime en una cadena desde una estructura va_arg.
 **vsnprintf** → Imprime en una cadena comprobando la longitud desde una estructura va_arg.
 **otras:** → syslog, ver, err, vwarn, warn y setproctile.

A continuación se muestran algunos ejemplos de funciones de formato, que si no se trata la información con la seguridad debida, pueden exponer a la aplicación a un Format String Attack, o a lo que es lo mismo, a un Ataque de Cadena de Formato.

**Funciones de Formato**

A continuación se presentan algunos parámetros de formato que se pueden utilizar y las consecuencias que tienen:
 **%x:** Lee los datos de la pila.
 **%s:** Lee cadenas de caracteres de la memoria del proceso.
 **%n:** Escribe un número entero en las ubicaciones de la memoria del proceso.

Para descubrir si la aplicación es vulnerable a este tipo de ataque, es necesario verificar si la función formato acepta y analiza los parámetros de la cadena de formato mostrados en la siguiente tabla:

**Parámetros comunes utilizados en un ataque de cadena de formato**

 La pila y su funcionamiento

El comportamiento de la función de formato es controlado por format string. Recuperando los parámetros solicitados
desde la pila de la siguiente manera:

    printf (" Número %d sin dirección , Número %d con dirección : %08x\n", i , a, &a );

En el lateral podemos ver el aspecto que tendría nuestra pila de instrucciones.

A continuación vamos a describir cada una de las variables usadas:
 A → Dirección de la cadena.
 i → Valor de la variable i.
 a → Valor de la variable a.
 &a → Dirección de la variable a.

La función de formato parseará la cadena A, leyendo carácter a carácter y copiándolo en la salida mientras que
este no sea ’%’. En el momento en el que encuentra el carácter a continuación de ’%’, especificará el tipo de parámetro
a evaluar.
La cadena ’%%’ se comporta de forma especial, y permite imprimir a la salida el carácter ’%’.
Los otros parámetros se relacionan con el resto de datos alojados en la pila.

 Prevención
La vulnerabilidad viene por el mal uso que se la da a la función printf. Cuando la utilizamos como:
   printf(cadena);

En lugar de:
   printf("%s", cadena);

Aunque el resultado devuelto es el mismo y funciona correctamente, lo más acertado sería la segunda opción.

La omisión del parámetro de formateado deriva en una vulnerabilidad que podría ser aprovechado por un atacante para provocar la ejecución de código malicioso.

Si queremos prevenir este tipo de ataques es conveniente tener en cuenta las siguientes medidas:

 Usar la forma completa de la función printf.
 Usar snprintf en vez de sprintf, dependiente del tamaño del buffer de destino.

 Bibliografía

Enlaces externos
 CERT Secure Coding Standards
 CERT Secure Coding Initiative
 Known vulnerabilities at MITRE's CVE project.
 OWASP.ORG
 Reversing Exploiting: Format String Attack
