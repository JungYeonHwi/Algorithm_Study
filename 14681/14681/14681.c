#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	int x, y;
	int pos;

	scanf("%d", &x);
	scanf("%d", &y);

	if (x > 0 && y > 0) pos = 1;
	if (x < 0 && y > 0) pos = 2;
	if (x < 0 && y < 0) pos = 3;
	if (x > 0 && y < 0) pos = 4;

	printf("%d", pos);

	return 0;
}