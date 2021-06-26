#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int N;
	int result;
	int A, B, C, D;
	int count = 0;

	scanf("%d", &N);
	result = N;

	while (1)
	{
		A = N / 10;
		B = N % 10;
		C = (A + B) % 10;
		D = (B * 10) + C;

		N = D;
		count++;
		if (D == result) break;

	}
	printf("%d", count);

	return 0;
}

