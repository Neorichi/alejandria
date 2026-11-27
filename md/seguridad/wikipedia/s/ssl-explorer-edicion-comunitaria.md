---
type: Artículo de enciclopedia
title: "SSL-Explorer: Edición comunitaria"
description: "SSL-Explorer: Edición Comunitaria fue un producto VPN SSL de código abierto desarrollado por 3SP Ltd, una empresa adquirida por Barracuda Networks."
resource: https://es.wikipedia.org/wiki/SSL-Explorer:_Edición_comunitaria
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SSL-Explorer:_Edición_comunitaria"}
license: CC BY-SA 4.0
id: "eswiki-SSL-Explorer:_Edición_comunitaria"
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SSL-Explorer: Edición comunitaria

- **Nombre:** SSL-Explorer:Community Edition
- **Captura:** autor=
- **Desarrollador:** 3SP Ltd
- **Licencia:** GNU General Public License
- **Lanzamiento:** 18 de marzo de 2088
- **Sistema operativo:** Microsoft Windows, Linux, Mac OS X

**SSL-Explorer**: Edición Comunitaria fue un producto VPN SSL de código abierto desarrollado por 3SP Ltd, una empresa adquirida por Barracuda Networks. Tiene Licencia de GNU GPL, y está dirigido principalmente a empresas más pequeñas que necesitan acceso remoto a recursos de red internos.

El producto está diseñado para instalarse en un servidor independiente. Permite que un usuario se conecte de forma remota a recursos corporativos internos, como sitios web de intranet, recursos compartidos de archivos de red, aplicaciones de "cliente pesado" y otros datos a través de un navegador web normal. Brinda a los usuarios finales acceso a aplicaciones que usarían todos los días en el trabajo a través de un simple navegador web, sin la necesidad de instalar un software de cliente VPN dedicado.

 Historia, versiones y discontinuidad
El producto se lanzó por primera vez en el sitio web SourceForge.net en agosto de 2004 y desde entonces ha tenido más de 275.000 descargas de la distribución principal del producto hasta diciembre de 2007. Todas las versiones del producto principal de Edición Comunitaria se licenciaron bajo la GPL, mientras que el producto comercial de Edición de Empresa, que se construyó sobre la Edición Comunitaria pero con funcionalidad adicional, fue licenciado por separado bajo una licencia comercial. Se ha creado una bifurcación de la última versión de GPL llamada Adito, que luego se renombró como OpenVPN ALS.

Alrededor de marzo de 2008, 3SP Ltd anunció que interrumpió el desarrollo de la Edición Comunitaria.

Se sabía que SSL-Explorer se instalaba y funcionaba en los siguientes sistemas operativos:

 Windows de Microsoft 2000, XP, XP x64, 2003, Vista, y Windows 7
 Varias distribuciones de Linux que incluyen Red Hat Enterprise Linux, Fedora, CentOS, Slackware, SUSE Linux, Debian, Gentoo, Conary basó distribuciones
 Mac OS X v10.4 o posteriores.
 Sol Microsystems Solaris 8 y 9 (en SPARC y x86)

Al igual que con cualquier producto con licencia anteriormente bajo la GPL, el código fuente todavía está disponible a través de SourceForge.net. Sin embargo, las actualizaciones futuras del código fuente o los binarios preconstruidos no estarán disponibles por parte de 3SP Ltd.

Desde el 18 de noviembre de 2008, 3SP Ltd. es ahora parte de Barracuda Networks. La tecnología detrás de SSL-Explorer ahora está incorporada en Barracuda SSL VPN.

 Cómo Trabaja
SSL-Explorer es una aplicación escrita en Java y contiene su propia base de datos y servidor web que se utiliza para servir páginas web seguras para acceder a los recursos de la red back-end. Mientras el producto se instala idealmente en un servidor independiente, puede instalarse como un servicio y ejecutarse en segundo plano para otros procesos si se desea.

El producto actúa como un proxy basado en la web que media las solicitudes de recursos de usuarios externos al mismo tiempo que proporciona un medio para autenticar las identidades de estos usuarios mediante la consulta de varias bases de datos de usuarios, incluido Active Directory de Microsoft. Los derechos de acceso se cumplen por el principio de control de acceso basado en roles y otras medidas de control de acceso secundario, como los permisos del sistema de archivos NTFS, también pueden afectar los recursos a los que puede acceder un usuario.

Algunos recursos (por ejemplo, el acceso a escritorio remoto) requieren el uso de reenvío de puertos para funcionar correctamente. Con este fin, el navegador del cliente descarga y ejecuta un subprograma Java applet conocido como "Agente de explorador SSL". El subprograma intercepta las solicitudes TCP / IP en ciertos puertos configurables y las reenvía al servidor SSL-Explorer, que a su vez las enruta al punto final apropiado en la red.

Utilizando una combinación de varias técnicas como el proxy web y el reenvío de puertos, la mayoría de las aplicaciones corporativas pueden seguir funcionando sin obstáculos con sus datos canalizados de forma transparente entre el punto final y el cliente (a través de SSL-Explorer) utilizando el protocolo HTTPS.

Los recursos de red que pueden externalizar SSL-Explorer incluyen los siguientes:

 Sitios web de intranet
 Aplicaciones enriquecidas basadas en web como Microsoft Outlook Web Access.
 Acceso a escritorios de puestos de trabajo
 Recursos de archivo publicados en montajes de archivos FTP / SFTP / SMB
 Otros recursos de la empresa accesibles por TCP / IP, p. Ej. bases de datos y otras aplicaciones personalizadas

El servidor VPN real en sí puede colocarse dentro de la DMZ o dentro de la propia red de confianza con conexiones entrantes en el puerto 443 reenviadas directamente a SSL-Explorer mediante reglas de firewall. Una de las principales ventajas asociadas con los productos SSL VPN radica en el hecho de que, cuando se configura correctamente, debería ser técnicamente posible cerrar todos los demás puertos del firewall, además del puerto HTTPS / SSL 443.

Aunque a menudo se agrupan como soluciones similares, SSL-Explorer es conceptualmente diferente de OpenVPN en que proporciona acceso controlado y autenticado a servicios y aplicaciones dentro de una red en lugar de acceso total e indiscutible a la red.

 Quién es pretendido para?
Mientras que los productos SSL-Explorer y SSL VPN en su conjunto son beneficiosos para muchas personas, hay varios grupos distintos que se benefician enormemente de su uso:

 **Guerreros de carretera** – Usuarios que pasan mucho tiempo "viajando" y que pueden volver a conectarse a la empresa de forma ad hoc desde varios equipos diferentes.
 **Personal de soporte técnico** – En muchas empresas, el soporte técnico a menudo se encuentra fuera del sitio en otra sucursal. Al usar una VPN SSL, el soporte se puede extender a ubicaciones remotas.
 **Estudiantes universitario** – Al conectarse a menudo desde varias ubicaciones en varios campus, una solución SSL VPN (especialmente una sin cliente / basada en navegador) es útil para proporcionar acceso ad hoc al correo web y otras aplicaciones básicas.
 **Teletrabajadores** – Por su naturaleza, estos trabajadores trabajan casi exclusivamente desde sus oficinas en casa y requieren instalaciones de trabajo remotas dedicadas.
 **Trabajadores de proyectos colaborativos** – Al extender el acceso remoto a través de fronteras geográficas, las limitaciones de distancia y zonas horarias se vuelven menos restrictivas cuando se trabaja en proyectos colaborativos.

 Medidas de seguridad
La Edición Comunitaria de SSL-Explorer proporcionó una serie de funciones de seguridad. Las características como el soporte de contraseña única y la autenticación de token de hardware se ofrecen a través de la implementación comercial, Barracuda SSL VPN.

 Gestión de derechos granular basada en políticas.
 Usuarios autenticados a través de múltiples bases de datos de usuarios, incluida la base de datos incorporada y Active Directory.
 Código fuente revisable por pares disponible bajo licencia GPL.
 Múltiples mecanismos de autenticación, por ejemplo, cuestiones de seguridad personalizadas.
 Protección contra ataques de inyección SQL.
 Los riesgos de explotación de desbordamiento de búfer se mitigan mediante el uso del código fuente de Java.
 Admite el acceso a través de proxy HTTP o SOCKS.
 Tunelización local y remota a través de SSL.
 Tiempos de espera de inactividad de la sesión.
 Enmascaramiento de URL de aplicaciones web.

 Testaje de rendimiento
En febrero de 2007, 3SP Ltd llevó a cabo una evaluación comparativa del rendimiento de la solución SSL-Explorer utilizando una plataforma de banco de pruebas de tres sistemas que utilizan diferentes especificaciones de hardware. La evaluación comparativa se realizó con el supuesto de que una tasa de rendimiento de datos mínima de 256 kbit / s sería un valor realista para colocar en un túnel VPN receptivo para su uso como acceso a escritorio remoto. El BEA jRockit JRE se utilizó en todas las pruebas en sistemas Microsoft Windows y Linux.

 Un PC de nivel de entrada basada en un Athlon de 1.8 GHz con 768 MB de RAM fue capaz de soportar 144 túneles simultáneos a 256 kbit / s (rendimiento general de 36 Mbit / s en Windows, 46 Mbit / s en Linux)
 Un PC de especificaciones medias basada en un Pentium 4 de 2,8 GHz con 1 GB de RAM sostenía 192 túneles simultáneos (rendimiento general de 49 Mbit / s en Windows, 61 Mbit / s en Linux)
 Un PC de alta especificación que usa un Core 2 Duo 6600 con 4 GB de RAM sostenía 528 túneles (rendimiento general de 135 Mbit / s en Windows, 168 Mbit / s en Linux)

Se sabe que SSL-Explorer funciona correctamente con la tarjeta aceleradora SSL nCipher nFast LN1200.

 Las tecnologías utilizaron por SSL-Explorer
SSL-Explorer se creó utilizando una serie de marcos y componentes de software de código abierto. Los proyectos más destacados se resumen aquí:

 **rPath Linux** – Proporciona una plataforma de dispositivo para el dispositivo virtualizado SSL-Explorer.
 **Puntales de apache** – Marco MVC para el desarrollo de aplicaciones web.
 **Jetty 5.0** – Contenedor de servlets y servidor web basado en Java de alto rendimiento.
 **HSQLDB** – Implementación de base de datos Java liviana utilizada para el almacenamiento de datos de configuración y base de datos de usuario interna (cuando se usa).
 **AJAXTags** – JavaScript y XML asincrónicos para una interfaz web receptiva.
 **Commons VFS** – Se utiliza para proporcionar implementación de sistema de archivos virtual.
 **Log4j** – Proporciona el componente de registro de SSL-Explorer.
 **Roma** – Lector de feeds RSS.
 **JCIFS** – proporciona compatibilidad con el protocolo SMB para la compatibilidad de redes de Windows.
 **BEA Sistemas** **jRockit** – entorno de ejecución de Java optimizado para el rendimiento que se utiliza para proporcionar instalaciones de SSL-Explorer de alto rendimiento.

 Vulnerabilidades de seguridad
En junio de 2007, Secunia publicó un aviso indicando que las versiones de SSL-Explorer anteriores a la 0.2.13 son vulnerables a ataques de scripts entre sitios y ataques de inyección de encabezados HTTP. 3SP Ltd solucionó esta vulnerabilidad en versiones posteriores del producto y recomendó a los usuarios que actualizaran sus servidores.

Actualmente existe un aviso de advertencia de US-Cert para una falla de seguridad potencial no resuelta que afecta a toda una clase de productos VPN SSL sin cliente con reescritura de URL, incluidas todas las versiones de SSL-Explorer y sus derivados, y muchas otras utilidades similares.

 Véase también
 Red privada virtual
 OpenVPN

 Referencias

 Enlaces externos

 OpenVPN ALS: Continuación de código abierto de SSL-Explorer Edición Comunitaria.
 OpenVPN ALS wiki: Documentación para el OpenVPN ALS proyecto.
 SSL-Explorer: Edición Comunitaria Sourceforge.net página de proyecto.
 3SP: SSL-foro de Explorer (actualmente leído-único).
 Barracuda SSL VPN: La implementación comercial basada en SSL-tecnología de Explorer.
 SSL EXPLORER – OPENVPN ALS –ADITO VPN: Alonso Ballesteros.
