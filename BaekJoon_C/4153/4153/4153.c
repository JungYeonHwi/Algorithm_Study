#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {

	int x, y, h;
	scanf("%d %d %d", &x, &y, &h);

	while (x != 0 && y != 0 && h != 0) {
		int temp = 0;

		if (x > y) {
			if (x > h) {
				temp = x;
				x = h;
				h = temp;
			}
		}

		else {
			if (y > h) {
				temp = y;
				y = h;
				h = temp;
			}
		}

		int n = x * x + y * y;

		if (h == sqrt(n)) printf("right\n");
		else printf("wrong\n");

		scanf("%d %d %d", &x, &y, &h);
	}

	return 0;
}