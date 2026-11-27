---
type: Artículo de enciclopedia
title: Pasarela de pago
description: "La pasarela de pago es el servicio de un proveedor de servicios de aplicación de comercio electrónico, con el que se autorizan pagos a negocios electrónicos, ventas en línea al detalle, negocios con presencia física y …"
resource: https://es.wikipedia.org/wiki/Pasarela_de_pago
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Pasarela_de_pago"}
license: CC BY-SA 4.0
id: eswiki-Pasarela_de_pago
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Pasarela de pago

La **pasarela de pago** es el servicio de un proveedor de servicios de aplicación de comercio electrónico, con el que se autorizan pagos a negocios electrónicos, ventas en línea al detalle, negocios con presencia física y en línea simultáneamente (modelo de negocio ladrillos y clics, o a negocios tradicionales (modelo de negocio *brick and mortar*, traducción literal "ladrillo y hormigón").

Es el equivalente de un terminal punto de venta (TPV) físico ubicada en la mayoría de los almacenes al detalle o negocios minoristas.

Las pasarelas de pago cifran información sensible, como los números de tarjetas de crédito, para garantizar que la información pasa en forma segura entre el cliente y el vendedor.

Es el método de pago más utilizado en el comercio electrónico, llegando a realizarse un 65,3% de la facturación de tiendas en línea a través de estas pasarelas. Los métodos de pago más comunes usados por un consumidor a la hora de pagar 'en línea' usando una pasarela de pagos son las tarjetas, básicamente de estos cuatro esquemas: Visa, MasterCard, American Express, Discover.

En los últimos tiempos y debido a la proliferación de más métodos de pago locales, se ha acuñado el término *APM* (métodos de pago alternativos) para todos aquellos que no se engloban dentro del grupo de tarjetas. Algunos ejemplos son: MultiBanco, SEPA Direct debit, Ideal, Sofort, Blik, Bizum...

 Funcionamiento
Una pasarela de pago facilita la transferencia de información entre un portal de pago (como un sitio web o un servicio *Interactive Voice Response* -IVR-) y el Procesador Interfaz o banco adquirente de manera rápida y segura.

Cuando un cliente ordena un producto de un vendedor que tiene habilitado una pasarela de pago, ésta realiza una serie de tareas para procesar la transacción, de manera transparente para el comprador. Por ejemplo:
 Un cliente realiza un pedido en un sitio web presionando el botón de «Pagar» (o similar) o introduce los detalles de su tarjeta de crédito a un servicio IVR.
 Si la orden es a través de un sitio web, el navegador web del cliente cifra la información que viaja hasta el servidor web del vendedor. Esto se hace normalmente mediante cifrado *Seguridad de la Capa de Transporte (en inglés Secure Socket Layer* o SSL) o *Transport Layer Security*.
 El vendedor reenvía los detalles de la transacción a su pasarela de pago, la cual contiene los detalles de las cuentas de sus vendedores. Normalmente, ésta es otra conexión cifrada mediante SSL al servidor de pago, almacenada en la pasarela de pago.
 La pasarela de pago que recibe la información de la transacción del vendedor, reenvía la información al banco adquirente del vendedor.
 El banco adquirente reenvía la información de la transacción al banco emisor (el banco que le emitió la tarjeta de crédito al cliente) para su autorización. En este momento la pasarela también envía datos de si la transacción se debe de procesar mediante el protocolo 3d Secure que añade una capa de seguridad adicional y que envía una notificación vía móvil o computadora de escritorio al comprador, para que certifique en tiempo real (y apruebe o no) que está queriendo hacer dicha transacción.
 El banco emisor de la tarjeta recibe la solicitud de autorización y envía una respuesta a la pasarela de pago (a través del banco adquirente) con un código de respuesta. Además de determinar el destino del pago (es decir, "aprobado" o "rechazado"), el código de respuesta se usa para definir la razón por la cual -eventualmenete- la transacción falló (como por ejemplo, por fondos insuficientes, código CVV inválido, tarjeta caducada).

 Véase también
 Comercio electrónico
 Ladrillos y clics
 Número de Referencia Completo (NRC)
 Pasarela de firma
 Proveedor de servicios de aplicación
 Terminal punto de venta (TPV)

 Referencias
