/**
 * _printf - Writes output to stdout
 * @format: string to print
 * Return: number of characters printed
 */	


int _printf(const char *format, ...)
{
    /* Inicializar lista variable de argumentos, contador, variable de función */
    va_list list;
    int i = 0;
    int len = 0;
    int (*f)(va_list); // puntero a función que acepta una lista variable de argumentos

    /* Iniciar la lista variable de argumentos */
    va_start(list, format);

    /* Verificar que la cadena de formato no sea nula */
    if (format == NULL)
    {
        return (-1);
    }

    /* Recorrer la cadena de formato carácter por carácter */
    while (format[i])
    {
        /* Si el carácter actual es un especificador de formato */
        if (format[i] == '%' && format[i + 1])
        {
            /* Obtener la función de impresión correspondiente al especificador de formato */
            f = specifier_match(format[i + 1]);

            /* Si la función de impresión se encuentra */
            if (f != NULL)
            {
                /* Llamar a la función de impresión con la lista variable de argumentos */
                len += f(list);

                /* Saltar al siguiente especificador de formato */
                i += 2;
                continue;
            }
        }

        /* Si el carácter actual es % pero no hay especificador después */
        else if (format[i] == '%' && format[i + 1] == '\0')
        {
            return (-1);
        }

        /* Si el carácter actual no es un especificador de formato */
        _putchar(format[i]);
        len++;
        i++;
    }

