---
type: Artículo de enciclopedia
title: Plan de recuperación ante desastres
description: "Un plan de recuperación ante desastres (del inglés Disaster Recovery Plan) es un proceso de recuperación que cubre los datos, el hardware y el software crítico, para que un negocio pueda comenzar de nuevo sus …"
resource: https://es.wikipedia.org/wiki/Plan_de_recuperación_ante_desastres
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Plan_de_recuperación_ante_desastres"}
license: CC BY-SA 4.0
id: eswiki-Plan_de_recuperación_ante_desastres
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Plan de recuperación ante desastres

Un **plan de recuperación ante desastres** (del inglés *Disaster Recovery Plan*) es un proceso de recuperación que cubre los datos, el hardware y el software crítico, para que un negocio pueda comenzar de nuevo sus operaciones en caso de un desastre natural o causado por humanos. Esto también debería incluir proyectos para enfrentarse a la pérdida inesperada o repentina de personal clave, aunque esto no sea cubierto en este artículo, el propósito es la protección de datos.

El Plan de Recuperación ante Desastres puede considerarse como uno de los subplanes dentro del Plan de Contingencia de TI.

 Negocios

Con el crecimiento de la tecnología de información y la confianza sobre datos decisivos, el panorama ha cambiado en años recientes a favor de la protección de datos irreemplazables. Esto es evidente sobre todo en la tecnología de información; con los sistemas de ordenadores más grandes que sostienen información digital para limitar pérdida de datos y ayudar recuperación de datos.

Se cree que algunas empresas gastan hasta el 25 % de su presupuesto en proyectos de recuperación de desastre, sin embargo, esto lo hacen para evitar pérdidas más grandes. De las empresas que tenían una pérdida principal de registros automatizados el 43 % nunca vuelve a abrir, el 51 % cierra en menos de dos años, y sólo el 6 % sobrevivirá el largo plazo.

El mercado de protección de datos existente es caracterizado por varios factores:

El permanente cambio de las necesidades de los clientes determinado por el crecimiento de datos, asuntos regulatorios y la creciente importancia de tener rápido acceso a los datos conservándolos en línea.
Respaldar los datos de vez en cuando teniendo tecnologías de cintas convencionales de reservas.

Como el mercado de recuperación de desastre sigue sufriendo cambios estructurales significativos, este cambio presenta oportunidades para las empresas de la nueva generación a que se especialicen en la planificación de continuidad de negocio y la protección de datos fuera de sitio.

 Razones para recurrir a un DRP

Existen diferentes riesgos que pueden impactar negativamente las operaciones normales de una organización. Una evaluación de riesgo debería ser realizada para ver que constituye el desastre y a que riesgos es susceptible una empresa específica, incluyendo:

Catástrofes.
Fuego.
Fallos en el suministro eléctrico.
Ataques terroristas.
Interrupciones organizadas o deliberadas.
Sistema y/o fallos del equipo.
Error humano.
Virus, amenazas y ataques informáticos.
Cuestiones legales.
Huelgas de empleados.
Conmoción social o disturbios.
Pandemia.

 Prevención ante los desastres
 Enviar respaldos fuera de sitio semanalmente para que en el peor de los casos no se pierda más que los datos de una semana.
 Incluir el software así como toda la información de datos, para facilitar la recuperación.
 Si es posible, usar una instalación remota de reserva para reducir al mínimo la pérdida de datos.
 Redes de Área de Almacenamiento (SANs) en múltiples sitios son un reciente desarrollo (desde 2003) que hace que los  datos estén disponibles inmediatamente sin la necesidad de recuperarlos o sincronizarlos.
 Protectores de línea para reducir al mínimo el efecto de oleadas sobre un delicado equipo electrónico.
 El suministro de energía ininterrumpido (SAI).
 La prevención de incendios - más alarmas, extintores accesibles.
 El software del antivirus.
 El seguro en el hardware.

 El plan

Para asegurar la continuidad del negocio, es recomendable partir de la siguiente premisa: "Siempre desear lo mejor y planear para lo peor". En un buen plan existen diferentes factores que hay que tomar en cuenta. Los más importantes son:

El árbol telefónico: para notificar todo el personal clave del problema y asignarles tareas enfocadas hacia el plan de recuperación.
Reservas de memoria: si las cintas de reserva son tomadas fuera de sitio es necesario grabarlas. Si se usan servicios remotos de reserva se requerirá una conexión de red a la posición remota de reserva (o Internet).
Clientes: la notificación de clientes sobre el problema reduce al mínimo el pánico.
Instalaciones: teniendo sitios calientes o sitios fríos para empresas más grandes. Instalaciones de recuperación móviles están también disponibles en muchos proveedores.
Trabajadores con conocimiento. Durante desastre a los empleados se les requiere trabajar horas más largas y más agotadoras. Debe haber un sistema de apoyo para aliviar un poco de tensión.
La información de negocio. Las reservas deben estar almacenadas completamente separadas de la empresa (Cummings, Haag y 2005 McCubbrey). La seguridad y la fiabilidad de los datos es clave en ocasiones como estas1.

 Proceso de recuperación

 Comprar nuevo equipamiento (el hardware) o reparar, o quitar virus, etc.
 Llamar al proveedor de software e instalar de nuevo el software.
 Recuperar los discos de almacenamiento que estén fuera de sitio.
 Re-instalar todos los datos de la fuente de respaldo.
 Volver a ingresar los datos de las pasadas semanas. (ver RPO)
 Tener estrategias periódicas de respaldos de base de datos.
 Monitorear el proceso.

 Tecnología

Biblioteca de cinta virtual.
Software de réplica sincrónico.
Tecnología de almacenaje de réplica.
Servicio telefónico virtual PBX/HOSTED.
Backups remotos de reserva.
Protector de datos continuo.
Sistema para la administración de planes (Moebius).
Cloud

**Terminología:**

Punto Objetivo de Recuperación (RPO, Recovery Point Objective). RPO es una medida que indica el máximo periodo de tiempo que una organización está dispuesta a perder datos. Podría simplificarse como lo que la organización está dispuesta a perder en cantidad de datos. Para reducir un RPO es necesario aumentar el sincronismo de réplica de datos.
Tiempo objetivo de recuperación (RTO, Recovery Time Objective) es el tiempo que pasará una infraestructura antes de estar disponible. Para reducir el RTO, se requiere que la Infraestructura (Tecnológica, Logística, Física) esté disponible en el menor tiempo posible pasado el evento de interrupción.

Cuando ocurre una pérdida de datos crítica, sin un plan de recuperación de desastre preventivo, la única opción es salvar los datos.

 Véase también
 Plan de continuidad del negocio
 Plan de contingencias

 Referencias

 Enlaces externos
 Plan de continuidad del negocio
