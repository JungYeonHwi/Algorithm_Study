#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	
	int N;
	scanf("%d", &N);

	int num;
	int count = 0;

	for (int i = 0; i < N; i++) {
		scanf("%d", &num);
		int chk = 0;

		if (num == 1) chk = 1;

		for (int k = 2; k < num; k++) {
			if (num % k == 0) chk = 1;
		}

		if (chk == 0) {
			count++;
		}
	}

	printf("%d", count);

	return 0;
}