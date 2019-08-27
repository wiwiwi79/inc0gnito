#include <stdio.h>
#include <stdlib.h>

void mirror() {
  char buf[0x10];

  while(1) {
    read(0, buf, 0x100);
    if (buf[0] == 'q')
      break;
    printf("%s\n", buf);
  }
}

int main() {
  setbuf(stdin, 0);
  setbuf(stdout, 0);

  puts("MIRROR PROGRAM");
  mirror();
  return 0;
}
