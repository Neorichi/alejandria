---
type: Artículo de enciclopedia
title: Cifrado negable
description: En criptografía y esteganografía, el cifrado negable es un tipo de cifrado que permite negar en modo convincente que los datos están cifrados, o de ser capaz de descifrarlos.
resource: https://es.wikipedia.org/wiki/Cifrado_negable
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_negable"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_negable
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado negable

En criptografía y esteganografía, el **cifrado negable** es un tipo de cifrado que permite negar en modo convincente que los datos están cifrados, o de ser capaz de descifrarlos. La negación, aunque falsa, no puede ser verificada por el atacante sin la cooperación del usuario, que podría realmente no ser capaz de descifrar los datos. El cifrado negable sirve para socavar la confianza del atacante y su duda se convierte en otra forma de protección.

 Función

Normalmente, un texto cifrado puede ser descifrado en un solo texto simple. El cifrado negable permite al usuario descifrar el texto cifrado y producir, en caso necesario, un texto simple diferente que hace función de señuelo. El atacante, aunque esté en condición de forzar la producción de un texto simple, no puede revelar alguna diferencia entre el texto verdadero y aquello alternativo. El usuario puede siempre defenderse escogiendo, de vez en vez, cuál de los textos producir a partir desde el mismo texto cifrado.

El concepto "de cifrado negable" fue utilizado por Julian Assange y Ralf Weinmann en el Rubberhose filesystem y explicado en detalle en un documento elaborado por Ran Canetti, Cynthia Dwork, Moni Naor y Rafail Ostrovsky en 1996.

 Escenario

El cifrado negable permite al emisor desmentir el envío de un mensaje cifrado. Esto requiere un tercero de confianza. He aquí un escenario posible:

 Alice es la esposa de Bob, que sospecha que su mujer sea adúltera. Ella quiere comunicarse con su amante secreto Carl. Ella crea dos claves, una (K1) destinada a ser sacrificada y otra (K2) con la intención de mantenerla en secreto. Ella pasa la clave secreta a Carl.
 Alice construye un mensaje inocuo M1 para Carl (destinado a ser revelado a Bob en caso de emergencia) y un mensaje comprometedor M2 para Carl. M1 es cifrado con la clave K1 y M2 con la clave K2. En el momento de la codificación, M1 y M2 se fusionan en un único mensaje cifrado que se envía a Carl.
 Carl utiliza la clave secreta K2 para descifrar el mensaje y lee el texto secreto M2.
 Bob descubre el mensaje cifrado a Carl, se hace sospechoso y obliga Alice a descifrar el mensaje.
 Alice sacrifica la clave K1 y revela Bob el mensaje inocuo M1. Bob no sabe de la existencia de la otra clave y tiene que presumir que no hay otro mensaje M2.

Otro escenario posible es la creación de un mensaje cifrado con instrucciones secretas de Alice a Bob y Carl, que tienen que recibir instrucciones diferentes y no deben llegar a saber las instrucciones del otro. Carl puede recibir el mensaje solamente por el trámite de Bob.

 Alice construye el mensaje cifrado (M1 con K1 y M2 con K2) y lo envía a Bob.
 Bob utiliza su clave K1 y lee sus instrucciones M1. No puede leer M2.
 Bob reenvía el mensaje cifrado a Carl.
 Carl utiliza su clave K2 y lee sus instrucciones M2. No puede leer M1.

 Formas modernas de cifrado negable

Las técnicas modernas de cifrado negable explotan las propiedades de permutación pseudoaleatoria de los cifrados por bloques, por las que no es posible probar que el texto cifrado no coincide con datos aleatorios generados por un generador de números pseudoaleatorios criptográficamente seguro. Se utilizan también algunos datos de señuelo, que el usuario supuestamente quiere mantener en secreto y que serán revelados en caso de ataque, afirmando que esto es todo lo que hay. Esta forma de cifrado negable se refiere a veces como esteganografía.

Otro ejemplo de cifrado negable es el sistema de archivos cifrado que utiliza el concepto de niveles abstractos, donde cada nivel está cifrado con una clave diferente, y niveles adicionales especiales, con función de "chaff", llenos de datos aleatorios. El usuario almacena archivos de señuelo en uno o más niveles y niega la existencia de otros niveles con archivos ocultos, afirmando que el resto del espacio está ocupado solo por los niveles de chaff. Físicamente, estos sistemas de archivos se almacenan en un directorio único y todos los archivos tienen mismo tamaño y timestamp aleatorio. Los nombres son aleatorios - si pertenecen a niveles de chaff - o son hash criptográficos de las cadenas que identifican los bloques. El sistema de archivos Rubberhose y PhoneBookFS utilizan este enfoque.

Otro método, utilizado por algunos software de cifrado de disco, es la creación de un segundo volumen cifrado dentro de un volumen contenedor. El volumen contenedor está formateado con datos aleatorios cifrados y luego inicializado con un sistema de archivos que el usuario rellene con datos sensibles creíbles. Después se inserta internamente al volumen contenedor un segundo volumen oculto y cifrado, en lo que el usuario almacena datos secretos. Como en los otros ejemplos, la protección del volumen cifrado trae origen de las propiedades de permutación pseudoaleatoria de los cifrados por bloques.

La integridad del volumen cifrado depende de la posibilidad de no aumentar el tamaño de los datos contenidos en el volumen contenedor hasta sobrescribir el espacio oculto cifrado asignado en el interno. Tal vez puede ser necesario "congelar" en el tiempo el volumen contenedor para preservar aquello oculto, corriendo el riesgo de hacerlo sospechoso en consecuencia de los timestamp del último acceso y modificación nunca más actualizados. FreeOTFE y BestCrypt pueden contener más volúmenes cifrados en el interno de un volumen contenedor; TrueCrypt se limita a un volumen oculto.

 Críticas

La existencia de un volumen oculto puede ser comprometida por implementaciones con elementos criptográficos predecibles o por algunas herramientas forenses que pueden revelar la presencia de datos cifrados no aleatorios. También se sugirió una vulnerabilidad de los volúmenes cifrados por trámite de la prueba de aleatoriedad chi-cuadrado, por la que sería necesaria, después de cada modificación de los datos cifrados, la inclusión de elementos correctivos para llevar el volumen a una condición de aleatoriedad verosímil.

El cifrado negable fue criticado también por su imposibilidad de defender los usuarios contra el criptoanálisis de manguera de goma (Rubber-hose cryptanalysis). Algunos usuarios y proyectistas temen que la utilización misma de instrumentos que soporten el cifrado negable puede empujar los atacantes a no interrumpir la investigación, incluso si el usuario proporciona una contraseña válida.

 Véase también

 OpenPuff
 FreeOTFE
 TrueCrypt
 Esteganografía

 Referencias

 Bibliografía
