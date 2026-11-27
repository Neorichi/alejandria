---
type: Artículo de enciclopedia
title: Protector de software
description: Un protector de software es un software que al aplicarse sobre programas dificulta la modificación y la ingeniería inversa sobre ellos.
resource: https://es.wikipedia.org/wiki/Protector_de_software
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protector_de_software"}
license: CC BY-SA 4.0
id: eswiki-Protector_de_software
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protector de software

Un **protector de software** es un software que al aplicarse sobre programas dificulta la modificación y la ingeniería inversa sobre ellos. Puede usar técnicas de empaquetamiento de ejecutables, cifrado y ofuscación.

Este tipo de herramientas son usadas frecuentemente para dificultar tanto la piratería de programas como la detección de malware. Se calcula que aproximadamente el 80% del malware usa estas herramientas. Esto obliga a los fabricantes de antimalware a implementar algoritmos que desempaqueten automáticamente estos programas antes de ser analizados para ver si se tratan o no de malware.

 Historia
Los protectores de software surgieron como empaquetadores de ejecutables que, además de reducir el tamaño de un ejecutable, obtenían el beneficio añadido de proteger el programa frente a ataques de ingeniería inversa al impedir que el código fuera analizado estáticamente.

Con el tiempo fueron evolucionando de tal forma que la protección del software frente a ataques de ingeniería inversa era cada vez más importante, creándose así herramientas con métodos de protección más sofisticados y sacrificando, en algunos casos, el tamaño del ejecutable final y su tiempo de ejecución. El tamaño del ejecutable deja de ser un aspecto crítico, aunque es habitual que los protectores de software sean también Empaquetador de ejecutables.

 Ejemplos
Algunos de los empacadores más importantes son:
 Ultimate Packer for Executables (UPX). Utiliza un algoritmo de código abierto y no requiere memoria adicional para la descompresión. Es el más usado.
 The Enigma Protector
 MPRESS.
 Exe Packer 2.300.
 ExeStealth.
 Morphine.
 Themida.
 MEW.
 FSG.
 PESpin.
 Andromeda.
 VMProtect.
 Obsidium.
 ASPack.
 PE Compact.
 ASProtect.
 NSPack.
 UPack.
 EXECryptor.
 Armadillo.

 Análisis

Hay una serie de herramientas que permite analizar el código que puede determinar en algunos casos el protector de software usado Estas son algunas de las estas herramientas:
 Windows Executable Packer Detection.
 PackerID.
 PEiD.
 RDG Packer Detector.
 Exeinfo PE.

Algunos protectores, como UPX, permiten desempaquetar y obtener el código original para poder analizarlo y aplicar técnicas de ingeniería inversa. Por ejemplo, podría usar un depurador como OllyDbg o Pe Explorer para desarrollar un análisis más profundo. Hay herramientas especializadas, como MASTIFF, automatizan el análisis estático del código malware.

 Referencias
