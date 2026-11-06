#include <stdio.h>
#include <string.h>

int main(void) {
    char text[100];

    printf("Enter a sentence: ");
    scanf("%s", text);

    size_t length = sizeof(text);

    printf("Character count: %zu\n", length);

    return 0;
}
