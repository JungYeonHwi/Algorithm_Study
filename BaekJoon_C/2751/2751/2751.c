#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void swap(int* arr, int x, int y)
{
	int temp = arr[x];
	arr[x] = arr[y];
	arr[y] = temp;
}

void heap(int* arr, int n)
{
	int count = n;

	int p, c;
	for (int i = 1; i < count; i++) {
		c = i;
		while (c > 0) {
			p = (c - 1) / 2;
			if (arr[p] < arr[c]) {
				swap(arr, p, c);
				c = p;
			}
			else break;
		}
	}
	swap(arr, 0, --count);

	while (count > 1) {

		p = 0;
		while (p <= (count / 2) - 1) {
			c = p * 2 + 1;
			if (c + 1 < count && arr[c] < arr[c + 1])
				c++;
			if (arr[p] < arr[c]) {
				swap(arr, p, c);
				p = c;
			}
			else break;
		}
		swap(arr, 0, count-- - 1);
	}
}

int main() {

    int N;
    scanf("%d", &N);

    int* arr = (int*)malloc(sizeof(int) * N);

    for (int i = 0; i < N; i++) scanf("%d", &arr[i]);

	heap(arr, N);

    for (int i = 0; i < N; i++) printf("%d\n", arr[i]);

    return 0;
}