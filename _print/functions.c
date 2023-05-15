#include "main.h"
#include <unistd.h>

/**
 * _putchar - writes the character c to stdout
 * @c: The character to print
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */

int _putchar(char c)
{
	return (write(1, &c, 1));
}


/**
 *print_c - prints char
 *@list: list of arg
 *Return: 1 on success
 */

int print_c(va_list list)
{
		_putchar(va_arg(list, int));
		return (1);
}

/**
  *print_s - prints string
  *@list: list of arguments
  *Return: string length
  */

int print_s(va_list list)
{
	int i = 0;
	char *c = va_arg(list, char *);

	if (c)
	{
		for (; c[i]; i++)
		{
			_putchar(c[i]);
		}
	}

	else
	{
		c = "(null)";
	}

	return (i);
}

/**
 *print_i - prints integer
 *@n: integer to printeded
 *Return: int
 */

int print_i(va_list list)
{
	int i = 0;
	int n = va_arg(list, int);
	int aux;

	if (n < 0)
	{
		_putchar('-');
		i++;
		aux = -n;
	}
	else
	{
		aux = n;
	}

	if (aux / 10)
	{
		i += print_i(aux / 10);
	}

	_putchar((aux % 10) + '0');
	i++;

	return (i);
}

/**
 * print_d - prints decimal int
 * @list: list of arg
 * Return: decimal int
 */

int print_d(va_list list)
{
	int d = va_arg(list, int);

	return (print_i(d));
}


/**
 * print_p - Prints a percentage sign
 * @list: Arguments
 *
 * Return: String length
*/

int print_p(__attribute__((unused)) va_list list)
{
	return (_putchar('%'));
}

