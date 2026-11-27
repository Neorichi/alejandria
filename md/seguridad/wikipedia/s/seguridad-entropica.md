---
type: Artículo de enciclopedia
title: Seguridad entrópica
description: La seguridad entrópica es una definición de seguridad utilizada en el campo de la criptografía.
resource: https://es.wikipedia.org/wiki/Seguridad_entrópica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_entrópica"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_entrópica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad entrópica

La **seguridad entrópica** es una definición de seguridad utilizada en el campo de la criptografía. En general, los esquemas de cifrado modernos deben proteger las comunicaciones incluso cuando el atacante dispone de información sustancial sobre los mensajes cifrados. Por ejemplo, aunque un atacante sepa que un texto cifrado interceptado encripta el mensaje "Ataque" o el mensaje "Retiro", un esquema de encriptación semánticamente seguro impedirá que el atacante sepa cuál de los dos mensajes está encriptado. Sin embargo, definiciones como la seguridad semántica son demasiado fuertes para lograrlas con ciertos esquemas de encriptación especializados. La seguridad entrópica es una definición más débil que puede utilizarse en el caso especial de que un atacante tenga muy poca información sobre los mensajes que se cifran.

Es bien sabido que ciertos tipos de algoritmos de cifrado no pueden satisfacer definiciones como la de seguridad semántica; por ejemplo, los algoritmos de cifrado deterministas nunca pueden ser semánticamente seguros. Las definiciones de seguridad entrópica relajan estas definiciones a los casos en los que el espacio de mensajes tiene una entropía sustancial (desde el punto de vista de un adversario). Con esta definición es posible demostrar la seguridad del cifrado determinista.

Obsérvese que, en la práctica, los algoritmos de encriptación con seguridad entrópica solo son "seguros" si la distribución del mensaje posee una alta entropía desde la perspectiva de cualquier adversario razonable. Esta es una suposición poco realista para un esquema de cifrado general, ya que no se puede suponer que todos los usuarios probables cifrarán mensajes de alta entropía. Para estos esquemas, son apropiadas definiciones más fuertes (como la seguridad semántica o la indistinguibilidad bajo un ataque de texto cifrado adaptable). Sin embargo, hay casos especiales en los que es razonable exigir mensajes de alta entropía. Por ejemplo, los esquemas de encriptación que solo encriptan el material de la clave secreta (por ejemplo, los esquemas de encapsulación de claves o de envoltura de claves) pueden considerarse bajo una definición de seguridad entrópica. Una aplicación práctica de este resultado es el uso de algoritmos de cifrado determinista para el cifrado seguro de material de clave secreta.

Russell y Wang formalizaron una definición de seguridad entrópica para el cifrado. Su definición se asemeja a la definición de seguridad semántica cuando los espacios de mensajes tienen una distribución altamente entrópica. En una formalización, la definición implica que un adversario dado el texto cifrado será incapaz de calcular cualquier predicado sobre el texto cifrado con una probabilidad (sustancialmente) mayor que un adversario que no posea el texto cifrado. Dodis y Smith propusieron posteriormente definiciones alternativas y demostraron su equivalencia.

 Referencias
