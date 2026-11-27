---
type: Artículo de enciclopedia
title: Política de no revelación de vulnerabilidades
description: La no revelación de la información sobre vulnerabilidades, en inglés Non-disclosure, es en sí misma una política de revelación.
resource: https://es.wikipedia.org/wiki/Política_de_no_revelación_de_vulnerabilidades
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Política_de_no_revelación_de_vulnerabilidades"}
license: CC BY-SA 4.0
id: eswiki-Política_de_no_revelación_de_vulnerabilidades
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Política de no revelación de vulnerabilidades

La **no revelación** de la información sobre vulnerabilidades, en inglés *Non-disclosure*, es en sí misma una política de revelación. La información se mantiene en **secreto**. Este enfoque se basa en dar prioridad a mantener en secreto la vulnerabilidad frente a dar publicidad a la información para podernos proteger frente a ella.

Algunas veces en lugar de una no revelación absoluta, la información sobre la vulnerabilidad se comparte de forma restringida (**pseudosecreto**). Cuanto más amplio sea el número de personas que conocen la vulnerabilidad se incrementa el riesgo para los usuarios finales. La información puede revelarse por ejemplo a:
 El proveedor del sistema para que arregle la vulnerabilidad
 Otros investigadores (hackers).
 Alguien que compra esa información. De esta forma se establece un mercado de vulnerabilidades.

Muchas veces el descubridor de la vulnerabilidad toma esta política y la información se va divulgando por canales privados hasta que llega a cierta organización o persona que decide publicarla para evitar daños mayores.

 Origen
Históricamente esta fue la primera política de revelación utilizada en el mundo de la informática. Las vulnerabilidades se comunicaban directamente a las empresas proveedoras para que éstas las arreglaran. Con el tiempo fueron apareciendo organizaciones como el CERT Coordination Center que se actuaban de intermediarios entre los investigadores y las empresas proveedoras. Los investigadores informaban a estas organizaciones sobre la vulnerabilidad, ellos la verificaban y si la confirmaban entonces informaban de forma secreta al proveedor y una vez que el arreglo estaba disponible entonces publicaba los detalles de la vulnerabilidad.

También aparecieron pequeños círculos cerrados donde hackers, ingenieros del software y profesionales de la seguridad intercambiaban información sobre vulnerabilidades. Como ejemplo de este tipo de organizaciones podríamos destacar la Zardoz 'Security-Digest'. El que la información fuera compartida por, en principio, personas que no iban a usar esta información de forma ilícita, no garantizaba en absoluto que no fuera usada de forma ilícita ya que tener acceso a esta información se convertía en objetivo básico de hackers con fines ilícitos. En definitiva, estos 'secretos' eran usados tanto de forma bienintencionada como maliciosa y esa información raramente llegaba a los ojos del público en general.

 Motivaciones
Motivaciones para que un investigador que descubre una vulnerabilidad adopte este tipo de política:
 Mantener en secreto para poder utilizar indefinidamente esa vulnerabilidad para atacar sistemas. Es la actitud típica de atacantes de sistemas que buscan beneficio propio.
 Poder venderla (mercado de vulnerabilidades)
 Por pereza. Puede resultar laborioso y tedioso estudiar y/o publicar una vulnerabilidad recién descubierta.

 Inconvenientes
Inconvenientes de esta política de revelación de vulnerabilidades:
 El sistema permanece vulnerable (puede ser objeto de ataque) sin que el usuario sepa el riesgo que corre y pueda tomar medidas. Se asume que los atacantes maliciosos no pueden descubrir por sí mismo vulnerabilidades. Sólo se revelan los detalles si se dispone el arreglo para la misma.
 La falta de publicidad no motiva al productor del software a reparar una vulnerabilidad en un tiempo adecuado. Se ha comprobado que sin esta motivación los proveedores no invierten recursos (dinero y tiempo) en hacer los sistemas más seguros y solucionar rápidamente las vulnerabilidades existentes. Tardan mucho tiempo en solucionar los problemas o simplemente los ignoran confiando en que la información no se difundirá porque se mantendrá en secreto. Esto es debido a que los proveedores ofrecen sistemas a otras empresas. Las vulnerabilidades no afectan directamente a las empresas proveedoras, afectan directamente a sus clientes. Por esta razón las empresas proveedoras tienden a tratar la información sobre vulnerabilidades como informes sobre problemas de sus productos, no como problemas que afectan a la empresa en sí. Hay que motivar más profundamente a los proveedores a resolver estos problemas.
 Es imposible evaluar el grado de seguridad ya que no hay un conjunto de personas de confianza que tengan acceso a toda la información sobre vulnerabilidades.
 Dificulta la educación sobre seguridad y por tanto dificulta que se pueda ir mejorando la calidad de los productos.

 Referencias
 Andrew Cencini et ali., "Software Vulnerabilities: Full-, Responsible-, and Non-Disclosure". Diciembre 2005
 Stephen A. Sheperd,"Vulnerability Disclosure. How do we define Responsible Disclosure?. SANS Institute. Abril 2003
