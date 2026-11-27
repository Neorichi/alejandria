---
type: Artículo de enciclopedia
title: Dan Kaminsky
description: Dan Kaminsky (c. 1979 - San Francisco (California), 23 de abril de 2021) fue un conocido investigador en seguridad informática estadounidense.
resource: https://es.wikipedia.org/wiki/Dan_Kaminsky
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Dan_Kaminsky"}
license: CC BY-SA 4.0
id: eswiki-Dan_Kaminsky
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Dan Kaminsky

**Dan Kaminsky** (c. 1979 - San Francisco (California), 23 de abril de 2021) fue un conocido investigador en seguridad informática estadounidense. Fue científico Jefe (*Chief Scientist*) de White Ops, una empresa especializada en detectar actividad de malware usando JavaScript. Trabajó para Cisco, Avaya, y IOActive, donde fue director de Pruebas de penetración. Es conocido por descubrir el error de envenenamiento de Caché DNS en el 2008 y que el Rootkit de Sony había infectado al menos a  computadores. Fue un habitual en conocidas conferencias de seguridad como el Black Hat y el Chaos Communication Congress.

En junio de 2010, Kaminsky liberó Interpolique, una herramienta en beta para identificar ataques de inyección tales como SQL injection o Cross-site scripting de una forma agradable para desarrolladores.

El 16 de junio de 2010, fue nombrado por ICANN como uno de los representantes con confianza de la comunidad para la raíz DNSSEC.

 Falla en DNS
En julio de 2008, el equipo de preparación para emergencias informáticas (US-CERT) de Estados Unidos anunció que Kaminsky había descubierto una falla fundamental en el protocolo del Sistema de nombres de dominio (DNS). El fallo podría permitir a los atacantes realizar fácilmente ataques de envenenamiento de caché en la mayoría de los servidores de nombres (solo djbdns, PowerDNS, MaraDNS y Unbound no eran vulnerables).
Con la mayoría de las aplicaciones basadas en Internet en función de DNS para localizar a sus compañeros, una amplia gama de ataques hizo factible, incluyendo la suplantación de sitios web, la interceptación de correo electrónico, y omisión de autenticación a través de la función "Olvidé mi contraseña" en muchos sitios web populares.

Kaminsky trabajó con los proveedores de DNS en secreto para desarrollar un parche y hacer que explotar la vulnerabilidad fuera mucho más difícil, liberándolo el 8 de julio de 2008. La vulnerabilidad en sí no ha sido completamente solucionada, ya que es un error de diseño de DNS en sí mismo.

Kaminsky había tenido la intención de no dar a conocer los detalles del ataque hasta 30 días después del lanzamiento del parche, pero los detalles se filtraron el 21 de julio de 2008. La información fue retirada rápidamente, pero no antes de que fuera difundida por otros.

Kaminsky recibió una cantidad sustancial de prensa generalista después de revelar su vulnerabilidad, pero también experimentó algo de rechazo de parte de la comunidad de seguridad informática por no revelar inmediatamente su ataque.

La vulnerabilidad se relaciona con el hecho de que el DNS solo tiene 65.536 posibles identificadores de transacción, un número suficientemente pequeño para ser adivinado al tener suficientes oportunidades. Dan Bernstein, autor de djbdns, había informado esta ya en 1999. djbdns solucionó el tema utilizando la asignación aleatoria de puerto de origen, en el que se utilizó el puerto UDP como un segundo identificador de transacción, aumentando así las opciones a identificar a miles de millones. Otras implementaciones de servidores de nombres más populares dejaron el asunto sin resolver debido a las preocupaciones sobre el rendimiento y la estabilidad, ya que muchos núcleos del sistema operativo simplemente no fueron diseñados para recorrer miles de sockets por segundo. En cambio, otros ejecutores asumieron que el Tiempo de vida (TTL) del DNS limitaría un adivinador que solo unos pocos intentos al día.

El ataque de Kaminsky omite esta defensa TTL apuntando nombres "hermanos" como "83.example.com" en lugar de "www.example.com" directamente. Debido a que el nombre era único, no tenía entrada en la caché, y por lo tanto no TTL. Pero debido a que el nombre era un hermano, la respuesta para adivinar la Id de transacción podría incluir no solo la información para sí mismo, sino que del objetivo también. Mediante el uso de muchos nombres "hermanos" seguidos, podría inducir a un servidor DNS para hacer muchas peticiones a la vez. Esto proporcionaba suficientes oportunidades para adivinar la ID de transacción y suplantar con éxito una respuesta en un plazo de tiempo razonable.

Para solucionar esto, todos los principales servidores DNS implementaron la aleatorización de puertos de origen, tal como djbdns y PowerDNS habían hecho antes. Esta corrección es ampliamente vista como una medida provisional, ya que solo hace que el ataque sea unas 65.536 veces más difícil. Un atacante dispuesto a enviar miles de millones de paquetes todavía podría corromper nombres. Se ha propuesto DNSSEC como la forma de dar garantía criptográfica a los resultados proporcionados por el DNS, y Kaminsky ha hablado a favor de ella.

 Rootkit de Sony
Durante el escándalo  de la protección de copia de CDs BMG Sony, Kaminsky utilizó snooping al caché DNS para averiguar si los servidores habían contactado recientemente cualquiera de los dominios que eran accedidos por el rootkit de Sony o no. Él utilizó esta técnica para estimar que había por lo menos 568 200 redes que tenían ordenadores con el rootkit.

 Earthlink y búsqueda de DNS

En abril de 2008 Kaminsky se dio cuenta de una práctica cada vez mayor entre los ISP que representaba una vulnerabilidad de seguridad potencial. Varios proveedores de Internet habían experimentado con la interceptación de mensajes de retorno de nombres de dominio no existentes y reemplazarlos con contenido publicitario. Esto podría permitir a piratas informáticos establecer esquemas de phishing atacando el servidor responsable de los anuncios y la vinculación a subdominios inexistentes de los sitios web de destino. Kaminsky demostró este proceso mediante la creación de Rickrolls en Facebook y PayPal. Si bien la vulnerabilidad utilizada inicialmente dependía en parte de que Earthlink utilizaba Barefruit para proporcionar su publicidad, Kaminsky fue capaz de generalizar la vulnerabilidad a Verizon, atacando su proveedor de anuncios, Paxfire.

Kaminsky se hizo pública después de trabajar con las redes de anuncios en cuestión para eliminar la vulnerabilidad cross-site scripting inmediata.

 Detección automática de Conficker
El 27 de marzo de 2009, Kaminsky descubrió que los hosts infectados por Conficker tienen una firma detectable cuando se escanea de forma remota. Las actualizaciones de firmas para una serie de aplicaciones de escaneo de red ahora están disponibles, incluyendo NMap y Nessus.

 Los defectos en Infraestructura X.509 de Internet
En 2009, en cooperación con Meredith L. Patterson y Len Sassaman, Kaminsky descubrió numerosas fallas en el protocolo SSL. Estos incluyen el uso de funciones hash MD2 débiles por Verisign en uno de sus certificados raíz y errores en los analizadores de certificación en varios navegadores web que permitían a los atacantes solicitar con éxito los certificados para sitios que no controlaban.

 Ataque de "Zero for 0wned"
El 28 de julio de 2009, Kaminsky, junto con varios otros consultores de seguridad de alto perfil, experimentó la publicación de sus correos electrónicos personales y datos de servidores por parte de piratas informáticos asociados a la revista en línea "Zero for 0wned". El ataque parecía estar diseñado para coincidir con la aparición de Kaminsky en las conferencias Black Hat Briefings y DEF CON.

 Referencias

 Enlaces externos
 Explicación sobre el error de envenenamiento de Cache
 Artículo de Wired en la historia de Dan Kaminsky y el DNS
 Sitio web de la empresa White Ops, de la cual Dan Kaminsky es uno de los fundadores
