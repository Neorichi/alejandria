---
type: Artículo de enciclopedia
title: Ataque por puerta trasera a XZ Utils
description: "El 29 de marzo de 2024, el desarrollador de software Andres Freund informó que había encontrado una puerta trasera introducida maliciosamente en la utilidad para Linux xz, contenida en la biblioteca liblzma en sus …"
resource: https://es.wikipedia.org/wiki/Ataque_por_puerta_trasera_a_XZ_Utils
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_por_puerta_trasera_a_XZ_Utils"}
license: CC BY-SA 4.0
id: eswiki-Ataque_por_puerta_trasera_a_XZ_Utils
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque por puerta trasera a XZ Utils

- **Género:** Puerta trasera
- **Cve:** CVE-2024-3094
- **Descubridor:** Andres Freund
- **Descubrimiento:** 29 de marzo de 2024
- **Parchado:** 29 de marzo de 2024
- **Software afectado:** xz, biblioteca liblzma

El 29 de marzo de 2024, el desarrollador de *software* Andres Freund informó que había encontrado una puerta trasera introducida maliciosamente en la utilidad para Linux xz, contenida en la biblioteca liblzma en sus versiones 5.6.0 y 5.6.1, publicadas en febrero de 2024.

Pese a que xz normalmente está presente en la mayor parte de las distribuciones Linux, al momento en que se había descubierto la puerta trasera, esta todavía no se había desplegado de manera amplia a los entornos de producción, pero sí se transmitió a las versiones en desarrollo de algunas de las distribuciones más importantes.

La puerta trasera brinda privilegios de ejecución de código remota a un atacante que posea una clave privada Ed448 concreta en los sistemas Linux afectados. Este problema ha recibido el número CVE-2024-3094 en la base de información *Common Vulnerabilities and Exposures* y se le ha otorgado una puntuación CVSS de 10.0, la más alta posible.

Antecedentes
Andres Freund, empleado de Microsoft y desarrollador de PostgreSQL, informó de la puerta trasera tras investigar una regresión de desempeño que se producía en Debian Sid. Freund se percató de que las conexiones efectuadas con SSH estaban generando una cantidad inesperadamente alta de ciclos de CPU y provocaban errores en Valgrind, una herramienta de depuración de memoria operativa. Freund informó de su descubrimiento a la lista de distribución de correo sobre seguridad del proyecto Openwall, lo que llamó la atención de varios proveedores de *software*. El o la atacante se esforzó en ofuscar el código, dado que la puerta trasera se compone de varios componentes que actúan en conjunto.

Una vez que la versión vulnerada se ha incorporado al sistema operativo, altera el comportamiento del servicio del servidor SSH de OpenSSH por medio de la biblioteca systemd, que permite a un atacante obtener privilegios administrativos. De acuerdo al análisis de Red Hat, la puerta trasera puede «habilitar a un actor malicioso para superar la autenticación por sshd y obtener acceso no autorizado a la totalidad del sistema de forma remota».

Una investigación posterior encontró que la campaña para insertar la puerta trasera en el proyecto XZ Utils fue una culminación de unos tres años de esfuerzo por parte de un usuario o usuaria con el nombre *Jia Tan* y el sobrenombre *JiaT75* para que se le diera acceso a un puesto de confianza en el proyecto. Luego de un período de presión hacia el fundador y responsable principal del proyecto para que cediera control del mismo, mediante aparentes usuarios títere, *Jia Tan* obtuvo el puesto de comantenedor de XZ Utils y, así, pudo autorizar la versión 5.6.0, que introdujo la puerta trasera, y la versión 5.6.1, que corrigió un comportamiento anómalo que podía manifestarse durante las puestas a prueba del sistema operativo. Algunas de las identidades títere son *Jigar Kumar*, *krygorin4545* y *misoeater91*. Se sospecha que los nombres *Jia Tan* y *Hans Jansen*, supuesto autor de código (para las versiones 5.6.0 y 5.6.1), son seudónimos escogidos por quien o quienes formaron parte de la campaña. Ninguna de estas personas han manifestado presencia pública alguna en la escena del desarrollo de *software* fuera de los años en que esta campaña tuvo lugar. La puerta trasera fue notoria por su nivel de sofisticación y por el hecho de que el o la perpetradora llevó a cabo un grado alto de seguridad operacional durante un período prolongado mientras trabajaba en alcanzar una posición de confianza. El investigador Dave Aitel ha sugerido que ello se ajusta al modelo atribuible al APT29, un agente de amenaza persistente avanzada del que se cree que trabajaba a nombre del Servicio de Inteligencia Exterior ruso. Thomas Claburn, periodista del *Register* que se especializa en las TI, sugirió que pudo haberse tratado de cualquier agente de Estado, o bien, de un agente independiente con una gran cantidad de recursos.

Mecanismo
El código malicioso se ha encontrado en las versiones 5.6.0 y 5.6.1 del paquete de *software* XZ Utils. El *exploit* permanece inactivo a menos que se use un parche de terceros concreto para el servidor SSH. Cuando se dan las circunstancias correctas, esta interferencia puede hacer posible que un agente malicioso venza la autenticación de sshd y obtenga acceso al sistema remotamente. La vulnerabilidad se distribuyó a través de dos archivos comprimidos de prueba que contienen el código en forma binaria. Estos archivos están disponibles en el repositorio Git, pero permanecen inactivos salvo que se extraigan e inyecten en el programa. El código hace uso del mecanismo IFUNC de glibc para sustituir una función existente en OpenSSH llamada  con una versión maliciosa. OpenSSH normalmente no carga liblzma, pero un parche de terceros que comúnmente usaban varias distribuciones Linux hace que integre libsystemd, el cual a su vez carga lzma. Una versión modificada de  se incluyó en el archivo TAR de la versión en GitHub, que extrae una secuencia de órdenes para inyectar la puerta trasera en . Este archivo m4 modificado no figuró nunca en el repositorio Git; solo estaba disponible en los TAR que el corresponsable emitió de forma separada al repositorio. Esta secuencia parece realizar la inyección solamente si el proyecto se está compilando en un sistema Linux de arquitectura x86-64 con glibc y GCC a través de dpkg o rpm.

Respuestas
Planes correctivos
La agencia federal estadounidense responsable de la ciberseguridad, la CISA, ha emitido una alerta de seguridad que recomienda que los dispositivos afectados retornen a una versión anterior del programa. Diversos proveedores de *software* para Linux, entre ellos Red Hat, SUSE y Debian, han seguido la recomendación de la CISA y han revertido las actualizaciones de los paquetes afectados a versiones previas. GitHub desactivó las replicaciones del repositorio de xz temporalmente.

Canonical pospuso una semana el lanzamiento en beta de  y sus «sabores» oficiales y eligió emprender una recompilación binaria completa de todos los paquetes de la distribución. Pese a que la versión estable de Ubuntu nunca resultó afectada, las versiones originarias sí. Esta medida precautoria se tomó porque Canonical no pudo garantizar que no hubiese paquetes afectados para la fecha límite original para compilar el lanzamiento final.

Debian y Ubuntu han comenzado a eliminar la funcionalidad que integraba libsystemd en el servidor OpenSSH para reducir la superficie de ataque del servicio.

Respuesta generalizada

El informático Alex Stamos opinó que «podría haber sido la puerta trasera más esparcida y eficaz jamás plantada en algún producto de *software*», y destacó que, de no haberse detectado, habría «dado a sus creadores una llave maestra para cualquiera de los cientos de millones de computadores del mundo que ejecutan SSH». Además, el incidente inició un debate sobre la viabilidad de que porciones cimentales de la ciberinfraestructura dependan de personas voluntarias no remuneradas.

Referencias

Enlaces externos

 Informe de Andres Freund a la lista de correo oss-security de Openwall
