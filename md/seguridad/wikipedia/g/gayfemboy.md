---
type: Artículo de enciclopedia
title: Gayfemboy
description: Gayfemboy es una cepa de malware que infecta dispositivos electrónicos corporativos, como los de DrayTek, TP-Link, Raisecom y Cisco, mediante el uso de CVEs.
resource: https://es.wikipedia.org/wiki/Gayfemboy
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Gayfemboy"}
license: CC BY-SA 4.0
id: eswiki-Gayfemboy
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Gayfemboy

**Gayfemboy** es una cepa de malware que infecta dispositivos electrónicos corporativos, como los de DrayTek, TP-Link, Raisecom y Cisco, mediante el uso de CVEs. Ha afectado a empresas de Brasil, Francia, Alemania, Israel, México, Estados Unidos, Suiza y Vietnam, y está impactando sectores como la construcción, la manufactura, la tecnología y los medios de comunicación.

 Historia
El malware fue descubierto por primera vez en febrero de 2024 por investigadores de seguridad de Fortinet, tras numerosos ataques realizados por Gayfemboy en enero. Este malware utilizó los equipos infectados como una botnet para lanzar una oleada de ataques DDoS contra sitios web objetivo. Las muestras conocidas estaban ofuscadas con un empaquetador UPX, pero su encabezado "UPX!" fue reemplazado por caracteres no imprimibles en código hexadecimal «10 F0 00 00», lo que dificulta su detección. Tras su ejecución, el malware investiga las rutas de cada proceso ubicado en «/proc/[PID]/exe» para recopilar información sobre los procesos activos y sus respectivas ubicaciones en el sistema de archivos. Carga 47 cadenas de comandos en memoria y revisa todas las entradas en «/proc/[PID]/cmdline». Si encuentra una coincidencia, finaliza el proceso correspondiente. Estos comandos incluyen «ls -l», «reboot» y «wget», entre otros. El Monitor se utiliza para la autopreservación y para detectar entornos aislados. Si Gayfemboy identifica que el proceso del malware ha finalizado, genera un reinicio. Debido a un retraso de 50 nanosegundos, el malware es capaz de detectar un entorno aislado, que no puede gestionar un retraso tan preciso, lo que provoca el fallo de la función invocada y provoca que el malware malinterprete el resultado, lo que desencadena un estado de inactividad de 27 horas.

Las infecciones y la segmentación son similares a las de la cepa de malware Mirai y se dirige a diversas arquitecturas de sistema, como ARM, AArch64, MIPS R3000, PowerPC e Intel 80386. El malware Gayfemboy rastrea hilos y procesos, incorporando técnicas de persistencia y evasión de entornos aislados, se enlaza al puerto UDP 47272, lanza ataques DDoS mediante los protocolos UDP, TCP e ICMP y habilita el acceso por puerta trasera conectándose a un servidor remoto para recibir comandos. Además, se autotermina si recibe el comando del servidor o detecta manipulación del entorno aislado. El ataque consiste principalmente en la búsqueda de servidores Redis no autenticados que operen en el puerto 6379. A continuación, se ejecutan los comandos legítimos CONFIG, SET y SAVE para iniciar una tarea cron dañina destinada a ejecutar un script de shell. Este script está diseñado para deshabilitar SELinux, implementar medidas de evasión de defensa, bloquear el acceso externo al puerto Redis para evitar que entidades rivales exploten la ruta de acceso inicial y finalizar procesos de minería de datos de la competencia (como Kinsing).

La botnet Gayfemboy, detectada por primera vez en febrero de 2024, ha estado utilizando estrategias sofisticadas, como la explotación de vulnerabilidades de día cero para infiltrarse en dispositivos. Para noviembre de 2024, la botnet había ampliado su alcance, centrándose en routers industriales y dispositivos domésticos inteligentes, con más de 15000 nodos activos. Quienes operan Gayfemboy también han lanzado ataques DDoS contra investigadores que monitorean sus operaciones. El malware incorpora métodos únicos de nomenclatura de archivos y ofuscación para evadir la detección, con cuatro módulos principales diseñados para diversos fines maliciosos.

En julio de 2025, FortiGuard Labs descubrió una carga útil de Gayfemboy que explotaba diversas vulnerabilidades en dispositivos. Los ataques se rastrearon hasta las direcciones IP 87.121.84.34 y 220.158.234.135. Los expertos identificaron scripts de descarga dirigidos a varios dispositivos atacados por el bot, entre ellos Asus, Vivo, ZyXEL y Realtek. El código malicioso recuperó malware y mineros de Monero, cuyos nombres de producto se enviaron como parámetros a Gayfemboy para su ejecución.

Para agosto de 2025, Fortinet implementó protección multicapa contra la campaña Gayfemboy mediante los servicios FortiGuard. Los servicios de filtrado web bloquean activamente los dominios C2 identificados, mientras que las firmas IPS brindan protección contra todas las vulnerabilidades explotadas. Estos dominios incluyen cross-compiling.org, i-kiss-boys.com, furry-femboys.top, twinkfinder.nl y 3gipcam.com.

 Referencias

 Enlaces externos
