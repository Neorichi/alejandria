---
type: Artículo de enciclopedia
title: Solitaire
description: "El algoritmo criptográfico Solitaire fue diseñado por Bruce Schneier a petición de Neal Stephenson para su uso en su novela Criptonomicón, en la que los agentes de campo lo utilizan para comunicarse de forma segura sin …"
resource: https://es.wikipedia.org/wiki/Solitaire
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Solitaire"}
license: CC BY-SA 4.0
id: eswiki-Solitaire
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Solitaire

El algoritmo criptográfico **Solitaire** fue diseñado por Bruce Schneier a petición de Neal Stephenson para su uso en su novela *Criptonomicón*, en la que los agentes de campo lo utilizan para comunicarse de forma segura sin tener que depender de la electrónica o tener que llevar herramientas incriminatorias. Fue diseñado para ser un sistema criptográfico manual calculado con una baraja ordinaria de jugar a las cartas . En *Criptonomicón*, este algoritmo se llamó originalmente **Pontifex** para ocultar el hecho de que se trataba de jugar a las cartas.

Una de las motivaciones detrás de la creación de Solitaire es que en entornos totalitarios, una baraja de cartas es mucho más asequible (y menos incriminatoria) que una computadora personal con una variedad de utilidades criptológicas. Sin embargo, como advierte Schneier en el apéndice de *Criptonomicón*, casi todas las personas interesadas en el criptoanálisis ahora conocerán este algoritmo, por lo que llevar una baraja de cartas también puede considerarse incriminatorio.

Desde su creación, el análisis ha revelado fallas en el cifrado. Ahora se considera inseguro.

 Cifrado y descifrado
Este algoritmo utiliza una baraja de cartas estándar con 52 cartas del mismo palo y dos comodines que se distinguen entre sí, llamados el comodín A y el comodín B. En aras de la simplicidad, en este ejemplo solo se utilizarán dos palos, tréboles y diamantes. A cada carta se le asigna un valor numérico: los tréboles se numerarán del 1 al 13 (del as al rey) y los diamantes se numerarán del 14 al 26 de la misma manera. A los comodines se les asignarán los valores de 27 y 28. Por lo tanto, la jota de tréboles tendría el valor 11 y el dos de diamantes tendría el valor 15. (En una baraja de cartas llena, los palos se valoran en orden de puente: tréboles, diamantes, corazones, espadas, con las cartas del mismo palo numeradas del 1 al 52, y los comodines numerados 53 y 54.)

Para comenzar el cifrado o descifrado, coloque la baraja de cartas boca arriba en el orden acordado previamente. La persona que descifra un mensaje debe tener una baraja dispuesta en el mismo orden que la baraja utilizada por la persona que cifró el mensaje. La forma en que se decide inicialmente el pedido depende de los destinatarios; Es preferible barajar el mazo perfectamente al azar, aunque existen muchos otros métodos.

El algoritmo genera un *flujo de claves*, una secuencia de valores que se combinan con el mensaje para cifrarlo y descifrarlo. Cada valor del flujo de claves se utiliza para cifrar un carácter del mensaje, por lo que el flujo de claves debe ser al menos tan largo como el mensaje. Si el flujo de claves es más largo que el mensaje, el mensaje puede rellenarse con un carácter repetido adicional, negando así al atacante el conocimiento de la longitud exacta del mensaje.

Para cifrar un mensaje (se asume que se refiere al inglés, idioma original de la novela, con alfabeto de 26 letras):

 Elimine toda la puntuación y los espacios, dejando solo las 26 letras A – Z.
 Convierta cada letra a su valor numérico natural, A = 1, B = 2, ..., Z = 26.
 Genere un valor de flujo de clave para cada letra del mensaje utilizando el algoritmo de flujo de clave siguiente.
 Sume cada valor de secuencia de claves al número de texto sin formato correspondiente, restando 26 si el valor resultante es mayor que 26 (en matemáticas, esto se llama aritmética modular).
 Convierta los números resultantes nuevamente a letras. Esta secuencia de letras es el texto cifrado.

Para descifrar un texto cifrado:

 Convierta cada letra del texto cifrado a su valor numérico natural.
 Genere un valor de flujo de claves para cada letra del texto cifrado.
 Reste cada valor de flujo de claves del valor de texto cifrado correspondiente, agregando 26 si el valor resultante es menor que 1.
 Convierta los números resultantes nuevamente a letras.

 Algoritmo de flujo de claves
Este algoritmo genera valores de flujo clave moviendo cartas dentro del mazo. El algoritmo de la secuencia de claves es *determinista*, por lo que los valores de la secuencia de claves dependen solo del orden inicial de la plataforma. Se supone que la baraja es una matriz circular, lo que significa que si una carta alguna vez necesita avanzar por debajo de la carta inferior en la baraja, simplemente rotará hacia la parte superior (en otras palabras, la primera carta sigue a la última). Tomaremos por ejemplo este mazo de inicio:
 1 4 7 10 13 16 19 22 25 28 3 6 9 12 15 18 21 24 27 2 5 8 11 14 17 20 23 26
Realice estos pasos para generar un carácter del flujo de claves:
 Localiza el comodín A (valor 27) y muévelo hacia abajo en la baraja un lugar. Si es la última carta, se convierte en la segunda carta. No hay forma de que se convierta en la primera carta. La baraja ahora se ve así:
 1 4 7 10 13 16 19 22 25 28 3 6 9 12 15 18 21 24 2 **27** 5 8 11 14 17 20 23 26
 Localiza el comodín B (valor 28) y muévelo hacia abajo en la baraja dos lugares. Tenga en cuenta que si es la penúltima carta, se convierte en la segunda carta envolviéndola. Si es la última carta, se convierte en la tercera carta. No hay forma de que se convierta en la primera carta.
 1 4 7 10 13 16 19 22 25 3 6 **28** 9 12 15 18 21 24 2 27 5 8 11 14 17 20 23 26
 Realice un "triple corte": divida la plataforma en tres secciones. Todo lo que esté arriba del comodín superior (que, después de varias repeticiones, puede que no sea necesariamente el comodín A) y todo lo que esté debajo del comodín inferior se intercambiará. Los propios comodines, y las cartas entre ellos, quedan intactos.
 **5 8 11 14 17 20 23 26** 28 9 12 15 18 21 24 2 27 **1 4 7 10 13 16 19 22 25 3 6**
 Realice un "corte de conteo": observe el valor de la carta en la parte inferior de la baraja. Si la carta es comodín, tome su valor en 27. Retire ese número de cartas de la parte superior de la baraja e insértelas justo encima de la última carta de la baraja.
 23 26 28 9 12 15 18 21 24 2 27 1 4 7 10 13 16 19 22 25 3 **5 8 11 14 17 20** 6
 Ahora, mire el valor de la carta superior. Una vez más, cualquiera de los comodines cuenta como 27. Cuente este número de lugares debajo de esa carta y tome el valor de esa carta como el siguiente valor en la secuencia de claves. Si la carta contada hasta es comodín, ignórela y repita el algoritmo de flujo de claves. En este ejemplo, la carta superior es 23, por lo que contamos hasta la 24ª carta, que es 11; por lo tanto, el valor de la secuencia de claves es 11. (Tenga en cuenta que ninguna tarjeta cambia de lugar en este paso, este paso simplemente determina el valor de la secuencia de claves).

 Criptoanálisis
En 1999, Paul Crowley descubrió que existe un sesgo hacia la repetición de caracteres en la secuencia clave, lo que ocurre aproximadamente cada 1 / 22.5 caracteres en lugar del esperado 1/26. Como resultado, Solitaire filtra información a una velocidad de aproximadamente 0,0005 bits por caracter. Si bien su seguridad quizás sea adecuada para mensajes muy cortos, en general Solitaire se considera inseguro.

Crowley también notó que, en algunos casos, hay dos configuraciones de plataforma diferentes que dan como resultado la misma configuración después de ejecutar el algoritmo de flujo de claves. Por ejemplo, cuando el comodín A está en la parte inferior del mazo o en la parte superior del mazo, se convertirá en la segunda carta después del paso 1. Esto significa que el algoritmo no siempre es reversible como Schneier había afirmado originalmente.

En 2019 Daniel Shiu propuso modificaciones al algoritmo que aumentarían su seguridad, a costa de dificultar al usuario la implementación manual.

 Véase también
 Bruce Schneier

 Referencias

 Enlaces externos
 Descripción del algoritmo
