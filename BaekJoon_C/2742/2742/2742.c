#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int input;
	int x, y;

	scanf("%d", &input);

	for (int i = input; i >= 1; i--) {
		printf("%d\n", i);
	}

	return 0;
}