#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int input;
	int n;

	scanf("%d", &input);
	int* arr = (int*)malloc(sizeof(int) * input);

	for (int i = 0; i < input; i++) {
		scanf("%d", &n);
		arr[i] = n;
	}

	int M = arr[0];

	for (int i = 0; i < input; i++) {
		if (M < arr[i]) M = arr[i];
	}

	float cal = 0;
	float sum = 0;

	for (int i = 0; i < input; i++) {
		cal = (float)arr[i] / M * 100;
		sum += cal;
	}

	printf("%f", sum / input);
	

	return 0;
}