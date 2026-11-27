---
type: Artículo de enciclopedia
title: Protocolo de Ko-Lee-Cheon-Hang-Park
description: El protocolo Ko-Lee-Hang-Park es un protocolo de clave pública que usa grupos no abelianos.
resource: https://es.wikipedia.org/wiki/Protocolo_de_Ko-Lee-Cheon-Hang-Park
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protocolo_de_Ko-Lee-Cheon-Hang-Park"}
license: CC BY-SA 4.0
id: eswiki-Protocolo_de_Ko-Lee-Cheon-Hang-Park
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protocolo de Ko-Lee-Cheon-Hang-Park

El protocolo **Ko-Lee-Hang-Park** es un protocolo de clave pública que usa grupos no abelianos. Fue propuesto por **Ki Hyoung Ko, Sang Jin Lee, Jung Hee Cheon, Jae Woo Han, Ju-sung Kang y Choonsik Park.** Utiliza el fundamento de que los grupos trenza pueden servir como una buena fuente de enriquecimiento para la criptografía, lo cual incluye lo siguiente:
 El problema de la palabra es solucionado por medio de un algoritmo rápido que computa la forma canónica que puede ser manejada de manera eficiente por computadores.
 Las operaciones de grupo pueden ser ejecutadas de manera eficiente.
 Los grupos de trenzas tienen algunos problemas matemáticos difíciles que pueden ser utilizados para diseñar primitivos criptográficos.

También tiene como fin proponer e implementar un protocolo de acuerdo de llave y sistema criptográfico de llave pública que puede ser utilizado para diseñar primitivas criptográficas. La seguridad de este sistema está basada en problemas topológicos, combinatorios y teóricos de grupos que son intractibles  de acuerdo al actual conocimiento matemático. La fundamentación de este sistema es diferente a la mayoría de criptosistemas usados en teoría de números, pero existen algunas similitudes en el diseño.

 Antecedentes

Desde que Diffie y Hellman presentaron por primera vez un criptosistema de llave pública usando funciones de una sola vía, algunos sistemas de cifrado de llave pública han sido vulnerados. Muchos de los sistemas de cifrado de llave pública requieren una gran cantidad de números primos. La dificultad de factorización de enteros con una gran cantidad de factores primos forma la base del sistema RSA y sus variantes como la de Rabin-Williams, el esquema de LUC o el cifrado de curva elíptica. También la dificultad del problema de algoritmo discreto forma la base de los cifrados tipo Diffie-Hellman como ElGamal.

Ha habido bastantes esfuerzos para desarrollar cifrados de llave pública alternativos que no están basados en la teoría de números. El primer intento fue usar los problemas de dificultad NP en combinatoria como el cifrado Merkle-Hellman y sus modificaciones. Algunos criptógrafos han sido pesimistas acerca de la criptografía combinatoria después del desciframiento del cifrado de clave pública tipo Knapsack realizado por Shamir, Brickell, Lagarias, Odlyzko, Vaudenay y otros. La mayoría de los criptosistemas derivados de la teoría de grupos combinatorios son principalmente teóricos o tienen ciertas limitaciones en la práctica amplia y general.

 Descripción de funcionamiento
Para este protocolo de encriptación se utiliza una función unidireccional basada en el problema de conjugación en grupos trenzados, y de esta función se derivara un protocolo de establecimiento de clave y un protocolo de clave pública.

 Función unidireccional

Si consideramos dos subgrupos  y  que pertenecen a , tales que  son las trenzas formadas al trenzar las trenzas izquierdas entre  , es decir, que las trenzas  son las únicas que están trenzadas, y las trenzas  no lo están. De forma similar el subgrupo  son las trenzas formadas por las trenzas trenzadas de la derecha, es decir que las trenzas  están trenzadas, pero las trenzas  no están trenzadas. De esta forma, cada subgrupo se genera así:

 se genera por σ, σ,..., σ, y el subgrupo  se genera por σ, σ,..., σ.

En la función también debe considerarse la propiedad conmutativa de los grupos trenza que dice que σσ σσ para  ≥ . Así, se puede decir que para cualquier  Є  y  Є , entonces . Así, se tiene que la función es:

 ×  →  × ,

Esta función es unidireccional debido a que dados  es fácil calcular , pero requiere un tiempo exponencial para calcular  conociendo , y en esto se basa la seguridad de este protocolo criptográfico. En este aspecto es similar al protocolo de Diffie-Hellman, ya que el rol de  es similar al de  en el protocolo Diffie-Hellman.

 Establecimiento de clave

 Paso de preparación: Se eligen dos enteros  y  tales que la trenza  de orden  es suficientemente complicada, y luego esta se publica.

 Paso de establecimiento de clave:
 Alice escoge un  Є  aleatoriamente y le envía  a Bob
 Bob escoge un  Є  aleatoriamente y le envía  a Alice
 Alice recibe  y calcula la clave compartida
 Bob recibe  y calcula la clave compartida

Como se sabe que , entonces:

Obteniendo Alice y Bob la misma trenza.

 Protocolo de clave pública

Usando el establecimiento de clave anterior, ahora se toma una función hash  → {} que se adapte del grupo de trenzas al mensaje que se quiere encriptar.

 Generación de clave:
 Se escoge un  Є  suficientemente complicado
 Se escoge una  Є
 Se define la clave pública como , donde , y la clave privada sería

 Encriptación: Tomando el mensaje  Є {} y la clave pública definida
 Se escoge una trenza cualquiera  Є
 Obteniendo así el texto cifrado , donde  y

 Descifrado:
 Con el texto cifrado y la clave privada se calcula

Como  y  conmutan, entonces . Así que  recuperando así el mensaje original.
Para este protocolo debe elegirse un  lo suficientemente complicado para evitar la “factorización” de  en , donde  Є ,  Є  y  es una trenza de orden  conmutable con  y . Esto es así ya que si es posible descomponer fácilmente ,  entonces:

 sería fácil de calcular usando  y  sin conocer  o .

 Operación del protocolo

Se discuten las características operativas teóricas del protocolo propuesto y los parámetros de seguridad / longitud del mensaje para futuras implementaciones, esto debido a que en el protocolo **Ko-Lee-Cheon-Hang-Park** no es posible comparar su desempeño con el de otros cifrados de clave pública. Recordemos que el protocolo usa tres hebras:  y , y el texto cifrado es . Cuando se trabaja con hebras, debemos considerar dos parámetros, el **índice de la hebra y la longitud canónica**. Por simplicidad, asumimos que los índices de las hebras en nuestro protocolo son  y las longitudes canónicas son . Las siguientes son las discusiones acerca de las características de operación del protocolo:

 Una permutación puede ser representada por un entero . Mientras , una hebra con cantidad de factores canónicos puede ser representada por una cadena de bits de tamaño .
 Para trenza  y para . Entonces  y  son a lo sumo . Para selecciones genéricas de  y , estos son no menores que . Además, asumimos que  y  están entre  y .
 El tamaño de la llave privada  es .
 El tamaño de la llave pública  es a lo sumo .
 La dificultad de un ataque de fuerza bruta para computar de  a , o de manera equivalente, calcular  de , es proporcional a

 Análisis de seguridad

 Similitudes con el esquema de ElGamal

El protocolo es similar al protocolo de ElGamal en diseño y tiene las siguientes propiedades:

 El problema de romper el protocolo Ko-Lee-Cheon-Hang-Park es equivalente a resolver el problema base, al igual que en el rompimiento del protocolo de ElGamal es equivalente a resolver el problema de Diffie-Hellman. En el esquema propuesto, el texto cifrado es:

Y desencriptar el texto cifrado  en un texto plano  es equivalente a conocer

 Como cualquier otro sistema de cifrado de llave pública, es crítico usar una llave  diferente para cada sesión: Si la misma llave de sesión  es usada para encriptar  y  cuyos textos cifrados correspondientes son  y , luego  puede ser fácilmente computado de  porque .

 Ataque de fuerza bruta
Un posible ataque de fuerza bruta es computar  de  o  de ,lo cual es justamente un ataque al problema generalizado de búsqueda conjugada. Asuma que le ha sido dada una pareja  de trenzas en , tal que  para algún . La trenza  puede ser elegida de un grupo infinito  en teoría. Pero en un sistema práctico, el adversario puede generar todas las trenzas  en la forma canónica con algún límite razonable para  y revisar el punto en el que  corresponde.

El número necesario es como mínimo . Si el  y , luego , lo cual muestra que el ataque de fuerza bruta es inútil.

 Referencias

 Bibliografía
 *I. Anshel and M. Anshel, From the Post-Markov theorem through decision problems to public-key cryptography, Amer. Math. Monthly 100 (1993), no. 9, 835–844.*
 *I. Anshel, M. Anshel and D. Goldfeld, An algebraic method for public-key cryptography, Mathematical Research Letters 6 (1999) 287–291*
 *E. Artin, Theory of braids, Annals of Math. 48 (1947), 101–126*
