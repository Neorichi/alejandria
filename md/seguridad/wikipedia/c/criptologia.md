---
type: Artículo de enciclopedia
title: Criptología
description: "La criptología (del griego κρύπτos, kryptós, ‘oculto’, y λóγος, lógos, ‘estudio’) es la disciplina que estudia los sistemas de escritura secreta."
resource: https://es.wikipedia.org/wiki/Criptología
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptología"}
license: CC BY-SA 4.0
id: eswiki-Criptología
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptología

La **criptología** (del griego κρύπτos, *kryptós*, ‘oculto’, y λóγος, *lógos*, ‘estudio’) es la disciplina que estudia los sistemas de escritura secreta. Su objeto es el análisis y diseño de métodos que transforman los mensajes de manera que resulten difíciles o imposibles de interpretar por personas o entidades no autorizadas.

Objetivos

Con la aparición de las tecnologías de la información y la comunicación y el uso masivo de las comunicaciones digitales, se han producido un número creciente de problemas de seguridad. El objetivo de la criptología se ha generalizado para estudiar las técnicas que se encargan de **proporcionar** seguridad a la información.

Disciplinas que comprende

Los campos en los que se divide la criptología son:
Criptografía. Se ocupa del estudio de los algoritmos, protocolos y sistemas que se utilizan para proteger la información y dotar de seguridad a las comunicaciones y a las entidades que se comunican.
Criptoanálisis. Se ocupa de conseguir comprender el significado de mensajes construidos mediante criptografía sin tener autorización para ello. Podríamos decir que el criptoanálisis tiene un objetivo opuesto al de la criptografía. Su objetivo es buscar el punto débil de las técnicas criptográficas para explotarlas y así reducir o eliminar la seguridad que teóricamente aportaba esa técnica criptográfica. A cualquier intento de criptoanálisis se le llama **ataque**. Un ataque tiene éxito, y se dice que el sistema se ha **roto**, cuando el atacante consigue **romper** la seguridad que la técnica criptográfica aporta al sistema.
Esteganografía. Se ocupa de ocultar mensajes con información privada por un canal inseguro, de forma que el mensaje no sea ni siquiera percibido. Normalmente, el mensaje es escondido dentro de datos con formatos de vídeo, imágenes, audio o mensajes de texto. Los usos más frecuentes de estas técnicas son: transmitir cierta información entre entidades sin que sea detectada por terceros, incluir información imperceptible en objetos digitales (p. ej. imágenes, vídeos, audios) para permitir un mayor control del uso de esos objetos digitales (por ejemplo, para implementar huellas digitales o marcas de agua).
Estegoanálisis. Se ocupa de detectar mensajes ocultos con técnicas esteganográficas. Podríamos decir que el estegoanálisis tiene un objetivo opuesto al de la esteganografía. Su objetivo es buscar el punto débil de las técnicas esteganográficas para explotarlas y así reducir o eliminar la seguridad que teóricamente aportaba esa técnica esteganográfica. A cualquier intento de estegoanálisis se le llama **ataque**. Un ataque tiene éxito, y se dice que el sistema se ha **roto**, cuando el atacante **detecta** que se ha usado esteganografía y, por tanto, puede obtener el mensaje.

Algunos autores aplican el término **estegología** al compendio de esteganografía y estegoanálisis.

 Combinando esteganografía y criptografía

Es frecuente el uso conjunto de técnicas de esteganografía y criptografía. La combinación de estas dos herramientas mejora la seguridad de los datos a los que se aplica. La forma más habitual de combinación es aplicando en una primera etapa criptografía cifrando el texto plano. En una segunda etapa se aplica esteganografía para ocultar ese texto cifrado y así hacerlo irreconocible (por ejemplo, metiendo el texto cifrado en una imagen usando técnicas esteganográficas). El receptor de la información, que sabe cómo se ha ocultado el mensaje, sólo tiene que recuperarlo y descifrarlo con el algoritmo de descifrado. De esta forma se consigue doble seguridad: por un lado, el mensaje es difícil de detectar y, por otro, aunque fuera detectado, está protegido por técnicas criptográficas. Esta asociación entre esteganografía y criptografía es tan frecuente que las aplicaciones de la esteganografía se suelen clasificar en:
**Esteganografía pura**: Se aplica sólo esteganografía.
**Esteganografía de clave simétrica o secreta**: Se aplica esteganografía en combinación con criptografía de clave simétrica.
**Esteganografía de clave asimétrica o pública**: Se aplica esteganografía en combinación con criptografía de clave asimétrica.

Revelación de la información

Cuando se quiere saber la información que se están comunicando ciertas entidades, se utilizan diversas técnicas. Si las entidades que se comunican quieren ocultar la información, suelen recurrir a técnicas criptológicas. Para intentar anular este tipo de protección, se usan técnicas de criptoanálisis y de estegoanálisis. Este tipo de técnicas se emplean entre un conjunto muy amplio de tecnologías que tienen como objetivo revelar la información. Por ejemplo, es frecuente utilizar técnicas de detección e interceptación de señales, de análisis de tráfico, de análisis de paquetes o el estudio de los canales encubiertos.

 Véase también

 Criptografía
 Esteganografía
 Criptoanálisis
 Estegoanálisis

 Referencias

Enlaces externos

Criptohistoria - portal en español consagrado a la criptología
