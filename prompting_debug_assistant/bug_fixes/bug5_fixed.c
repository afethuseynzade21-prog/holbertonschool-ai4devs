#include <stdio.h>
#include <string.h>

int main(void) {
    char text[100];

    printf("Enter a sentence: ");
    if (fgets(text, sizeof(text), stdin) == NULL) {
        return 1;
    }
    text[strcspn(text, "\n")] = '\0';

    size_t length = strlen(text);

    printf("Character count: %zu\n", length);

    return 0;
}
