
 ## Project printf 
  ##### Write a function that produces output according to a format.
  ----------------------------------------------------------------------------------------------------------

*printf is a c language function, provided by the stdio library, in this project we will re-create a printf function that prints through the introduction of a format, using variadic functions and structures to connect everything when compiling*

This is a simple implementation of printf function that formats and prints data

>Description
The _printf() function produces output according to a prototype which is described below. This function write its output to the stdout, the standard output stream. Returns the count of printed characters when the function is successful and -1 when the function fails.

![xxxz](https://user-images.githubusercontent.com/124454895/229006128-acf5b9b0-5ec5-4b69-991e-6f359f755497.png)




*The function receives a format string (format) and a variable list of arguments (list) that are specified with ellipses (...) in the function definition.
A variable i of type unsigned int and strlen of type int are declared. The variable i is used to iterate through the format string and the variable strlen is used to count the number of characters that are printed.
A variable argument list is initialized using va_start(), which takes the address of the last argument before the ellipses.
If the format string is NULL, the function returns -1.*

*Otherwise, a for loop is performed to traverse the format string.
If a % character is found in the format string, a check is made to see if there is a valid specifier after the % character. 
If there is no valid specifier, -1 is returned. 
If a valid specifier is found, the function is called;*



![carbon](https://user-images.githubusercontent.com/124454895/229324445-7640757d-555b-47ba-a9d3-73dcd217657d.png)


*which performs a corresponding action according to the specifier, and updates the variable strlen with the number of characters printed.
If a % character is not found in the format string, the current character is printed and the strlen variable is updated.
After traversing the format string, va_end() is called to finalize the variable argument list.
Finally, the function returns strlen, which contains the total number of characters printed.*

| Specifiers | Description     |
| --- | --- |
| %d | Print   decimal     numbers          |
| %i | Print  integers             |
| %c | Print    single     character       |
| %s | Print     string     of   characteres |




| File | Description |
| --- | --- |
| [main.h] | Header file  
| [main.c] |Include all function prototypes  
| [...] |Include structure of specifiers |
| [_printf.c] | Project function: \_printf 


                                                       🚧   site under construction 🚧
