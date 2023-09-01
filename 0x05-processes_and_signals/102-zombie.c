#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>
#define _GNU_SOURCE


/**
*infinite_while - Running an infinite while loop
*Return: Always 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
*main - Creating five zombie processes.
*Return: Always 0
*/
int main(void)
{
	int i;

	for (i = 2; i < 7; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
