---
type: Artículo de enciclopedia
title: Emparejamiento
description: El concepto de emparejamiento (o apareamiento) aquí tratado es referente al campo de las matemáticas, específicamente al álgebra lineal.
resource: https://es.wikipedia.org/wiki/Emparejamiento
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Emparejamiento"}
license: CC BY-SA 4.0
id: eswiki-Emparejamiento
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Emparejamiento

El concepto de **emparejamiento** (o **apareamiento**) aquí tratado es referente al campo de las matemáticas, específicamente al álgebra lineal. Con aplicaciones prácticas en el área de la criptografía.

 Definición
Sea *R* un anillo comutativo más la unidad, y sean *M*, *N* y *L* tres *R*-módulos.

Un **emparejamiento** es cualquier mapa bilinear *R* . Que satisfaga:

para cualquier . O equivalentemente, un emparejamiento es un mapa linear *R*:

donde  denota el producto tensorial de *M* y *N*.

Un emparejamiento también puede ser considerado como un mapa linear R
, que satisfaga la primera definición y establezca
.

Un emparejamiento es llamado **no degenerativo** si para el mismo mapa se tiene que  para todo valor de  y .

 Ejemplos
Cualquier producto escalar en un espacio vectorial V **real** es un emparejamiento (sean *M* = *N* = *V*, R = **R** en las definiciones anteriores).

El mapa determinante (matriz 2 × 2 en *k*)  *k* se puede considerar como un emparejamiento .

El mapa de Hopf  definido como  es un ejemplo de un emparejamiento. En, Hardie et al. presentan una construcción explícita de este tipo de mapas utilizando conjuntos parcialmente ordenados.

 Emparejamientos criptográficos

El cómputo de los emparejamientos criptográficos utiliza dos grupos,  y . Estos dos grupos son finitos, cícilos y aditivamente formulados en donde al menos uno de estos grupos tiene orden primo, denotado como **r**. El emparejamiento toma un elemento de cada uno de los dos grupos y los mapa hacia un tercero , el cual es finito, cíclico, pero formulado multiplicativamente, también de order primo **r**. Un emparejamiento criptográfico útil satisface las siguientes propiedades:

 Bilineariedad:
  y , se tiene que:  y
 No degeneración:
  con , existe  tal que .
  con , existe  tal que .
 Computable:
 e puede ser fácilmente calculado.

Los mejores métodos para calcular los emparejamientos criptográficos están basados en el algoritmo de Miller. Este método está estandarizado **de facto** y su mejoramiento tanto en el bucle principal como en la llamada exponenciación final es tema actual de investigación.

 Referencias

 Enlaces externos
 The Pairing-Based Crypto Lounge
