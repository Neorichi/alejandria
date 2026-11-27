---
type: Artículo de enciclopedia
title: EdDSA
description: En criptografía de clave pública, el algoritmo de firma digital de curva de Edwards (EdDSA) es un esquema de firma digital que utiliza una variante de la firma de Schnorr basada en curvas de Edwards torcidas.
resource: https://es.wikipedia.org/wiki/EdDSA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/EdDSA"}
license: CC BY-SA 4.0
id: eswiki-EdDSA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# EdDSA

En criptografía de clave pública, el **algoritmo de firma digital de curva de Edwards** (**EdDSA**) es un esquema de firma digital que utiliza una variante de la firma de Schnorr basada en curvas de Edwards torcidas. Está diseñado para ser más rápido que los esquemas de firma digital existentes sin sacrificar la seguridad. Fue desarrollado por un equipo que incluía a Daniel J. Bernstein, Niels Duif, Tanja Lange, Peter Schwabe y Bo-Yin Yang. La implementación de referencia es el software de dominio público.

 Resumen
La siguiente es una descripción simplificada de EdDSA, ignorando los detalles de codificación de números enteros y puntos de curva como cadenas de bits; los detalles completos están en los documentos y RFC.

Un **esquema de firma EdDSA** es una elección:

 de campo finito  sobre potencia prima impar ;
 de curva elíptica  sobre  cuyo grupo  de -los puntos racionales tienen orden , dónde  es un primo grande y  se llama el cofactor;
 de punto base  Con orden ; y
 de la función hash criptográfica  con salidas de  bits, donde  para que elementos de  y puntos de curva en  pueda ser representado por cadenas de  bits

Estos parámetros son comunes a todos los usuarios del esquema de firma EdDSA. La seguridad del esquema de firma EdDSA depende de manera crítica de las elecciones de parámetros, excepto por la elección arbitraria del punto base; por ejemplo, se espera que el algoritmo rho de Pollard para logaritmos tome aproximadamente  adiciones de curvas antes de que pueda calcular un logaritmo discreto, por lo que  debe ser lo suficientemente grande para que esto no sea factible y, por lo general, se considera que supera los . La elección de  está limitada por la elección de , ya que por el teorema de Hasse,  no puede diferir de  por más de . la función hash  normalmente se modela como un oráculo aleatorio en los análisis formales de la seguridad de EdDSA. En la variante HashEdDSA, una función hash adicional resistente a colisiones  se necesita

Dentro de un esquema de firma EdDSA,

 Clave pública
 Una clave pública EdDSA es un punto de curva , codificado en  bits
 Firma
 Una firma EdDSA en un mensaje  por clave pública  es el par , codificado en  bits, de un punto de curva  y un entero  satisfaciendo la siguiente ecuación de verificación.  denota concatenación.

 Clave privada
 Una clave privada EdDSA es una cadena de  bits  que debe elegirse uniformemente al azar. La clave pública correspondiente es , donde  es el menos significativo  pedazos de  interpretado como un número entero en little-endian. La firma en un mensaje  es  dónde  por , y

 Ed25519
**Ed25519** es el esquema de firma EdDSA que utiliza SHA-512 (SHA-2) y Curve25519 donde

  es la curva torcida de Edwards

  y
  es el único punto en  cuyo  coordenada es  y de quien  coordenada es positiva. "positivo" se define en términos de codificación de bits:
 Las coordenadas "positivas" son coordenadas pares (se borra el bit menos significativo)
 Las coordenadas "negativas" son coordenadas impares (se establece el bit menos significativo)
  es SHA-512, con .

La curva  es biracionalmente equivalente a la curva de Montgomery conocida como Curve25519. La equivalencia es

 Rendimiento
El equipo original ha optimizado Ed25519 para la familia de procesadores x86-64 Nehalem/Westmere. La verificación se puede realizar en lotes de 64 firmas para un rendimiento aún mayor. Ed25519 está destinado a proporcionar una resistencia a los ataques comparable a los cifrados simétricos de 128 bits. Las claves públicas tienen una longitud de 256 bits y las firmas tienen una longitud de 512 bits.

 Codificación segura
Como características de seguridad, Ed25519 no utiliza operaciones de rama ni pasos de indexación de matriz que dependan de datos secretos, a fin de derrotar muchos ataques de canal lateral.

Al igual que otros esquemas de firma basados en registros discretos, EdDSA utiliza un valor secreto llamado nonce único para cada firma. En los esquemas de firma DSA y ECDSA, este nonce se genera tradicionalmente de forma aleatoria para cada firma, y si el generador de números aleatorios alguna vez se rompe y es predecible al realizar una firma, la firma puede filtrar la clave privada, como sucedió con el firmware de Sony PlayStation 3. actualizar la clave de firma. Por el contrario, EdDSA elige el nonce de manera determinista como el hash de una parte de la clave privada y el mensaje. Por lo tanto, una vez que se genera una clave privada, EdDSA ya no necesita un generador de números aleatorios para hacer firmas, y no hay peligro de que un generador de números aleatorios roto que se usa para hacer una firma revele la clave privada.

 Inconsistencias de estandarización e implementación
Tenga en cuenta que hay dos esfuerzos de estandarización para EdDSA, uno de IETF informativo, y uno de NIST como parte de FIPS 186-5 (2019). Se han analizado las diferencias entre los estándares, y los vectores de prueba están disponibles.

 Software
Los usos notables de Ed25519 incluyen OpenSSH, GnuPG y varias alternativas, y la herramienta signify de OpenBSD. Se ha estandarizado el uso de Ed25519 (y Ed448) en el protocolo SSH. En 2019, una versión preliminar del estándar FIPS 186-5 incluía el Ed25519 determinista como esquema de firma aprobado.

 Implementación de referencia SUPERCOP (lenguaje C con ensamblador lineal)
 Una implementación alternativa en Python, lenta pero concisa, no incluye protección contra ataques de canal lateral
 NaCl/libsodium
 Protocolo de criptomonedas CryptoNote
 loboSSL
 I2Pd tiene su propia implementación de EdDSA
 Minisign y Minisign Miscellanea para macOS
 Virgil PKI usa claves Ed25519 por defecto
 Apple Watch y iPhone usan claves Ed25519 para autenticación mutua IKEv2
 Botan
 Dropbear SSH desde 2013.61test
 OpenSSL 1.1.1
 Libgcrypt
 Kit de desarrollo de Java 15
 Cardano

 Ed448
**Ed448** es el esquema de firma EdDSA que utiliza SHAKE256 y Curve448 definido en la . También ha sido aprobado en el borrador del estándar FIPS 186-5.

 Referencias
