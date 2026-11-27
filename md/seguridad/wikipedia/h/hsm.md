---
type: Artículo de enciclopedia
title: HSM
description: "HSM son las siglas de \"Hardware Security Module\" (Módulo de Seguridad de Hardware)."
resource: https://es.wikipedia.org/wiki/HSM
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/HSM"}
license: CC BY-SA 4.0
id: eswiki-HSM
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# HSM

**HSM** son las siglas de "**H**ardware **S**ecurity **M**odule" (Módulo de Seguridad de Hardware).

Un HSM es un dispositivo criptográfico basado en hardware que genera, almacena y protege claves criptográficas y suele aportar aceleración hardware para operaciones criptográficas.
Estos dispositivos pueden tener conectividad SCSI / IP u otras y aportar funcionalidad criptográfica de clave pública (PKI) de alto rendimiento que se efectúa dentro del propio hardware.

 Usos
La funcionalidad de un periférico HSM es la generación de datos **seguros** (asegurados mediante criptografía de clave pública o PKI) para su acceso a lo largo del tiempo pudiendo aportar adicionalmente seguridad física. Los datos custodiados por un HSM suelen ser las claves privadas usadas en PKI, y en algunas ocasiones también permiten la protección de claves simétricas.

Algunos sistemas HSM tienen mecanismos de backup seguro de claves PKI, bien sea vía los servicios del Sistema Operativo del ordenador, o bien externamente utilizando una tarjeta criptográfica o algún otro periférico criptográfico.

Muchos sistemas HSM son también aceleradores criptográficos. Estos sistemas no permiten la extracción de las claves sin cifrar, y se utilizan para acelerar la realización de operaciones criptográficas en su hardware dedicado.

Los dispositivos HSM no son solo periféricos locales de un ordenador, algunas compañías ofrecen hardware HSM con conectividad de red para la protección de material residente en múltiples sistemas conectados.

 Consideraciones de seguridad

Como se ha mencionado el objetivo de un HSM es el almacenado seguro de certificados PKI, que son los datos sensibles de esta tecnología.

 La seguridad que proporcionan dichos dispositivos es muy elevada si se siguen ciertas políticas de seguridad.

 Las claves protegidas por los HSM solo están 'completamente protegidas por hardware' si fueron generadas dentro del propio hardware. (si se generan fuera y se importan, las copias de dichas claves fuera del dispositivo -obviamente- no podrán ser protegidas por el dispositivo HSM).

 Información adicional

Aunque el hardware de los dispositivos HSM tiene un muy buen rendimiento, la rápida evolución del software y el empuje de las soluciones de código abierto ha hecho que existan soluciones aceleradoras software que superan en rendimiento a los aceleradores hardware, aunque requieren un esfuerzo mayor de configuración y mantenimiento.

 Referencias
 Hardware Security Modules  (en inglés).
 Artículo en la Wikipedia en inglés (en inglés).

 Enlaces externos
 Algunas empresas fabricantes de módulos HSM
 BULL
 EraCom Technologies - ProtectServer
 IBM - IBM 4758
 ARX - PrivateServer HSM
 nCipher - netHSM, nShield, nForce
 SafeNet - LunaSA
 Futurex - Excrypt SSP7000 & Excrypt SSP71000
 Crypto Accelerator 6000 - Sun
 REALSEC-Encryptación y Firma digital - Cryptosec
 Current NIST FIPS-140 certificates
  - HSM8000 saldrá el 2020
 HP - ATALLA Boxes NSP (Network Security Processor)
