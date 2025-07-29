// large.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOTES 10

char* notes[MAX_NOTES];

void add_note() {
    int idx;
    printf("Index: ");
    scanf("%d", &idx); //

    if (idx >= 0 && idx < MAX_NOTES) {
        notes[idx] = malloc(8);
        printf("Note: ");
        gets(notes[idx]); // 
    }
}

void delete_note() {
    int idx;
    printf("Index to delete: ");
    scanf("%d", &idx); //

    if (idx >= 0 && idx < MAX_NOTES) {
        free(notes[idx]);
        notes[idx] = NULL;
    }
}

void print_note() {
    int idx;
    printf("Index to view: ");
    scanf("%d", &idx); //

    printf("Note: %s\n", notes[idx]); //
}

int main() {
    int choice;

    while (1) {
        printf("\n1. Add\n2. Delete\n3. View\n4. Exit\n> ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: add_note(); break;
            case 2: delete_note(); break;
            case 3: print_note(); break;
            case 4: return 0;
            default: printf("Invalid.\n"); break;
        }
    }

    return 0;
}
