---
type: Artículo de enciclopedia
title: Función-T
description: "En criptografía, una función T es un mapeo biyectivo que actualiza cada bit del estado de forma que puede describirse como ,o, en palabras sencillas, una función de actualización en la que cada bit del estado se …"
resource: https://es.wikipedia.org/wiki/Función-T
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Función-T"}
license: CC BY-SA 4.0
id: eswiki-Función-T
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Función-T

En criptografía, una **función T** es un mapeo biyectivo que actualiza cada bit del estado de forma que puede describirse como ,o, en palabras sencillas, una función de actualización en la que cada bit del estado se actualiza mediante una combinación lineal del mismo bit y una función de un subconjunto de sus bits menos significativos. Si cada uno de los bits menos significativos se incluye en la actualización de cada bit del estado, dicha función T se denomina **triangular**. Gracias a su bijetividad (no hay colisiones y, por tanto, no hay pérdida de entropía), independientemente de las funciones booleanas utilizadas y de la selección de las entradas (siempre que todas procedan de un lado del bit de salida), las funciones T se utilizan ahora ampliamente en criptografía para construir cifrados de bloque, cifrados de flujo, PRNG y funciones hash. Las funciones T fueron propuestas por primera vez en 2002 por A. Klimov y A. Shamir en su artículo "A New Class of Invertible Mappings". Cifras como TSC-1, TSC-3, TSC-4, ABC, Mir-1 y VEST se construyen con diferentes tipos de funciones T.

Dado que las operaciones aritméticas, como la suma, la resta y la multiplicación, son también funciones T (funciones T triangulares), se pueden construir funciones T basadas en palabras y eficientes desde el punto de vista del software, combinando la lógica de bits con las operaciones aritméticas. Otra propiedad importante de las funciones T basadas en operaciones aritméticas es la predictibilidad de su periodo, que resulta muy atractiva para los criptógrafos. Aunque las funciones T triangulares son naturalmente vulnerables a los ataques de adivinar y determinar, las transposiciones a nivel de bits bien elegidas entre rondas pueden neutralizar ese desequilibrio. En los cifrados eficientes por software, esto puede hacerse intercalando operaciones aritméticas con operaciones de intercambio de bytes y, en menor medida, con operaciones de rotación a nivel de bits. Sin embargo, las funciones T triangulares siguen siendo muy ineficientes en hardware.

Las funciones T no tienen ninguna restricción en cuanto a los tipos y las anchuras de las funciones de actualización utilizadas para cada bit. La transposición posterior de los bits de salida y la iteración de la función T tampoco afectan a la bijetividad. Esta libertad permite al diseñador elegir las funciones de actualización o las cajas S (S-box) que satisfacen todos los demás criterios criptográficos e incluso elegir funciones de actualización arbitrarias o dependientes de la clave (véase la clave familiar).

Por lo tanto, se pueden construir fácilmente funciones T ligeras y eficientes desde el punto de vista del hardware con anchos idénticos de todas las funciones de actualización para cada bit del estado. Los acumuladores del núcleo de los cifradores VEST son un buen ejemplo de tales funciones T razonablemente ligeras que se equilibran después de 2 rondas por la capa de transposición haciendo que todas las funciones de retroalimentación de 2 rondas tengan aproximadamente el mismo ancho y perdiendo el sesgo de la "función T" de depender sólo de los bits menos significativos del estado.

 Bibliografía
