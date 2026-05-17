Traductor Pseudocodigo a Python — Analizador Léxico  
El analizador léxico escanea el pseudocódigo en español para identificar sus componentes básicos (tokens) utilizando expresiones regulares.
Además, procesa y gestiona los niveles de indentación para estructurar correctamente los bloques de código antes de su transpilación a Python.

Información del Curso

Materia: Sistemas Base 1

Institución: Univerisdad Autonoma de Tamaulipas

Semestre: 8°I 2026-1

Profesor: Muñoz Quintero Dante Adolfo

Integrantes del Equipo

Nombre - 	Matrícula
Posadas Perez Isaac Sayeg - a2213332197
Díaz Rosas Kevin Jesus - a2213332154
Sánchez Morales Sergio Israel - a2213332209
Vega González Jesús Alejandro - a2213339033

Descripción del Lenguaje  
El lenguaje es un pseudocódigo fuertemente estructurado en español, cuyo propósito es facilitar el aprendizaje y la transición de lógica de programación hacia el lenguaje Python. 
Utiliza un sistema de indentación obligatoria para delimitar los bloques de código (sin necesidad de llaves). 
Soporta la declaración de funciones, manejo de estructuras de control clásicas (como si, sino, mientras), operaciones matemáticas, 
relacionales y el uso de tipos de datos básicos como enteros, flotantes y cadenas de texto.

Tokens Reconocidos  
Palabras Reservadas: si, sino_si, sino, mientras, para, en, funcion, retornar, imprimir, leer, inicio, y fin.
Operadores Aritméticos: Suma (+), Resta (-), Multiplicación (*), División (/) y Módulo (%).
Operadores Relacionales y Asignación: Asignación (=), Igual (==), Diferente (!=), Mayor (>), Menor (<), Mayor o igual (>=) y Menor o igual (<=).
Tipos de Dato (Literales): Cadenas de texto encerradas entre comillas (LIT_CADENA), números enteros (LIT_ENTERO) y números con decimales (LIT_FLOTANTE).
Delimitadores: Paréntesis ( ), corchetes [ ] y comas ,.
Identificadores: Nombres para variables o funciones (ID), que deben comenzar con una letra o guion bajo.
Tokens Especiales de Control: Tokens generados dinámicamente para la indentación (TOKEN_INDENT), remoción de indentación (TOKEN_DEDENT), 
fin del archivo (TOKEN_EOF) y detección de errores léxicos (TOKEN_ERROR).

Cómo ejecutar  
Asegúrate de tener Python (versión 3) instalado en tu equipo.

Verifica que los archivos MainProyecto (1).py, ScannerProyecto.py, TokenType.py y Tokens.py (referenciado en el código) se encuentren dentro del mismo directorio.

Abre tu terminal o línea de comandos, navega hasta la carpeta del proyecto y ejecuta el archivo principal con el siguiente comando:

python "MainProyecto (1).py"

Ejemplos de uso  
Entrada esperada (Fragmento extraído del código fuente de prueba):

inicio
    imprimir("Iniciando prueba del scanner")
    leer(numero)
fin

Salida en consola:
El programa imprimirá una tabla listando la línea, el tipo de token y el valor detectado. Para la entrada anterior, el resultado será:

2       | KW_INICIO            | inicio
3       | TOKEN_INDENT         | 4
3       | KW_IMPRIMIR          | imprimir
3       | DEL_PAREN_IZQ        | (
3       | LIT_CADENA           | "Iniciando prueba del scanner"
3       | DEL_PAREN_DER        | )
4       | KW_LEER              | leer
4       | DEL_PAREN_IZQ        | (
4       | ID                   | numero
4       | DEL_PAREN_DER        | )
5       | TOKEN_DEDENT         | 0
5       | KW_FIN               | fin
5       | TOKEN_EOF            | EOF
