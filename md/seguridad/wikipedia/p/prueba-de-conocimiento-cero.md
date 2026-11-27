---
type: Artículo de enciclopedia
title: Prueba de conocimiento cero
description: "En criptografía, un protocolo de conocimiento cero o prueba de conocimiento nulo, también conocidas por las siglas ZKP (del inglés Zero Knowledge Proof), es un protocolo criptográfico que establece un método para que …"
resource: https://es.wikipedia.org/wiki/Prueba_de_conocimiento_cero
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Prueba_de_conocimiento_cero"}
license: CC BY-SA 4.0
id: eswiki-Prueba_de_conocimiento_cero
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Prueba de conocimiento cero

En criptografía, un **protocolo de conocimiento cero** o **prueba de conocimiento nulo**, también conocidas por las siglas ZKP (del inglés *Zero Knowledge Proof*), es un protocolo criptográfico que establece un método para que una de las partes pruebe a otra que una declaración (generalmente matemática) es cierta, sin revelar nada más que la veracidad de la declaración.

 Ejemplo intuitivo

Hay una historia bien conocida que presenta algunas de las ideas de pruebas de conocimiento cero, publicado por primera vez por Jean-Jacques Quisquater y otros en su artículo "Cómo explicar pruebas de conocimiento cero a tus hijos".  Es una práctica común para etiquetar las dos partes en una prueba de conocimiento cero como Peggy (el probador de la declaración, *prover*) y Victor (el verificador de la declaración, *verifier*).

En esta historia, Peggy ha puesto al descubierto la palabra secreta que se utiliza para abrir una puerta mágica en una cueva. La cueva tiene forma de círculo, con la entrada en un lado y el bloqueo de la puerta mágica al otro lado. Víctor dice que va a pagarle por el secreto, pero no hasta que esté seguro de que ella realmente lo sabe. Peggy dice que va a decirle el secreto, pero no hasta que reciba el dinero. Ellos establecen un plan por el cual Peggy puede demostrar que conoce la palabra sin decírsela a Víctor.

En primer lugar, Víctor espera fuera de la cueva mientras que Peggy ingresa. Ellos etiquetan los caminos a la izquierda y derecha de la entrada A y B. Peggy toma al azar cualquier camino A o B. A continuación, Víctor entra en la cueva y grita el nombre de la ruta en la que quiere que Peggy regrese, ya sea A o B, elegidos al azar. Probar que ella realmente conoce la palabra mágica es fácil: ella abre la puerta, si es necesario, y vuelve a lo largo de la trayectoria deseada. Tenga en cuenta que Víctor no sabe cuál es el camino que ella ha elegido.

Sin embargo, supongamos que no conocía la palabra. Entonces, solo sería capaz de volver por el camino si Victor diese el nombre de la misma ruta por la que ella había entrado. Dado que Victor elegiría A o B al azar, habría una probabilidad del 50% de acertar. Si tuviera que repetir este truco muchas veces, por ejemplo 20 veces seguidas, su probabilidad de éxito sería prácticamente nula.

Por lo tanto, si Peggy fiablemente aparece en la salida que Víctor nombra, se puede concluir que es muy probable que conozca la palabra secreta.

Observe que también es posible demostrar que Peggy sabe la palabra si ella entra en una ruta y regresa en otra. Pero en este caso, Peggy prueba a todo el mundo que ella sabe la palabra. En el sistema donde Peggy toma una ruta al azar sin decirla a nadie, los de fuera pueden pensar que Peggy y Víctor tienen un acuerdo sobre la orden de rutas que Víctor va a gritar, entonces Peggy solo va a demostrar su conocimiento de la palabra a Víctor.

 Otro ejemplo: dos pelotas y un amigo daltónico

Imagina que tu amigo Víctor es daltónico rojo-verde (mientras que tú no lo eres) y que tenéis dos pelotas: una roja y otra verde, pero por lo demás idénticas. A Víctor, las pelotas le parecen completamente idénticas. Víctor no cree que las pelotas sean realmente distinguibles. Usted quiere demostrarle a Víctor que, en realidad, las bolas tienen colores diferentes, pero nada más. En concreto, no quiere revelar qué bola es la roja y cuál es la verde.

Este es el sistema de prueba. Le das las dos bolas a Víctor y él se las pone detrás de la espalda. A continuación, coge una de las bolas, la saca de detrás de la espalda y la muestra. A continuación, vuelve a colocarla detrás de la espalda y decide mostrar sólo una de las dos bolas, eligiendo una de las dos al azar con la misma probabilidad. Le preguntará: "¿He cambiado la bola?". Todo este procedimiento se repite tantas veces como sea necesario.

Por supuesto, observando el color de las bolas se puede saber con certeza si las ha cambiado o no. En cambio, si las bolas fueran del mismo color y, por lo tanto, indistinguibles, es imposible acertar con una probabilidad superior al 50%.

Como la probabilidad de que hayas acertado al azar en la identificación de cada ronda es del 50%, la probabilidad de haber acertado al azar en todas las rondas se aproxima a cero ("solvencia"). Si usted y su amigo repiten esta "prueba" varias veces (por ejemplo, 20 veces), su amigo debería convencerse ("completitud") de que las bolas son efectivamente de distinto color.

La prueba anterior es de conocimiento nulo porque tu amigo nunca aprende qué bola es verde y cuál es roja; de hecho, no adquiere ningún conocimiento sobre cómo distinguir las bolas ("conocimiento cero").
 Definición

Una prueba de conocimiento cero deben satisfacer tres propiedades:
 **Completitud**. Supongamos que la declaración es verdadera y se quiere probar. Si tenemos un verificador y un probador honestos (siguen el protocolo correctamente), el protocolo hará que el probador convenza con certeza al verificador de que la declaración es verdadera. Tal certeza depende de la aplicación pero, generalmente, implica que la probabilidad de fallo no es significativa en la práctica.
 **Solvencia**. Supongamos que la declaración es falsa. No existe un probador engañoso que pueda convencer al verificador honesto de que la declaración es verdad, excepto con alguna probabilidad pequeña.
 **Conocimiento cero**: Si la declaración es verdadera, un verificador engañoso no aprende otra cosa más que este hecho. Esto se formaliza mostrando que cada verificador engañoso tiene algún *simulador* que, teniendo en cuenta sólo la declaración a ser demostrada (y sin acceso al probador), puede producir una transcripción que "parece" una interacción entre el probador honesto y el verificador tramposo. Esta es la condición que la distingue dentro del conjunto de las pruebas de conocimiento.
Si se cumplen las dos primeras se dice que es una prueba de conocimiento.

Las pruebas de conocimiento cero no son pruebas en el sentido matemático del término, porque hay una probabilidad pequeña, el *error de solidez* (*soundness error*), de que un probador engañoso será capaz de convencer al verificador de una declaración falsa. En otras palabras, que son probabilistas y no deterministas. Sin embargo, hay técnicas para disminuir el error de la solidez a valores insignificantes.

Una definición formal de conocimiento cero tiene que usar algún modelo computacional, la más común es la de una máquina de Turing . Sean , y  máquinas de Turing. Un sistema de prueba interactiva con  para un lenguaje  es de conocimiento cero, si para cualquier tiempo polinomial probabilístico (PPT) verificador  existe un simulador PPT esperado  tal que:

El probador  se modela teniendo un poder de cálculo ilimitado (en la práctica, por lo general es una máquina de Turing probabilística). Intuitivamente, la definición establece que un sistema de prueba interactiva  es de cero-conocimiento, si para cualquier verificador , existe un simulador de  eficiente que puede reproducir la conversación entre  y  en cualquier entrada. La cadena de auxiliar  en la definición desempeña el papel de "conocimiento previo". La definición implica que  no puede utilizar ningún conocimiento previo  para extraer información de su conversación con , porque se demanda que  también tiene este conocimiento previo, entonces puede reproducir la conversación entre  igual que antes.

La definición que se da es el de perfecto conocimiento cero. El conocimiento cero computacional se obtiene al exigir que las opiniones de los supervisores  y el simulador sean computacionalmente indistinguibles , dada la cadena auxiliar.

Clasificación
Las pruebas de conocimiento cero pueden ser **interactivas** o **no interactivas**.
Pruebas de conocimiento cero interactivas
En las **pruebas de conocimiento cero interactivas**, también conocidas por las siglas **IZKP** (del inglés *Interactive Zero-Knowledge Proof*), tanto el probador como el verificador necesitan estar presentes durante la ejecución del protocolo. Las pruebas de conocimiento cero interactivas suelen tener la siguiente forma:
El probador genera un mensaje de compromiso indicando que conoce el secreto.
El verificador devuelve un desafío al probador. El desafío suele ser aleatorio.
El probador envía una respuesta al verificador. El cálculo de la respuesta necesita tener en cuenta el compromiso de que se posee el secreto, el desafío y el secreto.
Este proceso puede repetirse varias veces para asegurar la verificación.

Ejemplos de este tipo de algoritmos son:
Algoritmo de identificación de Schnorr
Protocolo de Chaum-Pedersen
Protocolo de Cramer-Damgard-Schoenmakers

Pruebas de conocimiento cero no interactivas
Las **pruebas de conocimiento cero no interactivas**, también conocidas por las siglas **NIZKP** (del inglés *Non-Interactive Zero-Knowledge Proof*), son pruebas de conocimiento cero que no necesitan que el verificador y el probador estén presentes durante la ejecución del protocolo. En estos protocolos el probador genera una transcripción del protocolo de tal forma que el verificador pueda verificarlo más tarde.

Para transformar una prueba interactiva en una no interactiva se suele usar la **heurística de Fiat-Shamir**.

 Véase también
 Protocolo criptográfico

 Notas

 Enlaces externos
