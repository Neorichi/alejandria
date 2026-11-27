---
type: Artículo de enciclopedia
title: Seguridad de Software de Código Abierto
description: La seguridad de software de código abierto es la medida para asegurarse o garantizar el estar libre de peligros o riesgos inherentes a un sistema de código abierto.
resource: https://es.wikipedia.org/wiki/Seguridad_de_Software_de_Código_Abierto
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_de_Software_de_Código_Abierto"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_de_Software_de_Código_Abierto
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad de Software de Código Abierto

La **seguridad de software de código abierto ** es la medida para asegurarse o garantizar el estar libre de peligros o riesgos inherentes a un sistema de  código abierto.

Software de código abierto contra algoritmos libres

Un proyecto de software es una implementación de un algoritmo en general. Aunque estas implementaciones sólo pueden ser probadas, y las pruebas sólo pueden demostrar la presencia de errores (y no la ausencia de estos), los algoritmos pueden ser probados correctamente.
En el cifrado de clave secreta, una de las premisas es que el algoritmo debe ser conocido y sólo una pequeña parte de la información debe mantenerse en secreto: La clave secreta. Es decir, para que un cifrado se considere seguro,  se debe de demostrar que el algoritmo es  correcto y la prueba de esto debe estar disponible para cualquier persona que quiera utilizar el cifrado.
Por lo tanto, en seguridad computacional, hay un consenso de que los algoritmos deben estar abiertos, sin embargo hay un debate sobre si sus implementaciones deben de ser de código abierto (público) o software propietario (secreto).

Debate de la implementación

El esfuerzo de probar (auditar) una implementación se reduce considerablemente, si se centra en la verificación que corresponde al algoritmo correcto (probado previamente). Teniendo en cuenta que el que realiza las pruebas (auditor) tiene acceso al código fuente, esto sólo se puede hacer si el software es de código abierto o software propietario.

Es muy importante entender que la auditoría de software depende del acceso al código fuente.
Debido a eso, una nueva auditoría de un software propietario depende de lo que desee el propietario del software, mientras que la auditoría en el software de código abierto se puede hacer en cualquier momento por cualquier persona que lo desee.

Esta preocupación se ha vuelto más y más severa ya que se dejan puertas traseras, en consecuencia, zonas de seguridad de software bien establecidas han sido reveladas. Además de esto, hay un debate en curso sobre si el software de código abierto aumenta la seguridad del software, o afecta a la misma, pero se ha vuelto inútil. A pesar de que algunos de los argumentos de ambos lados son subjetivos y no hay relación entre el número de vulnerabilidades en una aplicación y como es que si es código abierto/propiedad influye, cada uno de ellos puede contener puertas traseras. Sin embargo, sólo el software de código abierto puede ser auditado libremente y por lo tanto, el software propietario debe considerarse inherentemente inseguro

Beneficios de la seguridad de código abierto
Más personas pueden inspeccionar el código fuente para encontrar y solucionar una posible vulnerabilidad. Esto puede llevar tanto al descubrimiento de vulnerabilidad de seguridad intencional rápidamente como a la prevención de vulnerabilidades intencionales (puertas traseras) localizadas  en el código, el cual es puesto allí por los propios desarrolladores.
El Software propietario obliga al usuario a aceptar el nivel de seguridad que el proveedor de software está dispuesto a ofrecer y a aceptar la cantidad de "parches" y actualizaciones disponibles.
El usuario final del código abierto tiene la capacidad de cambiar y modificar la fuente para implementar cualquier "característica" extra de seguridad que quiera para un uso específico, que puede extenderse hasta el nivel de kernel si así lo desea.
Se asume que cualquier compilador que es utilizado crea código confiable, pero se ha demostrado por Ken Thompson que un compilador puede ser subvertido utilizando un *Thompson hack* para crear ejecutables defectuosos que se producen involuntariamente por un desarrollador sin malas intenciones. Con el acceso al código fuente para el compilador, el desarrollador tiene por lo menos la capacidad de descubrir si hay alguna mala intención.
 David A. Wheeler demuestra que la existencia de dos diferentes compiladores de auto-compilación de código abierto (que deben de ser capaz de compilar entre sí) se puede utilizar para establecer un binario para uno de ellos que es conocido por no ser subvertido por el Thompson hack.
El principio de Kerckhoffs se basa en la idea de que un enemigo puede robar un sistema militar seguro, pero no es capaz de poner en peligro la información. Sus ideas fueron la base para muchas de las prácticas modernas de seguridad , y dice que la seguridad por obscuridad son malas prácticas.

Esquemas de seguridad de código abierto
Los atacantes pueden encontrar vulnerabilidades más fáciles con el código fuente.
Simplemente, al crear un código fuente no se garantiza que exista una revisión. Un buen ejemplo de que esto ocurre fue cuando Marcus Ranum, un experto en el diseño de sistemas de seguridad y aplicaciones, lanzó su primer kit de herramientas firewall públicas. Hubo una época en la que había más de 2,000 sitios que usaban este kit de herramientas, pero solo 10 personas dieron algún comentario de retroalimentación o algún parche.
Tener una gran cantidad de ojos revisando el código puede "hacer que un usuario tenga una falsa sensación de seguridad". Tener muchos usuarios mirando el código fuente no garantiza que los problemas de seguridad se vayan a encontrar y arreglar.

Métricas y modelos
Hay una gran variedad de modelos y métricas para medir la seguridad de un sistema. Estos son algunos métodos que pueden utilizarse para medir la seguridad de los sistemas de software.

Número de días entre vulnerabilidades
Se discute que un sistema es más vulnerable después de que se descubre una vulnerabilidad potencial, pero antes de que se ponga un parche. Al medir el número de días entre la vulnerabilidad, cuando la vulnerabilidad es arreglada, se puede determinar una base en la seguridad del sistema. Hay algunas advertencias en este enfoque: no toda vulnerabilidad es igual de mala; arreglar muchos errores rápidamente puede ser peor que buscar y arreglar solamente unos pocos y que se tome un poco más de tiempo en cada uno de ellos, tomando en cuenta el sistema operativo o la efectividad del parche.

Proceso de Poisson
El proceso de Poisson se puede utilizar para medir las tasa de cambio con la que diferentes personas encuentran fallos de seguridad entre el software de código abierto y cerrado. El proceso puede ser dividido entre el número de voluntarios Nv y revisores pagados Np. Las tasas de cambio con la que los voluntarios encuentran un defecto se mide por λv y la tasa con la que revisores pagados se encuentran un defecto se mide por λp. El tiempo que se espera para que un grupo de voluntarios encuentre un error es 1/(Nv λv) y el tiempo que se espera para que un grupo pagado encuentre un defecto es 1/(Np λp).

Modelo estrella
Mediante la comparación de una gran variedad de códigos abiertos y cerrados con un sistema de estrellas, se puede analizar la seguridad del proyecto, similar a la empresa Morningstar, Inc. la cual valora los fondos de inversión. Con un conjunto de datos suficientemente grande, las estadísticas se podrían utilizar para medir la eficacia global de un grupo sobre otro. Un ejemplo de como funciona el sistema es el siguiente:

1 Estrella: Muchas vulnerabilidades de seguridad.
2 Estrellas: Problemas de fiabilidad.
3 Estrellas: Sigue las mejores prácticas de seguridad.
4 Estrellas: Proceso documentado de desarrollo de seguro.
5 Estrellas: Pase de revisión de seguridad independiente.

Escáner Coverity
Coverity en colaboración con la Universidad de Stanford ha establecido un nuevo punto de referencia para la calidad y seguridad del código abierto. El desarrollo se completa a través de un contrato con el Departamento de Seguridad Nacional. Ellos están utilizando las innovaciones en la detección automática de defectos para identificar los tipos de errores críticos encontrados en el software.  El nivel de calidad y de seguridad se mide en los escalones. Los escalones no tienen un sentido definitivo, y pueden cambiar a medida que Coverity lanza sus nuevas herramientas. Los escalones se basan en el progreso de desarrollo de parches  encontrados en los resultados del análisis de Coverity y con el grado de colaboración, en conjunto con Coverity.  Comienzan con el escalón 0 y actualmente llega al escalón 2.

**Escalón 0**
El proyecto ha sido analizado por la infraestructura de escaneo de Coverity, pero no hay representantes del software de código abierto que se hayan presentado a revisar los resultados.

**Escalón 1**
En el escalón 1, existe colaboración entre Coverity y el equipo de desarrollo. El software se analiza con un subconjunto de funciones de escaneado para evitar que el equipo de desarrollo sea abrumado.

**Escalón 2**
Hay 11 proyectos que se han analizado y actualizado a la condición de escalón 2 al llegar a no tener ningún defecto en el primer año de exploración. Estos proyectos incluyen: AMANDA, ntp, OpenPAM, OpenVPN, Overdose, Perl, PHP, Postfix, Python, Samba, y  tcl.

Referencias

Enlaces externos
 Bruce Schneier: Open Source and Security Crypto-Gram Newsletter, 15 September 1999
