---
type: Artículo de enciclopedia
title: Cifrado de flujo
description: Un cifrado de flujo es un cifrado de clave simétrica en el que los dígitos de texto plano se combinan con un flujo de dígitos de cifrado pseudoaleatorio (flujo de claves).
resource: https://es.wikipedia.org/wiki/Cifrado_de_flujo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_de_flujo"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_de_flujo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado de flujo

Un **cifrado de flujo** es un cifrado de clave simétrica en el que los dígitos de texto plano se combinan con un flujo de dígitos de cifrado pseudoaleatorio (flujo de claves). En un cifrado de flujo, cada dígito de texto sin formato se cifra uno a la vez con el dígito correspondiente del flujo de claves, para dar un dígito del flujo de texto cifrado. Dado que el cifrado de cada dígito depende del estado actual del cifrado, también se conoce como ***cifrado de estado***. En la práctica, un dígito es típicamente un bit y la operación de combinación es un exclusivo-o (XOR).

El flujo de claves pseudoaleatorio se genera típicamente en serie a partir de un valor semilla aleatorio utilizando registros de desplazamiento digitales. El valor semilla sirve como clave criptográfica para descifrar el flujo de texto cifrado. Los cifrados de flujo representan un enfoque diferente del cifrado simétrico al cifrado de bloques. Los cifrados de bloque operan en grandes bloques de dígitos con una transformación fija e invariable. Esta distinción no siempre es clara: en algunos modos de funcionamiento, una primitiva de cifrado de bloque se utiliza de tal manera que actúa eficazmente como un cifrado de flujo. Los cifrados de flujo normalmente se ejecutan a una velocidad mayor que los cifrados de bloque y tienen menor complejidad de hardware. Sin embargo, los cifrados de flujo pueden ser susceptibles a graves problemas de seguridad si se utilizan incorrectamente (como en los ataques de cifrado de flujo); en particular, el mismo estado inicial (semilla) nunca debe usarse dos veces.

 Inspiración suelta de la libreta de un solo uso
Los cifrados de flujo se pueden ver como una aproximación a la acción de un cifrado irrompible probado, la libreta de un solo uso (OTP). Un teclado de una sola vez utiliza un flujo de claves de dígitos completamente aleatorios. El flujo de claves se combina con los dígitos de texto plano uno a la vez para formar el texto cifrado. Claude E. Shannon demostró que este sistema era seguro en 1949. Sin embargo, el flujo de claves debe generarse completamente al azar con al menos la misma longitud que el texto sin formato y no se puede usar más de una vez. Esto hace que el sistema sea complicado de implementar en muchas aplicaciones prácticas y, como resultado, la almohadilla de un solo uso no se ha utilizado ampliamente, excepto en las aplicaciones más críticas. La generación, distribución y gestión de claves son fundamentales para esas aplicaciones.

Un cifrado de flujo utiliza una clave mucho más pequeña y conveniente, como 128 bits. Basado en esta clave, genera una secuencia de claves pseudoaleatoria que se puede combinar con los dígitos de texto sin formato de una manera similar al pad de un solo uso. Sin embargo, esto tiene un costo. El flujo de claves ahora es pseudoaleatorio y, por lo tanto, no es verdaderamente aleatorio. La prueba de seguridad asociada con la libreta de un solo uso ya no es válida. Es muy posible que un cifrado de flujo sea completamente inseguro.

 Tipos
Un cifrado de flujo genera elementos sucesivos del flujo de claves en función de un estado interno. Este estado se actualiza esencialmente de dos maneras: si el estado cambia independientemente de los mensajes de texto sin formato o de texto cifrado, el cifrado se clasifica como un cifrado de flujo *síncrono* . Por el contrario, los cifrados de flujo de *sincronización automática* actualizan su estado en función de los dígitos del texto cifrado anterior.

 Cifrados de flujo sincrónico

En un **cifrado de flujo síncrono,** se genera un flujo de dígitos pseudoaleatorios independientemente del texto plano y los mensajes de texto cifrado, y luego se combina con el texto plano (para cifrar) o el texto cifrado (para descifrar). En la forma más común, se utilizan dígitos binarios (bits) y el flujo de claves se combina con el texto sin formato utilizando la operación exclusiva o (XOR). Esto se denomina **cifrado de flujo aditivo binario**.

En un cifrado de flujo síncrono, el remitente y el receptor deben estar exactamente en el mismo paso para que el descifrado sea exitoso. Si se agregan o eliminan dígitos del mensaje durante la transmisión, se pierde la sincronización. Para restaurar la sincronización, se pueden probar varias compensaciones de forma sistemática para obtener el descifrado correcto. Otro enfoque es etiquetar el texto cifrado con marcadores en puntos regulares de la salida.

Sin embargo, si un dígito se corrompe durante la transmisión, en lugar de agregarse o perderse, solo un dígito del texto sin formato se ve afectado y el error no se propaga a otras partes del mensaje. Esta propiedad es útil cuando la tasa de errores de transmisión es alta; sin embargo, hace menos probable que el error se detecte sin más mecanismos. Además, debido a esta propiedad, los cifrados de flujo síncronos son muy susceptibles a ataques activos: si un atacante puede cambiar un dígito en el texto cifrado, podría realizar cambios predecibles en el bit de texto plano correspondiente; por ejemplo, voltear un bit en el texto cifrado hace que el mismo bit se invierta en el texto sin formato.

 Cifrados de flujo de sincronización automática
Otro enfoque utiliza varios de los *N* dígitos de texto cifrado anteriores para calcular el flujo de claves. Estos esquemas se conocen como **cifrados de flujo de sincronización automática**, **cifrados de flujo asíncronos** o **clave automática de texto cifrado** (**CTAK**). La idea de la autosincronización se patentó en 1946 y tiene la ventaja de que el receptor se sincronizará automáticamente con el generador de flujo de claves después de recibir *N* dígitos de texto cifrado, lo que facilita la recuperación si se eliminan o se agregan dígitos al flujo de mensajes. Los errores de un solo dígito tienen un efecto limitado y solo afectan hasta *N* dígitos de texto sin formato.

Un ejemplo de un cifrado de flujo autosincronización es un cifrado de bloques en modo de la retroalimentación de cifrado (CFB).

 Basado en registros de desplazamiento de retroalimentación lineal
Los cifrados de flujo binario a menudo se construyen utilizando registros de desplazamiento de retroalimentación lineal (LFSR) porque se pueden implementar fácilmente en hardware y se pueden analizar matemáticamente fácilmente. Sin embargo, el uso de LFSR por sí solos es insuficiente para proporcionar una buena seguridad. Se han propuesto varios esquemas para aumentar la seguridad de las LFSR.

 Funciones de combinación no lineales

Debido a que los LFSR son inherentemente lineales, una técnica para eliminar la linealidad es alimentar las salidas de varios LFSR paralelos en una función booleana no lineal para formar un *generador de combinación*. Varias propiedades de dicha *función de combinación* son críticas para garantizar la seguridad del esquema resultante, por ejemplo, para evitar ataques de correlación.

 Generadores controlados por reloj
Normalmente, los LFSR se escalonan con regularidad. Un enfoque para introducir la no linealidad es hacer que el LFSR se sincronice de manera irregular, controlado por la salida de un segundo LFSR. Dichos generadores incluyen el generador de parada y arranque , el generador de pasos alternos y el generador de contracción .

Un generador de pasos alternos comprende tres LFSR, que llamaremos LFSR0, LFSR1 y LFSR2 por conveniencia. La salida de uno de los registros decide cuál de los otros dos se utilizará; por ejemplo, si LFSR2 emite un 0, LFSR0 se sincroniza, y si emite un 1, LFSR1 se sincroniza en su lugar. La salida es el OR exclusivo del último bit producido por LFSR0 y LFSR1. El estado inicial de los tres LFSR es la clave.

El generador intermitente (Beth y Piper, 1984) consta de dos LFSR. Un LFSR se sincroniza si la salida de un segundo es 1, de lo contrario, repite su salida anterior. Luego, esta salida se combina (en algunas versiones) con la salida de un tercer LFSR sincronizado a una velocidad regular.

El generador de contracción adopta un enfoque diferente. Se utilizan dos LFSR, ambos cronometrados regularmente. Si la salida del primer LFSR es 1, la salida del segundo LFSR se convierte en la salida del generador. Sin embargo, si el primer LFSR genera 0, la salida del segundo se descarta y el generador no genera ningún bit. Este mecanismo sufre de ataques de sincronización en el segundo generador, ya que la velocidad de la salida es variable de una manera que depende del estado del segundo generador. Esto se puede aliviar almacenando la salida en búfer.

 Generador de filtros
Otro enfoque para mejorar la seguridad de un LFSR es pasar todo el estado de un solo LFSR a una *función de filtrado* no lineal.

 Otros diseños

En lugar de un dispositivo de conducción lineal, se puede utilizar una función de actualización no lineal. Por ejemplo, Klimov y Shamir propusieron funciones triangulares (funciones T) con un solo ciclo en palabras de n bits.

 Seguridad
Para que un cifrado de flujo sea seguro, su flujo de claves debe tener un período largo y debe ser imposible *recuperar la clave del cifrado* o el estado interno del flujo de claves. Los criptógrafos también exigen que el flujo de claves esté libre de sesgos incluso sutiles que permitan a los atacantes *distinguir* un flujo de ruido aleatorio, y libre de relaciones detectables entre flujos de claves que correspondan a *claves* relacionadas o nones criptográficos relacionados. Eso debería ser cierto para todas las claves (no debería haber *claves débiles*), incluso si el atacante puede *saber* o *elegir* algún *texto plano* o *cifrado*.

Al igual que con otros ataques en criptografía, los ataques de cifrado de flujo pueden ser de *certificación,* por lo que no son necesariamente formas prácticas de romper el cifrado, pero indican que el cifrado podría tener otras debilidades.

El uso seguro de un cifrado de flujo síncrono seguro requiere que nunca se reutilice el mismo flujo de claves dos veces. Eso generalmente significa que se debe proporcionar un nonce o clave diferente para cada invocación del cifrado. Los diseñadores de aplicaciones también deben reconocer que la mayoría de los cifrados de flujo brindan no *autenticidad* sino *privacidad* : es posible que los mensajes cifrados se hayan modificado en tránsito.

Los períodos cortos para los cifrados de flujo han sido una preocupación práctica. Por ejemplo, los cifrados de bloque de 64 bits como DES se pueden utilizar para generar un flujo de claves en el modo de retroalimentación de salida (OFB). Sin embargo, cuando no se utiliza la retroalimentación completa, el flujo resultante tiene un período de alrededor de 232 bloques en promedio; para muchas aplicaciones, el período es demasiado bajo. Por ejemplo, si el cifrado se realiza a una velocidad de 8 megabytes por segundo, se repetirá una secuencia de bloques de período 232 después de aproximadamente media hora.

Algunas aplicaciones que utilizan el cifrado de flujo RC4 son atacables debido a debilidades en la rutina de configuración de claves de RC4; las nuevas aplicaciones deben evitar RC4 o asegurarse de que todas las claves sean únicas e idealmente no relacionadas (como las generadas por un CSPRNG bien sembrado o una función hash criptográfica) y que los primeros bytes del flujo de claves se descarten.

Los elementos de los cifrados de flujo suelen ser mucho más sencillos de entender que los cifrados de bloque y, por lo tanto, es menos probable que oculten debilidades accidentales o maliciosas.

 Uso
Los cifrados de flujo se utilizan a menudo por su velocidad y simplicidad de implementación en hardware y en aplicaciones donde el texto sin formato viene en cantidades de longitud desconocida, como una conexión inalámbrica segura. Si se usara un cifrado de bloque (que no opera en un modo de cifrado de flujo) en este tipo de aplicación, el diseñador debería elegir entre la eficiencia de transmisión o la complejidad de implementación, ya que los cifrados de bloque no pueden trabajar directamente en bloques más cortos que su tamaño de bloque. Por ejemplo, si un cifrado de bloque de 128 bits recibe ráfagas de texto sin formato de 32 bits, tres cuartas partes de los datos transmitidos serían de relleno. Los cifrados de bloque se deben utilizar en el robo de texto cifrado o en la terminación de bloque residual modo para evitar el relleno, mientras que los cifrados de flujo eliminan este problema al operar naturalmente en la unidad más pequeña que se puede transmitir (generalmente bytes).

Otra ventaja de los cifrados de flujo en la criptografía militar es que el flujo de cifrado se puede generar en una caja separada que está sujeta a estrictas medidas de seguridad y se alimenta a otros dispositivos, como un aparato de radio, que realizará la operación xor como parte de su función. Este último dispositivo se puede diseñar y utilizar en entornos menos estrictos.

ChaCha se está convirtiendo en el cifrado de flujo más utilizado en software; otros incluyen: RC4, A5/1, A5/2, Chameleon,  FISH,  Helix, ISAAC,  MUGI, Panama, Phelix,  Pike, Salsa20, SEAL,  SOBER, SOBER-128, y WAKE.

 Comparación

Trivia
 La National Security Agency de Estados Unidos a veces usa el término **algoritmos de tipo combinador**, refiriéndose a algoritmos que usan alguna función para combinar un generador de números pseudoaleatorios (PRNG) con un flujo de texto plano.

 Véase también
 LFSR
RC4

Notas

Referencias

Enlaces externos
En inglés:

 Criptoanálisis y diseño de cifrados de flujo (tesis de Hongjun Wu)
 Análisis de cifrados de flujo ligero (tesis de S. Fischer)
