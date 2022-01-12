#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int x;

	int i, tmp, cnt;

	int child, parent;

	scanf("%d", &x);

	if (x == 1)
		printf("1/1");
	else {

		cnt = 1;

		tmp = x;

		while (tmp > cnt)
		{
			tmp -= cnt;
			cnt++;
		}

		if (cnt % 2 == 0)
		{
			parent = cnt; child = 1;

			for (i = 1; i < tmp; i++)
			{
				parent--;
				child++;
			}
		}
		else
		{
			parent = 1; child = cnt;

			for (i = 1; i < tmp; i++)
			{
				parent++;
				child--;
			}
		}

		printf("%d/%d", child, parent);
	}

	return 0;

}