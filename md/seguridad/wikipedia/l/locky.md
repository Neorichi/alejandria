---
type: Artículo de enciclopedia
title: Locky
description: Locky es un malware de tipo ransomware lanzado en 2016.
resource: https://es.wikipedia.org/wiki/Locky
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Locky"}
license: CC BY-SA 4.0
id: eswiki-Locky
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Locky

- **Nombre:** LOcky
- **Desarrollador:** Necurs
- **Licencia:** GNU General Public License
- **Género:** Ransomware
- **Idiomas:** Inglés

**Locky** es un malware de tipo ransomware lanzado en 2016. Se distribuye por correo electrónico (supuestamente una factura que requiere pago) con un documento de Microsoft Word adjunto que contiene macros maliciosas. Cuando el usuario abre el documento, parece estar lleno de texto sin sentido e incluye la frase «Habilite las macros si la codificación de datos es incorrecta», una técnica de ingeniería social. Si el usuario habilita las macros, se guarda y ejecuta un archivo binario que descarga el troyano de cifrado real, que cifrará todos los archivos que coincidan con extensiones específicas. Los nombres de los archivos se convierten en una combinación única de 16 letras y números. Inicialmente, solo se utilizaba la extensión de archivo .locky para estos archivos cifrados. Posteriormente, se han utilizado otras extensiones de archivo, como .zepto, .odin, .aesir, .thor y .zzzzz. Tras el cifrado, un mensaje (que se muestra en el escritorio del usuario) le indica que descargue el navegador Tor y visite un sitio web específico operado por delincuentes para obtener más información.

El sitio web contiene instrucciones que exigen el pago de un rescate de entre 0,5 y 1 bitcoin (en noviembre de 2017, el valor de un bitcoin oscilaba entre 9000 y 10 000 dólares en el mercado de intercambio de bitcoins). Dado que los delincuentes poseen la clave privada y controlan los servidores remotos, las víctimas se ven motivadas a pagar para descifrar sus archivos. Las criptomonedas son muy difíciles de rastrear y son muy fáciles de transferir.

 Operación
El mecanismo de infección más común consiste en recibir un correo electrónico con un documento de Microsoft Word adjunto que contiene el código. El documento es incomprensible y solicita al usuario que habilite las macros para poder verlo. Al habilitar las macros y abrir el documento, se activa el virus Locky. Una vez iniciado, el virus se carga en la memoria del sistema del usuario, cifra los documentos como archivos hash.locky, instala archivos .bmp y .txt, y puede cifrar los archivos de red a los que el usuario tiene acceso. Esta ruta es diferente a la de la mayoría de los programas de rescate, ya que utiliza macros y archivos adjuntos para propagarse, en lugar de instalarse mediante un troyano o utilizar un exploit previo.

 Actualizaciones
El 22 de junio de 2016, Necurs lanzó una nueva versión de Locky con un nuevo componente de carga, que incluye varias técnicas para evitar la detección, como detectar si se está ejecutando dentro de una máquina virtual o dentro de una máquina física, y la reubicación del código de instrucciones.

Desde el lanzamiento de Locky, han aparecido numerosas variantes que utilizan diferentes extensiones para los archivos cifrados. Muchas de estas extensiones reciben el nombre de dioses de la mitología nórdica y egipcia. Cuando se lanzó por primera vez, la extensión utilizada para los archivos cifrados era .Locky. Otras versiones utilizaban las extensiones .zepto, .odin, .shit, .thor, .aesir y .zzzzz para los archivos cifrados. La versión actual, lanzada en diciembre de 2016, utiliza la extensión .osiris para los archivos cifrados.

 Métodos de distribución
Desde que se lanzó el ransomware Locky, se han utilizado muchos métodos de distribución diferentes. Estos métodos de distribución incluyen kits de explotación, archivos adjuntos de Word y Excel con macros maliciosas, archivos adjuntos DOCM y archivos adjuntos JS comprimidos.

El consenso general entre los expertos en seguridad para protegerse del ransomware, incluido Locky, es mantener actualizados los programas instalados y abrir solo los archivos adjuntos de remitentes conocidos.

 Cifrado
Locky utiliza el cifrado RSA-2048 + AES-128 con modo ECB para cifrar archivos. Las claves se generan en el lado del servidor, lo que hace imposible el descifrado manual, y el ransomware Locky puede cifrar archivos en todas las unidades fijas, unidades extraíbles, unidades de red y unidades de disco RAM.

 Prevalencia
Se informa que Locky se envió a aproximadamente medio millón de usuarios el 16 de febrero de 2016, y que inmediatamente después del ataque los atacantes aumentaron su distribución a millones de usuarios. A pesar de la nueva versión, los datos de Google Trend indican que las infecciones han disminuido alrededor de junio de 2016.

 Vector de correo electrónico no deseado
Un ejemplo de mensaje con Locky como archivo adjunto es el siguiente:

*Estimado (nombre del usuario):*

*Adjuntamos nuestra factura por los servicios prestados y los gastos adicionales en el asunto mencionado anteriormente.*

*Esperando que lo anterior sea de su satisfacción, quedamos a su disposición.*

*Atentamente,*

*(nombre del usuario)*

*(título aleatorio)*

 Referencias
