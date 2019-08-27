#include <stdio.h>
#include <string.h>
void hacked()
{
 printf("hacked");
 exit(0);
}

unsigned getbuf()
{
 char buf[8];
 gets(buf);
 return 1;
}

int main()
{
 int val;
 val = getbuf();
 printf("0x%x\n",val);
}

