---
type: Artículo de enciclopedia
title: Seguridad de memoria
description: La seguridad de memoria es la forma de estar protegido de varios errores de software y vulnerabilidades de seguridad cuando se realizan accesos a la memoria, como desbordamientos de buffer y punteros colgantes .
resource: https://es.wikipedia.org/wiki/Seguridad_de_memoria
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_de_memoria"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_de_memoria
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad de memoria

**La seguridad de memoria** es la forma de estar protegido de varios errores de software y vulnerabilidades de seguridad cuando se realizan accesos a la memoria, como desbordamientos de buffer y punteros colgantes . Por ejemplo, se dice que Java es seguro para la memoria porque su detección de errores en tiempo de ejecución verifica los límites de los arrays y los punteros desreferenciados.  Por el contrario, C y C ++ permiten la aritmética de punteros, con punteros implementados como direcciones de memoria directas sin verificar los límites, y por lo tanto son potencialmente **inseguros para la memoria**.

 Historia
Los errores de memoria se consideraron por primera vez en el contexto de la gestión de recursos y los sistemas de tiempo compartido, en un esfuerzo por evitar problemas como la Bomba fork. Los desarrollos fueron principalmente teóricos hasta el gusano Morris, que explotó un desbordamiento de buffer en Finger . El campo de la seguridad informática se desarrolló rápidamente a partir de entonces, intensificándose con la aparición de multitud de nuevos ataques como el ataque return-to-libc, las técnicas de defensa como la pila no ejecutable y la aleatoriedad del diseño del espacio de direcciones . La aleatoriedad previene la mayoría de los ataques de desbordamiento de buffer y requiere que el atacante use heap spraying u otros métodos dependientes de la aplicación para obtener direcciones.  Sin embargo, las implementaciones de la tecnología generalmente se limitan a la distribución aleatoria de bibliotecas y la ubicación de la pila.

 Herramientas
DieHard, su rediseño DieHarder y la herramienta Allinea Distributed Debugging son asignadores de heap especiales que asignan objetos en su propia página de memoria virtual aleatoria, lo que permite detener y depurar lecturas y escrituras no válidas en la instrucción exacta que las provoca. La protección se basa en la protección de la memoria del hardware y, por lo tanto, la sobrecarga no suele ser sustancial, aunque puede aumentar significativamente si el programa hace un uso intensivo de la asignación. La aleatoriedad proporciona solo protección probabilística contra errores de memoria.

La herramienta memcheck de Valgrind utiliza un simulador de conjunto de instrucciones y ejecuta el programa compilado en una máquina virtual de verificación de memoria, lo que garantiza la detección de un subconjunto de errores de memoria en tiempo de ejecución. Sin embargo, normalmente ralentiza el programa en un factor de 40, y además debe ser informado explícitamente de los asignadores de memoria personalizados.

Con acceso al código fuente, existen bibliotecas que recopilan y rastrean valores legítimos para punteros ("metadatos") y verifican cada acceso de puntero contra los metadatos para verificar su validez, como el recolector de basura Boehm . En general, la seguridad de la memoria puede garantizarse de forma segura mediante el seguimiento de la recolección de basura y la inserción de comprobaciones de tiempo de ejecución en cada acceso a la memoria; este enfoque tiene gastos generales, pero menos que los de Valgrind. Todos los lenguajes de recolección de basura adoptan este enfoque.

Para C y C ++, existen muchas herramientas que realizan una transformación del código en tiempo de compilación para realizar comprobaciones de seguridad de la memoria en tiempo de ejecución, como CheckPointer y AddressSanitizer, que impone un factor de desaceleración promedio de 2.

Otro enfoque utiliza el análisis de programa estático y la demostración automatizada de teoremas para garantizar que el programa no tenga errores de memoria. Por ejemplo, el lenguaje de programación Rust implementa un comprobador de préstamos para garantizar la seguridad de la memoria. Herramientas como Coverity ofrecen análisis de memoria estática para C. Los punteros inteligentes de C++ son una forma limitada de este enfoque.

 Tipos de errores de memoria
Pueden ocurrir muchos tipos diferentes de errores de memoria:

 **Errores de acceso** : lectura o escritura inválidas de un puntero.
 **Desbordamiento del buffer** : las escrituras fuera del buffer pueden dañar el contenido de los objetos adyacentes, los datos internos (como la información del heap ) o las direcciones de retorno.
 **Lecturas fuera del buffer:** las lecturas fuera del buffer pueden revelar datos confidenciales o ayudar a los atacantes a evitar la distribución aleatoria del espacio de direcciones.
 **Condición de carrera** : ocurre cuando se realizan lecturas o escrituras simultáneas en la memoria compartida.
 **Error de página no válida** : se produce al acceder a un puntero fuera del espacio de memoria virtual. Una desreferencia de un puntero nulo a menudo causará una excepción o la terminación del programa en la mayoría de los entornos, pero puede causar daños en los núcleos del sistema operativo, en sistemas sin protección de memoria, o cuando el uso del puntero nulo implica un desplazamiento grande o negativo.
 **Usar después de liberar**: sucede al desreferenciar un puntero colgante que almacena la dirección de un objeto que ha sido eliminado.
 **Variables no inicializadas** - utilizar una variable a la que no se le ha asignado un valor puede contener un valor no deseado o corrupto.
 Desreferencia de un puntero nulo : desreferenciar un puntero no válido o un puntero a la memoria que no se ha asignado
 **Punteros salvajes** : surgen cuando se usa un puntero antes su inicialización. Muestran el mismo comportamiento errático que los punteros colgantes, aunque es menos probable que pasen desapercibidos.
 **Fuga de memoria** - sucede cuando no se realiza un seguimiento del uso de la memoria o se realiza un seguimiento incorrecto
 **Desbordamiento de pila** : ocurre cuando un programa se queda sin espacio en la pila, normalmente debido a una recursividad demasiado profunda. Una página de protección generalmente detiene el programa, evitando que se dañe la memoria, pero las funciones con marcos de pila grandes pueden omitir la página.
 **Desbordamieno del heap** : se produce cuando un programa intenta asignar más memoria que la cantidad disponible.
 **Doble Liberación** : ocurre cuando se realizan varias llamadas para liberar la memoria, esto puede provocar una pérdida de memoria si se llama con el mismo valor.
 **Liberación inválida** : se produce al pasar una dirección no válida a la función la función malloc, esto puede dañar el heap.
 **Libre no coincidente** : sucede cuando se utilizan varios asignadores y se intenta liberar la memoria con una función de liberación con un asignador diferente del que hizo la asignación.
 **Alias no encontrado** : ocurre cuando se asigna la misma ubicación de memoria y se modifica dos veces para fines no relacionados.

 Referencias
