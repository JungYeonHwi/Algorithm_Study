#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int M, N;
	scanf("%d", &M);
	scanf("%d", &N);

	int sum = 0;
	int count = 0;
	int min = 0;

	for (int i = M; i <= N; i++) {
		int chk = 0;

		if (i == 1) chk = 1;

		for (int k = 2; k < i; k++) {
			if (i % k == 0) chk = 1;
		}

		if (chk == 0) {
			sum += i;
			count++;
			if (count == 1) {
				min = i;
			}
		}

	}

	if (sum == 0) {
		printf("-1");
		return 0;
	}

	printf("%d\n", sum);
	printf("%d", min);

	return 0;
}