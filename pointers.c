/*
 * main - printing the size, in bytes, of a pointer
 *
 * Return: Always 0.
 */
#include <stdio.h>


int main(void)
{
	int *p;
	printf("size of pointer: %lu\n", sizeof(p));
	return (0);
}
