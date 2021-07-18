#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int rev(int n) {
    int x = 0;

    while (n > 0) {
        x = x * 10 + n % 10;
        n /= 10;
    }
    return x;
}

int main()
{
    int A, B;
    scanf("%d %d", &A, &B);

    int rA = rev(A);
    int rB = rev(B);
    int result = rev(rA + rB);
    printf("%d", result);

    return 0;
}