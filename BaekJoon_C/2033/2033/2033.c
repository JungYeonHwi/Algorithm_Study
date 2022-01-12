#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
    int initnum = 10;
    int tmp;

    while (N / initnum != 0) {
        if (N % initnum >= 5 * (initnum / 10)) {
            N += initnum * 1;
            tmp = (N % initnum) / (initnum / 10);
            N -= (tmp * (initnum / 10));
        }
        else {
            tmp = (N % initnum) / (initnum / 10);
            N -= (tmp * (initnum / 10));
        }
        initnum *= 10;
    }

    printf("%d", N);
}