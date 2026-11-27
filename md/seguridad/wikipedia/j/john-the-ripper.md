---
type: Artículo de enciclopedia
title: John the Ripper
description: John the Ripper es una herramienta para recuperación de contraseñas.
resource: https://es.wikipedia.org/wiki/John_the_Ripper
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/John_the_Ripper"}
license: CC BY-SA 4.0
id: eswiki-John_the_Ripper
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# John the Ripper

- **Nombre:** John the Ripper
- **Lanzamiento:** 1996
- **Última versión:** 1.9.0
- **Género:** Password cracking
- **Sistema operativo:** Linux, Windows y macOS
- **Plataforma:** Multiplataforma
- **Licencia:** GPLv2+
- **Español:** Inglés

**John the Ripper** es una herramienta para recuperación de contraseñas. Originalmente desarrollado para el sistema operativo Unix, puede funcionar en quince plataformas diferentes (once de las cuales son versiones específicas de la arquitectura Unix, DOS, Win32, BeOS y OpenVMS). Es una de las herramientas para descifrado de contraseñas más utilizados, ya que combina varios descifradores de contraseñas en un solo paquete, auto-detecta los tipos de hash de las contraseñas e incluye un descifrador personalizable.

Puede ser ejecutado contra varios formatos de contraseñas cifradas, incluyendo varios tipos de hash de contraseñas criptográficas que se encuentran comúnmente en varias versiones de Unix (basadas en DES, MD5 o Blowfish), Kerberos AFS, y hash LM en Windows NT/2000/XP/2003. Los módulos adicionales han ampliado su capacidad para incluir hashes de contraseñas basados en MD4 y contraseñas almacenadas en LDAP, MySQL y otros.

 Resultado de muestra

La primera línea es un comando para expandir los datos almacenados en el archivo "pass.txt". La siguiente línea es el contenido del archivo, es decir, el usuario (AZl) y el hash asociado a ese usuario (zWwxIh15Q). La tercera línea es el comando para ejecutar John the Ripper utilizando el flag "-w". "password.lst" es el nombre de un archivo de texto lleno de palabras que el programa utilizará contra el hash, pass.txt hace otra aparición como el archivo en el que queremos que John trabaje.

Entonces vemos el resultado de John trabajando. Cargado 1 hash de contraseña, el que vimos con el comando "cat", y el tipo de hash que John cree que es (DES tradicional). También vemos que el intento requirió una conjetura a la vez de 0 con una tasa de conjetura del 100%.

 Tipos de ataque
Uno de los modos que puede utilizar John es el ataque de diccionario. Toma muestras de cadenas de texto (normalmente de un archivo, llamado lista de palabras, que contiene palabras encontradas en un diccionario o contraseñas reales crackeadas con anterioridad), cifrándolas en el mismo formato que la contraseña que se está examinando (incluyendo tanto el algoritmo de cifrado como la clave), y comparando el resultado con la cadena cifrada. También puede realizar una variedad de alteraciones a las palabras del diccionario y probarlas (añade números, signos, mayúsculas y minúsculas, cambia letras, combina números, etc.). Muchas de estas alteraciones también se utilizan en el modo ataque individual de John, que modifica un texto plano asociado (como un nombre de usuario con una contraseña cifrada) y comprueba las variaciones con los hashes.

John también ofrece un modo fuerza bruta. En este tipo de ataque, prueba todos los posibles textos sin formato (crea combinaciones de letras, números y símbolos), aplicando un hash a cada uno de ellos y comparándolo con el hash de entrada. John utiliza distribución de frecuencias de caracteres para probar primero los textos sin formato que contienen los caracteres más utilizados. Este método es útil para descifrar contraseñas que no aparecen en las listas de palabras del diccionario, pero tarda mucho en ejecutarse.

 Ética
Aunque esté catalogada como herramienta de cracking, John the Ripper es una utilidad para administradores muy sencilla y que no comporta peligro para el usuario si la usa de forma adecuada.

Los administradores de sistemas lo pueden emplear para evitar que sus usuarios pongan contraseñas demasiado fáciles, pero lo habitual es hacerlo mediante un programa automático, que solo se interese por si la clave se puede adivinar fácilmente o no. *En ningún caso es necesario que el administrador conozca la clave exacta*; solo ha de saber si es buena o no.

En un sistema Unix, algunos usuarios malintencionados pueden intentar usar este programa para obtener información de acceso. Para evitarlo, basta con asegurarse de que las contraseñas cifradas no estén visibles en el fichero /etc/passwd, sino en el fichero /etc/shadow, que *ha de tener desactivado el permiso de lectura* para los usuarios normales. Esta es la configuración predeterminada en los sistemas operativos de tipo Unix (BSD, GNU/Linux, macOS, etc.).

 Curiosidades
"John the Ripper" es un nombre que alude al de "Jack the Ripper" (Jack el Destripador), que es el nombre popularizado por el asesino en serie que mató a cinco prostitutas en el East End, una zona conocida de Londres, en 1888. Su nombre se originó en una carta escrita por alguien quien alegó ser el asesino del cual hablaban los periódicos de la época.

 Véase también
 Hashcat
 Aircrack-ng

 Referencias

 Enlaces externos

 Repositorio oficial en GitHub
