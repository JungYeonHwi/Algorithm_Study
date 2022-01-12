#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

char arr[2500][2500];

//��� ĭ�� *�� ä���ֱ�
void AllStar(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            arr[i][j] = '*';
    }
}

//������ ��(x,y)���� ���λ��η� 3^cnt��ŭ �������� ä���
void Blank(int x, int y, int cnt) {
    for (int i = x; i < x + (int)pow(3, cnt); i++) {
        for (int j = y; j < y + (int)pow(3, cnt); j++) {
            arr[i][j] = ' ';
        }
    }
}

//�������� ������ ��(x,y) ã��
void Pivot(int n, int cnt) {
    if (n > 0) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                //�ش� �������� ��������
                Blank((int)pow(3, cnt) + i * (int)pow(3, cnt + 1),
                    (int)pow(3, cnt) + j * (int)pow(3, cnt + 1), cnt);
            }
        }
        //������ �̵��ϱ�
        Pivot(n / 3, cnt + 1);
    }
}

int main() {
    int N;
    scanf("%d", &N);
    AllStar(N);

    Pivot(N / 3, 0);

    //������
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf("%c", arr[i][j]);
        printf("\n");
    }
    return 0;
}