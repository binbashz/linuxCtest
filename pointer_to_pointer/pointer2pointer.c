#include <stdio.h>
#include <stdlib.h>

/*************** punteros simples con variables estaticas *****************/

int main()
{
	int num = 5;
	trabajoConReferencia(&num);
	num = trabajoConCopia(num);
	printf("Numero: %d",num);
}

	int trabajoConCopia(int num)

{
	printf("Ingrese el numero");
	scanf("%d", &num);
	return (num);
}
	void trabajoConReferencia (int *num)
{	printf("Ingrese el numero\n");
	scanf("%d", num);
}

/***************** punteros dobles con variable estaticas*****************/

	int main()
{
	int num = 5;
	int *NumPunteroSimple = &num;
	trabajoConReferenciaDoble(&numPunterosSimple);
	printf("Numero: %d", num);
}
	void trabajoConReferenciaDoble(int **num)
{
	printf("Ingrese el numero\n");
	scanf("%d", (*num));
}
