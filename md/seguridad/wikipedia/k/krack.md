---
type: Artículo de enciclopedia
title: KRACK
description: KRACK (Ataque de Reinstalación de Clave) es un grave ataque de repetición (un tipo de defecto explotable) en el protocolo de Acceso Protegido Wi-Fi que asegura conexiones Wi-Fi.
resource: https://es.wikipedia.org/wiki/KRACK
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/KRACK"}
license: CC BY-SA 4.0
id: eswiki-KRACK
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# KRACK

**KRACK** (*Ataque de Reinstalación de Clave*) es un grave ataque de repetición (un tipo de defecto explotable) en el protocolo de Acceso Protegido Wi-Fi que asegura conexiones Wi-Fi. Fue descubierto en 2016 por los investigadores belgas Mathy Vanhoef y Frank Piessens de la Universidad de Leuven. El grupo de búsqueda de Vanhoef publicó detalles del ataque en octubre de 2017. Reiniciando repetidamente el nonce transmitido en el tercer paso del apretón de manos WPA2, un atacante puede gradualmente emparejar paquetes cifrados vistos antes y aprender por completo el conjunto de claves utilizado para cifrar el tráfico.

La debilidad está en el propio estándar Wi-Fi, y no en implementaciones o productos individuales. Por tanto, cualquier implementación correcta de WPA2 es probable que sea vulnerable. La vulnerabilidad afecta a todas las plataformas de software importantes, incluyendo Microsoft Windows, macOS, iOS, Android, y Linux.

La implementación ampliamente usada de código abierto wpa_supplicant, utilizada por Linux, Android, y OpenBSD, es especialmente susceptible ya que puede ser manipulada para instalar una clave de cifrado de todo-ceros, anulando eficazmente la protección WPA2 en un ataque man-in-the-middle.

 Detalles
El ataque apunta al apretón de manos de cuatro vías usado para establecer un nonce (un tipo de "secreto compartido") en el protocolo WPA2. El estándar para WPA2 anticipa desconexiones WiFi ocasionales, y permite reconectar utilizando el mismo valor del tercer apretón de manos (para una rápida reconexión y continuidad). Ya que el estándar no requiere una clave distinta para ser utilizada en este tipo de reconexion, la cual podría ser necesitada en cualquier momento, un ataque de repetición es posible.

Un atacante puede re-enviar repetidamente el tercer apretón de manos de la comunicación de otro dispositivo para manipular o reiniciar la clave de cifrado de WPA2. Cada reinicio provoca que los datos sean cifrados usando los mismos valores, de manera que bloques con el mismo contenido pueden ser vistos y emparejados, trabajando de manera invertida para identificar partes del conjunto de claves que fueron usados para cifrar aquel bloque de datos. Repetidos reinicios exponen gradualmente más del conjunto de claves hasta que finalmente se conoce la clave completa, y el atacante puede leer todo el tráfico del objetivo en esa conexión.

El riesgo es especialmente severo porque WPA2 es utilizado en la mayoría de dispositivos móviles con internet habilitado a un punto de acceso fijo o router doméstico (a pesar de que parte del mismo tráfico puede estar todavía más cifrado, a través del uso de protocolos de alto nivel como SSL/TLS).

De acuerdo a US-CERT:"US-CERT ha sido consciente de varias vulnerabilidades en la administración de claves en el apretón de manos de 4 vías del protocolo de seguridad de Acceso Protegido Wi-Fi II (WPA2). El impacto de explotar estas vulnerabilidades incluye descifrado, replicación de paquetes, secuestro de conexiones TCP, inyección de contenido HTTP, y otros. Tenga en cuenta que como problemas a nivel de protocolo, la mayoría o todas las implementaciones correctas del estándar serán afectadas. El CERT/CC y el informe de investigación de KU Leuven, serán publicados revelando estas vulnerabilidades el 16 de octubre de 2017."El papel describiendo la vulnerabilidad está disponible en línea, y debe ser formalmente presentado en la Conferencia ACM sobre Seguridad Informática y de Comunicaciones el 1 de noviembre de 2017. US-CERT está siguiendo esta vulnerabilidad, listada como VU#228519, a través de múltiples plataformas. Los siguientes identificadores CVE relacionados con la vulnerabilidad KRACK: CVE-2017-13077, CVE-2017-13078, CVE-2017-13079, CVE-2017-13080, CVE-2017-13081, CVE-2017-13082, CVE-2017-13084, CVE-2017-13086, CVE-2017-13087, CVE-2017-13088.

Algunos usuarios de WPA2 pueden contrarrestar el ataque actualizando el cliente y el software del punto de acceso del dispositivo Wi-Fi, si tienen dispositivos para los que están disponibles parches del proveedor. Aun así, muchos dispositivos antiguos pueden no ser actualizados, o recibir una actualización retrasada.

 Véase también
 Seguridad inalámbrica

 Referencias

 Enlaces externos
 http://www.krackattacks.com/
