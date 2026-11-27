---
type: Artículo de enciclopedia
title: Código Lorenz
description: "La Lorenz SZ 40 y la SZ 42 (Schlüsselzusatz, que significa \"cifrado adjunto\") eran máquinas alemanas de cifrado utilizadas durante la Segunda Guerra Mundial en circuitos de teletipo."
resource: https://es.wikipedia.org/wiki/Código_Lorenz
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Código_Lorenz"}
license: CC BY-SA 4.0
id: eswiki-Código_Lorenz
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Código Lorenz

La **Lorenz SZ 40** y la **SZ 42** (***Schlüsselzusatz***, que significa "cifrado adjunto") eran máquinas alemanas de cifrado utilizadas durante la Segunda Guerra Mundial en circuitos de teletipo. Criptógrafos británicos, que se refirieron al tráfico alemán de datos de teletipo cifrados como "Fish", denominaron al aparato y su tráfico como "**Tunny**" (Atunes, Atún). Mientras la bien conocida Enigma fue usada generalmente por unidades de combate, la Máquina de Lorenz fue usada para comunicaciones de alto nivel. El ingenio en sí tenía unas medidas de 51cm × 46cm × 46cm, y funcionó como dispositivo adjunto a las máquinas de teletipo de Lorenz estándares. Los mecanismos implementaban un cifrado de flujo.

 Operación

Las máquinas teletipo generaban cada carácter como cinco bits paralelos en cinco líneas, comúnmente cifradas en Código Baudot o alguno similar. La máquina de Lorenz emitía grupos de cinco bits pseudoaleatorios para ser XOReados con Texto Plano. Los bits pseudoaleatorios eran generados por diez rodillos de pines, cinco de los cuales pasaban regularmente, rodillos identificados con el símbolo  ("chi"), y cinco de los cuales pasaban irregularmente, rodillos identificados con el símbolo  ("psi"). El paso de los rodillos  era determinado por dos o más rodillos de pines, llamados "rodillos motor". Además del paso de los cinco rodillos irregulares (que permanecían juntos), la máquina de Lorenz era en realidad un generador de cinco pseudoaleatorios en paralelo; no hay otra interacción entre las cinco líneas. El número de pines en todos los rodillos era primo relativo.

Estas máquinas eran parte del espíritu de las primeras propuestas por el Coronel Parker Hitt del Ejército de los Estados Unidos de América durante la Primera Guerra Mundial.

 Criptoanálisis
Criptógrafos británicos en Bletchley Park dedujeron la operación de la máquina en enero de 1942 sin haber visto nunca una máquina de Lorenz. Ese fue posible debido a un error cometido por un operador alemán. El 30 de agosto de 1941 un mensaje de 4000 letras fue transmitido, pero el mensaje no fue recibido correctamente del otro lado por lo cual el receptor envió un mensaje descifrado solicitando la retransmisión del mensaje original. Esto permitió a los "rompedores del código" saber que era lo que estaba ocurriendo. El mensaje fue retransmitido con la misma configuración de clave (HQIBPEXEZMUG), una práctica prohibida. Por otra parte, la segunda vez el operador realizó pequeñas alteraciones al mensaje, como utilizar abreviaciones. A partir de estos dos textos cifrados John Tiltman logró recuperar ambos mensajes en texto plano y el código de cifrado.
A partir del código de cifrado, la estructura completa de la máquina fue reconstruida por W. T. Tutte.

El tráfico fue interceptado en Knockholt, Kent, luego enviado a Bletchley Park.

Los británicos construyeron máquinas realmente complejas para atacar al sistema Tunny. Las primeras fueron una familia de máquinas conocidas como "Heath Robinsons", que usaban cintas magnéticas de "alta velocidad", construidas con circuitería lógica electrónica, para poder romper el sistema Tunny.

La siguiente fue Colossus, el primer computador electrónico digital del mundo (como ENIAC, éste no tenía programa almacenado, y fue programado mediante paneles de cableado). Era mucho más rápido y fiable que las Heath Robinsons; usándola, los británicos fueron capaces de leer una gran proporción de tráfico "Tunny".

El servicio sueco criptoanalítico, el FRA (Försvarets Radioanstalt), también "rompió" una primera versión del sistema de Lorenz; Su ruptura se produjo en abril de 1943. Se aprovecharon los cables de transmisión de datos entre Alemania y Noruega. El trabajo fue encabezado por el matemático Arne Beurling.

 Véase también
 STURGEON
 SIGCUM
 Newmanry
 Testery

 Lectura posterior
 Stephen Budiansky, *Battle of Wits* (Free Press, New York, 2000) Contains a short but informative section (pages 312-315) describing the operation of Tunny, and how it was attacked.
 Paul Gannon "Colossus: Bletchley Park's Greatest Secret" (Atlantic Books, 2006) Using recently declassified material and dealing exclusively with the efforts to break into Tunny. Clears up many previous misconceptions about Fish traffic, the Lorenz cipher machine and Colossus.
 F. H. Hinsley, Alan Stripp, *Codebreakers: The Inside Story of Bletchley Park* (Oxford University, 1993) Contains a lengthy section (pages 139-192) about Tunny, the British attack on it, and the British replicas of the Lorenz machine.
 Michael Smith, *Station X: Decoding Nazi Secrets* (TV Books, New York, 2001) Contains a lengthy section (pages 183-202) about Tunny and the British attack on it.

 Referencias
 Jack Good, Donald Michie, and Geoffrey Timms, *General Report on Tunny*, 1945, HW 25/4 and HW 25/5
 W. T. Tutte, *FISH and I* Transcript of a lecture by Prof. Tutte explaining how he broke into Tunny.
 Donald W. Davies, *The Lorenz Cipher Machine SZ42*, (reprinted in *Selections from Cryptologia: History, People, and Technology*, Artech House, Norwood, 1998)
 Entry for "Tunny" in the GC&CS *Cryptographic Dictionary*
 The Lorenz Cipher and how Bletchley Park broke it by Tony Sale

 Enlaces externos

 Lorenz ciphers and the Colossus
 Information on Lorenz
 Photographs and description of Tunny
