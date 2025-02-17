#include <stdio.h>
#include <stdlib.h>

int is_punctuation(char c) {

    return (c == ',' || c == '.' || c == '-' || c == ';' || c == ':' || c == '?' || c == '!');

}
char* concat_strings(char **strings) {

    char **ptr = strings;

    size_t total_length = 0;
while (*ptr) {

        char *s = *ptr;

        while (*s != '\0') {

            total_length++;

            s++;   }

        ptr++;   }
char *result = (char *)malloc(total_length + 1);

    if (!result) {

        fprintf(stderr, "Memory allocation failed\n");

        exit(EXIT_FAILURE); }

    char *dest = result;

    ptr = strings;
while (*ptr) {

        char *s = *ptr;
int is_first_char = 1;

        while (*s != '\0') {
 if (is_first_char && is_punctuation(*s) && (dest != result) && (*(dest - 1) == ' ')) {

  dest--;  }

   *dest = *s;

   dest++;

   is_first_char = 0;

   s++;
 }

  ptr++;  }

  *dest = '\0';

  return result;

}
int main(int argc, char **argv) {
if (argc < 2) {

        fprintf(stderr, "Error: Please provide at least one string.\n");

        return EXIT_FAILURE;

    }
char *concatenated = concat_strings(argv + 1);
printf("%s\n", concatenated);
free(concatenated);

    return EXIT_SUCCESS;

}
