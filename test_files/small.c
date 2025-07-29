// small.c
#include <stdio.h>
#include <string.h>
int main() {
    char buf[8];
    printf("Enter input: ");
    gets(buf); 
    printf("You entered: %s\n", buf);
    return 0;
}