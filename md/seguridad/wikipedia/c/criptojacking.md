---
type: Artículo de enciclopedia
title: Criptojacking
description: "El Criptojacking, también llamado Criptominado malicioso o Criptosecuestro, en inglés Cryptojacking (derivado de la combinación de los vocablos Cryptocurrency , criptomoneda, y Hijacking, secuestro), consiste en el …"
resource: https://es.wikipedia.org/wiki/Criptojacking
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptojacking"}
license: CC BY-SA 4.0
id: eswiki-Criptojacking
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptojacking

El **Criptojacking**, también llamado **Criptominado malicioso** o **Criptosecuestro**, en inglés *Cryptojacking* (derivado de la combinación de los vocablos *Cryptocurrency* , criptomoneda, y *Hijacking*, secuestro), consiste en el secuestro de un dispositivo electrónico sin el consentimiento o conocimiento del usuario, para aprovechar sus recursos en el minado de criptomonedas.

La criptomoneda más usada para minar en este tipo de ataques es Monero debido a sus características de privacidad y anonimato y por tanto las transacciones no se pueden trazar. Además, algoritmo Proof-of-Work de Monero (CryptoNight) se ha diseñado para hacer que las actividades de minería sean viables con una CPU estándar en vez de requerir grandes cantidades de recursos o incluso hardware especializado. También es habitual el criptosecuestro para minado de Bitcoin y Ethereum debido a su alto valor en el mercado.

El éxito de este tipo de ataque se debe a que es fácil de efectuar y automatizar, además de la dificultad de detectar su presencia en el dispositivo infectado.

Cualquier dispositivo puede ser objetivo de este tipo de secuestro. Por ejemplo supercomputadores,servidores, routers, ordenadores personales, consolas de juegos, tabletas, dispositivos móviles, dispositivos inteligentes y dispositivos IoT.
Tipos
Podemos clasificar los criptosecuestros en función de su modo de funcionamiento en:
**Criptosecuestro basado en navegador**.
**Criptosecuestro basado en routers**.
**Criptosecuestro basado en archivos**
**Criptosecuestro en la nube**

Criptosecuestro basado en navegador
Consiste en que el servidor web envía código manipulado donde se inyecta el código malicioso en el navegador. Una vez que el usuario cierra el navegador o el proceso afectado, el dispositivo dejaría de realizar acciones de minado.

Este tipo de criptosecuentro empezó en 2017 cuando la empresa alemana de servicios web Coinhive desarrolló un javascript que al instalarlo en el sitio web permitía realizar minería para la criptomoneda Monero. De esta forma se permitía a los propietarios de sitios web obtener ingresos alternativos a la visualización de anuncios.

Inicialmente, el acuerdo era abierto, transparente y consensuado entre los visitantes y los propietarios del sitio web. Sin embargo, los ciberdelincuentes pronto vieron el potencial lucrativo y comenzaron a colocar en secreto en miles de sitios web versiones modificadas de la biblioteca de Coinhive pero mandando los ingresos a los grupos delictivos.

Poco a poco, los fabricantes de navegadores, al ver la expansión del minado ilícito a través de navegadores que relentizaban los sitios web, comenzaron a implementar funciones de seguridad para detectar y bloquear este tipo de operaciones. En 2018, Google prohibió las extensiones web que extrajeran criptomonedas de Chrome Web Store.

En marzo de 2019, los operadores de Coinhive anunciaron que iban a cerrar, citando varias razones, incluida la creciente dificultad y eficiencia en la extracción de Monero dentro de los navegadores web. Además, se publicaron artículos demostrando que la ineficiencia del cryptojacking para generar ingresos, a pesar de su popularidad entre los grupos de delitos cibernéticos, con solo tres anuncios clásicos en línea que generaban 5,5 veces más ingresos que un script de cryptojacking basado en la web. Estas fueron las razones por las que después del cierre de Coinhive se redujeron a niveles casi inexistentes el criptojacking basado en el navegador, ya que la mayoría de las bandas de delitos cibernéticos pasaron a otras tácticas.

Criptosecuestro basado en routers
El funcionamiento en este tipo de criptosecuestro es similar al criptosecuestro basado en navegadores, salvo que el origen del código malicioso no está en un servidor web modificado, si no en un router con código malicioso que modifica el tráfico para introducir dicho código. Es decir, aprovechándose vulnerabilidades de los routers, se instala software que reescribe el tráfico del usuario y embebe código de criptominado en cada conexión a cualquier web. De esta forma cualquier página web visitada por cualquier usuario detrás de router infectado realizaría procesos de minado a favor de los ciberdelincuentes.

Observar que la inyección puede funcionar en ambos sentidos, para el tráfico que llega al usuario y, si por ejemplo, un sitio web está alojado en una red local detrás de un router afectado, el tráfico a ese sitio web también se inyectará con el código malicioso.

En 2019, Interpol lideró una operación en el sudeste asiático que redujo el cryptojacking en un 78% en la zona. Las autoridades de los países participantes recibieron pautas para detectar y eliminar el malware malicioso parcheando enrutadores infectados. El ataque se aprovechaba de una vulnerabilidad publicada, que no había sido parcheada en miles routers, para cambiar su configuración e inyectar un script de minería de criptomonedas en algunas partes del tráfico web. Algunos ISP usaban estos routers para su red principal, lo que permitió al atacante inyectar el código malicioso en una gran cantidad de tráfico web.

Criptosecuestro basado en archivos
Consiste en la instalación de malware en los propios dispositivos. Este malware es el que se encarga de realizar el minado de criptomonedas. La instalación en  como en cualquier otro tipo de malware. Puede originarse en el contenido en archivos adjuntos en correos electrónicos, instalación de plugins modificados, aprovechamiento vulnerabilidades, contraseñas débiles, gusanos, ...

En este tipo de infección, al estar instalado en el propio del dispositivo es más difícil eliminar.

Este tipo de malware puede realizar, además del criptominado, otro tipo de técnicas maliciosas y formar sus propias botnets. Por ejemplo, la botnet Smominru realiza criptominado para la criptomoneda Monero y también permite el robo de información y captura de credenciales. Esta red ha sido detectada desde 2017 y en 2020 se estimaba que estaba compuesta por más de 500.000 nodos. El objetivo de este malware son servidores windows, los cuales están encendidos todo el tiempo, de pequeño tamaño.

Criptosecuestro basado en la nube
La característica que más atrae de la nube para el criptosecuestro es el aumento en la capacidad de computo según las necesidades de consumo. Esto logra que sea casi imperceptible la presencia de minadores dentro de la infraestructura de las empresas, tanto el aumento de uso de CPU y el consumo eléctrico es algo que se contempla como normal en los montajes en la nube.

Para poder tener acceso a los recursos en la nube es frecuente:
Búsqueda en el código o archivos de una organización con la esperanza de encontrar las claves API para acceder al servicio en la nube.
Aprovechar los errores de configuración que dejan los administradores en el momento de realizar las migraciones.
Aprovechar las nuevas vulnerabilidades de los sistemas y mecanismos de administración de la computación en la nube.

A partir del acceso instalan software y usan los recursos de la CPU para extraer criptomonedas.

En febrero de 2018, FireEye, publicó como los delincuentes aprovecharon una vulnerabilidad de los servidores Oracle en entornos en la nube para inyectar minadores en la configuración de Oracle WebLogic Server Security. En el mismo mes, L.A. Times sufrió un ataque que aprovechó vulnerabilidades en Amazon Web Services S3 para inyectar javascript que hacía que los visitantes de su web minaran para los delincuentes.

En 2018, al no modificarse la contraseña de gestión por defecto del administrador del sistema, se introdujo código de criptojacking en los nodos de Kubernetes de Tesla.

Detección
Debido a que el proceso de minado requiere de un alto grado de uso del procesador y de la conexión a internet, los principales síntomas son que funcionan lento, se quedan colgados constantemente o que la velocidad de conexión a Internet se ralentiza. Además, el uso de los dispositivos al máximo rendimiento provoca otra serie de indicadores físicos, como sobrecalentamiento de los componentes y un alto consumo de energía eléctrica.

Para aumentar la dificultad de la detección, los ciberdelincuentes ha ido distintas estrategias como por ejemplo:
Algoritmos de minado ligeros que dificultan enormemente su detección.
Detener la minería cuando se detecta la actividad del mouse para que el usuario del dispositivo no sepa que está infectado.
Operar muy por debajo del 100% de potencia de procesamiento.

Referencias
