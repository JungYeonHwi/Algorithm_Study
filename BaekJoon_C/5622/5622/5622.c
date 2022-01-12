#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char* input = (char*)malloc(sizeof(char) * 15);

	scanf("%s", input);

	int time = 0;

	int len = strlen(input);

	for (int i = 0; i <= len; i++) {
		if (input[i] == 'A') time += 3;
		if (input[i] == 'B') time += 3;
		if (input[i] == 'C') time += 3;
		if (input[i] == 'D') time += 4;
		if (input[i] == 'E') time += 4;
		if (input[i] == 'F') time += 4;
		if (input[i] == 'G') time += 5;
		if (input[i] == 'H') time += 5;
		if (input[i] == 'I') time += 5;
		if (input[i] == 'J') time += 6;
		if (input[i] == 'K') time += 6;
		if (input[i] == 'L') time += 6;
		if (input[i] == 'M') time += 7;
		if (input[i] == 'N') time += 7;
		if (input[i] == 'O') time += 7;
		if (input[i] == 'P') time += 8;
		if (input[i] == 'Q') time += 8;
		if (input[i] == 'R') time += 8;
		if (input[i] == 'S') time += 8;
		if (input[i] == 'T') time += 9;
		if (input[i] == 'U') time += 9;
		if (input[i] == 'V') time += 9;
		if (input[i] == 'W') time += 10;
		if (input[i] == 'X') time += 10;
		if (input[i] == 'Y') time += 10;
		if (input[i] == 'Z') time += 10;
	}

	printf("%d", time);

	return 0;
}