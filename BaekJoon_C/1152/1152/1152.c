#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char *input = (char*)malloc(sizeof(char) * 1000000);
	int count = 0;

	gets(input);

	if (input[0] == ' ') {
		char* ptr = strtok(input, " ");

		while (ptr != NULL)
		{
			count++;
			ptr = strtok(NULL, " ");
		}

		printf("%d", count);
	}

	else {
		char* ptr = strtok(input, " ");

		while (ptr != NULL)
		{
			count++;
			ptr = strtok(NULL, " ");
		}

		printf("%d", count);
	}

	return 0;
}