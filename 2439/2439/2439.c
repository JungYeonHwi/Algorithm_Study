#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int input;
	int x, y;

	scanf("%d", &input);

	for (int i = 1; i <= input; i++) {
		for (int j = 1; j <= (input - i); j++)
			printf(" ");
		for (int j = 1; j <= i; j++)
			printf("*");
		printf("\n");
	}

	return 0;
}