#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int n;
	int max;
	int index = 0;

	int* arr = (int*)malloc(sizeof(int) * 9);

	for (int i = 0; i < 9; i++) {
		scanf("%d", &n);
		arr[i] = n;
	}

	max = arr[0];

	for (int i = 0; i < 9; i++) {
		if (max < arr[i]) {
			max = arr[i];
			index = i;
		}
	}

	printf("%d\n%d", max, index+1);

	return 0;
}