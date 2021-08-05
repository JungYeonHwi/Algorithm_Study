#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include<stdlib.h>
int compare(const void* a, const void* b)
{
    int num1 = *(int*)a;
    int num2 = *(int*)b;
    if (num1 < num2)
        return -1;
    if (num1 > num2)
        return 1;
    return 0;
}

int main()
{
    int i, j, sum = 0, max = -1, cnt;
    int arr[5] = { 0, };
    int arr2[105] = { 0, };
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    sum /= 5;
    qsort(arr, 5, sizeof(int), compare);
    printf("%d\n%d", sum, arr[2]);
}