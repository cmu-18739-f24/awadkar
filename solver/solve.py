from pwn import *

KEY = b'Hello, world of spaces!'

host = "localhost" # Remote machine name
port = "39227" # Remote port

conn = remote(host, port)

content = conn.recvuntil(b"phrase: ").decode("utf-8")

print(content)

conn.sendline(KEY)

content = conn.recvall().decode("utf-8")

print('Flag = ', content[:35])