---
type: Artículo de enciclopedia
title: Seguridad por oscuridad
description: "En criptografía y seguridad informática, la seguridad por oscuridad o por ocultación es un controvertido principio de ingeniería de la seguridad, que intenta utilizar el secreto (de diseño, de implementación, etc.) para …"
resource: https://es.wikipedia.org/wiki/Seguridad_por_oscuridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_por_oscuridad"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_por_oscuridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad por oscuridad

En criptografía y seguridad informática, la **seguridad por oscuridad** o **por ocultación** es un controvertido principio de ingeniería de la seguridad, que intenta utilizar el *secreto* (de diseño, de implementación, etc.) para garantizar la *seguridad*. Este principio se puede plasmar en distintos aspectos como por ejemplo:
Mantener el secreto del código fuente del software.
Mantener el secreto de algoritmos y protocolos utilizados.
Adopción de políticas de no revelación pública de la información sobre vulnerabilidades.

Un sistema que se apoya en la seguridad por ocultación puede tener vulnerabilidades teóricas o prácticas, pero sus propietarios o diseñadores creen que sus puntos débiles, debido al secreto que se mantiene sobre los entresijos del sistema, son muy difíciles de encontrar, y por tanto los atacantes tienen muy pocas probabilidades de descubrirlos.

 Introducción
Un ejemplo práctico de **seguridad por oscuridad** es esconder una copia de la llave de la casa bajo el felpudo de la entrada para evitar quedar atrapado fuera por olvido o pérdida de la llave principal. En este caso, la seguridad se basa en la ocultación, ya que los propietarios asumen que, al no ser visible, la llave está protegida. Sin embargo, esta medida presenta una vulnerabilidad: los ladrones suelen conocer escondites comunes, lo que hace que la protección sea poco efectiva.

Por otro lado, la seguridad por oscuridad no debe confundirse con medidas ineficaces que no mitigan un problema real. Por ejemplo, una organización que bloquea el Protocolo de transferencia de noticias a través de la red (NNTP) de los enrutadores de borde para evitar que los empleados lean grupos de noticias pero que permita el shell seguro (SSH) saliente no se considera seguridad por oscuridad. Debido a que SSH puede abrirse paso en cada protocolo, el problema no está oculto; la mitigación implementada no puede hacer nada más que evitar que los usuarios legítimos consigan realizar tareas legítimas sin infringir las directivas de seguridad. Dichas medidas no son seguridad por oscuridad.

 Argumentos contra la seguridad por oscuridad
Muchos argumentan que la seguridad por oscuridad es débil. Si la seguridad de un sistema depende única o principalmente de mantener oculta una debilidad, entonces, claramente, si esa debilidad es descubierta, la seguridad se compromete fácilmente. Se argumenta que mantener ocultos los detalles de sistemas y algoritmos ampliamente utilizados es difícil. En criptografía, por ejemplo, hay un buen número de ejemplos de algoritmos de cifrado que han pasado a ser de conocimiento público, bien por ingeniería inversa (ej. A5/1), bien por una fuga de información (ej. RC4).

Por otro lado, la seguridad por oscuridad implica llevar a cabo alguna medida que no detenga el vector de ataque sino que simplemente lo oculte. Por ejemplo, puede decidir mover el servidor web al puerto 81 en lugar de al 80, de forma que tan solo los usuarios que saben donde encontrar su servidor web lo podrán hacer. Al menos, ese es el argumento. En realidad, al mover el servidor web al puerto 81, solo se detienen algunos ataques y, en la mayoría de los casos, solo causa inconvenientes al usuario final. Un intruso tan solo tendrá que ejecutar un escaneo de puertos, y un captador de pancartas web contra un gran número de puertos para descubrir servidores web en puertos no estándar. Al encontrar uno, se podrá aprovechar de la vulnerabilidad de un servidor debido a que en realidad no se eliminó el vector de ataque, sino que tan solo se ocultó (temporalmente)

 En la práctica
Los operadores, desarrolladores y vendedores de sistemas que confían en la seguridad por oscuridad a menudo mantienen en secreto que sus sistemas tienen fallos, para evitar crear desconfianza en sus servicios o productos y por tanto, en su imagen de mercado. Es posible que esto pudiera conducir en algunos casos a una representación fraudulenta de la seguridad de sus productos, aunque la aplicación de la ley a este respecto ha sido poco contundente, en parte porque las condiciones de uso impuestas por los vendedores como parte del contrato de licencia redimen (con más o menos éxito) sus aparentes obligaciones bajo el estatuto legal de muchas jurisdicciones que requieren una adecuación para el uso o estándares de calidad similares.

Estas prácticas de seguridad dejan a los usuarios frente a problemas cuando el software que usan está deliberada o accidentalmente ocultado, como ha ocurrido otras veces:
 Sistema de Boleta Única Electrónica — sistema de voto electrónico de la República Argentina.
 Diebold — software de voto electrónico; publicación aparentemente accidental en un sitio web oficial.
 Microsoft — Windows y otros; penetración supuestamente deliberada en una red de desarrollo corporativa.
 RSADSI — algoritmos criptográficos; código de RC4 probablemente publicado con intención en Usenet.
 Cisco — sistema operativo de enrutadores; exposición accidental en una red corporativa.

Cuando se usa software *seguro por estar oculto* de manera amplia, existe un riesgo potencial de problema global; por ejemplo, vulnerabilidades en las diferentes versiones del sistema operativo Windows, sus componentes obligatorios como su navegador web Internet Explorer o sus aplicaciones de correo electrónico (Microsoft Outlook/Outlook Express) han causado problemas a lo largo y ancho del planeta cuando virus, troyanos, gusanos y demás se han aprovechado de ellas. Véase seguridad en Windows o seguridad en Internet Explorer.

Todavía hay muchas organizaciones que aceptan esta configuración porque permite que los ingenieros sean operadores de servidores en lugar de administradores, lo que significa que es menos probable que destruyan el servidor por accidente. Esto puede suponer alguna ventaja.

 Véase también
 Principios de Kerckhoffs
 Seguridad informática
 Esteganografía
 Criptografía

Referencias

 Enlaces externos
 A Model for when Disclosure Helps Security: What Is Different About Computer & Network Security?, Peter P. Swire
 Eric Raymond on Cisco's IOS source code 'release' v Open Source
 Computer Security Publications
