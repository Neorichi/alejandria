---
type: Artículo de enciclopedia
title: Criptovirología
description: La criptovirología es la rama de la informática que se encarga del estudio del uso de la criptografía empleado en la creación de software malicioso.
resource: https://es.wikipedia.org/wiki/Criptovirología
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptovirología"}
license: CC BY-SA 4.0
id: eswiki-Criptovirología
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptovirología

La **criptovirología** es la rama de la informática que se encarga del estudio del uso de la criptografía empleado en la creación de software malicioso. El nacimiento de esta rama de la informática se basó en la observación de como la criptografía asimétrica es utilizada para romper la simetría entre lo que ve un analista desarrollador de antivirus y lo que ve el autor de los virus. El analista desarrollador de antivirus solo llega a ver la clave pública mientras que el autor del virus tiene acceso a la clave pública y a la clave privada. El primer ataque que se identificó en esta rama de estudio se llama “Extorsión Criptoviral” (inglés: *cryptoviral extortion*). En este tipo de ataques, un virus, gusano o troyano cifra los archivos de la víctima y la extorsiona con el fin de que pague una suma de dinero al creador del programa malicioso responsable quien le enviaría la clave necesaria para poder descifrar la información perdida.

 Información en general

La **criptovirología** se originó en espacios académicos. Sin embargo, los expertos en el tema expandieron el área de estudio de esta rama incluyendo el análisis de algoritmos criptográficos utilizado por los programadores de Malware, ataques automatizados como *X-raying* y el análisis de los cifradores de los virus y los compresores(Inglés: *packers*).
También se incluyó en esta rama el estudio de técnicas basadas en la criptografía como, por ejemplo, *delayed code*(Inglés: *código demorado*) para dificultar el análisis del código malicioso.

La criptovirología explora cómo se utiliza la criptografía para crear malware potente, a menudo con el fin de ganar dinero. A medida que la tecnología ha mejorado, también lo ha hecho el desarrollo de ataques de criptoransomware más potentes y duraderos. El uso cada vez mayor de criptomonedas como Bitcoin y Monero, que permiten a los ciberatacantes permanecer en el anonimato mientras se benefician del ciberdelito, ha contribuido al aumento de estos criptoataques.

 Historia
El primer ataque de criptovirología y discusión del concepto fue por Adam L. Young y Moti Yung, en su momento llamado "extorsión criptoviral" y fue presentado en la conferencia IEEE Security & Privacy de 1996.En este ataque, un criptovirus (criptogusano o criptotroyano) contiene la clave pública del atacante y cifra de forma híbrida los archivos de la víctima. El malware pide al usuario que envíe el texto cifrado al atacante. Este último lo descifrará y enviará de vuelta la clave de descifrado, a cambio de una cantidad de dinero, como  un rescate.  El documento del IEEE de 1996 predijo que los atacantes de la extorsión criptoviral exigirían algún día dinero electrónico, mucho antes incluso de que existiera Bitcoin. Muchos años después, los medios de comunicación rebautizaron la extorsión criptoviral como ransomware. En 2016, los ataques de criptovirología a proveedores de atención sanitaria alcanzaron niveles epidémicos, lo que llevó al Departamento de Salud y Servicios Humanos de Estados Unidos a publicar una hoja informativa sobre ransomware e HIPAA.

La hoja de datos indica cuando un ransomware cifra la información electrónica protegida sobre la salud, esto se considera una violación. Esto sucede porque el ataque representa una divulgación no autorizada según la HIPAA, ya que un atacante ha tomado el control de la información.

 Ejemplo de los virus que usan criptografía

Si bien es cierto que los virus poseían funciones criptográficas, éstas solo estaban destinadas a evitar la detección de los programas antivirus. Por ejemplo, el virus Tremor utilizaba un código polimórfico como un mecanismo de defensa para evitar ser detectado por un antivirus. Aunque la criptografía ciertamente no contribuye al tiempo de vida de un virus dado, esta tampoco se usa en el *payload* (código ejecutable del virus).

Otro ejemplo es el virus *One-half* que se descubrió como uno de los primeros virus que se encargaba de cifrar los archivos que encontraba. Sin embargo, el virus *One-half* no era un ransomware por lo cual este no pedía ningún tipo de dinero de rescate para el descifrado de los datos que este cifraba y tampoco hacía uso de una clave púbica.
Un ejemplo de estos tipos de virus que si pedían un rescate es el virus *Tro_Ransom.A*. Este virus le pide al usuario del equipo infectado que envíe $10.99 a una cuenta mediante Western Union.
El virus Win32.Gpcode.ag es un virus criptográfico (criptovirus) muy conocido. Este virus usa, en parte, una versión del algoritmo RSA de 660 bits para cifrar archivos de diferentes extensiones. Luego le pide al usuario del equipo infectado que envie un correo electrónico con un ID (un código de letras y números) para obtener en descifrador que recuperaría los archivos previamente cifrados. Si el usuario logra ser contactado por correo electrónico, éste leerá un mensaje que le pedirá una suma de dinero para pagar por el programa descifrador.

Referencias
