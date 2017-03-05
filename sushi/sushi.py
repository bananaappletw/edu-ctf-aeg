#!/usr/bin/python -u
import time
import random
import string
import os
import subprocess
import signal

code1 = """
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
"""

code2 = """
int nobody_love_you()
{
"""
code3 = """
    sleep(1);
    puts("Let's restart your life");
    puts("Guess what sushi looks like now!");
    int pos = 0;
    for(int i = 0;i<20;i++)
    {
        int tmp;
        char tmpchar[5];
        printf("Enter sum of sushi %d and %d",pos,pos+1);
        puts("");
        read(0,tmpchar,4);
        tmp = atoi(tmpchar);
        if(tmp != sushi[pos]+sushi[pos+1])
        {
            puts("Wrong answer, commit suicide");
            exit(1);
        }
        pos = abs(pos + sushi[pos] + sushi[pos+1]) % (strlen(sushi)-1);
    }
    puts("Now rewrite your sushi");
    read(0,sushi,100);
    gets(s);
    return 0;
}
void sushi_is_like_your_life()
{
"""
code4 =  """
    sleep(1);
    puts("You are sushi!");
    for(int i = 0;i<strlen(sushi);i++)
        sushi[i] = (sushi[i] % randint) & 0xff;
}

void holy_shit_you_ruin_everything()
{
"""
code5 =  """
    sleep(1);
    puts("Holy shit, I ruin everything!");
    for(int i = 0;i<strlen(sushi);i++)
        sushi[i] = (sushi[i] * randint) & 0xff;
}

void roll_the_salmon_in_rice()
{
"""
code6 =  """
    sleep(1);
    puts("Roll salmon in rice!");
    for(int i = 0;i<strlen(sushi);i++)
        sushi[i] = (sushi[i]-randint) & 0xff;
}

void how_to_make_sushi()
{
"""
code7 = """
    sleep(1);
    puts("Let's make sushi!");
    for(int i = 0;i<strlen(sushi);i++)
        sushi[i] = (sushi[i]+randint) & 0xff;
}

int main(int argc, char * argv[])
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);
"""
code8 = """

    nobody_love_you();
    return 0;
}
"""

def timeout(signum,frame):
    print("TIMEOUT")
    exit(0)

if __name__ == "__main__":
    sushi = ''.join(random.choice(string.letters) for _ in range(50))
    sushi_len = random.randint(100,150)
    topping = random.randint(0,1000)
    functions = ["how_to_make_sushi();",
    "roll_the_salmon_in_rice();",
    "holy_shit_you_ruin_everything();",
    "sushi_is_like_your_life();"]
    random.shuffle(functions)
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(120)
    os.chdir("/tmp/")

    print("There is a old saying that life is like making sushi")
    print("Try to make a sushi")
    print("I will send you program encoded by base64")
    time.sleep(1)
    filename = time.strftime("%m%d_%H%M%S", time.localtime()) + os.urandom(10).encode('hex') + ".c"
    with open(filename, "wb") as f:
        f.write(code1)
        f.write("char sushi["+str(sushi_len)+"]=\""+sushi+"\";")
        f.write(code2)
        f.write("char s["+str(topping)+"];")
        f.write(code3)
        f.write("int randint="+str(random.randint(1,255))+";")
        f.write(code4)
        f.write("int randint="+str(random.randint(1,255))+";")
        f.write(code5)
        f.write("int randint="+str(random.randint(1,255))+";")
        f.write(code6)
        f.write("int randint="+str(random.randint(1,255))+";")
        f.write(code7)
        for function in functions:
            f.write(function)
        f.write(code8)
        
    os.system("gcc -o ./"+filename[:-2]+" ./"+filename+" -fno-stack-protector -z execstack 2>/dev/null")
    os.system("strip ./"+filename[:-2])
    result = subprocess.check_output("base64 ./"+filename[:-2] , shell=True)
    print(result)
    print("\nNOW MAKE A SUSHI\n")
    os.execv('./'+filename[:-2],[''])
