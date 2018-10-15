def int2Text(number, size):
    text = "".join([chr((number >> j) & 0xff)
                    for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

num = 555555555 #The integer to be converted to string
s = 513
print num,s
print int2Text(num,s)
