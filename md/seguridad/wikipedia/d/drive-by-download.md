---
type: Artículo de enciclopedia
title: Drive-by-download
description: "Drive-by-download significa dos cosas, ambas referidas a la descarga involuntaria de software de ordenador proveniente de Internet: Descargas autorizadas por una persona que no comprende las consecuencias (p. ej. …"
resource: https://es.wikipedia.org/wiki/Drive-by-download
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Drive-by-download"}
license: CC BY-SA 4.0
id: eswiki-Drive-by-download
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Drive-by-download

**Drive-by-download** significa dos cosas, ambas referidas a la descarga involuntaria de software de ordenador proveniente de Internet:
 Descargas autorizadas por una persona que no comprende las consecuencias (p. ej. descargas que instalan automáticamente una falsificación de un programa ejecutable, componente ActiveX, o applet de Java).
 Cualquier descarga realizada sin el conocimiento de una persona, a menudo un virus de ordenador, spyware, malware, o crimeware.
Drive-by-Download puede suceder visitando un sitio web, visualizando un mensaje de correo electrónico, pulsando sobre un mensaje emergente que muestre información engañosa, por ejemplo: un informe de error del sistema operativo, publicidad aparentemente inofensiva,... En tales casos, el «proveedor» puede reclamar que el usuario «consintió» la descarga, a pesar de que el usuario era de hecho inconsciente de haber autorizado la dicha descarga de software no deseada o maliciosa. De modo parecido si una persona está visitando un sitio con contenido malicioso, la puede llegar a ser víctima de un ataque Drive-by-download. El contenido malicioso puede ser capaz de explotar vulnerabilidades en el navegador o en complementos de este para ejecutar código maligno sin el conocimiento del usuario.

Un **drive-by-install** (o **instalación**) es un suceso similar. Hace referencia a la instalación más que a la descarga (aun así a veces la diferencia entre los dos términos es difusa y estos son empleados indistintamente).

 Proceso
Al crear un Drive-by-Download, un atacante debe crear primero su contenido malicioso para realizar el ataque. Con el aumento de los packs de exploit que contienen las vulnerabilidades necesarias para llevar a cabo ataques Drive-by-Download, el nivel de habilidad necesario para llevar a cabo este tipo de ataque se ha reducido.

El siguiente paso es alojar el contenido malicioso que el atacante desea distribuir. Una opción es que el atacante hospede el contenido malicioso en su propio servidor. Sin embargo, debido a la dificultad de dirigir a los usuarios a una nueva página, también puede alojarse en un sitio web legítimo que haya sido comprometido, o un sitio web legítimo que distribuye, sin saberlo, el contenido de los atacantes a través de un servicio de terceros (por ejemplo, un anuncio). Cuando el contenido es cargado por el cliente, el atacante analizará la huella digital del cliente para adaptar el código de cara a explotar las vulnerabilidades específicas de ese cliente.

Finalmente, el atacante explora las vulnerabilidades necesarias para lanzar el ataque Drive-by-Download. Generalmente este tipo de ataque usa dos estrategias: la primera está orientada a explorar la API de uno o varios plugins. Por ejemplo, la API DownloadAndInstall del componente ActiveX Sina no comprueba correctamente algunos parámetros permitiendo la descarga e instalación de archivos indeseados desde Internet. La segunda estrategia implica escribir shellcode en memoria, y entonces explorar vulnerabilidades del navegador web o de algún complemento para desviar el flujo de control del programa al propio shellcode.  Después de que este shellcode haya sido ejecutado, el atacante tiene la capacidad realizar accionar ladinas de forma remota. Esto podría incluir robar información valiosa para el atacante, pero más habitualmente implica la descarga e instalación de otras formas de malware.

Además del proceso descrito anteriormente, el atacante también puede tomar medidas para impedir detección durante el ataque. Un método es depender de la ofuscación del código malicioso, esto puede ser realizado a través del uso de IFrames.  Otro método es para encriptar el código malicioso para impedir su detección. Generalmente el atacante encripta este código en un ciphertext, entonces incluye también el método de desencriptado a continuación en el ciphertext.

 Detección
La detección de los ataques Drive-by-Download es un área activa de investigación. Algunos métodos de detección implican la detección de anomalías, que rastrean los cambios de estado en el sistema informático de un usuario mientras el usuario visita una página web. Esto implica supervisar el sistema informático del usuario para detectar cambios anómalos cuando se procesa una página web. Otros métodos de detección incluyen detectar cuando el código malicioso (shellcode) es cargado en memoria por el exploit de un atacante. Los métodos de detección también incluyen la creación de entornos en tiempo de ejecución que permiten al código JavaScript ejecutarse rastreando su comportamiento mientras es ejecutado. Otros métodos de detección incluyen examinar contenidos de páginas HTML para identificar características que se pueden utilizar para identificar páginas web maliciosas y utilizar características de servidores web para determinar si una página es maliciosa. Además, algunas herramientas antivirus utilizan firmas estáticas para emparejar patrones de secuencias de comandos maliciosas, aunque éstas no son muy eficaces debido a técnicas de ofuscación. Por último, la detección también se puede realizar mediante el uso de baja interacción o de alta interacción honeyclients.

 Véase también
 Hijacking
 Vulnerabilidad de Windows Metafile

 Referencias
