# Question:

# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".



# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.
import zlib

s = "Hello! This is Hellow  .Ram,kadam hellow!"
t=zlib.compress(s)
print(t)
d=zlib.decompress(t)
print(d)