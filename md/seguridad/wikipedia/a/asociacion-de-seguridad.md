---
type: Artículo de enciclopedia
title: Asociación de seguridad
description: Una Asociación de Seguridad (SA) es el establecimiento de atributos de seguridad compartidos entre dos entidades de red para permitir una comunicación segura.
resource: https://es.wikipedia.org/wiki/Asociación_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Asociación_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Asociación_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Asociación de seguridad

Una **Asociación de Seguridad** (SA) es el establecimiento de atributos de seguridad compartidos entre dos entidades de red para permitir una comunicación segura. Una SA puede incluir atributos tales como: algoritmo de cifrado y el modo, la clave de cifrado del tráfico y los parámetros de los datos de la red que se deben pasar por la conexión. El marco para el establecimiento de asociaciones de seguridad es proporcionada por la Asociación de Seguridad de Internet y el protocolo de administración de claves (ISAKMP). Los protocolos como Internet Key Exchange y Kerberos Internet negociación de claves proporcionan material de claves autenticado.

Una SA es un simple (canal unidireccional) y la conexión lógica que respalda y proporciona una conexión de datos segura entre los dispositivos de red. El requisito fundamental de una SA llega cuando las dos entidades se comunican a través de más de un canal. Tomemos, por ejemplo, un abonado móvil y una estación base. El abonado puede suscribirse a sí mismo más de un servicio. Por lo tanto, cada servicio puede tener diferentes primitivas de servicio, tales como algoritmo de cifrado de datos, clave pública o el vector de inicialización. Para facilitar las cosas, toda esta información de seguridad se agrupa lógicamente, y el propio grupo lógico es una asociación de seguridad. Cada SA tiene su propio ID llamado SAID. Así pues, tanto la estación base y el abonado móvil compartirán el SAID, y van a derivar todos los parámetros de seguridad.

En otras palabras, una SA es un grupo lógico de los parámetros de seguridad que permiten el intercambio de información a otra entidad.

 Véase también
 IPsec
 Virtual Private Network (VPN)
 Internet key exchange (IKE)
 Group Domain of Interpretation (GDOI)

 Referencias

 Enlaces externos
 Explicación de SAs en IPSec (en inglés)
