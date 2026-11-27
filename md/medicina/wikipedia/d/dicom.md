---
type: Artículo de enciclopedia
title: DICOM
description: "DICOM (“Digital Imaging and Communication in Medicine”) es un estándar de transmisión de imágenes médicas y datos entre hardware de propósito médico."
resource: https://es.wikipedia.org/wiki/DICOM
tags: [medicina, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/DICOM"}
license: CC BY-SA 4.0
id: eswiki-DICOM
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# DICOM

**DICOM** (“***D**igital **I**maging and **Co**mmunication in **M**edicine*”) es un estándar de transmisión de imágenes médicas y datos entre hardware de propósito médico. Las aplicaciones más comunes de este estándar son la visualización, almacenamiento, impresión y transmisión de las imágenes. El protocolo incluye la definición de un formato de fichero, un protocolo de comunicación de red basado en TCP/IP.

DICOM permite la integración de escáneres, servidores, estaciones de trabajo, impresoras y hardware de red de múltiples proveedores dentro de un sistema de almacenamiento y comunicación de imágenes. Las diferentes máquinas, servidores y estaciones de trabajo tienen una declaración de conformidad DICOM *(conformance statements)*  (discus.) que establece claramente las clases DICOM que soportan. DICOM ha sido adoptado ampliamente por hospitales y está haciendo incursión en pequeñas aplicaciónes de oficinas de dentistas y de médicos.

 Formato de datos DICOM

Independientemente del uso, siempre se utiliza el mismo formato, incluyendo el uso de ficheros y de red.
DICOM se diferencia de otros ficheros de datos en que agrupa la información dentro de un conjunto de datos. Es decir, una radiografía de TORAX contiene el ID de paciente junto con ella, de manera que la imagen no puede ser separada por error de su información.

Los ficheros DICOM consisten en una cabecera con campos estandarizados y de forma libre, y un cuerpo con datos de imagen. Un objeto DICOM simple puede contener solamente una imagen, pero esta imagen puede tener múltiples "fotogramas" (frames), permitiendo el almacenamiento de bloques de cine o cualquier otros datos con varios fotogramas. Los datos de imagen puede estar comprimidos usando gran variedad de estándares, incluidos JPEG, JPEG Lossless, JPEG 2000, LZW y Run-length encoding (RLE).

 Servicios DICOM

DICOM tiene un conjunto muy amplio de servicios, la mayoría de los cuales implica transmisión de datos sobre la red, y el formato de fichero en que se sustenta es en realidad una ampliación posterior y de menor importancia del estándar.

 Dicom Store

El servicio DICOM Store es usado para mandar imágenes u otros objetos persistentes (informes estructurados, etc.) a un PACS o a una estación de trabajo.

 Storage Commitment

El servicio DICOM storage commitment es usado para confirmar que una imagen ha sido almacenada permanentemente por un dispositivo. El usuario de la clase de servicio (modalidad, estación de trabajo, etc.) utiliza la confirmación de la clase de servicio proveedor (estación de almacenamiento) para asegurarse de que puede borrar la imagen localmente.

 Query/Retrieve

Permite a una estación de trabajo hacer búsquedas de imágenes en un PACS y recuperarlas.

 Dicom Worklist

Permite a un equipo de imagen que incluya esta funcionalidad o Servicio DICOM leer la "Lista de Pacientes citados", obtener detalles de los pacientes y exámenes médicos solicitados electrónicamente, evitando la necesidad de introducir esa información varias veces y sus consiguientes errores.

 Modality Performed Procedure Step

Un servicio complementario al Modality Worklist, que permite a la modalidad mandar un informe sobre los exámenes médicos realizados incluyendo datos sobre las imágenes adquiridas, las dosis dispensadas, etc.
Consta de tres estados:
 En progreso: significa que la realización del estudio ha comenzado.
 Terminado: significa que la realización del estudio fue terminada satisfactoriamente.
 Descontinuado: significa que la realización del estudio fue cancelada o no pudo ser terminada.

 DicomPrint

Este servicio es usado para mandar imágenes a una impresora DICOM, normalmente para imprimir una placa de rayos X. Hay una calibración estándar (definida en la parte 14 de DICOM) para ayudar a asegurar la consistencia entre distintos dispositivos de pantalla.

 Ficheros DICOM

Los ficheros DICOM corresponden a la parte 10 del estándar DICOM. Describe como almacenar información de imágenes médicas en un medio extraíble. Generalmente es obligatorio incluir también los metadatos de la imagen.

DICOM restringe los nombres de los ficheros a nombres de 8 caracteres (mucha gente utiliza erróneamente 8.3, pero esto no es legal). Del nombre del fichero no debe de extraerse ninguna información. Esta es una fuente común de problemas con contenidos creados por desarrolladores que no han leído la especificación cuidadosamente. Este es un requerimiento histórico para mantener compatibilidad con antiguos sistemas existentes. También es obligatorio la presencia de un directorio de contenido, el fichero DICOMDIR, que proporciona un índice e información de resumen para cada uno de los ficheros DICOM del contenido.
La información del DICOMDIR proporciona sustancialmente más información sobre cada fichero de los nombres de los ficheros, de manera que hay menos necesidad de nombres de fichero con significado.

 Historia

El primer estándar DICOM importante es la versión 3.0, que fue desarrollado en 1993. Detalles de la especificación DICOM está disponibles en la web National Electrical Manufacturers Association (NEMA), y existen muchas implementaciones de código abierto y de dominio público.

 Integración de DICOM con estándares HL7

HL7 v3, incluye un dominio de imagenología diagnóstica (Imaging Integration Domain), para la integración con DICOM.

Este dominio cuenta con modelos, guías de implementación y ejemplos de documentos e imágenes necesarios para ilustrar la transformación de un reporte estructurado DICOM a documentos electrónicos CDA R2 HL7, así como la creación de informes CDA de imagenología diagnóstica.

A este respecto, el comité de estándares DICOM mantiene un acuerdo con Health Level Seven Inc, cuyo memorando de acuerdo fue renovado en 2008.

 Véase también

 NEMA

 Referencias

 Enlaces externos

 Página oficial de NEMA
 DCM4CHEE: Servidor de imágenes médicas DICOM (software libre)
WEASIS: Visualizador de imágenes médicas DICOM (software libre)
 Conversor gratuito en-linea de DICOM
