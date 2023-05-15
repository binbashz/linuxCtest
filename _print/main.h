#ifndef MAIN_H
#define MAIN_H
#include <stdarg.h>
#include <stdlib.h>
#include <stddef.h>
#include <limits.h>

/**
 *struct op_t - specifier
 *@ops: type of argunment
 *@f: function pointer
 */

typedef struct ops
{
	char *op;
	int (*f)(va_list list);
} specifier_t;

int _printf(const char *format, ...);
int _putchar(char c);
int print_c(va_list list);
int print_s(va_list list);
int print_i(va_list list);
int print_d(va_list list);
int format_specifier(va_list list, char spec);
int print_p(va_list list);

#endif
