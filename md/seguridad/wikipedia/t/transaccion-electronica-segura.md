---
type: Artículo de enciclopedia
title: Transacción electrónica segura
description: "Transacción electrónica segura o SET (del inglés, Secure Electronic Transaction) es un protocolo estándar para proporcionar seguridad a una transacción con tarjeta de Identificación en redes de computadoras inseguras, …"
resource: https://es.wikipedia.org/wiki/Transacción_electrónica_segura
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Transacción_electrónica_segura"}
license: CC BY-SA 4.0
id: eswiki-Transacción_electrónica_segura
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Transacción electrónica segura

**Transacción electrónica segura** o **SET** (del inglés, *Secure Electronic Transaction*) es un protocolo estándar para proporcionar seguridad a una transacción con tarjeta de Identificación en redes de computadoras inseguras, en especial Internet.

SET surge de una solicitud de estándar de seguridad por VISA y MasterCard en diciembre de 1996 y la especificación inicial involucró a un amplio rango de Empresas, tales como GTE, IBM, Microsoft, Netscape, RSA y VeriSign.

SET utiliza técnicas criptográficas tales como certificados digitales y criptografía de clave pública para permitir a las entidades llevar a cabo una autenticación entre sí y además intercambiar información de manera segura.

SET fue muy Editado a finales de la década de 1990 como el estándar de facto para el uso de tarjetas de crédito. Sin embargo, no logró el éxito anunciado, debido a la necesidad de instalar software cliente (por ejemplo, una eWallet), y el costo y la complejidad de los vendedores para ofrecer soporte.

A partir del año 2000, las compañías de tarjetas de crédito comenzaron a promocionar un nuevo estándar para reemplazar SET, denominado 3-D Secure.

Por otro lado las implementaciones actuales de e-commerce que solo utilizan el protocolo SSL presentan un bajo costo y simplicidad en su implementación sin ofrecer la misma calidad de servicios criptográficos que las nuevas alternativas.

 Requerimientos del negocio
El *Libro 1* de la especificación de SET enlista los siguientes requerimientos de negocio para procesamiento de pago seguro con tarjeta de crédito a través de Internet y otras redes:
 Proveer confidencialidad de pago e información de órdenes de compra
 Asegurar la integridad de la totalidad de los datos que se transmiten
 Proveer autenticación de que el portador de una tarjeta es un usuario legítimo de una cuenta de tarjeta de crédito
 Proveer autenticación de que el comerciante puede aceptar transacciones con tarjetas de crédito a través de su relación con una institución financiera
 Asegurar el uso de las mejores prácticas de seguridad y de técnicas de diseño de sistemas para proteger los involucrados legítimos en la transacción de comercio electrónico
 Crear un protocolo que no dependa de mecanismos de seguridad de transporte ni que prevenga su uso
 Facilitar y promover la interoperabilidad entre proveedores de software y redes

 Funcionamiento
Hay que tener en cuenta que el protocolo SET opera a nivel de aplicación y para comercio electrónico.

Pasos:

1. Intercambios de certificados de vendedor y de pasarela de pago.

2. El servidor responde con su certificado de vendedor que se emplea en la firma y el certificado de pasarela para la transacción.

3. En la petición de compra, el cliente proporciona la información del pedido, y adjunta la firma del titular. El titular ha creado un doble mensaje, uno para el vendedor con la información del pedido y otro para la entidad bancaria con la información del pago. El banco actúa de intermediario para autorizar el pago entre el cliente y el vendedor.

4. El proceso termina con una confirmación firmada con el certificado del vendedor.

 Véase también
 SSL

 Referencias
