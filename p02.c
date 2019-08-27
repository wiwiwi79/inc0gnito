#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

void give_shell(){
	system("/bin/sh");

}

void vul(){
	char buf[8];
        while(1){
                read(0,buf,0x1000);
                printf("%s",buf);
		if(buf[0]=='N'){
		break;
}
                
        }	
}

void main(int argc,char *argv[]){

	vul();
}
