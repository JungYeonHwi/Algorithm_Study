#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int a[100][100];
	int b[100][100];
	int sum[100][100];
	int n, m;
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			scanf("%d", &a[i][j]);
		}
	}
	for (int k = 0; k < n; k++)
	{
		for (int l = 0; l < m; l++)
		{
			scanf("%d", &b[k][l]);
		}
	}
	for (int q = 0; q < n; q++)
	{
		for (int w = 0; w < m; w++)
		{
			sum[q][w] = a[q][w] + b[q][w];
			printf("%d ", sum[q][w]);
		}
		printf("\n");
	}
	return 0;

}