---
type: Artículo de enciclopedia
title: Stunnel
description: Stunnel es un programa de computadora libre multiplataforma, utilizado para la creación de túneles TLS/SSL.
resource: https://es.wikipedia.org/wiki/Stunnel
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Stunnel"}
license: CC BY-SA 4.0
id: eswiki-Stunnel
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Stunnel

- **Nombre:** Stunnel
- **Desarrollador:** Michal Trojnara & Brian Hatch
- **Ultima version:** 5.20
- **Fecha ultima version:** 9 de julio de 2015
- **Sistema operativo:** Multiplataforma
- **Genero:** Proxy, Criptografía
- **Licencia:** GNU General Public License

**Stunnel** es un programa de computadora libre multiplataforma, utilizado para la creación de túneles TLS/SSL.

Stunnel puede ser utilizado para proveer conexiones cifradas seguras para clientes o servidores que no utilizan TLS o SSL de forma nativa. Corre en una gran variedad de sistemas operativos, incluyendo a la mayoría de los basados en el sistema operativo Unix y a la familia Windows. Su funcionamiento se basa en una biblioteca independiente como puede ser OpenSSL o SSLeay para implementar el protocolo TLS o SSL de capas inferiores.

Stunnel utiliza criptografía de clave pública con el certificado digital X.509 para asegurar la conexión SSL. Los clientes se pueden autentificar de manera opcional a través de un certificado digital.

Si es conectado a una libwrap, se puede configurar también para que funcione como un servicio de firewall-proxy.

Stunnel es mantenido por Michal Trojnara y Brian Hatch. Liberado bajo los términos de la GNU General Public License.

 Situación de Ejemplo
La aplicación puede presentar un puerto externo SSL seguro que es mapeado a un puerto TCP o UDP no seguro perteneciente a una aplicación existente.

Por ejemplo, para proveer de una conexión SSL segura a un servidor de correo SMTP existente, Stunnel deberá mapear el puerto 465 de SSL al puerto 25 del servidor de correo. El tráfico en la red creado por los clientes conectándose al servidor de correo a través del puerto 25 inicialmente pasará a través de SSL a la aplicación Stunnel, la cual redireccionará de forma transparente el tráfico inseguro del puerto 25 del servidor de correo. El proceso de Stunnel puede estar corriendo en el mismo servidor o en uno diferente al que utiliza la aplicación de correo insegura, de cualquier manera ambas máquinas se encontrarán típicamente detrás de un firewall en una red interna segura.

 Véase también

 Referencias

 Enlaces externos
 Sitio Oficial
 Stunnel FAQ / descargas
 STunnel.org
