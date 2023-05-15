#include "main.h"

/**
 * _printf - Writes output to stdout
 * @format: String to print
 *
 * Return: Number of characters printed
*/

int _printf(const char *format, ...)
{
	int i = 0; /* indice para recorrer el string 'format'*/
	int strlen = 0; /* contador de caracteres */

	va_list list; /* lista de argunmentos variables*/

	va_start(list, format); /* inicializa la lista de argumentos variables, con el ultimo argumento conocido */

	if (format == NULL) /* si el string format es NULL, retorna -1 (error)*/
		return (-1);

	for (i = 0; format[i] != '\0'; i++) /*  Recorre el string "format" hasta el final */
	{
		if (format[i] == '%') /* Si se encuentra un carácter %, se está especificando un formato */
	{
			if (format[i + 1] == '\0') /* Si el siguiente carácter es el final del string, retorna -1 (error) */
			return (-1);

		strlen += format_specifier(list, format[i + 1]); /*  Llama a la función correspondiente para imprimir el argumento */
		i++; /* Avanza una posición adicional para saltar el carácter de formato */
	}
		else

	{
		_putchar(format[i]); /* Si no se está especificando un formato, simplemente imprime el carácter */

		strlen++; /* Aumenta el contador de caracteres impresos */
	}
}
	va_end(list);	/* Finaliza la lista de argumentos variables */
	return (strlen); /* Retorna la cantidad de caracteres impresos */
}
