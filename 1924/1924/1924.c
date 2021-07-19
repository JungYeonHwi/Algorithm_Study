#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int x, y;
	scanf("%d %d", &x, &y);
	
	int month[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	int day = 0;

	for (int i = 1; i < x; i++)  day += month[i - 1];
	day += y;

	if (day % 7 == 0) printf("SUN\n");
	else if (day % 7 == 1) printf("MON\n");
	else if (day % 7 == 2) printf("TUE\n");
	else if (day % 7 == 3) printf("WED\n");
	else if (day % 7 == 4) printf("THU\n");
	else if (day % 7 == 5) printf("FRI\n");
	else if (day % 7 == 6) printf("SAT\n");

	return 0;
}