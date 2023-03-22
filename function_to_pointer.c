#include <stdio.h>
void imprime(void)
{
	printf("Imprimiendo un message\n");
}
int main(void)
{
	void (*ptr_funct)(void) = imprime;

	ptr_funct();
	/* Llama a imprime*/
	return (0);
 }
