---
type: Artículo de enciclopedia
title: Código de control
description: El código de control es un mecanismo de detección de errores utilizado para verificar la corrección de un dato, generalmente en soporte informático.
resource: https://es.wikipedia.org/wiki/Código_de_control
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Código_de_control"}
license: CC BY-SA 4.0
id: eswiki-Código_de_control
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Código de control

El **código de control** es un mecanismo de detección de errores utilizado para verificar la corrección de un dato, generalmente en soporte informático. Los dígitos de control se usan principalmente para detectar errores en el tecleo o transmisión de los datos.

Generalmente consisten en uno o más caracteres numéricos o alfabéticos añadidos al dato original y calculados a partir de este mediante un determinado algoritmo. Algunos de los ejemplos de uso frecuentes son los números de identificación personal, códigos de barras, tarjetas de crédito y códigos bancarios.

  Denominación
No existe unanimidad en la denominación de esta técnica en el mundo hispanoparlante. La traducción directa del inglés *check digit* sería *dígito de chequeo*, *de verificación* o *de control*. Estas denominaciones solamente son aplicables cuando se trata, efectivamente, de uno o varios dígitos y no de otros caracteres. Más correctas son las variantes *carácter de chequeo*, *de verificación* o *de control*, aunque esta última tiene otro significado específico en el contexto de la informática. También son aplicables *código de control* (la forma más usada de entre las correctas), *de chequeo* o *de verificación*, aunque esta última expresión se refiere casi siempre a técnicas para filtrar el acceso a páginas web, como los *captcha*.

 Utilización

Es utilizado normalmente en representaciones numéricas que exijan integridad, como por ejemplo:

 **Documentos de identificación:** Algunos documentos de identificación como la cédula de identidad o el DNI dependiendo del país.
 **Códigos de pagos:** Número de factura, número de identificación tributaria, etc.
 **Códigos en general:** Cuenta bancaria, cuenta corriente, número de matrícula, código de barras, ISBN, etc.

 Cálculo del dígito verificador

El método de cálculo de esos dígitos varía conforme el caso. Sin embargo, muchos de ellos se basan en dos rutinas tradicionales: **Módulo 11** y **Módulo 10**.

 Módulo 11

El método denominado *módulo 11* detecta errores en un solo dígito e intercambios simples o dobles. Se basa en aplicar un factor de chequeo ponderado a cada dígito del número original. El cálculo se realiza como sigue:
 A cada dígito del número base se le asigna un factor de chequeo ponderado. Dicho factor será 2 para el dígito menos significativo (el que está más a la derecha) y, en orden, 3, 4, 5, 6, 7 para los siguientes. Si hubiere más de 6 dígitos, la secuencia se repetirá, de modo que el séptimo dígito se multiplicará por 2, el octavo por 3, etcétera.
 Cada dígito del número base se multiplica por el factor de chequeo asignado.
 Se suman los resultados de todas las multiplicaciones.
 Al resultado de la suma se le calcula el módulo 11 (de ahí el nombre del método), es decir, el resto de la división entera entre 11.
 A 11 se le resta el módulo calculado en el punto anterior. Si el resultado de la resta es < 10, dicho resultado es el dígito de control que buscábamos. Si el resultado es 11 el dígito de control es 0 y si el resultado es 10 el dígito de control resultante es 1.

El siguiente esquema desarrolla un ejemplo de cálculo:

Número ejemplo: 41261533-?

Pasos 1 y 2
        +---+---+---+---+---+---+---+---+   +---+
        | 4 | 1 | 2 | 6 | 1 | 5 | 3 | 3 | - | ? |
        +---+---+---+---+---+---+---+---+   +---+
          |   |   |   |   |   |   |   |
         x3  x2  x7  x6  x5  x4  x3  x2
          |   |   |   |   |   |   |   |
        =12  =2 =14 =36  =5 =20  =9  =6

Paso 3   12  +2 +14 +36  +5 +20  +9  +6 = 104

Paso 4   104 mod 11 = 5     (ya que 104 = 11 x 9 + 5)

Paso 5   11 - 5 = 6

Resultado = 41261533-6

A veces se usan variantes, como sustituir el resultado por una letra cuando el resultado es 10. Por ejemplo, en Chile el Rol Único Nacional (RUN) y el Rol Único Tributario (RUT) utilizan este sistema y cuando el resultado del algoritmo es 10 el carácter de control es la letra "K".

 Módulo 10

Conforme al esquema de abajo, cada dígito del número, comenzando de la derecha para la izquierda (menos significativo para el más significativo) es multiplicado, en orden, por 2, después 1, después 2, después 1 y así sucesivamente.

Número ejemplo: 261533-4

  +---+---+---+---+---+---+   +---+
  | 2 | 6 | 1 | 5 | 3 | 3 | - | 4 |
  +---+---+---+---+---+---+   +---+
    |   |   |   |   |   |
   x1  x2  x1  x2  x1  x2
    |   |   |   |   |   |
   =2 =12  =1 =10  =3  =6
    +---+---+---+---+---+-> = (16 / 10) = 1, resto 6 => DV = (10 - 6) = 4

En vez de ser hecha la sumatoria de las multiplicaciones, será hecha la sumatoria de los dígitos de las multiplicaciones (si una multiplicatoria da 12, por ejemplo, será sumatoriado 1 + 2 = 3).

La sumatoria será dividida por 10 y si el resto (módulo 10) es diferente de cero, el dígito será 10 menos este valor. En caso de que el resto sea cero, ese será el dígito verificador.

Estas condiciones finales, sin embargo, podrán ser alteradas conforme el caso.

 Véase también
 Algoritmo de Luhn
 CUIT (Argentina)

 Notas

 Enlaces externos

Algoritmo para el Cálculo del Dígito Verificador del Registro Único de Contribuyente (R.U.C. - Paraguay) http://www.set.gov.py/pset/hgxpp001?6,18,273,O,S,0,PAG;CONC;287;4;D;370;1;PAG;MNU;E;103;5;MNU;,

Implementación del algoritmo en php
