#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {

	int x, y, w, h;
	scanf("%d %d %d %d", &x, &y, &w, &h);

	int x1 = abs(x);
	int y1 = abs(y);
	int w1 = abs(w - x);
	int h1 = abs(h - y);

	int min1 = 0;

	if (x1 > w1) {
		min1 = w1;
		if (y1 > h1) {
			if (min1 > h1) min1 = h1;
		}
		else {
			if (min1 > y1) min1 = y1;
		}
	}

	else {
		min1 = x1;
		if (y1 > h1) {
			if (min1 > h1) min1 = h1;
		}
		else {
			if (min1 > y1) min1 = y1;
		}
	}

	printf("%d", min1);
	

	return 0;
}