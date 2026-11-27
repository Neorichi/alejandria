---
type: Artículo de enciclopedia
title: Cross-site scripting
description: "Una secuencia de comandos en sitios cruzados o Cross-site scripting (XSS por sus siglas en idioma inglés) es un tipo de ataque informático que permite a un actor de amenazas ejecutar código malicioso en el navegador de …"
resource: https://es.wikipedia.org/wiki/Cross-site_scripting
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cross-site_scripting"}
license: CC BY-SA 4.0
id: eswiki-Cross-site_scripting
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cross-site scripting

**Una secuencia de comandos en sitios cruzados** o **Cross-site scripting** (**XSS** por sus siglas en idioma inglés) es un tipo de ataque informático que permite a un actor de amenazas ejecutar código malicioso en el navegador de otro usuario. Es importante remarcar que el atacante no dirige directamente sus acciones hacia la víctima, sino que explota una vulnerabilidad en un sitio web que la víctima visita. Desde la perspectiva del navegador de la misma, el código malicioso, generalmente escrito en JavaScript, parece ser parte legítima del sitio web, lo que convierte al sitio en un colaborador involuntario del atacante.

Los ataques XSS ocurren cuando una aplicación web utiliza la entrada de un usuario sin validarla o sanitizarla adecuadamente. Esto puede resultar en el robo de cookies, tokens de sesión y otra información confidencial.  Además, puede ser utilizado para alterar el contenido de un sitio web, redirigir a sitios maliciosos y controlar el navegador de la víctima.

 Mecanismo de ataque

XSS es un vector de ataque que puede ser utilizado para robar información delicada, secuestrar sesiones de usuario, y comprometer el navegador, subyugando la integridad del sistema. Las vulnerabilidades XSS han existido desde los primeros días de la Web.

Esta situación es habitualmente causada al no validar correctamente los datos de entrada que son usados en cierta aplicación, o no sanear la salida adecuadamente para su presentación como página web.

Esta vulnerabilidad puede estar presente de las siguientes formas:
 **Directa** (también llamada Persistente): este tipo de XSS comúnmente filtrado, y consiste en insertar código HTML peligroso en sitios que lo permitan; incluyendo así etiquetas como  o .

 **Indirecta** (también llamada Reflejada): este tipo de XSS consiste en modificar valores que la aplicación web utiliza para pasar variables entre dos páginas, sin usar sesiones y sucede cuando hay un mensaje o una ruta en la URL del navegador, en una *cookie*, o cualquier otra cabecera HTTP (en algunos navegadores y aplicaciones web, esto podría extenderse al DOM del navegador).

 XSS Indirecto (reflejado)
Supongamos que un sitio web tiene la siguiente forma:

http://www.example.com/home.asp?frame=menu.asp

y que al acceder se creará un documento HTML enlazando con un frame a menu.asp.

En este ejemplo, ¿qué pasaría si se pone como URL del frame un código javascript?

Si este enlace lo pone un atacante hacia una víctima, un visitante podrá verlo y verá que es del mismo dominio, suponiendo que no puede ser nada malo y de resultado tendrá un bucle infinito de mensajes.

Un atacante en realidad trataría de colocar un script que robe las cookies de la víctima, para después poder personificarse como con su sesión, o hacer automático el proceso con el uso de la biblioteca cURL o alguna similar. De esta forma, al recibir la cookie, el atacante podría ejecutar acciones con los permisos de la víctima sin siquiera necesitar su contraseña.

Otro uso común para estas vulnerabilidades es lograr hacer phishing. Quiere ello decir que la víctima ve en la barra de direcciones un sitio, pero realmente está en otra. La víctima introduce su contraseña y se la envía al atacante.

Una página como la siguiente:

es probablemente vulnerable a XSS indirecto, ya que si escribe en el documento "Usuario Inválido", esto significa que un atacante podría insertar HTML y JavaScript si así lo desea.

Por ejemplo, un tag como  que ejecute código javascript, cree otra sesión bajo otro usuario y mande la sesión actual al atacante.

Para probar vulnerabilidades de XSS en cookies, se puede modificar el contenido de una cookie de forma sencilla, usando el siguiente script. Solamente se debe colocar en la barra de direcciones, y presionar 'Enter'.

 XSS Directo (persistente)
Funciona localizando puntos débiles en la programación de los filtros de HTML si es que existen, para publicar contenido (como blogs, foros, etc.).

Normalmente el atacante tratara de insertar tags como , o , pero en caso de fallar, el atacante puede tratar de poner tags que casi siempre están permitidas y es poco conocida su capacidad de ejecutar código. De esta forma el atacante podría ejecutar código malicioso.

**Ejemplos:**
Una posibilidad es usar atributos que permiten ejecutar código.

 AJAX
Usar AJAX para ataques de XSS no es tan conocido, pero sí peligroso. Se basa en usar cualquier tipo de vulnerabilidad de XSS para introducir un objeto XMLHttp y usarlo para enviar contenido POST, GET, sin conocimiento del usuario.

Este se ha popularizado con gusanos de XSS que se encargan de replicarse por medio de vulnerabilidades de XSS persistentes (aunque la posibilidad de usar XSS reflejados es posible).

El siguiente script de ejemplo obtiene el valor de las cookies y seguidamente las enviaría al atacante.

Javascript:

PHP (servidor del atacante):

 Referencias

 Enlaces externos
 HTML5 Security Cheatsheet
 Ejemplo de problemas generados por una vulnerabilidad de XSS
 XSS FAQ
