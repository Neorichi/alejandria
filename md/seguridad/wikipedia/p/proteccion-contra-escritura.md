---
type: Artículo de enciclopedia
title: Protección contra escritura
description: "La protección contra escritura es una política que impide la eliminación, modificación y formateo de cualquier tipo de información en una unidad, ya sea por el hecho de que el usuario no posea privilegios o que esa …"
resource: https://es.wikipedia.org/wiki/Protección_contra_escritura
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protección_contra_escritura"}
license: CC BY-SA 4.0
id: eswiki-Protección_contra_escritura
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protección contra escritura

La **protección contra escritura** es una política que impide la eliminación, modificación y formateo de cualquier tipo de información en una unidad, ya sea por el hecho de que el usuario no posea privilegios o que esa información esté protegida por el propio dispositivo (hardware) en el que está almacenada.

 Protección por hardware

En este caso, la protección es un medio físico que previene la escritura, modificación o borrado de los datos del dispositivo. Buena parte del video, el audio y el software comercial en formato físico grabable está protegido contra escritura al ser distribuido.

Ejemplos:

 Los carretes de cinta magnética de IBM de 7 pistas y 9 pistas, introducidos en la década de 1950, tenían una ranura circular en un lado del carrete, en la que se tenía que colocar un anillo de plástico blando para escribir en la cinta («Sin anillo, sin escritura»).
 Los casetes de audio y videocasetes VHS tienen pestañas en el borde superior/posterior que se pueden romper (sin pestaña = protegido).
 Los disquetes de 8 y 5 1/4 pulgadas pueden tener, respectivamente, muescas de protección contra escritura y de activación de escritura en el lado derecho (8": perforado = protegido; 5 1/4": tapado/muesca no presente = protegido). Una práctica común con los disquetes de un solo lado era perforar una segunda muesca en el lado opuesto del disco para permitir el uso de ambos lados del medio.
 Los disquetes de 3 1/2 pulgadas tienen una pestaña deslizante en una ventana en el lado derecho (abierto = protegido).
 Los discos zip de Iomega estaban protegidos contra escritura mediante el software IomegaWare.
 Los discos Syquest EZ-drive (135 y 250 MB) estaban protegidos contra escritura usando un pequeño interruptor de metal en la parte trasera del disco en la parte inferior.
 Los  videocasetes VHS-C, Video8, Hi8 y DV tienen una pestaña deslizante en el borde posterior.
 Los cartuchos de cinta Iomega Ditto tenían una pequeña lengüeta deslizante en la esquina superior izquierda de la cara frontal del cartucho.
 Las unidades flash USB a veces tienen un pequeño interruptor, aunque esto se ha vuelto poco común. Un ejemplo de una unidad flash USB compatible con protección de escritura a través de un interruptor es la serie Transcend JetFlash.
 Las memorias Secure Digital (SD) tienen una pestaña de protección contra escritura en el lado izquierdo.
 De forma extensiva, soportes que, por diseño, no pueden operar fuera de este modo: CD-R, DVD-R, discos de vinilo, etc.
Estos mecanismos están destinados a prevenir únicamente la pérdida accidental de datos o los ataques de virus informáticos. Un usuario determinado puede eludirlos fácilmente ya sea cubriendo una muesca con cinta adhesiva o creando una con un perforador según corresponda, o a veces alterando físicamente el dispositivo para ignorar el mecanismo de protección contra escritura.

La protección contra escritura normalmente la aplica el hardware. En el caso de los dispositivos informáticos, intentar violarlo devolverá un error al sistema operativo mientras que algunas grabadoras bloquean físicamente el botón de grabación cuando hay un casete protegido contra escritura.

 Protección por software

El sistema operativo puede proteger un archivo contra escritura para un usuario con pocos privilegios, generalmente protege los archivos del sistema y los de las carpetas del administrador y los demás usuarios. También protege a aquellos archivos que están ejecutándose y los que contienen en ellos unas líneas que le indican al sistema operativo su protección. Esto es muy importante en el tema de seguridad informática, ya que un usuario tiene permiso de leer ese archivo, pero no modificarlo o eliminarlo, esto hace que la información sea accesible y segura al mismo tiempo.

 Protección por digitalización

Un grabador de discos, puede proteger contra escritura digitalmente a la unidad para que no pueda ser regrabada nunca más, esto hace que solo los archivos se puedan leer pero no podrán regrabar el disco, este método es frecuentemente utilizado por empresas discográficas y de desarrollo de software.

 Métodos para poder escribir sobre archivos protegidos

 Sudo

El Sudo es un comando que se utiliza en sistemas unix que permite ejecutar desde un usuario con privilegios bajos, una línea con privilegios altos.

Ejemplo de ejecución del kwrite sobre un archivo protegido utilizando Sudo:

 $sudo kwrite /root/archivo.txt

Luego nos pedirá la contraseña del usuario "root", una vez ingresada, podremos ver y editar el archivo como si estaríamos autentificados como root.

 Desbloqueadores

Existe una clase de software que puede utilizar algoritmos sobre una aplicación bloqueada para permitir su modificación.

 Véase también

Disquete
Eliminar (informática)
Formato
Partición

 Enlaces externos

Herramienta muy útil para pasar por alto algunas protecciones contra escritura

Se puede desbloquear fácilmente en un SD card.
