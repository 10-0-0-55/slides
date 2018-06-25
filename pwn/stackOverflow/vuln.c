#include <stdio.h>

void F2()
{
	printf("I'm Here!\n");
}

void F1(int num1, int num2)
{
	int result = num1 + num2;
	printf("num1 + num2 = %d\n", result);

	char buf[8];
	scanf("%s", buf);//vulnerable
	printf("%s\n", buf);
}

int main()
{
	F1(1, 2);
	return 0;
}
