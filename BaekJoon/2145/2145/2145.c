#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int N;
    while (1) {
        scanf("%d", &N);
        if (N == 0) break;
        while (N >= 10) {
            int temp1 = N;
            int sum = 0;
            while (temp1 > 0) {
                sum += temp1 % 10;
                temp1 /= 10;
            }
            N = sum;
        }
        printf("%d\n", N);
    }

    return 0;
}