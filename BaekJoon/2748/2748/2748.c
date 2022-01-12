#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long int fib[100];

long long int answer(int n)
{
    fib[1] = 1;
    fib[0] = 0;

    for (int i = 2; i <= n; i++) fib[i] = fib[i - 1] + fib[i - 2];
    
    return fib[n];
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld", answer(n));
}