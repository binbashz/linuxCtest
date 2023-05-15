#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	struct Nodo
{
	int dato;
	struct Nodo *izquierda;
	struct Nodo *derecha;
};

struct Nodo *Nuevo_nodo(int dato)
{ /* solicitar memoria */
	size_t tamanioNodo = sizeof(struct Nodo);
	struct Nodo *nodo = (struct Nodo *) malloc(tamanioNodo);
	/* asignar el dato e inicar hojas */
	nodo->dato = dato;
	nodo->izquierda = nodo->derecha = NULL;
	return (nodo);
}
