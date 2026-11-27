---
type: Artículo de enciclopedia
title: Vocoder
description: "Un vocoder (nombre derivado de voice coder, «codificador de voz») es un analizador y sintetizador de voz. Fue desarrollado en la década de 1930 como un codificador de voz para telecomunicaciones."
resource: https://es.wikipedia.org/wiki/Vocoder
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Vocoder"}
license: CC BY-SA 4.0
id: eswiki-Vocoder
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Vocoder

Un **vocoder** (nombre derivado de *voice coder*, «codificador de voz») es un analizador y sintetizador de voz. Fue desarrollado en la década de 1930 como un codificador de voz para telecomunicaciones. Su primer uso fue la seguridad en radiocomunicaciones, donde la voz tiene que ser digitalizada, cifrada y transmitida por un canal de ancho de banda estrecho.

El vocoder se ha usado también como instrumento musical. Como instrumento, es usado con guitarras y sintetizadores y produce un sonido de «guitarra parlante» o «teclado parlante», según el instrumento. Los vocoders son usados con frecuencia para crear el sonido de un robot hablando, como en la canción *Mr. Roboto* de Styx. También ha sido utilizado con frecuencia en música electrónica y hip hop, por ejemplo, Beastie Boys rescataron este efecto a finales de los noventa en su popular *Intergalactic*.

Anteriormente fue ampliamente empleado por el grupo alemán Kraftwerk durante los años 70s por lo que son considerados los padres de la música electrónica experimental y todas sus variantes, siendo algunas de sus más conocidas interpretaciones *Die Roboter* y *Autobahn*.

El vocoder está relacionado con el algoritmo denominado *phase vocoder*, aunque esencialmente es diferente de este.

 Cómo funciona un vocoder

 Teoría del vocoder
La voz humana consiste en sonidos generados por la apertura y cierre de la glotis (cuerdas vocales), lo que produce una onda periódica con muchos sonidos armónicos. Este sonido básico es entonces filtrado por la nariz y la garganta (un complicado sistema resonante conocido como el tracto vocal) de forma controlada, creando la amplia variedad de timbres del habla. Hay otro conjunto de sonidos, conocidos como sordos, que no son generados por la vibración de las cuerdas vocales.

El vocoder examina el habla encontrando su onda básica, que es la frecuencia fundamental, y midiendo cómo cambian en el tiempo las características espectrales, es decir los formantes, que son bandas de frecuencia donde se concentra la mayor parte de la energía sonora de un sonido, grabando el habla. Esto da como resultado una serie de números representando esas frecuencias modificadas en un tiempo particular a medida que el usuario habla. Al hacer esto, el vocoder reduce en gran medida la cantidad de información necesaria para almacenar el habla. Para recrear el habla, el vocoder simplemente revierte el proceso, creando la frecuencia fundamental en un oscilador electrónico y pasando su resultado por una serie de filtros basado en la secuencia original de símbolos.

 Primeros vocoders
Muchos vocoders usan un gran número de canales, cada uno en una frecuencia. Los diversos valores de esos filtros no son almacenados como números, que están basados en la frecuencia original, sino por una serie de modificaciones que el fundamental necesita para ser modificado en la señal vista en el filtro. Durante la reproducción esos números son enviados de vuelta a los filtros y entonces se modifican con el conocimiento de que el habla varía típicamente entre esas frecuencias. El resultado es habla inteligible, aunque algo mecánica. Los vocoders a menudo incluyen también un sistema para generar sonidos sordos, usando un segundo sistema consistente en un generador de ruido en lugar de la frecuencia fundamental.

Un ejemplo de uno de los primeros vocoders es el *Sonovox* que fue usado en una buena cantidad de canciones desde la década de 1940 a la década de 1960, y se usó para crear la voz de Casey Junior, el tren de *Dumbo* y el piano de *El Piano Mágico de Sparky*.

 Vocoders basados en predicción lineal
Desde finales de la década de 1970, muchos vocoders no musicales se han empleado usando predicción lineal, donde la envolvente espectral de la señal se estima por un filtro digital IIR todo polos. En codificación lineal predictiva, el sistema todo-polos reemplaza el banco de filtros paso-banda de su predecesor y se usa en el *encoder* para blanquear la señal (aplanar su espectro) y de nuevo en el decodificador para reasignar la envolvente espectral de la señal de voz original. En contraste con los vocoders realizados usando bancos de filtros, la localización de los picos espectrales está determinada totalmente por la señal objetivo y no necesita ser armónica, es decir, un múltiplo de la frecuencia fundamental.

 Implementaciones modernas del vocoder
Incluso con la necesidad de grabar muchas frecuencias y los sonidos sordos, la compresión del vocoder es impresionante. Los sistemas estándar de grabación de habla registran un rango de frecuencias entre 500 Hz y 3400 Hz (ancho de banda habitual en telefonía), requieren 64 kbits/s de ancho de banda, según el Teorema de muestreo de Nyquist-Shannon. Sin embargo, un vocoder puede proporcionar una simulación razonablemente buena con menos de 2400 bits/s de ancho de banda.

Muchos vocoders se usan en los sistemas de cifrado de la NSA:
 LPC-10, FIPS Pub 137, 2400 bit/s, que usa codificación lineal predictiva.
 *Code Excited Linear Prediction*, (CELP), 2400 and 4800 bit/s, Federal Standard 1016, usado en STU-III.
 *Continuously Variable Slope Delta-modulation* (CVSD), 16 kbit/s, usado en cifradores de banda ancha como el KY-57.
 *Mixed Excitation Linear Prediction* (MELP), MIL STD 3005, 2400 bit/s, usado en la *Future Narrowband Digital Terminal* FNBDT.
 *Adaptive Differential Pulse Code Modulation* (ADPCM), anterior ITU-T G.721, 32Kbit/s usado en el teléfono seguro STE.

ADPCM no es un vocoder propiamente dicho sino un codificador general de formas de onda. ITU ha reunido G.721 con algunos otros codificadores ADPCM en la recomendación G.726.

 Aplicaciones musicales
Para las aplicaciones musicales, una fuente de sonidos musicales se usa como portadora, en lugar de extraer la frecuencia fundamental. Por ejemplo, se puede usar el sonido de una guitarra como la entrada del banco de filtros, una técnica popular en la década de 1970.

En 1970, los pioneros de la música electrónica Wendy Carlos y Robert Moog desarrollaron uno de los primeros vocoders verdaderamente musicales. Un dispositivo de diez bandas inspirado por los diseños de vocoder de Homer Dudley, que recibió el nombre de codificador-decodificador de espectro, y más tarde nominado simplemente como vocoder. La señal portadora es un sintetizador modular de Moog, y se modulaba a partir de la entrada de un micrófono. La salida del vocoder de diez bandas era bastante inteligible, pero necesitaba de un habla especialmente articulada. Algunas mejoras posteriores usan un filtro de frecuencias de paso alto para permitir la producción de un sonido sibilante; esto no es conveniente para la aplicación original de codificación del habla, pero hace que el «sintetizador parlante» sea mucho más inteligible.

El vocoder de Carlos y Moog fue usado en muchas grabaciones, incluyendo la banda sonora de la película *La naranja mecánica*, dirigida por Stanley Kubrick, donde el vocoder «canta» la parte vocal de la Novena Sinfonía de Ludwig van Beethoven. También aparece en una canción llamada *Timesteps*.

A finales de la década de 1970, el vocoder empezó a usarse en música pop, especialmente en la llamada música disco. El grupo Alan Parsons Project usó un vocoder en su primer álbum *Tales of Mistery and Imagination*, al igual que la Electric Light Orchestra en algunos de sus principales éxitos (Mr. Blue Sky). El vocoder ha aparecido en grabaciones pop regularmente desde entonces. Artistas electrónicos experimentales (muchos de ellos formaron parte más tarde del género New Age) también utilizaron ocasionalmente el vocoder. Otros artistas que han hecho del vocoder una parte esencial de sus trabajos son el grupo alemán Kraftwerk, Herbie Hancock, Stevie Wonder en *I just called to say I love you* y Phil Collins, quien usó el efecto para acentuar ciertas palabras para dar un efecto dramático en su canción *In the Air Tonight*.

Recientemente fue utilizado por la cantante estadounidense Britney Spears en Su Canción It Should Be Easy, perteneciente a su octavo álbum de estudio "Britney Jean".

Tampoco debemos olvidar su utilización por músicos de jazz, muy especialmente Joe Zawinul tanto en Weather Report como con Zawinul Syndicate.

También fue utilizado por Mike Shinoda de la banda de Nu Metal Linkin Park en la mayoría de sus canciones del álbum "A Thousand Suns".

Otro uso singular de los vocoder fue el que le dio la banda de rock británica Queen a la canción *Radio Ga Ga* en donde era utilizado, como enfatizador en los coros y algunos arreglos en los versos. Este hecho era más notorio en los conciertos.

Daft Punk es un claro ejemplo, ya que la mayoría de música que ellos producen es con vocoder, no con Auto-Tune.

Este uso del vocoder no debe ser confundido con el efecto de guitarra inventado por Doug Forbes y popularizado por Peter Frampton llamado talkbox. En este efecto, el sonido amplificado es enviado por un tubo a la boca del músico y entonces toma forma mediante los movimientos de sus labios, lengua y boca antes de ser recogido por un micrófono. Stevie Wonder usó el talkbox ingeniosamente, no con la amplificación de la guitarra eléctrica, sino con el sintetizador, lo que fue aún más popularizado por Roger Troutman de la banda de funk Zapp en temas como *More Bounce To The Ounce*. La canción *Livin' on a Prayer* de Bon Jovi es una grabación más reciente con este efecto. En contraste, el efecto del vocoder se produce de forma completamente electrónica. Tampoco está basado en esta técnica el efecto del *Órgano que habla* desarrollado en los años 50 sobre los Órganos Hammond.

La codificación por predicción lineal se usa también como efecto musical (generalmente para síntesis cruzada de timbres musicales), pero no es tan popular como los bancos de filtros del vocoder, y el uso musical de la palabra *vocoder* se refiere exclusivamente a este último tipo de dispositivo.

 TV y cine
Los vocoders se han usado también en televisión y cine, normalmente por robots o computadores parlantes.

 Transformers — Los efectos vocales fueron creados con vocoders. Además se usó para darle la voz de Soundwave en la caricatura.
 Los Cylons de *Battlestar Galactica* usaban un vocoder de Roland para crear su voz.
 Wendy Carlos utilizó un vocoder para la banda sonora de *La naranja mecánica*, de Stanley Kubrick.
 Se usó un vocoder en la banda sonora de la película *Donnie Darko* para crear tensión y misterio.
 Las voces de Dalek en *Doctor Who* fueron creadas usando un *ring modulator*, no un vocoder.
 El programa de televisión Muchachada nui utiliza el aparato de forma frecuente a partir del final de la 2.ª temporada y en los capítulos emitidos de la 3.ª y la 4.ª.

 Véase también
 Audio de alta gama
 Dolby Surround
 Full-HD Voice
 HD Radio
 Vocaloid
 Dispositivo generador de voz

 Enlaces externos

 Vocoders en el explorador Vintage
 Implementación GPL de un vocoder, como plugin de LADSPA
 Varios enlaces sobre compresión de habla
 Eiosis ELS Vocoder
