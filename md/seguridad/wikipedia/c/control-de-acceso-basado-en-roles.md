---
type: Artículo de enciclopedia
title: Control de acceso basado en roles
description: "En la seguridad de los sistemas informáticos, el control de acceso basado en roles (RBAC, por sus siglas en inglés) o seguridad basada en roles es un enfoque para restringir el acceso al sistema a usuarios autorizados y …"
resource: https://es.wikipedia.org/wiki/Control_de_acceso_basado_en_roles
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Control_de_acceso_basado_en_roles"}
license: CC BY-SA 4.0
id: eswiki-Control_de_acceso_basado_en_roles
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Control de acceso basado en roles

En la seguridad de los sistemas informáticos, **el control de acceso basado en roles** (**RBAC**, por sus siglas en inglés)   o **seguridad basada en roles** es un enfoque para restringir el acceso al sistema a usuarios autorizados y para implementar un control de acceso obligatorio (MAC) o control de acceso discrecional (DAC).

El control de acceso basado en roles es un mecanismo de control de acceso neutral en cuanto a políticas, definido en torno a roles y privilegios. Los componentes de RBAC, como los permisos por rol, y las relaciones entre usuarios y roles, facilitan la asignación de usuarios. Un estudio realizado por el Instituto Nacional de Estándares y Tecnología (NIST) ha demostrado que RBAC satisface muchas necesidades de organizaciones comerciales y gubernamentales. RBAC se puede utilizar para facilitar la administración de la seguridad en grandes organizaciones con cientos de usuarios y miles de permisos. Aunque RBAC es diferente de los marcos de control de acceso MAC y DAC, puede hacer cumplir estas políticas sin ninguna complicación.

 Diseño
Dentro de una organización, se crean roles para diversas funciones laborales. Los permisos para realizar determinadas operaciones se asignan a roles específicos. Dado que los usuarios no reciben permisos directamente, sino que sólo los adquieren a través de su rol (o roles), la gestión de los derechos de los usuarios individuales se reduce a asignar los roles apropiados a la cuenta del usuario; lo que simplifica las operaciones comunes como agregar un usuario o cambiarle de departamento.

Se definen tres reglas principales para RBAC:

 Asignación de roles: un sujeto puede ejercer un permiso solo si ha seleccionado o se le ha asignado un rol.
 Autorización de roles: el rol activo de un sujeto debe estar autorizado para el sujeto. Junto con la regla 1, esta regla garantiza que los usuarios solo puedan asumir roles para los que están autorizados.
 Autorización de permisos: un sujeto puede ejercer un permiso solo si el permiso está autorizado para el rol activo del sujeto. Junto con las reglas 1 y 2, esta regla garantiza que los usuarios solo puedan ejercer permisos para los que están autorizados.

También pueden aplicarse restricciones adicionales, y los roles se pueden combinar en una jerarquía donde los roles de nivel superior incluyen los permisos de los sub-roles.

Con los conceptos de jerarquía de roles y restricciones, se puede controlar RBAC para crear o simular el control de acceso basado en redes (LBAC). Por tanto, puede considerarse que RBAC es un superconjunto de LBAC.

Convenciones utilizadas en el modelo RBAC

Al definir un modelo RBAC, las siguientes convenciones son útiles:

 S = Sujeto = Una persona o agente automatizado
 R = Rol = Función laboral o título que define un nivel de autoridad
 P = Permisos = Aprobación de un modo de acceso a un recurso
 SE = Sesión = Un mapeo que involucra S, R y/o P
 SA = Asignación de sujetos
 PA = Asignación de permisos
 RH = Jerarquía de roles parcialmente ordenada. RH también se puede escribir: ≥ (La notación: x ≥ y significa que x hereda los permisos de y).
 Un sujeto puede tener múltiples roles.
 Un rol puede tener múltiples sujetos.
 Un rol puede tener muchos permisos.
 Se puede asignar un permiso a muchos roles.
 A una operación se le pueden asignar muchos permisos.
 Se puede asignar un permiso a muchas operaciones.

Una restricción impone una regla restrictiva sobre la posible herencia de permisos de roles opuestos, logrando así una adecuada separación de funciones. Por ejemplo, no se debe permitir que la misma persona cree una cuenta de inicio de sesión y que autorice la creación de la cuenta.

Utilizando la notación de la teoría de conjuntos:

  y es una relación de muchos a muchos para asignación de permisos a roles.
  y es una relación de muchos a muchos para asignación de sujetos a roles.

Un sujeto puede tener *múltiples* sesiones simultáneas con diferentes roles.
 Niveles estandarizados de RBAC
El estándar NIST/ANSI/INCITS RBAC (2004) reconoce tres niveles de RBAC:

 RBAC básico
 RBAC jerárquico: Añade soporte para la herencia entre roles
 RBAC restringido: Añade separación de funciones

 Relación con otros modelos
RBAC es una tecnología de control de acceso flexible cuya flexibilidad permite implementar DAC  o MAC.  DAC con grupos (por ejemplo, como se implementa en sistemas de archivos POSIX) puede emular RBAC.  MAC puede simular RBAC si el gráfico de roles se restringe a un árbol en lugar de a un conjunto parcialmente ordenado.

Antes del desarrollo de RBAC, el modelo Bell-LaPadula (BLP) era sinónimo de MAC y los permisos del sistema de archivos eran sinónimo de DAC. Estos se consideraban los únicos modelos conocidos de control de acceso: si un modelo no era BLP, se consideraba un modelo DAC, y viceversa. La investigación a finales de la década de 1990 demostró que RBAC no se encuentra en ninguna de estas categorías.  A diferencia del control de acceso basado en contexto (CBAC), RBAC no analiza el contexto del mensaje (como el origen de una conexión). RBAC también ha sido criticado por conducir a una explosión de roles,  un problema en los sistemas empresariales grandes que requieren un control de acceso de granularidad más fina que el que RBAC puede proporcionar, ya que los roles están inherentemente asignados a operaciones y tipos de datos. Similar al CBAC, un sistema de control de acceso basado en entidad-relación (ERBAC, aunque el mismo acrónimo también se utiliza para sistemas RBAC modificados,  como el Control de Acceso Basado en Roles Extendido ) es capaz de proteger instancias de datos considerando su asociación al sujeto ejecutor.

 Comparación con las Listas de Control de Acceso (ACL)
Las listas de control de acceso (ACL) se utilizan en sistemas de control de acceso discrecional (DAC) tradicionales para afectar objetos de datos de bajo nivel. RBAC se diferencia de ACL en asignar permisos a operaciones que cambian las relaciones directas entre varias entidades (ver: *ACLg* a continuación). Por ejemplo, una ACL podría usarse para conceder o denegar acceso de escritura a un archivo del sistema en particular, pero no dictaría cómo podría cambiarse ese archivo. En un sistema basado en RBAC, una operación podría consistir en "crear una cuenta de crédito" en una aplicación financiera o "registrar un nivel de azúcar en sangre" en una aplicación médica. Por tanto, un rol es una secuencia de operaciones dentro de una actividad más amplia. Se ha demostrado que RBAC es particularmente adecuado para los requisitos de separación de funciones (SoD), que garantizan que dos o más personas deben participar en la autorización de operaciones críticas. Se han analizado las condiciones necesarias y suficientes para la seguridad de SoD en RBAC. Un principio subyacente de SoD es que ningún individuo debería poder violar la seguridad mediante un doble privilegio. Por extensión, ninguna persona puede tener un rol que ejerza autoridad de auditoría, control o revisión sobre otro rol que ocupe simultáneamente.

Un "modelo RBAC mínimo", *RBACm*, se puede comparar con un mecanismo de ACL, *ACLg*, donde solo se permiten grupos como entradas en la ACL. Barkley (1997)  demostró que *RBACm* y *ACLg* son equivalentes.

En las implementaciones modernas de SQL, como la ACL del marco CakePHP, las ACL también gestionan grupos y herencia en una jerarquía de grupos. Bajo este aspecto, las implementaciones específicas de "ACL moderno" se pueden comparar con implementaciones específicas de "RBAC moderno", mejor que las implementaciones "antiguas" (del sistema de archivos).

Para el intercambio de datos y para "comparaciones de alto nivel", los datos de ACL pueden traducirse a XACML.

 Control de acceso basado en atributos
El control de acceso basado en atributos o ABAC es un modelo que evoluciona desde RBAC para considerar atributos adicionales además de roles y grupos. En ABAC, es posible utilizar atributos de:

 el usuario, por ejemplo, ciudadanía, autorización,
 el recurso, por ejemplo, clasificación, departamento, propietario,
 la acción, y
 el contexto, por ejemplo, tiempo, ubicación, IP.

ABAC está basado en políticas en el sentido de que utiliza políticas en lugar de permisos estáticos para definir qué está permitido y qué no.

 Control de acceso basado en relaciones
El control de acceso basado en relaciones o ReBAC es un modelo que evoluciona desde RBAC. En ReBAC, el permiso de un sujeto para acceder a un recurso se define por la presencia de relaciones entre esos sujetos y recursos.

La ventaja de este modelo es que permite permisos de gran precisión. Por ejemplo, en una red social donde los usuarios pueden compartir publicaciones con otros usuarios específicos.

 Uso y disponibilidad
El uso de RBAC para gestionar privilegios de usuario (permisos informáticos) dentro de un único sistema o aplicación es ampliamente aceptado como una buena práctica. Un informe de 2010 preparado para NIST por el Research Triangle Institute analizó el valor económico de RBAC para las empresas y estimó los beneficios por empleado de la reducción del tiempo de inactividad de los empleados, un aprovisionamiento más eficiente y una administración de políticas de control de acceso más eficiente.

En una organización con una infraestructura de TI heterogénea y requisitos que abarcan docenas o cientos de sistemas y aplicaciones, el uso de RBAC para gestionar suficientes roles y asignar membresías de rol adecuadas se vuelve extremadamente complejo sin la creación jerárquica de roles y asignaciones de privilegios.  Los sistemas más recientes amplían el modelo NIST RBAC anterior  para abordar las limitaciones de RBAC para implementaciones en toda la empresa. El modelo NIST fue adoptado como estándar por INCITS como ANSI/INCITS 359-2004. También se ha publicado un análisis de algunas de las opciones de diseño del modelo NIST.

 Vulnerabilidades potenciales
La interferencia del control de acceso basado en roles es un problema relativamente nuevo en las aplicaciones de seguridad, donde múltiples cuentas de usuario con niveles de acceso dinámicos pueden conducir a la inestabilidad en la clave de cifrado, permitiendo que un usuario externo aproveche la debilidad del acceso no autorizado. Las aplicaciones para compartir claves dentro de entornos virtualizados dinámicos han mostrado cierto éxito al abordar este problema.

 Véase también

 Referencias

 Enlaces externos

 Preguntas frecuentes sobre modelos y estándares RBAC
 Controles de acceso basados en roles en NIST
 Perfil de control de acceso basado en roles jerárquicos y centrales XACML
 Instituto de Seguridad Cibernética de la Universidad de Texas San Antonio
 Experiencias prácticas en la implementación de RBAC
