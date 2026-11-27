---
type: Artículo de enciclopedia
title: Ryuk (ransomware)
description: Ryuk es un tipo de ransomware conocido por realizar ciberataques a grandes entidades públicas.
resource: https://es.wikipedia.org/wiki/Ryuk_(ransomware)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ryuk_(ransomware)"}
license: CC BY-SA 4.0
id: eswiki-Ryuk_(ransomware)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ryuk (ransomware)

**Ryuk** es un tipo de ransomware conocido por realizar ciberataques a grandes entidades públicas. Por lo general, encripta los datos en un sistema infectado, haciendo inaccesible los datos del mismo hasta que se consigue un rescate pagado en Bitcoin. Se cree que Ryuk es utilizado por dos o más grupos criminales, probablemente rusos, cuyos objetivos son las organizaciones gubernamentales, en lugar de atacar a los individuos o consumidores.

Origen
El ransomware apareció por primera vez en 2018. Aunque hubo sospechas iniciales de que era de origen norcoreano, más adelante las dudas recayeron en un origen ruso, ligado a dos o más cárteles del crimen de Europa del Este. A diferencia de otros piratas informáticos malintencionados, los controladores de Ryuk buscan principalmente extorsionar el pago de rescates para liberar los datos que su malware ha inutilizado mediante el cifrado. En una entrevista al *Baltimore Sun*, en referencia a su *modus operandi*, un analista de ciberseguridad estadounidense expresó, después de un ataque al sistema escolar del condado de Baltimore (Maryland) en noviembre de 2020, que usan Ryuk porque "todo es un negocio [para ellos], sólo les gusta hacer el trabajo", en referencia a las acciones para extorsionar un gran pago de rescate.

Forma de actuación
El Centro Nacional de Seguridad Cibernética británico señaló que Ryuk usa el malware Trickbot para instalarse una vez que obtiene los accesos para entrar a los servidores de una red. Tiene la capacidad de derrotar muchas contramedidas antimalware que pueden estar presentes y pueden deshabilitar por completo una red de computadoras. Entre sus funciones, es capaz de buscar y deshabilitar archivos de respaldo si se mantienen en servidores compartidos. Otro malware troyano usado por los piratas informáticos tras Ryuk es Emotet.

La Agencia de Ciberseguridad y Seguridad de las Infraestructuras estadounidense (CISA) ha proporcionado información en red sobre cómo Ryuk infecta y toma el control de una red informática, expresando que el acceso se puede obtener inicialmente mediante "campañas de phishing que contienen enlaces a sitios web maliciosos que alojan el malware o los archivos adjuntos con el malware. Los cargadores inician la cadena de infección distribuyendo la carga útil; despliegan y ejecutan la puerta trasera desde el servidor de comando y control y la instalan en la máquina de la víctima". Los esfuerzos de phishing generalmente contienen documentos maliciosos (o hipervínculos a ellos). Cuando la víctima lo habilita, un cargador o macro malicioso inicia la secuencia de infección.

Una vez que Ryuk toma el control de un sistema, cifra los datos almacenados, lo que hace imposible que los usuarios accedan a los mismos, a menos que éste realice un pago o rescate mediante el uso de bitcoin a una cuenta desconocida e ilocalizable. En muchos casos, pueden pasar días o semanas entre el momento en que los piratas informáticos obtienen acceso inicialmente a un sistema antes de que se produzca el cifrado masivo, ya que los delincuentes penetran más profundamente en la red para infligir el máximo daño. Ryuk es un malware especialmente pernicioso porque también encuentra y cifra las unidades y los recursos de la red. También deshabilita la función de "restaurar sistema" de Microsoft Windows que, de lo contrario, permitiría restaurar los archivos del sistema, las aplicaciones y el registro del ordenador a su estado anterior sin cifrar.

Acciones del ransomware
Ryuk tiene por objetivo grandes organizaciones y corporaciones que sus promotores entienden tienen la capacidad de pagar importantes sumas de dinero para recuperar el acceso a sus valiosos datos. Entre 2018 y 2019, según datos del FBI, se llegaron a pagar más de 61 millones de dólares en rescate por los ataques de malware de Ryuk. En diciembre de 2018, un ataque con base en Ryuk afectó la publicación de *Los Angeles Times* y otros periódicos de Estados Unidos que utilizaban el software Tribune Publishing. La impresión del *Sun-Sentinel*, en Fort Lauderdale (Florida), se detuvo en seco e incluso los teléfonos del periódico no funcionaron. El 20 de octubre de 2020, la consultora de IT francesa Sopra Steria sufrió un ataque por Ryuk. Los ciberdelincuentes cifraron los datos de la empresa utilizando una variante de Ryuk, haciéndolos inaccesibles a menos que se pagara un rescate. El ataque le costó a la empresa un desembolso calculado entre 47 y 59 millones de dólares. A raíz del ataque, Ryuk fue descrito como "uno de los grupos de ransomware más peligrosos que operan a través de campañas de phishing".

Entre 2019 y 2020, hospitales de Estados Unidos en los estados de California, Nueva York y Oregón, así como en el Reino Unido y Alemania, se vieron afectados por el malware, provocando dificultades para acceder a las bases de datos de los pacientes e incluso afectando a los cuidados intensivos. Los médicos de los hospitales afectados tuvieron que recurrir a métodos clásicos para recetas y elaborar informes de alta en lugar de la digitalización de los mismos. El 29 de octubre de 2020, tres agencias del gobierno estadounidense, el FBI, CISA y el Departamento de Salud y Servicios Humanos emitieron una declaración conjunta, advirtiendo que los hospitales deberían anticipar un aumento e inminente "ola de ataques cibernéticos de ransomware que podrían comprometer la atención del paciente y exponer información personal", probablemente de los ataques de Ryuk. A finales de ese año, más de una docena de hospitales en Estados Unidos se habían visto afectados por estos ataques.

El ransomware se ha utilizado para atacar a decenas de sistemas escolares en Estados Unidos, que han sido generalmente deficientes en materia de ciberseguridad, con más de mil escuelas atacadas desde el origen del ransomware. El rescate exigido por los perpetradores ha oscilado entre 100 000 y 377 000 o más dólares.

A principios de 2021, se descubrió una nueva cepa del ransomware Ryuk que presentaba capacidades similares a gusanos que podían llevar a que se propagara por sí mismo y se distribuyera a otros dispositivos en la base de datos local en la que se infiltraban.

El 9 de marzo de 2021, se perpetró un ciberataque en España contra el Servicio Público de Empleo Estatal (SEPE) que comprometió los servidores que almacenaban la información de este departamento del Ministerio de Trabajo y Economía Social, impidiendo atender a diversas resoluciones presenciales en las oficinas del paro y vía telemática, aunque fuentes oficiales descartaron que se hubieran vulnerado datos personales o afectado en el pago de las prestaciones por desempleo o ERTE.

Referencias
