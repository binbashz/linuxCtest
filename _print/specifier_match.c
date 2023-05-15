#include "main.h"
/**
 * format_specifier - Selects correct function
 * @list: Arguments
 * @spec: Character corresponding to printf specifier (format[i + 1])
 * Return: Pointer to selected function or length of string printed
*/


int format_specifier(va_list list, char spec)
{
	specifier_t caracter[] = {
		{"c", print_c},
		{"s", print_s},
		{"d", print_d},
		{"i", print_i},
		{"%", print_p},
		{NULL, NULL}
	};	/* prototypes in main.h*/

	int i = 0;

	while (caracter[i].op && spec)
	{	/*check that spec matches the functions*/
		if (caracter[i].op[0] == spec)
	{	/* if there is a coincidence, take the correct function */
		return ((caracter[i].f)(list));
	}
	i++;
}
	_putchar('%'); /* if not match, print '%' and spec */
	_putchar(spec);

	return (2); /* return lenght 2 character printed */
}
