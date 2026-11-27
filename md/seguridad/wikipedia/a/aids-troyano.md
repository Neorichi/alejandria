---
type: Artículo de enciclopedia
title: AIDS (troyano)
description: AIDS, también conocido como Aids Info Disk o PC Cyborg Trojan, es un troyano que reemplaza al archivo AUTOEXEC.BAT, que luego sería utilizado por AIDS para contar la cantidad de veces que la computadora se ha iniciado.
resource: https://es.wikipedia.org/wiki/AIDS_(troyano)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/AIDS_(troyano)"}
license: CC BY-SA 4.0
id: eswiki-AIDS_(troyano)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# AIDS (troyano)

- **Autor:** Joseph Popp
- **Nombre común:** PC Cyborg Trojan
- **Nombre técnico:** Aids Info Disk/PC Cyborg Trojan

**AIDS**, también conocido como **Aids Info Disk** o **PC Cyborg Trojan**, es un troyano que reemplaza al archivo AUTOEXEC.BAT, que luego sería utilizado por AIDS para contar la cantidad de veces que la computadora se ha iniciado. Una vez que este recuento de arranque alcanza 90, AIDS oculta los directorios y cifra los nombres de todos los archivos en la unidad C: (inutiliza el sistema), momento en el que se le pide al usuario que 'renueve la licencia' y se comunique con PC Cyborg Corporation para el pago (que implicaría enviar US$189 a un apartado postal en Panamá). Existe más de una versión de AIDS, y al menos una versión no espera a C :, pero ocultará directorios y cifrará los nombres de los archivos en el primer arranque después de instalar AIDS. También presenta al usuario un acuerdo de licencia de usuario final, algunos de los cuales decían:

 *Si instala [esto] en una microcomputadora...*
 *entonces, según los términos de esta licencia, usted acepta pagar a PC Cyborg Corporation en su totalidad por el costo del arrendamiento de estos programas...*
 *En caso de incumplimiento de este acuerdo de licencia, PC Cyborg se reserva el derecho de emprender las acciones legales necesarias para recuperar las deudas pendientes con PC Cyborg Corporation y de utilizar los mecanismos del programa para garantizar la finalización de su uso...*
 *Estos mecanismos del programa afectarán negativamente a otras aplicaciones del programa...*
 *Se le informa de las consecuencias más graves de su incumplimiento de los términos de este acuerdo de licencia; su conciencia puede perseguirlo por el resto de su vida...*
 *y su [PC] dejará de funcionar normalmente...*
 *Está estrictamente prohibido compartir [este producto] con otros...*

AIDS se considera un ejemplo temprano de una clase de malware conocido como "ransomware".

 Historia
AIDS se introdujo en los sistemas a través de un disquete llamado "Disquete de introducción de información sobre el SIDA", que había sido enviado a una lista de correo. El biólogo evolutivo Dr. Joseph Popp, fue identificado como el autor del troyano.

Popp fue finalmente descubierto por la industria antivirus británica y se dictó contra él una orden de arresto de  Scotland Yard por lo que fue detenido e ingresado en la prisión de Brixton. Aunque acusado de once cargos de chantaje y claramente vinculado con el troyano, Popp se defendió diciendo que el dinero que se destinaba a la Corporación Cyborg de PC era para la investigación del SIDA. Biólogo formado en  Harvard, Popp era también colaborador de Flying Doctors, una sucursal de la African Medical Research Foundation (AMREF), y consultor de la OMS en Kenia, donde había organizado una conferencia  sobre el nuevo Programa Global de SIDA.

Joseph Popp se había comportado de manera errática desde el día de su arresto (durante una inspección de equipaje de rutina), en el aeropuerto Schiphol de Ámsterdam.Tras el juicio, fue declarado mentalmente no apto para ser juzgado y  devuelto a los Estados Unidos.

Jim Bates analizó el troyano en detalle y publicó sus hallazgos en el Virus Bulletin. Escribió que el troyano no altera el contenido de ninguno de los archivos del usuario, solo los nombres de archivo. Explicó que una vez que se conocen las tablas de extensión y cifrado de nombre de archivo, es posible la restauración. AIDSOUT fue un programa de eliminación confiable para el troyano y el programa CLEARAID recuperó texto plano cifrado después de que se activó el troyano. CLEARAID invirtió automáticamente el cifrado sin tener que contactar al extorsionista.

El troyano fue analizado aún más algunos años después. Young y Yung señalaron la debilidad fatal del malware como el troyano AIDS, es decir, la dependencia de la criptografía simétrica. Mostraron cómo usar la criptografía de clave pública para implementar un ataque seguro de extorsión de información. Publicaron este descubrimiento (y lo ampliaron) en un documento de Seguridad y Privacidad de la IEEE de 1996. Un híbrido de cryptovirus, cryptotroyano o cryptoworm encripta los archivos de la víctima utilizando la clave pública del autor y la víctima debe pagar (con dinero, información, etc.) para obtener la clave de sesión necesaria. Este es uno de los muchos ataques, tanto abiertos como encubiertos, en el campo conocido como criptovirología.

 Referencias

 Enlaces externos

 Un análisis temprano del troyano
 LA CAPACIDAD DE ASESORAMIENTO DE INCIDENTES INFORMÁTICOS, por CIAC, sobre la infección y distribución del SIDA
 The Original Anti-Piracy Hack, de George Smith, sobre el interesante EULA del SIDA
 Virus informáticos (A), por la Enciclopedia Probert
 Troyano de información sobre el SIDA, por CA
 Ayuda troyano, por CA
