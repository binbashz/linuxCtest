#include <unistd.h>
#include <stdio.h>

	int var = 22;
int main(void)
{	
	pid_t pidC;
	printf(" procesos. PID = %d comienza \n", getpid());
	pidC = fork();

	printf("PROCESO. PID = %d ejecutandose\n", getpid());

	if(pidC > 0)
	{
		var = 43;
	}
	else if(pidC == 0)
	{ 

	}
	
	else 
	{

	}

	while(1)
	{
		sleep(2);
	}
	return (0);
}
