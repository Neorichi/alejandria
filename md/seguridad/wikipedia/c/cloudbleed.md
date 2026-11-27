---
type: Artículo de enciclopedia
title: Cloudbleed
description: Cloudbleed fue un desbordamiento del búfer de Cloudflare revelado por Project Zero el 17 de febrero de 2017.
resource: https://es.wikipedia.org/wiki/Cloudbleed
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cloudbleed"}
license: CC BY-SA 4.0
id: eswiki-Cloudbleed
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cloudbleed

**Cloudbleed** fue un desbordamiento del búfer de Cloudflare revelado por Project Zero el 17 de febrero de 2017. El código de Cloudflare reveló el contenido de la memoria que contenía información privada de otros clientes, como cookies HTTP, tokens de autenticación, cuerpos HTTP POST y otros datos confidenciales.  Como resultado, los datos de los clientes de Cloudflare se filtraron a todos los demás clientes de Cloudflare que tenían acceso a la memoria del servidor. Esto ocurrió, según cifras proporcionadas por Cloudflare en ese momento, más de 18.000.000 de veces antes de que se corrigiera el problema.   Algunos de los datos filtrados fueron almacenados en caché por los motores de búsqueda.

 Descubrimiento
El descubrimiento fue informado por el equipo Project Zero de Google.  Tavis Ormandy publicó el problema en el rastreador de problemas de su equipo y dijo que informó a Cloudflare sobre el problema el 17 de febrero. En su propio ataque de prueba de concepto, consiguió que un servidor Cloudflare devolviera "mensajes privados de los principales sitios de citas, mensajes completos de un conocido servicio de chat, datos del administrador de contraseñas en línea, marcos de sitios de videos para adultos, reservas de hotel". Estamos hablando de solicitudes HTTPS completas, direcciones IP de clientes, respuestas completas, cookies, contraseñas, claves, datos, todo".

 Similitudes con Heartbleed
En sus efectos, Cloudbleed es comparable al error Heartbleed de 2014, en el sentido de que permitió a terceros no autorizados acceder a datos en la memoria de programas que se ejecutan en servidores web, incluidos datos que habían sido protegidos durante el tránsito por TLS .   Es probable que Cloudbleed también haya afectado a tantos usuarios como Heartbleed, ya que afectó a una red de entrega de contenido que presta servicios a casi dos millones de sitios web.

Tavis Ormandy, el primero en descubrir la vulnerabilidad, inmediatamente hizo una comparación con Heartbleed, diciendo que "se necesitó cada gramo de fuerza para no llamar a este problema 'cloudbleed'" en su informe.

 Reacciones

 Cloudflare
El jueves 23 de febrero de 2017, Cloudflare escribió una publicación señalando que:

Cloudflare reconoció que la memoria podría haberse filtrado ya el 22 de septiembre de 2016. La compañía también afirmó que se ha filtrado una de sus propias claves privadas, utilizada para el cifrado de máquina a máquina.

John Graham-Cumming, CTO de Cloudflare, señaló que los clientes de Cloudflare, como Uber y OkCupid, no fueron informados directamente de las filtraciones debido a los riesgos de seguridad involucrados en la situación. "No había comunicación de puerta trasera fuera de Cloudflare, sólo con Google y otros motores de búsqueda", dijo.

Graham-Cumming también dijo que "Desafortunadamente, era el antiguo software el que contenía un problema de seguridad latente y ese problema sólo apareció cuando estábamos en el proceso de migrar fuera de él". Añadió que su equipo ya ha comenzado a probar su software para detectar otros posibles problemas.

 Equipo del Proyecto Cero de Google
Tavis Ormandy inicialmente declaró que estaba "realmente impresionado con la rápida respuesta de Cloudflare y lo dedicados que están a solucionar este desafortunado problema".  Sin embargo, cuando Ormandy presionó a Cloudflare para obtener información adicional, "dieron varias excusas que no tenían sentido",  antes de enviar un borrador que "minimiza gravemente el riesgo para los clientes".

 Uber
Uber afirmó que el impacto en su servicio fue muy limitado.  Un portavoz de Uber agregó que "sólo un puñado de tokens de sesión estuvieron involucrados y desde entonces se cambiaron. Las contraseñas no fueron expuestas".

 OKCupid
Elie Seidman, director ejecutivo de OKCupid, dijo: "CloudFlare nos alertó anoche de su error y hemos estado investigando su impacto en los miembros de OkCupid. Nuestra investigación inicial ha revelado una exposición mínima, si es que hay alguna. Si determinamos que alguno de nuestros usuarios ha sido afectados, les notificaremos de inmediato y tomaremos medidas para protegerlos".

 Fitbit
Fitbit afirmó que habían investigado el incidente y sólo encontraron que "un puñado de personas se vieron afectadas". Recomendaron que los clientes preocupados cambiaran sus contraseñas y borraran los tokens de sesión revocando y volviendo a agregar la aplicación a su cuenta.

 1Password
En una publicación de blog, Jeffery Goldberg declaró que ningún dato de 1Password estaría en riesgo debido a Cloudbleed, citando el uso por parte del servicio del protocolo Secure Remote Password (SRP), en el que el cliente y el servidor prueban su identidad sin compartir ningún secreto a través de la red. . Los datos de 1Password se cifran adicionalmente utilizando claves derivadas de la contraseña maestra del usuario y un código de cuenta secreto, que según Goldberg protegería las credenciales incluso si los propios servidores de 1Password fueran violados. 1Password no sugirió a los usuarios que cambiaran su contraseña maestra en respuesta a una posible infracción relacionada con el error.

Medidas para hacerle frente
Muchos medios de comunicación importantes aconsejaron a los usuarios de sitios alojados en Cloudflare que cambiaran sus contraseñas, ya que incluso las cuentas protegidas por autenticación multifactor podrían estar en riesgo.      Las contraseñas de las aplicaciones móviles también podrían haberse visto afectadas.  Los investigadores de Arbor Networks, en una alerta, sugirieron que "Para la mayoría de nosotros, la única respuesta verdaderamente segura a esta fuga de información a gran escala es actualizar nuestras contraseñas para los sitios web y servicios relacionados con aplicaciones que utilizamos todos los días... Casi todos."

Sin embargo, el columnista de ciberseguridad de Inc. Magazine, Joseph Steinberg, aconsejó a la gente que no cambiara sus contraseñas, afirmando que "el riesgo actual es mucho menor que el precio a pagar en una mayor 'fatiga de ciberseguridad' que conducirá a problemas mucho mayores en el futuro".

 Referencias
