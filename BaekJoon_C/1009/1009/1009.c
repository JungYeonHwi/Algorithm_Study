#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int T, a, b;
	scanf("%d", &T);

	for (int i = 0; i < T; i++) {
		scanf("%d %d", &a, &b);

		int num = 1;

		for (int k = 0; k < b; k++) {
			num *= a;
			num %= 10;
		}
		if (num == 0) printf("10\n");
		else printf("%d\n", num);
	}

	return 0;
}