---
type: Artículo de enciclopedia
title: Modelo de oráculo aleatorio
description: "El modelo de oráculo aleatorio es un heurística usada para proveer argumentos de seguridad para protocolos criptográficos modelizando ciertos algoritmos, normalmente funciones hash criptográficas, como oráculos …"
resource: https://es.wikipedia.org/wiki/Modelo_de_oráculo_aleatorio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelo_de_oráculo_aleatorio"}
license: CC BY-SA 4.0
id: eswiki-Modelo_de_oráculo_aleatorio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelo de oráculo aleatorio

El modelo de oráculo aleatorio es un heurística usada para proveer argumentos de seguridad para protocolos criptográficos modelizando ciertos algoritmos, normalmente funciones hash criptográficas, como oráculos (teóricamente una caja negra) que responde a cada consulta con una respuesta realmente aleatoria elegida uniformemente en su rango de salida (funciones aleatorias perfectas). A este tipo de oráculos se les llama **oráculos aleatorios**.

 El modelo de oráculo aleatorio fue introducido por Bellare and Rogaway. Fue diseñado para mostrar la dificultad de romper algoritmos criptográficos modelizando ciertas partes del cifrador (normalmente la función hash) como funciones aleatorias.

Por ejemplo los esquemas de relleno de RSA OAEP y PSS, los cuales son estandards del cifrado y la firma digital, encuentran su justificación formal en el modelo de oráculo aleatorio.

 Crítica a su validez
Recientes estudios han mostrado que los protocolos probados seguros en el modelo de oráculo aleatorio no siempre lo son cuando los oráculos aleatorios son instanciados con funciones computables eficientemente. Por ejemplo Canetti, Goldreich y Halevi probaron que existe un esquema de firma digital que es segura en el modelo de oráculo aleatorio pero inseguro cuando la función aleatoria es reemplazada con una función computable en tiempo polinomial. Ha habido otros estudios que han llegado a conclusiones similares

El significado exacto de estos resultados es un punto de controversia en la comunidad criptográfica, algunos creen que sus construcciones artificiales son evidencias de la fortaleza del modelo de oráculo aleatorio, otros creen que la existencia de tales esquemas es indicación suficiente para que el modelo sea abandonado. Entre otras cosas algunos detractores aseguran que los oráculos aleatorios nunca pueden ser realizados en la práctica desde el momento en que estas funciones son privadas mientras que las funciones hash son objetos públicos.

En cualquier caso, usar el modelo de oráculo aleatorio para 'probar' la seguridad de un protocolo criptográfico reduce la fortaleza de la prueba ya que asume como cierto que:
 Los adversarios no explotan ciertas propiedades de la función hash escogida.
 Las funciones hash se comportan como funciones aleatorias.
 Todos los valores aleatorios son efectivamente aleatorios.
y estas premisas puede que no sean ciertas en el mundo real.

 Referencias
