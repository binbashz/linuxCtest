#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	struct Persona
	{
		char nombre[40];
		int edad;
	};

	int main(void)
	{
		struct Persona *p_persona;

		/* reservamos memoria para la estructura, utilizando malloc */
		p_persona = (struct Persona *)malloc(sizeof(struct Persona));
		/*asignamos valores a la estructura utilizando el punteros */
		strcpy(p_persona->nombre, "matt");
		/* impresion de los valores de la estructira utilizando el puntero*/
		printf(" el nombre de la persona es %s y su edad es %d.", p_persona->nombre, p_persona->edad);

		/* liberamos la memoria resevada*/
		free(p_persona);
		return (0);
	}
