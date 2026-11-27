---
type: Artículo de enciclopedia
title: Mikey
description: Multimedia Internet KEYing (MIKEY) es un protocolo informático de gestión de claves propuesto con la intención de ser usado en aplicaciones de tiempo real.
resource: https://es.wikipedia.org/wiki/Mikey
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Mikey"}
license: CC BY-SA 4.0
id: eswiki-Mikey
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Mikey

**Multimedia Internet KEYing (MIKEY)** es un protocolo informático de gestión de claves propuesto con la intención de ser usado en aplicaciones de tiempo real. Puede ser utilizado específicamente para configurar las claves de cifrado que se utilizarán en sesiones multimedia aseguradas con SRTP.

MIKEY está definido en el RFC 3830.

 Transporte Básico de las Claves y Métodos de Intercambio

MIKEY soporta tres métodos diferentes de configurar una clave:
 **pre-shared key (PSK)**: Este es el método más eficiente para gestionar el transporte de la clave dado que únicamente se utiliza criptografía simétrica y solamente se intercambia una pequeña cantidad de datos. Sin embargo, es necesario intercambiar una clave individual para cada elemento interviniente en la comunicación, por lo que pueden darse problemas de escalabilidad para grupos grandes de usuarios.

 **public-key**: La clave inicial se intercambia con la ayuda de criptografía de clave pública. En sistemas grandes esto requiere una PKI para gestionar la distribución segura de las claves.

 **Diffie-Hellman**: Se emplea un intercambio de claves Diffie-Hellman para fijar la clave inicial. Este método consume mayores recursos (en computación y ancho de banda) que los anteriores y precisa una PKI al igual que en el caso de clave pública. Sin embargo, tiene la ventaja de proporcionar perfect forward secrecy.
