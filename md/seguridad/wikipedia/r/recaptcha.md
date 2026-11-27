---
type: Artículo de enciclopedia
title: ReCAPTCHA
description: Recaptcha o reCAPTCHA es el sistema Captcha que utiliza Google para detectar el tráfico procedente de programas automatizados o bots.
resource: https://es.wikipedia.org/wiki/ReCAPTCHA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/ReCAPTCHA"}
license: CC BY-SA 4.0
id: eswiki-ReCAPTCHA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# ReCAPTCHA

- **Nombre:** reCAPTCHA
- **Desarrollador:** Google
- **Autor:** * Luis von Ahn Ben Maurer Colin McMillen Harshad Bhujbal Manuel Blum
- **Genero:** Captcha

**Recaptcha** o **reCAPTCHA** es el sistema Captcha que utiliza Google para detectar el tráfico procedente de programas automatizados o *bots*.

Siguiendo prácticas monopolísticas, Google ha roto el sistema reCAPTCHA para usuarios DeGoogleados, lo que impide que teléfonos que no hayan sido certificados por Google puedan acceder al sistema.

 Versiones

 Primera versión (v1)
Inicialmente reCAPTCHA era un proyecto de una empresa independiente que fue comprada por Google en 2009. Era de tipo textual y obligaba al usuario a escribir en un recuadro el texto poco claro que venía en una imagen. El sistema colocaba dos palabras en sus pruebas de Captcha. De esas dos palabras una era conocida por el sistema y la otra provenía de palabras que el sistema OCR era incapaz de reconocer. El sistema pedía al usuario, que desconocía qué palabra es conocida y cuál no lo era, que introdujera ambas palabras como texto. Si la palabra conocida por el sistema era introducida correctamente por un humano, el sistema asumía que había probabilidades altas de que el usuario también hubiera introducido la palabra desconocida correctamente. Si la palabra desconocida recibe en múltiples ocasiones la misma transcripción humana (traducción de imagen a texto) se considera que esa transcripción es correcta.

A partir de 2012, Google empezó a incluir imágenes obtenidas de Google Street View, con el fin de que la palabra desconocida sean números o nombres de calles, para alimentar su base de datos y mejorar la precisión de direcciones.

Debido a la evolución de la Inteligencia Artificial se han creado programas que permiten automáticamente saltarsey

 Segunda versión (v2)
También llamada **No CAPTCHA reCAPTCHA**. Apareció en diciembre de 2020 como evolución del versión anterior. El sistema, en lugar de hacer los CAPTCHAs cada vez más complejos, nos  de vez en cuando una caja (caja de reCAPTCHA) en la que nos solicita que pulsemos sobre un recuadro con la etiqueta "No soy un robot". Cuando se pulsa, el sistema revisa el comportamiento que el usuario ha tenido anteriormente y en función de todo ello decide si es un usuario humano o un programa, permitiendo o prohibiendo su acceso. Para analizar el comportamiento el sistema usa un algoritmo secreto. Este algoritmo usa, por ejemplo, las cookies activas y dirección IP para verificar el comportamiento a través de Internet. También analiza el movimiento del ratón para ver cómo se comporta el usuario para pulsar en el cuadro de la caja de reCAPTCHA. Los bots suelen hacerlo de una manera automática, mientras que los humanos acostumbran ir manera indirecta a la caja seleccionable, por lo que el recorrido de nuestro ratón es diferente. En el caso de que el comportamiento del usuario le haga dudar al sistema de su naturaleza humana, el reCaptcha mostrará una ventana en la que le pedirá que escriba un texto o que haga clic sobre determinadas imágenes.

Todo el seguimiento que realiza sobre el comportamiento del usuario para determinar si es un humano o no, ha preocupado porque puede suponer una amenaza a la privacidad. Esta información podría ser usada, por ejemplo, para mejorar sus prestaciones (en publicidad, por ejemplo) más allá de la prevención para evitar el abuso por parte de programas. Ha habido investigadores que al analizar el comportamiento del reCaptcha acusaron a Google de estar almacenando mucha más información sobre el comportamiento de los usuarios de la que decían. Dijeron también que aunque el sistema de seguridad no estaba anunciado como un producto de Google, hacía uso de sus cookies para registrar nuestros movimientos. Esto le permite tener unos perfiles más completos del comportamiento de los usuarios. Además aseguraron que también estaba registrando la resolución, el tamaño de pantalla de los cibernautas, la hora, su idioma, los plugins que tienen instalados en el navegador, todos los objetos de Javascript, información de CSS y registro de movimientos táctiles o de ratón que realice.

 Tercera versión (v3)
También llamada **reCaptcha invisible**. Apareció en octubre de 2019 Su objetivo es que los usuarios humanos no necesiten realizar ninguna acción para verificar que no son bots, ni siquiera marcando una casilla. Para ello introduce un análisis de riesgos y elabora distintos perfiles de riesgo. A cada usuario le asigna una puntuación diferente, clasificándolos del 0.0 al 1.0 en orden de más posible a menos posible de que sea un programa. La puntuación se basará en diferentes tipos de interacciones que realicen los usuarios, que van desde el movimiento del ratón al tiempo que pasan en cada sección de la web o los clicks que se realizan. La compañía aconseja su introducción en distintas páginas web para poder trazar un patrón de comportamiento con el que identificar interacciones de cada usuario en cada web. El sistema aumenta el control que tiene el sistema de la actividad del usuario, lo cual amenaza su privacidad. Además, esta tercera generación también permite a los administradores un mayor control de los usuarios. Podrán ver las puntuaciones de sus visitantes para saber hasta qué punto reciben tráfico real, y podrán requerir autenticación en dos pasos o verificación por correo electrónico para los usuarios con menos puntuación. Por defecto, reCaptcha v3 usará un umbral de 0.5 puntos, y los visitantes con una puntuación inferior necesitará demostrar que es humano como pasa ahora cuando el automatismo falla. Sin embargo, los usuarios de cada web podrán modificar este umbral, y se les permitirá entrenar el modelo de su web para combatir los bots que busquen saltarse la seguridad.

 Referencias
