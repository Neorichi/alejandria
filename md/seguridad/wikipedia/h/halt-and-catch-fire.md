---
type: Artículo de enciclopedia
title: Halt and Catch Fire
description: "Halt and Catch Fire, conocida por el nemónico HCF, fue en origen una instrucción ficticia en código máquina que se decía estaba siendo desarrollada por IBM para su uso en sus computadoras System/360, junto con muchas …"
resource: https://es.wikipedia.org/wiki/Halt_and_Catch_Fire
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Halt_and_Catch_Fire"}
license: CC BY-SA 4.0
id: eswiki-Halt_and_Catch_Fire
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Halt and Catch Fire

**Halt and Catch Fire**, conocida por el nemónico **HCF**, fue en origen una instrucción ficticia en código máquina que se decía estaba siendo desarrollada por IBM para su uso en sus computadoras System/360, junto con muchas otras instrucciones divertidas como "Execute Operator".

En la actualidad, HCF se refiere a una instrucción en código máquina no documentada con efectos secundarios poco habituales, incluidas en el procesador con propósitos de prueba. Los usuarios que descubrían estas instrucciones se apropiaron de la antigua instrucción "Halt and Catch Fire" y su nemónico HCF como manera de expresar humorísticamente que la ejecución no deseada de tales instrucciones hace que el sistema deje de realizar sus funciones normales, aunque parezca estar muy atareado. La expresión "catch fire" (prenderse fuego) es estrictamente metafórica.

Existe una historia apócrifa de finales de la década de 1960, cuando las computadoras usaban memorias de núcleo magnético. Dice la historia que para poder hacer más rápidas las memorias de su siguiente modelo, los ingenieros aumentaron las corrientes de lectura/escritura en los delgadísimos alambres que atravesaban los núcleos. Esto funcionaba sin problemas cuando se ejecutaban programas normales, ya que los accesos a memoria se distribuían por toda ella. Sin embargo, la instrucción HALT estaba implementada como un "Salto al mismo sitio". Esto significaba que se accedía de forma repetida a la misma posición de memoria y que los finísimos alambres se calentaban tanto que empezaban a echar humo (de ahí "Halt and Catch Fire").

 Una HCF real

El microprocesador Motorola 6800 fue el primero en incluir un opcode 'HCF' que se hiciera conocido. El origen del opcode HCF del 6800 (0xDD o 0xD9) está en un artículo escrito por Gerry Wheeler (1952–2006) en el número de diciembre de 1977 de *BYTE* magazine, que versaba sobre opcodes no documentados. La instrucción hace que el procesador entre en un modo pensado para pruebas de fabricación, en el que realiza de forma continua ciclos de lectura de memoria en direcciones sucesivas, sin que intervenga ninguna lectura (*fetch*) de instrucciones. El bus de direcciones se convierte de forma efectiva en un contador, permitiendo que se verifique de forma rápida la operatividad de todas las líneas de dirección. Una vez que el procesador ha entrado en este modo, no responde a interrupciones así que solo se puede recuperar el modo normal mediante un 'reset'.

 Procesadores con opcode HCF
 6502 y, en general, las series NMOS 650x y 651x de procesadores
 6800
 6809
 MIPS-X: procesador financiado por la Defense Advanced Research Projects Agency; el Manual del programador describe una instrucción HSC (Halt and Spontaneously Combust - *Detenerse y entrar en Combustión Espontánea*) en la versión -NSA del procesador

 Véase también
 Killer poke
 Cyrix coma bug
 SEX
 f00f
 Printer on fire

 Referencias

*Este artículo se basa parcialmente en el Jargon File, que se encuentra en el dominio público*
