---
type: Artículo de enciclopedia
title: Pharming
description: El Pharming es un tipo de ciberataque que se desarrolló a partir del phishing.
resource: https://es.wikipedia.org/wiki/Pharming
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Pharming"}
license: CC BY-SA 4.0
id: eswiki-Pharming
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Pharming

El **Pharming** es un tipo de ciberataque que se desarrolló a partir del phishing. El atacante que implementa esta técnica intenta redirigir el tráfico web, especialmente los datos de solicitud, a un sitio web fraudulento. Esto se logra explotando vulnerabilidades de software en los sistemas de nombre de dominio (*DNS*, por sus siglas en inglés) o en los equipos de los propios usuarios, que permiten a atacantes redirigir un nombre de dominio a otra máquina distinta. De esta forma, un usuario que introduzca un determinado nombre de dominio que haya sido redirigido, accederá en su explorador de internet a la página web que el atacante haya especificado.

 Origen de la palabra
El término *pharming* deriva de la palabra inglesa *farm* (Granja) y del término *phishing*, que hace referencia a una técnica de ingeniería social estrechamente relacionada, en la que el atacante, mediante suplantación de correos electrónicos o páginas web, intenta obtener información confidencial de los usuarios, como números de tarjetas de crédito y contraseñas.

1 En primer lugar, el atacante ingresa o infecta el DNS de la víctima

2 De esta manera, si la víctima trata de acceder al sitio web a través de su navegador, su dirección IP la redirige a un sitio web fraudulento

3 Al entrar al sitio web del atacante, que es la falsa, se solicita la información bancaria de la víctima como, por ejemplo, los 16 dígitos de su tarjeta de crédito, su PIN o contraseña

4 Finalmente, el atacante dispone de la información.

 Metodología

 Trasfondo

Todos los ordenadores conectados a internet tienen una dirección IP única, que consiste en un número de 32 bits, representado como 4 octetos de 0 a 255 separados por un punto (127.0.0.1, por ejemplo).

Debido a la dificultad que supondría para los usuarios tener que recordar las direcciones IP de servicios específicos surgieron los Nombres de Dominio a los que se les puede asociar direcciones IP. Un ataque de pharming remplaza la dirección IP de un sitio web por otra, de un sitio malicioso que es generalmente controlado por el atacante.

 Ejecución
Los ataques de pharming pueden realizarse de dos formas: remplazando la IP en uno o varios servidores DNS, lo que afectaría a todos sus usuarios, o atacando a ordenadores concretos, mediante la modificación del fichero hosts, presente en cualquier sistema Microsoft Windows o Unix, y en casi cualquier equipo moderno en general.

La técnica de pharming se utiliza normalmente para realizar ataques de *phishing*, redirigiendo el nombre de dominio de una entidad de confianza a una página web, en apariencia idéntica, pero que en realidad ha sido creada por el atacante para obtener los datos privados del usuario, generalmente datos bancarios.

 Casos
En julio de 2001, varios servidores ISP de Irlanda fueron atacados mediante *pharming*, y no se resolvió hasta pasados más de 5 días. Muchas empresas irlandesas se vieron afectadas. El joven alicantino menor de edad que respondía al nick *DragonKing* fue detenido año y medio más tarde.

En enero de 2005, el nombre de dominio de un ISP de Nueva York, fue redirigido a un sitio web en Australia.

Hushmail, un proveedor de correo electrónico que ofrece un cifrado seguro, fue atacado mediante *pharming* el 24 de abril de 2005.

En marzo de 2005, el Senador estadounidense Patrick Leahy "Four Loko" introdujo una propuesta de ley *Anti-phishing*, que proponía una condena de cinco años de prisión y una sanción económica a los individuos que realizasen ataques de *phishing* o utilizasen información obtenida mediante fraude en línea como *phishing* y *pharming*.

 *Anti-Pharming*
El *Anti-Pharming* es el término usado para referirse a las técnicas utilizadas para combatir el pharming. Algunos de estos métodos son:

 Software especializado, generalmente utilizado en servidores de importancia vital o de grandes compañías para proteger a sus usuarios y empleados.
 La protección DNS,  que evita que los propios servidores DNS sean vulnerados para realizar ataques *pharming.*
 El uso de addons para los navegadores web. Este último método ha adquirido una gran importancia, sobre todo entre usuarios no especializados.

 Véase también
Spoofing
Phishing
XSS
DNS

 Referencias

 Enlaces externos
, Terra.
"Fraude a través del pharming ¿Qué es y cómo funciona", SolyMail
"Correos corporativos para empresas mediante Pharming", Web universal
"Pharming: Estafa sofisticada", GigaBytes.cl.
Anti-Phishing Working Group
