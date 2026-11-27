---
type: Artículo de enciclopedia
title: Zebedee
description: "ZeBeDee es una herramienta de software para establecer transferencia de datos cifrados y comprimidos \"túnel\" entre dos sistemas utilizando TCP/IP o UDP."
resource: https://es.wikipedia.org/wiki/Zebedee
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Zebedee"}
license: CC BY-SA 4.0
id: eswiki-Zebedee
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Zebedee

- **Nombre:** Túnel ZeBeDee
- **Desarrollador:** Neil Winton
- **Última version:** 2.4.1A
- **Fecha última versión:** 6 de noviembre de 2005
- **Sistema operativo:** Multiplatforma
- **Género:** Compresión, cifrado
- **Licencia:** GNU General Public License

** ZeBeDee ** es una herramienta de software para establecer transferencia de datos cifrados y comprimidos "túnel" entre dos sistemas utilizando TCP/IP o UDP. Esto permite que el tráfico por telnet, ftp y “X”, sean protegidos de snooping así como también obtener un mejor rendimiento en redes de bajo ancho de banda debido a la compresión de sus datos. ZeBeDee se puede implementar para trabajar tanto en Linux como en Windows, es totalmente gratuita para su uso comercial y no comercial, y es distribuido bajo los términos de GNU General Public License.

 Objetivos
Proporcionar plena funcionalidad cliente-servidor en plataformas UNIX / Linux y Windows.
Ser fácil de instalar, utilizar y mantener con poca o ningún requerimiento de configuración.
Deja una pequeña huella (footprint), bajo overhead y reducir significativamente el tráfico con el uso de compresión.

ZeBeDee no pretende competir con empresas, ni, en términos de funcionalidad con SSH, SSL o FreeS/WAN. Es una herramienta **rápida, sencilla y gratis**.

 Desventajas

Multithread , implementar con kernel 2.6.
En UDP o límite por datagrama, es de 16kb.
Tuneliza sobre TCP. No garantiza integridad de los datos (es posible introducir ruido).

 Su Nombre
ZeBeDee lleva el nombre de sus tres componentes principales:
**Zlib** compresión

**Blowfish** cifrado

**Diffie-Hellman** acuerdo de clave secreta

 Versiones
Versión estable: 2.4.1A (2005/09/06)
Desarrollo Versión: 2.5.3 (2005/09/06) correcciones en negación de servicios y actualizaciones de las bibliotecas de compresión.

 Aplicaciones
Conexión de un host a una máquina remota (debiendo configurar Zebedee server en la máquina remota).
Conexión de un Servidor con varias máquinas (debiendo especificar el nombre de las máquinas y una lista con los puertos a conectarse).
Para consultar información de configuración, ver: https://web.archive.org/web/20071013015824/http://www.winton.org.uk/zebedee/manual.html

 Enlaces externos
https://web.archive.org/web/20071011020216/
http://www.winton.org.uk/zebedee/  Página oficial - Download
http://www.stunnel.org/
http://lists.sourceforge.net/lists/listinfo/zebedee-announce Anuncio de nuevas versiones
http://lists.sourceforge.net/lists/listinfo/zebedee-talk Reporte de problemas – Discusiones
