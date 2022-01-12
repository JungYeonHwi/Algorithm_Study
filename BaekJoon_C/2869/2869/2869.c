#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {

	int A, B, V;

	scanf("%d %d %d", &A, &B, &V);

	int day = (V - B - 1) / (A - B) + 1;
	printf("%d", day);

	return 0;
}