#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

char arr[8][8];

int main() {

	int count = 0, i, j;

	for (i = 0; i < 8; i++) scanf("%s", arr[i]);

	for (i = 0; i < 8; i++) {

		if (i == 0 || i == 2 || i == 4 || i == 6) {

			for (j = 0; j < 8; j = j + 2) {

				if (arr[i][j] == 'F') count++;
			}
		}
		else if (i == 1 || i == 3 || i == 5 || i == 7) {

			for (j = 1; j < 8; j = j + 2) {

				if (arr[i][j] == 'F') count++;
			}
		}
	}

	printf("%d", count);

	return 0;

}