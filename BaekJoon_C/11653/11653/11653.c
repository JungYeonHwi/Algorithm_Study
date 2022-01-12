#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);

	if (n == 1) return 0;

	int i = 2;

    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            printf("%d\n", i);
            n /= i;
            --i;
        }
    }
    if (n > 1)
        printf("%d\n", n);

	return 0;
}