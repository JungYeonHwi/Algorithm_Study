#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int T;
	scanf("%d", &T);

	int num;

	char* S = (char*)malloc(sizeof(char) * 20);

	for (int i = 0; i < T; i++) {
		scanf("%d", &num);
		scanf("%s", S);

		for (int j = 0; j< strlen(S); j++) {
			for (int c = 0; c < num; c++) printf("%c", S[j]);
		}
		printf("\n");
	}
	


	return 0;
}