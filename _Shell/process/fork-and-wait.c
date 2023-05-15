/* fork, wait y multopes procesos hijo */

#include <unistd.h> /* cabecera para el fork */
#include <sys/wait.h> /* header para wait  */ 
#include <stdio.h>
#include <stdlib.h>

#define NUM_CHILD 5

int doSomething(void)
{
	int ret;
	srand(getpid());
	ret = (rand() % 256);
	printf("HIJO: PID = %d, valor aleatorio calculado %d \n", getpid() , ret);

int main(void)
{
	for(int i = 0; i < NUM_CHILD; i++)
	{
		pidC = fork();
		if(pidC > 0)
			continue;
		else if(pidC == 0)
		{
			doSomething();
			exit(0);
	}
		else 
		{ /* error */
		}

		for(int  i = 0; i < NUM_CHILD; i++)
		{
			pidC = wait(&status);
			printf("PADRE DE pid + %D, HIJO DE PID = %d terminado, st  %d \n", getpid(), pidC, WEXITSTATUS(status) );

		while(1)
		{
			sleep(10);
		}


	return (0);
}
