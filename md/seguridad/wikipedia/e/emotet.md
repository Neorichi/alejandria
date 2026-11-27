---
type: Artículo de enciclopedia
title: Emotet
description: Emotet es un malware troyano polimórfico (cambia automáticamente su código cada cierto tiempo), haciendo que sea más difícil para los antivirus detectar su firma.
resource: https://es.wikipedia.org/wiki/Emotet
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Emotet"}
license: CC BY-SA 4.0
id: eswiki-Emotet
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Emotet

**Emotet** es un malware troyano polimórfico (cambia automáticamente su código cada cierto tiempo), haciendo que sea más difícil para los antivirus detectar su firma. Anteriormente este *malware* se consideraba del tipo bancario debido a su objetivo el cual eran cuentas bancarias en sus inicios de 2014. Hoy en día está integrado con varias funciones maliciosas debido a que consta de varios módulos que descarga de su servidor C&C (comando y control):

• Módulo de *spam*.

• Módulo de gusano de red.

• Módulo para visualizar la contraseña del correo electrónico.

• Módulo para visualizar las contraseñas del navegador web.

Este *malware* en sus principios, cuando era considerado un *malware* bancario, obtenía información financiera usando métodos de *sniffing* y algunas de sus variantes usaban distintos tipos de *payloads* como, por ejemplo, inyectando código en la pila de red de un ordenador infectado, permitiendo que información sensible sea robada por medio de transmisión de datos. El malware Emotet de igual manera se auto inserta en los módulos del software los cuales le permiten robar datos de direcciones de teléfono y realizar ataques DOS (Ataque de denegación de servicio) en otros sistemas.

Emotet ha evolucionado en su manera de esparcirse. El modo más destacado que usa es por medio de una *botnet* de *spam*, adjuntado documentos maliciosos o URL en el cuerpo de un correo electrónico, a veces disfrazado como factura o PDF adjunto, así que cuando el usuario da clic al archivo se descarga un documento con una macro que por medio de PowerShell descarga el *malware* Emotet. Las versiones de hoy en día integran un módulo que se aprovecha de ataques de fuerza bruta con diccionario.

Su primera aparición fue en Alemania, Austria, y Suiza en el año 2014, rápidamente siguió con Estados Unidos  esparciéndose no necesariamente a través de las maneras descritas anteriormente. Las infecciones del *malware* más bien se dieron a través de código malicioso JavaScript (.JS); cuando el código *javascript* malicioso es ejecutado le da la capacidad al *malware* Emotet de infectar al actual dispositivo anfitrión.

Una vez que Emotet ha infectado a un dispositivo, tiene la capacidad de interceptar, registrar, y guardar todo el tráfico de red saliente del navegador web, dejando que información sensible de la víctima sea guardada por el *malware* para acceder a su(s) cuenta(s) de banco, o hasta convertir el sistema anfitrión en parte de la *botnet* para esparcir *malware* a través de redes compartidas.

Emotet es miembro de la familia de *malware* troyano Feodo. Cuando este *malware* es ejecutado en un entorno virtual(máquina virtual) cambia su manera de comportarse con el objetivo de engañar a los investigadores del *malware* en cuestión. Esto lo hace usando la función de Win32 API "CREATETIMEQUEUETIMER".

Este Malware fue desmantelado en 2021 por la Europol manipulando uno de sus módulos para incluir un desintalador en su código para hacer un chequeo del malware sus funciones y etc.

 Referencias
