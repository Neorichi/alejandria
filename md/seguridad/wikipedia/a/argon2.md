---
type: Artículo de enciclopedia
title: Argon2
description: Argon2 es una función de derivación de clave que fue seleccionada como la ganadora del concurso de comprobación de contraseñas de 2015.
resource: https://es.wikipedia.org/wiki/Argon2
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Argon2"}
license: CC BY-SA 4.0
id: eswiki-Argon2
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Argon2

**Argon2** es una función de derivación de clave que fue seleccionada como la ganadora del concurso de comprobación de contraseñas de 2015. Fue diseñada por Alex Biryukov, Daniel Dinu, y Dmitry Khovratovich de la Universidad de Luxemburgo. La implementación de referencia de Argon2 se publica bajo una licencia Creative Commons CC0 (es decir, de dominio público) o la Apache License 2.0, y proporciona tres versiones relacionadas:

 Argon2d maximiza la resistencia a los ataques de cracking por GPU. Accede al array en memoria en un orden dependiente de la contraseña, lo que reduce la posibilidad de ataques de compensación tiempo-memoria (TMTO), pero introduce posibles ataques de canal lateral.
 Argon2i está optimizado para resistir ataques de canal lateral. Accede al array de memoria en un orden independiente de la contraseña.
 Argon2id es una versión híbrida. Sigue el enfoque de Argon2i en la primera mitad del recorrido de la memoria y el enfoque de Argon2d en los recorridos posteriores. El RFC 9106 recomienda usar Argon2id si no conoces la diferencia entre los tipos o consideras los ataques de canal lateral como una amenaza viable.

Los tres modos permiten la especificación de tres parámetros que controlan:

 Tiempo de ejecución
 Memoria requerida
 Grado de paralelismo

 Criptoanálisis
Aunque no existe un criptoanálisis público aplicable a Argon2d, hay dos ataques publicados contra la función Argon2i. El primer ataque es aplicable solo a la versión antigua de Argon2i, mientras que el segundo se ha extendido a la versión más reciente (1.3).

El primer ataque muestra que es posible calcular una función Argon2i de una pasada utilizando entre una cuarta y una quinta parte del espacio deseado sin penalización de tiempo, y calcular una Argon2i de múltiples pasadas utilizando solo N/e (≈ N/2.72) de espacio sin penalización de tiempo. Según los autores de Argon2, este vector de ataque fue solucionado en la versión 1.3.

El segundo ataque muestra que Argon2i puede ser computado por un algoritmo que tiene complejidad O(n7/4 log(n)) para todas las opciones de parámetros  (costo de espacio),  (costo de tiempo), y cantidad hilos de tal manera que n=σ∗τ. Los autores de Argon2 afirman que este ataque no es eficiente si se usa Argon2i con tres o más pasadas. Sin embargo, Joël Alwen y Jeremiah Blocki mejoraron el ataque y demostraron que, para que el ataque falle, Argon2i v1.3 necesita más de 10 pasadas sobre la memoria.

Para abordar estas preocupaciones, el RFC 9106 recomienda usar Argon2id para mitigar en gran medida tales ataques.

 Algoritmo
 **Function** Argon2
    **Inputs:**
       password (**P**):       Bytes (0..232-1)    Contraseña (o mensaje) a ser procesado
       salt (**S**):           Bytes (8..232-1)    Salida (16 bytes recomendados para la contraseña encriptada)
       parallelism (**p**):    Number (1..224-1)   Grado de paralelismo (i.e. número de threads)
       tagLength (**T**):      Number (4..232-1)   Número deseado de bytes devueltos
       memorySizeKB (**m**):   Number (8p..232-1)  Cantidad de memoria (en kibibytes) para usar
       iterations (**t**):     Number (1..232-1)   Número de iteraciones a realizar
       version (**v**):        Number (0x13)       La versión actual es 0x13 (19 decimal)
       key (**K**):            Bytes (0..232-1)    Llave opcional (Errata: PDF says 0..32 bytes, RFC says 0..232 bytes)
       associatedData (**X**): Bytes (0..232-1)    Datos adicionales arbitrarios opcionales
       hashType (**y**):       Number (0=Argon2d, 1=Argon2i, 2=Argon2id)
    **Output:**
       tag:                Bytes (tagLength)   Los bytes generados resultantes, tagLength bytes long

    Genera el bloque inicial de 64 bytes H0. Todos los parámetros de entrada se concatenan y se introducen como fuente de entropía adicional. Erratas: RFC dice que H0 es de 64 bits; PDF dice que H0 es de 64 bytes.
      Errata: RFC dice que el Hash es H^, el PDF dice que es ℋ (pero no documenta lo que es ℋ). En realidad es Blake2b.
      Los artículos de longitud variable se preparan con su longitud como números enteros de 32 bits.
    buffer ← parallelism ∥ tagLength ∥ memorySizeKB ∥ iterations ∥ version ∥ hashType
          ∥ Length(password)       ∥ Password
          ∥ Length(salt)           ∥ salt
          ∥ Length(key)            ∥ key
          ∥ Length(associatedData) ∥ associatedData
    H0 ← Blake2b(buffer, 64) *// El tamaño de hash por defecto de Blake2b es de 64 bytes*

    Calcula el número de bloques de 1 KB redondeando hacia abajo (memorySizeKB) al múltiplo más cercano de 4*parallelism kibibytes
    blockCount ← Floor(memorySizeKB, 4*parallelism)

    Asignar una matriz bidimensional de bloques de 1 KiB (filas de parallelism x columnCount)
    columnCount ← blockCount / parallelism;   //En la RFC, columnCount se denomina **q**

    Computa el primer y segundo bloque (es decir, la columna cero y una ) de cada carril (es decir, la fila)
    **for** i ← 0 **to** parallelism-1 **do** para cada fila
       Bi[0] ← Hash(H0 ∥ 0 ∥ i, 1024) *// Genera 1024-byte digest*
       Bi[1] ← Hash(H0 ∥ 1 ∥ i, 1024) *// Genera 1024-byte digest*

    Computa las columnas restantes de cada carril
    **for** i ← 0 **to** parallelism-1 **do** // para cada fila
       **for** j ← 2 **to** columnCount-1 **do** // para cada columna subsiguiente
          //Los índices "i" y "j" dependen de si se trata de Argon2i, Argon2d o Argon2id (véase la sección 3.4)
          i′, j′ ← GetBlockIndexes(i, j)  //la función GetBlockIndexes no está definida
          Bi[j] = G(Bi[j-1], Bi′[j′]) // la función G hash no está definida

    Further passes when iterations > 1
    **for** nIteration ← 2 **to** iterations **do**
       **for** i ← 0 **to** parallelism-1 **do** para cada fila
         **for** j ← 0 **to** columnCount-1 **do** // para cada columna subsiguiente
            //Los índices "i" y "j" dependen de si se trata de Argon2i, Argon2d o Argon2id (véase la sección 3.4)
            i′, j′ ← GetBlockIndexes(i, j)
            **if** j == 0 **then**
              Bi[0] = Bi[0] xor G(Bi[columnCount-1], Bi′[j′])
            **else**
              Bi[j] = Bi[j] xor G(Bi[j-1], Bi′[j′])

    Calcula el bloque final C como el XOR de la última columna de cada fila
    C ← B0[columnCount-1]
    **for** i ← 1 **to** parallelism-1 **do**
       C ← C **xor** Bi[columnCount-1]

    Calcular la etiqueta de salida
    **return** Hash(C, tagLength)

 Función hash de longitud-variable
Argón2 hace uso de una función hash capaz de producir digests de hasta 232 bytes de largo. Esta función hash esta construida internamente construida sobre Blake2.
 **Function** Hash(message, digestSize)
    **Inputs:**
       message:         Bytes (0..232-1)     Mensaje a ser procesado
       digestSize:      Integer (1..232)     Número deseado de bytes a devolver
    Output:
       digest:          Bytes (digestSize)   Los bytes generados resultantes, digestSize de los bytes de largo

    El **hash** es una función de longitud variable, construida usando Blake2b, capaz de generar digests de hasta 232 bytes.

    Si el digestSize solicitada es de 64 bytes o menos, entonces usamos Blake2b directamente
    **if** (digestSize <= 64) **then**
       **return** Blake2b(digestSize ∥ message, digestSize) //concatenar 32-bit little endian digestSize con los bytes del mensaje

    Para los hashes deseados de más de 64 bytes (por ejemplo, 1024 bytes para los bloques de Argon2), utilizamos Blake2b para generar el doble del número de bloques de 64 bytes necesarios, y luego sólo utilizamos 32 bytes de cada bloque

    Calcula el número de bloques enteros (sabiendo que sólo vamos a usar 32 bytes de cada uno)
    r ← Ceil(digestSize/32)-1;

    Genera r bloques.
    Bloque inicial generado desde el mensaje
    V1 ← Blake2b(digestSize ∥ message, 64);
    Los bloques subsiguientes se generan a partir de los bloques anteriores
    **for** i ← 2 **to** r **do**
       Vi ← Blake2b(Vi-1, 64)
    Genera el bloque final (posiblemente parcial)
    partialBytesNeeded ← digestSize – 32*r;
    Vr+1 ← Blake2b(Vr, partialBytesNeeded)

    Concatena los primeros 32 bytes de cada bloque Vi
    (excepto el posible último bloque parcial, del que toma todo)
    Que Ai represente los 32-bytes inferiores del bloque Vi
    **return** A1 ∥ A2 ∥ ... ∥ Ar ∥ Vr+1

 Referencias

 Enlaces externos

 Argón2 source code repository on Github
 Argón2 specification
 Password Hashing Competition
 Uni.Lu Argon2 Page
 Balloon Hashing: A Memory-Hard Function Providing Provable Protection Against Sequential Attacks
