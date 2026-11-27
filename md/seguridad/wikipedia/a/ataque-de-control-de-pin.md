---
type: Artículo de enciclopedia
title: Ataque de control de pin
description: "El Ataque de control de pin es una clase de ataque contra un sistema en un chip (SoC) en un sistema integrado donde el atacante apunta a la configuración de E/S de los sistemas integrados y deshabilita las funciones de …"
resource: https://es.wikipedia.org/wiki/Ataque_de_control_de_pin
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_de_control_de_pin"}
license: CC BY-SA 4.0
id: eswiki-Ataque_de_control_de_pin
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque de control de pin

El **Ataque de control de pin** es una clase de ataque contra un sistema en un chip (SoC) en un sistema integrado donde el atacante apunta a la configuración de E/S de los sistemas integrados y deshabilita las funciones de E/S del software o del sistema operativo sin detección. El ataque se ve facilitado por la falta de protección de hardware para la configuración de pin y las configuraciones de multiplexación de pin.

El objetivo más importante para el ataque de control de pin es un controlador lógico programable (PLC). La aplicación del ataque de control de pin en los PLC es significativa porque la E/S es el mecanismo principal a través del cual los PLC interactúan y controlan el mundo exterior. Las E/S de los PLC, al igual que otros dispositivos integrados, se controlan mediante un enfoque basado en pin. El ataque de control de pin es un ataque en el que el atacante puede alterar la integridad y la disponibilidad de E/S del PLC mediante la explotación de ciertas operaciones de control de pin y la falta de interrupciones de hardware asociadas a ellos.

La familia del ataque se presentó por primera vez en Black Hat Europe 2016.  El ataque de control de pin utiliza los ajustes de configuración periféricos de E/S del SoC del PLC para finalizar físicamente la interfaz de comunicación del módulo de E/S desde el PLC.  Al dirigirse a la configuración de E/S del PLC en lugar del tiempo de ejecución del PLC o al cambiar el programa lógico, los atacantes pueden evitar que existan mecanismos de detección típicos en los sistemas integrados.

 Trasfondo
Los ataques clásicos contra los PLC dependen de la modificación del firmware del dispositivo, sus parámetros de configuración o el flujo de ejecución de los procesos en ejecución.  Estos ataques típicos provocan interrupciones en el modo normal de operación del PLC, el software de seguridad como IDS detecta y alerta al operador humano.  El Ataque de control de pin se dirige a la memoria dinámica del PLC, donde el dispositivo almacena su configuración de E / S.

 Vectores de ataque
Los investigadores sugirieron al menos dos variantes del ataque llamado *Ataque de configuración de pin* y *Ataque de multiplexación de pin*.  Si bien estos dos vectores de ataque actúan de manera diferente, su concepto es similar y ambos terminan físicamente el acceso a la E/S sin que el software lo detecte, debido a la falta de interrupciones de hardware para la Multiplexación de E/S y la Configuración de E/S.

 Ataque de multiplexación de pin
Los SoC suelen emplear cientos de pines conectados al circuito eléctrico.  Algunos de estos pines tienen un único propósito definido.  Por ejemplo, algunos solo proporcionan electricidad o una señal de reloj.  Dado que diferentes proveedores de equipos con diversos requisitos de E/S utilizarán estos SoC, el fabricante de SoC produce sus SoC para usar un determinado pin físico para múltiples funcionalidades mutuamente exclusivas, según la aplicación.  El concepto de redefinir la funcionalidad del pin se denomina multiplexación de pin y es una de las especificaciones necesarias del diseño de SoC.  Con respecto a la interacción de la multiplexación de pines con el sistema operativo, los proveedores de SoC recomiendan que solo multiplexen los pines durante el inicio, ya que no hay interrupciones para la multiplexación.  Sin embargo, el usuario todavía puede multiplexar un pin en tiempo de ejecución y no hay limitación en eso.

El diseño actual de multiplexación de pin a nivel de hardware plantea cuestiones de seguridad.  Por ejemplo, supongamos que una aplicación utiliza un controlador periférico particular conectado a un pin con una configuración de multiplexación particular.  En un punto, otra aplicación cambia la configuración de multiplexación del pin utilizado por la primera aplicación.  Una vez que el pin se multiplexa, la conexión física al primer controlador periférico se desconecta.  Sin embargo, como no hay interrupciones a nivel de hardware, el sistema operativo asumirá que el primer controlador periférico todavía está disponible.  Por lo tanto, el sistema operativo continuará realizando las operaciones de lectura y escritura solicitadas por la aplicación sin reportar ningún error.

El concepto de cambiar la funcionalidad de un pin conectado a la E/S en el tiempo de ejecución se llama Ataque de multiplexación de pin.

 Ataque de configuración de pin
Un PLC puede recibir y transmitir varios tipos de señales eléctricas y electrónicas.  La entrada, que generalmente proviene de sensores, y la salida, que se puede usar para controlar motores, válvulas o relés, están vinculadas a las clavijas de entrada y salida en un circuito integrado conocido como sistema en chip (SoC).  El controlador pin del SoC puede configurar los modos de un pin (es decir, están configurados para servir como entrada o salida).  Los expertos descubrieron que un atacante que ha comprometido el PLC puede manipular la entrada y la salida sin ser detectado y sin alertar a los operadores que monitorean el proceso a través de una interfaz hombre-máquina (HMI).

 Sigilo
Tanto la Configuración de pines como la Multiplexación de pines no activan ninguna alerta o interrupción de hardware.  Por lo tanto, durante un ataque activo, el tiempo de ejecución del PLC interactuará con una memoria de E/S virtual mientras el atacante finaliza físicamente la conexión de la E/S con la memoria virtual.  El estado donde los valores de E/S en la memoria del software no reflejan la memoria física de E/S es llamado **ilusión de memoria de E/S**.

 Véase también

 Ataque DMA
 Ataque de arranque en frío
 Problema de seguridad FireWire

 Referencias
