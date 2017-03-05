#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <signal.h>

uint64_t map = (1ULL<<36)-1;
uint64_t piece[9][9] = {
{4096,2097152,512,134217728,8,0,0,0,0},{16,1024,134217728,1073741824,0,0,0,0,0},{4,16777216,16384,262144,0,0,0,0,0},{67108864,2,268435456,1,0,0,0,0,0},{1,65536,67108864,8192,4194304,0,0,0,0},{256,8388608,8,16777216,4096,0,0,0,0},{2,32,262144,16384,8589934592,0,0,0,0},{2,16384,262144,134217728,0,0,0,0,0},{0,0,0,0,0,0,0,0,0},
};
int p=0;
int num_piece = 9;
char in[4]={0,0,0,0},i=0;

void catflag(){
	system(" echo GJ!");
}

void handler(){
    puts("Time's up!");
    exit(-1);
}

int main(){
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
    signal(SIGALRM, handler);
    alarm(60);
    for( p = 0 ; p < num_piece; p++ ){
	printf("%dth Piece\n",p);
        read(0,in,3);
	if( in[0] < '0' || in[0] > '6' ) return -1;
	if( in[1] < '0' || in[1] > '6' ) return -1;
	if( in[2] != '\n' ) return -1;
        in[0] -= '0';
        in[1] -= '0';
        for( i = 0 ; piece[p][i] != 0 ; i++ ){
            piece[p][i] = piece[p][i]*(1ULL<<in[0])*(1ULL<<(6*in[1]));
            map -= piece[p][i];
        }
    }
    if( map == 0 ){
        catflag();
	return 0;
	}
    else{
        puts("GG");
	return -1;
	}
}

