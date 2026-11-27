---
type: Artículo de enciclopedia
title: Permisos de aplicación
description: Los permisos de aplicación son un medio para controlar y regular por software el acceso a funciones a nivel de sistema y de dispositivo.
resource: https://es.wikipedia.org/wiki/Permisos_de_aplicación
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Permisos_de_aplicación"}
license: CC BY-SA 4.0
id: eswiki-Permisos_de_aplicación
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Permisos de aplicación

Los **permisos de aplicación** son un medio para controlar y regular por software el acceso a funciones a nivel de sistema y de dispositivo. Normalmente, los tipos de permisos cubren funciones susceptibles de tener implicaciones para la privacidad, por ejemplo, la capacidad de acceder a los componentes hardware del dispositivo (incluyendo la cámara y el micrófono de un teléfono) y a datos personales (como dispositivos de almacenamiento, listas de contactos y la ubicación geográfica actual del usuario). Los permisos suelen estar declarados en el manifiesto de la aplicación, y determinados permisos deben ser concedidos específicamente en tiempo de ejecución por el usuario, quien podrá revocarlos en cualquier momento.

Los sistemas de administración de permisos son habituales en los sistemas operativos móviles, en que los permisos que necesitan determinadas aplicaciones deben declararse a través de la tienda de aplicaciones de la plataforma.

 Permisos para dispositivos móviles
A continuación se enumeran tipos de permisos habituales en sistemas operativos móviles para teléfonos inteligentes o tabletas:

 Acceso a almacenamiento e información personal, como contactos, citas de calendario, etc.
 Geolocalización.
 Acceso a la cámara interna o al micrófono del dispositivo.
 Acceso a sensores biométricos, como lectores de huellas dactilares o sistemas de reconocimiento facial.
 Acceso a Internet.
 Acceso a interfaces de comunicaciones (incluyendo sus identificadores de hardware y la intensidad de la señal, en los casos relevantes, así como las solicitudes para habilitarlos), como Bluetooth, Wi-Fi, NFC, etc.
 Realizar o recibir llamadas telefónicas.
 Enviar o leer mensajes de texto.
 Capacidad de realizar compras intraaplicación.
 Capacidad de integrarse con otras aplicaciones.
 Capacidad de instalar, borrar y administrar aplicaciones.
 Tokens de autenticación (por ejemplo, tokens OAuth) de servicios web almacenados en el sistema para compartir entre aplicaciones.
En las versiones anteriores a Android 6.0 «Marshmallow», se otorgaban los permisos automáticamente a las aplicaciones en tiempo de ejecución y se presentaban dichos permisos al instalarse en Google Play Store. Desde Marshmallow, ciertos permisos requieren que la aplicación pida permiso al usuario en tiempo de ejecución. Estos permisos también se pueden revocar en cualquier momento a través del menú de configuración de Android.

En ocasiones, los desarrolladores de aplicaciones abusan de los permisos en Android para recopilar información personal y enviar publicidad; en particular, se sabe que numerosas aplicaciones para utilizar la cámara del teléfono móvil a modo de linterna (que se han vuelto en gran medida redundantes debido a la integración de esta funcionalidad a nivel de sistema en versiones posteriores de Android) requieren una gran cantidad de permisos que no son necesarios para realizar la funcionalidad declarada.

IOS impone requisitos similares para la concesión de permisos en tiempo de ejecución, incluyendo controles particulares para habilitar Bluetooth, Wi-Fi y la geolocalización.

 Permisos web
Los permisos web (también conocidos como *WebPermission*) son un sistema de permisos para navegadores web. Cuando una aplicación web necesita algún dato tras un permiso, debe solicitarlo primero. Cuando lo hace, el usuario ve una ventana emergente que le pide que tome una decisión. La decisión se almacena en memoria, aunque últimamente también se puede borrar.

En la actualidad, se controlan los siguientes recursos:

 Geolocalización.
 Notificaciones de escritorio.
 «Trabajadores de servicio».
 Sensores.
 Dispositivos de captura de audio, tales como tarjetas de sonido, así como su nombre de modelo y sus características.
 Dispositivos de captura de vídeo, tales como cámaras, así como sus identificadores y características.

 Análisis
El modelo de control de acceso basado en permisos asigna a una aplicación privilegios de acceso a determinados objetos de datos. Se trata de un modelo derivado del modelo de control de acceso discrecional. Los permisos de acceso suelen concederse en el contexto de un determinado usuario en un determinado dispositivo. Los permisos se conceden de forma permanente con pocas restricciones automáticas.

En algunos casos, la implementación de los permisos sigue un enfoque de «todo o nada»: el usuario debe conceder todos los permisos requeridos para poder acceder a la aplicación o de lo contrario no podrá acceder a la misma. Aún existe falta de transparencia cuando el programa o aplicación utiliza un permiso para acceder a datos protegidos por el mecanismo de control de acceso. Aunque el usuario pueda revocar un permiso, la aplicación podría tratar de forzarlo a volver a concedérselo, por ejemplo, colgándose o volviendo a pedirle el permiso para poder acceder a la aplicación.

El sistema de permisos ha sido ampliamente criticado por investigadores por varios motivos, entre ellos:

 Falta de transparencia en la extracción de datos personales y en la vigilancia, incluyendo la creación de una falsa sensación de seguridad.
 Fatiga del usuario final debido a que la microgestión de permisos de acceso conduce a una aceptación fatalista de la vigilancia y de la falta de transparencia.
 Extracción de datos personales y vigilancia masivas una vez que se han concedido los permisos.

Algunas aplicaciones, como XPrivacy y Mockdroid, falsifican datos como medida de privacidad. Otros métodos de transparencia son la elaboración de perfiles de comportamiento longitudinales y el análisis de privacidad de múltiples fuentes del acceso a datos de aplicaciones.

 Referencias
