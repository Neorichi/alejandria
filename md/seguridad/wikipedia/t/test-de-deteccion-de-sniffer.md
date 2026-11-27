---
type: Artículo de enciclopedia
title: Test de detección de sniffer
description: Por test de detección de sniffer se entienden diversas pruebas que permiten reconocer la presencia de un sniffer en la red.
resource: https://es.wikipedia.org/wiki/Test_de_detección_de_sniffer
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Test_de_detección_de_sniffer"}
license: CC BY-SA 4.0
id: eswiki-Test_de_detección_de_sniffer
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Test de detección de sniffer

Por **test de detección de *sniffer*** se entienden diversas pruebas que permiten reconocer la presencia de un *sniffer* en la red.

 El test DNS
En este método, la herramienta de detección en sí misma está en modo promiscuo. Creamos numerosas conexiones TCP falsas en nuestro segmento de red, esperando un *sniffer* pobremente escrito para atrapar estas conexiones y resolver la dirección IP de los inexistentes hosts.

Algunos *sniffers* realizan búsquedas inversas DNS en los paquetes que capturan. Cuando se realiza una búsqueda inversa DNS, una utilidad de detección de *sniffers* "huele" la petición de las operaciones de búsqueda para ver si el objetivo es aquel que realiza la petición del host inexistente.

 El test del Ping
Este método confía en un problema en el núcleo de la máquina receptora. Podemos construir una petición tipo "ICMP echo" con la dirección IP de la máquina sospechosa de hospedar un sniffer, pero con una dirección MAC deliberadamente errónea.

Enviamos un paquete "ICMP echo" al objetivo con la dirección IP correcta, pero con una dirección de *hardware* de destino distinta.

La mayoría de los sistemas desatenderán este paquete ya que su dirección MAC es incorrecta. Pero en algunos sistemas Linux, NetBSD y NT, puesto que el NIC está en modo promiscuo, el sniffer asirá este paquete de la red como paquete legítimo y responderá por consiguiente. Si el blanco en cuestión responde a nuestra petición, sabremos que está en modo promiscuo.

Un atacante avanzado puede poner al día sus sniffers para filtrar tales paquetes para que parezca que el NIC no hubiera estado en modo promiscuo.

 El Test ICMP. Ping de Latencia.
En este método, se hace ping al blanco y se registra el *round-trip delay time* (o RTT, retardo de ida y vuelta o tiempo de latencia).

Creamos centenares de falsas conexiones TCP en nuestro segmento de red en un período muy corto. Esperamos que el *sniffer* esté procesando estos paquetes a razón de que el tiempo de latencia se incremente.

Entonces hacemos ping otra vez, y comparamos el RTT esta vez con el de la primera vez.

Después de una serie de tests y medias, podemos concluir o no si un *sniffer* está realmente funcionando en el objetivo o no.

 El test ARP
Es posible enviar una petición ARP al host objetivo con toda la información rápida excepto con una dirección hardware de destino errónea.

Una máquina que no esté en modo promiscuo nunca verá este paquete, puesto que no era destinado a ellos, por lo tanto no contestará. En cambio, si una máquina está en modo promiscuo, la petición ARP sería considerada y el núcleo la procesaría y contestaría. Por la máquina que contesta, se sabe que está en modo promiscuo.

 El test Etherping
Se envía un "ping echo" al host a testear con una IP de destino correcta y dirección MAC falseada. Si el host responde, es que su interfaz está en modo promiscuo, es decir, existe un sniffer a la escucha y activo.

 IFCONFIG
En entornos Linux o UNIX la verificación de una interfaz en modo promiscuo se puede hacer usando ifconfig. Este programa configura la interfaz de red instalada en un determinado host y obtiene información de la configuración en el momento de ejecutar el programa.

 Véase también
 Sniffer
 Detección de sniffer

 Referencias
