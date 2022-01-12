#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main() {
	
	int H = 0;
	int M = 0;
	int h, m;

	scanf("%d %d", &H, &M);

	if (M >= 45) {
		h = H;
		m = M - 45;
	}

	else {
		if (H == 0) {
			h = 23;
			m = 60 + M - 45;
		}

		else {
			h = H - 1;
			m = 60 + M - 45;
		}
	}

	printf("%d %d", h, m);
}