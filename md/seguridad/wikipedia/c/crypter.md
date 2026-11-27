---
type: Artículo de enciclopedia
title: Crypter
description: Un Crypter es un software que se usa para esconder malware (virus, keyloggers,...) para que no sea fácilmente detectado por los antivirus.
resource: https://es.wikipedia.org/wiki/Crypter
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Crypter"}
license: CC BY-SA 4.0
id: eswiki-Crypter
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Crypter

Un **Crypter** es un software que se usa para esconder malware (virus, keyloggers,...) para que no sea fácilmente detectado por los antivirus. Para realizar su función pueden usa técnicas de cifrado y a veces ofuscación.

El Crypter toma el archivo ejecutable y obtiene un nuevo archivo ejecutable que al ejecutarse descifra código cifrado que contiene y obtiene el antiguo archivo ejecutable original.

 Funcionamiento
El ejecutable una vez aplicado el crypter tiene una parte sin cifrar, llamada en inglés *stub*, y la parte que contiene código cifrado. En la parte sin cifrar es lo primero que se ejecuta y lo que hace es localizar dentro del binario el ‘malware cifrado’, a continuación localiza la clave de ‘cifrado/descifrado’ e inicia el proceso de descifrado del ‘malware’ en memoria. Por último hace que se ejecute el código malicioso.

 Tipos de Crypter
Según su forma de funcionamiento los Crypter pueden ser:
 De tiempo de escaneado. Toman el ejecutable cifrado, lo descifran, escriben el ejecutable descifrado en el disco y lo ejecutan desde allí. Este tipo de crypters generalmente evaden la detección del escaneo antivirus hasta la ejecución. Tan pronto como el archivo no está cifrado y se escribe en el disco, la mayoría de los antimalware los detecta y los pone en cuarentena.
 De tiempo de ejecución. El crypter no escribe nada en disco. La parte sin cifrar prepara el código incrustado y ofuscado para su ejecución. Para ello descifrar el código y ejecuta la imagen binaria descifrada desde la memoria, realizando las tareas que generalmente hace el cargador de programas del sistema operativo al ejecutar un programa. Esto permite evadir la detección de firmas antivirus. Para ejecutar una imagen binaria por sí misma, emplean técnicas similares a las de los ficheros obtenidos después de aplicar un empaquetador de ejecutables. Por esta razón, los términos empaquetador y crypter se usan a menudo como sinónimos.

Según como está diseñado el crypter los podemos clasificar en:
 Crypter con stub en su interior. Son los más sencillos y fáciles de construir pero tienen la desventaja que si un antimalware detecta el crypter, el stub (código que hará de parte sin cifrar de los programas resultantes) tendrá que ser cambiado también.
 Crypter con la stub externo. La experiencia ha demostrado que crypters de este tipo han permanecido indetectables durante más tiempo.

 Ejemplos
Ejemplos de este tipo de herramientas son:
 AIO FUD Crypter.
 Hidden Sight Crypter.
 Galaxy Crypter.
 Criogenic Crypter.
 Heaven Crypter.
 SwayzCryptor.
 Dr.True Crypt.
 Techo negro crypter.
 Deeps.
 Hack Crypter.
 Root Crypter.
 Kazy Crypter.
 Ghost Crypter.
 Haqman.

Referencias
