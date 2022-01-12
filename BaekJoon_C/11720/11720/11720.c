#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);

	int sum = 0;

	char* num = (char*)malloc(sizeof(char) * 100);
	scanf("%s", num);

	for (int i = 0; i < N; i++) {
		sum += num[i] - '0';
	}

	printf("%d", sum);
	return 0;
}