#ifndef colaDePedidos_h
#define colaDePedidos_h


#include <stdio.h>

	typedef struct LineaPedido
{
	int id_producto;
	int cantidad;
	float precio_unidad;
} lineaPedido;

	typedef struct NodoLineaPedido
{
	LineaPedido linea;
	struct NodoLineaPedido* siguiente;
} NodoLineaPedido;

	typedef struct Pedido
{
	int id_cliente;
	NodoLienaPedido* lista_productos;
} Pedido;

#endif 

