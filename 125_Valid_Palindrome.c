#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

bool isPalindrome(char* s) {

	for (int i = 0; s[i] != '\0'; i++) { 
		s[i] = tolower((unsigned char)s[i]);
	}

	char* new_str = (char*)malloc((strlen(s) + 1) * sizeof(char));
	if (new_str == NULL) {
		fprintf(stderr, "Memory allocation failed\n");
		return false; // Return false if memory allocation fails
	}

	int j = 0;

	for (int i = 0; s[i] != '\0'; i++) {
		if (isalnum((unsigned char)s[i])) {
			new_str[j++] = s[i]; //postincrement

		}
	}

	new_str[j] = '\0';
	printf("%s\n", new_str);

	int left_pointer = 0;
	int right_pointer = strlen(new_str)-1;

	while (left_pointer <= right_pointer) {
		if (new_str[left_pointer++] == new_str[right_pointer--]) {
			continue;
		}
		else {
			//printf("false");
			free(new_str);
			return false;
		}
	}
	//printf("true");




	free(new_str);
	return true;
}

int main() {
	char s[] = "QZrD2 7UL91z, i`O2ef:6e'2\"yP !:,U.:pX90PU3CXo'i!;3 `j 0 ? \"'hK8 ? BAjM2\"DBw?7!4R3?U2E8F2y!?3 R2!fw 6e!:0  ErCi98KM`,8`8648,mi3P0`,!5 E.?00J3A 52\"x8,tHy!'2!DLBbK'j!tt1C' 7`JPulW\"\"uRTbr\"',\",U`ZOW5'\"LMDQDMJ\"'5WOZ`U,\",'\"rbTRu\"\"WluPJ`7 'C1tt!j'KbBJD!2'!yHt,8x\"25 A3J00?.E 5!,`0P3im,8468`8,`MK89iCrE  0:!e6 wf!2R 3?!y2F8E2U?3R4!7?wBD\"2MjAB ? 8Kh'\"?0 j` 3;!i'oXC3UP09Xp:.U,:! Py\"2'e6:fe2O`i,z19LU7 2DrZQ"; // Example string
	

	bool result = isPalindrome(s); // Convert to lowercase
	printf("%s\n", result ? "true" : "false");

	return 0;
}