#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int n;
	int* arr = (int*)malloc(sizeof(int) * 10);

	for (int i = 0; i < 10; i++) {
		scanf("%d", &n);
		arr[i] = n;
	}

	int* num = (int*)malloc(sizeof(int) * 10);

	for (int i = 0; i < 10; i++) {
		num[i] = arr[i] % 42;
	}
	int result = 0;

	for (int i = 0; i < 10; i++) {
		int count = 0;
		for (int j = 0; j < i; j++) {
			if (num[i] == num[j]) count++;
			
		}

		if (count == 0) result++;
	}

	printf("%d", result);

	return 0;
}