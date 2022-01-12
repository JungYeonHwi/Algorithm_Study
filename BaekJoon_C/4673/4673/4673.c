#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#include <string.h>

int funtion(int num) {
	int count = 1;
	int i = 0;
	int origin = num;
	int reorigin = num;
	int sum = 0;
	while (num / 10) {
		num = num / 10;
		count++;
	}

	int* arr = (int*)malloc(sizeof(int) * count);
	//printf("count : %d\n", count);

	for (int i = 0; i < count; i++) {
		//printf("origin %d\n", origin);
		arr[i] = origin % 10;
		origin = origin / 10;
		//printf("%d\n", arr[i]);
		sum += arr[i];
	}

	sum += reorigin;

	//printf("sum : %d\n\n", sum);

	return sum;
	
}

int main() {
	int arr[10001];
	int i;
	int check;

	for (i = 1; i < 10001; i++) {
		check = funtion(i);
		if (check < 10001) arr[check] = 1;
	}
	for (i = 1; i < 10001; i++) {
		if (arr[i] != 1) printf("%d\n", i);
	}

	return 0;
}