#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char* str = (char*)malloc(sizeof(char*) * 100);
	gets(str);
	int count = 0;
	for (int i = 0; i < strlen(str); i++) {
		if (str[i] >= 'A' && str[i] <= 'M') str[i] = str[i] + 13;
		else if (str[i] >= 'N' && str[i] <= 'Z') str[i] = str[i] - 13;
		else if (str[i] >= 'a' && str[i] <= 'm') str[i] = str[i] + 13;
		else if (str[i] >= 'n' && str[i] <= 'z') str[i] = str[i] - 13;
	}
	printf("%s", str);

	return 0;
}