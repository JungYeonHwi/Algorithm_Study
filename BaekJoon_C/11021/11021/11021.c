#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int input;
	int x, y;

	scanf("%d", &input);

	for (int i = 1; i <= input; i++) {
		scanf("%d %d", &x, &y);
		printf("Case #%d: %d\n", i, x + y);
	}

	return 0;
}