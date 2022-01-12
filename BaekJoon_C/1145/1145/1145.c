#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

int main()
{
    int count = 0;
    int* arr = (int*)malloc(sizeof(int) * 5);
    for (int i = 0; i < 5; i++) scanf("%d", &arr[i]);

    int Min = 1;

    while (1) {
        int cnt = 0;
        for (int i = 0; i < 5; i++)
        {
            if (Min >= arr[i] && Min % arr[i] == 0) cnt++;
        }

        if (cnt >= 3) break;

        Min++;
    }

    printf("%d", Min);

	return 0;
}