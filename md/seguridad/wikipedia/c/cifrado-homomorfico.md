---
type: Artículo de enciclopedia
title: Cifrado homomórfico
description: "Se dice que un sistema de cifrado es homomórfico si es capaz de realizar una operación algebraica concreta sobre un texto original, equivalente a otra operación algebraica (no necesariamente la misma) sobre el resultado …"
resource: https://es.wikipedia.org/wiki/Cifrado_homomórfico
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_homomórfico"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_homomórfico
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado homomórfico

Se dice que un sistema de cifrado es **homomórfico** si es capaz de realizar una operación algebraica concreta sobre un texto original, equivalente a otra operación algebraica (no necesariamente la misma) sobre el resultado cifrado de ese texto original. De esta manera, si se realizan operaciones sobre datos cifrados, y posteriormente se descifra el resultado, se obtendrá lo mismo que si se realizan operaciones equivalentes sobre los datos originales.

Formalización
Si:
 representa la función de cifrado
 representa la función de descifrado

 representa una operación algebraica sobre el texto original.
 representa la operación equivalente a  en el texto cifrado.

Un cifrado es homomórfico si y solo si se cumple la igualdad:

Es importante recalcar que  puede ser igual o diferente que .

Simplificando un poco la notación se podría decir que si:
 representa la función de cifrado del texto  usando el valor aleatorio
El operador  representa la operación binaria *producto*
El operador  la operación binaria *suma*.
Un cifrado es homomórfico si y solo si se cumple la igualdad:

Aplicaciones
Esta característica es deseable en las arquitecturas de sistemas de comunicación actuales. El cifrado homomórfico permitiría encadenar entre sí diferentes servicios sin necesidad de exponer los datos de cada uno de los servicios, por ejemplo: una cadena de servicios independientes de diversas empresas podrían: 1) calcular la tasa impositiva, 2) el tipo de cambio y 3) el envío de una operación comercial, sin exponer los datos de cada uno de los servicios involucrados en la operación completa. Los sistemas de cifrado homomórfico son criptográficamente maleables por diseño. La propiedad homomórfica de algunos sistemas criptográficos o criptosistemas puede utilizarse para desarrollar sistemas de votación seguros, funciones resumen anticolisión, sistemas de recuperación de información privada, y permitir el uso generalizado de la computación en nube, garantizando la confidencialidad de los datos procesados.

 Sistemas criptográficos parcialmente homomórficos
Un sistema de cifrado que es homomórfico en la suma o en el producto se dice que es parcialmente homomórfico. En los siguientes ejemplos, la notación  se usa para representar el cifrado del mensaje .

 RSA sin relleno
En el sistema criptográfico RSA, dada cierta clave pública definida como el módulo  y el exponente , entonces el cifrado de un mensaje  se expresa como: . La propiedad homomórfica viene dada por la expresión:

 ElGamal

En el sistema criptográfico ElGamal, dado un grupo  con clave pública , donde , y  representa la clave privada, el cifrado de un mensaje  se expresa como: , para un  aleatorio. La propiedad homomórfica viene dada por la expresión:

 Goldwasser-Micali
En el sistema criptográfico Goldwasser-Micali, dada cierta clave pública definida como el módulo  y la cuadrática no residual , entonces el cifrado de un bit  se expresa como: , para un  aleatorio. La propiedad homomórfica viene dada por la expresión:

donde  denota la suma de módulo 2 o suma binaria (XOR).

 Benaloh
En el sistema criptográfico Benaloh, dada cierta clave pública definida como el módulo  y la base , con un tamaño de bloque , entonces el cifrado del mensaje  se expresa como: , para un  aleatorio. La propiedad homomórfica viene dada por la expresión:

 Paillier
En el sistema criptográfico Paillier, dada cierta clave pública definida como el módulo  y la base , entonces el cifrado de un mensaje  se expresa como: , para un  aleatorio. La propiedad homomórfica viene dada por la expresión:

 Otros sistemas criptográficos parcialmente homomórficos
 Criptosistema Okamoto–Uchiyama
 Criptosistema Naccache–Stern
 Criptosistema Damgård–Jurik
 Criptosistema Boneh–Goh–Nissim

 Cifrado totalmente homomórfico
Un sistema de cifrado homomórfico que soporta tanto la suma como el producto (preservando así la estructura en anillo de los textos origen) se conoce como cifrado totalmente homomórfico, también conocido por las siglas FHE (del inglés *fully homomorphic encryption*). Se han descrito sistemas completamente homomórficos pero todavía no son lo suficientemente rápidos para poder ser usados en aplicaciones reales.

Utilizando este tipo de esquemas, cualquier circuito puede ser homomorficamente evaluado, lo que permite la construcción de programas que pueden procesar datos cifrados de entrada y producir datos cifrados de salida. Puesto que estos programas nunca descifran los datos de entrada, pueden ejecutarse en equipos no confiables sin necesidad de revelar los datos de entrada y su estado interno. La existencia de un sistema criptográfico eficiente y completamente homomórfico tendría grandes implicaciones prácticas en la externalización de sistemas de cómputo privados, por ejemplo, en el contexto de la computación en nube (cloud computing).

La cualidad homomórfica, de un sistema completamente homomórfico, también puede ser descrita por la teoría de categorías. De esta manera, si  es la categoría de objetos que representa ciertos números enteros (es decir, flujos finitos de datos) cuyos morfismos son funciones computables, entonces (idealmente) en un sistema completamente homomórfico, la función de cifrado, equivale a un functor desde  hacia sí mismo.

La utilidad del cifrado completamente homomórfico está manifiestamente reconocida desde hace tiempo. El problema de implementar tal sistema fue propuesto por primera vez durante el año en que se estaba desarrollando el algoritmo RSA. La solución fue más difícil de alcanzar, durante más de 30 años se estuvo trabajando en este problema, y no estaba claro si el cifrado completamente homomórfico llegaría a ser posible. Durante este periodo de tiempo, la mejor aproximación fue el sistema criptográfico Boneh-Goh-Nissim, que permitía la evaluación de un número ilimitado de operaciones de suma, pero a lo sumo una multiplicación.

En el año 2009, el estudiante de la Universidad de Stanford Craig Gentry, mientras trabajaba en su tesis doctoral y hacía prácticas en el centro de investigación de IBM, propone el primer sistema de cifrado completamente homomórfico capaz de evaluar circuitos de profundidad arbitraria, usando criptografía basada en retículos, según anunciaba la compañía IBM en junio de 2009.

El trabajo de Craig parte de un sistema de cifrado genérico, parcialmente homomórfico, y que se limita a evaluar polinomios de bajo grado sobre datos cifrados, usando retículos ideales. Esta limitación se debe a que cada texto cifrado contiene *ruido*, dicho ruido aumenta a medida que se suman y multiplican textos cifrados, hasta que finalmente el texto cifrado resultante se hace indescifrable. A continuación, el trabajo de Craig, muestra como modificar ligeramente el sistema de cifrado para que sea capaz de evaluar su propio circuito de descifrado, y establece que dicho sistema modificado se puede transformar en un sistema de cifrado genérico completamente homomórfico, dicho sistema se conoce como esquema de cifrado autoevaluado. Por último, demuestra que cualquier sistema de cifrado homomórfico autoevaluado puede convertirse en un sistema de cifrado completamente homomórfico, a través de un proceso recursivo autocontenido. En el caso particular de los sistemas homomórficos de Craig, basados en retículos ideales, el procedimiento autoevaluado regenera de manera efectiva el texto cifrado, reduciendo el ruido asociado, de modo que los textos cifrados pueden sumarse y multiplicarse sin riesgo de que el texto cifrado resultante sea indescifrable. Craig fundamenta la seguridad de su sistema en la supuesta dificultad de dos problemas: ciertos problemas del *peor caso* en retículos ideales, y la escasa influencia del problema de la suma de subconjuntos.

En cuando al rendimiento, los textos cifrados con el sistema de Craig conservan su tamaño, dado que éste no depende en absoluto de la complejidad de la función que se evalúa sobre el texto cifrado, y el tiempo de cálculo depende linealmente del número de operaciones ejecutadas. Sin embargo, en gran cantidad de aplicaciones, el sistema no tiene utilidad debido a que el tamaño del texto cifrado, y el tiempo requerido para el cálculo, aumentan bruscamente si aumenta el nivel de seguridad. Para obtener un nivel de seguridad  contra  ataques conocidos, el tiempo de cálculo y el tamaño del texto cifrado son polinomios de alto grado en . Stehle y Steinfeld consiguen reducir sustancialmente la dependencia de , por medio de mejoras que permiten que el cálculo sea casi  por cada operación booleana de la función que se está evaluando.

Además del trabajo expuesto en su tesis doctoral, Craig Gentry publicó en la edición de marzo de 2010 de la revista *Comunicaciones de la ACM* (en inglés: *Communications of the ACM*), un análisis sobre un sistema de cifrado propuesto por Marten Van Dijk. En el trabajo de Van Dijk, publicado en 2009 junto con Craig Gentry, Shai Halevi y Vinod Vaikuntanathan, se propone otro sistema de cifrado completamente homomórfico basado en el de Craig, pero que no requiere el uso de retículos ideales. En lugar de partir del sistema de cifrado parcialmente homomórfico de Craig, basado en retículos ideales, se parte de un sistema más simple basado en números enteros. El sistema es conceptualmente más simple que el de Craig, pero tiene propiedades similares en cuanto a homomorfísmo y eficiencia. El componente parcialmente homomórfico al que se hace referencia en el trabajo de Van Dijk es similar otro sistema de cifrado propuesto por Levieil y Naccache en 2008, y también a un sistema propuesto por Bram Cohen en 1998. Sin embargo, el método de Cohen ni tan siquiera permite la operación de suma de manera homomórfica. El sistema Levieil-Naccache permite la operación de suma de manera homomórfica, y puede ser modificado para soportar un número limitado de multiplicaciones.

 Implementaciones
En 2009, Riggio y Sicari dieron a conocer una aplicación práctica de cifrado homomórfico para una red de comunicaciones inalámbrica de arquitectura híbrida: en este caso de sensores (WSN) y en malla (WMN). El sistema permite múltiples envíos de datos entre nodos, de manera transparente, que son capaces de realizar análisis estadísticos de diferentes parámetros (temperatura, humedad, etc.) procedentes de una WSN y garantizando al mismo tiempo tanto el cifrado como la autenticación entre nodos.

En 2010, Nigel P. Smart y Frederik Vercauteren presentaron una versión refinada del sistema de Craig, que proporcionaba claves y tamaños de textos cifrados más reducidos, pero que no era totalmente práctico. En la última sesión de Eurocrypt 2010, Craig Gentry y Shai Halevi presentaron una implementación funcional de un sistema de cifrado completamente homomórfico (es decir, el procedimiento completo autoevaluación) junto con las estadísticas de rendimiento

En 2012, Coron, Naccache y Tibouchi propusieron una técnica que permitía reducir el tamaño de la clave pública del sistema de Van Dijk a 600 KB. En abril de 2013, IBM liberó en GitHub la primera versión de HElib, una librería que implementa el sistema de cifrado homomórfico de Brakerski, Gentry y Vaikuntanathan (BGV), escrita en lenguaje C++ y bajo licencia GNU GPL.

 Hacia aplicaciones de Internet totalmente seguras
Los principios en los que se fundamenta el cifrado homomórfico pueden servir como punto de partida para mejorar los sistemas de seguridad (o aplicaciones) que almacenan y manipulan datos de carácter personal o sensibles. Esta garantía de protección deriva de la capacidad, que tiene el sistema de cifrado homomórfico, de realizar operaciones aritméticas sobre datos cifrados. Basándose en un sistema de cifrado completamente homomórfico, Youssef Gahi desarrolló el esquema básico, y el diseño de unos circuitos genéricos, fácilmente adaptables, que pueden preservar de manera efectiva la privacidad y confidencialidad entre diversos sistemas o aplicaciones. El modelo propuesto por Gahi, acepta datos de entrada cifrados y luego los procesa en función de las directrices marcadas por el usuario, sin llegar a descifrarlos nunca, y ofreciendo la garantía de que sólo el usuario que solicitó el procesado de los datos tiene la capacidad de descifrarlos. De esta manera, el sistema permite a los clientes utilizar determinados servicios, ofrecidos por aplicaciones o sistemas remotos, con la confianza de que no existe riesgo de que sus datos sean revelados, incluso cuando los servidores sean de dudosa reputación.

 Véase también
 Homomorfismo

 Referencias

 Notas

 Enlaces externos
 Homomorphic encryption en Cryptology Pointers
 The Homomorphic Encryption Project
 The Open Source hcrypt Project
 American Scientist article
 HElib - Librería de cifrado homomórfico escrita en C++ bajo licencia GNU GPL
 Translucent Database - Una arquitectura basada en estos principios.
