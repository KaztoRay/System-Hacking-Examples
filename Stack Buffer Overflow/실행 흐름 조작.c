#include <stdio.h>
#include <unistd.h>

void win() {

    printf("You won!\n");

}

int main(void) {

    char buf[8];

    printf("Overwrite return addresss with %p : \n", &win);\
    read(0, buf, 32);

    return 0;

}