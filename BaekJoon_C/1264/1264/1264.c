#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	while (1) {
		char input[256];
		gets(input);
		if (strcmp(input, "#") == 0) return 0;

		int sum = 0;
		for (int i = 0; i < strlen(input) - 1; i++) {
			if (input[i] == 'a') sum++;
			if (input[i] == 'e') sum++;
			if (input[i] == 'i') sum++;
			if (input[i] == 'o') sum++;
			if (input[i] == 'u') sum++;
			if (input[i] == 'A') sum++;
			if (input[i] == 'E') sum++;
			if (input[i] == 'I') sum++;
			if (input[i] == 'O') sum++;
			if (input[i] == 'U') sum++;
		}
		printf("%d\n", sum);
	}
	
	return 0;
}