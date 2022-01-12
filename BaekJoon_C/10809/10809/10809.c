#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char* S = (char*)malloc(sizeof(char) * 100);
	scanf("%s", S);

	int *alpha = (int*)malloc(sizeof(int) * 26);

	for (int i = 0; i < 26; i++) {
		alpha[i] = -1;
	}

	for (int i = 0; i < strlen(S); i++) {
		if (alpha[S[i] - 97] == -1) alpha[S[i] - 97] = i;
	}

	for (int i = 0; i < 26; i++) printf("%d ", alpha[i]);

	
	return 0;
}