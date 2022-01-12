#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX 1000000

void upper(char* str);

int alpha[26] = { 0, };

int main() {
    char word[MAX];
    int i, index;
    int max = 0;
    int flag = 0;
    int len;
    scanf("%s", word);
    upper(word);

    len = strlen(word);
    for (i = 0; i < len; i++) {
        index = word[i] - 65;
        alpha[index] += 1;
    }

    for (i = 0; i < 26; i++) {
        if (alpha[i] > max) {
            max = alpha[i];
            index = i;
        }
    }

    for (i = 0; i < 26; i++) {
        if (i == index) continue;
        if (max == alpha[i]) {
            flag = 1;
        }
    }

    if (flag) {
        printf("?");
    }
    else {
        printf("%c", index + 65);
    }

    return 0;
}

void upper(char* str) {
    int i;
    int len = strlen(str);
    for (i = 0; i < len; i++) {
        if (islower(str[i])) {
            str[i] = toupper(str[i]);
        }
    }
}
