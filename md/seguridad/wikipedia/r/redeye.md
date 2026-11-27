---
type: Artículo de enciclopedia
title: RedEye
description: RedEye es un virus que finge encriptar los archivos de un computador para cobrar por su respectivo rescate.
resource: https://es.wikipedia.org/wiki/RedEye
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/RedEye"}
license: CC BY-SA 4.0
id: eswiki-RedEye
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# RedEye

- **Titulo:** RedEye
- **Titulo2:** Ransom.RedEye
- **Tipocabecera:** informática
- **Etiqueta1:** Nombre Técnico
- **Etiqueta2:** Desarrollador
- **Datos2:** iCoreX
- **Etiqueta3:** País de Origen
- **Etiqueta4:** Tipo
- **Datos4:** Troyano y Ransomware
- **Etiqueta5:** Fecha de descubrimiento

**RedEye** es un virus que finge encriptar los archivos de un computador para cobrar por su respectivo rescate. Fue desarrollado por la misma persona que hizo Anabelle y Jigsaw.

Interfaz

Al ejecutar RedEye por primera vez el sistema operativo se reinicia inmediatamente sin consentimiento del usuario, esto lo hace para consolidar su control sobre el computador y poder ejecutar su software malicioso. Cuando el PC finaliza el reinicio se puede observar la interfaz de RedEye.

La interfaz muestra la IP del computador, la ID del usuario, el tiempo restante, un selector de idioma, el dinero recibido, el botón para chequear el pago y la dirección de bitcoin a pagar junto con un menú en el cual están las opciones "hogar", "archivos encriptados", "archivos desencriptados", "soporte" y  "destruir PC", cada una con sus correspondientes funciones.

En ella (interfaz) se destaca el siguiente mensaje:

¡Todos sus archivos personales han sido encriptados con una clave muy fuerte por RedEye!(Rijndael-Algoritmo – AES – 256 Bit)

La única manera de recuperar su archivos es:

**Diríjase a http://redeye85x9tbxiyki.onion/tbxlyki**
**Ingrese su ID personal y pague 0.1 bitcoins**
**Después da clic en "chequear pago".**
**Entonces recibirá una contraseña especial para desbloquear su computador**

**Tienes cuatro días, si no pagas a tiempo tu PC será destruida por completo.**

¿Cómo actúa?

RedEye para evitar su detención, somete al usuario y lo obliga a pagar, también oculta la barra de tareas, elimina los puntos de restauración del sistema, carga contenido audiovisual intimidante, y amenaza diciendo que si no se cumple el tiempo límite de pago (cuatro días) destruirá el sistema operativo.

Si el usuario da los 0.1 bitcoins (700 €) que el malware solicita, este no le restaurará los archivos.

Es un malware muy engañoso ya que finge ser un ransomware que ha secuestrado los archivos del PC, pero en realidad este sólo los reemplaza por ficheros falsos (vacíos), estos últimos llevan el mismo nombre de los originales y sólo se diferencian en su extensión ".RedEye".

Método de eliminación

Desafortunadamente los archivos no podrán ser recuperados salvo que se haya guardado una copia de restauración del sistema en una unidad de almacenamiento externa con anterioridad.

Para eliminar el malware se puede instalar un Antivirus, en caso de que RedEye impida la instalación de este se puede entrar en la restauración del sistema, acceder a la opción "modo seguro con solicitud de comando", digitar "cd restore", es necesario insertar un disco externo con una copia del sistema en el PC, y escribir "rstrui.exe" para que el programa de restauración se abra y poder restaurar el computador a una versión posterior al virus. Si la PC muestra la pantalla de la muerte y se desea recuperarla se puede cambiar de disco duro.

Referencias

 https://bartblaze.blogspot.com/2018/06/redeye-ransomware-theres-more-than.html. *Blaze's Security Blog (inglés). 6 de junio de 2018*
 https://www.malwarerid.com/malwares/redeye-ransomware. *Malwarerid. 14 de junio de 2018*
 https://www.2-viruses.com/remove-redeye-ransomware. *Viruses 2 (inglés). 11 de junio de 2018*
 https://tomassierra.com/redeye-el-ransomware-que-destruye-archivos/. *Tomás Sierra. 7 de junio de 2018*
 https://www.pcrisk.com/removal-guides/12884-redeye-ransomware. *PCrisk (inglés). 7 de junio de 2018*
 https://sensorstechforum.com/es/remove-redeye-ransomware-virus-restore-redeye-files/. *Sensors tech forum. 7 de junio de 2018*
