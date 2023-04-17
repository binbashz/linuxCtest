## Task 0

0.getppid.sh


Este es un script de shell simple que imprime el PID del proceso padre utilizando la variable de entorno $PPID. Aquí está la explicación línea por línea:

#!/bin/bash: Esta es la línea de shebang, que indica el intérprete de shell a utilizar para ejecutar el script. En este caso, se está utilizando el intérprete de shell bash.

pid_padre=$PPID: Esta línea asigna el valor de la variable de entorno $PPID a la variable de shell pid_padre. La variable de entorno $PPID contiene el PID del proceso padre del proceso actual.

echo "PID del proceso padre: $pid_padre": Esta línea imprime el valor de la variable pid_padre, que contiene el PID del proceso padre, utilizando el comando echo.
 El texto "PID del proceso padre: " se muestra como una cadena literal, y el valor de la variable pid_padre se
 imprime usando la notación de variable $pid_padre, que se expande al valor de la variable en tiempo de ejecución.

En resumen, este script de shell obtiene el PID del proceso padre utilizando la variable de entorno $PPID,
 lo asigna a una variable de shell, y luego lo imprime en la salida estándar utilizando el comando echo.


-------------------------------------------------------------------------------------------------------------------------------------------------


## Task 1 

1. /proc/sys/kernel/pid_max

------------------------------------------------------------------------------------------------------------------------------------------------


# Task AV

Los argumentos de la línea de comandos se pasan a través de la función main: int main(int ac, char **av);

av es una matriz de cadenas terminada en NULL
ac es el número de elementos en av
av[0] suele contener el nombre utilizado para invocar el programa actual. av[1] es el primer argumento del programa, av[2] el segundo, y así sucesivamente.

0. av
Write a program that prints all the arguments, without using ac.
#include <stdio.h>

int main(int ac, char **av) {
    int i = 0; // Inicializa una variable entera i con valor 0

    while (av[i]) { // Mientras el elemento av[i] no sea NULL (marcador de fin de array)
        printf("%s ", av[i]); // Imprime el valor del elemento av[i] (argumento)
        i++; // Incrementa el valor de i en 1 para pasar al siguiente elemento del array
    }

    printf("\n"); // Imprime una nueva línea al final
    return 0; // Retorna 0 como indicación de que el programa finalizó correctamente
}



imprime todos los argumentos pasados por línea de comandos utilizando un bucle while y la variable av en lugar de la variable ac. 
El programa recorre el array de argumentos av hasta que encuentra un marcador de fin de array (NULL), imprimiendo cada argumento utilizando la función printf.
 Al final, se imprime una nueva línea y
 se retorna 0 como indicación de que el programa ha finalizado correctamente.




-------------------------------------------------------------------------------------------------------------------------------------------------
## Getline

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char *buffer = malloc(1024); /* Se asigna memoria dinámicamente para el buffer de tamaño 1024 */
	size_t len = 1024; /* Variable que almacena el tamaño del buffer */

	while (1) /* Bucle infinito para mantener el programa en ejecución */
	{
		printf("$ "); /* Imprime "$ " en la pantalla */
		getline(&buffer, &len, stdin); /* Utiliza getline para leer la línea ingresada por el usuario y almacenarla en el buffer */
		printf("%s", buffer); /* Imprime el contenido del buffer, que es el comando ingresado por el usuario */
	}

	return (0); /* Retorna 0 como indicación de que el programa ha finalizado correctamente */
}




Se incluyen las bibliotecas estándar de C stdio.h y stdlib.h necesarias para el uso de funciones de entrada/salida y asignación de memoria dinámica.
La función main es la función principal del programa, que se ejecuta al iniciar el programa.
Se utiliza malloc para asignar memoria dinámicamente al puntero buffer, que se utilizará para almacenar la línea ingresada por el usuario. Se reserva un espacio de 1024 bytes para el buffer.
len es una variable que almacena el tamaño del buffer.
Dentro de un bucle infinito while (1), se imprime "$ " en la pantalla utilizando la función printf para indicar que el programa está esperando un comando.
Luego, se utiliza la función getline para leer la línea ingresada por el usuario desde la entrada estándar (stdin) y almacenarla en el buffer.
Después de leer la línea ingresada por el usuario, se imprime el contenido del buffer utilizando printf y el especificador de formato %s, que indica que se imprimirá una cadena de caracteres.
El programa continuará en este bucle infinito, imprimiendo "$ " en la pantalla,
 leyendo la línea ingresada por el usuario, e imprimiendo el contenido del buffer, hasta que sea interrumpido por el usuario o por alguna otra condición de salida del programa.
Finalmente, se retorna 0 como indicación de que el programa ha finalizado 
