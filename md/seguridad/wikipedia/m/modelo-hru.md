---
type: Artículo de enciclopedia
title: Modelo HRU
description: El modelo HRU fue creado en 1976 al tratar de mejorar el modelo de matriz de acceso, ya que de manera general no toma en cuenta lo que un cambio en el modelo implica.
resource: https://es.wikipedia.org/wiki/Modelo_HRU
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modelo_HRU"}
license: CC BY-SA 4.0
id: eswiki-Modelo_HRU
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modelo HRU

El **modelo HRU** fue creado en 1976 al tratar de mejorar el modelo de matriz de acceso, ya que de manera general no toma en cuenta lo que un cambio en el modelo implica.

 Características
El modelo HRU define un sistema de protección que se encuentra constituido por dos elementos:

 Un conjunto de derechos genéricos, donde ese conjunto representa los tipos de acceso al sujeto hacia el objeto como leer, escribir, borrar, modificar, ejecutar, etc.
 Un conjunto de comandos, donde un comando cuenta con una parte condicional y una principal. La condicional prueba la presencia de ciertos derechos en la matriz de acceso, si la prueba es exitosa la parte principal se ejecuta realizando una serie de operaciones primitivas que cambian la configuración de protección. Las operaciones primitivas crean y destruyen objetos y sujetos, añaden o borran derechos en la matriz de acceso.

El modelo HRU mejora la seguridad puesto que verifica si realmente se trata de un sujeto autorizado y contempla que un cambio en la matriz de acceso no permite a sujetos no autorizados obtener derechos.

Otros rasgos del modelo de la matriz de acceso aparecen en diferentes versiones del modelo de la matriz de acceso:

 Transferencia de derechos: en algunos sistemas los sujetos pueden recibir derechos que son transferibles. Esta transferencia es descrita como una copia de bandera, si dicha copia se añade a un derecho en una celda en la columna *o*, escogiendo si se puede o no copiar la bandera también.
 Monitor de referencia: algún mecanismo que monitorea todos los accesos a los recursos. Este mecanismo asegura que cada acceso sea autorizado por la matriz
 Petición y decisión de acceso: una petición es el evento sobre el cual el monitor de referencia interviene. Esto es, el sujeto *s* pide acceso de tipo *r* sobre el objeto *o*. La decisión permite o niega la petición o la convierte en otra petición. En este punto, otros elementos deben ser tomados en cuenta:

 Reglas de validación de acceso: especifican cómo el monitor de referencia decide el destino de la petición, es decir, como realiza la decisión
 Reglas de autorización: especifican cómo la matriz de acceso puede ser modificada.

 Véase también
 Modelo Bell-LaPadula
 Modelo Clark-Wilson
 Modelo Take-Grant

 Bibliografía
 López Barrientos, M. J., & Quezada Reyes, C. (2006). Fundamentos de Seguridad Informática. México: UNAM, Facultad de Ingeniería.
