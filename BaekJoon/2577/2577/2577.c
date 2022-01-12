#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int n;
	int index = 0;
	int cal = 1;

	int* arr = (int*)malloc(sizeof(int) * 3);

	for (int i = 0; i < 3; i++) {
		scanf("%d", &n);
		arr[i] = n;
	}

	for (int i = 0; i < 3; i++) {
		cal *= arr[i];
	}

	int* num = (int*)malloc(sizeof(int) * 9);
	for (int i = 0; i < 10; i++) {
		num[i] = 0;
	}

	//printf("%d\n", cal);

	while (cal) {
		for (int i = 0; i < 10; i++) {
			if (i == cal % 10) num[i]++;
		}
		cal = cal / 10;
	}

	for (int i = 0; i < 10; i++) {
		printf("%d\n", num[i]);
	}

	return 0;
}