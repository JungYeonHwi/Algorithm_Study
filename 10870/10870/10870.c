#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int N;
	scanf("%d", &N);

	int result = 0;

	if (N == 0) result = 0;
	if (N == 1) result = 1;

	int f1 = 1;
	int f2 = 0;

	for (int i = 2; i <= N; i++) {
		result = f1 + f2;
		f2 = f1;
		f1 = result;
		printf("%d %d %d\n", f1, f2, result);
	}

	printf("%d", result);

	return 0;

}