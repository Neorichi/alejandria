---
type: Artículo de enciclopedia
title: Protocolo de rellenado con paja y aventado
description: Se dice que un protocolo criptográfico es un protocolo de rellenado con paja y aventado cuando utiliza la técnica añadiendo paja y aventando (traducción del inglés chaffing and winnowing).
resource: https://es.wikipedia.org/wiki/Protocolo_de_rellenado_con_paja_y_aventado
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protocolo_de_rellenado_con_paja_y_aventado"}
license: CC BY-SA 4.0
id: eswiki-Protocolo_de_rellenado_con_paja_y_aventado
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protocolo de rellenado con paja y aventado

Se dice que un protocolo criptográfico es un *protocolo de rellenado con paja y aventado* cuando utiliza la técnica **añadiendo paja y aventando** (traducción del inglés *chaffing and winnowing*). El nombre de esta técnica viene derivado de la agricultura: Cuando se recoge el cereal se obtiene un compuesto en el que está mezclado la paja (inútil) y el grano (útil). Para separar el grano de la paja se echa al aire el compuesto y el viento se lleva la paja separándola así del grano. A este proceso se le llama **aventar** (en inglés *winnowing*).

De forma similar en 1998 Ron Rivestpropuso una técnica para conseguir confidencialidad en un canal inseguro. Para ello propone añadir tráfico de relleno (paja) a la comunicación útil (grano) y establecer un mecanismo de autenticación que permita al receptor del mensaje identificar la comunicación útil (el grano) ('aventar'). Por tanto el receptor como el emisor se tienen que poner de acuerdo en el mecanismo de autenticación a utilizar.

Ejemplo de funcionamiento
Veamos un ejemplo de como podríamos implementar esta técnica:
Supongamos que A quiere enviar un mensaje M a B. A divide el mensaje M en bits y cada bit lo envía en un paquete separado. Cada paquete a enviar va a contener:
Un número de serie que permita recomponer el mensaje M a partir del bit que se va recibiendo en cada paquete
El bit del dato
Un código de autenticación que autentica cada paquete y que es construido por una clave secreta compartida por A y B.
Estos paquetes constituyen lo que se llama el 'grano'.
Una vez construidos los paquetes anteriores A fabrica una serie de paquetes basura (tráfico de relleno) independientes de los paquetes anteriores, que siguen el mismo formato pero que en lugar del código de autenticación tienen un valor aleatorio. Estos paquetes constituyen lo que se llama la 'paja'.
A continuación A envía todos los paquetes (grano y paja) a B mezclados en cualquier orden. El receptor B filtrará sólo aquellos paquetes que contengan un valor válido del código de autenticación de mensajes ('aventa') y ordena los bits de datos obtenidos de acuerdo al número de serie obtenido en cada paquete.

Alguien que escuche el canal será incapaz de distinguir los paquetes útiles de los de relleno ya que no conoce la clave de autenticación compartida solo por A y por B.

Consideraciones
 El nivel de confidencialidad que provee la técnica está basado en la dificultad para un adversario de distinguir los paquetes irrelevantes de los que tienen carga útil. Por tanto depende de:

La fortaleza del mecanismo de autenticación;
Por ejemplo podríamos usar un código de autenticación de mensajes como HMAC-SHA1. Esta, vista desde fuera, es difícil de distinguirse de una función aleatoria y por tanto el adversario le será difícil distinguir la 'paja' del 'grano'

De como el mensaje original es partido en paquetes;
Si cada paquete útil contiene un solo bit de información del mensaje, entonces si el atacante obtiene un paquete es difícil, que este determine mirando esa información si el paquete es útil o de relleno. Si en lugar de meter un bit por paquete metemos varios entonces se mejorará la eficiencia del protocolo (sobrecarga producida por los paquetes de relleno). Sin embargo hay que tener en cuenta que cuanta más información metamos en un paquete, esta puede ser aprovechada por un atacante para poder distinguir mejor los paquetes con información útil del tráfico de relleno. Por ejemplo, no es lo mismo distinguir paquetes útiles si la parte del mensaje contenido en cada paquete es un bit, que si el contenido del mensaje en cada paquete es un texto en inglés.

De como se añaden los paquetes de relleno;
Cuanto más tráfico de relleno se introduzca, por un lado, tendremos más seguridad y, por otro lado, el uso de la red será más ineficiente (sobrecarga producida por los paquetes de relleno). Habrá que tomar decisiones de compromiso.
No se trata de meter paquetes de relleno sin más. El relleno tendrá que ser de calidad para que pueda ser aprovechado al máximo y que pueda confundir al atacante. Por ejemplo:
Los paquetes de relleno deberán de tener formato similar a los paquetes con carga útil.
 Los números de serie que tienen los paquetes de relleno tienen que coincidir con los paquetes de carga útil para que puedan confundirse. Si por ejemplo sólo hay un paquete que tiene cierto número de serie, entonces es bastante probable que ese número de serie se corresponda con un paquete con información útil. Por tanto es bueno que por cada paquete de carga útil haya al menos un paquete de relleno con el mismo número de serie.
 La parte del mensaje que va en los paquetes útiles tiene que ser similar a la parte que va en la misma posición en los paquetes de relleno para que así puedan confundirse ambos tipos de paquetes. Por ejemplo, si los paquetes con información útil contienen texto en inglés y los paquetes de relleno contienen bits aleatorios, entonces es trivial distinguir unos paquetes de otros.

Lo ideal sería que cada paquete útil contuviera sólo un bit del mensaje y que para cada paquete con información útil hubiera un paquete de relleno con el mismo número de serie que contuviera el bit complementario como la parte que corresponde al mensaje. En este caso distinguir unos paquetes de otros requeriría romer el algoritmo de autenticación usado. Con un buen algoritmo de autenticación el proceso proveería una confidencialidad perfecta del contenido del mensaje

 Supongamos que un atacante es suficientemente fuerte (Ejemplo gobierno con ley que le respalda) y puede forzar al emisor a revelarle la clave de autenticación usada. El emisor podría usar esa clave para generar una serie de paquetes que fueran aparentemente el tráfico útil de la comunicación y por otro lado tener una clave verdadera que utilizaría en algunos de los paquetes del tráfico de relleno. Esos paquetes, aparentemente del tráfico de relleno, serían los que realmente tienen los datos útiles. De esta forma el emisor y el receptor pueden establecer distintos canales usando distintos claves de autenticación y poniéndose de acuerdo en cual es en verdad el canal útil.

 En lugar de usar códigos de autenticación de mensajes podríamos usar esquemas de firma digital no denegables que pudieran ser verificadas solo por el receptor.

Esta técnica se añade a las dos técnicas tradicionales para conseguir confidencialidad en un canal inseguro: Cifrado y esteganografía. Aunque tiene similitudes con ambas técnicas no puede ser clasificada como ninguna de las dos. Por un lado no hay cifrado de datos ni descifrado, los datos viajan en claro y etiquetados con su número de serie. El proceso se parece a la esteganografía en que el mensaje real está enterrado dentro de un alto volumen de datos irrelevantes. Sólo el receptor conoce como separar la información relevante de la irrelevante para así poder leer el mensaje. Sin embargo en esteganografía los datos no relevantes es un mensaje útil en sí mismo o al menos lo parece. Sin embargo en esta nueva técnica los datos irrelevante son basura que está presente con el propósito único de ocultar el mensaje real. Otra diferencia con la esteganografía es que el contenido irrelevante no tiene que se insertado por el emisor del mensaje, puede ser introducido por otro. Puede ser introducido por una tercera parte ya sea intermediaria (Ej un  proxy) o que tenga acceso al mismo canal. El que introduce el mensaje no necesita conocer la clave de validación. Por ejemplo puede ser insertado por un Proveedor de Servicios de Internet para sus clientes. Esto podría ser aprovechado para reducir la sobrecarga producida por el tráfico de relleno. Si la introducción de los paquetes de relleno es realizada por el proveedor de servicios de internet, éste podría multiplexar varios mensajes de forma que los paquetes con carga útil de unos mensajes fueran la paja de otros mensajes y viceversa.

 Ventajas legales
 Esta técnica no usa cifrado y por tanto no tiene claves de cifrado/descifrado. Por tanto no le sería aplicable cualquier ley que obligara a permitir el descifrado de cualquier texto cifrado. Esta técnica convierte un mecanismo aparentemente diseñado para autenticación de datos para conseguir confidencialidad. Esto demuestra que no hay límites claros entre autenticación y cifrado. Cualquier ley que intent prohibir el cifrado fuerte mientras permiten la autenticación fuerte está condenada a ser inaplicable en la práctica.

 Esta técnica no está especialmente diseñada para ser práctica ya que gasta una gran ancho de banda para los paquetes irrelevantes (gran ineficiencia). Esta técnica no fue inventada para usarla de forma práctica, sino que fue publicada como una prueba de la existencia de una forma de enviar mensajes de forma confidencial sin tener que usar cifrado.

 Esta técnica permite al emisor denegar responsabilidad sobre el cifrado del mensaje. El emisor transmite el mensaje en claro. Aunque el emisor y el receptor comparten un secreto, ellos lo usan sólo para autenticación.

 Referencias
