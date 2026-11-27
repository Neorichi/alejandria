---
type: Artículo de enciclopedia
title: OpenPuff
description: "OpenPuff Steganography and Watermarking, a veces abreviado en OpenPuff o Puff, es una herramienta libre de esteganografía para Microsoft Windows creada por Cosimo Oliboni y todavía desarrollada como software …"
resource: https://es.wikipedia.org/wiki/OpenPuff
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/OpenPuff"}
license: CC BY-SA 4.0
id: eswiki-OpenPuff
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# OpenPuff

- **Nombre:** OpenPuff
- **Desarrollador:** Eng. Cosimo Oliboni
- **Última versión:** 4.01
- **Sistema operativo:** Microsoft Windows
- **Género:** Esteganografía
- **Licencia:** GNU LGPL

**OpenPuff Steganography and Watermarking**, a veces abreviado en **OpenPuff** o **Puff**, es una herramienta libre de esteganografía para Microsoft Windows creada por Cosimo Oliboni y todavía desarrollada como software independiente. El programa es notable por haber sido uno de los primeros instrumentos de esteganografía (versión 1.01 liberada el diciembre de 2004) que:
 permite que los usuarios escondan datos en más que un solo portador. Cuando los datos ocultos se distribuyen entre un juego de portadores forman una cadena, sin algún límite del tamaño teórico (256MB, 512MB, ... depende solo de la implementación)
 implementa 3 niveles de ofuscación de los datos ocultos (criptografía, whitening y encoding)
 extiende la criptografía negable en la esteganografía negable

La última revisión soporta una gama amplia de formatos de portadores:
 Archivos de imagen Bmp, Jpg, Png, Tga
 Archivos de audio Aiff, Mp3, Wav
 Archivos de video 3gp, Mp4, Mpeg I, Mpeg II, Vob
 Archivos de Flash-Adobe Flv, Pdf, Swf

 Utilización

Se usa OpenPuff principalmente para intercambiar datos de forma asincrónica y anónima:
 el emisor trasmite un flujo de datos escondidos dentro de algunos portadores públicamente disponibles (contraseña + portadores+ orden de los portadores constituyen la clave secreta)
 el receptor recupera el flujo de datos ocultos usando la clave secreta
La ventaja de la esteganografía, en comparación con la sola criptografía, está que los mensajes elaborados por la esteganografía no atraen atención a sí mismos. Los mensajes cifrados, aunque robustos, engendran sospechas y pueden ser incriminatorios en países donde la criptografía es ilegal. Por lo tanto, mientras que el cifrado protege el contenido de un mensaje, puede decirse que la esteganografía protege mensajes y ambas las partes de la comunicación

Watermarking o marca de agua digital es la acción de firma un archivo con un ID que certifica el derecho de propiedad literaria. OpenPuff lo hace en una manera esteganográfica invisible, aplicando la esteganografía a cualquier formato de portador soportado. La marca invisible no está protegida por contraseña y es accesible por todos (usando el programa).

 Multi-criptografía

OpenPuff es un programa open source:
 la criptografía, el CSPRNG, el hash (usado para ampliar las contraseñas) y el scrambling son open source

Los algoritmos criptográficos (16, tomados del Advanced Encryption Standard process, NESSIE y CRYPTREC) se juntan en un algoritmo único de multi-criptografía:
 se inicializan las claves y los datos interiores estáticos para cada algoritmo **f**
 cada bloque de datos **D [ i ]** (128bit) está cifrado usando un algoritmo diferente **f [ i ]**
 **f [ i ]** es elegido por un oráculo aleatorio, inicializada por una segunda contraseña independiente

 1. Elección del algoritmo para el bloque **i**
 **f [ i ] = rand ( Oracle )**

 2. Aplicación en el bloque **i**
 **Cipher ( D [ i ] ) = f [ i ] ( D [ i ] )**

 Resistencia estadística

Numerosas pruebas han sido realizadas en las propiedades de la resistencia estadísticas de los módulos de CSPRNG y de multi-criptografía, usando: ENT, NIST y DIEHARD. Los resultados de las pruebas proceden de muestras de 64KB, 128KB. 256MB:
 prueba de entropía a nivel de bit > 7.9999xx / 8,000000
 prueba de compresión: 0% de reducción del tamaño después de la compresión
 prueba de la distribución chi-cuadrado: 40% < desviación < 60%
 prueba del valor medio: 127.4x/ 127,5
 prueba del método de Montecarlo: error < 0,01%
 prueba de correlación serial: < 0,0001

 Resistencia estegoanálitica

Seguridad, rendimiento y resistencia estegoanálitica son trade-off, objetivos contraditorios.

[Seguridad contra Rendimiento]: Whitening
 Pro: garantiza una mayor seguridad
 Pro: permite el cifrado negable
 **Contra 1**: requiere muchos carrier bits adicionales

[Seguridad contra Estegoanálisis]: Criptografía + Whitening
 Pro:  garantiza una mayor seguridad
 **Contra 2**: los portadores pueden ser identificados como "sospechosos" por la fuerte componente aleatoria.

Los datos, antes de ser inyectados en los portadores, son cifrados y sometidos a whitening: pequeñas cantidades de datos ocultos se convierten en grandes cantidades de datos pseudoaleatorios "sospechosos". El operación de inyección en los portadores utiliza una función no lineal de cobertura que toma también en input los bit originales del portador. Los portadores modificados necesitan de muchas menos modificaciones (**Contra 1**) y, decreciendo la respuesta pseudoaleatoria estadística, superan más pruebas estegoanáliticas (**Contra 2**).

 Esteganografía negable

Siempre habrá una probabilidad no nula de ser detectado incluso si los datos ocultos se comportan como un "portador natural" (por un efecto secundario impredecible, el ser detenido en delito flagrante...). Es posible resistir también a estos ataques imprevisibles, aunque si se vea obligado (por la coacción física o jurídica) a proporcionar una contraseña válida. La esteganografía negable (una técnica basada en la utilización de uno o más "señuelos") permite negar en modo convincente el hecho mismo que se ocultan datos sensibles: necesita solo proporcionar una contraseña de señuelo, revelar el atacante algunos datos no comprometedores y afirmar plausiblemente que no hay nada más.

 Referencias

 Enlaces externos

 HomePage
 SourcePage
