/*  comunica procesos "relacionados" , envio de "bytes streams" , pipe asocado a dos fd.*/
 /* ejemplo 
  * crear hijo 
  * hijo envia un mensaje 
  * padre recibe el mensaje.
  *
  *
  * pdre hijo y tuberia
  * **/


#include <unistd.h>

int main(void)
{
	intf fd[2];
	pid_t pidC;


	pipe(fd); /* error managment */
	swicht(pidC)
	{
		case 0; /* hijo */
		break;
		case 1;  /* too error */
		break
			default;  /* padre */
		close(fd[1]);
		break;


	fork();
