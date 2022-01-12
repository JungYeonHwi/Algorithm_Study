#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int arr[101][101] = { 0 };

	for (int i = 0; i < 4; i++) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

		for (int i = x1; i < x2; ++i)
			for (int j = y1; j < y2; ++j)
				arr[i][j]++;
	}

	int count = 0;

	for (int i = 0; i < 101; ++i)
		for (int j = 0; j < 101; ++j)
			if (arr[i][j] > 0) count++;

	printf("%d", count);
	return 0;

}