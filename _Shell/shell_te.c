#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_LINE 80 // Máxima longitud de línea de comando
#define MAX_ARGS 10 // Máximo número de argumentos de la línea de comando

int main() {
    char *args[MAX_ARGS]; // Arreglo para almacenar los argumentos de la línea de comando
    char line[MAX_LINE]; // Arreglo para almacenar la línea de comando ingresada por el usuario

    while (1) {
        printf(">> "); // Imprime el indicador de la shell para solicitar al usuario que ingrese una línea de comando

        fgets(line, MAX_LINE, stdin); // Lee la línea de comando ingresada por el usuario desde la entrada estándar y la almacena en el arreglo line

        // Reemplazamos el carácter de nueva línea con el carácter nulo para eliminarlo
        if (line[strlen(line) - 1] == '\n') {
            line[strlen(line) - 1] = '\0';
        }

        // Separamos la línea de comando en argumentos individuales
        char *token = strtok(line, " "); // Utilizamos la función strtok para separar la línea de comando en argumentos individuales utilizando el espacio como delimitador
        int i = 0;

        while (token != NULL && i < MAX_ARGS - 1) { // Recorremos cada argumento y los almacenamos en el arreglo args
            args[i++] = token;
            token = strtok(NULL, " ");
        }

        args[i] = NULL; // Establecemos el último elemento del arreglo args como nulo, lo que indica el final de la lista de argumentos

        // Ejecutamos el comando ingresado por el usuario
        pid_t pid = fork(); // Creamos un proceso hijo utilizando la función fork

        if (pid == 0) { // Si el valor de pid es cero, significa que estamos en el proceso hijo
            // Este es el proceso hijo, ejecutamos el comando ingresado por el usuario
            execvp(args[0], args); // Utilizamos la función execvp para ejecutar el comando ingresado por el usuario. El primer argumento es el nombre del comando y el segundo argumento es un arreglo que contiene los argumentos del comando

            // Si llegamos a este punto, significa que la ejecución falló
            printf("Error to exe command.\n");
            exit(1);
        } else if (pid < 0) { // Si el valor de pid es negativo, significa que ha ocurrido un error al crear el proceso hijo
            printf("Error to create child pid.\n");
            exit(1);
        } else {
            // Este es el proceso padre, esperamos a que el proceso hijo termine
            wait(NULL); // Utilizamos la función wait para esperar a que el proceso hijo termine y evitar que la shell imprima otro indicador de entrada antes de que el proceso hijo termine
        }
    }

    return 0;
}
