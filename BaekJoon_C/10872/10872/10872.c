#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int N;
	scanf("%d", &N);

	int result = 1;

	if (N == 0) result = 1;

	for (int i = 1; i <= N; i++) {
		result *= i;
	}

	printf("%d", result);

	return 0;

}