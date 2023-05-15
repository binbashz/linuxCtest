



MINI SHELL 


Analizar la entrada del usuario: Implementa la lógica para analizar la entrada del usuario y dividirla en comandos y argumentos. Puedes usar funciones de manipulación de cadenas en C,
 como strtok() y strcmp(), para dividir y comparar cadenas.

Implementar la ejecución de comandos: Utiliza la función execve() o sus variantes, como execvp() o execv(), para ejecutar comandos en un proceso hijo. 
Asegúrarse de manejar adecuadamente la creación, espera y finalización de procesos hijos.

Manejar la redirección y tuberías: Implementa la funcionalidad para redireccionar la entrada/salida de los comandos, así como para crear tuberías (pipes) para la comunicación entre comandos.

Implementar la gestión de procesos: Añade la capacidad de administrar procesos en segundo plano (background) y en primer plano (foreground),
 así como manejar señales y eventos relacionados con los procesos, como la terminación y suspensión de procesos.

Implementar variables y entorno: Agrega la capacidad de manejar variables de entorno, como las variables de entorno estándar ($HOME, $PATH, etc.), así como variables específicas de la shell.

Manejar errores y mensajes de usuario: Asegúrate de manejar adecuadamente los errores, como comandos no encontrados, errores de sintaxis, etc.,
 y proporcionar mensajes de usuario adecuados para ayudar en la interacción con el usuario.

Implementar características adicionales: Puedes agregar otras características avanzadas, como la auto-completación de comandos, el historial de comandos,
 la personalización del prompt, y más, según tus necesidades y objetivos.
