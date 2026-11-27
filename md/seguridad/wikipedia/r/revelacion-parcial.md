---
type: Artículo de enciclopedia
title: Revelación parcial
description: "La políticas de revelación parcial (en inglés partial disclosure) es una tipo de políticas de revelación de vulnerabilidades que establecerse como punto intermedio entre la política de no revelación de vulnerabilidades …"
resource: https://es.wikipedia.org/wiki/Revelación_parcial
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Revelación_parcial"}
license: CC BY-SA 4.0
id: eswiki-Revelación_parcial
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Revelación parcial

La políticas de **revelación parcial** (en inglés *partial disclosure*) es una tipo de políticas de revelación de vulnerabilidades que establecerse como punto intermedio entre la política de no revelación de vulnerabilidades y la política de revelación completa. Intentan aprovechar buenas ideas de una y otra para situarse en un punto intermedio con mejores características. Se han desarrollado distintos modelos pero cada uno tiene sus inconvenientes considerándose el problema de la política de revelación como un problema abierto y pendiente de solución.

 Origen
El uso masivo de políticas de revelación completa provocó la aparición masiva de exploits. Esto, junto con la tardanza de los proveedores de software en liberar los parches y las malas prácticas de los responsables de seguridad en aplicarlos, provocó un éxito masivo de dichos exploits hasta proporciones epidémicas. En esta situación aparició un movimiento importante por parte de algunas compañías de software y de algunos investigadores de seguridad para promover otro tipo de políticas de revelación de vulnerabilidades que no redujeran la información publicada de forma que no se dieran detalles que permitieran el desarrollo de exploits que permitieran automatizar el ataque y permitir así que cualquier persona pudiera realizar dicho ataque script kiddies. Este tipo de políticas estarían basadas en las siguientes ideas no desprovistas de polémica:
 La amenaza de publicar una vulnerabilidad es tan buena como el hecho real de publicarla.
 La información sobre la vulnerabilidad debería ser compartida por el menor número de personas posible hasta que se desarrolle un parche que solucione la vulnerabilidad. Siguiendo este precepto no se debería revelar la información de forma pública sino dársela primero al proveedor del software e idealmente mantenerla secreta hasta que el parche que soluciona la vulnerabilidad esté disponible.
 Para evitar que el proveedor retrase demasiado la publicación del parche que arregla la vulnerabilidad, se pueden establecer tiempos límites en los que el proveedor tiene que mostrar avances en la construcción del parche. Si no se cumplen el originador puede proceder a hacer una revelación completa de la vulnerabilidad. Se trata de dotar al proveedor de cierta ventaja frente a atacantes maliciosos para poder desarrollar el parche que arregle la vulnerabilidad, pero sin darle potestad para retrasar indefinidamente la publicación de la información.
 No es necesario tener acceso a toda la información sobre la vulnerabilidad para poder defenderse de ella. Se promueve que en la revelación de una vulnerabilidad no se de provea de un exploit ni se den detalles que se puedan utilizar para la construcción del mismo.
 A veces es interesante designar un coordinador entre el informador de la vulnerabilidad y el proveedor.

 Críticas
Críticas a este tipo de políticas frente a las políticas de revelación completa:
 La posible víctima del ataque no tiene desde el principio (desde que se comunica al proveedor) toda la información sobre la vulnerabilidad de su sistema y por tanto **pierde oportunidades de protegerse adecuadamente**. Esto se debe a que la vulnerabilidad puede ser descubierta por atacantes o simplemente ser filtrada maliciosamente por alguna de las personas a las que se comunica la misma.
 La amenaza al proveedor con una revelación completa puede ser **efectiva** sólo si es posible aplicar una política de revelación completa. Es la única herramienta que se tiene para estimular al proveedor de que arregle cierta vulnerabilidad.
 No dar toda la información sobre la vulnerabilidad puede no ser necesario para la mayoría de los administradores para asegurar sus sistemas, sin embargo, hay casos particulares donde la posesión de toda la información de la vulnerabilidad (Ej. el exploit) **ayudaría a mejorar la protección** (Ej. testear si un sistema es vulnerable a dicha vulnerabilidad).
 **No espolea a los proveedores** de software para que mejoren la seguridad de sus productos. No promueve que las propias organizaciones proveedoras hagan ellos mismos un análisis exhaustivo (con su correspondiente coste) de las vulnerabilidades de sus productos. Pueden esperar a que se los descubran los demás.
 Favorece el que los proveedores **mantengan vulnerabilidades** que conocen pero que son costosas de eliminar o se mantienen porque realmente son puertas traseras que permiten accesos no autorizados. Se especula que las agencias de seguridad y servicios secretos promueven y utilizan este tipo de 'vulnerabilidades'.
 No favorece a la única forma de conseguir verdadera seguridad: El **escrutinio público** de los entresijos del sistema (en la industria software el código abierto. Da una falsa **apariencia de seguridad** a proveedores que mantienen el secreto del funcionamiento de sus sistemas. Se especula que para muchos productos software es inviable publicar su código fuente porque al ser estudiadas por el público revelaría una enorme cantidad de vulnerabilidades que hasta que no fueran corregidos no permitiría su uso.
 No favorece la educación sobre como **conseguir mejoras en la seguridad** de los productos que se desarrollan. Sin una explicación completa sobre el fallo cometido los diseñadores y/o programadores continuarán cometiendo errores similares haciendo su trabajo.
 No recompensa a organizaciones que se esfuerzan por conseguir, desde el principio, una calidad más alta en la seguridad de sus productos.

 Ejemplos
Basándose en las distintas consideraciones han aparecido distintas políticas de revelación que establecen términos medios entre la política de no-revelación y la política de revelación completa. Ejemplos: Revelación limitada, revelación responsable, revelación constructiva, RFPolicy, las políticas de revelación llevadas a cabo por ciertas organizaciones (Ej. IBM Internet Security Systems, NTBugTraq, CERT Coordination Center) o la política de revelación propuesta por Steven Christey y Chris Wysopal (borrador de estándar para el IETF que finalmente no fue aprobado).

Se han propuesto también organismos que ayuden como intermediarios entre originadores de la vulnerabilidad y proveedores de sistemas. Ejemplos de propuestas: The Responsible Disclosure Forum y Fisher Plan

 Referencias
 Andrew Cencini et ali., "Software Vulnerabilities: Full-, Responsible-, and Non-Disclosure". Diciembre 2005
 Stephen A. Sheperd,"Vulnerability Disclosure. How do we define Responsible Disclosure?. SANS Institute. Abril 2003
