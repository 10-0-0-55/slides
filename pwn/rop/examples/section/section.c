#include <stdio.h>
#include <stdlib.h>

int var1 = 111;									//.data
int var2;										//.bss
char str[] = "ting ting sister strong a";		//.data / .rodata
const double PAI = 3.1414926;					//.rodata

int main()
{
	int var3 = 666;								//stack
	getchar();
	char *point = malloc(16);					//heap
	return 0;
}
