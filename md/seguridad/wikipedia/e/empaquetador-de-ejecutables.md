---
type: Artículo de enciclopedia
title: Empaquetador de ejecutables
description: Un Empaquetador de ejecutables, genera archivos auto-extraíbles (en inglés self-extracting archives).
resource: https://es.wikipedia.org/wiki/Empaquetador_de_ejecutables
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Empaquetador_de_ejecutables"}
license: CC BY-SA 4.0
id: eswiki-Empaquetador_de_ejecutables
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Empaquetador de ejecutables

Un **Empaquetador de ejecutables**, genera archivos auto-extraíbles (en inglés *self-extracting archives*). A esta técnica se la llama **compresión ejecutable** porque comprime en ficheros que luego se desempaquetan en memoria cuando son ejecutados. De esta forma se pueden tener ficheros más pequeños sin que el usuario tenga que desempaquetarlos manualmente antes de que puedan ejecutarse.

Dado el tamaño actual de los medios portátiles y las velocidades de Internet, la necesidad de archivos más pequeños ya no es tan urgente. Hoy en día, casi siempre que se usan empaquetadores es porque tienen funciones de protector de software, es decir, hacer que la ingeniería inversa sea más difícil, o para que la huella en la máquina infectada sea más pequeña en la máquina infectada. De esta forma, el software funciona como una herramienta de ofuscación, ya sea para proteger la propiedad intelectual u otros datos confidenciales para que no se copien o simplemente para que no sea detectado por el sistema. Hay algunos empaquetadores que se construyen solo con el objetivo de ocultar código malicioso, por eso se les llama **empaquetadores de malware** (en inglés **malware packers**).

 Funcionamiento

Para conseguir su propósito el empaquetador puede cifrar, comprimir, o simplemente cambiar el formato de un archivo consiguiendo qu el fichero se vea como algo completamente diferente. Como resultado, para el sistema es más difícil detectar el malware.

El proceso generalmente consiste en tener una pequeña porción de código que contiene el agente de descifrado y/o descompresión.

El proceso de empaquetado es el siguiente:
 El código original se carga en la herramienta de empaquetamiento y pasa por el proceso de empaquetamiento para comprimir o cifrar los datos.
 El encabezado del código ejecutable original (ejemplo, encabezado PE en Windows) y el código original se comprimen o cifran y se almacenan en la sección empaquetada del nuevo ejecutable.
 El nuevo fichero empaquetado consiste en:
 Nueva cabecera de formato ejecutable (ejemplo, PE)
 Sección/es empaquetada/s
 Código auxiliar que contiene el agente de descifrado y/o descompresión
 Durante el proceso de empaquetado, el punto de entrada original se reubica / ofusca en la sección empaquetada.
 Se embebe el código auxiliar dentro del ejecutable.

Por tanto, tomando como entrada un ejecutable (ejecutable original), se generar otro ejecutable (ejecutable empaquetado) que contiene tanto el código y datos del programa original como la rutina de desempaquetado. Al ejecutarse el ejecutable empaquetado primero se ejecuta la rutina de desempaquetado y una vez finalizada se transfiere el control a la primera instrucción del programa original, descomprimido en la memoria del programa.

 Detección
Hay una serie de herramientas que permite analizar el código para determinar si se ha empaquetado y frecuentemente también puede identificar el empaquetador usado. Estas son algunas de las mejores herramientas para identificar empaquetadores de malware:
 Windows Executable Packer Detection.
 PackerID.
 PEiD.
 RDG Packer Detector.
 Exeinfo PE.

 Análisis
Algunos empaquetadores, como UPX, permiten desempaquetar y obtener el código original para poder analizarlo y aplicar técnicas de ingeniería inversa. Por ejemplo, podría usar un depurador como OllyDbg o Pe Explorer para desarrollar un análisis más profundo. Hay herramientas especializadas que automatizan el análisis estático del código malware como MASTIFF.

 Referencias
