#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char key[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
char secret[] = {0};
char flag[29] = {0x77, 0x7e, 0x72, 0x76, 0x4a, 0x60, 0x5f, 0x52, 0x40, 0x45, 0x56, 0x42, 0x47, 0x6c, 0x70, 0x5f, 0x55, 0x41, 0x5c, 0x50, 0x5d, 0x6d, 0x7c, 0x5c, 0x5d, 0x5a, 0x5f, 0x56, 0x4e };

void dead(){
    printf("You died\n");
}

void exitAngrman(){
    dead();
    exit(0);
}

void Ha(char a, char b, char c){ // 1 3 3
    key[0] = key[0]^a - key[1]^b + key[3]^c + (c & b) - a ;
    key[1] = key[0]^a - key[1]^b + key[3]^c + b ;
    key[2] = (key[0]^a - key[1]^b + key[3]^c)*-1 + a;
    if( key[0] + 0x33 != 0x2c + 0x33 ||
        key[1] - 0x22 != 0x52 - 0x22 ||
        key[2] + 0x11 != 0x3a + 0x11 )
        exitAngrman();
    printf("Hayaku!\n");
    sleep(1);
}
void Haya(char a, char b, char c){
    key[3] = key[0]*a - key[1]^b + key[3]^c + (a+b)/c;
    key[4] = key[1]^a - key[2]*b + key[4]^c + (c+a)/a;
    key[5] = key[2]^a - key[3]^b + key[5]*c + a + b + c;
    if( key[3] + 0x33 != 0x43 + 0x33||
        key[4] + 0x22 != 0xffffff83 + 0x22 ||
        key[5] + 0x11 != 0x38 + 0x11 )
        exitAngrman();
    printf("Modo..");
    fflush(stdout);
    sleep(1);
}
void Hayaku(char a, char b, char c){
    key[6] = key[3]^a - key[1]^b + key[6]^c + a;
    key[7] = key[4]^a - key[2]^b + key[7]^c + b;
    key[8] = key[5]^a - key[3]^b + key[8]^c + c;
    if( key[6] + 0x33 != 0xfffffffe + 0x33||
        key[7] + 0x22 != 0x27 + 0x22 ||
        key[8] + 0x11 != 0xffffff92 + 0x11 )
        exitAngrman();
    printf(" Hayaku!!\n");
    sleep(1);
}
void Star(char a, char b, char c){
    key[9] = key[3]^a - key[2]^b + key[1]^c - a;
    key[10] = key[4]^a - key[5]^b + key[6]^c - b;
    key[11] = key[7]^a - key[8]^b + key[9]^c - c;
    if( key[9] + 0x33 != 0x32 + 0x33||
        key[10] + 0x22 != 0x4b + 0x22 ||
        key[11] + 0x11 != 0xffffffdc + 0x11 )
        exitAngrman();
    printf("Star ");
    fflush(stdout);
    sleep(1);
}
void Buster(char a, char b, char c){
    key[12] = key[12]^a - key[9]^b + key[6]^c + a;
    key[13] = key[10]^a - key[13]^b + key[7]^c + b;
    key[14] = key[5]^a - key[11]^b + key[14]^c + c;
    if( key[12] + 0x33 != 0xffffffbf + 0x33||
        key[13] + 0x22 != 0x52 + 0x22 ||
        key[14] + 0x11 != 0x4f + 0x11 )
        exitAngrman();
    printf("Buster ");
    fflush(stdout);
    sleep(1);
}

void Stream(){
    int i ;
    printf("Stream!!!!\n");
    for( i = 0 ; i < 29 ; i ++ )
	printf("%c",flag[i]^secret[i%15]);
    printf("\n");
    fflush(stdout);
}

void opening(){
    Ha(secret[0],secret[5],secret[10]);
    Haya(secret[1],secret[6],secret[11]);
    Hayaku(secret[2],secret[7],secret[12]);
    Star(secret[3],secret[8],secret[13]);
    Buster(secret[4],secret[9],secret[14]);
    Stream();
}

void startSAO(){
    opening();
}

void loadRecord(){
    int i;
    read(0,secret,16);
    for( i = 0 ; i < 15 ; i++ )
        if( secret[i] < '0' || secret[i] > '9' )
            exitAngrman();
    opening();
}

int menu(){
    char option[2];
    printf("ANGRMAN X\n");
    printf("1 GAME START\n");
    printf("2 PASS WORD\n");
    printf("3 EXIT GAME\n");
    read(0,&option,2);
    return option[0];
}

int main(){
    int choice = 0;
    choice = menu();
    switch(choice){
        case '1':
            startSAO();
            break;
        case '2':
            loadRecord();
            break;
        case '3':
            exitAngrman();
            break;
    }
    return 0;
}
