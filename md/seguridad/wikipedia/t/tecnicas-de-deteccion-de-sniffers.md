---
type: Artículo de enciclopedia
title: Técnicas de detección de sniffers
description: "Las técnicas de detección de sniffers se basan en la búsqueda del problema que varía según se tenga acceso local al ordenador o haya que descubrirlo de algún ordenador remoto, esta última es la variante más usual …"
resource: https://es.wikipedia.org/wiki/Técnicas_de_detección_de_sniffers
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Técnicas_de_detección_de_sniffers"}
license: CC BY-SA 4.0
id: eswiki-Técnicas_de_detección_de_sniffers
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Técnicas de detección de sniffers

Las *** técnicas de detección de sniffers*** se basan en la búsqueda del problema que varía según se tenga **acceso local al ordenador** o haya que descubrirlo de algún **ordenador remoto**, esta última es la variante más usual aunque la más compleja. El objetivo de la mayoría de pruebas es conseguir que la máquina que tiene la tarjeta de red en modo *promiscuo* se traicione a sí misma, revelando que ha tenido acceso a información que no iba dirigida a ella y que, por tanto, tiene un sniffer. Sin embargo es un objetivo que puede llegar a ser imposible por su complejidad.
Si la búsqueda es una consulta directa sobre un ordenador, lo que tendremos que hacer es mirar el estado de las diferentes interfaces de redes que tengamos en dicho equipo, la forma más habitual es utilizar el comando ipconfig.

En el caso de que no podamos acceder y consultar el estado de las interfaces de red, entonces utilizaríamos algún defecto en la implementación concreta del protocolo TCP/IP por algún programa/comando, las técnicas de búsqueda de sniffer en este caso se dividen en dos: las dependientes del sistema operativo y las que no lo son. La ventaja de las técnicas que dependen del sistema operativo es su excelente rendimiento cuando explora máquinas que tienen el mismo sistema operativo del que la técnica obtiene partido, la principal desventaja es el gran número de *falsos negativos* que ocasiona debido a que en muchos casos las implementaciones de la pila TCP/IP varían entre versiones del mismo sistema operativo. Como ejemplos destacar el filtrado de paquetes en kernels de Linux.

En condiciones normales, los paquetes son aceptados o rechazados a nivel hardware por la tarjeta de red según la MAC address de destino que aparezca en el frame Ethernet. Sólo si esa MAC address es la de la propia máquina o la de broadcast, el paquete es aceptado (copiado) y procesado (se pasa al kernel); en caso contrario, se rechaza (se ignora). Para cada PC del segmento de red que se desee analizar se crea un paquete con una MAC address de destino que no exista en el segmento, cualquier máquina con la tarjeta de red en modo no promiscuo rechazará directamente un paquete que tiene como destino una que no es la suya ni la de broadcast, y no procesará el paquete, mientras que una tarjeta en modo promiscuo pasará el paquete al kernel, este analizará el paquete exclusivamente según los datos del paquete IP que encapsule, el paquete es un ping completamente normal que es contestado por la máquina que tiene el sniffer revelando así su estado.

Filtrado de paquetes broadcast en algunos drivers de Windows:
La idea es la misma que en el filtrado de paquetes en kernels de Linux, la característica a considerar en este caso es cómo el driver del sistema operativo decide cuándo un paquete va dirigido a la dirección broadcast **ff:ff:ff:ff:ff:ff**, cuando la tarjeta de red está en modo no promiscuo, se verifican los seis octetos mientras que en estado promiscuo sólo se verifica el primero de ellos, este hecho facilita mucho la detección de sniffers. Se crea un paquete dirigido a la MAC address **ff:00:00:00:00:00**, cualquier tarjeta en modo no promiscuo lo va a rechazar automáticamente, mientras que una tarjeta en modo promiscuo con un sistema operativo Windows que use el driver afectado confundirá ese paquete con uno dirigido a broadcast, y lo procesará.
Las técnicas no dependientes del sistema operativo son menos fiables y menos concluyentes, suelen basarse en suposiciones del comportamiento de determinados sniffers, convirtiendo estas técnicas inútiles en determinados ambientes. A destacar como ventaja no suelen provocar falsos negativos.

 Ejemplos
 El Test DNS
En este método, la herramienta de detección en sí misma está en modo promiscuo. Creamos numerosas conexiones TCP/IP falsas en nuestro segmento de red, esperando un sniffer pobremente escrito para atrapar esas conexiones y resolver la dirección IP de los inexistentes host. Algunos sniffers realizan búsquedas inversas DNS en los paquetes que capturan. Cuando se realiza una búsqueda inversa DNS, una utilidad de detección de sniffers *huele* la petición de las operaciones de búsqueda para ver si el objetivo es aquel que realiza la petición del host inexistente.

 El Test del Ping
Este método confía en un problema en el núcleo de la máquina receptora. Podemos construir una petición tipo "ICMP echo" con la dirección IP de la máquina sospechosa de hospedar un sniffer, pero con una dirección MAC deliberadamente errónea. Enviamos un paquete "ICMP echo" al objetivo con la dirección IP correcta, pero con una dirección de hardware de destino distinta. La mayoría de los sistemas desatenderán este paquete ya que su dirección MAC es incorrecta. Pero en algunos sistemas Linux, NetBSD y NT, puesto que el NIC está en modo promiscuo, el sniffer analizará este paquete de la red como paquete legítimo y responderá por consiguiente. Si el blanco en cuestión responde a nuestra petición, sabremos que está en **modo promiscuo**. Un atacante avanzado puede poner al día sus sniffers para filtrar tales paquetes para que parezca que el NIC no hubiera estado en modo promiscuo.

 El Test ICMP
Ping de Latencia. En este método, hacemos ping al blanco y anotamos el Round Trip Time (RTT, retardo de ida y vuelta o tiempo de latencia) Creamos centenares de falsas conexiones TCP en nuestro segmento de red en un período muy corto. Esperamos que el sniffer esté procesando estos paquetes a razón de que el tiempo de latencia incremente. Entonces hacemos ping otra vez, y comparamos el RTT esta vez con el de la primera vez. Después de una serie de tests y medias, podemos concluir o no si un sniffer está realmente funcionando en el objetivo o no.

 El Test ARP
Podemos enviar una petición ARP a nuestro objetivo con toda la información rápida excepto con una dirección hardware de destino errónea. Una máquina que no esté en **modo promíscuo** nunca verá este paquete, puesto que no era destinado a ellos, por lo tanto no contestará. Si una máquina está en modo promiscuo, la petición ARP sería considerada y el núcleo la procesaría y contestaría. Por la máquina que contesta, sabremos que la máquina está en modo promiscuo.

 El Test Etherping
Enviamos un ping echo al host a testear con una IP de destino correcta y dirección MAC falseada. Si el host responde, es que su interfaz está en modo promiscuo, es decir, existe un sniffer a la escucha y activo.
