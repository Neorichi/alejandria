---
type: Artículo de enciclopedia
title: Clickjacking
description: "El clickjacking (secuestro de clic) es una técnica maliciosa para engañar a usuarios de Internet con el fin de que revelen información confidencial o tomar control de su ordenador cuando hacen clic en páginas web …"
resource: https://es.wikipedia.org/wiki/Clickjacking
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Clickjacking"}
license: CC BY-SA 4.0
id: eswiki-Clickjacking
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Clickjacking

El **clickjacking** (secuestro de clic) es una técnica maliciosa para engañar a usuarios de Internet con el fin de que revelen información confidencial o tomar control de su ordenador cuando hacen clic en páginas web aparentemente inocentes. En un ataque de clickjacking mediante el uso de script, iframe, CSS y cuadros de texto permite que el atacante capture los datos en una capa que controla y el usuario no puede ver, debido a que utilizan diversos métodos para ocultarla.
 Descripción

El clickjacking es posible debido a características aparentemente inofensivas de una página web HTML que pueden ser empleadas para realizar acciones inesperadas.

Existen varias formas de ejecutar esta técnica:

 **Completamente oculto**: el ataque original consistía en cargar una pieza de contenido de la víctima en un iframe de 1x1 que evita que el usuario final pueda verla. Luego, el atacante centra el iframe 1x1 debajo del cursor para que el usuario final haga clic en él.
 **Eventos de puntero**: se crea una etiqueta div flotante sobre la interfaz de confianza. Utilizando la propiedad de CSS pointer-events en 'none', los eventos ocurren en el div implantado que recibe toda la información.
 **Recortar**: consiste en ocultar parte del contenido mediante recorte dejando visibles los botones originales de 'permitir' y 'cancelar'. Sin embargo, el atacante superpondría una nueva pregunta encima de la pregunta original. También puede presentarse como variante de este ataque, que se realice superposición de palabras individuales en la pantalla de confianza en lugar de superponer una sección completa.
 **Superposición transparente**: sobre la ventana de confianza  se crea una capa transparente. Esto hace que el usuario final crea que está haciendo clic en el contenido que se encuentra debajo de la ventana transparente, cada clic es registrado por la ventana transparente ya que es el contenido más alto en el momento del clic.

 Historia
El término clickjacking fue acuñado por Jeremiah Grossman y Robert Hansen en 2008, también conocido como UI redressing. El clickjacking puede ser entendido como una variante del problema de reemplazo confuso. La directiva de la Unión Europea de 2011 sobre privacidad, conocida como ley de cookies, obliga a los sitios web que almacenan datos sobre sus visitantes a incluir una advertencia. Recientemente, se ha comprobado el ataque a sitios web que consiste en modificar la advertencia incluida en el sitio para que su clic sea desviado, abriendo un sitio web diferente. Los ataques detectados incluyen publicidad no visible dentro del aviso de privacidad. Al hacer clic en cualquier parte del aviso aparece la página del sitio publicitado.

 Referencias

 Enlaces externos

 UNAM-CERT  Subdirección de Seguridad de la Información UNAM-CERT (noticias, documentos, información para usuarios, revista .Seguridad, alertas de seguridad, Malware UNAM, Honeynet UNAM, etc.)
 CORP: A Browser Policy to Mitigate Web Infiltration Attacks. December 2014, Bruhadeshwar Bezawada.
 CAPEC-103: Clickjacking. Common Attack Pattern Enumeration and Classification (CAPEC)
 Clickjacking. Mozilla.org
 Clickjacking: Attacks and Defenses. Actas del 21.º Simposio de Seguridad de USENIX. Agosto 2012.Microsoft. Lin-Shung Huang, Alex Moshchuk, Helen Wang, Stuart Schechter, Collin Jackson.
 Amenaza Clickjacking .World Wide Web Consortium
