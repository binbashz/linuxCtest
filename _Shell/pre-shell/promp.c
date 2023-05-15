#include <stdio.h>
#include <stdlib.h>

#define MAX_INPUT_LENGTH 1024  /* Maximum length of user input */

int main() {
    char *input = NULL;   /* Pointer to store user input */
    size_t input_size = 0;  /* Size of user input */
    ssize_t input_length;  /* Length of user input */

    while (1) {
        printf("My_Shell> ");  /* Print the prompt for the mini shell */

        input_length = getline(&input, &input_size, stdin);  /* Read user input */

        if (input_length == -1) {
            /* If getline() returns -1, it means there was an error or reached EOF */
            printf("Error reading user input\n");
            break;
        }

        /* Remove the newline character (\n) from the end of the input line */
        if (input[input_length - 1] == '\n') {
            input[input_length - 1] = '\0';
        }

        /* Here you can process the user input, execute commands, etc. */
        /* ... */
    }

    free(input);  /* Free the memory allocated by getline() */

    return 0;
}

