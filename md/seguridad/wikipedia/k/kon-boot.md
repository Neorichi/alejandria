---
type: Artículo de enciclopedia
title: Kon-Boot
description: "Kon-Boot (kon boot, konboot) es una utilidad que permite a los usuarios evitar las contraseñas de Microsoft Windows y Apple macOS (el soporte para Linux es obsoleto) sin cambios duraderos o persistentes al sistema en el …"
resource: https://es.wikipedia.org/wiki/Kon-Boot
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Kon-Boot"}
license: CC BY-SA 4.0
id: eswiki-Kon-Boot
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Kon-Boot

- **Nombre:** Kon-Boot
- **Desarrollador:** Piotr Bania
- **Última versión:** 5.0
- **Sistema operativo:** Multiplataforma
- **Género:** Seguridad informática

Kon-Boot (*kon boot*, *konboot*) es una utilidad que permite a los usuarios evitar las contraseñas de Microsoft Windows y Apple macOS (el soporte para Linux es obsoleto) sin cambios duraderos o persistentes al sistema en el que se ejecuta. También es la primera herramienta capaz de evitar contraseñas de Windows 10 en línea (en vivo) y soporta tanto sistemas Windows como macOS. Desde la versión 3.5 Kon-Boot también puede evitar la función de SecureBoot.

 Historia
Kon-Boot fue diseñado originalmente como una prueba de concepto, herramienta freeware de seguridad, principalmente para las personas que suelen olvidar sus contraseñas. La idea principal era permitir a los usuarios iniciar sesión en la computadora objetivo sin saber la contraseña correcta y sin hacer cambios persistentes en el sistema en el que se ejecutaba.

La primera salida de Kon-Boot fue anunciada en 2008 en la lista de correos DailyDave La Versión 1.0 (freeware) permitía a los usuarios iniciar sesión en sistemas operativos basados en Linux y evitar el proceso de autenticación (permitiendo el acceso al sistema sin saber la contraseña).

En 2009, el autor del software anunció Kon-Boot para sistemas operativos Linux y Microsoft Windows de 32-bit. Esta versión brindó soporte adicional para evitar contraseñas del sistema en cualquier sistema operativo Windows, desde Windows Server 2008 a Windows 7. Esta versión aún está disponible como freeware

Las versiones más nuevas de Kon-Boot están disponibles solamente como productos comerciales y siguen siendo mantenidos. La versión actual (3.1) es capaz de evitar contraseñas en los siguientes sistemas operativos:

 Tecnología
Kon-Boot funciona como un bootkit (por eso a veces crea alertas en falso positivo en el software antivirus). Se inyecta (oculta) en la memoria BIOS. Kon-Boot modifica el código kernel en el momento (tiempo de ejecución), cambiando temporalmente el código responsable de la verificación de datos de autenticación de usuario mientras carga el sistema operativo.

A diferencia de herramientas de restablecimiento de contraseñas, como CHNTPW, Kon-Boot no modifica los archivos del sistema y el SAM, todos los cambios son temporales y desaparecen tras reiniciar el sistema.

 Limitaciones (prevención)
Los usuarios preocupados sobre herramientas como Kon-Boot deberían usar cifrado de disco (FileVault, Bitlocker, TrueCrypt, etc.), ya que Kon-Boot no es capaz de ignorar el cifrado de disco. La característica de contraseña de BIOS y SecureBoot también son buenas medidas preventivas. Sin embargo, la versión 3.5 de Kon-Boot es capaz de evitar la función de SecureBoot.

 Referencias
