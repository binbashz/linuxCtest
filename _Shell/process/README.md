
fork() Procesos padre, hijo, huerfano

pid_t fork(void)

	-crea un nuevo proceso ("hijo")
	- el proceso hijo es un diplicado del "padre"
	-los dos procesos 
		- tienen PIDs diferentes
		- corren en espacios separados de memoria 

	

	Retorno de fork()
	   > si todo va bien :
			- al padre se le retornara un valor, que sera el id del proceso del nuevo hijo creado
			- el valor que se retorne al procesos hijo sera un 0


	>si hay errores: - el proceso no se crea
			retorno al padre : -1

