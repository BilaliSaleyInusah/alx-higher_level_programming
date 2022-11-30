#!/usr/bin/python3
def uppercase(c):
    str1 = ""
    for i in range(len(c)):
        num = ord(c[i])
        if num >= 97 and num <= 122:
            num = num - 32
        print("{}".format(chr(uni_code)), end='')
    print()
