#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int N;
	scanf("%d", &N);

	int count = 0;

	int sit[101] = { 0 };

	int num;

	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		if (sit[num] == 1)
			count++;
		sit[num] = 1;
	}

	printf("%d", count);

	return 0;

}