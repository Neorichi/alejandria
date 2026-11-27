---
type: Artículo de enciclopedia
title: LogicLocker
description: LogicLocker es un ransomware que afecta a los Controladores lógicos programables (PLC) utilizados en los Sistemas de control industrial (ICS).
resource: https://es.wikipedia.org/wiki/LogicLocker
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/LogicLocker"}
license: CC BY-SA 4.0
id: eswiki-LogicLocker
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# LogicLocker

**LogicLocker** es un ransomware que afecta a los Controladores lógicos programables (PLC) utilizados en los Sistemas de control industrial (ICS). Descrito por primera vez en un documento de investigación publicado por el Instituto de Tecnología de Georgia, el malware es capaz de secuestrar múltiples PLC de varios proveedores populares. Los investigadores, utilizando un modelo de planta de tratamiento de agua, pudieron demostrar la capacidad de mostrar lecturas falsas, cerrar válvulas y modificar la liberación de cloro a niveles venenosos utilizando un Schneider Modicon M241, Schneider Modicon M221 y un PLC Allen Bradley MicroLogix1400. El ransomware está diseñado para eludir los mecanismos de autenticación débiles que se encuentran en varios PLC y bloquear a los usuarios legítimos al plantar una bomba lógica en el PLC. A partir del 14 de febrero de 2017, se observa que hay más de 1400 de los mismos PLC utilizados en el ataque de prueba de concepto a los que se podía acceder desde Internet como se encontraron utilizando Shodan.

 Método de ataque
El método de ataque utilizado con *LogicLocker* emplea cinco etapas: Infección inicial, movimiento horizontal y vertical, bloqueo, cifrado y negociación. La infección inicial puede tener lugar a través de varias vulnerabilidades. Como los dispositivos ICS generalmente están en un estado siempre encendido, esto les da a los ciberdelincuentes suficiente tiempo para intentar comprometer el PLC. Los PLC generalmente no cuentan con mecanismos de autenticación sólidos para ayudar a protegerse de posibles ataques. La infección inicial podría tener lugar cuando los usuarios hacen clic en un archivo adjunto de correo electrónico potencialmente malicioso. Tras la infección inicial del PLC, se puede lograr un movimiento horizontal o vertical desde el PLC a la red corporativa, dependiendo de las capacidades del PLC. La siguiente etapa del ataque es el bloqueo en el que el atacante bloquea a los usuarios legítimos para inhibir o prevenir los esfuerzos de restauración. Esto se puede hacer a través de cambios de contraseña, bloqueo OEM, uso excesivo de los recursos del PLC o cambio de IP/puertos. Estos métodos de bloqueo ofrecen diversos grados de éxito y fuerza. Para garantizar aún más un ataque exitoso, se utiliza el cifrado para seguir las prácticas tradicionales de criptoransomware para futuras negociaciones. Por último, se realizan negociaciones entre el atacante y la víctima para la restauración del servicio. Algunos PLC contienen una capacidad de correo electrónico que se puede utilizar para enviar el mensaje de rescate como fue el caso con el PLC MicroLogix 1400 utilizado en el ataque de prueba de concepto.

 Estrategias de defensa
Para ayudar en los esfuerzos de defensa y mitigación de la vulnerabilidad, se pueden emplear varias estrategias.

 Puesto final de seguridad
Deben usarse técnicas de seguridad de punto final como cambios de contraseña, deshabilitación de puertos y protocolos no utilizados e implementación de Listas de control de acceso (ACL), mantenimiento de copias de seguridad y actualizaciones de firmware adecuadas. Esto puede reducir significativamente la superficie de ataque presentada por los ciberdelincuentes.

 Seguridad de la red
Se debe utilizar un monitoreo de red más minucioso para detectar anormalidades. La lista blanca de protocolos en los firewalls, la segmentación de la red y las copias de seguridad automáticas pueden proporcionar seguridad adicional y disminuir el tiempo de restauración siempre que las copias de seguridad no se vean comprometidas en el ataque.

 Políticas
La capacitación de los empleados para identificar adecuadamente los correos electrónicos de phishing, la prohibición de dispositivos USB y la incorporación de un plan integral de respuesta a incidentes deben usarse para ayudar a contrarrestar esta amenaza.

 Véase también

 Pin Control Attack
 Stuxnet

 Referencias
