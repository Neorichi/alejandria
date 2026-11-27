---
type: Artículo de enciclopedia
title: Virus Málaga
description: "El Virus Málaga (también conocido como Virus:DOS/Malaga.2610 o Málaga) es un código malicioso informático de tipo multipartito detectado por primera vez en España entre 1991 y 1992."
resource: https://es.wikipedia.org/wiki/Virus_Málaga
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Virus_Málaga"}
license: CC BY-SA 4.0
id: eswiki-Virus_Málaga
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Virus Málaga

- **Nombre:** Virus Málaga
- **Alias:** DOS/Malaga.2610
- **Tipo:** Virus informático
- **Subtipo:** Multipartito
- **Plataforma:** MS-DOS
- **Origen:** Universidad de Málaga
- **Año:** 1991–1992
- **Autor:** Antonio Enrique Astorga

El **Virus Málaga** (también conocido como *Virus:DOS/Malaga.2610* o *Málaga*) es un código malicioso informático de tipo multipartito detectado por primera vez en España entre 1991 y 1992. Originado en el ámbito académico de la Universidad de Málaga (UMA), es considerado un hito fundacional en la historia de la ciberseguridad española, ya que su aparición y posterior análisis impulsaron la carrera de Bernardo Quintero, fundador de VirusTotal.

 Clasificación
El Virus Málaga está clasificado técnicamente como un virus **multipartito** (o *multipartite*), una categoría de *malware* compleja para la época de su creación (principios de la década de 1990).

 **Tipo:** Multipartito y residente en memoria.
 **Objetivos de infección:** Archivos ejecutables (.COM y .EXE) y estructuras de arranque del disco (Sector de arranque y *Master Boot Record* o Registro de arranque principal).
 **Tamaño:** La versión original tiene un tamaño de **2610 bytes**. Existe una variante posterior, denominada *Málaga II*, de **2385 bytes**.
 **Entorno:** Sistemas operativos MS-DOS / PC-DOS.

 Variantes
Además de la versión original de 2610 bytes, se identificó posteriormente una variante denominada **Málaga II**, de 2385 bytes, que incluía la cadena de texto «KIKESOYYO» como firma del autor.

 Historia
A finales de los años ochenta y principios de los noventa, el uso de ordenadores personales en España estaba mayoritariamente restringido a ámbitos académicos y profesionales. Los sistemas MS-DOS dominaban el entorno universitario y carecían de mecanismos avanzados de seguridad, lo que facilitaba la experimentación directa con el hardware y el software de bajo nivel.

En este contexto, los laboratorios de la Escuela Universitaria Politécnica de la Universidad de Málaga, ubicados entonces en el campus de El Ejido, se convirtieron en un espacio de aprendizaje práctico donde los estudiantes exploraban programación en ensamblador, arquitectura de sistemas y control de memoria.

El virus surgió entre 1991 y 1992 en esta escuela andaluza. A diferencia de otras amenazas de la época que solían ser importadas, el Virus Málaga fue un desarrollo local que paralizó los laboratorios de la universidad, los cuales operaban con esas estaciones de trabajo bajo MS-DOS.

En 1992, ante la ineficacia de los antivirus comerciales del momento para erradicar la infección, el profesor de Informática General, Adolfo Cid, retó a sus alumnos a desarrollar una herramienta de desinfección. Bernardo Quintero, entonces estudiante de primer curso, aceptó el desafío.

Tras más de tres décadas de especulación, la autoría del virus fue atribuida en diciembre de 2025 a Antonio Enrique Astorga, ya fallecido, antiguo estudiante de la Universidad de Málaga, cerrando uno de los enigmas históricos de la informática española.

 Funcionamiento
El Virus Málaga es clasificado como un virus **multipartito**, capaz de infectar simultáneamente archivos ejecutables (.COM y .EXE) y el sector de arranque (MBR) de los discos. Una vez ejecutado un archivo infectado, el virus permanecía residente en memoria y utilizaba interrupciones del sistema como INT 21h e INT 13h para interceptar operaciones de disco y propagarse a nuevos soportes de almacenamiento.

Infectaba el sector de arranque de los discos. Cuando se cumplía una condición (Año 1992 o superior y día 1 de cualquier mes) se activaba una rutina que iba leyendo los bytes, les restaba 100 y los imprimía por pantalla. Mostraba un mensaje contra la organización terrorista ETA, lo que ha sido interpretado como una forma temprana de expresión política mediante software malicioso.

 Autoría
Durante más de treinta años, la autoría del Virus Málaga fue objeto de especulación en el entorno académico y tecnológico de Málaga. En diciembre de 2025, tras un llamamiento público realizado por Bernardo Quintero, se confirmó que el autor fue Antonio Enrique Astorga, antiguo estudiante de la Escuela Universitaria Politécnica. La identificación se apoyó en testimonios de antiguos compañeros, como Adolfo Ariza Ruz, y en el análisis de las firmas incluidas en el código del virus.

 Desinfección
Bernardo Quintero desarrolló una herramienta de limpieza utilizando Turbo Pascal 5.5, combinando código Pascal con ensamblador para restaurar archivos ejecutables y reconstruir sectores de arranque sin dañar las particiones del disco.

 Impacto
El Virus Málaga es considerado un hito en la historia temprana de la ciberseguridad en España. Su análisis y erradicación contribuyeron a la formación de especialistas que posteriormente desempeñaron un papel relevante en la industria global de la seguridad informática, incluyendo el desarrollo del Google Safety Engineering Center en Málaga.

 Véase también

 Malware
 Virus informático
 Seguridad informática en España

 Referencias
