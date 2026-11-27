---
type: Artículo de enciclopedia
title: Criptoanálisis acústico
description: En criptografía, el criptoanálisis acústico es un tipo de ataque de canal lateral que aprovecha los sonidos emitidos por computadores o máquinas.
resource: https://es.wikipedia.org/wiki/Criptoanálisis_acústico
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptoanálisis_acústico"}
license: CC BY-SA 4.0
id: eswiki-Criptoanálisis_acústico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptoanálisis acústico

En criptografía, el **criptoanálisis acústico** es un tipo de ataque de canal lateral que aprovecha los sonidos emitidos por computadores o máquinas. El criptoanálisis acústico moderno está enfocado mayormente en los sonidos producidos por los teclados de ordenador y los sonidos de los componentes internos del computador, pero históricamente también ha sido aplicado a las impresoras de impacto y las máquinas de cifrado electromecánicas.

 Historia
Victor Marchetti y John D. Marks decidieron hacer públicas las intercepciones acústicas de los sonidos de la impresión del texto en claro de las máquinas de cifrado de la CIA.

Técnicamente este método de ataque se remonta a la época del hardware FFT que era lo suficientemente barato para llevar a cabo esta tarea - en este caso desde finales de los 60 hasta la mitad de los 70. Sin embargo, se conoce el uso de otros más primitivos, lo que significa que estos ataques acústicos se dieron en la mitad de los años 50.

En su libro Spycatcher, el extrabajador del MI5 Peter Wright, analiza el uso de un ataque acústico contra las máquinas de cifrado Egyptian Hagelin en 1956. A este ataque se le puso el nombre en clave de “ENGULF”
.

 Ataques conocidos
En 2004, Dimitri Asonov y Rakesh Agrawal, trabajadores del Centro de Investigación Almaden de IBM, anunciaron que los teclados de ordenador y los teclados utilizados en teléfonos y cajeros automáticos son vulnerables a los ataques basados en los sonidos producidos por diferentes teclas. Su ataque hizo uso de una red neuronal para reconocer qué tecla había sido pulsada. Analizando sonidos grabados, eran capaces de recuperar el texto que había sido introducido. Estas técnicas permiten al atacante utilizar dispositivos de escucha secreta para obtener contraseñas, números de identificación personal (PINs) y cualquier otra información introducida por teclado. En 2005, un grupo de investigadores de la Universidad de Berkeley en California llevaron a cabo varios experimentos prácticos demostrando la validez de este tipo de amenazas
.

También, en 2004, Adi Shamir y Eran Tromer demostraron que era posible dirigir ataques temporizados contra una CPU llevando a cabo operaciones criptográficas analizando variaciones en emisiones de sonidos. Las emisiones analizadas eran ruidos ultrasónicos que emanaban de condensadores y bobinas de la placa base de un computador, no emisiones electromagnéticas o el sonido audible para los humanos del refrigerador del computador.

Shamir y Tromer, junto con el nuevo colaborador Daniel Genkin y otros, consiguieron una exitosa implementación del ataque en un ordenador portátil con una versión de GnuPG (una implementación de RSA), usando un teléfono móvil localizado cerca del ordenador portátil y un micrófono localizado a unos 4 metros de distancia, y publicaron los resultados de su experimento en diciembre de 2013.

 Contramedidas
Este tipo de criptoanálisis puede ser destruido generando sonidos que están en el mismo espectro y la misma forma que los sonidos producidos al presionar una tecla. Si aleatoriamente reproduces sonidos producidas por teclas al ser presionadas, es posible que destruyas por completo este tipo de ataque. Es recomendable usar al menos 5 variaciones grabadas diferentes (36x5=180 variaciones) para cada tecla pulsada para evitar el tema de las huellas digitales de FFT. Alternativamente, el ruido blanco a un volumen considerable (que puede ser más simple de generar por repetición) también enmascarará las emanaciones acústicas de las teclas individuales.

 Referencias
