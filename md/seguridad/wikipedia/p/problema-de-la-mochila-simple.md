---
type: Artículo de enciclopedia
title: Problema de la mochila simple
description: "El problema de la mochila simple, también llamado problema de la mochila supercreciente, es un tipo de problema de la mochila (problema NP-completo) al que le aplican una serie de condiciones que hacen que pueda ser …"
resource: https://es.wikipedia.org/wiki/Problema_de_la_mochila_simple
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Problema_de_la_mochila_simple"}
license: CC BY-SA 4.0
id: eswiki-Problema_de_la_mochila_simple
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Problema de la mochila simple

El **problema de la mochila simple**, también llamado **problema de la mochila supercreciente**, es un tipo de problema de la mochila (problema NP-completo) al que le aplican una serie de condiciones  que hacen que pueda ser planteado como un problema de la suma de subconjuntos (problema NP-completo) que, si tiene solución, esta será única.

Este tipo de problemas tiene importantes aplicaciones en el mundo de la criptografía

Definición
Dados:
Un conjunto de m números enteros positivos S={S1, S2, ..., Sm}, ordenados de menor a mayor, donde la secuencia de los elementos cumplen la condición de que el elemento i-ésimo es mayor que la suma de los anteriores elementos (es una **secuencia supercreciente**). Matemáticamente

Un valor T que es el resultado de alguna de las posibles sumas de esos elementos,

Se debe encontrar S'={Sa, Sb, ..., Sj}, siendo S' el subconjunto de S cuya suma sea igual al valor T.

Resolución
La solución a este tipo de mochila es muy fácil debido a que la secuencia S es una secuencia supercreciente:

Se recorren los elementos de la mochila de mayor a menor comprobando si dicho valor es menor que T. Si es mayor, ese valor no estará en la suma y por tanto en la posición correspondiente del vector solución *xi* habrá un 0. En caso contrario tendrá un 1 y se continuará la resolución con los restantes elementos de la mochila para el problema T-Sj

Para este tipo de problemas, en el caso de que exista la solución, esta será única.

Aplicaciones
Clave simétrica
Un problema de la mochila simple puede usarse como clave secreta de una algoritmo de cifrado simétrico. Para ello lo que hay que hacer es representar la información que se quiera cifrar en binario y se pasa cada bit por la mochila por la secuencia  de números del conjunto S. Si un bit es 1 entonces se incluye en la suma el elemento que le corresponde. Si es un 0 entonces no se incluye.

Por ejemplo sea S = {2, 4, 10, 19, 40}. Por tanto m = 5. Supongamos que quiero cifrar el mensaje M = ADIOS. Pasando el mensaje a ASCII/ANSI( A = 01000001, D = 01000100, I = 01001001, O = 01001111, S = 01010011) tenemos el mensaje (agrupo de 5 en 5 ya que m=5)
M = 01000 00101 00010 00100 10010 10011 11010 10011
Haciendo las sumas de cada quinteto obtengo
C = (4), (10+40), (19), (10), (2+19), (2+19+40), (2+4+19), (2+19+40)= 4, 50, 19, 10, 21, 61, 25, 61
Que será el **mensaje cifrado**.

Para descifrar es receptor, que conoce S, recibe el mensaje C y opera de forma contraria resolviendo el problema de la mochila simple para cada uno de los valores de C.
Para obtener como suma un 4 la solución es 01000
50 -> 00101
19 -> 00010
10 -> 00100
21 -> 10010
61 -> 10011
25 -> 11010
61 -> 10011

Si uno todos los bits y agrupo en grupos de 8 bits (ANSI/ASCII) obtengo el mensaje original.

Esta forma de cifrar **no es segura** ya que es evidente que teniendo un suficientes pares, de mensaje originale y mensaje cifrado asociado, será muy fácil obtener la clave S con la que se está cifrando. Sin embargo esta forma de cifrar es muy rápida y puede será aprovechada en las aplicaciones de cifrado con clave asimétrica.

Clave asimétrica
La idea básica para usar una mochila simple en un sistema de criptografía asimétrica es conseguir una transformación secreta que transforme la mochila simple en una mochila general cuya resolución tenga un coste computacional alto. A esta mochila la llamaremos **mochila tramposa**. La clave pública será la mochila tramposa y con ella el emisor cifrará el mensaje de la misma forma que se hacía antes. La clave privada estará formada por los parámetros que permiten convertir el mensaje cifrado con la mochila tramposa en un mensaje cifrado con la mochila simple. Una vez obtenido esto el receptor puede descifrar el mensaje fácilmente usando la mochila simple.

En resumen, el esquema se basa en cifrar con una función unidireccional basada en un problema NP-completo (el problema de la mochila) que tienen una puerta trampa que aprovecha el receptor para descifrar el mensaje. Si no se dispone de esa puerta trampa, el proceso de descifrado, al ser un problema NP-completo, teóricamente tendría un coste computacional muy alto.

En esta idea se basa por ejemplo El criptosistema de Merkle-Hellman. Este algoritmo para hacer la transformción halla:
Un valor u tal que           donde  son los elementos de la mochila simple.
Un valor w entero tal que              (aseguramos la existencia de  en el grupo de los enteros de módulo u

La mochila tramposa se halla usando la expresión . Hay que verificar que la mochila tramposa así obtenida no sea una mochila fácil de resolver (no siempre es así).

Para descifrar el criptograma hay que aplicar  para cada una de las sumas C obtenidas al cifrar. A continuación cada valor suma transformado hay que descifrarlo de la forma habitual con la mochila simple original, lo cual es trivial.

Bibliografía
Jorge Ramió Aguirre,"Aplicaciones criptográficas: libro guía de la asignatura seguridad informática". Universidad Politécnica, Escuela Universitaria de Informática. Enero 1998.
