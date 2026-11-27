---
type: Artículo de enciclopedia
title: Rubberhose
description: "En computación, Rubberhose (también conocido por su nombre de desarrollo Marutukku) es un fichero de cifrado negable que contiene múltiples sistemas de ficheros cuya existencia sólo puede ser verificada utilizando la …"
resource: https://es.wikipedia.org/wiki/Rubberhose
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Rubberhose"}
license: CC BY-SA 4.0
id: eswiki-Rubberhose
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Rubberhose

En computación, **Rubberhose** (también conocido por su nombre de desarrollo **Marutukku**) es un fichero de cifrado negable que contiene múltiples sistemas de ficheros cuya existencia sólo puede ser verificada utilizando la clave criptográfica apropiada.

 Nombre e historia
El proyecto fue originalmente llamado Rubberhose, ya que fue diseñado para ser resistente a los ataques de personas que deseen utilizar la tortura en aquellos que conocían las claves de cifrado. Esta es una referencia al eufemismo del criptoanálisis de manguera de goma (rubber-hose cryptanalysis).

Fue escrito en 1997-2000 por Julian Assange, Suelette Dreyfus, y Ralf Weinmann.

 Aspecto técnico
El siguiente párrafo está extraído de la documentación del proyecto:

Rubberhose trabaja inicialmente escribiendo caracteres aleatorios en un disco duro entero u otro dispositivo de almacenamiento dinámico. Este ruido aleatorio es indistinguible de los datos cifrados para ser almacenados en ese disco. Si tiene una unidad de 1GB y desea tener dos porciones cifradas de 400MB y 200MB de Rubberhose, asume que cada aspecto (como se llaman las particiones cifradas) será 1GB y llenará toda la unidad. Seguirá haciendo esto hasta que el disco esté lleno con el material cifrado. Se dividen las partes de cada aspecto en partes pequeñas y las dispersa a través del disco de 1GB al azar, con cada aspecto lo detecta como si ocupase 1GB de tamaño sobre el descifrado.

Cada aspecto tiene su propia contraseña que debe descifrarse por separado y si se captura un disco duro, ni el análisis matemático ni la prueba de disco físico pueden revelar cuántos aspectos existen realmente. Los mapas internos se utilizan para localizar dónde se almacenan los datos entre los caracteres aleatorios, teniendo cada aspecto su propio mapa que sólo se puede descifrar a través de su contraseña específica. Por lo tanto, un disco de Rubberhose sólo se puede escribir con seguridad después de que todas las contraseñas se han introducido. Todo funciona sobre una base de "necesidad de saber", es decir, cada aspecto no sabe nada de los otros aparte de cuándo evitar escribir sobre la parte superior de otro.

 Estado
Rubberhose no se mantiene activamente, aunque está disponible para Linux kernel 2.2, NetBSD y FreeBSD. La última versión disponible, aún en fase alpha, es v0.8.3.

 Véase también

Criptoanálisis de manguera de goma
Key disclosure law
StegFS

 Referencias

Enlaces externos

Marutukku.org documentation and downloads
