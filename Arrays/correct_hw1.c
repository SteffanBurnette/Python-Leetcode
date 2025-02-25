#include <stdio.h>
#include <stdlib.h>

// Counts the number of characters in the array of strings (terminated by NULL)
int total_chars(char** arr) {
    int count = 0;
    while (*arr != NULL) {
        char* workingReference = *arr;
        while (*workingReference != '\0') {
            count++;
            workingReference++;
        }
        arr++;
    }
    return count;
}

// Concatenates an array of strings into a single string.
// Assumes that the array is terminated by a NULL pointer.
char* concat_string(char** strings) {
    int total_length = total_chars(strings);
    // Allocate enough space for the concatenated string and the null terminator.
    char* result = (char*) malloc((total_length + 1) * sizeof(char));
    if (result == NULL) {
        perror("malloc failed");
        exit(EXIT_FAILURE);
    }
    char* start = result;  // Save the starting address of the allocated memory

    while (*strings != NULL) {
        char* current = *strings;
        while (*current != '\0') {
            *result = *current;
            result++;
            current++;
        }
        strings++;
    }
    *result = '\0'; // Null-terminate the concatenated string
    return start;
}

int main(int argc, char *argv[]) {
    // Check if the user provided at least one string (skip program name)
    if (argc < 2) {
        printf("Usage: %s <string1> <string2> ...\n", argv[0]);
        return 1;
    }
    
    // argv is an array of pointers; argv[argc] is guaranteed to be NULL,
    // so we can pass argv+1 (ignoring the program name) to concat_string.
    char* concatenated = concat_string(argv + 1);
    
    printf("Concatenated string: %s\n", concatenated);
    
    free(concatenated);
    return 0;
}
