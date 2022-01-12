#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int count;
	int num;

	scanf("%d", &count);

	if (count < 1 || count > 1000) return -1;
    int* arr = (int*)malloc(sizeof(int) * count);

	for (int i = 0; i < count; i++) {
		scanf("%d", &num);
		arr[i] = num;
	}

	/*for (int i = 0; i < count; i++) {
		printf("%d", arr[i]);
	}*/

    int min, min_index, temp;
    for (int i = 0; i < count; i++) {
        min = 1001;
        for (int j = i; j < count; j++) {
            if (arr[j] < min) {
                min = arr[j];
                min_index = j;
            }
        }
        temp = arr[min_index];
        arr[min_index] = arr[i];
        arr[i] = temp;
    }
    for (int i = 0; i < count; i++) {
        printf("%d\n", arr[i]);
    }

}