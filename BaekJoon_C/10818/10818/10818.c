#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int input;
	int n;
	int min, max;

	scanf("%d", &input);
	int* arr = (int*)malloc(sizeof(int) * input);

	for (int i = 0; i < input; i++) {
		scanf("%d", &n);
		arr[i] = n;
	}

	min = arr[0];
	max = arr[0];

	for (int i = 0; i < input; i++) {
		if (min > arr[i]) min = arr[i];
		if (max < arr[i]) max = arr[i];
	}

	printf("%d %d", min, max);

	return 0;
}