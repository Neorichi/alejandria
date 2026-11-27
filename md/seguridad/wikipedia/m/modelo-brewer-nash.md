---
type: Artículo de enciclopedia
title: Modelo Brewer-Nash
description: El Modelo Brewer-Nash, también conocido como Muralla China (Chinese Wall), es un modelo de seguridad informática formulado en 1989 por David F.C.
resource: https://es.wikipedia.org/wiki/Modelo_Brewer-Nash
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelo_Brewer-Nash"}
license: CC BY-SA 4.0
id: eswiki-Modelo_Brewer-Nash
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelo Brewer-Nash

El **Modelo Brewer-Nash**, también conocido como **Muralla China** (**Chinese Wall**), es un modelo de seguridad informática formulado en 1989 por David F.C. Brewer y Michael J. Nash. Diseñado para proporcionar controles que minimizaran los conflictos de intereses en organizaciones comerciales, y construido sobre un modelo de flujo de información. Se le conoce como la muralla China debido a que se basa en crear una pared lógica entre un usuario y la información que no debe acceder. Si dos usuarios tienen el mismo nivel de acceso, esto no quiere decir que puedan leer la misma información.

Este modelo no distingue entre sujetos y objetos por lo cual se puede aplicar la misma política de seguridad a ambos elementos. Su principal virtud es la de ofrecer una gran confidencialidad, ya que los datos que se manejan no pueden ser leídos por sujetos distintos a los interesados, en el caso de que esto ocurriera el modelo garantiza que la información obtenida no pueda ser dada a conocer en otros medios.

 Introducción

En el tema de políticas de seguridad, la industria militar es la que se encarga de realizar los mayores avances. Sin embargo, actualmente existe una preocupación para proteger el ámbito comercial, por eso surgió la necesidad de crear políticas específicas para esto, como es el caso de Muralla China.

Uno de los escenarios para aplicar la política, es el de los consultores comerciales, quienes tienen conocimiento directo de la información confidencial de una compañía y con el fin de prevenir el flujo de datos confidenciales, lo cual causa un conflicto de intereses, se recomienda aplicar las reglas de esta la política de seguridad, la cual surge como una alternativa para garantizar grados de confidencialidad.

 Organización de la base de datos

Para todos los modelos formales de seguridad, es importante tener una clasificación de los datos del negocio. Esta información puede ser almacenada en un sistema jerárquico de tres niveles de importancia:

 *Nivel inferior*. Está integrada por partes individuales de información, cada una forma parte de una sola empresa. Se le considera como objetos a este tipo de información.
 *Nivel intermedio*. Se agrupan todos los objetos pertenecientes a la misma empresa y se denomina como datos de la Empresa.
 *Nivel superior*. Se agrupan todos los conjuntos de datos de las empresas que están en competencia; a dichas agrupaciones se les llama clases de Conflicto de Interés.

Para establecer la política de seguridad, se asocia cada objeto con el nombre del conjunto de datos de la empresa, y el nombre de la clase del conflicto de interés, a los que pertenece.

 Accesibilidad

La accesibilidad puede ser representada mediante las siguientes reglas.
 Una vez que un sujeto haya accedido a un objeto en particular, solo podrá acceder a otros objetos que se encuentren dentro del mismo conjunto de datos de la empresa o que estén en un conflicto de intereses diferente.
 Un sujeto puede acceder a lo sumo a un solo conjunto de datos de empresas por cada clase de conflicto de intereses.

 Ejemplo de uso

Consideremos los conjuntos de datos del banco A, de la Empresa de Petróleo A y la Empresa de Petróleo B; un usuario nuevo puede acceder a cualquier conjunto de datos que desee ya que este usuario no posee ninguna información y por lo tanto tampoco existe conflicto de intereses.

Si el usuario accede primero al conjunto de datos de la Empresa de Petróleo A, se dice que éste posee información que concierne a esta empresa. El usuario podrá siempre acceder a la información del banco A, porque el conjunto de datos del Banco A y de la Empresa de Petróleo A pertenecen a diferentes clases de conflicto de intereses.

Si después de esto intenta acceder al conjunto de datos de la Empresa de Petróleo B, esta petición debe ser negada, debido a que existe un conflicto entre el conjunto de datos que ya posee (Empresa de Petróleo A) y los datos que quiere acceder (Empresa de Petróleo B).

Si el usuario hubiera elegido en primera instancia acceder a la información de la Empresa de Petróleo B, las restricciones de este modelo no le permitirían acceder a la información de la Empresa de Petróleo A, porque causaría un conflicto de intereses. Sin embargo, todavía podría acceder a la información del Banco A.

Como se puede observar en este ejemplo, la política de la Muralla China es una combinación de elección libre y control obligatorio, ya que el usuario puede elegir libremente cual será el primer objeto al que accederá, después de esto se creará una Muralla China para evitar conflictos de interés.

 Comparación con Clark-Wilson

La principal diferencia entre estos dos modelos de seguridad es que el modelo de Clark-Wilson está orientado al sector militar, mientras que Brewer-Nash tiene un enfoque comercial. Otra diferencia es que el acceso de información para Clark-Wilson depende del nivel de acceso de los usuarios, mientras que la accesibilidad de Brewer-Nash está determinada por la información que haya accedido con anterioridad el usuario.

 Véase también

 Modelo Clark-Wilson
 Modelo Bell-LaPadula
 Modelo Take-Grant

 Referencias

 Enlaces externos
