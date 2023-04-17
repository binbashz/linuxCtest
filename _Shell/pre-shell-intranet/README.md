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


--------


 programa en C que imprime "$ ", espera a que el usuario ingrese un comando y luego lo imprime en la siguiente línea utilizando la función 

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	char *buffer = NULL; /* Puntero al buffer que contendrá la línea ingresada por el usuario */
	size_t len = 0; /* Variable que almacenará el tamaño del buffer */
	ssize_t read; /* Variable para almacenar el número de caracteres leídos por getline() */

	while (1) /* Bucle infinito para mantener el programa en ejecución */
	{
		printf("$ "); /* Imprime "$ " en la pantalla */
		fflush(stdout); /* Limpia el búfer de salida para asegurarse de que "$ " se muestre en la pantalla */

		read = getline(&buffer, &len, stdin); /* Utiliza getline para leer la línea ingresada por el usuario y almacenarla en el buffer */

		if (read == -1) /* Si getline devuelve -1, indica un error o el fin del archivo (EOF) */
		{
			printf("\n"); /* Imprime una nueva línea para separar el último comando ingresado del prompt "$ " */
			break; /* Sale del bucle infinito para finalizar el programa */
		}

		printf("%s", buffer); /* Imprime el contenido del buffer, que es el comando ingresado por el usuario */
	}

	free(buffer); /* Libera la memoria asignada dinámicamente para el buffer */
	buffer = NULL; /* Asigna NULL al puntero del buffer para evitar el acceso a memoria no válida */

	return 0; /* Retorna 0 como indicación de que el programa ha finalizado correctamente */
}


Este programa utiliza getline() para leer la línea ingresada por el usuario y almacenarla en el buffer. Luego imprime el contenido del buffer, que es el comando ingresado por el usuario, y repite el proceso en un bucle infinito hasta que se encuentre con un error o el fin del archivo (EOF) indicado por getline(). Es importante leer el manual (man) de la función getline() y tener en cuenta la sección "RETURN VALUE" para saber cuándo detener la lectura de entrada, especialmente en caso de EOF (End-Of-File) que puede ocurrir al presionar Ctrl+D en la terminal.
