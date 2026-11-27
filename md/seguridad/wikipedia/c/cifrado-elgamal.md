---
type: Artículo de enciclopedia
title: Cifrado ElGamal
description: El procedimiento de cifrado/descifrado ElGamal se refiere a un esquema de cifrado basado en el problema matemático del logaritmo discreto.
resource: https://es.wikipedia.org/wiki/Cifrado_ElGamal
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_ElGamal"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_ElGamal
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado ElGamal

El **procedimiento de cifrado/descifrado ElGamal** se refiere a un esquema de cifrado basado en el problema matemático del logaritmo discreto. Es un algoritmo de criptografía asimétrica basado en la idea de Diffie-Hellman y que funciona de una forma parecida a este algoritmo discreto.

El algoritmo de ElGamal puede ser utilizado tanto para generar firmas digitales como para cifrar o descifrar.

Fue descrito por Taher Elgamal en 1984 y se usa en software GNU Privacy Guard, versiones recientes de PGP, y otros sistemas criptográficos. Este algoritmo no está bajo ninguna patente lo que lo hace de uso libre.

La seguridad del algoritmo se basa en la suposición que la función utilizada es de un solo sentido debido a la dificultad de calcular un logaritmo discreto.

El procedimiento de cifrado (y descifrado) está basado en cálculos sobre un grupo cíclico cualquiera  lo que lleva a que la seguridad del mismo dependa de la dificultad de calcular logaritmos discretos en .

 El algoritmo original
Mostremos el criptosistema propuesto inicialmente por Tahar ElGamal en su artículo.

 Generación de la clave
Para generar la clave, Alicia escoge un número primo  cualquiera tal que el logaritmo discreto no es soluble en un tiempo asumible en  (grupo multiplicativo módulo un primo p). Esto último se traduce en que   tenga un factor primo grande (lo que hace que el problema del logaritmo discreto sea difícil).

Además Alicia elige dos números aleatorios  (el generador del grupo cíclico  y  (que actuará como clave privada) tal que .

Alicia calcula el valor de . La clave pública será , mientras que el valor de  lo mantendrá en secreto. Despejando   de la ecuación  obtenemos la relación siguiente entre los componentes de la clave pública y la clave privada  con lo que el criptosistema es seguro siempre que sea difícil hallar el logaritmo discreto.

 Cifrado
Supongamos que Bruce tiene un texto claro que quiere enviar cifrado a Alicia. Lo primero por hacer es convertir este texto en un entero m entre 1 y  . Esto no es parte del cifrado, sino que es una manera de codificar estándar, conocida por todos. Luego Bruce escoge arbitrariamente un número  (que mantendrá secreto) para finalmente calcular:

El mensaje cifrado final corresponde a la tupla

Descifrado

Para descifrar aprovechamos que:

Por tanto para descifrar se tiene que realizar el siguiente cálculo:

donde  representa el inverso de  módulo  lo que indica que para calcular el descifrado, es necesario conocer , que es la clave privada de Alicia.

Por el pequeño teorema de Fermat se demuestra que  y lo podemos aplicar.

Demostración: El pequeño teorema de Fermat indica que  con p primo y x>0 coprimo con p. Elevando a  la expresión obtenemos que . Por tanto . Despejando

 Ejemplos
 Simple
Alicia elige los valores:
 (**primo** aleatorio y suponemos que p-1=16 tiene un factor primo grande lo cual no es cierto)
 (**generador** aleatorio)
 (**clave privada** aleatoria)

Alicia calcula
 (valor calculado)
Por tanto la **clave pública** será .

Bruce tiene el **texto claro**
 (el cual está entre 1 y p-1)
Bruce escoge un  aleatorio entre 2 y p-1
Bruce calcula

.
Por lo que el **texto cifrado** es

Para descifrar Alicia usa la clave privada  y el Pequeño Teorema de Fermat:
.

 Complejo
Veamos una aplicación más real del algoritmo:

Alicia elige los valores:
 (**primo** aleatorio y para  suponemos que 52673 es sufientemente grande)
 (**generador** aleatorio)
 (**clave privada** aleatoria)

Alicia calcula
 (valor calculado)
Por tanto la **clave pública** será .

Bruce tiene el **texto claro** "HIJO"
 (el cual está entre 1 y p-1)
Bruce escoge un  aleatorio entre 2 y p-1

Bruce calcula

.
Por lo que el **texto cifrado** es  que al decodificarlo queda:
=BAGVLB
=SCEAZ
Con lo que el mensaje a enviar es (BAGVLB, SCEAZ)

Para descifrar Alicia usa la clave privada :
 ya que por el pequeño teorema de fermat tenemos

 Generalización
Lo único que se utiliza de la congruencia módulo  es que el conjunto  forma un grupo con las operaciones módulo  y que en dicho grupo el problema del logaritmo discreto resulta difícil.

Por lo tanto, puede cambiarse en este criptosistema al grupo  por cualquier otro grupo  en el que el logaritmo discreto sea complicado.

Por ejemplo, resulta bastante efectivo utilizar como grupo una curva elíptica sobre  (véase Criptografía de curva elíptica), ya que no se conoce un algoritmo de tiempo subexponencial capaz de resolver el problema del logaritmo discreto en curvas elípticas en general.

Propiedades

Efectividad
Hasta el momento el algoritmo ElGamal de cifrado/descifrado puede ser considerado un algoritmo efectivo.

Un adversario con la habilidad de calcular logaritmos discretos podría ser capaz de romper un cifrado ElGamal. Sin embargo, en la actualidad, el algoritmo de computación de logaritmos discretos (cuando trabajamos módulo un primo) es subexponencial con una complejidad de λ = 1/3, la misma que la de factorizar dos números primos, y por tanto, no es accesible de realizar tal tarea en números grandes en un tiempo razonable. El logaritmo discreto es aún más difícil si trabajamos en otros grupos (como por ejemplo, curvas elípticas).

Véase Récords en logaritmos discretos para una muestra de las posibilidades que da la computación actual a la hora de resolver este problema.

Maleabilidad
Existe un caso en que este algoritmo se vuelve maleable. Esto implica que bajo un ataque específico la seguridad de ElGamal se puede quebrar.
Este ataque usa el hecho de tener el texto cifrado  del texto claro  (ambos conocidos). Sabiendo esto se puede llegar a que el texto cifrado  corresponde al texto plano . Si ahora la persona que cifró el mensaje anterior genera otro texto cifrado  (utilizando el mismo  con el que cifró anteriormente) el adversario debería ser capaz de llegar al texto plano  correspondiente siguiente los siguientes pasos:
Calcular

 Buscar un  tal que  tomando en cuenta que  al igual que  cumple con estar entre  y

 Tomando el peor caso, el atacante obtendrá dos textos claros (debido a la función módulo).

Rendimiento
El análisis de rendimiento del algoritmo ElGamal es similar al de RSA.
Concretamente tenemos el siguiente análisis

 Sea  el módulo usado en ElGamal. Los procesos de cifrado y descifrado de ElGamal toman tiempos .

Homomórfico

El cifrado ElGamal es un cifrado homomórfico en la multiplicación. En efecto si:

entonces:

Prueba de conocimiento del texto original
Este tipo de cifrado permite probar el conocimiento del texto original cifrado sin tener que revelarlo (esta propiedad en inglés se llama *plaintext aware*). Por ejemplo esto es muy útil en sistemas de voto electrónico para asegurarnos de que el elector es el que realmente ha cifrado sus intenciones de voto y no las suministradas por un posible atacante. Para hacer la demostración se aprovecha del Algoritmo de identificación de Schnorr.

Para un texto cifrado de ElGamal , con el algoritmo de identificación de Schnorr, se prueba que P conoce b. Como la clave pública es   entonces si P conoce b, entonces se puede recuperar m calculando . Por tanto el protocolo prueba que P conoce el texto original m.

Prueba de recifrado
El Protocolo de Chaum-Pedersen puede ser usado para que un texto cifrado  es un recifrado de  sin revelar el factor de aleatorización s. La prueba de demostrar por el Protocolo de Chaum-Pedersen que  o lo que es lo mismo  que en ambos casos es igual a . Esto implica que existe un valor s que lo hace posible.

Prueba de cifrado de uno de los textos claros predefinidos
El Protocolo de Cramer-Damgard-Schoenmakers permite demostrar que un texto cifrado con **ElGamal** es el correspondiente a un texto claro de entre los posibles (los textos claros posibles tienen que estar predeterminados) sin revelar cual es. Esto es muy útil para votaciones electrónicas que usan este tipo de cifrado.

 Referencias
