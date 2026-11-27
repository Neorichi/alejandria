---
type: Artículo de enciclopedia
title: MAC spoofing
description: "MAC spoofing es una técnica para enmascarar la dirección MAC de un dispositivo de red que está codificada en una tarjeta de red. En términos generales, la dirección MAC es la dirección que identifica a los controladores …"
resource: https://es.wikipedia.org/wiki/MAC_spoofing
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/MAC_spoofing"}
license: CC BY-SA 4.0
id: eswiki-MAC_spoofing
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# MAC spoofing

***MAC spoofing*** es una técnica para enmascarar la dirección MAC de un dispositivo de red que está codificada en una tarjeta de red. En términos generales, la dirección MAC es la dirección que identifica a los controladores de interfaces de red y se caracterizan por ser inequívocas o "estar grabadas" en el dispositivo, por lo que no se pueden cambiar. Sin embargo, existen herramientas que pueden hacer al sistema operativo creer que un controlador de interfaces de red (NIC) tiene la dirección MAC de la elección de otro usuario. El proceso de enmascaramiento de una dirección MAC se conoce como suplantación de dirección MAC (*MAC spoofing*). En esencia, esta técnica implica el cambio de identidad de una computadora por cualquier razón.

 Motivación
El cambio de la dirección MAC asignada puede permitir que se incumplan las listas de control de acceso en los servidores o routers, o bien ocultar un ordenador en una red o permitir que se haga pasar por otro dispositivo de red. La suplantación de una dirección MAC se hace con fines legítimos e ilegales por igual.

 Nuevo hardware existente para un proveedor de servicios de Internet
La mayor parte del tiempo, un ISP registra la dirección MAC del cliente para los servicios de servicio y facturación. Dado que las direcciones MAC son únicas y están incrustadas directamente en las tarjetas de red, cuando el cliente quiere conectar un nuevo dispositivo de red o cambiar uno existente, el ISP podría detectar diferentes direcciones MAC y no permitir el acceso a Internet a los nuevos dispositivos. Esto se puede evitar fácilmente mediante la suplantación de dirección MAC. El cliente solo tiene que suplantar la dirección MAC del nuevo dispositivo con la dirección MAC con la que fue registrado por el proveedor de Internet. En este caso, el cliente falsifica su dirección MAC para acceder a Internet desde múltiples dispositivos. Aunque esto parece un caso legítimo, la suplantación de dirección MAC en nuevos aparatos pueden considerarse ilegales si el acuerdo entre el proveedor y el usuario impide que este se conecta con más de un dispositivo a su servicio. Por otra parte, el cliente no es la única persona que puede suplantar su dirección MAC para acceder al proveedor. Los clientes pueden obtener acceso no autorizado a la ISP a través de la misma técnica. Esto permite a los *cibercriminales* acceder a los servicios no autorizados, y el pirata va a ser difícil de identificar porque el *cibercriminal* utiliza la identidad del cliente. Esta acción se considera un uso ilegítimo de la suplantación de dirección MAC e ilegal también. Sin embargo, es muy difícil realizar un seguimiento de los *cibercriminales* que utilizan *MAC spoofing*.

 Cumplimiento de los requisitos del *software*
Algunos programas de software solo se pueden instalar y ejecutar en sistemas con direcciones MAC predefinidas según lo indicado en el contrato de licencia de software para el usuario final, y los usuarios tienen que cumplir con este requisito para poder acceder al software. Si el usuario tiene que instalar un hardware diferente debido al mal funcionamiento del dispositivo original o si hay un problema con la tarjeta de red del usuario, el software no reconocerá el nuevo hardware. Sin embargo, este problema se puede resolver utilizando *MAC spoofing*. El usuario solo tiene que suplantar la nueva dirección MAC para imitar la dirección MAC con la que se registró el software. Esta actividad es muy difícil de definir como legítima o ilegítima. Cuestiones jurídicas podrían surgir si el usuario concede acceso al software en varios dispositivos simultáneamente. Al mismo tiempo, el usuario puede obtener acceso al software para que él o ella no se ha asegurado una licencia. Ponerse en contacto con el proveedor de software podría ser la ruta más segura para tomar, si hay un problema de hardware que impide el acceso al software. El software también puede realizar el filtrado de la dirección MAC por impedir que usuarios no autorizados tengan acceso a ciertas redes con acceso al software. En tales casos, la suplantación de una dirección MAC se puede considerar una actividad ilegal grave  con su consecuente sanción.

 Enmascaramiento de identidad
Si un usuario decide suplantar su dirección MAC con el fin de proteger su privacidad, esto se llama enmascaramiento de identidad. Un posible motivo para desear hacer esto sería porque en una conexión Wi-Fi la dirección MAC no está cifrada. Incluso con el método de cifrado seguro IEEE 802.11i-2004  no se impide que las redes Wi-Fi envíen las direcciones MAC. Por lo tanto, con el fin de evitar ser rastreado, el usuario puede optar por enmascarar la dirección MAC del dispositivo. Sin embargo, utilizan la misma técnica para maniobrar sobre de los permisos de la red sin revelar su identidad. Algunas redes usan el filtrado de direcciones MAC con el fin de evitar el acceso no deseado. Pueden utilizar la suplantación de dirección MAC para tener acceso a una red en particular y hacer algo dañino. Un cibercriminal que utiliza la suplantación de dirección MAC «pasa» la responsabilidad por cualquier actividad ilegal hacia otros usuarios. Como resultado de ello, el verdadero delincuente puede no ser detectado por la policía.

 Véase también
 MAC
 Dirección MAC
 Filtrado MAC

 Referencias
