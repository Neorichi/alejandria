---
type: Artículo de enciclopedia
title: Red de confianza
description: En criptografía, una red de confianza es un concepto usado en PGP, GnuPG, y otros sistemas compatibles con OpenPGP para certificar la autenticidad de que una clave pública pertenece a su dueño.
resource: https://es.wikipedia.org/wiki/Red_de_confianza
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Red_de_confianza"}
license: CC BY-SA 4.0
id: eswiki-Red_de_confianza
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Red de confianza

En criptografía, una **red de confianza** es un concepto usado en PGP, GnuPG, y otros sistemas compatibles con OpenPGP para certificar la autenticidad de que una clave pública pertenece a su dueño.

Se basa en que los participantes en la red firman entre sí sus claves públicas con sus claves privadas, certificando de esta manera que la clave pública pertenece a la persona física a la que se atribuye. La persona que firma debe establecer esta correspondencia sobre la base de un conocimiento externo, como por ejemplo haberse encontrado físicamente con la persona de la que certifica la clave en el mundo real. El interés del concepto está en que todos los demás conocidos del firmante, aunque se encuentren en un lugar remoto, tienen ahora un vínculo que les asegura que pueden confiar en los mensajes (por ejemplo, código de software) firmados con la clave privada de la persona certificada.

 Características

El concepto de red de confianza fue propuesto por primera vez en 1992 por el creador de PGP Phil Zimmermann en el manual para la versión 2.0 de PGP:

Los participantes en una red de confianza deben firmar entre sí sus claves públicas, certificando que avalan la correspondencia entre el nombre atribuido a la clave y la clave en sí misma. Esto sucede a menudo en fiestas conocidas como fiestas de firmado de claves (*key signing parties*, en inglés).

De este modo se implementa un modelo de confianza descentralizado que contrasta con el modelo centralizado basado en PKI (que sólo considera certificados firmados por autoridades certificadoras). Existen multitud de redes de confianza, y un usuario puede pertenecer a cuantas de ellas desee.

Las implementaciones compatibles con OpenPGP suelen incluir un sistema de recuento de votos que puede servir para determinar cuáles asociaciones entre dueño y clave pública serán de confianza para un usuario mientras esté usando PGP. Por ejemplo, si tres avalistas parcialmente confiados por el usuario han garantizado un certificado (y por tanto la correspondencia que incluye entre clave pública y dueño), o si un avalista plenamente de confianza ha hecho lo mismo, entonces la correspondencia se tomará como cierta. Los parámetros son ajustables por el usuario; por ejemplo, se puede requerir que no haya votos de avalistas solo parcialmente de confianza, o como mínimo 6 parciales sustituirán a un aval directo, o circunvalar el sistema de votos por completo.

 Contraste con el esquema PKI

Por contraste, el esquema PKI formalizado en X.509 solo permite que cada certificado esté firmado por una única entidad: una autoridad de certificación (CA, en sus siglas en inglés). El certificado de la CA puede estar él mismo firmado por una CA diferente, subiendo en una jerarquía de certificados hasta un llegar a uno firmado por sí mismo, también llamado certificado raíz (en inglés, *root certificate*). Los certificados raíz deben estar disponibles para aquellos que usen una CA de menor nivel y por tanto son ampliamente distribuidos. Por ejemplo, vienen incorporados en aplicaciones como navegadores, clientes de correo electrónico, y en sistemas operativos como Mac OS X. De esta manera, aquellas páginas web o correos electrónicos protegidos mediante el protocolo SSL/TLS pueden ser autenticados sin necesidad de que el usuario instale manualmente un certificado raíz. Estas aplicaciones comúnmente incluyen más de un centenar de certificados raíz de una docena de PKIs diferentes, otorgando así por defecto confianza a toda la jerarquía de certificados que asciende de nuevo hasta ellos.

El mecanismo de red de confianza es flexible, al contrario que la mayoría de arquitecturas de PKI, y deja las decisiones acerca de la confianza en las manos de los usuarios individuales. No es un sistema perfecto y requiere al mismo tiempo precaución y supervisión inteligente por parte de los usuarios. Esencialmente todos los diseños de PKI son menos flexibles y requieren que el usuario siga la cadena de garantías de los certificados generados por la CA.

A cambio, el usuario gana en comodidad y en facilidad de uso con un esquema PKI, puesto que no necesita tener conocimientos técnicos para establecer una comunicación de confianza a través de los mecanismos ya establecidos en su navegador.

 Referencias

 Enlaces externos

 Explicación de la red de confianza en PGP (en inglés)
 "The PGP Trust Model" de Alfarez Abdul-Rahman
