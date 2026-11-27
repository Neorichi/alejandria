---
type: Artículo de enciclopedia
title: Seguridad de redes
description: La seguridad de redes consiste en las políticas y prácticas adoptadas para prevenir y supervisar el acceso no autorizado, el uso indebido, la modificación o la denegación de una red informática y sus recursos accesibles.
resource: https://es.wikipedia.org/wiki/Seguridad_de_redes
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_de_redes"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_de_redes
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad de redes

La **seguridad de redes** consiste en las políticas y prácticas adoptadas para prevenir y supervisar el acceso no autorizado, el uso indebido, la modificación o la denegación de una red informática y sus recursos accesibles. La seguridad de redes involucra la autorización del acceso a datos en la red, que es controlada por el administrador de red. Los usuarios eligen o se les asigna una identificación y contraseña u otra información de autenticación que les permite acceder a información y programas dentro de sus autorizaciones. La seguridad de red cubre una variedad de redes de computadoras, tanto públicas como privadas, que se usan en trabajos cotidianos; realizar transacciones y comunicaciones entre empresas, agencias gubernamentales e individuos. Las redes pueden ser privadas, como dentro de una empresa, y otras que pueden estar abiertas al público. La seguridad de la redes está presente en organizaciones, empresas y otros tipos de instituciones. Hace como su nombre indica: protege la red, además de proteger y supervisar las operaciones que se realizan. La forma más común y simple de proteger un recurso de red es asignándole un nombre único y la contraseña correspondiente.

Principios Fundamentales
La seguridad de redes se basa en tres principios principales, conocidos como la triada CIA:

1. Confidencialidad: Garantizar que la información solo sea accesible para las personas autorizadas.
2. Integridad: Asegurar que los datos no sean alterados de manera no autorizada durante la transmisión o almacenamiento.
3. Disponibilidad: Garantizar que los recursos y servicios de la red estén disponibles para los usuarios autorizados cuando los necesiten.

Conceptos de seguridad de redes

La seguridad de redes empieza con la autenticación, usualmente con un nombre de usuario y una contraseña. Ya que esto requiere solamente autenticar un nombre de usuario, por ejemplo, con la contraseña, se utiliza el término autenticación de un factor. Con un doble factor de autenticación se utiliza algo que el usuario "tiene", por ejemplo, un token de seguridad, una tarjeta de crédito o un teléfono celular; y con un factor triple de autenticación se usa algo que el usuario "es", por ejemplo huella dactilar o reconocimiento de iris.

Una vez autenticado, un cortafuegos aplica políticas de acceso, por ejemplo, asignar los servicios a los cuales pueden acceder los usuarios de la red. Aunque esta medida es efectiva para prevenir acceso no autorizado, este componente puede fallar al revisar contenido que puede ser dañino, un ejemplo sería un gusano informático o un troyano que esté siendo transmitido en la red. Un antivirus o un Sistema de prevención de intrusos (SPI) ayuda a detectar e inhibir la acción de un malware. Un sistema de prevención de intrusos, basado en anomalías, también puede monitorear la red, por ejemplo usando wireshark se puede analizar tráfico en la red con propósitos de auditoría o para un análisis de alto nivel.

La comunicación entre dos hosts en una red puede ser encriptada para asegurar la privacidad.

Los *honeypots*, esencialmente recursos accesibles en la red que actúan como señuelos, pueden ser desplegados en una red para vigilar y como herramienta de vigilancia y alerta temprana, ya que los *honeypots* normalmente no se utilizan para fines legítimos. Las técnicas utilizadas por los atacantes que intentan comprometer estos recursos señuelo se estudian durante y después de un ataque, para observar las nuevas técnicas de intrusión. Dicho análisis puede ser usado para futuros reforzamientos en la seguridad de la red que está siendo protegida por ese *honeypot*. Un *honeypot* también puede dirigir la atención de un atacante lejos de servidores legítimos. Un honeypot alienta a los atacantes a gastar su tiempo y energía en el servidor señuelo mientras distrae su atención de los datos del servidor real. Similar a un *honeypot*, una *honeynet* es una red configurada con vulnerabilidad intencional. Su propósito es, también, el de invitar a los atacantes para que sus técnicas de ataque puedan ser analizadas y ese conocimiento pueda ser usado para aumentar la seguridad de la red. Una *honeynet* normalmente contiene uno o más *honeypots*.

La seguridad de una arquitectura de red, hoy en día debe diseñarse bajo un concepto de **capas** dándole profundidad a la defensa y, tal cual lo propone Alejandro Corletti Estrada en su libro **Seguridad en Redes** también deben considerarse diferentes **planos** o alturas de la red.  Estos conceptos se pueden ver reflejados en la siguiente imagen.

Las investigaciones anteriores sobre seguridad de redes se centraban principalmente en el uso de herramientas para proteger las transacciones y el flujo de información, y en qué tan bien los usuarios conocían y utilizaban estas herramientas. Sin embargo, más recientemente, el debate se ha ampliado para considerar la seguridad de la información en el contexto más amplio de la economía digital y la sociedad. Esto indica que no se trata sólo de usuarios y herramientas individuales; también se trata de la cultura más amplia de seguridad de la información en nuestro mundo digital.

Administración de seguridad

La administración de seguridad para redes varía según las diversas situaciones. Una casa u oficina pequeña puede requerir solamente seguridad básica, mientras que las grandes empresas pueden requerir un software y hardware de alto mantenimiento y avanzado para evitar ataques maliciosos de piratería y *spam*.

Tipos de ataques
Las redes están sujetas a ataques de fuentes maliciosas. Los ataques pueden ser de dos categorías: "pasivos" cuando un intruso intercepta datos que viajan a través de la red, y "activos" cuando un intruso inicia comandos para interrumpir el funcionamiento normal de la red o para realizar reconocimiento y "espionaje" para encontrar y obtener acceso a activos disponibles a través de la red.

Tipos de ataque:
 Pasivos
 Red
 Escucha telefónica
 Escáner de puertos
 Escaneo libre
 Activos
 Ataque de denegación de servicio
 DNS spoofing
 Ataque Man-in-the-middle
 ARP Spoofing
 Ataque por salteo de VLAN
 Ataque smurf
 Desbordamiento de búfer
 Desbordamiento de montículo
 Ataque de formato String
 Inyección SQL
 Phishing
 Cross-site scripting
 CSRF
 Ataque informático

Amenazas Comunes

La seguridad de redes busca mitigar una variedad de amenazas, incluidas:

Ataques de malware: Virus, ransomware, spyware y otros tipos de software malicioso.
Ataques de phishing: Intentos de engañar a los usuarios para que revelen información confidencial.
Ataques de denegación de servicio (DoS y DDoS): Saturar una red o servidor para interrumpir su operación.
Interceptación de datos: Espionaje o captura de información durante la transmisión (ataques "man-in-the-middle").
Ingeniería social: Manipulación psicológica para obtener acceso no autorizado.

Tecnologías de Seguridad
La seguridad de redes utiliza diversas tecnologías y herramientas para proteger los sistemas:

1. Firewalls: Controlan el tráfico entrante y saliente basado en reglas predefinidas.

2. Sistemas de detección y prevención de intrusos (IDS/IPS): Monitorean el tráfico de red para detectar y prevenir actividades maliciosas.

3. VPN (Redes Privadas Virtuales): Protegen las comunicaciones en redes
públicas mediante el cifrado de datos.

4. Cifrado: Utilización de algoritmos para proteger los datos en tránsito y en reposo.

5. Autenticación multifactor (MFA): Combina múltiples métodos de verificación para garantizar la identidad de los usuarios.

Buenas Prácticas
Para implementar una seguridad de redes efectiva, se recomiendan las siguientes prácticas:

Mantener el software y hardware actualizados con los últimos parches de seguridad.
Implementar políticas claras de control de acceso y permisos de usuario.
Realizar auditorías y pruebas regulares de vulnerabilidades.
Capacitar a los empleados en ciberseguridad y concienciación sobre amenazas.
Usar segmentación de red para limitar el impacto de posibles incidentes.

Véase también

Seguridad de computo en la nube
Crimeware
Software de prevención de pérdida de datos
Greynet
Seguridad basada en identidad
Prevención de filtrado de información
Metasploit
Seguridad en telefonía móvil
Netsentron
Ataque de predicción de secuencia TCP

Referencias

Otras lecturas
*Libro Seguridad en Redes*, isbn=978-84-617-5291-1, Corletti Estrada Alejandro,   2016
*Case Study: Network Clarity* , SC Magazine 2014
Cisco. (2011). What is network security?. Retrieved from cisco.com
pcmag.com
Security of the Internet (*The Froehlich/Kent Encyclopedia of Telecommunications vol. 15*. Marcel Dekker, New York, 1997, pp. 231–255.)
*Introduction to Network Security* , Matt Curtin.
 *Security Monitoring with Cisco Security MARS*, Gary Halleen/Greg Kellogg, Cisco Press, Jul. 6, 2007.
 *Self-Defending Networks: The Next Generation of Network Security*, Duane DeCapite, Cisco Press, Sep. 8, 2006.
 *Security Threat Mitigation and Response: Understanding CS-MARS*, Dale Tesch/Greg Abelar, Cisco Press, Sep. 26, 2006.
 *Securing Your Business with Cisco ASA and PIX Firewalls*, Greg Abelar, Cisco Press, May 27, 2005.
 *Deploying Zone-Based Firewalls*, Ivan Pepelnjak, Cisco Press, Oct. 5, 2006.
*Network Security: PRIVATE Communication in a PUBLIC World*, Charlie Kaufman | Radia Perlman | Mike Speciner, Prentice-Hall, 2002.  ISBN .
*Network Infrastructure Security*, Angus Wong and Alan Yeung, Springer, 2009.

 Enlaces externos

Cyber Security Network
Definition of Network Security
Network Security - Comprehensive Security from Layer 2 to Layer 8
Cisco IT Case Studies about Security and VPN
¿Qué es la seguridad en la red?
Definition of Network Security
OpenLearn - Network Security
