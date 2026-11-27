---
type: Artículo de enciclopedia
title: "Criptosistema de Goldwasser–Micali"
description: El criptosistema Goldwasser-Micali (GM) es un algoritmo de cifrado de clave asimétrica desarrollado por Shafi Goldwasser y Silvio Micali en 1982.
resource: https://es.wikipedia.org/wiki/Criptosistema_de_Goldwasser–Micali
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptosistema_de_Goldwasser–Micali"}
license: CC BY-SA 4.0
id: "eswiki-Criptosistema_de_Goldwasser–Micali"
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptosistema de Goldwasser–Micali

El criptosistema Goldwasser-Micali (GM) es un algoritmo de cifrado de clave asimétrica desarrollado por Shafi Goldwasser y Silvio Micali en 1982. GM tiene la distinción de ser el primer esquema de cifrado probabilístico de clave pública que es demostrablemente seguro bajo supuestos criptográficos estándar. Sin embargo, no es un criptosistema eficiente, ya que los textos cifrados pueden ser varios cientos de veces más grandes que el texto sin formato inicial. Para demostrar las propiedades de seguridad del sistema criptográfico, Goldwasser y Micali propusieron la definición ampliamente utilizada de seguridad semántica .

 Base
El criptosistema GM es semánticamente seguro en función de la supuesta intratabilidad del módulo de problema de residuos cuadrático un compuesto *N* = *pq* donde *p, q* son números primos grandes. Esta suposición establece que dado ( *x*, *N* ) es difícil determinar si *x* es un módulo de residuo cuadrático *N* (es decir, *x* = *y* 2 mod *N* para algunos *y* ), cuando el símbolo de Jacobi para *x* es   +1. El problema de los residuos cuadráticos se resuelve fácilmente dada la factorización de *N*, mientras que cualquier parte puede generar nuevos residuos cuadráticos, incluso sin el conocimiento de esta factorización. El criptosistema GM aprovecha esta asimetría al encriptar bits de texto sin formato individuales como residuos cuadráticos aleatorios o módulos no residuales *N*, todos con símbolo de residuo cuadrático   +1. Los destinatarios utilizan la factorización de *N* como clave secreta y descifran el mensaje probando la residualidad cuadrática de los valores de texto cifrado recibidos.

Porque Goldwasser – Micali produce un valor de tamaño aproximadamente | *N* | Para cifrar cada bit de un texto sin formato, el cifrado de GM da como resultado una expansión sustancial de texto cifrado . Para evitar ataques de factorización, se recomienda que | *N* | ser varios cientos de bits o más. Por lo tanto, el esquema sirve principalmente como una prueba de concepto, y desde entonces se han desarrollado esquemas más eficientes con seguridad comprobable como Elgamal .

Debido a que el cifrado se realiza utilizando un algoritmo probabilístico, un texto plano dado puede producir textos cifrados muy diferentes cada vez que se cifra. Esto tiene ventajas significativas, ya que evita que un adversario reconozca los mensajes interceptados al compararlos con un diccionario de textos cifrados conocidos.

 Definición del esquema
Goldwasser-Micali consta de tres algoritmos: un algoritmo de generación de clave probabilística que produce una clave pública y una privada, un algoritmo de cifrado probabilístico y un algoritmo de descifrado determinista.

El esquema se basa en decidir si un valor dado *x* es un mod cuadrado *N*, dada la factorización ( *p*, *q* ) de *N.* Esto se puede lograr utilizando el siguiente procedimiento:

 Calcule *x p* = *x* mod *p*, *x q* = *x* mod *q* .
 Si  y , entonces *x* es un mod de residuo cuadrático   *N.*

 Generación clave
El módulo utilizado en el cifrado GM se genera de la misma manera que en el criptosistema RSA . (Ver RSA, generación de claves para más detalles. )

 Alice genera dos números primos grandes distintos *p* y *q*, aleatoriamente e independientemente uno del otro.
 Alice calcula *N* = *pq* .
 Luego encuentra algo que no deja residuos *x, de* modo que los símbolos Legendre satisfagan  y de ahí el símbolo de Jacobi  es   +1. El valor *x* se puede encontrar, por ejemplo, seleccionando valores aleatorios y probando los dos símbolos Legendre. Si *p*, *q* = 3 mod 4 (es decir, *N* es un número entero de Blum ), entonces el valor *N*   −   1 está garantizado para tener la propiedad requerida.

La *clave pública* consta de ( *x*,   *N* ) La clave secreta es la factorización.   ( *p*,   *q* ).

 Cifrado de mensajes
Supongamos que Bob desea enviar un mensaje *m* a Alice:

 Bob primero codifica *m* como una cadena de bits ( *m* 1, ..., *m n* ).
 Por cada bit **', Bob genera un valor aleatorio **' del grupo de unidades módulo   *N* o '''' . Saca el valor  .

Bob envía el texto cifrado ( *c* 1, ..., *c* *n* ).

 Descifrado de mensajes
Alicia recibe ( *c* 1, ..., *c* *n* ). Ella puede recuperar *m* utilizando el siguiente procedimiento:

 Para cada *i*, usando la factorización prima ( *p*, *q* ), Alice determina si el valor *c* *i* es un residuo cuadrático; si es así, *m* *i* = 0, de lo contrario *m* *i* = 1.

Alice emite el mensaje *m* = ( *m* 1, ..., *m* *n* ).

 Propiedades de seguridad
Hay una reducción simple de romper este criptosistema al problema de determinar si un módulo de valor aleatorio *N* con el símbolo de Jacobi *+1* es un residuo cuadrático. Si un algoritmo *A* rompe el sistema criptográfico, para determinar si un valor dado *x* es un módulo de residuo cuadrático *N*, probamos *A* para ver si puede romper el sistema criptográfico utilizando ( *x*, *N* ) como clave pública. Si *x no* es un residuo, entonces *A* debería funcionar correctamente. Sin embargo, si *x* es un residuo, entonces cada "texto cifrado" será simplemente un residuo cuadrático aleatorio, por lo que *A* no puede ser correcto más de la mitad del tiempo. Además, este problema es auto-reducible al azar, lo que garantiza que para una *N* dada, cada clave pública sea tan segura como cualquier otra clave pública.

El criptosistema GM tiene propiedades homomórficas, en el sentido de que si *c* 0, *c* 1 son los cifrados de los bits *m* 0, *m* 1, entonces *c* 0 *c* 1 mod   *N* será un cifrado de  . Por esta razón, el criptosistema GM a veces se usa en primitivas criptográficas más complejas.

 Referencias

 Véase también

 Blum – Goldwasser cryptosystem
