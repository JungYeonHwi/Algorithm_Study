#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int N, K;
    scanf("%d %d", &N, &K);

    int result = 1;
    int result1 = 1;
    int result2 = 1;
    int i = 1;

    while (i < K+1) {
        result1 *= N;
        N--;
        i++;
    }

    for (int i = 1; i <= K;i++) result2 *= i;

    printf("%d", result1 / result2);

}