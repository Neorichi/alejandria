---
type: Artículo de enciclopedia
title: Automated Certificate Management Environment
description: "El Automatic Certificate Management Environment (ACME) es un protocolo de comunicaciones para automatizar las interacciones entre las autoridades de certificación y los servidores de los usuarios, permitiendo el …"
resource: https://es.wikipedia.org/wiki/Automated_Certificate_Management_Environment
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Automated_Certificate_Management_Environment"}
license: CC BY-SA 4.0
id: eswiki-Automated_Certificate_Management_Environment
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Automated Certificate Management Environment

El **Automatic Certificate Management Environment (ACME)** es un protocolo de comunicaciones para automatizar las interacciones entre las autoridades de certificación y los servidores de los usuarios, permitiendo el despliegue automatizado de infraestructuras de clave pública a muy bajo coste. Fue diseñado por el *Internet Security Research Group* (ISRG) para su servicio Let's Encrypt.

El protocolo, basado en el intercambio de mensajes en formato JSON a través de HTTPS, ha sido publicado como un Estándar de Internet en el  por su propio grupo de trabajo del IETF.

 Implementaciones de clientes
El ISRG proporciona implementaciones de referencia gratuitas y de código abierto para ACME: certbot es una implementación en Python del software de gestión de certificados de servidor que utiliza el protocolo ACME, y *boulder* es una implementación de autoridad de certificación escrita en Go.

Desde 2015, ha aparecido una gran variedad de opciones de clientes para todos los sistemas operativos.

 Versiones de la API

 API Versión 1
La especificación de la API v1 fue publicada el 12 de abril de 2016. Permite la emisión de certificados para nombres de dominio completamente cualificados, como example.com o cluster.example.com, pero no para comodines como *.example.com. Let's Encrypt desactivó el soporte para la API v1 el 1 de junio de 2021.

 API Versión 2
La API v2 fue lanzada el 13 de marzo de 2018 tras varios retrasos. ACME v2 no es compatible hacia atrás con la v1. La versión 2 admite dominios comodín, como *.example.com, lo que permite que muchos subdominios tengan TLS confiable, por ejemplo: https://cluster01.example.com, https://cluster02.example.com, https://example.com, en redes privadas bajo un solo dominio usando un único certificado "comodín" compartido.

Un nuevo requisito importante en la v2 es que las solicitudes para certificados comodín requieren la modificación de un registro TXT del sistema de nombres de dominio (DNS), verificando el control sobre el dominio.

Los cambios en el protocolo ACME v2 respecto a la v1 incluyen:

 Ha cambiado el flujo de autorización/emisión.
 Ha cambiado la autorización de solicitudes JWS.
 El campo "resource" en los cuerpos de las solicitudes JWS ha sido reemplazado por una nueva cabecera JWS: "url".
 Renombramiento de recursos/puntos finales del directorio.
 Cambio de URI → URL en los recursos de desafíos.
 La creación de cuenta y la aceptación de los Términos de Servicio se combinan en un solo paso. Anteriormente, eran dos pasos separados.
 Se implementó un nuevo tipo de desafío, TLS-ALPN-01. Dos tipos de desafío anteriores, TLS-SNI-01 y TLS-SNI-02, fueron eliminados por problemas de seguridad.

 Casos de uso comunes

 Automatización de certificados web (Web TLS Automation): Uso más extendido, típicamente con Let's Encrypt para HTTPS gratuito en servidores web como Apache o Nginx.
 IoT y dispositivos embebidos (IoT Certificate Provisioning): Algunos dispositivos usan ACME para aprovisionar certificados automáticamente y cifrar sus comunicaciones.
 Entornos DevOps y CI/CD (DevOps Automation): ACME permite rotación automática de certificados en pipelines de despliegue sin intervención manual.
 Servicios internos (Internal Services with Private PKI): A través de autoridades de certificación internas compatibles con ACME, es posible asegurar servicios internos sin depender de CA públicas.

 Seguridad y vulnerabilidades
Aunque ACME ha simplificado la gestión de certificados, su uso conlleva ciertos riesgos de seguridad que deben conocerse:

 **Authorization Cache Attack**: Un atacante que compromete una cuenta ACME puede reutilizar autorizaciones previamente validadas para emitir nuevos certificados sin revalidación.
 *Mitigación: Emplear extensiones como ACME++, que vinculan la solicitud a la IP y cliente específico, forzando una validación en cada solicitud.*

 **Cross-Site Scripting in HTTP-01 Challenge**: En implementaciones inseguras del desafío HTTP-01, es posible introducir scripts maliciosos en respuestas HTTP.
 *Mitigación: Validar y sanear correctamente las respuestas HTTP. Usar HTTPS siempre que sea posible.*

 **Enterprise ACME Integration Limitations**: Algunas soluciones empresariales no admiten ACME fuera de Let's Encrypt, dificultando su adopción en infraestructuras privadas.
 *Mitigación: Utilizar servidores ACME privados, que permitan control y personalización.*

 **Wildcard Certificate Automation Issues**: El desafío DNS-01, necesario para certificados comodín, puede complicarse en entornos sin automatización DNS.
 *Mitigación: Integrar proveedores DNS compatibles con APIs o herramientas como lego, certbot-dns-, o soluciones CI/CD para gestionar los* *registros TXT automáticamente.*

 Véase también
Simple Certificate Enrollment Protocol (SCEP), un intento previo de protocolo de despliegue automático de certificados.

 Referencias

 Enlaces externos

 Automatic Certificate Management Environment (ACME) RFC 8555.
 List of ACME clients, Let's Encrypt
 List of commonly used ACME clients, acmeclients.com
