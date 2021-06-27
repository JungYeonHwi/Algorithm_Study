#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#include <string.h>

int main() {
	int input;


	scanf("%d", &input);
	char* arr = (char*)malloc(sizeof(char) * 81);

	for (int i = 0; i < input; i++) {
		int sum = 0;
		int add = 1;
		scanf("%s", arr);
		
		for (int j = 0; j < strlen(arr); j++) {
			if (arr[j] == 'O') {
				sum += add;
				add++;
			}

			else add = 1;
		}
		printf("%d\n", sum);
	}

	

	return 0;
}