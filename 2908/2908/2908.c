#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int num1, num2;
	int rnum1 = 0;
	int rnum2 = 0;
	int* pos = (int*)malloc(sizeof(int) * 3);
	int i = 0;

	scanf("%d %d", &num1, &num2);

	while (num1 != 0) {
		pos[i] = num1 % 10;
		//printf("%d\n", pos[i]);
		num1 = num1 / 10;
		i++;
	}

	rnum1 = pos[0] * 100 + pos[1] * 10 + pos[2];

	i = 0;

	while (num2 != 0) {
		pos[i] = num2 % 10;
		//printf("%d\n", pos[i]);
		num2 = num2 / 10;
		i++;
	}

	rnum2 = pos[0] * 100 + pos[1] * 10 + pos[2];
	
	if (rnum1 > rnum2) printf("%d", rnum1);
	else printf("%d", rnum2);


	return 0;
}